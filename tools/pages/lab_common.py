"""Helpers for the Computer Engineering and Machine Learning pages."""
import json, random, re, html
from gen_unit import topic, chapter, worked, box, detailed, quiz_section, page, close, eq
from math_common import lab as graph, fn, steps, fr, m, mini, table, q, check, balance

def _j(o): return json.dumps(o, ensure_ascii=False).replace("'", "&#39;")
def xlab(type, **p):
    p["type"] = type
    return f"<div class=\"xlab\" data-lab='{_j(p)}'></div>"

PYKW = set("def return if elif else for in while import from as class None True False and or not lambda with range len print".split())
def code(src, lang="py"):
    src = src.strip("\n"); out = []
    pat = r'(#.*$|;.*$)|("(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\')|(\b\d+(?:\.\d+)?\b)|([A-Za-z_]\w*)|(\s+)|(.)'
    for mm in re.finditer(pat, src, re.M):
        t = mm.group(0)
        if mm.group(1) and (lang == "asm" or t.startswith("#")): out.append(f'<span class="c">{html.escape(t)}</span>')
        elif mm.group(1): out.append(html.escape(t))
        elif mm.group(2): out.append(f'<span class="s">{html.escape(t)}</span>')
        elif mm.group(3): out.append(f'<span class="n">{t}</span>')
        elif mm.group(4) and (t in PYKW or (lang == "asm" and t.isupper() and len(t) > 1)): out.append(f'<span class="k">{t}</span>')
        else: out.append(html.escape(t))
    return f'<pre class="code"><code>{"".join(out)}</code></pre>'

def build(course, slug, level, n, title, h1, intro, desc, chapters, PQ, CHAL, EXQ, FRQS, out, tags, minutes=(30, 25), footer=None):
    check(PQ); check(CHAL); check(EXQ)
    seed = sum(map(ord, slug))
    balance(PQ, seed); balance(CHAL, seed + 1); balance(EXQ, seed + 2)
    cid = slug; ch = list(chapters)
    ch.append(chapter(f"practice-{cid}", "Practice Questions", "Practice", [quiz_section(f"practice-quiz-{cid}", "Practice questions", f"{len(PQ)} questions on everything in this unit. Work each one out before you pick.", f"quiz-{cid}", tags)]))
    ch.append(chapter(f"challenge-{cid}", "Challenge Questions", "Challenge", [quiz_section(f"challenge-quiz-{cid}", "Challenge questions", "Harder, multi-step questions in the style of a college exam.", f"quiz-challenge-{cid}", tags)], hard=True))
    ch.append(chapter(f"exam-ch-{cid}", "Practice Exam", "Practice Exam", [f'<section class="topic" id="exam-box-{cid}"><h2>Practice exam</h2><p class="sub">{len(EXQ)} multiple-choice questions ({minutes[0]} minutes) and {len(FRQS)} free-response questions ({minutes[1]} minutes). No feedback until you submit. Grade the free response with the rubric.</p><div class="exam" data-src="exam-{cid}"></div></section>']))
    EX = {"title": f"{level} Unit {n} Practice Exam: {title}", "mcqMinutes": minutes[0], "frqMinutes": minutes[1], "tags": tags, "mcq": EXQ, "frq": FRQS}
    HTML = page(slug, f"{level} Unit {n}: {title}", f"{level} · Unit {n}", h1, intro, desc, ch,
                {f"quiz-{cid}": PQ, f"quiz-challenge-{cid}": CHAL, f"exam-{cid}": EX},
                course=course, footer=footer or f"Margin · {level} · Click, drag and break things in the labs", extra_js=("wa.js", "math.js", "labs.js"))
    HTML = HTML.replace('<script src="../../assets/js/sims.js"></script>\n', "")
    open(out, "w").write(HTML)
    print(f"{level} unit {n} written:", len(PQ), len(CHAL), len(EXQ), len(FRQS))
