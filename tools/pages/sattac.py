from tp_common import *
C = "sat"; L = "SAT"; OUT = "../../courses/sat/sat-tactics.html"
TAGS = {"r": "Reading tactics", "w": "Writing tactics", "m": "Math tactics", "t": "Test day"}
P = psg

RW = topic("rw-playbook", "Reading and Writing: a tactic for every question type", f'''
{table(["When the question says…", "Do this", "Watch out for"], [
 ["\"most logical and precise word\"", "Cover the choices, predict a word from the clue in the sentence, then match.", "Words with the right vibe but wrong meaning; second meanings."],
 ["\"function of the underlined sentence\" / \"main purpose\"", "Ask: what job does it do? Use a verb (contrasts, illustrates, introduces).", "Choices that describe content instead of function."],
 ["\"overall structure\"", "Label each sentence in 2–3 words, then match the sequence.", "Right moves in the wrong order."],
 ["Text 1 / Text 2", "Summarize each author's claim in 5 words. Agree, disagree, or partly?", "Choices that only restate one text."],
 ["\"main idea\"", "What would the author say in one sentence?", "True details that are too narrow; claims too broad."],
 ["\"most directly support/weaken\"", "Restate the exact claim. The answer must hit its key word.", "Related facts that don't touch the claim."],
 ["Graph/table + claim", "Find the claim's two parts; the answer must be true in the data AND match the claim.", "Accurate data that answers a different question."],
 ["\"most logically completes the text\"", "Follow the chain of reasoning; pick what MUST follow.", "Choices that might be true but go further."],
 ["Grammar (\"conventions\")", "Look at what changes between choices. Identify the rule: boundary? agreement? tense?", "Picking what \"sounds right\" instead of applying the rule."],
 ["Transition", "Name the relationship before looking (contrast, cause, example, addition).", "Two choices that mean the same thing: both are wrong."],
 ["Notes / \"accomplish this goal\"", "Underline the goal. Ignore everything else.", "Well-written sentences that don't meet the goal."]])}
{box("tip", "Two-choice tiebreak", "Down to two? Find the single word that makes one of them wrong. Right answers are boring and fully supported; wrong answers have one word too strong (\"always,\" \"proves,\" \"only\").")}
''', pill=("r", "1"))

MATH = topic("math-playbook", "Math: seven tactics that save time", f'''
{tactic(1, "Read the last line first", "Circle what they actually ask for: x, 2x + 1, the y-intercept, the number of solutions. Many wrong choices are the right answer to a different question.", [])}
{tactic(2, "Plug in numbers", "Variables in the answer choices? Pick easy numbers (x = 2, not 0 or 1), compute the answer, then test each choice.", [], steps("Plug in: which equals (x² − 9)/(x − 3)?", [("a|Pick x = 2|e", "Original: (4 − 9)/(2 − 3) = −5/−1 = 5."), ("b|Target: 5|v", "Now test choices with x = 2."), ("c|x + 3 → 5 ✓|g  d|x − 3 → −1 ✗|x", "Only x + 3 matches.")]))}
{tactic(3, "Backsolve", "Numbers in the choices and a question like \"what is x?\" Try the middle choice in the problem; adjust up or down.", [])}
{tactic(4, "Desmos it", "Graphs, systems, quadratics, tables. See the Desmos tactics page.", [])}
{tactic(5, "Look for the shortcut", "If they ask for 6x + 4 and you know 3x + 2 = 7, the answer is 14. Don't solve for x.", [])}
{tactic(6, "Units and labels", "Write units on every number in a word problem. Answers in the wrong units are planted traps (minutes vs hours, cm vs m).", [])}
{tactic(7, "Sanity check", "Does the answer make sense? A probability above 1, a negative length, or a sale price above the original means a mistake.", [])}
''', pill=("m", "2"))

KNOW = topic("memorize", "What to memorize (it's NOT on the reference sheet)", f'''
<p>The built-in reference sheet gives area and volume formulas, the Pythagorean theorem, the special right triangles, and that a circle has 360° (2π radians) and a triangle 180°. Everything below you need to know cold:</p>
{table(["Topic", "Know this"], [
 ["Lines", "m = (y₂ − y₁)/(x₂ − x₁); y = mx + b; parallel = same m; perpendicular m₁·m₂ = −1"],
 ["Quadratics", "vertex x = −b/(2a); x = (−b ± √(b² − 4ac))/(2a); discriminant b² − 4ac; sum of roots −b/a, product c/a"],
 ["Exponential", "y = a(1 ± r)ᵗ; doubling: a·2^(t/d); half-life: a·(½)^(t/h)"],
 ["Percent", "change = (new − old)/old; successive changes multiply"],
 ["Exponents", "x^(m/n) = ⁿ√xᵐ; x⁻ⁿ = 1/xⁿ"],
 ["Circles", "(x − h)² + (y − k)² = r²; arc = (θ/360)·2πr; sector = (θ/360)·πr²; arc = rθ in radians"],
 ["Trig", "SOH-CAH-TOA; sin x° = cos(90 − x)°; radians = degrees × π/180"],
 ["Statistics", "mean, median, range; SD = spread; margin of error gives a plausible range"],
 ["Geometry", "similar figures: lengths ×k, areas ×k², volumes ×k³; exterior angle = sum of two remote interior angles"],
 ["Systems", "no solution: same slope, different intercept; infinite: equations are multiples"]])}
''', pill=("m", "3"))

MODULE = topic("module", "Module strategy and test day", f'''
{mini(("Module 1 decides a lot", "Your Module 1 performance sets the difficulty of Module 2, and only the harder Module 2 can reach top scores. Slow down a little and double-check Module 1."), ("Use the tools", "Flag questions, cross out choices (the strikethrough tool), and use the on-screen timer. Hide the timer if it stresses you; it warns you at 5 minutes."), ("Two passes", "Pass 1: answer everything you can in under ~90 seconds. Pass 2: flagged questions. Last minute: no blanks."), ("Energy", "Use the 10-minute break: water, snack, walk. Math comes second, when you're most tired."))}
{table(["Test-day checklist", ""], [["Night before", "Charge your device; open Bluebook and finish any updates; check in to the test preview; print/save your admission ticket."], ["Bring", "Charged device + charger, admission ticket, photo ID, pencils/pens (scratch paper is provided), optional approved calculator, snack and water."], ["Morning", "Eat breakfast. Arrive early. Do 3–4 easy warm-up questions to wake up."]])}
''', pill=("t", "4"))

CH = [chapter("ch-rw", "Reading and Writing Playbook", "R&W tactics", [RW]), chapter("ch-math", "Math Playbook", "Math tactics", [MATH, KNOW]), chapter("ch-day", "Modules and Test Day", "Test day", [MODULE])]
PQ = [
 q("A question asks which choice \"most effectively uses data from the table to complete the example.\" Two choices are accurate. What decides it?", ["Which one matches the specific claim in the text", "Which one has bigger numbers", "Which one comes first in the table", "Which one is longer"], 0, "True AND relevant.", "r"),
 q("Two transition choices are \"However\" and \"Nevertheless.\" What does that tell you?", ["Both mean contrast, so if contrast is right, there's a problem; likely the answer isn't contrast", "Pick However", "Pick Nevertheless", "Both are correct"], 0, "Synonym choices cancel each other.", "w"),
 q("On a notes question, the best first step is…", ["underline the student's goal", "read all the notes carefully", "pick the longest choice", "check grammar"], 0, "Only the goal matters.", "w"),
 q("Choices are (A) proves, (B) suggests, (C) demonstrates conclusively, (D) guarantees. Without reading the passage, which is most likely right?", ["B", "A", "C", "D"], 0, "Moderate language is usually supported; extreme words rarely are.", "r"),
 q("If 4x + 6 = 18, what is 2x + 3?", ["9", "3", "12", "6"], 0, "Half of 18. Shortcut, no need to find x.", "m"),
 q("Which is equivalent to (x² − 16)/(x − 4)? Plug in x = 3 to check.", ["x + 4", "x − 4", "x² − 4", "x + 16"], 0, "Original at 3: (9 − 16)/(−1) = 7; x + 4 = 7.", "m"),
 q("A grid-in answer is 2/3. Which entry is NOT accepted?", ["0.66", "2/3", ".6667", "0.667"], 0, "Use all available spaces: .6666, .6667, 0.666 or 0.667. 0.66 is too short.", "m"),
 q("Is the quadratic formula on the reference sheet?", ["No", "Yes", "Only in Module 2", "Only for grid-ins"], 0, "Memorize it.", "m"),
 q("You've spent 2.5 minutes on one math question. Best move?", ["Guess, flag, move on", "Keep going until solved", "Leave it blank", "Restart the module"], 0, "Protect the rest of the module.", "t"),
 q("What should you do the night before the test?", ["Charge your device and update Bluebook", "Take a full practice test", "Stay up to cram", "Download new apps"], 0, "Avoid tech problems.", "t"),
 q("Why does Module 1 accuracy matter so much?", ["It determines whether you get the harder Module 2", "Module 1 questions count double", "Module 2 is unscored", "It's longer"], 0, "Adaptive routing.", "t"),
 q("A word problem's answer choices include 45 and 0.75. The question asks for hours; you computed 45 minutes. Answer?", ["0.75", "45", "Both", "Neither"], 0, "Units trap.", "m"),
]
CHAL = [
 q("A word-in-context question's sentence says the critic's review was \"anything but ___\": she praised every scene. Your prediction for the blank?", ["something like \"harsh\"", "something like \"positive\"", "something like \"long\"", "something like \"famous\""], 0, "\"Anything but\" flips it: praised → anything but harsh.", "r"),
 q("Cross-text: Text 1 says a drug works; Text 2 says it works only at high doses. The best answer describes Text 2 as…", ["qualifying Text 1's claim", "rejecting Text 1 entirely", "agreeing completely", "changing the subject"], 0, "Adds a condition.", "r"),
 q("Plug in for: which is equivalent to 2^(x+2)?", ["4·2ˣ", "2ˣ + 4", "2·2ˣ", "4ˣ"], 0, "x = 1: 2³ = 8; 4·2 = 8 ✓; 2 + 4 = 6; 2·2 = 4; 4.", "m"),
 q("\"If x + y = 8 and x − y = 2, what is x² − y²?\" Fastest route?", ["(x + y)(x − y) = 16", "Solve for x and y separately", "Desmos regression", "Backsolve"], 0, "Difference of squares shortcut.", "m"),
 q("Module 2 feels much harder than Module 1. What does that likely mean?", ["You did well on Module 1", "You did poorly on Module 1", "There's an error", "Nothing"], 0, "Harder Module 2 is good news.", "t"),
 q("In a grammar question, choices differ only in commas. What should you do first?", ["Find the main subject and verb, then decide what's essential", "Pick the one with the most commas", "Pick the one with the fewest commas", "Read it aloud"], 0, "Rule-based approach.", "w"),
]
EX = []
build(C, "sat-tactics", L, 0, "Strategy Playbook", 'The SAT <span class="hl">playbook</span>', "A tactic for every Reading and Writing question type, seven math time-savers, what to memorize, module strategy and a test-day checklist.", "SAT strategy playbook: question-type tactics, math shortcuts, what to memorize, adaptive module strategy and test-day checklist.", CH, PQ, CHAL, EX, TAGS, OUT)
