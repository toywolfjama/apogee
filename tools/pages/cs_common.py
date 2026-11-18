"""Helpers for the AP Computer Science A pages: code blocks, labs, traces and a Java checker
that compiles and runs every code question so the marked answer matches real Java output."""
import html, json, os, re, subprocess, tempfile, shutil
from concurrent.futures import ThreadPoolExecutor

KW = set("int double boolean char long String if else while for return new public private protected class static void final this null true false break continue".split())

def esc(s): return html.escape(str(s), quote=False)

def hl(src):
    out = []
    for m in re.finditer(r'(//.*$)|("(?:[^"\\]|\\.)*")|(\'(?:[^\'\\]|\\.)\')|(\b\d+(?:\.\d+)?\b)|([A-Za-z_]\w*)|(\s+)|(.)', src, re.M):
        t = m.group(0)
        if m.group(1): out.append(f'<span class="c">{esc(t)}</span>')
        elif m.group(2) or m.group(3): out.append(f'<span class="s">{esc(t)}</span>')
        elif m.group(4): out.append(f'<span class="n">{t}</span>')
        elif m.group(5) and t in KW: out.append(f'<span class="k">{t}</span>')
        elif m.group(5) and t[0].isupper(): out.append(f'<span class="t">{t}</span>')
        else: out.append(esc(t))
    return "".join(out)

def code(src):
    src = src.strip("\n")
    return f'<pre class="code"><code>{hl(src)}</code></pre>'

def ic(s): return f'<code>{esc(s)}</code>'

def outbox(s): return f'<div class="out-box">{esc(s)}</div>'

def lab(**p):
    return f"<div class=\"cslab\" data-lab='{json.dumps(p).replace(chr(39), '&#39;')}'></div>"

def anim(spec, caption=None, reveal=True):
    sp = dict(spec)
    if caption: sp["caption"] = caption
    if reveal: sp["reveal"] = True
    return f"<div class=\"sim\" data-sim='{json.dumps(sp).replace(chr(39), '&#39;')}'></div>"

class Tr:
    """Build a trace: t = Tr(code_lines); t.s(line, var=value, ...); t.p("printed"); spec = t.spec()"""
    def __init__(self, code, title=None):
        self.code = [l for l in code.strip("\n").split("\n")] if isinstance(code, str) else code
        self.vars = {}; self.out = ""; self.steps = []; self.title = title
    def s(self, line, out=None, **kv):
        for k, v in kv.items():
            if isinstance(v, bool): v = "true" if v else "false"
            elif isinstance(v, float): v = repr(v)
            elif isinstance(v, str) and not v.startswith("@"): v = f'"{v}"'
            self.vars[k] = v
        if out is not None: self.out += out
        self.steps.append([line, dict(self.vars), self.out])
        return self
    def drop(self, *names):
        for n in names: self.vars.pop(n, None)
    def spec(self, ask=None, title=None):
        d = {"type": "trace", "code": self.code, "steps": self.steps}
        if ask: d["ask"] = ask
        if title or self.title: d["title"] = title or self.title
        return d

def q(text, opts, a, x, t="e", run=None, cls=None, exp=None, err=None, sim=None, k=None, pre=None):
    """One question. opts are HTML (already escaped where needed). run = Java statements for main();
    cls = extra top-level classes; pre = extra static members for the test class; exp = expected output override."""
    d = {"t": t, "q": text, "o": opts, "a": a, "x": x, "h": True}
    if sim: d["sim"] = sim
    if k: d["k"] = k
    if run is not None or err: d["_run"] = {"run": run or "", "cls": cls or "", "pre": pre or "", "exp": exp, "err": err}
    return d

def plain(h):
    return html.unescape(re.sub(r"<[^>]+>", "", h))

def norm(s): return re.sub(r"\s+", " ", s.replace("\r", "")).strip()

_checks = []
def jcheck(run, expected, cls="", pre="", label="example"):
    """Register a stand-alone check for worked examples."""
    _checks.append({"label": label, "run": run, "cls": cls, "pre": pre, "exp": expected, "err": None})

def verify(groups):
    """groups: {name: [questions]} plus any jcheck() examples. Compiles and runs each in its own folder."""
    jobs = []
    for g, qs in groups.items():
        for i, it in enumerate(qs):
            r = it.get("_run")
            if not r: continue
            exp = r["exp"] if r["exp"] is not None else plain(it["o"][it["a"]])
            jobs.append((f"{g}#{i+1}", r["run"], r["cls"], r["pre"], exp, r["err"], plain(it["q"])[:70]))
    for n, c in enumerate(_checks):
        jobs.append((f'{c["label"]}{n}', c["run"], c["cls"], c["pre"], c["exp"], None, ""))
    root = tempfile.mkdtemp(prefix="jq")
    def one(j):
        name, run, cls, pre, exp, err, qt = j
        d = os.path.join(root, re.sub(r"\W", "_", name)); os.makedirs(d)
        src = f"import java.util.*;\n{cls}\npublic class Main {{\n{pre}\npublic static void main(String[] args) {{\n{run}\n}}\n}}\n"
        open(os.path.join(d, "Main.java"), "w").write(src)
        env = dict(os.environ); env.pop("JAVA_TOOL_OPTIONS", None)
        c = subprocess.run(["javac", "-nowarn", "Main.java"], cwd=d, capture_output=True, text=True, env=env)
        if err == "compile":
            return None if c.returncode else f"{name}: expected a compile error but it compiled | {qt}"
        if c.returncode:
            return f"{name}: COMPILE ERROR {c.stderr.strip()[:300]} | {qt}"
        r = subprocess.run(["java", "-cp", ".", "Main"], cwd=d, capture_output=True, text=True, timeout=20, env=env)
        if err == "runtime":
            return None if r.returncode else f"{name}: expected a runtime error, got output {r.stdout!r} | {qt}"
        if r.returncode:
            return f"{name}: RUNTIME ERROR {r.stderr.strip()[:200]} | {qt}"
        if norm(r.stdout) != norm(exp):
            return f"{name}: output {r.stdout.strip()!r} but answer says {exp!r} | {qt}"
        return None
    with ThreadPoolExecutor(8) as ex:
        res = list(ex.map(one, jobs))
    shutil.rmtree(root, ignore_errors=True)
    bad = [r for r in res if r]
    print(f"java checks: {len(jobs)} run, {len(bad)} problems")
    for b in bad: print("  ", b)
    _checks.clear()
    return not bad

def strip_private(qs):
    return [{k: v for k, v in it.items() if not k.startswith("_")} for it in qs]

def balance(qs, seed):
    """Shuffle options (keeping the right answer) so answer letters are spread out. Keeps 'All/None of the above' last."""
    import random
    rnd = random.Random(seed)
    for it in qs:
        o = it["o"]; right = o[it["a"]]
        fixed = [x for x in o if re.match(r"^(I|II|III|I and II|I and III|II and III|I, II,? and III|None of|All of|Nothing)", plain(x))]
        if fixed or it.get("keep"): continue
        rnd.shuffle(o); it["a"] = o.index(right)
    return qs
