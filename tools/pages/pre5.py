from math_common import *
L = "Before Precalc"; OUT = "../../courses/math/pre-5.html"
import math as M

PYTH = topic("pyth", "Pythagorean theorem and distance", f'''
<p>In a right triangle with legs {m('a')}, {m('b')} and hypotenuse {m('c')} (the side across from the right angle): {m('a')}² + {m('b')}² = {m('c')}².</p>
{eq("a² + b² = c²")}
{mini(("Pythagorean triples", "3-4-5, 5-12-13, 8-15-17, 7-24-25 and their multiples (6-8-10, 9-12-15…)."), ("Distance formula", f"It's just Pythagoras on the grid: {m('d')} = √(({m('x')}₂ − {m('x')}₁)² + ({m('y')}₂ − {m('y')}₁)²). Midpoint = average the coordinates."))}
{steps("Distance from (1, 2) to (7, 10)", [
 ("a|Δx = 7 − 1|s  b|Δy = 10 − 2|v", "Find the run and the rise."),
 ("c|6|s  d|8|v", "Δx = 6, Δy = 8."),
 ("e|√(6² + 8²)|e", "They are the legs of a right triangle."),
 ("f|√100|e", "36 + 64 = 100."),
 ("g|10|g", "d = 10 (a 3-4-5 triangle scaled by 2)."),
])}
''', pill=("c", "5.1"))

SPEC = topic("special", "Special right triangles", f'''
{mini(("45°-45°-90°", f"Sides 1 : 1 : √2. A square cut on its diagonal. Legs {m('x')}, hypotenuse {m('x')}√2."), ("30°-60°-90°", f"Sides 1 : √3 : 2. Half an equilateral triangle. Short leg {m('x')} (across from 30°), long leg {m('x')}√3, hypotenuse 2{m('x')}."))}
{worked("A 30-60-90 triangle has hypotenuse 14. Find both legs.", "Short leg = 14/2 = 7. Long leg = 7√3 ≈ 12.1.")}
{box("tip", "Why these matter", "These two triangles give you the exact values on the unit circle in precalc: sin 30° = 1/2, cos 45° = √2/2, sin 60° = √3/2.")}
''', pill=("c", "5.2"))

TRIG = topic("sohcahtoa", "SOH-CAH-TOA", f'''
<p>For an acute angle θ in a right triangle:</p>
{table(["Ratio", "Definition", "Memory"], [["sin θ", "opposite / hypotenuse", "SOH"], ["cos θ", "adjacent / hypotenuse", "CAH"], ["tan θ", "opposite / adjacent", "TOA"]])}
{lab(type="circle", deg=35)}
<p>In the unit circle above, the hypotenuse is 1, so the legs <i>are</i> cos θ (horizontal) and sin θ (vertical). That's the bridge into precalc.</p>
{steps("Find x: hypotenuse 12, angle 40°, x opposite", [
 ("a|sin 40°|s  b|=  c|x / 12|v", "Opposite and hypotenuse → sine."),
 ("d|12 · sin 40°|e  b|=  e|x|v", "Multiply both sides by 12."),
 ("f|12 · 0.643|e  b|=  e|x|v", "Calculator in DEGREE mode: sin 40° ≈ 0.643."),
 ("g|x ≈ 7.71|g", "x ≈ 7.71."),
])}
<p>To find an <b>angle</b>, use the inverse: if tan θ = 3/4, then θ = tan⁻¹(3/4) ≈ 36.9°.</p>
{box("trap", "Calculator mode", "Degrees vs radians is the #1 lost-points mistake. sin 30 in radian mode gives −0.988, not 0.5.")}
''', pill=("p", "5.3"))

GEO = topic("geo", "Area, volume and circles", f'''
{table(["Shape", "Formula"], [["Triangle", "A = ½bh"], ["Circle", "A = πr², C = 2πr"], ["Trapezoid", "A = ½(b₁ + b₂)h"], ["Cylinder", "V = πr²h"], ["Cone", "V = ⅓πr²h"], ["Sphere", "V = ⁴⁄₃πr³, S = 4πr²"], ["Rectangular box", "V = lwh"]])}
<p>A <b>circle</b> with center ({m('h')}, {m('k')}) and radius {m('r')}: ({m('x')} − {m('h')})² + ({m('y')} − {m('k')})² = {m('r')}². It's the distance formula again.</p>
{lab(title="Circle equation", sub="Top half and bottom half: y = k ± √(r² − (x − h)²).", h=540, x=[-8, 8], y=[-6, 6], gx=1, gy=1, params={"r": [0.5, 5, 0.25, 3, "r"], "h": [-4, 4, 0.5, 1, "h"], "k": [-3, 3, 0.5, 0, "k"]}, fns=[fn("k+sqrt(r^2-(x-h)^2)", "(x − h)² + (y − k)² = r²"), dict(e="k-sqrt(r^2-(x-h)^2)", c="#2563EB", hide=True)], dots=[["h", "k", "center", "#EA580C"]], read=[["area πr² =", "pi*r^2"], ["circumference =", "2*pi*r"]])}
<p><b>Arc length</b> and <b>sector area</b> are fractions of the whole circle: for a central angle θ°, arc = (θ/360)·2π{m('r')}.</p>
''', pill=("c", "5.4"))

SUM = topic("summary-pre5", "Unit summary", mini(
 ("Right triangles", "a² + b² = c². Special: 1:1:√2 and 1:√3:2."),
 ("SOH-CAH-TOA", "sin = opp/hyp, cos = adj/hyp, tan = opp/adj. Inverse trig finds angles."),
 ("Coordinates", "Distance √(Δx² + Δy²); midpoint = averages; circle (x − h)² + (y − k)² = r²."),
 ("Formulas", "Area and volume table above. Use the calculator in degree mode for now."),
))
CH = [chapter("ch-pyth", "Right Triangles", "Triangles", [PYTH, SPEC]), chapter("ch-trig", "Trigonometry", "Trig", [TRIG]), chapter("ch-geo", "Geometry Toolkit", "Geometry", [GEO, SUM])]
close(12 * M.sin(M.radians(40)), 7.71); close(M.degrees(M.atan(.75)), 36.87)
PQ = [
 q("Legs 9 and 12. Hypotenuse?", ["15", "21", "√63", "18"], 0, "81 + 144 = 225.", "p"),
 q("Hypotenuse 13, one leg 5. Other leg?", ["12", "8", "√194", "18"], 0, "169 − 25 = 144.", "p"),
 q("Distance from (−2, 1) to (4, 9)?", ["10", "14", "√52", "8"], 0, "√(36 + 64).", "p"),
 q("Midpoint of (2, −4) and (8, 6)?", ["(5, 1)", "(3, 5)", "(10, 2)", "(6, 10)"], 0, "Average each coordinate.", "p"),
 q("45-45-90 with leg 6. Hypotenuse?", ["6√2", "12", "6√3", "3√2"], 0, "Leg × √2.", "p"),
 q("30-60-90 with short leg 5. Long leg?", ["5√3", "10", "5√2", "5/√3"], 0, "Short × √3.", "p"),
 q("sin θ = ?", ["opposite/hypotenuse", "adjacent/hypotenuse", "opposite/adjacent", "hypotenuse/opposite"], 0, "SOH.", "c"),
 q("Right triangle: opposite 3, adjacent 4. tan θ = ?", ["3/4", "4/3", "3/5", "4/5"], 0, "TOA.", "p"),
 q("Same triangle. cos θ = ?", ["4/5", "3/5", "3/4", "5/4"], 0, "Hypotenuse is 5.", "p"),
 q("sin 30° = ?", ["1/2", "√3/2", "√2/2", "1"], 0, "Short leg / hypotenuse = 1/2.", "c"),
 q("A 20 ft ladder makes a 70° angle with the ground. How high does it reach?", ["≈ 18.8 ft", "≈ 6.8 ft", "≈ 54.9 ft", "≈ 7.3 ft"], 0, "20 sin 70° ≈ 18.79.", "w"),
 q("Area of a circle with radius 4?", ["16π", "8π", "4π", "64π"], 0, "πr².", "p"),
 q("Center and radius of (x − 2)² + (y + 3)² = 25?", ["(2, −3), r = 5", "(−2, 3), r = 5", "(2, −3), r = 25", "(2, 3), r = 5"], 0, "Signs flip; r = √25.", "g"),
 q("Volume of a cylinder with r = 3, h = 10?", ["90π", "30π", "60π", "900π"], 0, "π·9·10.", "p"),
]
close(20 * M.sin(M.radians(70)), 18.79)
CHAL = [
 q("From 50 m away, the angle up to a tower's top is 32°. Height?", ["≈ 31.2 m", "≈ 26.5 m", "≈ 42.4 m", "≈ 80.0 m"], 0, "50 tan 32° ≈ 31.24.", "w"),
 q("Angle whose tangent is 1?", ["45°", "30°", "60°", "90°"], 0, "Equal legs.", "c"),
 q("Equilateral triangle with side 8. Area?", ["16√3", "32", "32√3", "8√3"], 0, "Height 4√3, area ½·8·4√3.", "p"),
 q("Arc length of a 60° arc on a circle with r = 9?", ["3π", "6π", "9π", "π"], 0, "(60/360)·18π.", "p"),
 q("Is (3, 4) inside, on, or outside x² + y² = 20?", ["Outside", "On", "Inside", "Can't tell"], 0, "9 + 16 = 25 > 20.", "g"),
 q("If sin θ = 0.6 for acute θ, then cos θ = ?", ["0.8", "0.4", "0.6", "1.6"], 0, "sin² + cos² = 1: cos² = 0.64.", "c"),
]
close(50 * M.tan(M.radians(32)), 31.24)
EXQ = [
 q("Legs 7 and 24. Hypotenuse?", ["25", "31", "√527", "17"], 0, "Triple 7-24-25.", "p"),
 q("Distance from (0, 0) to (5, 12)?", ["13", "17", "√119", "7"], 0, "5-12-13.", "p"),
 q("45-45-90 with hypotenuse 10. Each leg?", ["5√2", "10√2", "5", "10/√3"], 0, "10/√2.", "p"),
 q("30-60-90 with hypotenuse 18. Short leg?", ["9", "9√3", "6", "18√3"], 0, "Half the hypotenuse.", "p"),
 q("cos 60° = ?", ["1/2", "√3/2", "√2/2", "0"], 0, "Adjacent to 60° is the short leg.", "c"),
 q("Opposite 5, hypotenuse 13. sin θ?", ["5/13", "12/13", "5/12", "13/5"], 0, "SOH.", "p"),
 q("tan θ = 1.5. θ ≈ ?", ["56.3°", "33.7°", "1.5°", "48.6°"], 0, "tan⁻¹(1.5).", "p"),
 q("Circle with center (0, 4), radius 3?", ["x² + (y − 4)² = 9", "x² + (y + 4)² = 9", "x² + (y − 4)² = 3", "(x − 4)² + y² = 9"], 0, "Plug in h, k, r².", "g"),
 q("Circumference with diameter 10?", ["10π", "20π", "25π", "5π"], 0, "πd.", "p"),
 q("Volume of a sphere with r = 3?", ["36π", "27π", "12π", "108π"], 0, "⁴⁄₃π·27.", "p"),
 q("A ramp rises 3 ft over a 12 ft run. Angle?", ["≈ 14.0°", "≈ 76.0°", "≈ 14.5°", "≈ 25.0°"], 0, "tan⁻¹(3/12).", "w"),
 q("In any right triangle, sin²θ + cos²θ = ?", ["1", "0", "tan θ", "It depends"], 0, "(a² + b²)/c² = 1.", "c"),
]
close(M.degrees(M.atan(.25)), 14.04); close(M.degrees(M.atan(1.5)), 56.31)
FRQS = [
 {"q": "A kite string is 150 ft long and makes a 38° angle with the ground.", "parts": [
  {"p": "(a) How high is the kite? (ignore the person's height)", "rubric": [["Uses sine: h = 150 sin 38°", 1], ["≈ 92.3 ft", 1]], "answer": "≈ 92.35 ft."},
  {"p": "(b) How far is the person from the point directly below the kite?", "rubric": [["Uses cosine", 1], ["≈ 118.2 ft", 1]], "answer": "150 cos 38° ≈ 118.20 ft."},
  {"p": "(c) Check your answers with the Pythagorean theorem.", "rubric": [["92.35² + 118.2² ≈ 150²", 1]], "answer": "8528 + 13971 ≈ 22500 ✓"}]},
 {"q": "Points A(−1, 2) and B(5, 10).", "parts": [
  {"p": "(a) Find AB and the midpoint M.", "rubric": [["AB = 10", 1], ["M = (2, 6)", 1]], "answer": "√(36 + 64) = 10; (2, 6)."},
  {"p": "(b) Write the circle with diameter AB.", "rubric": [["Center M, radius 5", 1], ["(x − 2)² + (y − 6)² = 25", 1]], "answer": "(x − 2)² + (y − 6)² = 25."}]},
]
close(150 * M.sin(M.radians(38)), 92.35); close(150 * M.cos(M.radians(38)), 118.20)
build("pre-5", L, 5, "Geometry and Right-Triangle Trig", 'Triangles and <span class="hl">trig</span>', "The Pythagorean theorem, special right triangles, SOH-CAH-TOA and the geometry formulas precalc assumes you know.", "Before Precalc unit 5: right-triangle trigonometry, special triangles, distance and circles.", CH, PQ, CHAL, EXQ, FRQS, OUT)
