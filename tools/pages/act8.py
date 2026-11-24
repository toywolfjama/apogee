from tp_common import *
from acttest_data import EN, MA, QR1, QR2, SC
C = "act"; OUT = "../../courses/act/act-test.html"
TE = {"p": "Punctuation", "u": "Grammar & usage", "s": "Sentence structure", "r": "Strategy & style"}
TM = {"a": "Algebra", "n": "Number", "g": "Geometry", "f": "Functions", "s": "Stats & probability", "t": "Trig", "h": "Higher topics"}
TR = {"m": "Main idea", "d": "Details", "i": "Inference", "w": "Word meaning", "p": "Purpose & structure"}
TS = {"d": "Reading data", "e": "Experiments", "v": "Viewpoints", "g": "Engineering"}
data = {}; chs = []
for cid, title, qs, mins, tags, name, rules, short in [
  ("en", "English (half length)", EN, 18, TE, "English", ["25 questions in 18 minutes, half of the real section.", "Choice A is NO CHANGE when it appears.", "No penalty for guessing."], "English"),
  ("ma", "Math (half length)", MA, 25, TM, "Math", ["22 questions in 25 minutes, about half of the real section.", "Calculator allowed; no formula sheet.", "Four answer choices, like the real ACT."], "Math"),
  ("rd", "Reading (half length)", QR1 + QR2, 20, TR, "Reading", ["2 passages, 18 questions, 20 minutes.", "Hide the passage once you know it.", "No penalty for guessing."], "Reading"),
  ("sc", "Science (optional, half length)", SC, 20, TS, "Science", ["18 questions in 20 minutes.", "No calculator.", "Data first, text second."], "Science")]:
    html, d = exam_box("act-" + cid, title, qs, mins, tags, name, rules, desc=f"{len(qs)} questions · {mins} minutes.")
    data.update(d); chs.append(chapter("ch-" + cid, title, short, [html]))
INTRO = topic("how", "How to use this practice test", f'''
<p>A half-length ACT: every section at real pace, about half the questions. Take it in one sitting (about 85 minutes) with a short break after Math.</p>
{table(["Section", "Here", "Real ACT"], [["English", "25 Q · 18 min", "50 Q · 35 min"], ["Math", "22 Q · 25 min", "45 Q · 50 min"], ["Reading", "18 Q · 20 min", "36 Q · 40 min"], ["Science (optional)", "18 Q · 20 min", "40 Q · 40 min"]])}
{box("tip", "Scoring", "The real 1–36 scale depends on that test's difficulty, so we show percent correct and a skill breakdown instead. Use them to choose which lesson to review.")}
''', pill=("s", "★"))
CH = [chapter("ch-how", "Before You Start", "Start", [INTRO])] + chs
HTML = page("act-test", "ACT: Half-Length Practice Test", "ACT · Practice test", 'Half-length <span class="hl">practice test</span>', "English, Math, Reading and Science at real ACT pace, with explanations and a skill breakdown.", "Free half-length ACT practice test: English, Math, Reading and Science sections with explanations.", CH, data, course=C, footer="Apogee · ACT prep · Not affiliated with ACT", extra_js=("tp.js",))
HTML = HTML.replace('<script src="../../assets/js/sims.js"></script>\n', "")
open(OUT, "w").write(HTML); print("act-test written")
