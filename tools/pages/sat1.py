from tp_common import *
C = "sat"; L = "SAT"; OUT = "../../courses/sat/sat-1.html"
TAGS = {"s": "Strategy", "r": "Reading", "w": "Writing", "m": "Math"}

FORMAT = topic("format", "How the SAT works", f'''
<p>The SAT is taken on a laptop or tablet in the Bluebook app. It has two sections, each split into two timed <b>modules</b>.</p>
{table(["Section", "Module", "Questions", "Time", "≈ per question"], [
 ["Reading and Writing", "Module 1", "27", "32 min", "71 s"], ["", "Module 2", "27", "32 min", "71 s"],
 ["10-minute break", "", "", "", ""],
 ["Math", "Module 1", "22", "35 min", "95 s"], ["", "Module 2", "22", "35 min", "95 s"],
 ["<b>Total</b>", "", "<b>98</b>", "<b>2 h 14 min</b>", ""]])}
{mini(("Adaptive modules", "Module 1 is a mix of easy, medium and hard questions. How you do there decides whether Module 2 is the harder or the easier version. Only the harder Module 2 can lead to top scores, so <b>Module 1 accuracy matters a lot</b>."),
      ("Scoring", "Each section is scored 200–800; the total is 400–1600. A few questions in each module are unscored pretest items, but you can't tell which, so treat every question as real."),
      ("No guessing penalty", "A wrong answer costs the same as a blank. <b>Never leave anything blank.</b>"),
      ("Calculator", "A graphing calculator (Desmos) is built into the app for the <b>whole</b> Math section, and you can bring an approved one. A reference sheet of geometry formulas is built in too."))}
<p>Inside a module you can skip around, flag questions, and cross out choices. Once a module's time is up you can't go back to it.</p>
''', pill=("s", "1.1"))

QTYPES = topic("qtypes", "What's on it", f'''
{table(["Reading and Writing domain", "≈ share", "What it asks"], [
 ["Information and Ideas", "26%", "central idea, evidence from text or a graph, logical inference"],
 ["Craft and Structure", "28%", "word in context, purpose and structure, connecting two texts"],
 ["Expression of Ideas", "20%", "transitions, combining notes to meet a goal"],
 ["Standard English Conventions", "26%", "punctuation, sentence boundaries, agreement, verb forms"]])}
<p>Every Reading and Writing question has its own short passage (25–150 words) and one question. Questions come grouped by type, in roughly that order.</p>
{table(["Math domain", "≈ share", "What it covers"], [
 ["Algebra", "35%", "linear equations, functions, systems, inequalities"],
 ["Advanced Math", "35%", "quadratics, exponentials, polynomials, equivalent expressions, functions"],
 ["Problem-Solving and Data Analysis", "15%", "ratios, rates, percents, units, statistics, probability"],
 ["Geometry and Trigonometry", "15%", "area, volume, angles, triangles, right-triangle trig, circles"]])}
<p>About 75% of Math questions are multiple choice. The rest are <b>student-produced responses</b> (grid-ins): you type the answer.</p>
{box("tip", "Grid-in rules", "Positive answers can be up to 5 characters (6 for negative, counting the minus sign). Use a fraction or a decimal, not a mixed number: 3½ must be entered as 7/2 or 3.5. If a decimal runs long, fill all the spaces: 2/3 can be 2/3, .6666, .6667, 0.666 or 0.667. If there's more than one right answer, enter just one.")}
''', pill=("c", "1.2"))

STRAT = topic("strategy", "Strategy that actually raises scores", f'''
{pace([["Reading & Writing module", 27, 32, "Grammar questions should take 30–45 s; spend the extra on hard reading ones."], ["Math module", 22, 35, "Early questions are usually faster. Save time for the last few, which tend to be harder."]], "Pacing clock")}
<ol class="steps">
<li><b>Read the question first</b> on Reading and Writing, then the passage. You'll know what to look for.</li>
<li><b>Predict before you peek.</b> Say the answer in your own words, then find the choice that matches. Trap answers are built to sound good.</li>
<li><b>Eliminate.</b> Cross out every choice with one wrong word. On hard questions you often find the right answer by being sure the other three are wrong.</li>
<li><b>Two-pass each module.</b> If a question takes more than about 2 minutes, flag it, guess, and move on. Come back at the end.</li>
<li><b>Use Desmos aggressively.</b> Graph both sides of an equation and read the intersection; type a system in and click the crossing point.</li>
<li><b>Plug in numbers</b> when answer choices have variables: pick x = 2, compute, and test each choice.</li>
<li><b>Backsolve</b> when choices are numbers: start with a middle value and check it in the problem.</li>
</ol>
{steps("Desmos shortcut: solve 2x² − 3x − 9 = 0", [
 ("a|2x² − 3x − 9 = 0|e", "Instead of factoring, type the left side into Desmos as y = 2x² − 3x − 9."),
 ("b|y = 2x² − 3x − 9|s", "Look where the graph crosses the x-axis."),
 ("c|x = −1.5|g  d|x = 3|g", "Click the gray points: the solutions are −1.5 and 3. Takes 10 seconds."),
])}
''', pill=("s", "1.3"))

PLAN = topic("plan", "A study plan", f'''
{table(["When", "Do this"], [
 ["8+ weeks out", "Take a full practice test in Bluebook to get a baseline. Note which domains cost you the most points."],
 ["Weeks 1–4", "One lesson page here per few days. Do every practice and hard question; reread explanations for the ones you missed."],
 ["Weeks 5–6", "Timed sets. Practice pacing with the clock above. Keep an error log: question, why you missed it, the rule."],
 ["Weeks 7–8", "Two more full practice tests in Bluebook under real timing. Review every miss."],
 ["Test week", "Light review of your error log. Sleep. Charge your device and install Bluebook updates the day before."]])}
{box("tip", "Error log beats volume", "Doing 50 questions and learning from the 10 you missed beats doing 200 and moving on. Write down the rule each miss teaches you.")}
''', pill=("s", "1.4"))

CH = [chapter("ch-format", "The Format", "Format", [FORMAT, QTYPES]), chapter("ch-strat", "Strategy", "Strategy", [STRAT, PLAN])]

PQ = [
 q("How many questions are in one Reading and Writing module?", ["27", "22", "54", "25"], 0, "27 questions in 32 minutes. There are two such modules (54 total).", "s"),
 q("What decides the difficulty of Module 2?", ["Your performance on Module 1", "Your grade level", "The section you start with", "It's random"], 0, "The test is adaptive by module.", "s"),
 q("You have 3 minutes left and 6 unanswered questions. Best move?", ["Answer all 6, guessing on any you can't finish", "Answer 2 carefully and leave 4 blank", "Leave them blank to avoid penalties", "Go back and recheck earlier answers"], 0, "There's no penalty for wrong answers, so a guess can only help.", "s"),
 q("Which is a valid grid-in entry for 3½?", ["7/2", "3 1/2", "3½", "31/2"], 0, "Mixed numbers aren't allowed; 3 1/2 would read as 31/2.", "s"),
 q("Can you use a calculator on every SAT Math question?", ["Yes", "Only in Module 2", "Only on grid-ins", "No"], 0, "A graphing calculator is built in for the whole Math section.", "s"),
 q("Which choice completes the text so that it conforms to the conventions of Standard English?<div class=passage><p>The octopus can change the color of its skin in less than a <span class=blank></span> special cells called chromatophores make this possible.</p></div>", ["second;", "second,", "second", "second, that"], 0, "Both sides are complete sentences, so they need a semicolon (or a period). A comma alone makes a comma splice; nothing at all makes a run-on.", "w"),
 q("If 3x + 5 = 20, what is 6x + 10?", ["40", "30", "15", "45"], 0, "6x + 10 = 2(3x + 5) = 2 · 20 = 40. No need to solve for x.", "m"),
 q("A shirt costs $40. It's on sale for 25% off. What is the sale price?", ["$30", "$10", "$35", "$15"], 0, "40 × 0.75 = 30.", "m"),
 q("<div class=passage><p>Engineers at a coastal city tested two seawall designs. The curved wall reflected waves back toward the ocean, while the stepped wall broke waves into smaller pieces. Over one stormy winter, the area behind the stepped wall flooded less often.</p></div>Which choice best states the main idea of the text?", ["In one winter test, a stepped seawall protected the area behind it better than a curved one.", "Curved seawalls are useless against storms.", "Engineers prefer to build seawalls in winter.", "Waves are made of smaller pieces of water."], 0, "That's exactly what the text reports. B overstates; C and D aren't the point.", "r"),
 q("Which choice completes the text with the most logical transition?<div class=passage><p>Honeybees communicate the location of food through a \"waggle dance.\" <span class=blank></span> bumblebees, which don't dance, rely mostly on scent left at the nest.</p></div>", ["By contrast,", "Similarly,", "For example,", "As a result,"], 0, "Bumblebees do it differently: a contrast.", "w"),
 q("What is the best first step on a hard Reading and Writing question?", ["Read the question so you know what to look for", "Read every answer choice first", "Skip it without reading", "Pick the longest answer"], 0, "Knowing the task first makes reading faster.", "s"),
 g("If x/4 = 3, what is the value of x?", ["12"], "Multiply both sides by 4.", "m"),
 q("When a Math question's answer choices are expressions in x, a fast strategy is to…", ["plug in a simple value for x and test each choice", "always factor first", "pick the choice with the most terms", "skip it"], 0, "Plugging in turns algebra into arithmetic.", "s"),
 q("A word in context question asks for the word that is \"most logical and precise.\" Your best approach is to…", ["predict a word from context, then match it", "pick the hardest vocabulary word", "pick the word you've seen most", "choose based on sound"], 0, "Context first; vocabulary second.", "s"),
]
CHAL = [
 g("The function f is defined by f(x) = 2x² − 8. For what positive value of x does f(x) = 0?", ["2"], "2x² = 8 → x² = 4 → x = 2 (positive).", "m"),
 q("<div class=passage><p>Many people assume that tomatoes have always been a staple of Italian cooking. In fact, tomatoes arrived in Europe from the Americas only in the 1500s, and for nearly two centuries many Europeans grew them as decorative plants, suspicious that the fruit was poisonous.</p></div>Which choice best describes the function of the underlined sentence (\"In fact…\") in the text as a whole?", ["It challenges a common assumption with historical evidence.", "It explains how tomatoes are grown.", "It argues tomatoes are poisonous.", "It describes modern Italian recipes."], 0, "\"Many people assume\" + \"In fact\" = set up and knock down an assumption.", "r"),
 q("A test-taker finishes Module 1 of Math with 6 minutes left. What is the best use of the time?", ["Revisit flagged questions and double-check any grid-in arithmetic", "Submit immediately to save energy", "Change answers at random", "Start Module 2 early"], 0, "Module 1 accuracy sets your Module 2 level; use every second.", "s"),
 q("Which choice completes the text so that it conforms to the conventions of Standard English?<div class=passage><p>The novelist's first book, a collection of short stories set in rural <span class=blank></span> won several regional awards.</p></div>", ["Ohio,", "Ohio", "Ohio;", "Ohio:"], 0, "The phrase \"a collection … Ohio\" is set off by commas on both sides.", "w"),
 q("A store raises a $50 price by 20%, then lowers the new price by 20%. Final price?", ["$48", "$50", "$52", "$40"], 0, "50 × 1.2 × 0.8 = 48. Percent changes don't cancel.", "m"),
 g("A line passes through (0, 3) and (2, 7). What is its slope?", ["2"], "(7 − 3)/(2 − 0) = 2.", "m"),
]
EX = [
 q("How long is the Math section in total?", ["70 minutes", "64 minutes", "60 minutes", "80 minutes"], 0, "Two 35-minute modules.", "s"),
 q("If 2a = 10, what is 4a − 1?", ["19", "20", "9", "21"], 0, "4a = 20.", "m"),
 q("Which choice completes the text with the most logical transition?<div class=passage><p>The trail is only two miles long. <span class=blank></span> it climbs nearly 1,500 feet, so most hikers need two hours.</p></div>", ["However,", "Therefore,", "In addition,", "For instance,"], 0, "Short trail, but slow: contrast.", "w"),
 q("Which choice completes the text so that it conforms to the conventions of Standard English?<div class=passage><p>Each of the paintings in the gallery <span class=blank></span> a small card describing its history.</p></div>", ["has", "have", "are having", "were having"], 0, "\"Each\" is singular.", "w"),
 g("What is 15% of 80?", ["12"], "0.15 × 80.", "m"),
 q("<div class=passage><p>Researchers found that students who explained a concept aloud to a partner remembered it better a week later than students who reread their notes for the same amount of time.</p></div>Which finding, if true, would most directly support the researchers' conclusion that explaining improves memory?", ["In a second study, students who explained a topic outscored rereaders on a delayed test.", "Students preferred rereading.", "Some partners were friends.", "The study took place in spring."], 0, "Only A gives more evidence for the effect.", "r"),
 q("You can't decide between two choices on a hard question. Best move?", ["Pick one, flag it, and move on", "Spend as long as needed", "Leave it blank", "Pick a third choice"], 0, "Protect your time; revisit if you can.", "s"),
 q("Solve: x² = 49 and x < 0.", ["−7", "7", "−49", "±7"], 0, "Negative root only.", "m"),
 q("A recipe uses 3 cups of flour for 12 cookies. How much flour for 20 cookies?", ["5 cups", "4 cups", "6 cups", "7.5 cups"], 0, "0.25 cup per cookie × 20.", "m"),
 q("Which describes the SAT total score range?", ["400–1600", "200–800", "1–36", "0–1600"], 0, "Two sections of 200–800.", "s"),
]
build(C, "sat-1", L, 1, "Format and Strategy", 'The SAT, <span class="hl">decoded</span>', "How the digital SAT is built, how scoring works, and the strategies that save the most points.", "SAT format, scoring, adaptive modules, grid-in rules, pacing and a study plan, with practice questions.", CH, PQ, CHAL, EX, TAGS, OUT, minutes=12)
