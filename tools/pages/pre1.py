from math_common import *
L = "Before Precalc"
OUT = "../../courses/math/pre-1.html"

ORDER = topic("order", "Order of operations", f'''
<p>Every calculation follows the same order, so everyone gets the same answer: <b>P</b>arentheses, <b>E</b>xponents, <b>M</b>ultiplication and <b>D</b>ivision (left to right), <b>A</b>ddition and <b>S</b>ubtraction (left to right).</p>
{steps("Simplify 3 + 2·(5 − 1)²", [
 ("a|3|n  b|+  c|2|n  d|·  e|(5 − 1)|e  f|²|v", "Start with the parentheses."),
 ("a|3|n  b|+  c|2|n  d|·  e|4|e  f|²|v", "5 − 1 = 4. Next come exponents."),
 ("a|3|n  b|+  c|2|n  d|·  g|16|e", "4² = 16. Now multiply."),
 ("a|3|n  b|+  h|32|e", "2 · 16 = 32. Last, add."),
 ("i|35|g", "3 + 32 = 35."),
])}
{box("trap", "Common trap", f"−3² means −(3²) = −9. Only (−3)² = 9. The exponent grabs the number right next to it, not the minus sign.")}
''', pill=("c", "1.1"))

EXP = topic("exponents", "Exponent rules", f'''
<p>An exponent counts repeated multiplication: {m("x")}⁴ = {m("x·x·x·x")}. Every rule below comes from counting factors.</p>
{table(["Rule", "Example", "Why"], [
 [f"{m('x')}<sup>a</sup> · {m('x')}<sup>b</sup> = {m('x')}<sup>a+b</sup>", f"{m('x')}² · {m('x')}³ = {m('x')}⁵", "2 factors then 3 more = 5 factors"],
 [f"{m('x')}<sup>a</sup> ÷ {m('x')}<sup>b</sup> = {m('x')}<sup>a−b</sup>", f"{m('x')}⁷ ÷ {m('x')}³ = {m('x')}⁴", "3 factors cancel"],
 [f"({m('x')}<sup>a</sup>)<sup>b</sup> = {m('x')}<sup>ab</sup>", f"({m('x')}²)³ = {m('x')}⁶", "three groups of two"],
 [f"({m('xy')})<sup>a</sup> = {m('x')}<sup>a</sup>{m('y')}<sup>a</sup>", f"(2{m('x')})³ = 8{m('x')}³", "the power hits every factor"],
 [f"{m('x')}<sup>0</sup> = 1", "5⁰ = 1", f"{m('x')}<sup>a</sup> ÷ {m('x')}<sup>a</sup> = 1"],
 [f"{m('x')}<sup>−a</sup> = 1 / {m('x')}<sup>a</sup>", f"2<sup>−3</sup> = 1/8", "keep dividing by x"],
 [f"{m('x')}<sup>1/n</sup> = ⁿ√{m('x')}", "8<sup>1/3</sup> = 2", "(8<sup>1/3</sup>)³ = 8"],
])}
{steps("Simplify (2x³)² · x⁻⁴", [
 ("a|(2x³)²|e  b|·  c|x⁻⁴|s", "Square everything inside the parentheses."),
 ("d|4|n  e|x⁶|e  b|·  c|x⁻⁴|s", "2² = 4 and (x³)² = x⁶. Now combine the x's."),
 ("d|4|n  f|x⁶⁺⁽⁻⁴⁾|e", "Same base, so add exponents."),
 ("d|4|n  g|x²|g", "6 + (−4) = 2. Answer: 4x²."),
])}
{lab(title="Exponential vs power", sub="Compare xⁿ with 2ˣ. Slide n and see who wins in the long run.", x=[-1, 8], y=[-2, 60], gx=1, gy=10, params={"n": [1, 5, 1, 2, "n"]}, fns=[fn("x^n", "y = xⁿ"), fn("2^x", "y = 2ˣ")], read=[["xⁿ at x=6:", "6^n"], ["2ˣ at x=6:", "2^6"]])}
{box("tip", "Fractional exponents", f"{m('x')}<sup>m/n</sup> = (ⁿ√{m('x')})<sup>m</sup>. Take the root first so the numbers stay small: 27<sup>2/3</sup> = (∛27)² = 3² = 9.")}
''', pill=("c", "1.2"))

RAD = topic("radicals", "Radicals", f'''
<p>√{m('x')} is the non-negative number whose square is {m('x')}. To simplify, pull out perfect-square factors: √({m('ab')}) = √{m('a')} · √{m('b')}.</p>
{steps("Simplify √72", [
 ("a|√72|e", "Look for the biggest perfect square that divides 72."),
 ("b|√36|v  c|·  d|√2|s", "72 = 36 · 2, and 36 is a perfect square."),
 ("e|6|n  d|√2|s", "√36 = 6. Answer: 6√2."),
])}
{steps("Rationalize 6 / √3", [
 ("a|6|n  b|/  c|√3|e", "We don't leave a root in the denominator. Multiply top and bottom by √3."),
 ("a|6|n  x|√3|v  b|/  c|√3|e  y|√3|v", "Multiplying by √3/√3 is multiplying by 1."),
 ("z|6√3|n  b|/  w|3|e", "√3 · √3 = 3."),
 ("g|2√3|g", "6/3 = 2. Answer: 2√3."),
])}
{box("trap", "Not allowed", "√(a + b) is NOT √a + √b. Check: √(9 + 16) = √25 = 5, but √9 + √16 = 7.")}
''', pill=("c", "1.3"))

FACT = topic("factoring", "Factoring", f'''
<p>Factoring is multiplication run backwards. Always try these in order:</p>
<ol class="steps"><li><b>GCF first.</b> 6{m('x')}² + 9{m('x')} = 3{m('x')}(2{m('x')} + 3).</li>
<li><b>Difference of squares:</b> {m('a')}² − {m('b')}² = ({m('a')} − {m('b')})({m('a')} + {m('b')}). So {m('x')}² − 49 = ({m('x')} − 7)({m('x')} + 7).</li>
<li><b>Trinomial {m('x')}² + {m('bx')} + {m('c')}:</b> find two numbers that multiply to {m('c')} and add to {m('b')}.</li>
<li><b>Trinomial {m('a')}{m('x')}² + {m('bx')} + {m('c')}:</b> AC method: multiply {m('a·c')}, split the middle term, factor by grouping.</li>
<li><b>Cubes:</b> {m('a')}³ ± {m('b')}³ = ({m('a')} ± {m('b')})({m('a')}² ∓ {m('ab')} + {m('b')}²).</li></ol>
{steps("Factor x² + 5x + 6", [
 ("a|x²|s  b|+  c|5x|v  d|+  e|6|n", "Need two numbers: multiply to 6, add to 5."),
 ("a|x²|s  b|+  f|2x|v  g|+  h|3x|v  d|+  e|6|n", "2 and 3 work. Split 5x into 2x + 3x."),
 ("i|x(x + 2)|e  g|+  j|3(x + 2)|e", "Group: pull x out of the first pair and 3 out of the second."),
 ("k|(x + 2)|g  l|(x + 3)|g", "Both pieces share (x + 2). Answer: (x + 2)(x + 3)."),
])}
{steps("Factor 2x² + 7x + 3 (AC method)", [
 ("a|2x²|s  b|+  c|7x|v  d|+  e|3|n", "a·c = 2·3 = 6. Need two numbers that multiply to 6 and add to 7."),
 ("a|2x²|s  b|+  f|x|v  g|+  h|6x|v  d|+  e|3|n", "1 and 6. Split 7x into x + 6x."),
 ("i|x(2x + 1)|e  g|+  j|3(2x + 1)|e", "Group the pairs."),
 ("k|(2x + 1)|g  l|(x + 3)|g", "Answer: (2x + 1)(x + 3). Multiply it back out to check."),
])}
{lab(title="Factors are x-intercepts", sub="y = (x − p)(x − q). Each factor makes a zero where the graph crosses the x-axis.", x=[-8, 8], y=[-12, 12], gx=1, gy=2, params={"p": [-6, 6, 1, -2, "p"], "q": [-6, 6, 1, 3, "q"]}, fns=[fn("(x-p)*(x-q)", "y = (x − p)(x − q)")], dots=[["p", "0", "x = {p}", "#EA580C"], ["q", "0", "x = {q}", "#EA580C"]], read=[["Expanded b =", "-(p+q)"], ["c =", "p*q"]])}
''', pill=("p", "1.4"))

FRAC = topic("rational-exp", "Rational expressions", f'''
<p>A rational expression is a fraction of polynomials. Simplify by <b>factoring first, then cancelling common factors</b> (never cancel terms that are added).</p>
{worked(f"Simplify ({m('x')}² − 9) / ({m('x')}² + 5{m('x')} + 6).", f"Factor: ({m('x')} − 3)({m('x')} + 3) / (({m('x')} + 2)({m('x')} + 3)). Cancel ({m('x')} + 3): ({m('x')} − 3)/({m('x')} + 2), with {m('x')} ≠ −3 and {m('x')} ≠ −2.")}
{worked(f"Add 1/{m('x')} + 2/({m('x')} + 1).", f"Common denominator {m('x')}({m('x')} + 1): ({m('x')} + 1 + 2{m('x')}) / ({m('x')}({m('x')} + 1)) = (3{m('x')} + 1)/({m('x')}({m('x')} + 1)).")}
{box("trap", "Cancelling terms", f"({m('x')} + 3)/3 is NOT {m('x')}. You can only cancel factors (things multiplied), not terms (things added).")}
''', pill=("p", "1.5"))

SUM = topic("summary-pre1", "Unit summary", mini(
 ("Order", "Parentheses → exponents → × ÷ left to right → + − left to right. −3² = −9."),
 ("Exponents", "Add when multiplying, subtract when dividing, multiply for a power of a power. x⁰ = 1, x⁻ⁿ = 1/xⁿ, x<sup>1/n</sup> = ⁿ√x."),
 ("Radicals", "Pull out perfect squares; rationalize denominators. √(a + b) ≠ √a + √b."),
 ("Factoring", "GCF → difference of squares → trinomials (AC method) → cubes. Check by multiplying back out."),
))

CH = [chapter("ch-arith", "Order and Exponents", "Exponents", [ORDER, EXP]),
      chapter("ch-rad", "Radicals", "Radicals", [RAD]),
      chapter("ch-fact", "Factoring and Fractions", "Factoring", [FACT, FRAC, SUM])]

close(3 + 2 * (5 - 1) ** 2, 35); close(27 ** (2 / 3), 9); close(72 ** .5, 6 * 2 ** .5)
PQ = [
 q("Evaluate 8 − 2 · 3².", ["−10", "54", "2", "−46"], 0, "Exponent first: 3² = 9. Then 2·9 = 18. Then 8 − 18 = −10.", "p"),
 q("Evaluate −4².", ["−16", "16", "−8", "8"], 0, "The exponent applies only to 4: −(4²) = −16.", "c"),
 q("Simplify x³ · x⁵.", ["x⁸", "x¹⁵", "2x⁸", "x²"], 0, "Same base, multiply → add exponents: 3 + 5 = 8.", "p"),
 q("Simplify (3x²)³.", ["27x⁶", "9x⁶", "27x⁵", "3x⁶"], 0, "3³ = 27 and (x²)³ = x⁶.", "p"),
 q("Simplify x⁻³ written with positive exponents.", ["1/x³", "−x³", "−3x", "x/3"], 0, "A negative exponent means reciprocal: x⁻³ = 1/x³.", "c"),
 q("Evaluate 16^(3/4).", ["8", "12", "4", "64"], 0, "Fourth root of 16 is 2, then 2³ = 8.", "p"),
 q("Simplify √50.", ["5√2", "25√2", "2√5", "10√5"], 0, "50 = 25 · 2, so √50 = 5√2.", "p"),
 q("Rationalize 10/√5.", ["2√5", "√5/2", "10√5", "5√2"], 0, "10√5/5 = 2√5.", "p"),
 q("Factor x² − 64.", ["(x − 8)(x + 8)", "(x − 8)²", "(x − 32)(x + 2)", "Can't be factored"], 0, "Difference of squares: x² − 8².", "p"),
 q("Factor x² − x − 12.", ["(x − 4)(x + 3)", "(x + 4)(x − 3)", "(x − 6)(x + 2)", "(x − 12)(x + 1)"], 0, "Multiply to −12 and add to −1: −4 and 3.", "p"),
 q("Factor 3x² + 10x + 8.", ["(3x + 4)(x + 2)", "(3x + 2)(x + 4)", "(3x + 8)(x + 1)", "(x + 4)(x + 2)"], 0, "a·c = 24; 4 and 6 add to 10. 3x² + 6x + 4x + 8 = 3x(x + 2) + 4(x + 2).", "p"),
 q("Simplify (x² − 4)/(x − 2), for x ≠ 2.", ["x + 2", "x − 2", "x² − 2", "1/(x + 2)"], 0, "(x − 2)(x + 2)/(x − 2) = x + 2.", "p"),
 q("Which equals √(9 + 16)?", ["5", "7", "25", "√9 + √16"], 0, "√25 = 5. A root does not split over addition.", "c"),
 q("The graph of y = (x − 1)(x + 4) crosses the x-axis at…", ["x = 1 and x = −4", "x = −1 and x = 4", "x = 1 and x = 4", "x = −4 only"], 0, "Set each factor to zero: x − 1 = 0 or x + 4 = 0.", "g"),
]
CHAL = [
 q("Simplify (2x⁻²y³)⁻² written with positive exponents.", ["x⁴/(4y⁶)", "4x⁴/y⁶", "x⁴y⁶/4", "−4x⁴y⁶"], 0, "(2)⁻² = 1/4, (x⁻²)⁻² = x⁴, (y³)⁻² = y⁻⁶. Together: x⁴/(4y⁶).", "p"),
 q("Factor completely: 2x³ − 18x.", ["2x(x − 3)(x + 3)", "2x(x² − 9)", "2(x − 3)(x + 3)", "x(2x − 9)(x + 2)"], 0, "GCF 2x first, then x² − 9 is a difference of squares. 'Completely' means keep going.", "p"),
 q("Factor x³ − 27.", ["(x − 3)(x² + 3x + 9)", "(x − 3)³", "(x − 3)(x² − 3x + 9)", "(x + 3)(x² − 3x + 9)"], 0, "a³ − b³ = (a − b)(a² + ab + b²) with a = x, b = 3.", "p"),
 q("Simplify 1/(x − 1) − 1/(x + 1).", ["2/(x² − 1)", "0", "−2/(x² − 1)", "2x/(x² − 1)"], 0, "((x + 1) − (x − 1))/((x − 1)(x + 1)) = 2/(x² − 1).", "p"),
 q("Solve 4^x = 8.", ["x = 3/2", "x = 2", "x = 1/2", "x = 2/3"], 0, "Write both as powers of 2: 2^(2x) = 2³, so 2x = 3.", "p"),
 q("If x > 0, which equals √(x³)?", ["x√x", "x³ᐟ²·x", "x²√x", "√3·x"], 0, "x³ = x²·x, and √(x²) = x. So √(x³) = x^(3/2) = x√x.", "c"),
]
EXQ = [
 q("Evaluate 20 ÷ 4 · 5.", ["25", "1", "100", "4"], 0, "Left to right: 20 ÷ 4 = 5, then 5 · 5 = 25.", "p"),
 q("Simplify x¹⁰ / x².", ["x⁸", "x⁵", "x¹²", "x²⁰"], 0, "Subtract exponents.", "p"),
 q("Evaluate 9^(−1/2).", ["1/3", "−3", "3", "−1/3"], 0, "9^(1/2) = 3, the negative exponent flips it: 1/3.", "p"),
 q("Simplify √18 + √8.", ["5√2", "√26", "6√2", "13√2"], 0, "3√2 + 2√2 = 5√2.", "p"),
 q("Factor 4x² − 25.", ["(2x − 5)(2x + 5)", "(4x − 5)(x + 5)", "(2x − 5)²", "4(x − 5)(x + 5)"], 0, "(2x)² − 5².", "p"),
 q("Factor x² + 2x − 15.", ["(x + 5)(x − 3)", "(x − 5)(x + 3)", "(x + 15)(x − 1)", "(x − 5)(x − 3)"], 0, "5 · (−3) = −15 and 5 + (−3) = 2.", "p"),
 q("Which expression is equivalent to (x²)³ · x?", ["x⁷", "x⁶", "x⁹", "x⁵"], 0, "(x²)³ = x⁶, times x is x⁷.", "p"),
 q("Simplify (x² + 3x)/x for x ≠ 0.", ["x + 3", "x² + 3", "x + 3x", "3x"], 0, "Factor: x(x + 3)/x.", "p"),
 q("Which is a factor of 2x² − x − 6?", ["2x + 3", "2x − 3", "x + 2", "x − 3"], 0, "2x² − x − 6 = (2x + 3)(x − 2).", "p"),
 q("Rationalize 3/(2√3).", ["√3/2", "3√3", "√3/6", "2√3"], 0, "Multiply top and bottom by √3: 3√3/6 = √3/2.", "p"),
 q("Where does y = x(x − 5) cross the x-axis?", ["x = 0 and x = 5", "x = 5 only", "x = −5 and x = 0", "It doesn't"], 0, "Each factor equal to zero.", "g"),
 q("Which statement is true for every positive a and b?", ["√(ab) = √a·√b", "√(a + b) = √a + √b", "(a + b)² = a² + b²", "a⁻¹ = −a"], 0, "Roots split over multiplication, not addition.", "c"),
]
FRQS = [
 {"q": "Simplify each expression. Show your steps.", "parts": [
  {"p": "(a) (4x³y⁻¹)² · (2xy)⁻¹, with positive exponents only.", "rubric": [["Squares the first factor: 16x⁶y⁻²", 1], ["Handles (2xy)⁻¹ = 1/(2xy)", 1], ["Final answer 8x⁵/y³", 1]], "answer": "16x⁶y⁻² · 1/(2xy) = 8x⁵y⁻³ = 8x⁵/y³."},
  {"p": "(b) √75 − 2√12", "rubric": [["√75 = 5√3", 1], ["2√12 = 4√3", 1], ["Answer √3", 1]], "answer": "5√3 − 4√3 = √3."}]},
 {"q": "Factor and simplify.", "parts": [
  {"p": "(a) Factor completely: 3x³ − 12x² − 15x.", "rubric": [["Takes out GCF 3x", 1], ["Factors x² − 4x − 5", 1], ["3x(x − 5)(x + 1)", 1]], "answer": "3x(x² − 4x − 5) = 3x(x − 5)(x + 1)."},
  {"p": "(b) Simplify (x² − 25)/(x² − 3x − 10) and state the excluded values.", "rubric": [["Factors top and bottom", 1], ["(x + 5)/(x + 2)", 1], ["x ≠ 5 and x ≠ −2", 1]], "answer": "(x − 5)(x + 5)/((x − 5)(x + 2)) = (x + 5)/(x + 2), x ≠ 5, −2."}]},
]
build("pre-1", L, 1, "Algebra Toolkit", 'The <span class="hl">algebra toolkit</span>', "Order of operations, exponents, radicals and factoring: the moves you'll use on every single precalc problem.", "Before Precalc unit 1: order of operations, exponent rules, radicals and factoring with animated steps and practice.", CH, PQ, CHAL, EXQ, FRQS, OUT)
