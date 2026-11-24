from math_common import *
L = "AP Precalculus"; OUT = "../../courses/math/precalc-1.html"

ROC = topic("roc", "Rates of change (1.1–1.3)", f'''
<p>Precalc is about <b>how outputs change as inputs change</b>. The <b>average rate of change</b> of {m('f')} on [{m('a')}, {m('b')}] is the slope of the secant line:</p>
{eq("AROC = (f(b) − f(a)) / (b − a)")}
<p>As the interval shrinks, the secant line approaches the tangent line and the average rate approaches the <b>rate of change at a point</b> (that's the derivative you'll meet in calculus).</p>
{lab(title="Secant line lab", sub="Shrink the gap between a and b and watch the secant turn into a tangent.", x=[-4, 4], y=[-6, 10], gx=1, gy=2, params={"b": [-3.5, 3.5, 0.05, 2.5, "b"], "a": [-3.5, 3.5, 0.25, 0.5, "a"]}, fns=[fn("x^3/2-2*x+1", "f(x) = x³/2 − 2x + 1", name="f")], secant={"f": "f", "a": "a", "b": "b"}, read=[["AROC =", "(f(b)-f(a))/(b-a)"]])}
{table(["Behavior", "Means"], [["Increasing", f"as {m('x')} increases, {m('f')}({m('x')}) increases (rate &gt; 0)"], ["Concave up", "the rate of change is increasing (graph bends like a cup)"], ["Concave down", "the rate of change is decreasing (graph bends like a frown)"], ["Point of inflection", "where concavity switches"]])}
<p><b>Linear</b> functions have a constant rate of change. <b>Quadratic</b> functions have rates that change at a constant rate: over equal input steps, the first differences form a linear pattern, and the second differences are constant.</p>
{lab(title="Differences table", sub="Equal x-steps: f(x) = a·x² + c. The second difference is always 2a.", x=[-1, 6], y=[-5, 40], gx=1, gy=5, params={"a": [-2, 2, 0.5, 1, "a"], "c": [-4, 4, 1, 0, "c"]}, fns=[fn("a*x^2+c", "f(x) = ax² + c")], table={"x": [0, 1, 2, 3, 4, 5], "rows": [["f(x)", "a*x^2+c"]], "diff": "diff"})}
''', pill=("c", "1.1"))

POLY = topic("polynomials", "Polynomial functions (1.4–1.6)", f'''
<p>A polynomial of degree {m('n')}: {m('p')}({m('x')}) = {m('a')}ₙ{m('x')}ⁿ + … + {m('a')}₁{m('x')} + {m('a')}₀. The <b>leading term</b> controls the end behavior.</p>
{table(["Degree", "Leading coefficient", "End behavior"], [["even", "+", "↑ on both ends"], ["even", "−", "↓ on both ends"], ["odd", "+", "↙ down on the left, ↗ up on the right"], ["odd", "−", "↖ up on the left, ↘ down on the right"]])}
<p><b>Zeros and multiplicity.</b> A factor ({m('x')} − {m('r')})<sup>k</sup> gives a zero at {m('r')} with multiplicity {m('k')}. Odd multiplicity: the graph <b>crosses</b>. Even multiplicity: it <b>bounces</b> (touches and turns).</p>
{lab(title="Multiplicity lab", sub="y = 0.1(x + 3)ᵖ(x − 1)^q(x − 4). Change each multiplicity: odd crosses, even bounces.", x=[-6, 7], y=[-12, 12], gx=1, gy=2, params={"p": [1, 3, 1, 1, "p"], "q": [1, 3, 1, 2, "q"]}, fns=[fn("0.1*(x+3)^p*(x-1)^q*(x-4)", "y = 0.1(x + 3)ᵖ(x − 1)^q(x − 4)")], dots=[["-3", "0", "x=−3", "#EA580C"], ["1", "0", "x=1", "#EA580C"], ["4", "0", "x=4", "#EA580C"]], read=[["degree =", "p+q+1"]])}
{mini(("Turning points", f"A degree-{m('n')} polynomial has at most {m('n')} − 1 turning points (local max/min) and at most {m('n')} real zeros."), ("Complex zeros", f"Degree {m('n')} means exactly {m('n')} complex zeros counting multiplicity. Non-real zeros come in conjugate pairs: if 2 + 3{m('i')} is a zero, so is 2 − 3{m('i')}."))}
{mini(("Even function", f"{m('f')}(−{m('x')}) = {m('f')}({m('x')}). Symmetric over the y-axis. Example {m('x')}⁴ − 3{m('x')}²."), ("Odd function", f"{m('f')}(−{m('x')}) = −{m('f')}({m('x')}). Symmetric about the origin. Example {m('x')}³ − 5{m('x')}."))}
''', pill=("g", "1.4"))

RAT = topic("rational", "Rational functions (1.7–1.10)", f'''
<p>A rational function is a ratio {m('r')}({m('x')}) = {m('p')}({m('x')})/{m('q')}({m('x')}). Factor first, then read off its features:</p>
{table(["Feature", "Where it comes from"], [
 ["Zeros", "x-values that make the numerator 0 (and not the denominator)"],
 ["Vertical asymptote", "a factor of the denominator that does NOT cancel"],
 ["Hole", "a factor that cancels from top and bottom"],
 ["Horizontal asymptote", "compare degrees: top &lt; bottom → y = 0; equal → ratio of leading coefficients; top &gt; bottom → none (slant if one more)"]])}
{steps("Analyze r(x) = (x² − x − 2) / (x² − 4)", [
 ("a|(x² − x − 2)|s  b|/  c|(x² − 4)|v", "Factor the numerator and denominator."),
 ("d|(x − 2)|e  e|(x + 1)|s  b|/  f|(x − 2)|e  g|(x + 2)|v", "x − 2 appears on top and bottom."),
 ("e|(x + 1)|s  b|/  g|(x + 2)|v", "It cancels → hole at x = 2, at y = (2 + 1)/(2 + 2) = 3/4."),
 ("h|zero x = −1|g  i|VA x = −2|e  j|HA y = 1|n", "Zero from the top, VA from the leftover bottom, HA from equal degrees (1/1)."),
])}
{lab(title="Rational function lab", sub="r(x) = a(x − z)/(x − v). Watch the asymptotes (red dashes) follow the sliders.", x=[-8, 8], y=[-8, 8], gx=1, gy=1, params={"v": [-5, 5, 0.5, 2, "v"], "z": [-5, 5, 0.5, -1, "z"], "a": [-3, 3, 0.5, 1, "a"]}, fns=[fn("a*(x-z)/(x-v)", "r(x) = a(x − z)/(x − v)")], vasym=["v"], hasym=["a"], dots=[["z", "0", "zero", "#059669"]])}
<p><b>End behavior with limits:</b> as {m('x')} → ∞, {m('r')}({m('x')}) → (horizontal asymptote). Near a vertical asymptote, {m('r')}({m('x')}) → ±∞; test a value on each side to get the sign.</p>
{box("trap", "Hole or asymptote?", f"Cancel common factors first! (x − 2)/(x − 2)(x + 2) has a hole at 2, not an asymptote.")}
''', pill=("c", "1.7"))

EQUIV = topic("equiv", "Equivalent forms and transformations (1.11–1.12)", f'''
<p><b>Polynomial long division</b> rewrites a rational function as quotient + remainder/divisor, which reveals a slant asymptote.</p>
{worked(f"Divide ({m('x')}² + 3{m('x')} + 5) ÷ ({m('x')} + 1).", f"{m('x')}·({m('x')} + 1) = {m('x')}² + {m('x')}, leaving 2{m('x')} + 5. Then 2({m('x')} + 1) = 2{m('x')} + 2, leaving 3. So {m('x')} + 2 + 3/({m('x')} + 1): slant asymptote {m('y')} = {m('x')} + 2.")}
<p><b>Binomial theorem</b>: expand ({m('a')} + {m('b')})ⁿ with Pascal's triangle coefficients. ({m('x')} + 2)³ = {m('x')}³ + 3·2{m('x')}² + 3·4{m('x')} + 8 = {m('x')}³ + 6{m('x')}² + 12{m('x')} + 8.</p>
<p><b>Transformations</b>: {m('g')}({m('x')}) = {m('a')}·{m('f')}({m('b')}({m('x')} + {m('c')})) + {m('d')}. The domain and range shift and scale with them.</p>
''', pill=("p", "1.11"))

MODEL = topic("models", "Choosing and building models (1.13–1.14)", f'''
<p>On the AP exam you pick a model from the data or the context, then justify it.</p>
{table(["Clue in the data", "Model"], [["constant first differences", "linear"], ["constant second differences", "quadratic"], ["constant third differences", "cubic"], ["a few known zeros, a turning shape", "polynomial built from factors"], ["output → constant as input grows, blows up near a value", "rational"], ["constant ratios over equal steps", "exponential (Unit 2)"]])}
{worked("A cubic has zeros at x = −1, 2, and 5 and passes through (0, 20). Find it.", f"{m('p')}({m('x')}) = {m('a')}({m('x')} + 1)({m('x')} − 2)({m('x')} − 5). At 0: {m('a')}(1)(−2)(−5) = 10{m('a')} = 20 → {m('a')} = 2.")}
{box("tip", "Justify", "Free-response answers need a reason in context: \"The second differences are all 4, so a quadratic model is appropriate.\"")}
''', pill=("w", "1.13"))

SUM = topic("summary-pc1", "Unit summary", mini(
 ("Rates", "AROC = slope of secant. Concave up ⇔ rate increasing."),
 ("Polynomials", "Leading term → end behavior. Multiplicity: odd crosses, even bounces. ≤ n zeros, ≤ n − 1 turns."),
 ("Rational", "Factor! Cancelled → hole. Leftover bottom → VA. Degrees → HA or slant."),
 ("Models", "Differences pick the polynomial degree. Build from zeros + one point."),
))
CH = [chapter("ch-roc", "Rates of Change", "Rates", [ROC]), chapter("ch-poly", "Polynomial Functions", "Polynomials", [POLY]), chapter("ch-rat", "Rational Functions", "Rational", [RAT, EQUIV]), chapter("ch-model", "Modeling", "Modeling", [MODEL, SUM])]

f = lambda x: x**3 - 2 * x
close((f(3) - f(1)) / 2, 11)
PQ = [
 q("f(x) = x³ − 2x. Average rate of change on [1, 3]?", ["11", "22", "10", "7"], 0, "(21 − (−1))/2 = 11.", "p"),
 q("A graph is concave down on an interval. Its rate of change there is…", ["decreasing", "increasing", "zero", "negative"], 0, "Concave down = rate of change decreasing.", "c"),
 q("x: 0,1,2,3; f: 3,5,11,21. Best model?", ["Quadratic", "Linear", "Exponential", "Cubic"], 0, "First differences 2, 6, 10; second differences 4, 4: constant.", "w"),
 q("End behavior of p(x) = −2x⁵ + x²?", ["Up on the left, down on the right", "Down on both ends", "Up on both ends", "Down on the left, up on the right"], 0, "Odd degree, negative leading coefficient.", "g"),
 q("p(x) = (x − 3)²(x + 1). At x = 3 the graph…", ["touches and turns", "crosses", "has an asymptote", "has a hole"], 0, "Even multiplicity bounces.", "g"),
 q("A degree-4 polynomial has at most how many turning points?", ["3", "4", "5", "2"], 0, "n − 1.", "c"),
 q("If 1 − 2i is a zero of a real polynomial, so is…", ["1 + 2i", "−1 + 2i", "2 − i", "−1 − 2i"], 0, "Conjugate pairs.", "c"),
 q("f(x) = x⁴ − 2x² is…", ["even", "odd", "neither", "both"], 0, "f(−x) = f(x).", "c"),
 q("Vertical asymptote of r(x) = (x + 1)/(x − 4)?", ["x = 4", "x = −1", "y = 1", "x = −4"], 0, "Denominator zero, doesn't cancel.", "g"),
 q("Horizontal asymptote of r(x) = (3x² + 1)/(2x² − 5)?", ["y = 3/2", "y = 0", "None", "y = 3"], 0, "Equal degrees: ratio of leading coefficients.", "g"),
 q("r(x) = (x − 5)(x + 2)/((x − 5)(x − 1)). At x = 5 there is…", ["a hole", "a vertical asymptote", "a zero", "nothing special"], 0, "The factor cancels.", "c"),
 q("lim as x → ∞ of (4x + 1)/(x² + 3)?", ["0", "4", "∞", "1/3"], 0, "Bottom degree is bigger.", "p"),
 q("(x² + 5x + 7) ÷ (x + 2) = ?", ["x + 3 + 1/(x + 2)", "x + 3", "x + 7 + 7/(x + 2)", "x + 3 − 1/(x + 2)"], 0, "x(x + 2) = x² + 2x, remainder 3x + 7; 3(x + 2) = 3x + 6, remainder 1.", "p"),
 q("Coefficient of x² in (x + 3)³?", ["9", "3", "27", "6"], 0, "3·3 = 9 (Pascal row 1 3 3 1).", "p"),
 q("g(x) = f(x − 2) + 3. If f has domain [0, 5], g has domain…", ["[2, 7]", "[−2, 3]", "[3, 8]", "[0, 5]"], 0, "Inputs shift right 2.", "g"),
]
CHAL = [
 q("A cubic with zeros −2, 1, 3 passes through (0, 12). Leading coefficient?", ["2", "−2", "6", "1"], 0, "a(2)(−1)(−3) = 6a = 12.", "p"),
 q("r(x) = (2x² − 8)/(x² − x − 2). Hole at…", ["(2, 8/3)", "(2, 0)", "(−1, 0)", "(−2, 8/3)"], 0, "2(x − 2)(x + 2)/((x − 2)(x + 1)) → 2(x + 2)/(x + 1); at x = 2: 8/3.", "p"),
 q("As x → −1⁺, r(x) = (x + 3)/(x + 1) →", ["+∞", "−∞", "1", "2"], 0, "Top ≈ 2 > 0, bottom small positive.", "c"),
 q("Slant asymptote of (x² − 4x + 1)/(x − 1)?", ["y = x − 3", "y = x − 4", "y = x + 3", "None"], 0, "Division gives x − 3 − 2/(x − 1).", "p"),
 q("A degree-5 real polynomial has zeros 2 (multiplicity 2) and 3i. How many real zeros can it have in total (with multiplicity)?", ["3", "2", "4", "5"], 0, "3i and −3i use 2 slots; 5 − 2 = 3 real.", "c"),
 q("On [0, 4], h(t) is increasing and concave down. Which is true?", ["h increases by less each second", "h increases by more each second", "h is decreasing", "AROC is negative"], 0, "Rate positive but decreasing.", "c"),
]
close(2 * (2 + 2) / (2 + 1), 8 / 3)
EXQ = [
 q("AROC of f(x) = x² from x = 1 to x = 4?", ["5", "15", "3", "8"], 0, "(16 − 1)/3.", "p"),
 q("Which has constant rate of change?", ["Linear", "Quadratic", "Cubic", "Rational"], 0, "By definition.", "c"),
 q("Zeros of p(x) = x(x − 2)²(x + 5)?", ["0, 2, −5", "0, −2, 5", "2, −5", "0, 4, −5"], 0, "Set each factor to zero.", "g"),
 q("End behavior of 3x⁴ − x³?", ["Up on both ends", "Down on both ends", "Down left, up right", "Up left, down right"], 0, "Even degree, positive.", "g"),
 q("Which is odd?", ["x³ + x", "x² + 1", "x³ + 1", "|x|"], 0, "f(−x) = −f(x).", "c"),
 q("Horizontal asymptote of (5x)/(x² + 1)?", ["y = 0", "y = 5", "None", "y = 1"], 0, "Lower degree on top.", "g"),
 q("Vertical asymptote(s) of 1/(x² − 9)?", ["x = ±3", "x = 3", "x = 9", "None"], 0, "x² = 9.", "g"),
 q("Domain of (x + 2)/(x² + 4)?", ["All real numbers", "x ≠ ±2", "x ≠ −2", "x ≠ 4"], 0, "x² + 4 is never 0.", "c"),
 q("A polynomial has degree 6. Max number of real zeros?", ["6", "5", "7", "3"], 0, "At most n.", "c"),
 q("Data with constant third differences suggests…", ["cubic", "quadratic", "exponential", "rational"], 0, "Degree = which difference is constant.", "w"),
 q("(x − 1)² expanded?", ["x² − 2x + 1", "x² − 1", "x² + 1", "x² − x + 1"], 0, "Binomial square.", "p"),
 q("r(x) = (x² − 1)/(x − 1). Which is true?", ["Hole at x = 1", "VA at x = 1", "Zero at x = 1", "HA y = 1"], 0, "Simplifies to x + 1 with x ≠ 1.", "c"),
 q("lim x→∞ (6x³ − 1)/(2x³ + x) = ?", ["3", "6", "0", "∞"], 0, "6/2.", "p"),
 q("If f is concave up on [a, b], the AROC on [a, (a+b)/2] is ___ the AROC on [(a+b)/2, b].", ["less than", "greater than", "equal to", "unrelated to"], 0, "Rates are increasing.", "c"),
]
FRQS = [
 {"q": "Let r(x) = (x² − 9)/(x² − 2x − 3).", "parts": [
  {"p": "(a) Find the domain of r and any holes.", "rubric": [["Factors: (x − 3)(x + 3)/((x − 3)(x + 1))", 1], ["x ≠ 3, −1", 1], ["Hole at (3, 3/2)", 1]], "answer": "Simplifies to (x + 3)/(x + 1); hole at x = 3, y = 6/4 = 3/2."},
  {"p": "(b) Find the vertical and horizontal asymptotes. Use limits to describe the behavior near the vertical asymptote.", "rubric": [["VA x = −1", 1], ["HA y = 1", 1], ["x → −1⁻: −∞; x → −1⁺: +∞", 1]], "answer": "Near −1: top ≈ 2. Left: bottom negative → −∞. Right: +∞."},
  {"p": "(c) Find the x- and y-intercepts.", "rubric": [["x = −3", 1], ["y = 3", 1]], "answer": "Zero −3; r(0) = 3."}]},
 {"q": "The table gives a population P (thousands) t years after 2020: t = 0, 1, 2, 3, 4 → P = 10, 13, 18, 25, 34.", "parts": [
  {"p": "(a) Show the data are quadratic.", "rubric": [["First differences 3, 5, 7, 9", 1], ["Second differences constant 2", 1]], "answer": "Second differences all 2."},
  {"p": "(b) Write a quadratic model P(t).", "rubric": [["a = 1 (half the second difference)", 1], ["P(t) = t² + 2t + 10", 1]], "answer": "P(t) = t² + 2t + 10. Check t = 3: 9 + 6 + 10 = 25 ✓"},
  {"p": "(c) Find the AROC from t = 1 to t = 4 and interpret it.", "rubric": [["(34 − 13)/3 = 7", 1], ["About 7,000 people per year on average", 1]], "answer": "7 thousand people per year."}]},
]
for t, P in zip(range(5), [10, 13, 18, 25, 34]): close(t * t + 2 * t + 10, P)
build("precalc-1", L, 1, "Polynomial and Rational Functions", 'Polynomial and <span class="hl">rational</span> functions', "Rates of change, polynomials and their zeros, rational functions and asymptotes, and choosing a model.", "AP Precalculus Unit 1: rates of change, polynomial and rational functions with interactive labs and an AP-style practice exam.", CH, PQ, CHAL, EXQ, FRQS, OUT, minutes=(35, 30), calc_note="Use a graphing calculator only where you'd be allowed one. ")
