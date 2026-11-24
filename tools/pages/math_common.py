"""Helpers for the math course pages (Before Precalc + AP Precalculus)."""
import json, random, math
from gen_unit import topic, chapter, worked, box, detailed, quiz_section, page, close, eq

def _j(o): return json.dumps(o, ensure_ascii=False).replace("'", "&#39;")
def lab(**p):
    """Interactive graph. type='graph' (default) or 'circle'."""
    p.setdefault("type", "graph")
    return f"<div class=\"mlab\" data-lab='{_j(p)}'></div>"
def fn(e, label=None, name=None, c=None, dash=False, dom=None):
    d = {"e": e}
    if label: d["label"] = label
    if name: d["name"] = name
    if c: d["c"] = c
    if dash: d["dash"] = True
    if dom: d["dom"] = dom
    return d
def steps(title, frames):
    """Step animation. frames: list of (tokens, note). tokens: 'id|text|cls' separated by two spaces."""
    fr = [{"t": t.split("  ") if isinstance(t, str) else t, "note": n} for t, n in frames]
    return f"<div class=\"msteps\" data-w='{_j({'title': title, 'frames': fr})}'></div>"
def fr(a, b): return f'<span class="frac"><span>{a}</span><span>{b}</span></span>'
def m(s): return f'<span class="mx">{s}</span>'
def mini(*cards):
    return '<div class="grid2">' + "".join(f'<div class="mini"><h4>{h}</h4>{b}</div>' for h, b in cards) + "</div>"
def table(head, rows):
    return '<div class="tblwrap"><table><tr>' + "".join(f"<th>{h}</th>" for h in head) + "</tr>" + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</table></div>"
def q(text, opts, a, x, t="c", k=None):
    d = {"t": t, "q": text, "o": [str(o) for o in opts], "a": a, "x": x}
    if k: d["k"] = k
    return d
def check(qs):
    for i, it in enumerate(qs):
        assert 0 <= it["a"] < len(it["o"]), i
        assert len(set(it["o"])) == len(it["o"]), ("duplicate option", i, it["o"])
    return qs
def balance(qs, seed):
    rnd = random.Random(seed)
    for it in qs:
        o = it["o"]; right = o[it["a"]]
        if it.get("keep"): it.pop("keep"); continue
        rnd.shuffle(o); it["a"] = o.index(right)
    return qs

TAGS = {"c": "Concept", "p": "Procedure", "g": "Graphs", "w": "Word problem"}
COURSE = "math"

def build(slug, level, n, title, h1, intro, desc, chapters, PQ, CHAL, EXQ, FRQS, out, minutes=(30, 25), calc_note=""):
    check(PQ); check(CHAL); check(EXQ)
    seed = hash(slug) % 1000
    balance(PQ, seed); balance(CHAL, seed + 1); balance(EXQ, seed + 2)
    cid = slug
    ch = list(chapters)
    ch.append(chapter(f"practice-{cid}", "Practice Questions", "Practice", [quiz_section(f"practice-quiz-{cid}", "Practice questions", f"{len(PQ)} questions on everything in this unit. Work each one on paper before you pick.", f"quiz-{cid}", TAGS)]))
    ch.append(chapter(f"challenge-{cid}", "Challenge Questions", "Challenge", [quiz_section(f"challenge-quiz-{cid}", "Challenge questions", "Harder, multi-step questions in the style of the toughest exam items.", f"quiz-challenge-{cid}", TAGS)], hard=True))
    ch.append(chapter(f"exam-ch-{cid}", "Practice Exam", "Practice Exam", [f'<section class="topic" id="exam-box-{cid}"><h2>Practice exam</h2><p class="sub">{len(EXQ)} multiple-choice questions ({minutes[0]} minutes) and {len(FRQS)} free-response questions ({minutes[1]} minutes). No feedback until you submit. {calc_note}Grade the free response with the rubric.</p><div class="exam" data-src="exam-{cid}"></div></section>']))
    EX = {"title": f"{level} Unit {n} Practice Exam: {title}", "mcqMinutes": minutes[0], "frqMinutes": minutes[1], "tags": TAGS, "mcq": EXQ, "frq": FRQS}
    HTML = page(slug, f"{level} Unit {n}: {title}", f"{level} · Unit {n}", h1, intro, desc, ch,
                {f"quiz-{cid}": PQ, f"quiz-challenge-{cid}": CHAL, f"exam-{cid}": EX},
                course=COURSE, footer=f"Apogee · {level} · Drag the sliders, then check yourself", extra_js=("wa.js", "math.js"))
    HTML = HTML.replace('<script src="../../assets/js/sims.js"></script>\n', "")
    open(out, "w").write(HTML)
    print(f"{level} unit {n} written:", len(PQ), len(CHAL), len(EXQ), len(FRQS))
