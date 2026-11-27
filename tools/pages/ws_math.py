from ws_common import M, build_ws

def match(mid, title, brief, expr, params, target, show, x, y, win, hints, gx=1, gy=1):
    return M(mid, title, brief, {"type": "match", "expr": expr, "params": params, "target": target, "show": show, "x": x, "y": y, "gx": gx, "gy": gy, "tol": 0.012}, win=win, hints=hints)

G1 = [
 match("m-line", "Match the line", "Drag the sliders until your blue line sits exactly on the dashed orange target.", "m*x+b",
       {"m": [-4, 4, 0.5, 0, "m"], "b": [-6, 6, 0.5, 0, "b"]}, {"m": 1.5, "b": -2}, "y = {m}x + {b}", [-6, 6], [-8, 8],
       "Slope = rise/run = 3/2, and the line crosses the y-axis at −2.", ["Read the y-intercept first: where does the target cross the y-axis?", "From the intercept, go right 2 and count how far up the line goes."], 1, 2),
 match("m-vertex", "Match the parabola", "Vertex form: y = a(x − h)² + k. Find a, h and k.", "a*(x-h)^2+k",
       {"a": [-3, 3, 0.5, 1, "a"], "h": [-5, 5, 0.5, 0, "h"], "k": [-6, 6, 0.5, 0, "k"]}, {"a": -0.5, "h": 2, "k": 4}, "y = {a}(x − {h})² + {k}", [-6, 8], [-8, 8],
       "The vertex is (h, k) = (2, 4). It opens downward and is wider than y = x², so a = −0.5.", ["The vertex is the highest point. Its coordinates are (h, k).", "From the vertex, move 2 right: the graph drops by 2. a·2² = −2 → a = −0.5."], 1, 2),
 match("m-roots", "Match the zeros", "Factored form: y = a(x − p)(x − q). The zeros are where the graph crosses the x-axis.", "a*(x-p)*(x-q)",
       {"a": [-2, 2, 0.25, 1, "a"], "p": [-6, 6, 0.5, 0, "p"], "q": [-6, 6, 0.5, 0, "q"]}, {"a": 0.5, "p": -3, "q": 1}, "y = {a}(x − {p})(x − {q})", [-7, 5], [-8, 8],
       "Zeros at x = −3 and x = 1. At x = 0 the target is −1.5 = a(3)(−1), so a = 0.5.", ["Set p and q to the two x-intercepts first.", "Then use the y-intercept: y(0) = a·p·q."], 1, 2),
]
G2 = [
 match("m-exp", "Match the exponential", "y = a · bˣ. a is the starting value at x = 0, b is the growth factor per step.", "a*b^x",
       {"a": [0.5, 5, 0.5, 1, "a"], "b": [0.25, 3, 0.25, 1, "b"]}, {"a": 2, "b": 1.5}, "y = {a} · {b}ˣ", [-4, 5], [-1, 16],
       "a = 2 (the y-intercept) and each step right multiplies by 1.5: 2, 3, 4.5, 6.75…", ["Read y at x = 0: that's a.", "Compare y at x = 1 with y at x = 0: the ratio is b."], 1, 2),
 match("m-sin", "Match the wave", "y = A sin(B(x − C)) + D. Amplitude, frequency, shift, midline.", "A*sin(B*(x-C))+D",
       {"A": [0, 4, 0.5, 1, "A"], "B": [0.5, 3, 0.5, 1, "B"], "C": [-3, 3, 0.25, 0, "C"], "D": [-3, 3, 0.5, 0, "D"]}, {"A": 2, "B": 2, "C": 0.5, "D": 1}, "y = {A} sin({B}(x − {C})) + {D}", [-4, 4], [-4, 5],
       "Midline y = 1, amplitude 2, period π (so B = 2), and the wave starts its rise at x = 0.5.", ["The midline is halfway between the max and min.", "Period = 2π / B. Measure the distance between two peaks."], 1, 1),
 match("m-log", "Match the logarithm", "y = a · ln(x − h) + k. The vertical asymptote is at x = h.", "a*ln(x-h)+k",
       {"a": [-3, 3, 0.5, 1, "a"], "h": [-4, 4, 0.5, 0, "h"], "k": [-4, 4, 0.5, 0, "k"]}, {"a": 2, "h": -1, "k": 1}, "y = {a} ln(x − {h}) + {k}", [-3, 8], [-6, 6],
       "Asymptote at x = −1 gives h = −1. At x = 0, ln(1) = 0 so y = k = 1. Then a stretches it vertically: a = 2.", ["Find the vertical asymptote: that's h.", "One unit right of the asymptote, ln(1) = 0, so the graph passes through (h + 1, k)."], 1, 1),
]
G3 = [
 M("m-exact", "Exact values", "No calculator. Type exact numbers (fractions are fine, e.g. 1/2).",
   {"type": "calc", "pass": 0.6, "qs": [
    {"q": "log₂ 32 = ?", "a": 5, "abs": 0, "x": "2⁵ = 32."},
    {"q": "8^(2/3) = ?", "a": 4, "abs": 0, "x": "Cube root of 8 is 2; 2² = 4."},
    {"q": "sin(π/6) = ?", "a": 0.5, "abs": 0.001, "show": "1/2", "x": "30° in a 30-60-90 triangle: opposite/hypotenuse = 1/2."},
    {"q": "cos(π) = ?", "a": -1, "abs": 0.001, "x": "The point on the unit circle at π is (−1, 0)."},
    {"q": "Solve 3ˣ = 81.", "a": 4, "abs": 0, "x": "81 = 3⁴."},
    {"q": "ln(e³) = ?", "a": 3, "abs": 0, "x": "ln and eˣ undo each other."},
    {"q": "Slope of the line through (2, 5) and (6, −3)?", "a": -2, "abs": 0, "x": "(−3 − 5)/(6 − 2) = −8/4."}]},
   win="Exact values come up on every AP Precalc exam, including the no-calculator section."),
 M("m-sprint", "Algebra sprint", "Eight quick algebra questions in four minutes. Type numbers.",
   {"type": "sprint", "time": 240, "pass": 0.75, "qs": [
    {"q": "Solve 3x − 7 = 11.", "a": 6, "x": "3x = 18."},
    {"q": "If f(x) = x² − 2x, what is f(−3)?", "a": 15, "x": "9 + 6."},
    {"q": "What is the vertex x-coordinate of y = x² − 8x + 3?", "a": 4, "x": "x = −b/(2a) = 8/2."},
    {"q": "Simplify (2³ · 2⁴) / 2⁵ to a number.", "a": 4, "x": "2^(3 + 4 − 5) = 2²."},
    {"q": "The sum of the roots of x² − 5x + 6 = 0?", "a": 5, "x": "Roots 2 and 3 (or −b/a)."},
    {"q": "Evaluate √50 · √2.", "a": 10, "x": "√100."},
    {"q": "A quantity doubles every 3 years. Starting at 100, what is it after 9 years?", "a": 800, "x": "Three doublings: 100 · 2³."},
    {"q": "Solve |x − 4| = 0.", "a": 4, "x": "Only x = 4."}]},
   win="Fluency with the basics is what frees up time for the hard questions."),
]
build_ws("math", "../../courses/math/workshop.html", "Math", 'The <span class="hl">graphing</span> workshop',
 "Match target graphs by dragging sliders, find exact values without a calculator, and race an algebra sprint. If you can match a graph, you understand its equation.",
 [("Lines and Parabolas", "Polynomials", G1), ("Exponential, Trig and Logs", "Curves", G2), ("No Calculator", "Exact", G3)], ("wa.js", "math.js"), "Margin · Math workshop · Drag the sliders until the curves match")
