from math_common import *
import math as M
L = "AP Precalculus"; OUT = "../../courses/math/precalc-2.html"

SEQ = topic("sequences", "Arithmetic and geometric sequences (2.1–2.2)", f'''
{mini(("Arithmetic", f"Add the same <b>common difference</b> {m('d')}: {m('a')}ₙ = {m('a')}₀ + {m('d')}{m('n')}. Like a linear function on whole numbers."), ("Geometric", f"Multiply by the same <b>common ratio</b> {m('r')}: {m('g')}ₙ = {m('g')}₀·{m('r')}ⁿ. Like an exponential function on whole numbers."))}
<p>Linear functions change by <b>equal differences</b> over equal input steps. Exponential functions change by <b>equal ratios</b>. That one sentence decides most modeling questions.</p>
{lab(title="Linear vs exponential", sub="Both start at 2. Which wins? Push the rate and watch the table.", x=[0, 10], y=[0, 60], gx=1, gy=10, params={"r": [1.05, 2, 0.05, 1.5, "r"], "d": [0.5, 6, 0.5, 3, "d"]}, fns=[fn("2+d*x", "linear: 2 + d·x"), fn("2*r^x", "exponential: 2·rˣ")], table={"x": [0, 1, 2, 3, 4, 5], "rows": [["2·rˣ", "2*r^x"], ["2 + d·x", "2+d*x"]], "diff": "ratio"})}
<p>The orange row shows the ratio of consecutive exponential outputs: always {m('r')}. Eventually any increasing exponential beats any linear function.</p>
''', pill=("c", "2.1"))

EXPF = topic("exp-fns", "Exponential functions (2.3–2.6)", f'''
<p>{m('f')}({m('x')}) = {m('a')}·{m('b')}ˣ with {m('a')} ≠ 0, {m('b')} &gt; 0, {m('b')} ≠ 1. {m('a')} is the initial value; {m('b')} is the growth factor.</p>
{table(["", "b > 1", "0 < b < 1"], [["Behavior", "growth", "decay"], ["End behavior", "→ 0 as x → −∞, → ∞ as x → ∞", "→ ∞ as x → −∞, → 0 as x → ∞"], ["Asymptote", "y = 0", "y = 0"], ["Concavity (a > 0)", "always up", "always up"]])}
{lab(title="Exponential lab", sub="y = a·bˣ + k. The horizontal asymptote is y = k.", x=[-5, 5], y=[-4, 12], gx=1, gy=2, params={"b": [0.2, 3, 0.05, 2, "b"], "a": [-3, 3, 0.25, 1, "a"], "k": [-3, 3, 0.5, 0, "k"]}, fns=[fn("a*b^x+k", "y = a·bˣ + k")], hasym=["k"], dots=[["0", "a+k", "(0, {a+k})", "#EA580C"]])}
{table(["Context", "Model"], [["grows 6% per year", f"{m('P')} = {m('P')}₀(1.06)<sup>{m('t')}</sup>"], ["loses 15% per year", f"{m('V')} = {m('V')}₀(0.85)<sup>{m('t')}</sup>"], ["doubles every 5 hours", f"{m('N')} = {m('N')}₀·2<sup>{m('t')}/5</sup>"], ["half-life 30 years", f"{m('A')} = {m('A')}₀(½)<sup>{m('t')}/30</sup>"], ["compounded n times a year", f"{m('A')} = {m('P')}(1 + {m('r')}/{m('n')})<sup>{m('nt')}</sup>"], ["continuous", f"{m('A')} = {m('P')}{m('e')}<sup>{m('rt')}</sup>"]])}
{box("tip", "Rewriting exponentials", f"Exponent rules let you change the time unit. 2<sup>{m('t')}/5</sup> = (2<sup>1/5</sup>)<sup>{m('t')}</sup> ≈ 1.149<sup>{m('t')}</sup>: about 14.9% growth per hour.")}
''', pill=("g", "2.3"))

INV = topic("inverses", "Composition and inverses (2.7–2.8)", f'''
<p>{m('f')} and {m('g')} are inverses when {m('f')}({m('g')}({m('x')})) = {m('x')} and {m('g')}({m('f')}({m('x')})) = {m('x')}. The input-output pairs swap, so the graphs reflect over {m('y')} = {m('x')}.</p>
{lab(title="bˣ and its inverse", sub="The inverse of y = bˣ is y = log_b x. Slide b.", x=[-4, 8], y=[-4, 8], gx=1, gy=1, params={"b": [1.2, 4, 0.1, 2, "b"]}, fns=[fn("b^x", "y = bˣ"), fn("ln(x)/ln(b)", "y = log_b x"), fn("x", "y = x", c="#94A3B8", dash=True)], dots=[["0", "1", "(0, 1)", "#2563EB"], ["1", "0", "(1, 0)", "#EA580C"], ["1", "b", "(1, b)", "#2563EB"], ["b", "1", "(b, 1)", "#EA580C"]])}
''', pill=("c", "2.7"))

LOG = topic("logs", "Logarithms (2.9–2.12)", f'''
<p>A logarithm answers "what exponent?": log<sub>{m('b')}</sub> {m('c')} = {m('a')} means {m('b')}<sup>{m('a')}</sup> = {m('c')}. So log₂ 8 = 3 because 2³ = 8. ln means log base {m('e')}; log with no base means base 10.</p>
{steps("Rewrite log₃ 81 = x", [
 ("a|log₃|s  b|81|v  c|=  d|x|e", "The base of the log becomes the base of the power."),
 ("a|3|s  d|ˣ|e  c|=  b|81|v", "3ˣ = 81."),
 ("a|3|s  d|ˣ|e  c|=  e|3⁴|v", "81 = 3⁴."),
 ("f|x = 4|g", "Same base, so the exponents match."),
])}
{table(["Property", "Rule", "Mirror of"], [["Product", "log_b(MN) = log_b M + log_b N", "bᵐbⁿ = bᵐ⁺ⁿ"], ["Quotient", "log_b(M/N) = log_b M − log_b N", "bᵐ/bⁿ = bᵐ⁻ⁿ"], ["Power", "log_b(Mᵏ) = k·log_b M", "(bᵐ)ᵏ = bᵐᵏ"], ["Change of base", "log_b M = ln M / ln b", ""], ["Inverse", "log_b(bˣ) = x, b^(log_b x) = x", ""]])}
<p><b>Log functions</b> {m('f')}({m('x')}) = {m('a')}·log<sub>{m('b')}</sub>{m('x')}: domain {m('x')} &gt; 0, vertical asymptote {m('x')} = 0, range all reals. With {m('b')} &gt; 1 they increase and are concave down: output grows by equal amounts when input is multiplied by equal factors.</p>
{steps("Expand ln(x³√y / z)", [
 ("a|ln(x³√y / z)|e", "Quotient first: top minus bottom."),
 ("b|ln(x³√y)|s  c|−|n  d|ln z|v", "Product: split the top."),
 ("e|ln x³|s  f|+|n  g|ln √y|s  c|−|n  d|ln z|v", "Power rule: √y = y^(1/2)."),
 ("h|3 ln x|g  f|+|n  i|½ ln y|g  c|−|n  d|ln z|g", "3 ln x + ½ ln y − ln z."),
])}
''', pill=("p", "2.9"))

EQN = topic("log-eq", "Equations, modeling and semi-log plots (2.13–2.15)", f'''
{steps("Solve 5·2ˣ = 60", [
 ("a|5|n  b|·  c|2ˣ|v  d|=  e|60|n", "Isolate the exponential first."),
 ("c|2ˣ|v  d|=  f|12|n", "Divide by 5."),
 ("g|x|v  d|=  h|log₂ 12|e", "Rewrite as a log."),
 ("g|x|v  d|=  i|ln 12 / ln 2|e", "Change of base for the calculator."),
 ("j|x ≈ 3.585|g", "Check: 2^3.585 ≈ 12 ✓"),
])}
{steps("Solve log₂(x + 3) + log₂(x − 3) = 4", [
 ("a|log₂(x + 3)|s  b|+  c|log₂(x − 3)|s  d|=  e|4|n", "Combine with the product rule."),
 ("f|log₂(x² − 9)|s  d|=  e|4|n", "(x + 3)(x − 3) = x² − 9."),
 ("g|x² − 9|v  d|=  h|16|n", "Rewrite: 2⁴ = 16."),
 ("i|x = ±5|e", "x² = 25."),
 ("j|x = 5|g", "Check the domain: x = −5 makes log₂(−2), not allowed. Only x = 5."),
])}
{box("trap", "Extraneous solutions", "Always plug log solutions back in. The argument of every log must be positive.")}
<p><b>Semi-log plots</b> put ln {m('y')} (or log {m('y')}) on the vertical axis. Exponential data {m('y')} = {m('a')}{m('b')}ˣ become a straight line: ln {m('y')} = ln {m('a')} + {m('x')}·ln {m('b')}. Slope = ln {m('b')}, intercept = ln {m('a')}.</p>
{lab(title="Semi-log view", sub="Blue: y = a·bˣ. Orange: ln y, which is a line with slope ln b.", x=[0, 6], y=[-2, 20], gx=1, gy=2, params={"b": [1.1, 2.5, 0.05, 1.6, "b"], "a": [0.5, 4, 0.25, 2, "a"]}, fns=[fn("a*b^x", "y = a·bˣ"), fn("ln(a)+x*ln(b)", "ln y = ln a + x·ln b")], read=[["slope ln b =", "ln(b)"], ["intercept ln a =", "ln(a)"]])}
''', pill=("w", "2.13"))

SUM = topic("summary-pc2", "Unit summary", mini(
 ("Linear vs exponential", "Equal differences vs equal ratios over equal steps."),
 ("Exponential", "a·bˣ: b > 1 growth, 0 < b < 1 decay; asymptote y = 0 (shifted by + k)."),
 ("Logs", "log_b c = a ⇔ bᵃ = c. Product → sum, quotient → difference, power → coefficient."),
 ("Solving", "Isolate, rewrite, change of base. Check log arguments > 0. Semi-log: exponential → line."),
))
CH = [chapter("ch-seq", "Sequences", "Sequences", [SEQ]), chapter("ch-exp", "Exponential Functions", "Exponential", [EXPF, INV]), chapter("ch-log", "Logarithms", "Logs", [LOG]), chapter("ch-eq", "Equations and Models", "Equations", [EQN, SUM])]
close(M.log(12) / M.log(2), 3.585); close(2 ** .2, 1.149)
PQ = [
 q("Arithmetic: a₀ = 7, d = −3. a₁₀ = ?", ["−23", "−20", "37", "−26"], 0, "7 + 10(−3).", "p"),
 q("Geometric: g₀ = 3, r = 2. g₅ = ?", ["96", "48", "30", "13"], 0, "3·2⁵.", "p"),
 q("x: 0,1,2,3; y: 5,15,45,135. Best model?", ["Exponential", "Linear", "Quadratic", "Logarithmic"], 0, "Constant ratio 3.", "w"),
 q("A car worth $20,000 loses 12% per year. Model?", ["V = 20000(0.88)ᵗ", "V = 20000(0.12)ᵗ", "V = 20000(1.12)ᵗ", "V = 20000 − 0.12t"], 0, "Keep 88% each year.", "w"),
 q("Horizontal asymptote of y = 3·2ˣ − 4?", ["y = −4", "y = 0", "y = 3", "x = −4"], 0, "Shifted down 4.", "g"),
 q("log₅ 125 = ?", ["3", "25", "5", "1/3"], 0, "5³ = 125.", "p"),
 q("log₂(1/8) = ?", ["−3", "3", "1/3", "−1/3"], 0, "2⁻³ = 1/8.", "p"),
 q("ln(e⁷) = ?", ["7", "e⁷", "7e", "1"], 0, "Inverse functions.", "p"),
 q("log 20 + log 5 = ?", ["2", "log 25", "100", "1"], 0, "log 100 = 2.", "p"),
 q("3 log₂ x − log₂ y = ?", ["log₂(x³/y)", "log₂(3x − y)", "log₂(x³y)", "3 log₂(x/y)"], 0, "Power then quotient rule.", "p"),
 q("Solve 3ˣ = 20.", ["x = ln 20/ln 3", "x = 20/3", "x = ln(20/3)", "x = log₂₀ 3"], 0, "Take ln of both sides.", "p"),
 q("Domain of f(x) = ln(x − 2)?", ["x > 2", "x ≥ 2", "x > 0", "All reals"], 0, "Argument positive.", "c"),
 q("Inverse of f(x) = 10ˣ?", ["log x", "ln x", "x¹⁰", "1/10ˣ"], 0, "Base 10.", "c"),
 q("On a semi-log plot (ln y vs x), exponential data look…", ["linear", "quadratic", "logarithmic", "periodic"], 0, "ln y = ln a + x ln b.", "g"),
 q("Bacteria double every 4 hours from 100. Model?", ["N = 100·2^(t/4)", "N = 100·4^(t/2)", "N = 100·2^(4t)", "N = 200t"], 0, "One doubling per 4 hours.", "w"),
]
CHAL = [
 q("Solve log₃(x) + log₃(x − 8) = 2.", ["x = 9", "x = −1 or 9", "x = −1", "x = 17"], 0, "x² − 8x = 9 → (x − 9)(x + 1) = 0; reject −1.", "p"),
 q("Solve e^(2x) − 5eˣ + 6 = 0.", ["x = ln 2 or ln 3", "x = 2 or 3", "x = ln 6", "No solution"], 0, "Let u = eˣ: u² − 5u + 6 = 0 → u = 2, 3.", "p"),
 q("A half-life is 8 days. Fraction left after 20 days?", ["(1/2)^2.5 ≈ 0.177", "0.4", "0.25", "(1/2)^0.4"], 0, "20/8 = 2.5 half-lives.", "w"),
 q("2^(t/5) written as bᵗ has b ≈", ["1.149", "1.4", "0.4", "2.5"], 0, "2^(1/5).", "p"),
 q("Semi-log line: ln y = 0.7 + 0.3x. Then y = ?", ["e^0.7 · (e^0.3)ˣ", "0.7·0.3ˣ", "0.7 + e^(0.3x)", "e^(0.7x)"], 0, "Exponentiate both sides.", "c"),
 q("$1000 at 5% compounded monthly for 10 years ≈", ["$1647", "$1629", "$1500", "$1649"], 0, "1000(1 + 0.05/12)^120 ≈ 1647.01.", "w"),
]
close(1000 * (1 + .05 / 12) ** 120, 1647.01); close(.5 ** 2.5, .177)
EXQ = [
 q("Common ratio of 2, 6, 18, 54?", ["3", "4", "2", "12"], 0, "Each ÷ previous.", "p"),
 q("Which grows fastest for large x?", ["1.01ˣ", "100x", "x²", "log x"], 0, "Exponential growth eventually wins.", "c"),
 q("y-intercept of y = 5(0.5)ˣ?", ["5", "0.5", "2.5", "0"], 0, "x = 0.", "g"),
 q("Is y = 4(0.9)ˣ growth or decay?", ["Decay", "Growth", "Neither", "Both"], 0, "0 < b < 1.", "c"),
 q("log₄ 64 = ?", ["3", "16", "4", "1/3"], 0, "4³.", "p"),
 q("Rewrite 10³ = 1000 in log form.", ["log 1000 = 3", "log 3 = 1000", "log₃ 1000 = 10", "ln 1000 = 3"], 0, "Base 10.", "c"),
 q("log₂ 12 − log₂ 3 = ?", ["2", "log₂ 9", "4", "3"], 0, "log₂ 4.", "p"),
 q("Solve log x = 3.", ["x = 1000", "x = 30", "x = e³", "x = 3"], 0, "10³.", "p"),
 q("Solve 2ˣ⁺¹ = 32.", ["x = 4", "x = 5", "x = 16", "x = 3"], 0, "x + 1 = 5.", "p"),
 q("Vertical asymptote of y = log₂(x + 3)?", ["x = −3", "x = 3", "y = −3", "x = 0"], 0, "x + 3 = 0.", "g"),
 q("ln 5 / ln 2 equals…", ["log₂ 5", "log₅ 2", "ln 2.5", "ln 3"], 0, "Change of base.", "c"),
 q("A town grows 3% per year from 8000. Population after 10 years ≈", ["10,751", "10,400", "8,240", "24,000"], 0, "8000(1.03)^10.", "w"),
 q("If f(x) = eˣ and g(x) = ln x, then f(g(5)) = ?", ["5", "e⁵", "ln 5", "1"], 0, "Inverses.", "c"),
 q("Which is concave down for x > 0?", ["y = ln x", "y = eˣ", "y = x²", "y = 2ˣ"], 0, "Logs bend down.", "g"),
]
close(8000 * 1.03 ** 10, 10751.33)
FRQS = [
 {"q": "A cup of coffee cools. Its temperature above room temperature is modeled by D(t) = a·bᵗ. At t = 0 minutes D = 120°F; at t = 10, D = 75°F.", "parts": [
  {"p": "(a) Find a and b.", "rubric": [["a = 120", 1], ["b¹⁰ = 75/120 = 0.625", 1], ["b ≈ 0.954", 1]], "answer": "b = 0.625^(1/10) ≈ 0.9541."},
  {"p": "(b) Find when D = 30°F. Show the log step.", "rubric": [["0.954ᵗ = 0.25", 1], ["t = ln 0.25 / ln b ≈ 29.5 min", 1]], "answer": "t = ln 0.25/ln 0.9541 ≈ 29.5 minutes."},
  {"p": "(c) Is D concave up or down? What does that mean for how fast it cools?", "rubric": [["Concave up (decreasing exponential)", 1], ["Cooling slows down over time", 1]], "answer": "Concave up: it drops fast at first, then more slowly."}]},
 {"q": "Symbolic manipulation.", "parts": [
  {"p": "(a) Solve log₄(x + 6) − log₄(x) = 1/2.", "rubric": [["log₄((x + 6)/x) = 1/2", 1], ["(x + 6)/x = 2", 1], ["x = 6, checked", 1]], "answer": "4^(1/2) = 2, x + 6 = 2x, x = 6."},
  {"p": "(b) Rewrite 9^(x/2) · 3^(1 − x) as a single number.", "rubric": [["9^(x/2) = 3ˣ", 1], ["3ˣ · 3^(1 − x) = 3", 1]], "answer": "3."}]},
]
b = .625 ** .1; close(b, .9541, 1e-3); close(M.log(.25) / M.log(b), 29.49)
build("precalc-2", L, 2, "Exponential and Logarithmic Functions", 'Exponentials and <span class="hl">logarithms</span>', "Sequences, exponential growth and decay, inverses, logarithms, log equations and semi-log plots.", "AP Precalculus Unit 2: exponential and logarithmic functions with interactive labs and an AP-style practice exam.", CH, PQ, CHAL, EXQ, FRQS, OUT, minutes=(35, 30), calc_note="Use a graphing calculator only where you'd be allowed one. ")
