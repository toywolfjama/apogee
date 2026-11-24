from tp_common import *
C = "act"; L = "ACT"; OUT = "../../courses/act/act-1.html"
TAGS = {"s": "Strategy", "e": "English", "m": "Math", "r": "Reading", "c": "Science"}

FORMAT = topic("format", "How the ACT works", f'''
<p>The current (enhanced) ACT can be taken online or on paper. You pick whether to add Science and Writing when you register.</p>
{table(["Section", "Questions", "Time", "≈ per question", "In the Composite?"], [
 ["English", "50", "35 min", "42 s", "Yes"], ["Math", "45", "50 min", "67 s", "Yes"], ["Reading", "36", "40 min", "67 s", "Yes"],
 ["Science (optional)", "40", "40 min", "60 s", "No: reported separately, plus a STEM score"], ["Writing (optional)", "1 essay", "40 min", "", "No: scored 2–12"]])}
{mini(("Scores", "Each section is scored 1–36. Your <b>Composite</b> is the rounded average of English, Math and Reading."),
      ("Math choices", "Math questions have <b>four</b> answer choices (the old test had five). A calculator is allowed on Math only: the digital ACT has Desmos built in; on paper, bring your own."),
      ("No guessing penalty", "Blank = wrong. Fill in every answer, even with seconds left."),
      ("Not adaptive", "Unlike the SAT, every student gets the same questions. Earlier questions in Math tend to be easier."))}
{box("tip", "SAT or ACT?", "Both are accepted everywhere that accepts test scores. The ACT gives less time per question but is not adaptive; the SAT gives more time and a built-in graphing calculator. Take one practice test of each and go with the one you score better on.")}
''', pill=("s", "1.1"))

WHAT = topic("whats-on", "What each section tests", f'''
{table(["Section", "What it covers"], [
 ["English", "Passages with underlined parts. Fix punctuation, grammar and sentence structure (about 40%), plus writing strategy, organization and style (about 60%: \"Production of Writing\" and \"Knowledge of Language\")."],
 ["Math", "Pre-algebra through precalc topics: number and quantity, algebra, functions, geometry, statistics and probability, plus some matrices, logs, complex numbers and vectors."],
 ["Reading", "Several passages (literary narrative, social science, humanities, natural science), including one pair of shorter passages. Main idea, details, inference, word meaning, author's purpose."],
 ["Science", "Graphs, tables and experiments in biology, chemistry, physics, earth science and engineering. It's mostly reading data, not memorized facts. Some passages present conflicting viewpoints."],
 ["Writing", "One prompt about an issue with three perspectives. You take a position and support it."]])}
''', pill=("c", "1.2"))

STRAT = topic("strategy", "Strategy", f'''
{pace([["English", 50, 35, "Don't reread the whole passage. Read around each underlined part."], ["Math", 45, 50, "The first 20 or so are usually quicker; bank time for the last 15."], ["Reading", 36, 40, "Roughly 10 minutes per passage set, including the questions."], ["Science", 40, 40, "Go to the graph first; read the text only when a question needs it."]], "ACT pacing clock")}
<ol class="steps">
<li><b>English: shorter is usually better.</b> When choices are all grammatically correct, pick the most concise one that keeps the meaning. \"DELETE\" is right more often than you'd think.</li>
<li><b>Math: skip and return.</b> Every question is worth the same. Don't spend 4 minutes on question 12.</li>
<li><b>Reading: find proof.</b> The right answer is backed by a specific line. If you can't point to it, it's probably a trap.</li>
<li><b>Science: data first.</b> Read axis labels and units. Many questions need only one figure.</li>
<li><b>Fill every bubble.</b> With 1 minute left, guess on everything blank. Pick one letter and use it for all your guesses.</li>
</ol>
''', pill=("s", "1.3"))

PLAN = topic("plan", "A study plan", f'''
{table(["When", "Do this"], [
 ["6–8 weeks out", "Take a full official practice test under time. Find your weakest section."],
 ["Weeks 1–4", "Lessons here, weakest section first. All practice + hard questions, then the timed set."],
 ["Weeks 5–6", "Half-length practice test on this site. Then a second official practice test."],
 ["Last week", "Review your error log, rest, and check your test-day requirements (photo ID, admission ticket, approved calculator)."]])}
''', pill=("s", "1.4"))

CH = [chapter("ch-format", "The Format", "Format", [FORMAT, WHAT]), chapter("ch-strat", "Strategy", "Strategy", [STRAT, PLAN])]
PQ = [
 q("How is the ACT Composite calculated now?", ["Average of English, Math and Reading", "Average of all four sections", "Sum of all sections", "Math and Reading only"], 0, "Science is reported separately.", "s"),
 q("How many answer choices do ACT Math questions have?", ["4", "5", "3", "6"], 0, "The enhanced ACT uses four.", "s"),
 q("How many questions are in the English section?", ["50", "75", "45", "36"], 0, "50 in 35 minutes.", "s"),
 q("Is the ACT adaptive like the SAT?", ["No", "Yes, by section", "Yes, by question", "Only Math is"], 0, "Everyone gets the same questions.", "s"),
 q("With 30 seconds left and 5 blank questions, you should…", ["fill in a guess for all 5", "leave them blank", "solve one carefully", "erase other answers"], 0, "No penalty.", "s"),
 q(psg("The museum, which opened in <u>1952, it</u> attracts thousands of visitors each year.") + "Which choice is best?", ["NO CHANGE", "1952,", "1952; it", "1952. It"], 1, "\"which opened in 1952\" is a nonrestrictive clause closed by a comma; the main verb is \"attracts.\" Adding \"it\" creates an error.", "e"),
 q("If 4x − 3 = 21, x = ?", ["6", "4.5", "5", "7"], 0, "4x = 24.", "m"),
 q(psg("The hikers were tired, so they <u>decided and chose</u> to rest.") + "Which choice is best?", ["NO CHANGE", "decided", "made a decision and chose", "decidedly chose"], 1, "\"decided and chose\" is redundant.", "e"),
 q("A graph shows plant height rising as fertilizer increases from 0 to 10 g, then flattening. What happens from 10 to 20 g?", ["Height stays about the same", "Height keeps rising sharply", "Height falls to zero", "Can't be read from a graph"], 0, "Flattening = little change.", "c"),
 q("On Reading questions, the right answer is…", ["supported by specific text", "the most interesting idea", "usually the longest", "based on outside knowledge"], 0, "Find proof.", "r"),
 q("What is the score range for each ACT section?", ["1–36", "200–800", "2–12", "0–100"], 0, "Writing alone is 2–12.", "s"),
 q("A calculator is allowed on…", ["Math only", "Math and Science", "every section", "no section"], 0, "Science is about data, not computation.", "s"),
]
CHAL = [
 q("Your section scores are English 27, Math 30, Reading 31, Science 24. Composite?", ["29", "28", "27", "30"], 0, "(27 + 30 + 31)/3 = 29.3 → 29. Science isn't included.", "s"),
 q(psg("Because the river flooded every spring, farmers in the valley <u>who wanted to protect their crops,</u> built raised fields.") + "Which choice is best?", ["NO CHANGE", "who wanted to protect their crops", ", who wanted to protect their crops,", "who, wanted to protect their crops"], 1, "Restrictive clause (which farmers) → no commas, and no comma between it and the verb.", "e"),
 q("You have 10 minutes left in Math with questions 36–45 unanswered. Best plan?", ["Do the quickest-looking ones first, then guess on the rest", "Do 36, 37, 38 in order no matter what", "Leave them blank", "Go back to check 1–10"], 0, "Maximize points per minute.", "s"),
 g("Average of 3 section scores is 31, and two are 29 and 33. What is the third?", ["31"], "93 − 62.", "m"),
 q("A table shows that as temperature rises from 20°C to 40°C, enzyme activity rises, but at 50°C activity drops to near zero. Best conclusion?", ["Activity peaks somewhere between 40°C and 50°C or at 40°C", "Activity always rises with temperature", "Temperature has no effect", "The enzyme works best at 20°C"], 0, "Rise then crash: an optimum.", "c"),
 q(psg("The author's argument is <u>very extremely persuasive</u> to most readers.") + "Which choice is best?", ["NO CHANGE", "persuasive", "very extremely, persuasive", "persuasive, in a very extreme way,"], 1, "Concise; \"very extremely\" is redundant.", "e"),
]
EX = [
 q("How long is the Math section?", ["50 minutes", "60 minutes", "45 minutes", "35 minutes"], 0, "45 questions, 50 minutes.", "s"),
 q("Which sections are optional?", ["Science and Writing", "Reading and Writing", "Math and Science", "Only Writing"], 0, "English, Math and Reading are required.", "s"),
 q("How many questions are in Reading?", ["36", "40", "50", "45"], 0, "36 in 40 minutes.", "s"),
 q(psg("Each of the players <u>have</u> a locker.") + "Which choice is best?", ["NO CHANGE", "has", "are having", "were having"], 1, "\"Each\" is singular.", "e"),
 q("x² = 36 and x < 0. x = ?", ["−6", "6", "−18", "±6"], 0, "Negative root.", "m"),
 q("When English choices are all grammatical and mean the same thing, choose…", ["the shortest clear one", "the longest one", "the one with commas", "NO CHANGE always"], 0, "Concision.", "s"),
 q("The Writing score range is…", ["2–12", "1–36", "1–6", "0–100"], 0, "Average of four 2–12 domain scores.", "s"),
 q("Science questions mainly test…", ["interpreting data and experiments", "memorized formulas", "essay writing", "vocabulary"], 0, "Data reasoning.", "s"),
 q("A store sells 3 pens for $2. Cost of 12 pens?", ["$8", "$6", "$24", "$4"], 0, "4 groups × $2.", "m"),
]
build(C, "act-1", L, 1, "Format and Strategy", 'The ACT, <span class="hl">decoded</span>', "How the enhanced ACT is built and scored, what each section tests, and how to pace yourself.", "ACT format, scoring, composite, sections, pacing and study plan with practice questions.", CH, PQ, CHAL, EX, TAGS, OUT, minutes=8)
