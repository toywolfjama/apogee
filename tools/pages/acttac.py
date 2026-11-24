from tp_common import *
C = "act"; L = "ACT"; OUT = "../../courses/act/act-tactics.html"
TAGS = {"e": "English", "m": "Math", "r": "Reading", "c": "Science", "t": "Test day"}

ENG = topic("english", "English tactics", f'''
{table(["Tactic", "Why it works"], [
 ["Read the sentence before and after the underline", "Tense, pronouns and transitions depend on context."],
 ["Look at what changes in the choices", "It tells you which rule is being tested."],
 ["Shortest grammatical choice wins (usually)", "ACT rewards concise writing. Check that meaning isn't lost."],
 ["Don't fear DELETE / OMIT", "If the underlined part is redundant or off-topic, removing it is often right."],
 ["\"Should the writer add/delete…\"", "Decide yes/no first, then pick the reason that matches what the sentence actually does."],
 ["Questions about the whole essay", "Do them when you reach the end of the passage."]])}
{mini(("The 6 rules that cover most questions", "1) Comma splices 2) Commas around extra info 3) Subject-verb agreement 4) Pronoun agreement/case 5) Verb tense consistency 6) Redundancy/wordiness"), ("Punctuation quick test", "Semicolon = period. Colon needs a full sentence before it. Dashes and commas around extra info come in pairs."))}
''', pill=("e", "1"))

MATH = topic("math", "Math tactics (no formula sheet!)", f'''
{table(["Tactic", "Use when"], [["Skip and return", "A question will take more than 2 minutes. All questions count the same."], ["Backsolve", "Numerical choices; plug them into the problem."], ["Plug in numbers", "Variables in the choices."], ["Estimate from figures", "Look at the diagram to eliminate impossible choices (a clearly obtuse angle isn't 40°)."], ["Use the calculator for graphs and tables", "Intersections, regressions, stats."], ["Write it down", "Labeling a diagram with every given value prevents misreads."]])}
<p><b>Must-know formulas (no sheet on the ACT):</b> area/perimeter of all basic shapes, circle area and circumference, Pythagorean theorem and special right triangles, volume of box/cylinder, slope, distance and midpoint, quadratic formula, SOH-CAH-TOA, sin²θ + cos²θ = 1, polygon angles (n − 2)·180°, arithmetic and geometric sequences, probability and combinations, percent change, log rules.</p>
''', pill=("m", "2"))

READ = topic("reading", "Reading tactics", f'''
{mini(("Order your passages", "Do your favorite passage type first (narrative, science, etc.). You choose the order on test day."), ("Skim, then answer", "2–3 minutes skimming: main idea of each paragraph and the author's tone. Then go to questions."), ("Line-reference questions first", "They're faster and teach you the passage."), ("Proof or it's wrong", "Every right answer is backed by specific words. Extreme words (always, never, entirely) are usually traps."), ("Paired passages", "Passage A questions, then B, then both."), ("Time check", "About 10 minutes per passage set. Move on at 11."))}
''', pill=("r", "3"))

SCI = topic("science", "Science tactics", f'''
{mini(("Data first", "Most questions only need a figure. Read axes, units and the legend, then answer."), ("Triage passages", "Data-heavy passages (graphs/tables) are fastest; do conflicting viewpoints last if they slow you down."), ("Trends language", "Increases, decreases, increases then levels off, no clear relationship. Match the choice wording to the data."), ("Experiments", "Independent = changed, dependent = measured, controls = kept the same. \"Which change would test…\": change only ONE variable."), ("Viewpoints", "Summarize each scientist in one line, note what they agree on."), ("Don't overthink", "Outside knowledge rarely helps; the answer is in the data."))}
''', pill=("c", "4"))

DAY = topic("day", "Guessing and test day", f'''
{mini(("Letter of the day", "Pick one letter and use it for every blind guess. It's faster than deciding each time, and there's no penalty."), ("Last 2 minutes", "Fill every blank. Then return to any flagged question you were close on."), ("Breaks", "Use them: snack, water, stretch. Don't review answers in your head."), ("Bring", "Admission ticket, photo ID, permitted calculator with fresh batteries, No. 2 pencils (paper test), watch without alarms, snack."))}
''', pill=("t", "5"))

CH = [chapter("ch-eng", "English", "English", [ENG]), chapter("ch-math", "Math", "Math", [MATH]), chapter("ch-read", "Reading", "Reading", [READ]), chapter("ch-sci", "Science", "Science", [SCI]), chapter("ch-day", "Test Day", "Test day", [DAY])]
PQ = [
 q("Two English choices are both grammatical and mean the same. Pick…", ["the shorter one", "the longer one", "the one with a semicolon", "NO CHANGE automatically"], 0, "Concision.", "e"),
 q("A sentence is off-topic for the paragraph. Best choice is likely…", ["DELETE the underlined portion", "NO CHANGE", "a longer version", "adding a comma"], 0, "Remove irrelevant info.", "e"),
 q("Choices differ only in where the comma goes. Which rule is likely tested?", ["Punctuation of clauses or extra info", "Verb tense", "Pronouns", "Redundancy"], 0, "Look at what changes.", "e"),
 q("Is there a formula sheet on ACT Math?", ["No", "Yes", "Only digital", "Only for geometry"], 0, "Memorize formulas.", "m"),
 q("Question 18 is taking forever. Best move?", ["Guess, mark it, come back later", "Keep working until solved", "Skip all remaining questions", "Leave it blank"], 0, "All questions are worth the same.", "m"),
 q("A figure shows a clearly obtuse angle. Which value can you eliminate?", ["35°", "110°", "130°", "145°"], 0, "Obtuse means more than 90°.", "m"),
 q("On Reading, a choice says the author \"completely rejects\" an idea. That's usually…", ["a trap unless the text is that strong", "right", "the main idea", "a detail"], 0, "Extreme language.", "r"),
 q("You can do Reading passages in any order. Smart choice?", ["Start with your strongest passage type", "Always go in order", "Start with the hardest", "Skip paired passages"], 0, "Bank easy points.", "r"),
 q("A Science question asks for a value from Figure 2. What should you read?", ["Just Figure 2's axes, units and data", "The whole passage", "Every figure", "Outside notes"], 0, "Data first.", "c"),
 q("To test whether light affects growth, a student should change…", ["only the light, keeping everything else the same", "light and water", "everything", "nothing"], 0, "One variable.", "c"),
 q("With 1 minute left and 6 blanks in Science, you should…", ["fill all 6 with your letter of the day", "solve one", "leave them", "erase answers"], 0, "No penalty.", "t"),
 q("For a paper ACT, bring…", ["a permitted calculator, ID, admission ticket, No. 2 pencils", "a phone for the calculator", "a laptop", "notes"], 0, "Test-day list.", "t"),
]
CHAL = [
 q(psg("The scientist's findings <u>were published in a journal that is published every month, monthly,</u> in 2021.") + "Best choice?", ["were published in a monthly journal", "NO CHANGE", "were monthly published in a journal every month", "were, in a monthly journal, published monthly"], 0, "Cut both redundancies.", "e"),
 q("\"Which choice most effectively concludes the paragraph?\" Your first step is…", ["identify the paragraph's main point", "pick the shortest", "pick NO CHANGE", "look at the next paragraph only"], 0, "Conclusion must match the point.", "e"),
 q("A right triangle has legs 6 and 8. Without a formula sheet, the hypotenuse is…", ["10", "14", "48", "√28"], 0, "Pythagorean (3-4-5 ×2).", "m"),
 q("Paired passages: author B \"qualifies\" author A's claim. Which choice would say that?", ["B accepts A's claim but adds limits", "B rejects A completely", "B ignores A", "B repeats A"], 0, "Qualify = limit.", "r"),
 q("Two scientists disagree about a cause. A question asks what they'd BOTH accept. Look for…", ["the facts both mention without disputing", "Scientist 1's conclusion", "Scientist 2's conclusion", "outside knowledge"], 0, "Common ground.", "c"),
 q("Your composite is the average of which scores?", ["English, Math, Reading", "All four sections", "Math and Science", "English and Reading"], 0, "Science is separate.", "t"),
]
build(C, "act-tactics", L, 0, "Strategy Playbook", 'The ACT <span class="hl">playbook</span>', "Section-by-section tactics, the English rules that cover most questions, formulas to memorize, passage strategy, and test day.", "ACT strategy playbook: English, Math, Reading and Science tactics, formulas to memorize and test-day checklist.", CH, PQ, CHAL, [], TAGS, OUT)
