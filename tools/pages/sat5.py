from tp_common import *
C = "sat"; L = "SAT"; OUT = "../../courses/sat/sat-5.html"
TAGS = {"q": "Quadratics", "e": "Exponentials", "x": "Expressions", "n": "Nonlinear functions"}

QUAD = topic("quad", "Quadratics", f'''
<p>Three forms, three jobs. Know which feature each one shows instantly.</p>
{table(["Form", "Shows"], [["y = a(x − h)² + k", "vertex (h, k): the max or min"], ["y = a(x − r)(x − s)", "x-intercepts r and s; vertex x is halfway: (r + s)/2"], ["y = ax² + bx + c", "y-intercept c; vertex x = −b/(2a); sum of roots −b/a; product c/a"]])}
{lab(title="Quadratic lab", sub="y = a(x − r)(x − s). The vertex sits halfway between the zeros.", x=[-6, 8], y=[-12, 12], gx=1, gy=2, params={"a": [-2, 2, 0.25, 1, "a"], "r": [-5, 5, 0.5, -1, "r"], "s": [-5, 7, 0.5, 4, "s"]}, fns=[fn("a*(x-r)*(x-s)", "y = a(x − r)(x − s)")], dots=[["(r+s)/2", "a*((r+s)/2-r)*((r+s)/2-s)", "vertex", "#EA580C"], ["r", "0", "r", "#059669"], ["s", "0", "s", "#059669"]], read=[["vertex x = ", "(r+s)/2"], ["c (y-intercept) = ", "a*r*s"]])}
{mini(("Discriminant", "b² − 4ac &gt; 0: two real solutions; = 0: one; &lt; 0: none. Questions like \"for what c does the equation have exactly one solution\" are discriminant questions."), ("Desmos move", "Graph the quadratic and click the vertex and zeros. Graph y = (your expression) and y = (other side) to solve any equation."))}
{worked("x² − 6x + c = 0 has exactly one real solution. Find c.", "b² − 4ac = 36 − 4c = 0 → c = 9.")}
''', pill=("q", "5.1"))

EXPO = topic("expo", "Exponential functions", f'''
<p>f(x) = a·bˣ: a is the starting value; b is the growth factor. Growth by r%: b = 1 + r/100. Decay by r%: b = 1 − r/100.</p>
{lab(title="Growth vs decay", sub="y = a·bˣ. b > 1 grows, 0 < b < 1 decays.", x=[0, 10], y=[0, 200], gx=1, gy=20, params={"b": [0.5, 1.6, 0.02, 1.2, "b"], "a": [10, 100, 5, 30, "a"]}, fns=[fn("a*b^x", "y = a·bˣ")], read=[["percent change per step: ", "(b-1)*100"]], table={"x": [0, 1, 2, 3, 4], "rows": [["y", "a*b^x"]], "diff": "ratio"})}
{table(["Statement", "Model"], [["increases 8% per year", "P(t) = P₀(1.08)ᵗ"], ["decreases 30% per year", "V(t) = V₀(0.7)ᵗ"], ["doubles every 6 hours", "N(t) = N₀·2^(t/6)"], ["halves every 3 days", "A(t) = A₀(½)^(t/3)"]])}
{box("trap", "Linear vs exponential", "\"Increases by 5 each year\" is linear (add). \"Increases by 5% each year\" is exponential (multiply).")}
''', pill=("e", "5.2"))

EXPR = topic("expr", "Equivalent expressions and polynomials", f'''
{steps("Which is equivalent to (2x − 3)² − 4x?", [
 ("a|(2x − 3)²|v  b|− 4x|s", "Expand the square: (a − b)² = a² − 2ab + b²."),
 ("c|4x² − 12x + 9|v  b|− 4x|s", "(2x)² − 2(2x)(3) + 3²."),
 ("d|4x² − 16x + 9|g", "Combine −12x − 4x."),
])}
{mini(("Fast check", "Plug x = 2 into the original and each choice. Equivalent expressions give the same number."), ("Factor patterns", "a² − b² = (a − b)(a + b); a² ± 2ab + b² = (a ± b)²."))}
<p><b>Rational expressions & radicals:</b> x^(1/2) = √x, x^(m/n) = (ⁿ√x)^m, x^(−n) = 1/xⁿ. To solve √(x + 3) = x − 3, square both sides, then <b>check</b> for extraneous solutions.</p>
{steps("Solve √(x + 3) = x − 3", [
 ("a|√(x + 3)|v  b|=  c|x − 3|s", "Square both sides."),
 ("d|x + 3|v  b|=  e|x² − 6x + 9|s", "(x − 3)² = x² − 6x + 9."),
 ("f|0 = x² − 7x + 6|e", "Move everything to one side."),
 ("g|0 = (x − 1)(x − 6)|e", "Factor."),
 ("h|x = 6|g  i|x = 1 ✗|x", "Check: x = 1 gives √4 = −2, false. Only x = 6."),
])}
''', pill=("x", "5.3"))

NL = topic("nonlinear", "Function notation, transformations and nonlinear systems", f'''
<p>f(x + 2) shifts the graph <b>left</b> 2; f(x) + 2 shifts it <b>up</b> 2. For f(g(x)), work from the inside out.</p>
{lab(title="Line meets parabola", sub="A nonlinear system: y = x² − 2 and y = m·x + b. Count the intersections.", x=[-5, 5], y=[-4, 10], gx=1, gy=1, params={"m": [-4, 4, 0.5, 1, "m"], "b": [-5, 6, 0.5, 0, "b"]}, fns=[fn("x^2-2", "y = x² − 2"), fn("m*x+b", "y = mx + b")], read=[["discriminant m² + 4(b + 2) = ", "m^2+4*(b+2)"]])}
<p>Setting x² − 2 = mx + b gives x² − mx − (b + 2) = 0. Positive discriminant → 2 crossing points, zero → tangent (1), negative → none.</p>
''', pill=("n", "5.4"))

CH = [chapter("ch-quad", "Quadratics", "Quadratics", [QUAD]), chapter("ch-expo", "Exponentials", "Exponentials", [EXPO]), chapter("ch-expr", "Expressions and Functions", "Expressions", [EXPR, NL])]
close(36 - 4 * 9, 0)
PQ = [
 q("Vertex of y = 2(x − 3)² + 5?", ["(3, 5)", "(−3, 5)", "(3, −5)", "(2, 5)"], 0, "Vertex form.", "q"),
 g("The zeros of y = (x − 2)(x + 8) are 2 and −8. What is the x-coordinate of the vertex?", ["-3"], "Halfway: (2 + (−8))/2.", "q"),
 q("How many real solutions does x² + 4x + 7 = 0 have?", ["0", "1", "2", "Infinitely many"], 0, "16 − 28 < 0.", "q"),
 g("x² − 10x + c = 0 has exactly one solution. c = ?", ["25"], "100 − 4c = 0.", "q"),
 q("A town's population is 12,000 and grows 3% per year. Which models it after t years?", ["12000(1.03)ᵗ", "12000(0.03)ᵗ", "12000 + 0.03t", "12000(1.3)ᵗ"], 0, "Growth factor 1.03.", "e"),
 q("A car worth $25,000 loses 15% of its value each year. Value after 2 years?", ["$18,062.50", "$17,500", "$21,250", "$18,750"], 0, "25000 × 0.85².", "e"),
 q("f(x) = 5(2)ˣ. What is f(3)?", ["40", "30", "1000", "15"], 0, "5 × 8.", "e"),
 q("Which is equivalent to (x + 4)(x − 4)?", ["x² − 16", "x² + 16", "x² − 8x − 16", "x² − 8"], 0, "Difference of squares.", "x"),
 q("Which is equivalent to x^(3/2)?", ["x√x", "√(x³)/x", "3√x/2", "x³/√x²"], 0, "x · x^(1/2).", "x"),
 q("Which is equivalent to (3x² − 12)/(x − 2), for x ≠ 2?", ["3(x + 2)", "3x + 2", "3(x − 2)", "3x² − 6"], 0, "3(x − 2)(x + 2)/(x − 2).", "x"),
 g("f(x) = x² − 3x. What is f(−2)?", ["10"], "4 + 6.", "n"),
 q("The graph of y = f(x − 3) is the graph of f shifted…", ["right 3", "left 3", "up 3", "down 3"], 0, "Inside is opposite.", "n"),
 q("How many points do y = x² and y = 4 intersect at?", ["2", "1", "0", "4"], 0, "x = ±2.", "n"),
 g("Solve for the positive solution: 2x² = 50.", ["5"], "x² = 25.", "q"),
]
CHAL = [
 g("y = x² − 4x + k and y = 2x − 5 intersect at exactly one point. What is k?", ["4"], "x² − 6x + (k + 5) = 0 needs 36 − 4(k + 5) = 0 → k = 4.", "n"),
 q("f(x) = a(x − 1)(x − 7) has a maximum value of 18. What is a?", ["−2", "2", "−1/2", "−18"], 0, "Vertex at x = 4: a(3)(−3) = −9a = 18 → a = −2.", "q"),
 q("A bacteria count doubles every 20 minutes from 500. Which gives the count after h hours?", ["500·2^(3h)", "500·2^(h/20)", "500·2^(20h)", "500·3^(2h)"], 0, "3 doublings per hour.", "e"),
 g("If x > 0 and x² − 5x − 14 = 0, what is x?", ["7"], "(x − 7)(x + 2) = 0.", "q"),
 q("Which expression is equivalent to 9x⁴ − 25?", ["(3x² − 5)(3x² + 5)", "(9x² − 5)(x² + 5)", "(3x − 5)²(3x + 5)²", "(3x² − 5)²"], 0, "Difference of squares with (3x²)².", "x"),
 q("The function p(t) = 800(0.9)^(t/4) models a quantity t years from now. Which is true?", ["It decreases by 10% every 4 years", "It decreases by 90% each year", "It decreases by 10% each year", "It increases by 10% every 4 years"], 0, "The exponent t/4 means one factor of 0.9 per 4 years.", "e"),
]
close(25000 * .85 ** 2, 18062.5)
EX = [
 q("Solutions of x² − 5x + 6 = 0?", ["2 and 3", "−2 and −3", "1 and 6", "−1 and 6"], 0, "(x − 2)(x − 3).", "q"),
 g("What is the y-intercept of y = 3x² − 2x + 7?", ["7"], "x = 0.", "q"),
 q("Minimum value of y = (x + 1)² − 9?", ["−9", "−1", "1", "9"], 0, "Vertex y.", "q"),
 q("Which equation has no real solutions?", ["x² + 9 = 0", "x² − 9 = 0", "x² − 9x = 0", "x² = 9x"], 0, "x² = −9.", "q"),
 q("An investment of $1,000 earns 5% compounded yearly. Value after 3 years?", ["$1,157.63", "$1,150.00", "$1,050.00", "$1,500.00"], 0, "1000 × 1.05³.", "e"),
 q("Which describes y = 300(0.95)ˣ?", ["Decreases 5% per unit of x", "Increases 95% per unit", "Decreases 95% per unit", "Increases 5% per unit"], 0, "0.95 = 1 − 0.05.", "e"),
 g("f(x) = 2ˣ + 1. What is f(4)?", ["17"], "16 + 1.", "e"),
 q("Which is equivalent to (2x + 1)²?", ["4x² + 4x + 1", "4x² + 1", "2x² + 4x + 1", "4x² + 2x + 1"], 0, "Square the binomial.", "x"),
 q("Which is equivalent to 1/x⁻³?", ["x³", "−x³", "1/x³", "3x"], 0, "Negative exponent flips.", "x"),
 g("If x > 0 and √(2x + 1) = 5, what is x?", ["12"], "2x + 1 = 25.", "x"),
 q("If f(x) = x + 3 and g(x) = x², f(g(2)) = ?", ["7", "25", "10", "8"], 0, "g(2) = 4, f(4) = 7.", "n"),
 q("Graph of y = −f(x) is f reflected over the…", ["x-axis", "y-axis", "line y = x", "origin"], 0, "Outputs flip sign.", "n"),
 q("y = x² + 1 and y = 1. How many intersection points?", ["1", "0", "2", "3"], 0, "x² = 0.", "n"),
 g("The product of the solutions of 2x² − 7x − 15 = 0 is…", ["-7.5", "-15/2"], "c/a = −15/2.", "q"),
 q("Which equation could represent a parabola that opens down with vertex (2, 4)?", ["y = −(x − 2)² + 4", "y = (x − 2)² + 4", "y = −(x + 2)² + 4", "y = −(x − 4)² + 2"], 0, "a < 0, h = 2, k = 4.", "q"),
]
close(1000 * 1.05 ** 3, 1157.625)
build(C, "sat-5", L, 5, "Math: Advanced Math", 'Advanced math, <span class="hl">simplified</span>', "Quadratics, exponential growth and decay, equivalent expressions, radicals and nonlinear systems.", "SAT Math Advanced Math domain: quadratics, exponentials, equivalent expressions and nonlinear functions with interactive graphs.", CH, PQ, CHAL, EX, TAGS, OUT, minutes=20, exam_name="Advanced Math set")
