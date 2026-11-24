from tp_common import *
C = "act"; L = "ACT"; OUT = "../../courses/act/act-3.html"
TAGS = {"n": "Number & quantity", "a": "Algebra", "f": "Functions", "w": "Word problems"}

NUM = topic("number", "Numbers and quantity", f'''
{mini(("Fractions, decimals, percents", "Convert freely: 3/8 = 0.375 = 37.5%."), ("Exponents and roots", "a^m·a^n = a^(m+n), (a^m)^n = a^(mn), a^(−n) = 1/aⁿ, √(ab) = √a·√b."), ("Factors and multiples", "LCM for \"when do they line up again\"; GCF for \"largest equal groups.\""), ("Complex numbers", "i = √−1, i² = −1. (3 + 2i)(1 − i) = 3 − 3i + 2i − 2i² = 5 − i."))}
{steps("Simplify (2 + 3i)(2 − 3i)", [
 ("a|(2 + 3i)(2 − 3i)|e", "This is (a + b)(a − b) = a² − b²."),
 ("b|4|n  c|−|s  d|9i²|v", "2² − (3i)²."),
 ("b|4|n  c|−|s  e|(−9)|v", "i² = −1, so 9i² = −9."),
 ("f|13|g", "4 + 9 = 13. Conjugates always multiply to a real number."),
])}
{worked("Bus A comes every 12 min, bus B every 18 min. Both just left. When together again?", "LCM(12, 18) = 36 minutes.")}
''', pill=("n", "3.1"))

ALG = topic("algebra", "Algebra", f'''
<p>Solve equations, inequalities, systems and absolute values; rearrange formulas; factor; work with quadratics.</p>
{steps("Solve for r: A = P(1 + rt)", [
 ("a|A|v  b|=  c|P(1 + rt)|s", "Divide both sides by P."),
 ("d|A/P|v  b|=  e|1 + rt|s", "Subtract 1."),
 ("f|A/P − 1|v  b|=  g|rt|s", "Divide by t."),
 ("h|r|g  b|=  i|(A/P − 1)/t|g", "r = (A − P)/(Pt)."),
])}
{lab(title="Absolute value equation", sub="|x − c| = d has solutions where the V crosses the line y = d.", x=[-8, 10], y=[-2, 10], gx=1, gy=1, params={"c": [-4, 5, 0.5, 2, "c"], "d": [-2, 8, 0.5, 4, "d"]}, fns=[fn("abs(x-c)", "y = |x − c|"), fn("x*0+d", "y = d")], dots=[["c-d", "d", "x = {c-d}", "#EA580C"], ["c+d", "d", "x = {c+d}", "#EA580C"]], read=[["solutions: ", "c-d"], ["and", "c+d"]])}
<p>When d &lt; 0 there are no solutions: an absolute value is never negative.</p>
''', pill=("a", "3.2"))

FUN = topic("functions", "Functions", f'''
{mini(("Notation", "f(3) means plug 3 in. f(x) = 5 means find the input(s) that give 5."), ("Composition", "f(g(x)): do g first."), ("Domain & range", "No division by 0; no even root of a negative; logs need positive inputs."), ("Logarithms", "log_b(a) = c means bᶜ = a. log 1000 = 3. log(xy) = log x + log y."))}
{lab(title="Exponential & log", sub="y = bˣ and its inverse y = log_b x mirror each other over y = x.", x=[-4, 8], y=[-4, 8], gx=1, gy=1, params={"b": [1.3, 4, 0.1, 2, "b"]}, fns=[fn("b^x", "y = bˣ"), fn("ln(x)/ln(b)", "y = log_b x"), fn("x", "y = x", c="#94A3B8", dash=True)])}
<p><b>Sequences:</b> arithmetic aₙ = a₁ + (n − 1)d; geometric aₙ = a₁·r^(n − 1).</p>
''', pill=("f", "3.3"))

WORD = topic("word", "Word problems and modeling", f'''
<ol class="steps"><li>Name the variable in words (\"x = number of adult tickets\").</li><li>Translate each sentence into an equation.</li><li>Solve, then answer the question actually asked (often not x itself).</li></ol>
{table(["Words", "Math"], [["is, equals", "="], ["of (with %)", "×"], ["per", "÷ (a rate)"], ["more than / less than", "+ / − (careful with order: 5 less than x is x − 5)"], ["at least / at most", "≥ / ≤"]])}
{worked("A rope is cut into two pieces. One is 4 m longer than twice the other. Total 31 m. Longer piece?", "x + (2x + 4) = 31 → x = 9. Longer = 2(9) + 4 = 22 m.")}
''', pill=("w", "3.4"))

CH = [chapter("ch-num", "Number and Quantity", "Numbers", [NUM]), chapter("ch-alg", "Algebra", "Algebra", [ALG]), chapter("ch-fn", "Functions and Modeling", "Functions", [FUN, WORD])]
PQ = [
 q("What is 3/8 as a percent?", ["37.5%", "38%", "3.8%", "26.7%"], 0, "0.375.", "n"),
 q("(2³)² · 2⁻⁴ = ?", ["4", "8", "16", "2"], 0, "2⁶ · 2⁻⁴ = 2².", "n"),
 q("(4 − i) + (2 + 5i) = ?", ["6 + 4i", "6 + 6i", "2 + 4i", "8 − 5i"], 0, "Add real and imaginary parts.", "n"),
 q("i² · i² = ?", ["1", "−1", "i", "−i"], 0, "(−1)(−1).", "n"),
 q("LCM of 8 and 12?", ["24", "48", "4", "96"], 0, "Smallest common multiple.", "n"),
 q("Solve 3(x − 4) = 2x + 1.", ["13", "11", "5", "−13"], 0, "3x − 12 = 2x + 1.", "a"),
 q("Solve |2x − 1| = 7.", ["x = 4 or x = −3", "x = 4", "x = −3 or x = 3", "x = 3 or x = −4"], 0, "2x − 1 = ±7.", "a"),
 q("Which is a factor of x² + x − 20?", ["x + 5", "x − 5", "x + 4", "x − 10"], 0, "(x + 5)(x − 4).", "a"),
 q("Solve for h: V = (1/3)πr²h.", ["h = 3V/(πr²)", "h = V/(3πr²)", "h = 3πr²/V", "h = πr²/(3V)"], 0, "Multiply by 3, divide by πr².", "a"),
 q("f(x) = 2x² − x. f(−3) = ?", ["21", "15", "−15", "−21"], 0, "18 + 3.", "f"),
 q("log₂ 32 = ?", ["5", "16", "4", "6"], 0, "2⁵ = 32.", "f"),
 q("Arithmetic sequence 7, 11, 15, … What is the 20th term?", ["83", "87", "80", "79"], 0, "7 + 19·4.", "f"),
 q("A phone plan costs $35 plus $0.10 per text. With a $50 budget, max texts?", ["150", "500", "15", "350"], 0, "0.10t ≤ 15.", "w"),
 q("A number decreased by 7 is 3 times 5. The number?", ["22", "8", "15", "−8"], 0, "x − 7 = 15.", "w"),
]
CHAL = [
 q("(3 + 2i)/(1 − i) = ?", ["1/2 + (5/2)i", "3 − 2i", "5 + i", "1 + 5i"], 0, "Multiply top and bottom by 1 + i: (3 + 3i + 2i + 2i²)/2 = (1 + 5i)/2.", "n"),
 q("If log x + log 4 = 2, x = ?", ["25", "50", "96", "1/2"], 0, "log 4x = 2 → 4x = 100.", "f"),
 q("Geometric sequence: 3, 6, 12, … The 10th term?", ["1,536", "768", "3,072", "30"], 0, "3 · 2⁹.", "f"),
 q("For what values of x is |x + 2| < 5?", ["−7 < x < 3", "x < 3", "−3 < x < 7", "x < −7 or x > 3"], 0, "−5 < x + 2 < 5.", "a"),
 q("A boat goes 24 km downstream in 2 h and back upstream in 3 h. Speed of the current?", ["2 km/h", "4 km/h", "10 km/h", "5 km/h"], 0, "b + c = 12, b − c = 8 → c = 2.", "w"),
 q("If f(x) = 3x − 1 and g(x) = x², for what x does f(g(x)) = 26?", ["±3", "3 only", "9", "±√(27)"], 0, "3x² − 1 = 26 → x² = 9.", "f"),
]
EX = [
 q("0.6 as a fraction in lowest terms?", ["3/5", "6/10", "2/3", "1/6"], 0, "6/10 = 3/5.", "n"),
 q("√50 − √8 = ?", ["3√2", "√42", "7√2", "5√2 − 2"], 0, "5√2 − 2√2.", "n"),
 q("(1 + i)² = ?", ["2i", "2", "1 + i²", "0"], 0, "1 + 2i + i² = 2i.", "n"),
 q("GCF of 36 and 60?", ["12", "6", "180", "24"], 0, "Largest common factor.", "n"),
 q("Solve 5x + 2 > 3x − 6.", ["x > −4", "x < −4", "x > 4", "x > −2"], 0, "2x > −8.", "a"),
 q("Solve: x + 2y = 7, x − y = 1. x = ?", ["3", "2", "1", "4"], 0, "3y = 6 → y = 2, x = 3.", "a"),
 q("x² − 9x + 14 = 0. Larger solution?", ["7", "2", "14", "9"], 0, "(x − 7)(x − 2).", "a"),
 q("Simplify (x² − 1)/(x + 1), x ≠ −1.", ["x − 1", "x + 1", "x", "1"], 0, "Difference of squares.", "a"),
 q("f(x) = √(x − 4). Domain?", ["x ≥ 4", "x > 4", "x ≥ 0", "all reals"], 0, "Radicand ≥ 0.", "f"),
 q("log 0.01 = ?", ["−2", "2", "−1", "0.01"], 0, "10⁻² = 0.01.", "f"),
 q("f(x) = x + 4, g(x) = 2x. g(f(1)) = ?", ["10", "6", "9", "12"], 0, "f(1) = 5, g(5) = 10.", "f"),
 q("A car rental is $40/day plus $0.20 per mile. 3 days, 150 miles. Total?", ["$150", "$120", "$160", "$130"], 0, "120 + 30.", "w"),
 q("Ana is 4 years older than Ben. In 6 years their ages sum to 40. Ana's age now?", ["16", "12", "14", "20"], 0, "(b + 4) + b + 12 = 40 → b = 12.", "w"),
 q("The sum of three consecutive integers is 72. The largest?", ["25", "24", "23", "26"], 0, "23, 24, 25.", "w"),
 q("If 2^(x+1) = 16, x = ?", ["3", "4", "7", "8"], 0, "x + 1 = 4.", "f"),
]
build(C, "act-3", L, 3, "Math: Numbers, Algebra and Functions", 'Math part 1: <span class="hl">algebra</span>', "Numbers and complex numbers, equations and formulas, functions, logs, sequences and word problems.", "ACT Math: number and quantity, algebra and functions with interactive graphs and practice.", CH, PQ, CHAL, EX, TAGS, OUT, minutes=17, rules=["15 questions in 17 minutes (ACT pace).", "Calculator allowed.", "No penalty for guessing."])
