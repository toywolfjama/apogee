"""Helpers for the French 1 course pages."""
import json, html, re, random
from gen_unit import topic, chapter, worked, box, detailed, quiz_section, page

def esc(s): return html.escape(str(s), quote=False)
def F(s, t=None):
    """French text the reader can tap to hear."""
    d = f' data-t="{esc(t)}"' if t else ""
    return f'<span class="fr" lang="fr"{d}>{s}</span>'
def ex(fr, en):
    """Example sentence with English below."""
    return f'<div class="ex">{F(fr)}<span class="en">{en}</span></div>'
def vt(rows, head=("French", "English"), cols=None):
    """Vocabulary table. rows: (fr, en) or (fr, en, note)."""
    n = max(len(r) for r in rows)
    hd = "".join(f"<th>{h}</th>" for h in (head if len(head) >= n else head + ("Notes",)))
    body = "".join("<tr><td>" + F(r[0]) + "</td>" + "".join(f"<td>{c}</td>" for c in r[1:]) + "<td></td>" * (n - len(r)) + "</tr>" for r in rows)
    return f'<div class="tblwrap"><table class="vocab">{"<tr>" + hd + "</tr>"}{body}</table></div>'
def vgrid(rows):
    """Compact vocabulary chips."""
    return '<div class="vgrid">' + "".join(f'<div class="vc">{F(a)}<span>{b}</span></div>' for a, b in rows) + "</div>"
def lab(**p):
    return f"<div class=\"cslab frlab\" data-lab='{json.dumps(p, ensure_ascii=False).replace(chr(39), '&#39;')}'></div>"
def wa(title, frames):
    """Word animation. frames: list of (tokens, note, english). token = 'id|text|cls'."""
    fr = [{"t": t.split("  ") if isinstance(t, str) else t, "note": n, "en": e} for t, n, e in frames]
    return f"<div class=\"wanim\" data-w='{json.dumps({'title': title, 'frames': fr}, ensure_ascii=False).replace(chr(39), '&#39;')}'></div>"
def listen(t, label="▶ Listen"):
    return f'<button type="button" class="listen" data-say="{esc(t)}">{label}</button>'
def q(text, opts, a, x, t="g", k=None):
    d = {"t": t, "q": text, "o": opts, "a": a, "x": x, "h": True}
    if k: d["k"] = k
    return d
def balance(qs, seed):
    rnd = random.Random(seed)
    for it in qs:
        o = it["o"]; right = o[it["a"]]
        if it.get("keep"): continue
        rnd.shuffle(o); it["a"] = o.index(right)
    # spread answer letters: avoid long runs
    return qs
def check(qs):
    for i, it in enumerate(qs):
        assert 0 <= it["a"] < len(it["o"]), i
        assert len(set(it["o"])) == len(it["o"]), ("duplicate option", i, it["o"])
    return qs

TAGS = {"g": "Grammar", "v": "Vocabulary"}
FOOT = "Apogee · French 1 · Tap any French word to hear it"

def build(n, slug, title, h1, intro, desc, chapters, PQ, CHAL, EXQ, FRQS, out):
    check(PQ); check(CHAL); check(EXQ)
    balance(PQ, 100 + n); balance(CHAL, 200 + n); balance(EXQ, 300 + n)
    cid = f"f{n}"
    ch = list(chapters)
    ch.append(chapter(f"practice-{cid}", "Practice Questions", "Practice", [quiz_section(f"practice-quiz-{cid}", "Practice questions", f"{len(PQ)} questions on everything in this unit. Say each answer out loud before you check it.", f"quiz-{cid}", TAGS)]))
    ch.append(chapter(f"challenge-{cid}", "Challenge Questions", "Challenge", [quiz_section(f"challenge-quiz-{cid}", "Challenge questions", "Harder questions that mix several rules at once.", f"quiz-challenge-{cid}", TAGS)], hard=True))
    ch.append(chapter(f"exam-ch-{cid}", "Practice Exam", "Practice Exam", [f'<section class="topic" id="exam-box-{cid}"><h2>Practice exam</h2><p class="sub">{len(EXQ)} multiple-choice questions (25 minutes) and {len(FRQS)} writing tasks (20 minutes). No feedback until you submit. Grade your writing with the rubric.</p><div class="exam" data-src="exam-{cid}"></div></section>']))
    EX = {"title": f"Unit {n} Practice Exam: {title}", "mcqMinutes": 25, "frqMinutes": 20, "tags": TAGS,
          "kinds": {"read": "Reading", "gram": "Grammar", "vocab": "Vocabulary", "listen": "Listening"}, "mcq": EXQ, "frq": FRQS}
    HTML = page(f"unit-{n}", f"French 1 Unit {n}: {title}", f"French 1 · Unit {n}", h1, intro, desc, ch,
                {f"quiz-{cid}": PQ, f"quiz-challenge-{cid}": CHAL, f"exam-{cid}": EX},
                course="french-1", footer=FOOT, extra_js=("fr.js",))
    HTML = HTML.replace('<script src="../../assets/js/sims.js"></script>\n', "")
    open(out, "w").write(HTML)
    print(f"French unit {n} written:", len(PQ), len(CHAL), len(EXQ), len(FRQS))
