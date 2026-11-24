from math_common import *
L = "Before Precalc"; OUT = "../../courses/math/pre-4.html"

NOTE = topic("f-notation", "What a function is", f'''
<p>A <b>function</b> assigns each input exactly one output. {m('f')}({m('x')}) is read "f of x": the output when the input is {m('x')}. It is <i>not</i> multiplication.</p>
{mini(("Vertical line test", "A graph is a function if no vertical line hits it twice. A circle fails; a parabola y = x² passes."), ("Evaluating", f"If {m('f')}({m('x')}) = {m('x')}² − 3{m('x')}, then {m('f')}(−2) = 4 + 6 = 10 and {m('f')}({m('a')} + 1) = ({m('a')} + 1)² − 3({m('a')} + 1)."))}
<p><b>Domain</b> = every allowed input. <b>Range</b> = every output you actually get. Watch for two things that shrink a domain:</p>
{table(["Danger", "Example", "Domain"], [["Division by zero", f"{m('f')}({m('x')}) = 1/({m('x')} − 2)", f"{m('x')} ≠ 2"], ["Even root of a negative", f"{m('g')}({m('x')}) = √({m('x')} + 5)", f"{m('x')} ≥ −5"], ["Both", f"{m('h')}({m('x')}) = 1/√(4 − {m('x')})", f"{m('x')} &lt; 4"]])}
{lab(title="Domain of a square root", sub="y = √(x − h) + k starts at (h, k) and only exists to the right.", x=[-6, 10], y=[-4, 8], gx=1, gy=1, params={"h": [-4, 6, 0.5, 1, "h"], "k": [-3, 4, 0.5, 0, "k"]}, fns=[fn("sqrt(x-h)+k", "y = √(x − h) + k")], dots=[["h", "k", "start ({h}, {k})", "#EA580C"]], read=[["domain: x ≥", "h"], ["range: y ≥", "k"]])}
''', pill=("c", "4.1"))

TRANS = topic("transform", "Transformations", f'''
<p>Every function family can be moved with the same four knobs: {m('y')} = {m('a')}·{m('f')}({m('b')}({m('x')} − {m('h')})) + {m('k')}.</p>
{table(["Change", "Effect"], [
 [f"{m('f')}({m('x')}) + {m('k')}", f"shift up {m('k')}"], [f"{m('f')}({m('x')} − {m('h')})", f"shift <b>right</b> {m('h')} (inside is opposite!)"],
 [f"{m('a')}·{m('f')}({m('x')})", f"vertical stretch by {m('a')}; negative {m('a')} reflects over the x-axis"],
 [f"{m('f')}({m('bx')})", f"horizontal squeeze by 1/{m('b')}; negative {m('b')} reflects over the y-axis"]])}
{lab(title="Transformation lab", sub="Gray dashed is the parent f(x) = x³/4 − 3x/2 (its bumps make every move easy to see). Blue is a·f(b(x − h)) + k.", x=[-8, 8], y=[-8, 8], gx=1, gy=1, params={"h": [-4, 4, 0.5, 2, "h"], "k": [-4, 4, 0.5, 1, "k"], "a": [-2, 2, 0.25, 1, "a"], "b": [-2, 2, 0.25, 1, "b"]}, fns=[fn("x^3/4-3*x/2", "parent f(x)", c="#94A3B8", dash=True, name="f"), fn("a*f(b*(x-h))+k", "y = a·f(b(x − h)) + k")])}
{box("trap", "Inside moves the other way", f"{m('f')}({m('x')} + 3) shifts LEFT 3, because you need {m('x')} = −3 to feed the same input {m('f')}(0) that {m('x')} = 0 used to.")}
''', pill=("g", "4.2"))

COMP = topic("composition", "Composition and inverses", f'''
<p><b>Composition</b> chains functions: ({m('f')} ∘ {m('g')})({m('x')}) = {m('f')}({m('g')}({m('x')})). Do the inside one first.</p>
{steps("f(x) = 2x + 1, g(x) = x². Find f(g(3)) and g(f(3)).", [
 ("a|f(|s  b|g(3)|v  c|)|s", "Work from the inside out: g(3) first."),
 ("a|f(|s  d|9|v  c|)|s", "g(3) = 3² = 9."),
 ("e|19|g", "f(9) = 2·9 + 1 = 19."),
 ("f|g(|v  g|f(3)|s  h|)|v", "Now the other order: f(3) first."),
 ("f|g(|v  i|7|s  h|)|v", "f(3) = 7."),
 ("j|49|g", "g(7) = 49. Order matters: 19 ≠ 49."),
])}
<p>An <b>inverse</b> {m('f')}⁻¹ undoes {m('f')}: if {m('f')}(2) = 5, then {m('f')}⁻¹(5) = 2. To find it: swap {m('x')} and {m('y')}, then solve for {m('y')}. Its graph is the mirror image across {m('y')} = {m('x')}.</p>
{steps("Find the inverse of f(x) = (x − 4)/3", [
 ("a|y|v  b|=  c|(x − 4)/3|s", "Write y = f(x)."),
 ("d|x|v  b|=  e|(y − 4)/3|s", "Swap x and y."),
 ("f|3x|v  b|=  g|y − 4|s", "Multiply both sides by 3."),
 ("h|3x + 4|v  b|=  i|y|g", "Add 4."),
 ("j|f⁻¹(x)|g  b|=  h|3x + 4|g", "Undo ÷3 and −4 in reverse order: ×3 then +4."),
])}
{lab(title="Mirror across y = x", sub="f(x) = mx + c and its inverse (x − c)/m.", x=[-8, 8], y=[-8, 8], gx=1, gy=1, params={"m": [0.25, 4, 0.25, 2, "m"], "c": [-4, 4, 0.5, 1, "c"]}, fns=[fn("m*x+c", "f(x)"), fn("(x-c)/m", "f⁻¹(x)"), fn("x", "y = x", c="#94A3B8", dash=True)], dots=[["1", "m+c", "({1}, {m+c})", "#2563EB"], ["m+c", "1", "({m+c}, 1)", "#EA580C"]])}
{box("tip", "One-to-one", "Only functions that pass the horizontal line test have inverses. y = x² fails, so we restrict it to x ≥ 0 to get √x.")}
''', pill=("p", "4.3"))

PARENT = topic("parents", "Parent function gallery", f'''
<p>Know these shapes cold. Every precalc problem starts from one of them.</p>
{lab(title="Parent functions I", sub="Hover to read points. Notice which ones are symmetric.", x=[-4, 4], y=[-4, 4], gx=1, gy=1, fns=[fn("x", "y = x"), fn("x^2", "y = x²"), fn("x^3", "y = x³"), fn("abs(x)", "y = |x|")])}
{lab(title="Parent functions II", sub="These have restricted domains or asymptotes.", x=[-4, 6], y=[-4, 6], gx=1, gy=1, fns=[fn("sqrt(x)", "y = √x"), fn("1/x", "y = 1/x"), fn("2^x", "y = 2ˣ"), fn("cbrt(x)", "y = ∛x")])}
''', pill=("g", "4.4"))

SUM = topic("summary-pre4", "Unit summary", mini(
 ("Domain", "No dividing by 0, no even roots of negatives."),
 ("Transformations", "a·f(b(x − h)) + k: outside moves are what they look like; inside moves are opposite and 1/b."),
 ("Composition", "f(g(x)): inside first. Usually f(g(x)) ≠ g(f(x))."),
 ("Inverse", "Swap x and y, solve. Mirror over y = x. f(f⁻¹(x)) = x."),
))
CH = [chapter("ch-fn", "Functions", "Functions", [NOTE]), chapter("ch-trans", "Transformations", "Transforms", [TRANS, PARENT]), chapter("ch-comp", "Composition and Inverses", "Inverses", [COMP, SUM])]
PQ = [
 q("f(x) = 3x² − x. Find f(−2).", ["14", "10", "−14", "38"], 0, "3·4 + 2.", "p"),
 q("Domain of f(x) = 1/(x + 7)?", ["x ≠ −7", "x ≠ 7", "x > −7", "All reals"], 0, "Denominator can't be 0.", "c"),
 q("Domain of g(x) = √(2x − 6)?", ["x ≥ 3", "x ≥ 6", "x > 3", "x ≤ 3"], 0, "2x − 6 ≥ 0.", "c"),
 q("Range of y = x² + 4?", ["y ≥ 4", "All reals", "y ≤ 4", "y ≥ 0"], 0, "x² ≥ 0.", "g"),
 q("y = f(x − 5) moves the graph of f…", ["right 5", "left 5", "up 5", "down 5"], 0, "Inside is opposite.", "g"),
 q("y = −f(x) reflects f over the…", ["x-axis", "y-axis", "line y = x", "origin"], 0, "Outputs change sign.", "g"),
 q("y = 3f(x) does what?", ["Vertical stretch by 3", "Horizontal stretch by 3", "Shift up 3", "Shift right 3"], 0, "Outside multiplier.", "g"),
 q("f(x) = x + 2, g(x) = 3x. Find f(g(4)).", ["14", "18", "12", "6"], 0, "g(4) = 12, f(12) = 14.", "p"),
 q("Same functions. Find g(f(4)).", ["18", "14", "12", "6"], 0, "f(4) = 6, g(6) = 18.", "p"),
 q("Inverse of f(x) = 2x − 6?", ["(x + 6)/2", "(x − 6)/2", "2x + 6", "1/(2x − 6)"], 0, "Swap and solve.", "p"),
 q("If f(3) = 10, then f⁻¹(10) = …", ["3", "10", "1/10", "−3"], 0, "The inverse swaps inputs and outputs.", "c"),
 q("The graph of f⁻¹ is the reflection of f over…", ["y = x", "the x-axis", "the y-axis", "y = −x"], 0, "Swapping x and y mirrors across y = x.", "g"),
 q("Which is NOT a function?", ["x² + y² = 9", "y = x²", "y = |x|", "y = 2ˣ"], 0, "A circle fails the vertical line test.", "c"),
 q("y = √x shifted left 2 and up 1?", ["y = √(x + 2) + 1", "y = √(x − 2) + 1", "y = √x + 3", "y = √(x + 1) + 2"], 0, "Left 2 is x + 2.", "g"),
]
CHAL = [
 q("f(x) = x² − 1, g(x) = √x. Domain of f(g(x))?", ["x ≥ 0", "All reals", "x ≥ 1", "x ≠ 0"], 0, "g needs x ≥ 0; then f(g(x)) = x − 1 but the domain still comes from g.", "c"),
 q("Inverse of f(x) = (2x + 1)/(x − 3)?", ["(3x + 1)/(x − 2)", "(x − 3)/(2x + 1)", "(3x − 1)/(x + 2)", "(x + 1)/(2x − 3)"], 0, "x(y − 3) = 2y + 1 → xy − 2y = 3x + 1 → y = (3x + 1)/(x − 2).", "p"),
 q("y = f(2x) compared to y = f(x)…", ["squeezes horizontally by ½", "stretches horizontally by 2", "stretches vertically by 2", "shifts left 2"], 0, "Each output arrives at half the x.", "g"),
 q("If f(g(x)) = x for all x, then g is…", ["f⁻¹", "f", "1/f", "−f"], 0, "That's the definition of inverse.", "c"),
 q("f(x) = x² on x ≤ 0. f⁻¹(x) = …", ["−√x", "√x", "±√x", "x²"], 0, "Outputs must be ≤ 0, the original inputs.", "p"),
 q("Domain of h(x) = √(x + 1)/(x − 4)?", ["x ≥ −1, x ≠ 4", "x > −1", "x ≠ 4", "x ≥ 4"], 0, "Both conditions at once.", "c"),
]
EXQ = [
 q("f(x) = 5 − 2x. f(3) = ?", ["−1", "1", "11", "−6"], 0, "5 − 6.", "p"),
 q("Domain of y = √(5 − x)?", ["x ≤ 5", "x ≥ 5", "x < 5", "All reals"], 0, "5 − x ≥ 0.", "c"),
 q("Domain of y = 3/(x² − 9)?", ["x ≠ ±3", "x ≠ 3", "x ≠ 9", "All reals"], 0, "x² = 9 at ±3.", "c"),
 q("y = (x + 4)² is y = x² moved…", ["left 4", "right 4", "up 4", "down 4"], 0, "Inside opposite.", "g"),
 q("y = f(−x) reflects over the…", ["y-axis", "x-axis", "y = x", "origin"], 0, "Inputs flip sign.", "g"),
 q("f(x) = x², g(x) = x − 3. (f ∘ g)(x) = ?", ["(x − 3)²", "x² − 3", "x² − 3x", "x − 9"], 0, "f of g.", "p"),
 q("Inverse of f(x) = x³ + 2?", ["∛(x − 2)", "∛x − 2", "x³ − 2", "1/(x³ + 2)"], 0, "Swap, subtract 2, cube root.", "p"),
 q("Which function has an inverse function?", ["y = 2x + 1", "y = x²", "y = |x|", "y = x² + 1"], 0, "Only the line is one-to-one.", "c"),
 q("If (2, 7) is on f, which point is on f⁻¹?", ["(7, 2)", "(2, 7)", "(−2, −7)", "(2, −7)"], 0, "Swap coordinates.", "g"),
 q("Range of y = −|x| + 3?", ["y ≤ 3", "y ≥ 3", "All reals", "y ≥ 0"], 0, "Peak at 3.", "g"),
 q("f(x) = 2x. f(f(f(1))) = ?", ["8", "6", "2", "16"], 0, "1 → 2 → 4 → 8.", "p"),
 q("y = 2f(x) − 1 does what to f?", ["stretch ×2, then down 1", "down 1, then stretch ×2", "shrink ½, up 1", "right 2, down 1"], 0, "Multiply outputs by 2, then subtract 1.", "g"),
]
FRQS = [
 {"q": "Let f(x) = √(x − 2) and g(x) = x² + 2.", "parts": [
  {"p": "(a) State the domain and range of f.", "rubric": [["Domain x ≥ 2", 1], ["Range y ≥ 0", 1]], "answer": "Domain [2, ∞), range [0, ∞)."},
  {"p": "(b) Find f(g(x)) and simplify.", "rubric": [["√(x² + 2 − 2)", 1], ["= |x|", 1]], "answer": "√(x²) = |x|."},
  {"p": "(c) Find f⁻¹(x) with its domain.", "rubric": [["Swap and square: y = x² + 2", 1], ["Domain x ≥ 0", 1]], "answer": "f⁻¹(x) = x² + 2, x ≥ 0."}]},
 {"q": "The graph of g is the graph of y = x² reflected over the x-axis, shifted 3 left and 5 up.", "parts": [
  {"p": "(a) Write g(x).", "rubric": [["−(x + 3)²", 1], ["+ 5", 1]], "answer": "g(x) = −(x + 3)² + 5."},
  {"p": "(b) Give the vertex, range, and the x-intercepts.", "rubric": [["Vertex (−3, 5)", 1], ["Range y ≤ 5", 1], ["x = −3 ± √5", 1]], "answer": "(x + 3)² = 5 → x = −3 ± √5."}]},
]
build("pre-4", L, 4, "Functions", 'All about <span class="hl">functions</span>', "Notation, domain and range, transformations, composition and inverses: the language of precalc.", "Before Precalc unit 4: functions, transformations, composition and inverses with interactive graphs.", CH, PQ, CHAL, EXQ, FRQS, OUT)
