from math_common import *
import math as M
L = "AP Precalculus"; OUT = "../../courses/math/precalc-3.html"
P = M.pi

RAD = topic("radians", "Periodic functions, radians and the unit circle (3.1–3.3)", f'''
<p>A function is <b>periodic</b> with period {m('k')} if {m('f')}({m('x')} + {m('k')}) = {m('f')}({m('x')}): the pattern repeats every {m('k')} units. Tides, daylight, Ferris wheels.</p>
<p>A <b>radian</b> is the angle that cuts off an arc equal to the radius. A full turn is 2π radians = 360°, so multiply degrees by π/180.</p>
{table(["Degrees", "0°", "30°", "45°", "60°", "90°", "180°", "270°", "360°"], [["Radians", "0", "π/6", "π/4", "π/3", "π/2", "π", "3π/2", "2π"]])}
<p>On the unit circle, the point at angle θ is (cos θ, sin θ). So sin θ is the <b>height</b>, cos θ is the <b>horizontal position</b>, and tan θ = sin θ / cos θ is the <b>slope</b> of the terminal ray. Press the preset angles below and watch the exact values.</p>
{lab(type="circle", deg=60)}
{mini(("ASTC", "Which are positive: All in Quadrant I, Sine in II, Tangent in III, Cosine in IV."), ("Reference angle", "Find the acute angle to the x-axis, use the special triangle, then fix the sign by quadrant. sin(5π/6) = +sin(π/6) = 1/2."))}
''', pill=("c", "3.1"))

SINU = topic("sinusoids", "Sinusoidal functions (3.4–3.7)", f'''
<p>{m('f')}(θ) = {m('a')}·sin({m('b')}(θ + {m('c')})) + {m('d')} (or cos).</p>
{table(["Parameter", "Effect"], [[f"|{m('a')}|", "amplitude: half the distance from max to min"], [f"{m('b')}", f"period = 2π/|{m('b')}|"], [f"{m('c')}", f"phase shift: moves left {m('c')}"], [f"{m('d')}", "midline y = d"]])}
{lab(title="Sinusoid lab", sub="y = a·sin(b(x + c)) + d. Gray dashed is plain sin x.", x=[-6.2832, 6.2832], y=[-5, 5], gx=1.5708, gy=1, xpi=True, params={"b": [0.25, 3, 0.25, 1, "b"], "a": [-4, 4, 0.25, 2, "a"], "c": [-3.1416, 3.1416, 0.1309, 0, "c"], "d": [-3, 3, 0.25, 0, "d"]}, fns=[fn("sin(x)", "sin x", c="#94A3B8", dash=True), fn("a*sin(b*(x+c))+d", "y = a·sin(b(x + c)) + d", c="#2563EB")], hasym=["d"], read=[["amplitude", "abs(a)"], ["period", "2*pi/abs(b)"], ["midline y =", "d"]])}
{steps("Model: a Ferris wheel, 50 m wide, center 30 m up, one turn per 8 min, you start at the bottom", [
 ("a|h(t)|v  b|=  c|?|x", "Start with the shape: starting at the bottom is a flipped cosine."),
 ("a|h(t)|v  b|=  d|−a·cos(bt)|s  e|+ d|n", "Midline d = center height = 30."),
 ("a|h(t)|v  b|=  d|−a·cos(bt)|s  f|+ 30|n", "Amplitude a = radius = 25."),
 ("a|h(t)|v  b|=  g|−25 cos(bt)|s  f|+ 30|n", "Period 8 → b = 2π/8 = π/4."),
 ("a|h(t)|v  b|=  h|−25 cos(πt/4)|g  f|+ 30|g", "Check: h(0) = 5 (bottom), h(4) = 55 (top) ✓"),
])}
''', pill=("g", "3.4"))

TAN = topic("tangent", "Tangent, inverse trig and the reciprocal functions (3.8–3.11)", f'''
<p>tan θ = sin θ / cos θ. It's undefined where cos θ = 0, so tan has vertical asymptotes at θ = π/2 + {m('k')}π, and its period is π.</p>
{lab(title="Tangent", sub="y = a·tan(b·x). Period π/b; asymptotes where cos(bx) = 0.", x=[-6.2832, 6.2832], y=[-5, 5], gx=1.5708, gy=1, xpi=True, params={"b": [0.5, 2, 0.25, 1, "b"], "a": [0.25, 3, 0.25, 1, "a"]}, fns=[fn("a*tan(b*x)", "y = a·tan(bx)")], vasym=["pi/(2*b)", "-pi/(2*b)", "3*pi/(2*b)", "-3*pi/(2*b)"], read=[["period π/b =", "pi/b"]])}
{table(["Inverse", "Restricted domain of the original", "Output range"], [["sin⁻¹ x (arcsin)", "[−π/2, π/2]", "[−π/2, π/2]"], ["cos⁻¹ x (arccos)", "[0, π]", "[0, π]"], ["tan⁻¹ x (arctan)", "(−π/2, π/2)", "(−π/2, π/2)"]])}
<p>The restrictions make each one-to-one. That's why sin⁻¹(1/2) = π/6 only, while sin θ = 1/2 has infinitely many solutions.</p>
{steps("Solve 2 sin θ − 1 = 0 on [0, 2π)", [
 ("a|2 sin θ|v  b|− 1|n  c|=  d|0|n", "Isolate the trig function."),
 ("e|sin θ|v  c|=  f|1/2|n", "sin θ = 1/2: height one half."),
 ("g|θ = π/6|g  h|(QI)|x", "Reference angle π/6, sine positive in I and II."),
 ("g|θ = π/6|g  i|θ = 5π/6|g", "Quadrant II: π − π/6 = 5π/6. Two solutions in one period."),
])}
{mini(("Reciprocals", "sec θ = 1/cos θ, csc θ = 1/sin θ, cot θ = cos θ/sin θ. They have asymptotes wherever the original is 0."), ("Inequalities", "Solve the equation, mark the solutions on the circle or graph, then test which arcs satisfy the inequality."))}
''', pill=("p", "3.8"))

IDEN = topic("identities", "Trig identities (3.12)", f'''
{table(["Identity", "Formula"], [["Pythagorean", "sin²θ + cos²θ = 1 (÷cos² → tan²θ + 1 = sec²θ; ÷sin² → 1 + cot²θ = csc²θ)"], ["Sum", "sin(α ± β) = sin α cos β ± cos α sin β"], ["", "cos(α ± β) = cos α cos β ∓ sin α sin β"], ["Double angle", "sin 2θ = 2 sin θ cos θ; cos 2θ = cos²θ − sin²θ = 1 − 2sin²θ = 2cos²θ − 1"]])}
{steps("Simplify (1 − cos²θ) / (sin θ cos θ)", [
 ("a|(1 − cos²θ)|v  b|/  c|(sin θ cos θ)|s", "Pythagorean identity on the top."),
 ("d|sin²θ|v  b|/  c|(sin θ cos θ)|s", "1 − cos²θ = sin²θ."),
 ("e|sin θ|v  b|/  f|cos θ|s", "Cancel one sin θ."),
 ("g|tan θ|g", "= tan θ."),
])}
{lab(title="Is it really an identity?", sub="If the two graphs lie on top of each other everywhere, the identity holds. Slide k: sin(2x) vs k·sin x cos x.", x=[-6.2832, 6.2832], y=[-2.5, 2.5], gx=1.5708, gy=0.5, xpi=True, params={"k": [0, 3, 0.25, 1, "k"]}, fns=[fn("sin(2*x)", "sin 2x"), fn("k*sin(x)*cos(x)", "k·sin x·cos x", dash=True)])}
''', pill=("p", "3.12"))

POLAR = topic("polar", "Polar coordinates and graphs (3.13–3.15)", f'''
<p>A polar point ({m('r')}, θ) means: turn θ, then go {m('r')}. Convert with {m('x')} = {m('r')} cos θ, {m('y')} = {m('r')} sin θ, {m('r')}² = {m('x')}² + {m('y')}², tan θ = {m('y')}/{m('x')}.</p>
<p>A polar function {m('r')} = {m('f')}(θ) is graphed by sweeping θ. In the labs below, the left panel is the polar curve and the right panel is the same function drawn as {m('r')} vs θ. Distance from the origin increases where {m('r')} is positive and increasing (or negative and decreasing).</p>
{lab(type="polar", title="Limaçon family", sub="Press Sweep: the point on the left traces the curve while the orange dot moves along r vs θ. a = b gives a cardioid, |a| < |b| an inner loop.", r="a+b*cos(t)", label="r = a + b·cos θ", params={"a": [-3, 4, 0.25, 1, "a"], "b": [-4, 4, 0.25, 2, "b"]}, R=5)}
{lab(type="polar", title="Roses", sub="r = a·cos(nθ). Odd n gives n petals, even n gives 2n.", r="a*cos(n*t)", label="r = a·cos(nθ)", params={"n": [1, 6, 1, 3, "n"], "a": [1, 4, 0.5, 3, "a"]}, R=4)}
{table(["Shape", "Equation"], [["Circle", "r = a or r = a cos θ"], ["Cardioid", "r = a(1 ± cos θ)"], ["Limaçon", "r = a + b cos θ"], ["Rose", "r = a cos(nθ): n petals if n odd, 2n if n even"]])}
''', pill=("g", "3.13"))

SUM = topic("summary-pc3", "Unit summary", mini(
 ("Unit circle", "(cos θ, sin θ). 360° = 2π. ASTC for signs."),
 ("Sinusoids", "a sin(b(x + c)) + d: amplitude |a|, period 2π/|b|, midline y = d."),
 ("Tangent & inverses", "tan period π, asymptotes at π/2 + kπ. Inverse trig outputs are restricted."),
 ("Polar", "x = r cos θ, y = r sin θ. Distance grows when r and its rate share a sign."),
))
CH = [chapter("ch-circle", "The Unit Circle", "Unit circle", [RAD]), chapter("ch-sin", "Sinusoids", "Sinusoids", [SINU]), chapter("ch-tan", "Tangent, Inverses, Identities", "Tan & inverses", [TAN, IDEN]), chapter("ch-polar", "Polar", "Polar", [POLAR, SUM])]

close(M.sin(5 * P / 6), .5)
PQ = [
 q("Convert 150° to radians.", ["5π/6", "3π/4", "2π/3", "5π/3"], 0, "150·π/180.", "p"),
 q("Convert 7π/4 to degrees.", ["315°", "225°", "135°", "330°"], 0, "7·45.", "p"),
 q("sin(π/3) = ?", ["√3/2", "1/2", "√2/2", "√3"], 0, "60° special triangle.", "c"),
 q("cos(2π/3) = ?", ["−1/2", "1/2", "−√3/2", "√3/2"], 0, "QII, reference π/3, cosine negative.", "p"),
 q("tan(π/4) = ?", ["1", "√2/2", "0", "Undefined"], 0, "sin = cos.", "c"),
 q("Amplitude and period of y = 3 sin(2x)?", ["3 and π", "3 and 2π", "2 and 3π", "6 and π"], 0, "Period 2π/2.", "g"),
 q("Midline of y = −2cos(x) + 5?", ["y = 5", "y = −2", "y = 3", "y = 7"], 0, "Vertical shift d.", "g"),
 q("Max of y = 4 sin x − 1?", ["3", "4", "5", "−1"], 0, "Midline −1 plus amplitude 4.", "g"),
 q("Period of y = tan(3x)?", ["π/3", "2π/3", "3π", "π"], 0, "π/b.", "g"),
 q("sin⁻¹(−1/2) = ?", ["−π/6", "7π/6", "11π/6", "5π/6"], 0, "Range of arcsin is [−π/2, π/2].", "p"),
 q("Solutions of cos θ = 0 on [0, 2π)?", ["π/2, 3π/2", "0, π", "π", "π/2"], 0, "Top and bottom of the circle.", "p"),
 q("sin²θ + cos²θ = ?", ["1", "0", "tan θ", "2"], 0, "Pythagorean identity.", "c"),
 q("sec θ = ?", ["1/cos θ", "1/sin θ", "cos θ/sin θ", "1/tan θ"], 0, "Reciprocal of cosine.", "c"),
 q("Rectangular coordinates of (r, θ) = (4, π/6)?", ["(2√3, 2)", "(2, 2√3)", "(4, π/6)", "(√3, 1)"], 0, "4cos(π/6), 4sin(π/6).", "p"),
 q("A tide's height has max 9 ft and min 1 ft. Amplitude and midline?", ["4 and y = 5", "8 and y = 5", "4 and y = 4", "9 and y = 1"], 0, "(9 − 1)/2 and (9 + 1)/2.", "w"),
]
CHAL = [
 q("Solve 2cos²θ − cos θ − 1 = 0 on [0, 2π).", ["0, 2π/3, 4π/3", "π/3, 5π/3", "0, π", "2π/3, 4π/3"], 0, "(2cos θ + 1)(cos θ − 1) = 0.", "p"),
 q("cos(75°) = ?", ["(√6 − √2)/4", "(√6 + √2)/4", "√3/4", "(√2 − 1)/2"], 0, "cos(45° + 30°) = cos45cos30 − sin45sin30.", "p"),
 q("A sinusoid has max at (1, 8) and the next min at (4, 2). Period?", ["6", "3", "4", "12"], 0, "Max to min is half a period.", "w"),
 q("sin θ = 3/5, θ in QII. cos θ = ?", ["−4/5", "4/5", "−3/4", "−3/5"], 0, "Cosine negative in QII.", "p"),
 q("r = 3 sin θ in rectangular form?", ["x² + (y − 1.5)² = 2.25", "x² + y² = 9", "y = 3", "x² + y² = 3x"], 0, "r² = 3r sin θ → x² + y² = 3y; complete the square.", "p"),
 q("On an interval where r > 0 and r is decreasing, the polar curve's distance from the origin is…", ["decreasing", "increasing", "constant", "undefined"], 0, "Distance is |r|.", "c"),
]
close(M.cos(M.radians(75)), (6 ** .5 - 2 ** .5) / 4)
EXQ = [
 q("225° in radians?", ["5π/4", "3π/4", "7π/4", "5π/3"], 0, "225/180 = 5/4.", "p"),
 q("sin(3π/2) = ?", ["−1", "1", "0", "Undefined"], 0, "Bottom of the circle.", "c"),
 q("cos(π/4) = ?", ["√2/2", "1/2", "√3/2", "1"], 0, "45°.", "c"),
 q("In which quadrant are sin < 0 and cos > 0?", ["IV", "II", "III", "I"], 0, "ASTC.", "c"),
 q("Period of y = cos(πx/6)?", ["12", "6", "π/6", "2π"], 0, "2π/(π/6).", "g"),
 q("y = sin(x − π/2) is y = sin x shifted…", ["right π/2", "left π/2", "up π/2", "down π/2"], 0, "Inside is opposite.", "g"),
 q("Range of y = 3cos x + 2?", ["[−1, 5]", "[−3, 3]", "[2, 5]", "[−1, 3]"], 0, "2 ± 3.", "g"),
 q("tan θ is undefined at θ = ?", ["π/2", "π", "0", "π/4"], 0, "cos = 0.", "c"),
 q("cos⁻¹(−1) = ?", ["π", "−π", "0", "2π"], 0, "Range [0, π].", "p"),
 q("Number of solutions of sin x = 0.3 on [0, 2π)?", ["2", "1", "3", "4"], 0, "QI and QII.", "c"),
 q("sin 2θ = ?", ["2 sin θ cos θ", "2 sin θ", "sin²θ − cos²θ", "sin θ + cos θ"], 0, "Double angle.", "c"),
 q("Polar coordinates of (0, −3)?", ["(3, 3π/2)", "(3, π/2)", "(−3, 0)", "(3, π)"], 0, "Straight down, distance 3.", "p"),
 q("How many petals does r = 2cos(3θ) have?", ["3", "6", "2", "9"], 0, "Odd n → n petals.", "g"),
 q("Daylight peaks at 15 h in June and bottoms at 9 h in December. A model's period (months) is…", ["12", "6", "24", "3"], 0, "One cycle per year.", "w"),
]
FRQS = [
 {"q": "A Ferris wheel has diameter 40 m, its lowest point is 2 m above the ground, and it turns once every 6 minutes. A rider boards at the lowest point at t = 0.", "parts": [
  {"p": "(a) Write h(t), the rider's height in meters.", "rubric": [["Midline 22, amplitude 20", 1], ["b = 2π/6 = π/3", 1], ["h(t) = −20cos(πt/3) + 22", 1]], "answer": "h(t) = 22 − 20cos(πt/3)."},
  {"p": "(b) Find all t in [0, 6] when the rider is 32 m up.", "rubric": [["cos(πt/3) = −1/2", 1], ["πt/3 = 2π/3 or 4π/3", 1], ["t = 2 and t = 4 minutes", 1]], "answer": "t = 2, 4."},
  {"p": "(c) On (0, 3), is h increasing or decreasing, and is it concave up or down near t = 1?", "rubric": [["Increasing (bottom to top)", 1], ["Concave up near t = 1 (below midline, speeding up)", 1]], "answer": "Increasing; at t = 1 the rider is below the midline (h = 12), where the graph is concave up."}]},
 {"q": "Let r(θ) = 1 + 2cos θ for 0 ≤ θ ≤ 2π.", "parts": [
  {"p": "(a) Find all θ where r = 0.", "rubric": [["cos θ = −1/2", 1], ["θ = 2π/3, 4π/3", 1]], "answer": "2π/3 and 4π/3 (the inner loop)."},
  {"p": "(b) On (π/2, 2π/3), is the distance from the origin increasing or decreasing? Explain.", "rubric": [["r > 0 there (r(π/2) = 1, r(2π/3) = 0)", 1], ["r decreasing → distance decreasing", 1]], "answer": "r is positive and decreasing, so the distance from the origin is decreasing."}]},
]
h = lambda t: 22 - 20 * M.cos(P * t / 3); close(h(2), 32); close(h(4), 32); close(h(1), 12)
build("precalc-3", L, 3, "Trigonometric and Polar Functions", 'Trig and <span class="hl">polar</span> functions', "Radians and the unit circle, sinusoidal models, tangent, inverse trig, identities and polar graphs.", "AP Precalculus Unit 3: trigonometric and polar functions with unit circle animation, sinusoid labs and an AP-style practice exam.", CH, PQ, CHAL, EXQ, FRQS, OUT, minutes=(35, 30), calc_note="Use a graphing calculator only where you'd be allowed one. ")
