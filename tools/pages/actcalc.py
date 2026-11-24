from tp_common import *
C = "act"; L = "ACT"; OUT = "../../courses/act/act-calc.html"
TAGS = {"d": "Desmos", "t": "TI-84", "s": "Strategy"}

WHICH = topic("which", "Which calculator will you have?", f'''
{table(["Format", "Calculator"], [["Digital ACT (online)", "A built-in Desmos graphing calculator on the Math section, plus your own permitted handheld if you want"], ["Paper ACT", "Only your own permitted calculator"]])}
<p>Calculators are allowed on Math only. Calculators with a computer algebra system (CAS), like the TI-89 or TI-Nspire CAS, are banned; the TI-84 Plus CE is allowed. Always check ACT's current calculator policy before test day.</p>
{box("tip", "Desmos on the ACT starts in degrees", "The ACT's Desmos defaults to degrees (desmos.com defaults to radians). If you practice on desmos.com, switch to degrees in the wrench menu so it matches.")}
{EMBED}
''', pill=("s", "1"))

DES = topic("desmos", "Desmos tactics for ACT Math", f'''
<p>All the SAT Desmos tactics work on the digital ACT too. The ones that pay off most on ACT questions:</p>
{tactic(1, "Intersections and systems", "Type both equations, click the crossing.", ["y=3x-7", "y=-x+5"])}
{tactic(2, "Regressions from a table", "ACT loves \"which equation fits this table.\"", ["y_1 ~ mx_1+b", "y_1 ~ ab^{x_1}"])}
{tactic(3, "Complex numbers: do them by hand", "Don't count on the test's Desmos for complex arithmetic. FOIL (a + bi)(c + di) with i² = −1; it takes seconds. A TI-84 in a+bi mode also works.", [])}
{tactic(4, "Matrices", "Desmos doesn't do matrices in the graphing calculator; compute the determinant ad − bc by hand or use a TI-84.", [])}
{tactic(5, "Trig values", "With degrees set, type the expression directly.", ["sin(150)", "cos(60)^2+sin(60)^2"])}
{tactic(6, "Counting", "Desmos has nCr and nPr and factorials.", ["nCr(10,3)", "nPr(5,3)", "6!"])}
{tactic(7, "Logs", "Natural log and any base.", ["log(1000)", "ln(e^3)", "log_2(32)"], "<p>Type log, then _2 for the base.</p>")}
{reg([[1, 4], [2, 7], [3, 12], [4, 19]], "quad", "Regression lab", "ACT-style table. Is it linear, quadratic or exponential? Try each model and watch r².")}
''', pill=("d", "2"))

TI = topic("ti84", "TI-84 Plus CE: the keystrokes that matter", f'''
{table(["Task", "Keystrokes"], [
 ["Intersection of two graphs", "Y= enter Y1 and Y2 → GRAPH → 2nd TRACE (CALC) → 5:intersect → ENTER, ENTER, ENTER"],
 ["Zeros (x-intercepts)", "2nd TRACE → 2:zero → left bound, right bound, guess"],
 ["Max / min", "2nd TRACE → 3:minimum or 4:maximum"],
 ["Table of values", "2nd GRAPH (TABLE)"],
 ["Linear regression", "STAT → 1:Edit (L1 = x, L2 = y) → STAT → CALC → 4:LinReg(ax+b) → ENTER"],
 ["Quadratic / exponential regression", "STAT → CALC → 5:QuadReg or 0:ExpReg"],
 ["Mean, median, SD", "STAT → CALC → 1:1-Var Stats (x̄ = mean, Sx/σx = SD, Med = median)"],
 ["Decimal → fraction", "MATH → 1:►Frac"],
 ["Combinations / permutations", "MATH → PROB → 3:nCr or 2:nPr; 4:! for factorial"],
 ["Complex numbers", "MODE → a+bi; i is 2nd . (decimal point)"],
 ["Matrices", "2nd x⁻¹ (MATRIX) → EDIT to enter; MATH → det( for the determinant"],
 ["Degree mode", "MODE → DEGREE (check before every trig question)"],
 ["Logs with any base", "MATH → logBASE("]])}
{steps("TI-84 linear regression", [
 ("a|STAT|s  b|1:Edit|v", "Enter x-values in L1 and y-values in L2."),
 ("a|STAT|s  c|CALC|e  d|4:LinReg(ax+b)|v", "Arrow right to CALC, choose LinReg."),
 ("e|y = ax + b|g", "Press ENTER (twice on some screens). Read a (slope) and b (intercept)."),
])}
<p>Crux also has <a href="../../calculator.html">TI-84 programs</a> you can load onto your calculator.</p>
''', pill=("t", "3"))

CH = [chapter("ch-which", "Your Calculator", "Which one", [WHICH]), chapter("ch-desmos", "Desmos on the ACT", "Desmos", [DES]), chapter("ch-ti", "TI-84 Keystrokes", "TI-84", [TI])]
PQ = [
 q("On the paper ACT, which calculator can you use on Math?", ["Your own permitted calculator", "A built-in Desmos", "None", "Any phone app"], 0, "Desmos is digital only.", "s"),
 q("Which calculator is NOT allowed?", ["TI-89", "TI-84 Plus CE", "TI-83 Plus", "TI-30XS"], 0, "TI-89 has a computer algebra system.", "s"),
 q("You type sin(30) in Desmos on the digital ACT. What should you see?", ["0.5", "−0.988", "30", "An error"], 0, "ACT's Desmos defaults to degrees.", "d"),
 g("x: 1, 2, 3, 4 and y: 4, 7, 12, 19. Using a quadratic regression, what is y at x = 5?", ["28"], "y = x² + 3 → 28.", "d"),
 q("On a TI-84, where is the intersect command?", ["2nd TRACE → 5", "STAT → CALC → 5", "MATH → 5", "Y= → 5"], 0, "CALC menu.", "t"),
 q("On a TI-84, 1-Var Stats gives…", ["mean, median and standard deviation", "regression lines", "matrix determinants", "intersections"], 0, "STAT → CALC → 1.", "t"),
 q("How do you type i on a TI-84?", ["2nd then the decimal point key", "ALPHA I", "MATH → i", "You can't"], 0, "i is above the decimal point.", "t"),
 g("nCr(8, 3) = ?", ["56"], "8·7·6/6.", "d"),
 g("log base 3 of 81?", ["4"], "3⁴ = 81. Desmos: log_3(81).", "d"),
 q("The fastest way to answer \"which equation fits the table\" is usually…", ["a regression", "guessing", "graphing each choice by hand", "1-Var Stats"], 0, "Fit and check r².", "s"),
 q("TI-84: decimal 0.375 to a fraction?", ["MATH → 1:►Frac", "2nd → FRAC", "STAT → Frac", "MODE → FRAC"], 0, "►Frac.", "t"),
 g("Determinant of [[4, 1], [6, 2]]?", ["2"], "8 − 6.", "t"),
]
CHAL = [
 g("y = x² − 4x + 1 and y = 2x − 8 intersect at one point. What is its x-coordinate?", ["3"], "x² − 6x + 9 = 0 → x = 3. Desmos: one tangent point.", "d"),
 q("x: 0, 1, 2, 3; y: 2, 6, 18, 54. Which regression gives r² = 1?", ["Exponential", "Linear", "Quadratic", "None"], 0, "Ratio 3 each step: y = 2·3ˣ.", "d"),
 g("(2 + 3i)(4 − i) = a + bi. What is a?", ["11"], "8 − 2i + 12i − 3i² = 11 + 10i.", "t"),
 g("How many 5-card hands from a 52-card deck? Give the number divided by 1000, rounded to the nearest whole number.", ["2599"], "nCr(52,5) = 2,598,960 → 2599.", "d"),
 q("A TI-84 shows 'ERR: DOMAIN' when computing log(−5). Why?", ["Logs of negative numbers aren't real", "Wrong mode", "Battery low", "Need degrees"], 0, "Domain x > 0.", "t"),
 q("Your TI-84's sin(90) gives 0.894. What's wrong?", ["It's in radian mode", "It's broken", "It's in degree mode", "Nothing"], 0, "sin 90° = 1; set MODE → DEGREE.", "t"),
]
build(C, "act-calc", L, 0, "Calculator Tactics: Desmos and TI-84", 'Calculator <span class="hl">tactics</span>', "Desmos on the digital ACT, TI-84 keystrokes for paper, regressions, stats, complex numbers and matrices.", "ACT calculator tactics: Desmos on the digital ACT and TI-84 Plus CE keystrokes for intersections, regressions, statistics and more.", CH, PQ, CHAL, [], TAGS, OUT)
