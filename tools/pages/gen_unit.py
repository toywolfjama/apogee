"""Shared helpers to build unit pages in the same structure as unit-3.html."""
import json, random, math

def close(a, b, tol=0.01):
    assert abs(a - b) <= tol * max(1, abs(b)), (a, b)

def sim(spec, caption=None, reveal=True):
    d = dict(spec)
    if reveal: d["reveal"] = True
    if caption: d["caption"] = caption
    return "<div class=\"sim\" data-sim='" + json.dumps(d, ensure_ascii=False).replace("'", "&#39;") + "'></div>"

def worked(q, a):
    return f'<div class="worked"><div class="q">Worked example: {q}</div><div class="a">{a}</div></div>'

def box(kind, label, text):
    return f'<div class="box {kind}"><b class="lbl">{label}</b>{text}</div>'

def eq(s):
    return f'<div class="big-eq">{s}</div>'

def detailed(title, html):
    return f'<details class="deep"><summary><span class="tag">Detailed explanation</span>{title}</summary><div class="deep-body">{html}</div></details>'

def topic(tid, title, body, pill=None, sub=None, det=None):
    p = f'<span class="pill {pill[0]}">{pill[1]}</span>' if pill else ""
    s = f'<p class="sub">{sub}</p>' if sub else ""
    d = detailed(*det) if det else ""
    return f'<section class="topic" id="{tid}">\n  <h2>{p}{title}</h2>\n  {s}\n  {body}\n  {d}\n</section>'

def quiz_section(tid, title, sub, src, tags=None):
    t = f" data-tags='{json.dumps(tags)}'" if tags else ""
    return f'<section class="topic" id="{tid}">\n  <h2>{title}</h2>\n  <p class="sub">{sub}</p>\n  <div class="quiz" data-src="{src}"{t}></div>\n</section>'

def chapter(cid, title, short, sections, hard=False):
    h = ' data-hard="1"' if hard else ""
    return f'<div class="chapter" id="{cid}" data-title="{title}" data-short="{short}"{h}>\n' + "\n".join(sections) + "\n</div>"

def shuffle(qs, seed):
    rng = random.Random(seed)
    for q in qs:
        c = q["o"][q["a"]]; o = q["o"][:]; rng.shuffle(o); q["o"] = o; q["a"] = o.index(c)
    return qs

def dump(o):
    return json.dumps(o, ensure_ascii=False, indent=1).replace("</", "<\\/")

def page(unit_id, title_tag, kicker, h1, intro, desc, chapters, data_blocks, course="ap-physics-1", footer="Margin · AP Physics 1 · g = 10 m/s²", extra_js=()):
    scripts = "\n".join(f'<script type="application/json" id="{k}">\n{dump(v)}\n</script>' for k, v in data_blocks.items())
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title_tag} | Margin</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=JetBrains+Mono:wght@400;500;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="icon" href="../../assets/img/logo.svg" type="image/svg+xml">
<link rel="stylesheet" href="../../assets/css/site.css">
</head>
<body class="{ {"ap-csa": "th-term", "french-1": "th-paris", "ap-precalc": "th-grid", "pre-precalc": "th-grid", "math": "th-grid", "sat": "th-grid th-exam", "act": "th-grid th-exam th-act"}.get(course, "th-space") }" data-root="../../" data-course="{course}" data-unit="{unit_id}">

<div class="hero">
  <span class="kicker">{kicker}</span>
  <h1>{h1}</h1>
  <p>{intro}</p>
</div>

<main class="page">
{chr(10).join(chapters)}
</main>

<footer>{footer}</footer>

{scripts}
<script src="../../assets/js/courses.js"></script>
<script src="../../assets/js/sims.js"></script>
{"".join(f'<script src="../../assets/js/{j}"></script>{chr(10)}' for j in extra_js)}<script src="../../assets/js/site.js"></script>
<script src="../../assets/js/exam.js"></script>
</body>
</html>
'''

def calc_section(prog, unit_label, sections_list):
    items = "".join(f"<li>{x}</li>" for x in sections_list)
    return f'''<section class="topic" id="calculator">
  <h2>TI-84 calculator program</h2>
  <p class="sub">A notes and solver program for the TI-84 Plus CE covering {unit_label}.</p>
  <p><a class="navbtn solid" href="../../downloads/{prog}.8xp" download>Download {prog}.8xp</a> &nbsp; <a class="navbtn" href="../../calculator.html">Install steps and all programs</a></p>
  <ul>{items}</ul>
  <p>Pick <b>FIND WHAT?</b>, choose what the question asks for, choose the situation, then type the numbers it asks for. After each answer it shows the full work and answer, which you can scroll with the arrow keys.</p>
  {box("plain", "Check first", "Ask your teacher before using calculator programs on a test.")}
</section>'''
