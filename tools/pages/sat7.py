from tp_common import *
from sattest_rw import RW1, RW2
from sattest_math import M1, M2
C = "sat"; OUT = "../../courses/sat/sat-test.html"
RT = {"v": "Words in context", "s": "Structure & purpose", "x": "Cross-text", "i": "Main idea", "e": "Evidence", "n": "Inference", "b": "Boundaries", "f": "Form & structure", "t": "Transitions", "r": "Rhetorical synthesis"}
MT = {"a": "Algebra", "m": "Advanced Math", "p": "Data & problem solving", "g": "Geometry & trig"}
RULES_RW = ["27 questions in 32 minutes, like one real module.", "Questions are grouped by type, just like the real test.", "No penalty for guessing: answer everything. Flag and come back."]
RULES_M = ["22 questions in 35 minutes, like one real module.", "A calculator is allowed on every question (use Desmos at desmos.com/calculator).", "Grid-ins: type a number or fraction like 7/2. No mixed numbers."]
data = {}; secs = []
for cid, title, qs, mins, tags, name, rules in [("rw1", "Reading and Writing · Module 1", RW1, 32, RT, "Reading and Writing", RULES_RW), ("rw2", "Reading and Writing · Module 2 (harder)", RW2, 32, RT, "Reading and Writing", RULES_RW), ("m1", "Math · Module 1", M1, 35, MT, "Math", RULES_M), ("m2", "Math · Module 2 (harder)", M2, 35, MT, "Math", RULES_M)]:
    html, d = exam_box("sat-" + cid, title, qs, mins, tags, name, rules, desc=f"{len(qs)} questions · {mins} minutes. Treat it like test day: one sitting, no notes.")
    secs.append((cid, title, html)); data.update(d)
INTRO = topic("how", "How to use this practice test", f'''
<p>This is a full-length SAT: four modules, 98 questions, written in the style of the real test. Module 2 of each section is the harder version, the one you'll see if Module 1 goes well.</p>
<ol class="steps"><li>Set aside about 2 hours 20 minutes. Take a 10-minute break between Reading and Writing and Math.</li>
<li>Do the modules in order. Don't look things up.</li>
<li>Afterward, review <b>every</b> question you missed or guessed on. Each review shows a skill breakdown so you know which lesson page to revisit.</li>
<li>Then take an official full-length test in the Bluebook app for a real scaled score.</li></ol>
{box("tip", "Why no score conversion?", "The real SAT scales scores using question difficulty data we don't have, so any 400–1600 number here would be a guess. Use the percent correct and skill breakdown instead.")}
''', pill=("s", "★"))
CH = [chapter("ch-how", "Before You Start", "Start", [INTRO])] + [chapter("ch-" + c, t, t.split(" · ")[0].replace("Reading and Writing", "R&W") + " " + t.split(" · ")[1].split(" ")[1], [h]) for c, t, h in secs]
HTML = page("sat-test", "SAT: Full-Length Practice Test", "SAT · Practice test", 'Full-length <span class="hl">practice test</span>', "Four timed modules, 98 original questions, a skill breakdown after each one.", "Free full-length SAT practice test: two Reading and Writing modules and two Math modules with grid-ins and explanations.", CH, data, course=C, footer="Crux · SAT prep · Not affiliated with College Board", extra_js=("tp.js",))
HTML = HTML.replace('<script src="../../assets/js/sims.js"></script>\n', "")
open(OUT, "w").write(HTML); print("sat-test written", len(RW1), len(RW2), len(M1), len(M2))
