from tp_common import *
C = "sat"; L = "SAT"; OUT = "../../courses/sat/sat-desmos.html"
TAGS = {"d": "Desmos", "s": "Strategy"}

INTRO = topic("why", "Why Desmos is your biggest advantage", f'''
<p>The Desmos graphing calculator is built into every SAT Math question. Used well, it turns many algebra problems into \"type it in and click.\" Open it with the <b>ƒ Desmos</b> button (bottom right) and try every tactic on this page as you read. Click any gray code chip to copy it, then paste it into Desmos.</p>
{EMBED}
{mini(("Typing shortcuts", f"{dz('sqrt')} → √, {dz('pi')} → π, {dz('^')} for exponents, {dz('/')} makes a fraction, {dz('|x|')} or {dz('abs(x)')} for absolute value, {dz('<=')} → ≤."), ("Practice the real one", "Bluebook's calculator is Desmos with a few features turned off. Practice in the test version too: desmos.com/testing → \"Digital SAT.\""))}
{box("trap", "Know when NOT to use it", "If you can do it in your head in 10 seconds (3x = 12), just do it. Desmos is for anything with a graph, a quadratic, a system, a table of data, or a messy equation.")}
''', pill=("d", "★"))

T1 = topic("solve", "Solving equations and systems", f'''
{tactic(1, "Solve any equation in one variable", "Any equation you'd have to rearrange or factor. Type the whole equation; Desmos draws vertical lines (or gray points) at the solutions.", ["2x^2-3x-9=0", "sqrt(x+3)=x-3"], "<p>Click the gray dots on the x-axis to read each solution. With a radical, Desmos automatically ignores the extraneous solution.</p>")}
{tactic(2, "Solve a system", "Two equations, any form. Type both; click where they cross.", ["2x+3y=12", "x-y=1"], "<p>Read the intersection: (3, 2). No elimination needed. Nonlinear systems work the same way: count the crossings to answer \"how many solutions.\"</p>")}
{tactic(3, "Graph both sides", "When an equation has x on both sides or looks ugly, graph y = left side and y = right side separately. The x-values where they cross are the solutions.", ["y=2^x", "y=x+3"], "")}
{steps("Desmos workflow for a system", [
 ("a|Type equation 1|s  b|Type equation 2|v", "Enter each equation exactly as given. No rearranging."),
 ("c|Zoom out (–)|e", "If you see no crossing, zoom out. It may be off-screen."),
 ("d|Click the gray point|g", "Desmos labels it with exact-looking coordinates, like (3, 2)."),
])}
''', pill=("d", "1"))

T2 = topic("regression", "Regressions: the tactic most students don't know", f'''
<p>Whenever a question gives you a <b>table of values</b> or <b>a few points</b> and asks for an equation, a constant, or a prediction, let Desmos find the equation with a regression. Type a table (click + → table), then a regression with a tilde <b>~</b>:</p>
{table(["Model", "Type in Desmos", "Use when"], [["Linear", dz("y_1 ~ mx_1+b"), "constant differences"], ["Quadratic", dz("y_1 ~ ax_1^2+bx_1+c"), "parabola, \"quadratic function f\""], ["Exponential", dz("y_1 ~ ab^{x_1}", "y_1 ~ ab^{x_1}"), "constant ratios, growth/decay"]])}
{reg([[0, 5], [1, 15], [2, 45], [3, 135]], "exp", "Regression lab", "This is what Desmos computes behind y₁ ~ … . Try the presets, edit the table, or drag points.", [
  {"name": "Exponential table", "points": [[0, 5], [1, 15], [2, 45], [3, 135]], "model": "exp"},
  {"name": "Quadratic through 3 points", "points": [[1, 2], [2, 7], [3, 14]], "model": "quad"},
  {"name": "Linear table", "points": [[2, 11], [5, 20], [9, 32]], "model": "lin"},
  {"name": "Scatterplot (best fit)", "points": [[1, 28], [2, 31], [3, 42], [4, 46], [5, 53], [6, 62], [7, 66]], "model": "lin"}])}
{worked("A quadratic function f has f(1) = 2, f(2) = 7, f(3) = 14. What is f(5)?", f"Table: x₁ = 1, 2, 3 and y₁ = 2, 7, 14. Type {dz('y_1 ~ ax_1^2+bx_1+c')} → a = 1, b = 2, c = −1, r² = 1. Then type {dz('5^2+2*5-1')} → <b>34</b>. (Or define f(x) = x² + 2x − 1 and type f(5).)")}
{worked("x: 0, 1, 2, 3; y: 5, 15, 45, 135. Which equation models this?", f"{dz('y_1 ~ ab^{x_1}', 'y_1 ~ ab^{x_1}')} gives a = 5, b = 3: y = 5(3)ˣ.")}
{box("tip", "r² = 1 means exact", "If r² = 1, the equation passes through every point: it's THE equation, not an estimate. If r² is less than 1, it's a line/curve of best fit (good for scatterplot questions).")}
''', pill=("d", "2"))

T3 = topic("more", "More tactics", f'''
{tactic(4, "Sliders for unknown constants", "\"For what value of k…\" questions. Type the equation with a letter; Desmos offers a slider. Drag until the condition happens (one solution, lines parallel, curve through a point).", ["y=x^2-6x+k", "y=0"], "<p>Drag k until the parabola just touches y = 0: k = 9. Confirm with algebra (b² − 4ac = 0) if the slider lands between values.</p>")}
{tactic(5, "Function notation", "Define the function once, then evaluate or compose by typing.", ["f(x)=3x^2-2", "f(4)", "g(x)=x+1", "f(g(2))"])}
{tactic(6, "Vertex, zeros and max/min", "Click the curve: Desmos shows gray points at x-intercepts, y-intercept, and the max/min.", ["y=-2x^2+12x-7"], "<p>Vertex (3, 11): the maximum value is 11 at x = 3.</p>")}
{tactic(7, "Statistics", "Mean, median and standard deviation of a list.", ["mean([12,15,15,18,40])", "median([12,15,15,18,40])", "stdev([2,4,4,4,5,5,7,9])"], "<p>Use this to compare spreads of two data sets quickly.</p>")}
{tactic(8, "Equivalent expressions", "Graph the original and each answer choice. The one that lies exactly on top is equivalent.", ["y=(2x-3)^2-4x", "y=4x^2-16x+9"])}
{tactic(9, "Inequalities and points", "Type the inequality to shade the solution region; type the point to see if it's inside.", ["y>2x-1", "y<-x+5", "(1,2)"])}
{tactic(10, "Circles", "Type the circle in any form. Hover or click the top/bottom/left/right points to read the center and radius.", ["x^2+6x+y^2-4y=12"], "<p>Leftmost (−8, 2), rightmost (2, 2): center (−3, 2), radius 5.</p>")}
{tactic(11, "Restrict a domain", "Graph only part of a function with curly braces.", ["y=x^2\\{x>0\\}"])}
{tactic(12, "Trig in degrees", "SAT Desmos starts in radians. Click the wrench (settings) → Degrees before any trig question with degrees.", ["sin(30)"], "<p>If sin(30) shows −0.988, you're in radians.</p>")}
''', pill=("d", "3"))

CH = [chapter("ch-why", "Why Desmos", "Why", [INTRO]), chapter("ch-solve", "Solve It by Graphing", "Solving", [T1]), chapter("ch-reg", "Regressions", "Regressions", [T2]), chapter("ch-more", "More Tactics", "More", [T3])]
PQ = [
 g("Solve 3x² − 5x − 2 = 0 for the positive solution.", ["2"], "Type 3x^2-5x-2=0. Solutions −1/3 and 2.", "d"),
 g("x + 2y = 10 and 3x − y = 2. What is y?", ["4"], "Type both, click the crossing: (2, 4).", "d"),
 q("How many real solutions does x² − 4x + 7 = 2x − 3 have?", ["0", "1", "2", "Infinitely many"], 0, "Graph both sides: they never cross (x² − 6x + 10 has a negative discriminant).", "d"),
 g("x: 0, 1, 2, 3 and f(x): 4, 10, 16, 22. f is linear. What is f(10)?", ["64"], "y_1 ~ mx_1+b → m = 6, b = 4. f(10) = 64.", "d"),
 g("A quadratic passes through (0, 3), (1, 0) and (2, −1). What is its y-value at x = 4?", ["3"], "Quadratic regression: a = 1, b = −4, c = 3. 16 − 16 + 3.", "d"),
 q("x: 0, 1, 2, 3; y: 800, 400, 200, 100. Which models y?", ["y = 800(0.5)ˣ", "y = 800 − 400x", "y = 800(2)ˣ", "y = 400x"], 0, "Exponential regression: a = 800, b = 0.5.", "d"),
 g("f(x) = −x² + 8x − 5. What is the maximum value of f?", ["11"], "Click the vertex: (4, 11).", "d"),
 g("Mean of 3, 8, 8, 10, 21?", ["10"], "mean([3,8,8,10,21]).", "d"),
 q("Which is equivalent to (x + 3)² − 2(x + 3)?", ["(x + 3)(x + 1)", "x² + 4x + 3 + x", "(x + 1)²", "x² + 9 − 2x"], 0, "Graph the original and each choice; (x + 3)(x + 1) overlaps it. Algebra: (x + 3)(x + 3 − 2).", "d"),
 g("y = x² − 10x + k touches the x-axis at exactly one point. k = ?", ["25"], "Slider on k until the vertex sits on the axis.", "d"),
 q("The circle x² − 8x + y² + 2y = 8 has center…", ["(4, −1)", "(−4, 1)", "(8, −2)", "(4, 1)"], 0, "Graph it and read the middle, or complete the square.", "d"),
 q("In which situation is Desmos LEAST helpful?", ["Solving 4x = 20", "Finding where two curves meet", "Fitting an equation to a table", "Finding the vertex of a parabola"], 0, "Too simple; do it mentally.", "s"),
]
CHAL = [
 g("f is quadratic with f(−1) = 6, f(1) = 2 and f(2) = 3. What is f(4)?", ["11"], "Quadratic regression: a = 1, b = −2, c = 3. f(4) = 16 − 8 + 3 = 11.", "d"),
 g("y = 2x + c and y = x² − 4x + 10 intersect at exactly one point. c = ?", ["1"], "Slider on c until the line is tangent; algebra: x² − 6x + (10 − c) = 0 → 36 = 4(10 − c).", "d"),
 q("A table shows t: 0, 2, 4 and P: 300, 432, 622.08. Which best models P?", ["P = 300(1.2)ᵗ", "P = 300(1.44)ᵗ", "P = 300 + 66t", "P = 300(2)ᵗ"], 0, "y_1 ~ ab^{x_1} gives b = 1.2 (1.2² = 1.44 per 2 steps).", "d"),
 g("x² + y² = 25 and y = x + 1 intersect at two points. What is the larger x-value?", ["3"], "Graph both; click intersections: (3, 4) and (−4, −3).", "d"),
 g("√(2x + 7) = x + 2. What is x?", ["1"], "Type the equation: Desmos shows only the valid solution x = 1 (x = −3 is extraneous).", "d"),
 q("Data A: 10, 20, 30, 40, 50. Data B: 28, 29, 30, 31, 32. Which has the larger standard deviation?", ["A", "B", "Equal", "Can't tell"], 0, "Same mean, but A is far more spread out: stdev([10,20,30,40,50]) ≈ 15.8 vs about 1.6.", "d"),
]
EX = [
 g("2x² + 5x − 12 = 0. Positive solution?", ["1.5", "3/2"], "Type it: −4 and 1.5.", "d"),
 g("4x − y = 7 and x + 2y = 4. What is x?", ["2"], "Intersection (2, 1).", "d"),
 q("x: 1, 2, 3, 4; y: 3, 12, 48, 192. Which model?", ["y = 0.75(4)ˣ", "y = 3(4)ˣ", "y = 9x − 6", "y = 4x²"], 0, "Exponential regression: a = 0.75, b = 4.", "d"),
 g("A line passes through (2, 11) and (6, 27). What is its y-intercept?", ["3"], "Linear regression on the two points: m = 4, b = 3.", "d"),
 g("f(x) = x² − 6x + 13. Minimum value?", ["4"], "Vertex (3, 4).", "d"),
 q("How many times do y = x³ − 3x and y = 1 intersect?", ["3", "1", "2", "0"], 0, "Graph both; count crossings.", "d"),
 g("median of 7, 1, 9, 4, 12, 3?", ["5.5", "11/2"], "median([7,1,9,4,12,3]).", "d"),
 g("f(x) = 2x + 1, g(x) = x². f(g(3)) = ?", ["19"], "Define both; type f(g(3)).", "d"),
 q("For what k do 3x + 2y = 6 and 6x + ky = 10 have no solution?", ["4", "2", "6", "−4"], 0, "Slider on k: the lines are parallel at k = 4.", "d"),
 g("A quadratic has zeros 1 and 7 and passes through (0, 14). What is its value at x = 4?", ["-18"], "Regression on (1,0), (7,0), (0,14): y = 2x² − 16x + 14. At 4: 32 − 64 + 14 = −18.", "d"),
]
build(C, "sat-desmos", L, 0, "Desmos and Regression Tactics", 'Desmos <span class="hl">tactics</span>', "Solve equations and systems by graphing, regressions from tables, sliders, statistics and more, with Desmos built right into the page.", "SAT Desmos calculator tactics: solving by graphing, regressions, sliders, statistics, with an embedded Desmos calculator.", CH, PQ, CHAL, EX, TAGS, OUT, minutes=12, exam_name="Desmos set", rules=["10 questions in 12 minutes.", "Use the Desmos button: these are all faster with it.", "Grid-ins: type a number or fraction."])
