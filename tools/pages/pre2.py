from math_common import *
L = "Before Precalc"; OUT = "../../courses/math/pre-2.html"

SOLVE = topic("solve-lin", "Solving linear equations", f'''
<p>Whatever you do to one side, do to the other. Undo operations in reverse order: first clear addition/subtraction, then multiplication/division.</p>
{steps("Solve 3x + 7 = 22", [
 ("a|3x|v  b|+  c|7|n  d|=  e|22|n", "Goal: get x alone. First undo the + 7."),
 ("a|3x|v  b|+  c|7|n  f|− 7|e  d|=  e|22|n  g|− 7|e", "Subtract 7 from both sides."),
 ("a|3x|v  d|=  h|15|n", "Now undo the × 3."),
 ("a|3x|v  i|÷ 3|e  d|=  h|15|n  j|÷ 3|e", "Divide both sides by 3."),
 ("k|x|g  d|=  l|5|g", "x = 5. Check: 3(5) + 7 = 22 ✓"),
])}
{steps("Solve 2(x − 3) = 4x + 10", [
 ("a|2(x − 3)|e  d|=  b|4x|v  c|+ 10|n", "Distribute first."),
 ("e|2x|v  f|− 6|n  d|=  b|4x|v  c|+ 10|n", "Move the x terms to one side."),
 ("e|2x|v  g|− 4x|e  f|− 6|n  d|=  c|10|n", "Subtract 4x from both sides."),
 ("h|−2x|v  f|− 6|n  d|=  c|10|n", "2x − 4x = −2x. Add 6."),
 ("h|−2x|v  d|=  i|16|n", "Divide by −2."),
 ("j|x|g  d|=  k|−8|g", "x = −8."),
])}
{box("tip", "Fractions", "If the equation has fractions, multiply every term by the common denominator first. x/2 + x/3 = 5 → 3x + 2x = 30 → x = 6.")}
''', pill=("p", "2.1"))

SLOPE = topic("slope", "Slope and the three forms of a line", f'''
<p><b>Slope</b> is rise over run: {m("m")} = ({m("y")}₂ − {m("y")}₁)/({m("x")}₂ − {m("x")}₁). It's how much {m("y")} changes every time {m("x")} goes up by 1.</p>
{table(["Form", "Equation", "Best for"], [
 ["Slope-intercept", f"{m('y')} = {m('mx')} + {m('b')}", "graphing: start at b, then rise m per 1 run"],
 ["Point-slope", f"{m('y')} − {m('y')}₁ = {m('m')}({m('x')} − {m('x')}₁)", "writing a line from a point and a slope"],
 ["Standard", f"{m('Ax')} + {m('By')} = {m('C')}", "intercepts: set x = 0, then y = 0"],
])}
{lab(title="Slope-intercept lab", sub="Drag m and b. Watch where the line crosses each axis.", x=[-10, 10], y=[-10, 10], gx=1, gy=1, params={"m": [-4, 4, 0.25, 1.5, "m"], "b": [-8, 8, 0.5, -2, "b"]}, fns=[fn("m*x+b", "y = mx + b")], dots=[["0", "b", "y-int {b}", "#EA580C"], ["-b/m", "0", "x-int {-b/m}", "#059669"]], read=[["slope:", "m"], ["x-intercept:", "-b/m"]])}
{mini(("Parallel lines", "Same slope. y = 2x + 1 and y = 2x − 5 never meet."), ("Perpendicular lines", "Slopes are negative reciprocals: 2 and −1/2. Their product is −1."))}
{worked("Write the line through (2, 5) and (6, −3).", f"Slope = (−3 − 5)/(6 − 2) = −8/4 = −2. Point-slope: {m('y')} − 5 = −2({m('x')} − 2). Slope-intercept: {m('y')} = −2{m('x')} + 9.")}
''', pill=("c", "2.2"))

SYS = topic("systems", "Systems of equations", f'''
<p>A system's solution is the point where the lines meet. Two lines can meet once, never (parallel), or everywhere (same line).</p>
{lab(title="Where do they cross?", sub="The solution is the intersection.", x=[-8, 8], y=[-8, 8], gx=1, gy=1, params={"m": [-3, 3, 0.5, -1, "m₂"], "b": [-6, 6, 0.5, 4, "b₂"]}, fns=[fn("2*x-2", "y = 2x − 2"), fn("m*x+b", "y = m₂x + b₂")], dots=[["(b+2)/(2-m)", "2*(b+2)/(2-m)-2", "({(b+2)/(2-m)}, {2*(b+2)/(2-m)-2})", "#7C3AED"]])}
{steps("Elimination: 2x + y = 7 and x − y = 2", [
 ("a|2x + y = 7|s  b|x − y = 2|v", "The y's are opposites. Add the equations."),
 ("c|3x = 9|e", "(2x + x) + (y − y) = 7 + 2."),
 ("d|x = 3|g", "Divide by 3."),
 ("d|x = 3|g  e|3 − y = 2|v", "Substitute into x − y = 2."),
 ("d|x = 3|g  f|y = 1|g", "Solution: (3, 1). Check in 2x + y: 6 + 1 = 7 ✓"),
])}
{box("tip", "Substitution vs elimination", "If one variable is already alone (y = …), substitute. If coefficients line up or are easy to make opposite, eliminate.")}
''', pill=("p", "2.3"))

INEQ = topic("inequalities", "Inequalities and absolute value", f'''
<p>Solve inequalities like equations, with one extra rule: <b>multiplying or dividing by a negative flips the sign.</b> −2x &lt; 6 → x &gt; −3.</p>
{table(["Absolute value", "Means", "Solution"], [
 [f"|{m('x')} − 3| = 5", "distance from 3 is 5", f"{m('x')} = 8 or {m('x')} = −2"],
 [f"|{m('x')} − 3| &lt; 5", "within 5 of 3", f"−2 &lt; {m('x')} &lt; 8"],
 [f"|{m('x')} − 3| &gt; 5", "more than 5 from 3", f"{m('x')} &lt; −2 or {m('x')} &gt; 8"],
])}
{lab(title="Absolute value graph", sub="y = a|x − h| + k makes a V with its corner at (h, k).", x=[-8, 8], y=[-6, 10], gx=1, gy=1, params={"a": [-3, 3, 0.5, 1, "a"], "h": [-5, 5, 0.5, 3, "h"], "k": [-5, 5, 0.5, -2, "k"]}, fns=[fn("a*abs(x-h)+k", "y = a|x − h| + k")], dots=[["h", "k", "vertex ({h}, {k})", "#EA580C"]])}
''', pill=("c", "2.4"))

SUM = topic("summary-pre2", "Unit summary", mini(
 ("Equations", "Distribute, collect x's on one side, undo + −, then × ÷. Always check."),
 ("Slope", "m = Δy/Δx. Parallel: same m. Perpendicular: m₁·m₂ = −1."),
 ("Systems", "Solution = intersection. Substitute or eliminate. Parallel → none, same line → infinitely many."),
 ("Inequalities", "Flip the sign when you × or ÷ by a negative. |x − c| < d → within d of c."),
))
CH = [chapter("ch-eq", "Linear Equations", "Equations", [SOLVE]), chapter("ch-lines", "Lines and Slope", "Lines", [SLOPE]), chapter("ch-sys", "Systems and Inequalities", "Systems", [SYS, INEQ, SUM])]

PQ = [
 q("Solve 5x − 4 = 21.", ["x = 5", "x = 17/5", "x = 25", "x = 4"], 0, "Add 4: 5x = 25, x = 5.", "p"),
 q("Solve 4(x + 1) = 2x − 6.", ["x = −5", "x = −1", "x = 5", "x = −7/3"], 0, "4x + 4 = 2x − 6 → 2x = −10.", "p"),
 q("Solve x/3 + 2 = x/2.", ["x = 12", "x = 6", "x = −12", "x = 2"], 0, "Multiply by 6: 2x + 12 = 3x.", "p"),
 q("Slope through (1, 2) and (4, 11)?", ["3", "1/3", "9", "−3"], 0, "(11 − 2)/(4 − 1) = 9/3.", "p"),
 q("Slope of 2x + 3y = 12?", ["−2/3", "2/3", "−3/2", "4"], 0, "3y = −2x + 12, y = −(2/3)x + 4.", "c"),
 q("Line with slope −4 through (0, 7)?", ["y = −4x + 7", "y = 7x − 4", "y = −4x − 7", "y = 4x + 7"], 0, "The point is the y-intercept.", "p"),
 q("Slope of a line perpendicular to y = 3x − 1?", ["−1/3", "3", "−3", "1/3"], 0, "Negative reciprocal of 3.", "c"),
 q("Solve: y = 2x and x + y = 9.", ["(3, 6)", "(6, 3)", "(2, 7)", "(4.5, 4.5)"], 0, "x + 2x = 9 → x = 3, y = 6.", "p"),
 q("How many solutions: y = 3x + 1 and y = 3x − 4?", ["None", "One", "Two", "Infinitely many"], 0, "Same slope, different intercepts: parallel.", "g"),
 q("Solve −3x + 2 ≥ 11.", ["x ≤ −3", "x ≥ −3", "x ≤ 3", "x ≥ 3"], 0, "−3x ≥ 9; dividing by −3 flips it.", "p"),
 q("Solve |x + 1| = 4.", ["x = 3 or x = −5", "x = 3", "x = −3 or x = 5", "x = ±4"], 0, "x + 1 = 4 or x + 1 = −4.", "p"),
 q("Solve |x − 2| < 3.", ["−1 < x < 5", "x < 5", "x < −1 or x > 5", "−5 < x < 1"], 0, "Within 3 of 2.", "p"),
 q("A plan costs $20 plus $0.15 per minute. Which models cost C for m minutes?", ["C = 0.15m + 20", "C = 20m + 0.15", "C = 20.15m", "C = 0.15(m + 20)"], 0, "Fixed fee is the intercept, rate is the slope.", "w"),
 q("The vertex of y = −2|x + 3| + 5 is…", ["(−3, 5)", "(3, 5)", "(−3, −5)", "(5, −3)"], 0, "y = a|x − h| + k with h = −3, k = 5.", "g"),
]
CHAL = [
 q("For which k does kx + 2y = 6 have no solution with y = 3x + 1?", ["k = −6", "k = 6", "k = −3", "k = 3"], 0, "kx + 2y = 6 → y = −(k/2)x + 3. Parallel needs −k/2 = 3, so k = −6 (intercepts 3 ≠ 1).", "c"),
 q("Solve 3(2x − 1) − 2(x + 4) = x.", ["x = 11/3", "x = 3", "x = −11/3", "x = 11/5"], 0, "6x − 3 − 2x − 8 = x → 3x = 11.", "p"),
 q("Tickets: adults $8, kids $5. 40 tickets earned $260. How many adults?", ["20", "15", "25", "30"], 0, "a + k = 40, 8a + 5k = 260 → 8a + 200 − 5a = 260 → a = 20.", "w"),
 q("Solve |2x − 5| ≥ 7.", ["x ≤ −1 or x ≥ 6", "−1 ≤ x ≤ 6", "x ≥ 6", "x ≤ −6 or x ≥ 1"], 0, "2x − 5 ≥ 7 → x ≥ 6; 2x − 5 ≤ −7 → x ≤ −1.", "p"),
 q("The line through (−2, 4) perpendicular to 2x − y = 3 is…", ["y = −x/2 + 3", "y = 2x + 8", "y = −2x", "y = x/2 + 5"], 0, "Given slope 2 → perpendicular slope −1/2: y − 4 = −½(x + 2) → y = −x/2 + 3.", "p"),
 q("A system has infinitely many solutions when the two lines…", ["are the same line", "have the same slope only", "are perpendicular", "cross at the origin"], 0, "Every point on one is on the other.", "c"),
]
EXQ = [
 q("Solve 7 − 2x = 15.", ["x = −4", "x = 4", "x = −11", "x = 11"], 0, "−2x = 8.", "p"),
 q("Solve 3x − 5 = x + 9.", ["x = 7", "x = 2", "x = 4", "x = −7"], 0, "2x = 14.", "p"),
 q("Slope through (−1, 3) and (3, −5)?", ["−2", "2", "−1/2", "−8"], 0, "−8/4.", "p"),
 q("y-intercept of 4x − 2y = 10?", ["−5", "5", "2.5", "10"], 0, "x = 0 → −2y = 10.", "p"),
 q("Line parallel to y = −x + 2 through (3, 3)?", ["y = −x + 6", "y = x", "y = −x + 3", "y = x + 6"], 0, "Slope −1: 3 = −3 + b.", "p"),
 q("Solve: x + y = 10, x − y = 4.", ["(7, 3)", "(3, 7)", "(6, 4)", "(5, 5)"], 0, "Add: 2x = 14.", "p"),
 q("Solve 2x − 3 < 9.", ["x < 6", "x > 6", "x < 3", "x < −6"], 0, "2x < 12.", "p"),
 q("Solve −x/4 > 2.", ["x < −8", "x > −8", "x > 8", "x < 8"], 0, "Multiply by −4 and flip.", "p"),
 q("Solve |x| = −3.", ["No solution", "x = ±3", "x = −3", "x = 3"], 0, "Absolute value is never negative.", "c"),
 q("A taxi charges $3 plus $2 per mile. Cost for 7 miles?", ["$17", "$14", "$21", "$23"], 0, "3 + 2·7.", "w"),
 q("Which line is steepest?", ["y = −5x + 1", "y = 4x", "y = x + 10", "y = 0.5x − 3"], 0, "Steepness is |m|; |−5| is largest.", "g"),
 q("Graph of y = |x − 4| has its corner at…", ["(4, 0)", "(−4, 0)", "(0, 4)", "(0, −4)"], 0, "h = 4, k = 0.", "g"),
]
FRQS = [
 {"q": "A gym charges a sign-up fee plus a monthly fee. After 3 months a member has paid $110; after 8 months, $235.", "parts": [
  {"p": "(a) Find the monthly fee and the sign-up fee.", "rubric": [["Slope (235 − 110)/(8 − 3) = 25", 1], ["Intercept 110 − 75 = 35", 1]], "answer": "$25 per month, $35 sign-up."},
  {"p": "(b) Write a linear model C(m) and interpret its slope in context.", "rubric": [["C(m) = 25m + 35", 1], ["Slope: total cost rises $25 for each extra month", 1]], "answer": "C(m) = 25m + 35. Each month adds $25."},
  {"p": "(c) A second gym charges $45 per month with no sign-up fee. After how many months is the first gym cheaper?", "rubric": [["Sets 25m + 35 < 45m", 1], ["m > 1.75, so from month 2 on", 1]], "answer": "35 < 20m → m > 1.75: from the 2nd month on."}]},
 {"q": "Solve and graph on a number line.", "parts": [
  {"p": "(a) |3x + 1| ≤ 8", "rubric": [["−8 ≤ 3x + 1 ≤ 8", 1], ["−3 ≤ x ≤ 7/3, closed dots", 1]], "answer": "−3 ≤ x ≤ 7/3."},
  {"p": "(b) 4 − 2x > 10", "rubric": [["−2x > 6", 1], ["x < −3 with the flip, open dot", 1]], "answer": "x < −3."}]},
]
build("pre-2", L, 2, "Linear Equations and Lines", 'Lines and <span class="hl">linear equations</span>', "Solving equations, slope, the three forms of a line, systems, and inequalities.", "Before Precalc unit 2: linear equations, slope, systems and inequalities with interactive graphs.", CH, PQ, CHAL, EXQ, FRQS, OUT)
