"""Shared builder for SAT / ACT pages."""
import json, random
from gen_unit import topic, chapter, worked, box, quiz_section, page, close, eq
from math_common import lab, fn, steps, fr, m, mini, table, _j

def q(text, opts, a, x, t="c", k=None):
    d = {"t": t, "q": text, "o": [str(o) for o in opts], "a": a, "x": x}
    if k: d["k"] = k
    return d
def g(text, answers, x, t="c"):
    """grid-in / student-produced response"""
    return {"t": t, "q": text, "g": [str(v) for v in answers], "x": x}
def psg(*paras, src=None):
    if len(paras) > 1 and all(" | " in x for x in paras):
        rows = [x.split(" | ") for x in paras]
        body = '<table class="dt"><tr>' + "".join(f"<th>{c}</th>" for c in rows[0]) + "</tr>" + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows[1:]) + "</table>"
        return f'<div class="passage">{body}</div>'
    body = "".join(f"<p>{p}</p>" for p in paras)
    return f'<div class="passage">{body}{f"<div class=src>{src}</div>" if src else ""}</div>'
def hl(title, items, sub=None):
    d = {"title": title, "items": items}
    if sub: d["sub"] = sub
    return f"<div class=\"tp\" data-hl='{_j(d)}'></div>"
def pace(modules, title=None):
    d = {"modules": modules}
    if title: d["title"] = title
    return f"<div class=\"tp\" data-pace='{_j(d)}'></div>"

def check(qs):
    for i, it in enumerate(qs):
        if "g" in it: assert it["g"], i; continue
        assert 0 <= it["a"] < len(it["o"]), (i, it["q"][:60])
        if any("<" in o for o in it["o"]): it["h"] = 1
        assert len(set(it["o"])) == len(it["o"]), ("dup", i, it["o"])
    return qs
def balance(qs, seed):
    rnd = random.Random(seed)
    for it in qs:
        if "g" in it: continue
        if it.pop("keep", False): continue
        o = it["o"]; right = o[it["a"]]
        if o[0] == "NO CHANGE":
            rest = o[1:]; rnd.shuffle(rest); o[1:] = rest
        else:
            rnd.shuffle(o)
        it["a"] = o.index(right)
    return qs

def exam_box(cid, title, mcq, minutes, tags, name, rules, kind="questions", frq=None, frq_minutes=0, desc=None):
    check(mcq); balance(mcq, sum(map(ord, cid)))
    E = {"title": title, "mcqMinutes": minutes, "frqMinutes": frq_minutes, "tags": tags, "mcq": mcq, "frq": frq or [], "mcqName": name, "mcqKind": kind, "rules": rules}
    html = f'<section class="topic" id="exam-box-{cid}"><h2>{title}</h2><p class="sub">{desc or f"{len(mcq)} questions in {minutes} minutes. No feedback until you submit."}</p><div class="exam" data-src="exam-{cid}"></div></section>'
    return html, {f"exam-{cid}": E}

def build(course, slug, level, n, title, h1, intro, desc, chapters, PQ, CHAL, EX, TAGS, out, minutes=20, rules=None, exam_name="Practice set", frq=None, frq_minutes=0, extra_data=None, js=("wa.js", "math.js", "tp.js")):
    check(PQ); check(CHAL)
    s = sum(map(ord, slug)); balance(PQ, s); balance(CHAL, s + 1)
    cid = slug; ch = list(chapters); data = {f"quiz-{cid}": PQ, f"quiz-challenge-{cid}": CHAL}
    if PQ: ch.append(chapter(f"practice-{cid}", "Practice Questions", "Practice", [quiz_section(f"practice-quiz-{cid}", "Practice questions", f"{len(PQ)} questions with instant explanations. Filter by skill with the buttons.", f"quiz-{cid}", TAGS)]))
    if CHAL: ch.append(chapter(f"challenge-{cid}", "Hard Questions", "Hard", [quiz_section(f"challenge-quiz-{cid}", "Hard questions", "The kind you'll see in the harder second module. Take your time.", f"quiz-challenge-{cid}", TAGS)], hard=True))
    if EX:
        html, d = exam_box(cid, f"{level} {title}: timed set", EX, minutes, TAGS, exam_name, rules or ["No feedback until you submit. Flag questions and come back to them.", "No penalty for wrong answers: never leave one blank."], frq=frq, frq_minutes=frq_minutes)
        ch.append(chapter(f"exam-ch-{cid}", "Timed Set", "Timed set", [html])); data.update(d)
    if extra_data: data.update(extra_data)
    HTML = page(slug, f"{level}: {title}", f"{level} · {'Part ' + str(n) if n else 'Tactics'}", h1, intro, desc, ch, data,
                course=course, footer=f"Apogee · {level} prep · Not affiliated with College Board or ACT", extra_js=js)
    HTML = HTML.replace('<script src="../../assets/js/sims.js"></script>\n', "")
    open(out, "w").write(HTML)
    print(f"{slug}: {len(PQ)} practice, {len(CHAL)} hard, {len(EX or [])} timed")

def dz(t, copy=None):
    c = f' data-copy="{copy}"' if copy else ""
    return f'<code class="dz"{c}>{t}</code>'
def tactic(n, title, when, types, body=""):
    ty = ('<div class="type"><b>Type:</b>' + " ".join(dz(t) for t in types) + "</div>") if types else ""
    return f'<div class="tactic"><h4><span class="tn">{n}</span>{title}</h4><p class="when">{when}</p>{ty}{body}</div>'
def reg(points, model="lin", title=None, sub=None, presets=None):
    d = {"points": points, "model": model}
    if title: d["title"] = title
    if sub: d["sub"] = sub
    if presets: d["presets"] = presets
    return f"<div class=\"tp\" data-reg='{_j(d)}'></div>"
EMBED = '<div class="dz-embed"></div>'
