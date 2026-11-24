from tp_common import *
C = "sat"; L = "SAT"; OUT = "../../courses/sat/sat-4.html"
TAGS = {"l": "Linear equations", "f": "Linear functions", "s": "Systems", "q": "Inequalities & models"}

LIN = topic("lin-eq", "Linear equations in one variable", f'''
<p>Isolate the variable. But on the SAT, often you don't need the variable at all: look for the expression they ask about.</p>
{steps("If 4x − 6 = 18, what is 2x − 3?", [
 ("a|4x − 6|v  b|=  c|18|n", "Notice 4x − 6 is exactly 2 × (2x − 3)."),
 ("d|2(2x − 3)|v  b|=  c|18|n", "Factor out the 2."),
 ("e|2x − 3|g  b|=  f|9|g", "Divide by 2. Done, without ever finding x."),
])}
{mini(("No solution", "Same x-coefficient, different constants: 3x + 2 = 3x + 5 is impossible."), ("Infinitely many", "Both sides identical after simplifying: 2(x + 1) = 2x + 2."))}
{worked("For what value of k does 5x + k = 5x − 2 have infinitely many solutions? For what values does it have none?", "Infinitely many when k = −2 (sides identical). No solution for any other k.")}
''', pill=("l", "4.1"))

FN = topic("lin-fn", "Linear functions and graphs", f'''
<p>f(x) = mx + b: m is the rate of change (slope), b is the starting value (y-intercept). Word problems love asking what m or b <b>means in context</b>.</p>
{lab(title="Context lab: phone plan", sub="C(m) = r·m + f: monthly fee f plus r dollars per GB of data m.", x=[0, 20], y=[0, 120], gx=2, gy=10, params={"r": [0, 6, 0.5, 3.5, "r ($/GB)"], "f": [0, 60, 5, 25, "f ($)"]}, fns=[fn("r*x+f", "C(m) = r·m + f")], dots=[["0", "f", "fee ${f}", "#EA580C"], ["10", "r*10+f", "10 GB: ${r*10+f}", "#2563EB"]], read=[["slope = ", "r"], ["intercept = ", "f"]])}
{worked("C(m) = 3.5m + 25. What does 3.5 mean?", "Each additional gigabyte of data adds $3.50 to the monthly cost. (25 is the cost with zero data.)")}
<p>From two points: slope = Δy/Δx. Parallel lines share a slope; perpendicular slopes multiply to −1. From a table: check the slope between any two rows.</p>
''', pill=("f", "4.2"))

SYS = topic("systems", "Systems of linear equations", f'''
{steps("Solve: 2x + 3y = 12 and x − y = 1", [
 ("a|2x + 3y = 12|s  b|x − y = 1|v", "Multiply the second equation by 3 so the y's cancel."),
 ("a|2x + 3y = 12|s  c|3x − 3y = 3|v", "Now add the equations."),
 ("d|5x = 15|e", "y's are gone."),
 ("e|x = 3|g  f|y = 2|g", "Then 3 − y = 1 → y = 2. Desmos check: graph both lines and click the crossing point."),
])}
{lab(title="How many solutions?", sub="Line 1: y = 2x + 1. Line 2: y = m·x + b. Make them parallel (no solution) or identical (infinite).", x=[-6, 6], y=[-8, 10], gx=1, gy=2, params={"m": [-3, 3, 0.5, -1, "m"], "b": [-4, 4, 0.5, 4, "b"]}, fns=[fn("2*x+1", "y = 2x + 1"), fn("m*x+b", "y = mx + b")], read=[["slopes equal?", "m-2"]])}
{table(["Equations look like…", "Solutions"], [["different slopes", "exactly one"], ["same slope, different intercept", "none (parallel)"], ["one is a multiple of the other", "infinitely many (same line)"]])}
{worked("For what value of c does the system 3x + 2y = 7 and 6x + cy = 10 have no solution?", "No solution means parallel: the left sides must be proportional, 6/3 = c/2 → c = 4 (and 10 ≠ 14, so not the same line).")}
''', pill=("s", "4.3"))

INEQ = topic("ineq", "Inequalities and linear models", f'''
<p>Same moves as equations, but <b>flip the sign</b> when you multiply or divide by a negative. Word cues: \"at least\" ≥, \"at most\" / \"no more than\" ≤, \"more than\" &gt;.</p>
{worked("A van can carry at most 1,200 kg. The driver weighs 80 kg and each box weighs 35 kg. What's the most boxes it can carry?", "80 + 35b ≤ 1200 → 35b ≤ 1120 → b ≤ 32. So 32 boxes.")}
{lab(title="Inequality region", sub="y ≤ m·x + b is everything on or below the line. Is the orange point a solution?", x=[-6, 6], y=[-6, 6], gx=1, gy=1, params={"m": [-3, 3, 0.5, 0.5, "m"], "b": [-4, 4, 0.5, 1, "b"]}, fns=[fn("m*x+b", "y = mx + b")], dots=[["2", "1", "(2, 1)", "#EA580C"]], read=[["is (2, 1) a solution? m·2 + b − 1 =", "m*2+b-1"]])}
<p>If that readout is ≥ 0, the point (2, 1) satisfies y ≤ mx + b.</p>
''', pill=("q", "4.4"))

CH = [chapter("ch-eq", "Equations", "Equations", [LIN]), chapter("ch-fn", "Functions", "Functions", [FN]), chapter("ch-sys", "Systems and Inequalities", "Systems", [SYS, INEQ])]

PQ = [
 q("If 3(x − 2) = 15, what is x?", ["7", "5", "3", "9"], 0, "x − 2 = 5.", "l"),
 g("If 6y + 9 = 45, what is 2y + 3?", ["15"], "Divide everything by 3.", "l"),
 q("How many solutions does 4(x + 1) = 4x + 7 have?", ["None", "One", "Two", "Infinitely many"], 0, "4x + 4 = 4x + 7 is impossible.", "l"),
 q("The line through (1, 4) and (3, 10) has slope…", ["3", "6", "1/3", "2"], 0, "6/2.", "f"),
 q("A taxi charges F(m) = 2.5m + 4 dollars for m miles. What does 4 represent?", ["The charge before any miles are driven", "The charge per mile", "The total for 4 miles", "The number of miles"], 0, "The intercept is the starting fee.", "f"),
 q("Which line is parallel to y = −3x + 2?", ["y = −3x − 5", "y = 3x + 2", "y = (1/3)x", "y = −(1/3)x + 2"], 0, "Same slope.", "f"),
 g("f(x) = 7x − 4. What is f(3)?", ["17"], "21 − 4.", "f"),
 q("Solve: x + y = 10, x − y = 2. What is x?", ["6", "4", "8", "5"], 0, "Add: 2x = 12.", "s"),
 g("If 2x + y = 11 and x + y = 7, what is x?", ["4"], "Subtract: x = 4.", "s"),
 q("For what value of k does 2x + 5y = 3 and 4x + ky = 9 have no solution?", ["10", "5", "6", "2.5"], 0, "4/2 = k/5 → k = 10; constants 3·2 ≠ 9 so not identical.", "s"),
 q("Which describes the solutions of −2x + 5 > 11?", ["x < −3", "x > −3", "x < 3", "x > 8"], 0, "−2x > 6, flip: x < −3.", "q"),
 q("Tickets cost $12 for adults and $7 for students. A group spends at most $150 with 6 adults. What's the max number of students?", ["11", "12", "10", "21"], 0, "72 + 7s ≤ 150 → s ≤ 11.14.", "q"),
 q("A plant is 5 cm tall and grows 1.5 cm per week. Which gives its height after w weeks?", ["h = 1.5w + 5", "h = 5w + 1.5", "h = 6.5w", "h = 1.5(w + 5)"], 0, "Start + rate × time.", "q"),
 g("Line ℓ is perpendicular to y = (2/5)x − 1. What is the slope of ℓ?", ["-5/2", "-2.5"], "Negative reciprocal.", "f"),
]
CHAL = [
 g("The system ax + 3y = 12 and 2x + y = 4 has infinitely many solutions. What is a?", ["6"], "Multiply the second equation by 3: 6x + 3y = 12. For the same line, a must be 6.", "s"),
 q("A gym charges a joining fee plus a monthly fee. After 4 months a member has paid $210; after 10 months, $435. What is the joining fee?", ["$60", "$37.50", "$22.50", "$90"], 0, "Monthly = 225/6 = 37.5. Fee = 210 − 150 = 60.", "q"),
 g("If 3a − 2b = 7 and a + 2b = 9, what is a + b?", ["6.5", "13/2"], "Add the equations: 4a = 16, so a = 4. Then 4 + 2b = 9 → b = 2.5. a + b = 6.5.", "s"),
 q("The graph of y = f(x) is a line with f(2) = 5 and f(6) = −3. What is f(0)?", ["9", "1", "7", "−7"], 0, "Slope −2; f(0) = 5 + 4 = 9.", "f"),
 q("Which point satisfies both y > 2x − 1 and y < −x + 5?", ["(1, 2)", "(3, 1)", "(0, −2)", "(2, 4)"], 0, "(1, 2): 2 > 1 ✓ and 2 < 4 ✓.", "q"),
 g("In the equation (x/3) + (x/6) = 5, what is x?", ["10"], "Multiply by 6: 2x + x = 30.", "l"),
]
close(225 / 6, 37.5)
EX = [
 q("If 5x − 8 = 2x + 7, what is x?", ["5", "−5", "1/3", "3"], 0, "3x = 15.", "l"),
 g("If x/2 + 4 = 10, what is x?", ["12"], "x/2 = 6.", "l"),
 q("Slope of the line 3x − 4y = 8?", ["3/4", "−3/4", "4/3", "−2"], 0, "y = (3/4)x − 2.", "f"),
 q("A pool has 800 L and drains 25 L per minute. Which models the volume V after t minutes?", ["V = 800 − 25t", "V = 25t − 800", "V = 800t − 25", "V = 775t"], 0, "Starting amount minus rate × time.", "q"),
 g("f(x) = −2x + 9. For what x is f(x) = 1?", ["4"], "−2x = −8.", "f"),
 q("Solve: y = 3x and 2x + y = 20. What is y?", ["12", "4", "6", "15"], 0, "5x = 20, x = 4, y = 12.", "s"),
 q("Which system has no solution?", ["y = 2x + 1, y = 2x − 3", "y = 2x + 1, y = −2x + 1", "y = x, y = 2x", "y = 3, x = 3"], 0, "Parallel lines.", "s"),
 q("x ≥ 4 and x < 9 for integers x. How many integers?", ["5", "4", "6", "9"], 0, "4, 5, 6, 7, 8.", "q"),
 q("The line y = mx + 3 passes through (2, 11). What is m?", ["4", "7", "5.5", "3"], 0, "11 = 2m + 3.", "f"),
 g("A line has slope 2 and passes through (3, 1). What is its y-intercept?", ["-5"], "1 = 6 + b.", "f"),
 q("Mia earns $15/hour and $40 in tips per shift. She wants at least $160 from one shift. Minimum hours?", ["8", "10", "11", "12"], 0, "15h + 40 ≥ 160 → h ≥ 8.", "q"),
 q("If 2(3x + 1) = 6x + k has infinitely many solutions, k = ?", ["2", "1", "6", "0"], 0, "6x + 2 = 6x + k.", "l"),
 g("Solve 0.4x + 1.2 = 3.6.", ["6"], "0.4x = 2.4.", "l"),
 q("Which equation describes a line with x-intercept 4 and y-intercept −2?", ["y = (1/2)x − 2", "y = −(1/2)x + 4", "y = 2x − 4", "y = −2x + 4"], 0, "Slope (0 − (−2))/(4 − 0) = 1/2.", "f"),
 q("Pens cost $2 and notebooks $5. Jo buys 8 items for $25. How many notebooks?", ["3", "5", "2", "4"], 0, "p + n = 8, 2p + 5n = 25 → 16 + 3n = 25.", "s"),
]
build(C, "sat-4", L, 4, "Math: Algebra", 'Algebra, <span class="hl">the fast way</span>', "Linear equations, linear functions in context, systems and inequalities, with Desmos shortcuts and grid-ins.", "SAT Math Algebra domain: linear equations, functions, systems and inequalities with interactive graphs and practice.", CH, PQ, CHAL, EX, TAGS, OUT, minutes=20, exam_name="Algebra set")
