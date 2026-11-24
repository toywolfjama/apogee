from math_common import *
L = "Before Precalc"; OUT = "../../courses/math/pre-3.html"

FORMS = topic("q-forms", "Three forms of a quadratic", f'''
<p>A quadratic makes a U-shaped <b>parabola</b>. Each form shows you something different at a glance.</p>
{table(["Form", "Equation", "Read off"], [
 ["Standard", f"{m('y')} = {m('a')}{m('x')}² + {m('bx')} + {m('c')}", f"y-intercept {m('c')}; axis {m('x')} = −{m('b')}/(2{m('a')})"],
 ["Vertex", f"{m('y')} = {m('a')}({m('x')} − {m('h')})² + {m('k')}", f"vertex ({m('h')}, {m('k')})"],
 ["Factored", f"{m('y')} = {m('a')}({m('x')} − {m('r')})({m('x')} − {m('s')})", f"x-intercepts {m('r')} and {m('s')}"],
])}
<p>The sign of {m('a')} decides the direction: {m('a')} &gt; 0 opens up (minimum), {m('a')} &lt; 0 opens down (maximum). Bigger |{m('a')}| means narrower.</p>
{lab(title="Vertex form lab", sub="y = a(x − h)² + k. Animate a to see the parabola flip.", x=[-8, 8], y=[-8, 10], gx=1, gy=1, params={"a": [-3, 3, 0.1, 1, "a"], "h": [-5, 5, 0.5, 1, "h"], "k": [-6, 6, 0.5, -3, "k"]}, fns=[fn("a*(x-h)^2+k", "y = a(x − h)² + k")], dots=[["h", "k", "vertex ({h}, {k})", "#EA580C"], ["h+sqrt(-k/a)", "0", "", "#059669"], ["h-sqrt(-k/a)", "0", "", "#059669"]], read=[["zeros: h ± √(−k/a) =", "h-sqrt(-k/a)"], ["and", "h+sqrt(-k/a)"]])}
''', pill=("c", "3.1"))

SOLVE = topic("q-solve", "Solving quadratic equations", f'''
<p>Four ways to solve {m('a')}{m('x')}² + {m('bx')} + {m('c')} = 0. Pick the fastest:</p>
<ol class="steps"><li><b>Factor</b> and use the zero-product rule: if AB = 0, then A = 0 or B = 0.</li>
<li><b>Square roots</b> when there's no {m('x')} term: {m('x')}² = 49 → {m('x')} = ±7.</li>
<li><b>Complete the square</b> (this is how you get vertex form).</li>
<li><b>Quadratic formula</b> always works: {m('x')} = (−{m('b')} ± √({m('b')}² − 4{m('ac')})) / (2{m('a')}).</li></ol>
{steps("Complete the square: x² + 6x + 2 = 0", [
 ("a|x² + 6x|s  b|+ 2|n  c|= 0", "Move the constant to the other side."),
 ("a|x² + 6x|s  c|=  d|−2|n", "Half of 6 is 3; 3² = 9. Add 9 to both sides."),
 ("a|x² + 6x|s  e|+ 9|e  c|=  d|−2|n  f|+ 9|e", "Now the left side is a perfect square."),
 ("g|(x + 3)²|v  c|=  h|7|n", "x² + 6x + 9 = (x + 3)²."),
 ("i|x + 3|v  c|=  j|±√7|e", "Square root both sides. Don't forget ±."),
 ("k|x|g  c|=  l|−3 ± √7|g", "x = −3 ± √7 ≈ −0.35 or −5.65."),
])}
{eq("x = (−b ± √(b² − 4ac)) / 2a")}
{worked(f"Solve 2{m('x')}² − 3{m('x')} − 5 = 0.", f"{m('a')} = 2, {m('b')} = −3, {m('c')} = −5. Discriminant 9 + 40 = 49. {m('x')} = (3 ± 7)/4 → {m('x')} = 5/2 or {m('x')} = −1.")}
''', pill=("p", "3.2"))

DISC = topic("discriminant", "The discriminant", f'''
<p>The part under the root, {m('D')} = {m('b')}² − 4{m('ac')}, tells you how many real solutions there are before you solve.</p>
{table(["D", "Real solutions", "Graph"], [["D &gt; 0", "2", "crosses the x-axis twice"], ["D = 0", "1 (double)", "touches the x-axis at the vertex"], ["D &lt; 0", "0 (two complex)", "misses the x-axis"]])}
{lab(title="Slide c and watch D", sub="y = x² + bx + c. When D hits 0 the parabola just kisses the axis.", x=[-8, 8], y=[-8, 10], gx=1, gy=1, params={"c": [-6, 8, 0.25, 2, "c"], "b": [-6, 6, 0.5, -3, "b"]}, fns=[fn("x^2+b*x+c", "y = x² + bx + c")], read=[["D = b² − 4c =", "b^2-4*c"]], dots=[["(-b+sqrt(b^2-4*c))/2", "0", "", "#059669"], ["(-b-sqrt(b^2-4*c))/2", "0", "", "#059669"]])}
{box("tip", "Complex numbers", f"When D &lt; 0 the solutions use {m('i')} = √−1. For example {m('x')}² + 4 = 0 → {m('x')} = ±2{m('i')}. You'll see these again in precalc.")}
''', pill=("c", "3.3"))

APPS = topic("q-apps", "Quadratics in the real world", f'''
<p>Projectile height: {m('h')}({m('t')}) = −16{m('t')}² + {m('v')}₀{m('t')} + {m('h')}₀ (feet), or −4.9{m('t')}² + … in meters. The vertex is the max height; the positive zero is when it lands.</p>
{lab(title="Launch a ball", sub="h(t) = −16t² + v·t + h₀ in feet.", x=[0, 6], y=[0, 160], gx=0.5, gy=20, params={"v": [16, 96, 4, 64, "v₀"], "h0": [0, 60, 4, 20, "h₀"]}, fns=[fn("-16*x^2+v*x+h0", "h(t)", dom=["0", "(v+sqrt(v^2+64*h0))/32"])], dots=[["v/32", "-16*(v/32)^2+v*v/32+h0", "max {-16*(v/32)^2+v*v/32+h0} ft", "#EA580C"], ["(v+sqrt(v^2+64*h0))/32", "0", "lands t={(v+sqrt(v^2+64*h0))/32}", "#059669"]])}
{worked("A ball is thrown up at 64 ft/s from 20 ft. Max height?", f"Vertex at {m('t')} = −64/(2·−16) = 2 s. {m('h')}(2) = −64 + 128 + 20 = 84 ft.")}
''', pill=("w", "3.4"))

SUM = topic("summary-pre3", "Unit summary", mini(
 ("Forms", "Standard (c, axis −b/2a), vertex (h, k), factored (zeros)."),
 ("Solve", "Factor · square roots · complete the square · quadratic formula."),
 ("Discriminant", "b² − 4ac: positive → 2, zero → 1, negative → 0 real solutions."),
 ("Vertex", "x = −b/(2a). Plug back in for the max or min value."),
))
CH = [chapter("ch-forms", "Parabolas", "Parabolas", [FORMS]), chapter("ch-solve", "Solving Quadratics", "Solving", [SOLVE, DISC]), chapter("ch-apps", "Applications", "Applications", [APPS, SUM])]
close(-16 * 4 + 128 + 20, 84)
PQ = [
 q("Vertex of y = (x − 4)² + 1?", ["(4, 1)", "(−4, 1)", "(1, 4)", "(4, −1)"], 0, "Vertex form a(x − h)² + k.", "g"),
 q("Does y = −2x² + 3 open up or down?", ["Down", "Up", "Sideways", "Can't tell"], 0, "a = −2 < 0.", "g"),
 q("Axis of symmetry of y = x² − 8x + 3?", ["x = 4", "x = −4", "x = 8", "x = 3"], 0, "−b/(2a) = 8/2.", "p"),
 q("Solve x² − 7x + 10 = 0.", ["x = 2 or 5", "x = −2 or −5", "x = 10 or 1", "x = 7"], 0, "(x − 2)(x − 5) = 0.", "p"),
 q("Solve x² = 81.", ["x = ±9", "x = 9", "x = 40.5", "x = ±81"], 0, "Two square roots.", "p"),
 q("Solve (x − 3)² = 16.", ["x = 7 or −1", "x = 7", "x = 19", "x = ±4"], 0, "x − 3 = ±4.", "p"),
 q("Discriminant of x² + 2x + 5?", ["−16", "24", "4", "−4"], 0, "4 − 20.", "p"),
 q("How many real solutions does 4x² − 12x + 9 = 0 have?", ["1", "2", "0", "Infinitely many"], 0, "D = 144 − 144 = 0.", "c"),
 q("To complete the square on x² + 10x, add…", ["25", "100", "10", "5"], 0, "(10/2)² = 25.", "p"),
 q("Solve 2x² + x − 6 = 0.", ["x = 3/2 or −2", "x = −3/2 or 2", "x = 3 or −2", "x = 6 or −1"], 0, "(2x − 3)(x + 2) = 0.", "p"),
 q("Write y = x² + 6x + 1 in vertex form.", ["y = (x + 3)² − 8", "y = (x + 3)² + 1", "y = (x − 3)² − 8", "y = (x + 6)² − 35"], 0, "x² + 6x + 9 − 9 + 1.", "p"),
 q("Zeros of y = 3(x + 1)(x − 6)?", ["x = −1 and 6", "x = 1 and −6", "x = 3, −1, 6", "x = −3"], 0, "Factored form shows zeros.", "g"),
 q("h(t) = −16t² + 32t. When does it reach max height?", ["t = 1", "t = 2", "t = 16", "t = 0.5"], 0, "−32/(2·−16) = 1.", "w"),
 q("A parabola touches the x-axis exactly once. Its discriminant is…", ["0", "positive", "negative", "1"], 0, "One repeated root.", "c"),
]
CHAL = [
 q("For which k does x² + kx + 9 = 0 have exactly one solution?", ["k = ±6", "k = 6 only", "k = ±3", "k = 9"], 0, "k² − 36 = 0.", "c"),
 q("Parabola with vertex (2, −3) through (0, 5)?", ["y = 2(x − 2)² − 3", "y = (x − 2)² − 3", "y = 2(x + 2)² − 3", "y = −2(x − 2)² − 3"], 0, "5 = a(4) − 3 → a = 2.", "p"),
 q("A rectangle has perimeter 40. Its largest possible area is…", ["100", "400", "80", "96"], 0, "A = x(20 − x), vertex at x = 10, A = 100.", "w"),
 q("Solve x² − 4x + 13 = 0.", ["x = 2 ± 3i", "x = −2 ± 3i", "x = 2 ± 3", "No solution at all"], 0, "D = 16 − 52 = −36: (4 ± 6i)/2.", "p"),
 q("Sum of the roots of 3x² − 12x + 5 = 0?", ["4", "−4", "5/3", "12"], 0, "Sum of roots = −b/a = 12/3.", "c"),
 q("h(t) = −4.9t² + 19.6t + 2 (m). Max height?", ["21.6 m", "19.6 m", "2 m", "41.2 m"], 0, "t = 2: −19.6 + 39.2 + 2 = 21.6.", "w"),
]
close(-4.9 * 4 + 39.2 + 2, 21.6)
EXQ = [
 q("Vertex of y = −(x + 2)² + 7?", ["(−2, 7)", "(2, 7)", "(−2, −7)", "(7, −2)"], 0, "h = −2, k = 7.", "g"),
 q("y-intercept of y = 2x² − 5x + 4?", ["4", "−5", "2", "0"], 0, "Set x = 0.", "g"),
 q("Solve x² + x − 12 = 0.", ["x = 3 or −4", "x = −3 or 4", "x = 12 or −1", "x = 6 or −2"], 0, "(x + 4)(x − 3).", "p"),
 q("Solve x² − 5 = 0.", ["x = ±√5", "x = 5", "x = ±5", "x = √5"], 0, "x² = 5.", "p"),
 q("Discriminant of 3x² − 4x + 2?", ["−8", "40", "8", "−20"], 0, "16 − 24.", "p"),
 q("Solutions of x² − 6x + 4 = 0?", ["3 ± √5", "−3 ± √5", "6 ± √5", "3 ± √13"], 0, "(6 ± √20)/2 = 3 ± √5.", "p"),
 q("Which parabola is narrowest?", ["y = −5x²", "y = 2x²", "y = 0.5x²", "y = x² + 9"], 0, "Largest |a|.", "g"),
 q("Minimum value of y = x² − 4x + 1?", ["−3", "1", "2", "−4"], 0, "x = 2: 4 − 8 + 1.", "p"),
 q("How many x-intercepts does y = x² + 3 have?", ["0", "1", "2", "3"], 0, "It sits above the axis.", "g"),
 q("Which equation has roots 4 and −1?", ["(x − 4)(x + 1) = 0", "(x + 4)(x − 1) = 0", "(x − 4)(x − 1) = 0", "x² + 3x − 4 = 0"], 0, "Each root r gives a factor (x − r).", "c"),
 q("A ball's height is h = −16t² + 48t. When does it land?", ["t = 3", "t = 1.5", "t = 48", "t = 16"], 0, "−16t(t − 3) = 0.", "w"),
 q("y = x² shifted 3 right and 2 down is…", ["y = (x − 3)² − 2", "y = (x + 3)² − 2", "y = (x − 2)² − 3", "y = x² − 3x − 2"], 0, "Right is x − 3.", "g"),
]
FRQS = [
 {"q": "Let f(x) = 2x² − 8x + 6.", "parts": [
  {"p": "(a) Write f in vertex form and state the vertex.", "rubric": [["Factors out 2 and completes the square", 1], ["f(x) = 2(x − 2)² − 2", 1], ["Vertex (2, −2)", 1]], "answer": "2(x² − 4x + 4) − 8 + 6 = 2(x − 2)² − 2."},
  {"p": "(b) Find the zeros.", "rubric": [["2(x − 1)(x − 3) or formula", 1], ["x = 1 and x = 3", 1]], "answer": "x = 1, 3."},
  {"p": "(c) For what x is f(x) < 0?", "rubric": [["Between the zeros since it opens up", 1], ["1 < x < 3", 1]], "answer": "1 < x < 3."}]},
 {"q": "A farmer has 120 m of fence to make a rectangular pen against a barn (the barn wall needs no fence).", "parts": [
  {"p": "(a) If the sides perpendicular to the barn are x, write the area A(x).", "rubric": [["Other side is 120 − 2x", 1], ["A(x) = x(120 − 2x)", 1]], "answer": "A = x(120 − 2x)."},
  {"p": "(b) Find the dimensions that maximize the area and the max area.", "rubric": [["Vertex x = 30", 1], ["30 by 60", 1], ["1800 m²", 1]], "answer": "x = 30, other side 60, A = 1800 m²."}]},
]
build("pre-3", L, 3, "Quadratics", 'Parabolas and <span class="hl">quadratics</span>', "Vertex form, factoring, completing the square, the quadratic formula and the discriminant.", "Before Precalc unit 3: quadratics with interactive parabola labs and animated completing-the-square.", CH, PQ, CHAL, EXQ, FRQS, OUT)
