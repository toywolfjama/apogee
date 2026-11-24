from tp_common import *
import math as M
C = "act"; L = "ACT"; OUT = "../../courses/act/act-4.html"
TAGS = {"g": "Geometry", "t": "Trigonometry", "s": "Statistics & probability", "h": "Higher topics"}

GEO = topic("geometry", "Plane and coordinate geometry", f'''
<p>The ACT gives <b>no formula sheet</b>. Memorize these.</p>
{table(["Shape", "Formulas"], [["Triangle", "A = ½bh; angles sum to 180°"], ["Rectangle / parallelogram", "A = bh"], ["Trapezoid", "A = ½(b₁ + b₂)h"], ["Circle", "A = πr², C = 2πr; arc = (θ/360)·2πr"], ["Polygon interior angles", "(n − 2)·180°"], ["Box / cylinder", "V = lwh, V = πr²h"], ["Coordinate", "distance √(Δx² + Δy²), midpoint = averages, slope Δy/Δx"]])}
{lab(title="Circle in the plane", sub="(x − h)² + (y − k)² = r²", h=540, x=[-8, 8], y=[-6, 6], gx=1, gy=1, params={"r": [1, 5, 0.5, 3, "r"], "h": [-4, 4, 0.5, 1, "h"], "k": [-3, 3, 0.5, -1, "k"]}, fns=[fn("k+sqrt(r^2-(x-h)^2)", "(x − h)² + (y − k)² = r²"), dict(e="k-sqrt(r^2-(x-h)^2)", c="#2563EB", hide=True)], dots=[["h", "k", "center", "#EA580C"]], read=[["area: ", "pi*r^2"]])}
{worked("A regular hexagon: each interior angle?", "(6 − 2)·180 = 720; 720/6 = 120°.")}
''', pill=("g", "4.1"))

TRIG = topic("trig", "Trigonometry", f'''
{mini(("SOH-CAH-TOA", "Right triangles only."), ("Unit circle", "(cos θ, sin θ). Know 30°, 45°, 60° exact values and the quadrant signs."), ("Identities", "sin²θ + cos²θ = 1; tan θ = sin θ/cos θ."), ("Law of Sines / Cosines", "Non-right triangles: a/sin A = b/sin B; c² = a² + b² − 2ab cos C. The ACT usually prints these in the question if needed."))}
{lab(type="circle", deg=135)}
{lab(title="Sinusoid", sub="y = a·sin(b·x) + d: amplitude |a|, period 2π/b, midline d.", x=[0, 12.566], y=[-5, 5], gx=1.5708, gy=1, xpi=True, params={"a": [-4, 4, 0.5, 2, "a"], "b": [0.5, 3, 0.5, 1, "b"], "d": [-2, 2, 0.5, 0, "d"]}, fns=[fn("a*sin(b*x)+d", "y = a·sin(bx) + d")], read=[["period: ", "2*pi/b"]])}
''', pill=("t", "4.2"))

STAT = topic("stats", "Statistics and probability", f'''
{mini(("Center", "Mean, median, mode. Adding a constant to every value shifts all three; multiplying scales them."), ("Spread", "Range, standard deviation. Adding a constant doesn't change spread."), ("Counting", "Multiply choices: 3 shirts × 4 pants = 12 outfits. Order matters → permutations; order doesn't → combinations: C(n, k) = n!/(k!(n − k)!)."), ("Probability", "P(A and B) = P(A)·P(B) if independent. P(not A) = 1 − P(A). Expected value = Σ value × probability."))}
{steps("How many ways to choose 3 of 5 students for a committee?", [
 ("a|C(5, 3)|e", "Order doesn't matter: combination."),
 ("b|5! / (3! · 2!)|s", "n!/(k!(n − k)!)."),
 ("c|120 / (6 · 2)|s", "5! = 120, 3! = 6, 2! = 2."),
 ("d|10|g", "10 committees."),
])}
''', pill=("s", "4.3"))

HIGH = topic("higher", "Matrices, vectors and other higher topics", f'''
{mini(("Matrices", "Add entry by entry (same size). Multiply rows × columns: (m×n)(n×p) gives m×p. Determinant of [[a, b], [c, d]] = ad − bc."), ("Vectors", "⟨a, b⟩ + ⟨c, d⟩ = ⟨a + c, b + d⟩. Magnitude √(a² + b²)."), ("Logs and exponentials", "Solve 3ˣ = 20 with x = log 20 / log 3."), ("Ellipses & parabolas", "x²/a² + y²/b² = 1 is an ellipse centered at the origin with x-intercepts ±a."))}
{steps("Multiply [[1, 2], [3, 4]] · [[5], [6]]", [
 ("a|[1 2]·[5 6]|s  b|[3 4]·[5 6]|v", "Each row times the column."),
 ("c|1·5 + 2·6|s  d|3·5 + 4·6|v", "Multiply matching entries and add."),
 ("e|17|g  f|39|g", "Result: the column [17, 39]."),
])}
''', pill=("h", "4.4"))

CH = [chapter("ch-geo", "Geometry", "Geometry", [GEO]), chapter("ch-trig", "Trigonometry", "Trig", [TRIG]), chapter("ch-stat", "Statistics, Probability, Higher Topics", "Stats & more", [STAT, HIGH])]
PQ = [
 q("Area of a triangle with base 10 and height 7?", ["35", "70", "17", "140"], 0, "½ · 70.", "g"),
 q("Sum of interior angles of a pentagon?", ["540°", "360°", "720°", "900°"], 0, "3 · 180.", "g"),
 q("Distance between (−1, 2) and (5, 10)?", ["10", "14", "8", "√52"], 0, "√(36 + 64).", "g"),
 q("Circle with radius 6. Length of a 60° arc?", ["2π", "6π", "π", "12π"], 0, "(60/360)·12π.", "g"),
 q("Volume of a box 3 × 4 × 5?", ["60", "47", "12", "94"], 0, "lwh.", "g"),
 q("sin 30° = ?", ["1/2", "√3/2", "√2/2", "1"], 0, "Special triangle.", "t"),
 q("cos θ = 5/13 in a right triangle. tan θ = ?", ["12/5", "5/12", "13/12", "12/13"], 0, "Opposite 12.", "t"),
 q("Period of y = 3 sin(2x)?", ["π", "2π", "3", "4π"], 0, "2π/2.", "t"),
 q("In which quadrant are both sin and cos negative?", ["III", "II", "IV", "I"], 0, "ASTC.", "t"),
 q("Mean of 4, 7, 9, 12, 18?", ["10", "9", "11", "12"], 0, "50/5.", "s"),
 q("A coin is flipped 3 times. P(all heads)?", ["1/8", "1/6", "3/8", "1/2"], 0, "(1/2)³.", "s"),
 q("How many 4-digit PINs use digits 0–9 with repeats allowed?", ["10,000", "5,040", "40", "9,999"], 0, "10⁴.", "s"),
 q("Determinant of [[2, 3], [1, 4]]?", ["5", "11", "8", "−5"], 0, "8 − 3.", "h"),
 q("Magnitude of the vector ⟨6, −8⟩?", ["10", "14", "2", "100"], 0, "√(36 + 64).", "h"),
]
CHAL = [
 q("A triangle has sides 7 and 10 with a 60° angle between them. Third side? (c² = a² + b² − 2ab cos C)", ["√79", "√149", "√51", "13"], 0, "49 + 100 − 140·½ = 79.", "t"),
 q("How many ways can 5 runners finish 1st, 2nd and 3rd?", ["60", "10", "125", "120"], 0, "5 · 4 · 3.", "s"),
 q("A game pays $10 with probability 0.2 and $0 otherwise. Costs $3 to play. Expected net?", ["−$1", "$2", "$7", "−$3"], 0, "0.2 · 10 − 3.", "s"),
 q("[[1, 0], [2, 1]] · [[3, 1], [0, 2]] = ?", ["[[3, 1], [6, 4]]", "[[3, 0], [0, 2]]", "[[3, 1], [2, 3]]", "[[4, 1], [2, 3]]"], 0, "Row 2: [2·3 + 1·0, 2·1 + 1·2] = [6, 4].", "h"),
 q("sin²(40°) + cos²(40°) = ?", ["1", "0", "2 sin 40°", "Can't tell"], 0, "Pythagorean identity.", "t"),
 q("Two similar triangles have areas 16 and 36. Ratio of perimeters?", ["2:3", "4:9", "16:36", "4:6"], 0, "√(16/36) = 2/3.", "g"),
]
close(49 + 100 - 140 * .5, 79)
EX = [
 q("Area of a trapezoid with bases 6 and 10 and height 4?", ["32", "64", "40", "24"], 0, "½ · 16 · 4.", "g"),
 q("Midpoint of (2, 8) and (6, −2)?", ["(4, 3)", "(4, 5)", "(8, 6)", "(2, 5)"], 0, "Averages.", "g"),
 q("Each interior angle of a regular octagon?", ["135°", "120°", "144°", "108°"], 0, "1080/8.", "g"),
 q("Circumference of a circle with area 49π?", ["14π", "7π", "49π", "28π"], 0, "r = 7.", "g"),
 q("Slope of a line perpendicular to 2x + 3y = 6?", ["3/2", "−2/3", "2/3", "−3/2"], 0, "Given slope −2/3.", "g"),
 q("tan 45° = ?", ["1", "0", "√2", "√3"], 0, "Equal legs.", "t"),
 q("A ladder 13 ft long reaches 12 ft up a wall. Distance from the wall at the base?", ["5 ft", "1 ft", "√313 ft", "25 ft"], 0, "5-12-13.", "g"),
 q("cos 120° = ?", ["−1/2", "1/2", "−√3/2", "√3/2"], 0, "QII, reference 60°.", "t"),
 q("Amplitude of y = −5 cos x + 2?", ["5", "−5", "2", "7"], 0, "|a|.", "t"),
 q("Median of 3, 9, 4, 12, 7, 8?", ["7.5", "7", "8", "6.5"], 0, "Sorted: 3, 4, 7, 8, 9, 12.", "s"),
 q("A bag has 3 red, 5 blue and 2 green. P(not blue)?", ["1/2", "1/5", "3/10", "1/3"], 0, "5/10.", "s"),
 q("Each data value is increased by 4. What happens to the standard deviation?", ["Stays the same", "Increases by 4", "Doubles", "Decreases by 4"], 0, "Shifting doesn't change spread.", "s"),
 q("C(6, 2) = ?", ["15", "30", "12", "36"], 0, "6·5/2.", "s"),
 q("⟨2, 5⟩ + ⟨−3, 1⟩ = ?", ["⟨−1, 6⟩", "⟨5, 6⟩", "⟨−6, 5⟩", "⟨−1, 4⟩"], 0, "Add components.", "h"),
 q("Solve 2ˣ = 10 (nearest hundredth).", ["3.32", "5.00", "3.16", "2.30"], 0, "log 10/log 2.", "h"),
]
close(M.log(10) / M.log(2), 3.32, 0.01)
build(C, "act-4", L, 4, "Math: Geometry, Trig and Statistics", 'Math part 2: <span class="hl">shapes & stats</span>', "Plane and coordinate geometry (no formula sheet!), trig, statistics, probability, counting, matrices and vectors.", "ACT Math: geometry, trigonometry, statistics, probability, matrices and vectors with interactive labs.", CH, PQ, CHAL, EX, TAGS, OUT, minutes=17, rules=["15 questions in 17 minutes (ACT pace).", "Calculator allowed. No formula sheet, just like the real ACT.", "No penalty for guessing."])
