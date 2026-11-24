from tp_common import *
from math_common import _j
C = "sat"; L = "SAT"; OUT = "../../courses/sat/sat-hardest.html"
TAGS = {"a": "Algebra", "m": "Advanced Math", "p": "Data", "g": "Geometry & trig", "r": "Reading", "w": "Writing"}
P = psg
DATA = {}
def dissect(hid, title, item, why, trap, stp, fast=None, dsm=None, rule=None, pill="m"):
    DATA[f"quiz-h-{hid}"] = balance(check([item]), len(hid))
    body = f'''<p class="sub">Try it first. Then open the dissection.</p>
<div class="quiz single" data-src="quiz-h-{hid}"></div>
<details class="dissect"><summary>Dissect it</summary>
<div class="dx-grid"><div class="dx why"><b>Why it's hard</b><p>{why}</p></div><div class="dx trap"><b>The trap</b><p>{trap}</p></div></div>
{stp}
{f'<div class="dx fast"><b>Fastest path</b><p>{fast}</p></div>' if fast else ""}
{f'<div class="dx dsm"><b>Desmos route</b><p>{dsm}</p></div>' if dsm else ""}
{f'<div class="dx rule"><b>Rule to steal</b><p>{rule}</p></div>' if rule else ""}
</details>'''
    return topic(f"h-{hid}", title, body, pill=(pill, "★"))

M1 = dissect("tangent", "The tangent line with a hidden parameter",
 g("In the xy-plane, the line y = kx − 4 intersects the parabola y = x² + 5 at exactly one point. If k > 0, what is the value of k?", ["6"], "Set them equal: x² − kx + 9 = 0. Exactly one point → discriminant 0: k² − 36 = 0 → k = 6.", "m"),
 "It looks like a graphing question, but it's really a discriminant question in disguise. Most students try to solve for x and get stuck because there are two unknowns.",
 "Answering −6 (ignoring k &gt; 0), or setting the two y-intercepts equal.",
 steps("Dissection", [
  ("a|x² + 5|v  b|=  c|kx − 4|s", "\"Intersect\" means set the two equations equal."),
  ("d|x² − kx + 9|e  b|=  e|0|n", "Move everything to one side: a quadratic in x."),
  ("f|\"exactly one point\"|x  g|→ b² − 4ac = 0|e", "One intersection = one solution = discriminant zero."),
  ("h|(−k)² − 4(1)(9) = 0|e", "a = 1, b = −k, c = 9."),
  ("i|k² = 36|v  j|k = 6|g", "k = ±6, and k &gt; 0."),
 ]), "Translate \"exactly one point\" into discriminant = 0 the moment you see it.",
 "Type y = kx − 4 and y = x² + 5, make k a slider, drag until the line just touches the parabola: k = 6.",
 "Line + curve + \"exactly one / no / two points\" → set equal, use the discriminant.")

M2 = dissect("infinite", "Infinitely many solutions with two unknown constants",
 g("In the equation a(2x − 3) + 4 = 6x − b, a and b are constants. If the equation has infinitely many solutions, what is the value of a + b?", ["8"], "Infinitely many → the two sides are identical. 2a = 6 → a = 3. Constants: −3a + 4 = −b → −5 = −b → b = 5. a + b = 8.", "a"),
 "There are three letters and one equation, so it feels unsolvable. The phrase \"infinitely many solutions\" is the extra information.",
 "Trying to solve for x. Any value of x is a solution; x isn't the point.",
 steps("Dissection", [
  ("a|a(2x − 3) + 4|s  b|=  c|6x − b|v", "Infinitely many solutions means both sides are the same expression."),
  ("d|2a·x − 3a + 4|s  b|=  c|6x − b|v", "Distribute the left side."),
  ("e|x-terms: 2a = 6|e  f|constants: −3a + 4 = −b|e", "Match the coefficients of x, then the constants."),
  ("g|a = 3|g  h|−9 + 4 = −b → b = 5|g", "Solve each."),
  ("i|a + b = 8|g", "Answer what they asked: a + b."),
 ]), "Match coefficients. Two equations, two unknowns.",
 None, "Infinitely many → match every coefficient. No solution → x-coefficients match, constants don't.", pill="a")

M3 = dissect("noreal", "No real solutions: a range, not a value",
 q("The equation x² − 2kx + 4k + 5 = 0 has no real solutions. Which of the following could be the value of k?", ["2", "−1", "−3", "6"], 0, "b² − 4ac = 4k² − 16k − 20 < 0 → k² − 4k − 5 < 0 → (k − 5)(k + 1) < 0 → −1 < k < 5. Only 2 works.", "m"),
 "You have to set up an inequality with the discriminant, then solve a quadratic inequality. Two layers.",
 "−1: it makes the discriminant exactly 0 (one real solution), not negative.",
 steps("Dissection", [
  ("a|\"no real solutions\"|x  b|→ b² − 4ac < 0|e", "Translate the phrase."),
  ("c|(−2k)² − 4(1)(4k + 5) < 0|e", "a = 1, b = −2k, c = 4k + 5."),
  ("d|4k² − 16k − 20 < 0|v", "Expand."),
  ("e|(k − 5)(k + 1) < 0|v", "Divide by 4, factor."),
  ("f|−1 < k < 5|g", "A product is negative between its zeros. Only 2 is in range."),
 ]), "Plug each choice into b² − 4ac. Only k = 2 gives a negative number (16 − 32 − 20 = −36).",
 "Type y = x² − 2kx + 4k + 5 with a k slider. Set k to each choice: the parabola floats above the x-axis only for k = 2.",
 "Backsolving answer choices into the discriminant is often faster than solving the inequality.")

M4 = dissect("exprewrite", "Rewriting an exponential to reveal the rate",
 q("A town's population t years from now is modeled by P(t) = 1,200(1.21)^(t/2). Which equivalent form shows the yearly growth factor as a constant?", ["P(t) = 1,200(1.1)ᵗ", "P(t) = 1,200(1.105)ᵗ", "P(t) = 1,200(1.21)^(2t)", "P(t) = 1,200(0.605)ᵗ"], 0, "1.21^(t/2) = (1.21^(1/2))ᵗ = 1.1ᵗ: 10% per year.", "m"),
 "The rate is hidden inside a fractional exponent. You need exponent rules, not just the growth formula.",
 "1.105: halving the 21% growth. Growth compounds, so you take a square root, not half.",
 steps("Dissection", [
  ("a|(1.21)|s  b|^(t/2)|v", "Use (b^m)^n = b^(mn) in reverse."),
  ("c|(1.21^(1/2))|s  d|^t|v", "Split t/2 into (1/2)·t."),
  ("e|(1.1)|g  d|^t|v", "√1.21 = 1.1."),
  ("f|10% per year|g", "1.1 = 1 + 0.10."),
 ]), None, "Graph y = 1200(1.21)^(x/2) and each choice; only 1200(1.1)^x lies on top of it.",
 "Exponent of t/n → take the nth root of the base to get the per-unit factor.")

M5 = dissect("circle", "A circle with an unknown constant",
 g("In the xy-plane, the graph of x² + y² − 10x + 4y = k is a circle with radius 7. What is the value of k?", ["20"], "(x − 5)² + (y + 2)² = k + 25 + 4. Radius 7 → k + 29 = 49 → k = 20.", "g"),
 "You must complete the square twice AND remember to add the same amounts to the right side.",
 "49 or 7: forgetting that completing the square adds 25 + 4 to the right side.",
 steps("Dissection", [
  ("a|x² − 10x|v  b|+ y² + 4y|s  c|= k|n", "Group x terms and y terms."),
  ("a|x² − 10x + 25|v  b|+ y² + 4y + 4|s  c|= k + 25 + 4|n", "Half of −10 is −5 (square 25); half of 4 is 2 (square 4). Add both to each side."),
  ("d|(x − 5)²|v  e|+ (y + 2)²|s  f|= k + 29|n", "Now it's in standard form."),
  ("g|r² = 49|e  h|k = 20|g", "k + 29 = 49."),
 ]), None, "Type the equation with a k slider; drag until the circle's width is 14 (radius 7).",
 "Whatever you add to complete the square on the left goes on the right too.", pill="g")

M6 = dissect("nosol", "No solution: signs matter",
 g("In the system ax + 3y = 7 and 4x − 6y = 5, a is a constant. If the system has no solution, what is the value of a?", ["-2"], "No solution → parallel lines: ratios of x and y coefficients equal: a/4 = 3/(−6) → a = −2. Check constants: −2x + 3y = 7 → ×(−2): 4x − 6y = −14 ≠ 5 ✓.", "a"),
 "You must compare ratios, and one coefficient is negative.",
 "a = 2: ignoring the minus sign in −6y.",
 steps("Dissection", [
  ("a|ax + 3y = 7|s  b|4x − 6y = 5|v", "No solution → same slope, different intercept."),
  ("c|a/4|e  d|=|  e|3/(−6)|e", "Coefficients must be proportional."),
  ("f|a = −2|g", "a/4 = −1/2."),
 ]), "Rewrite both in slope form: y = (7 − ax)/3 and y = (4x − 5)/6. Slopes −a/3 and 2/3 → a = −2.",
 "Graph both with a slider on a; at a = −2 the lines are parallel.", "Parallel = same slope. Write slopes explicitly when signs are involved.", pill="a")

M7 = dissect("sumroots", "Sum of solutions without solving",
 g("What is the sum of the solutions to 2x² − 11x = 3x − 9?", ["7"], "2x² − 14x + 9 = 0. Sum of roots = −b/a = 14/2 = 7.", "m"),
 "The roots are irrational, so solving takes forever and invites arithmetic errors.",
 "11/2: using −b/a before moving everything to one side.",
 steps("Dissection", [
  ("a|2x² − 11x|v  b|=  c|3x − 9|s", "First, standard form."),
  ("d|2x² − 14x + 9 = 0|e", "Subtract 3x, add 9."),
  ("e|sum = −b/a|v", "Sum of roots of ax² + bx + c."),
  ("f|14/2 = 7|g", ""),
 ]), None, "Graph y = 2x² − 11x and y = 3x − 9; add the two intersection x-values: 0.716 + 6.284 = 7.",
 "Sum = −b/a, product = c/a. Only after the equation equals zero.")

M8 = dissect("sd", "Transforming a data set",
 q("A data set has mean 20 and standard deviation 4. Each value is multiplied by 3, then 5 is added. What are the new mean and standard deviation?", ["Mean 65, SD 12", "Mean 65, SD 17", "Mean 60, SD 12", "Mean 65, SD 4"], 0, "Mean: 3·20 + 5 = 65. SD scales by 3 but isn't affected by adding 5: 12.", "p"),
 "Mean and SD react differently to adding vs multiplying.",
 "SD 17: applying \"+5\" to the spread.",
 steps("Dissection", [
  ("a|× 3|v  b|+ 5|s", "Two operations on every value."),
  ("c|mean: 20 → 60 → 65|e", "The mean follows both."),
  ("d|SD: 4 → 12 → 12|g", "Adding shifts everything equally, so spread doesn't change."),
 ]), None, "Test with a tiny list: stdev([16,24]) = 5.66; stdev([53,77]) = 16.97 = 3 × 5.66.",
 "Adding a constant: center moves, spread doesn't. Multiplying: both scale.", pill="p")

M9 = dissect("similar", "Similar triangles and area",
 g("In triangle ABC, D is on AB and E is on AC, with DE parallel to BC. AD = 4, DB = 6, and the area of triangle ADE is 12. What is the area of quadrilateral DBCE?", ["63"], "AB/AD = 10/4 = 2.5. Areas scale by 2.5² = 6.25: area ABC = 75. 75 − 12 = 63.", "g"),
 "Two traps at once: using DB instead of AB, and scaling area by the length ratio.",
 "30 (using 12 × 2.5) or 27 (using 6/4 ratio): the scale factor must be AB/AD and squared for area.",
 steps("Dissection", [
  ("a|DE ∥ BC|s  b|→ ΔADE ~ ΔABC|v", "Parallel lines make similar triangles."),
  ("c|scale = AB/AD = 10/4|e", "AB = AD + DB = 10."),
  ("d|area scale = (2.5)² = 6.25|e", "Areas scale by the square."),
  ("e|ABC = 75|v  f|DBCE = 75 − 12 = 63|g", "Subtract the small triangle."),
 ]), None, None, "Lengths ×k, areas ×k², volumes ×k³.", pill="g")

M10 = dissect("cofunction", "Sine equals cosine",
 g("In a right triangle, sin(x°) = cos((4x − 20)°). What is the value of x?", ["22"], "sin a = cos b when a + b = 90: x + 4x − 20 = 90 → x = 22.", "g"),
 "Looks like it needs inverse trig. It needs one identity.",
 "Setting x = 4x − 20 (x = 20/3).",
 steps("Dissection", [
  ("a|sin(x°)|v  b|=  c|cos((4x − 20)°)|s", "Complementary angles: sin θ = cos(90° − θ)."),
  ("d|x + (4x − 20) = 90|e", "The angles add to 90."),
  ("e|5x = 110|v  f|x = 22|g", ""),
 ]), None, "In degrees mode, graph y = sin(x) and y = cos(4x − 20); click the first positive intersection: x = 22.",
 "sin a = cos b ⇒ a + b = 90 (for acute angles).", pill="g")

M11 = dissect("nested", "Percent of a percent",
 g("x is 40% greater than y, and y is 20% less than z. x is what percent of z?", ["112"], "x = 1.4y and y = 0.8z → x = 1.12z → 112%.", "p"),
 "Two chained percent changes in words; easy to add instead of multiply.",
 "120% (adding +40 and −20).",
 steps("Dissection", [
  ("a|x = 1.4y|v  b|y = 0.8z|s", "\"40% greater\" = ×1.4; \"20% less\" = ×0.8."),
  ("c|x = 1.4(0.8z)|e", "Substitute."),
  ("d|x = 1.12z → 112%|g", ""),
 ]), "Pick z = 100: y = 80, x = 112.", None, "Percent changes multiply. Use 100 as a test number.", pill="p")

R1 = dissect("infer", "Inference: what MUST follow",
 q(P("Biologists compared beetles of one species living in a dry valley with beetles living in a wet forest nearby. Valley beetles had thicker shells. In lab tests, thicker shells sharply reduced water loss but gave no extra protection from the valley's main predator, a lizard. The biologists concluded that the thicker shells most likely <span class=blank></span>") + "Which choice most logically completes the text?", ["help the valley beetles survive dry conditions.", "evolved to protect valley beetles from lizards.", "make valley beetles slower than forest beetles.", "are found in every population of the species."], 0, "Water loss reduced; predator protection ruled out. So: dryness.", "r"),
 "Two plausible explanations are introduced, and the text quietly rules one out.",
 "\"Protect from lizards\": it sounds like what shells do, but the text says the lab tests found no extra protection.",
 steps("Dissection", [
  ("a|Fact 1: thicker shells in dry valley|s", "Set up a puzzle: why the difference?"),
  ("a|Fact 1|s  b|Fact 2: less water loss ✓|g", "Supports a dryness explanation."),
  ("a|Fact 1|s  b|Fact 2 ✓|g  c|Fact 3: no predator benefit ✗|x", "Rules out the predator explanation."),
  ("d|→ survive dry conditions|g", "Only the explanation left standing."),
 ]), None, None, "In completion questions, track which ideas the text supports and which it eliminates.", pill="r")

R2 = dissect("data", "Data that's true but irrelevant",
 q(P("Age group | Read daily, 2015 | Read daily, 2023", "13–17 | 30% | 48%", "18–29 | 35% | 38%", "30+ | 42% | 41%") + P("A researcher claims that the overall rise in daily reading between 2015 and 2023 was driven mainly by teenagers.") + "Which choice most effectively uses data from the table to support the claim?", ["The share of 13–17-year-olds who read daily rose 18 points, while the other groups changed by 3 points or less.", "In 2023, 48% of 13–17-year-olds read daily, more than the 38% of 18–29-year-olds.", "In 2015, the 30+ group had the highest share of daily readers.", "The 30+ group's share fell slightly from 42% to 41%."], 0, "\"Driven mainly by\" is about change across groups. Only A compares the changes.", "r"),
 "Every choice is accurate. Only one matches the specific claim, which is about CHANGE, compared across groups.",
 "B is true and mentions teens, but it compares levels in 2023, not changes.",
 steps("Dissection", [
  ("a|Claim: rise driven by teens|s", "Key words: \"rise\" (change over time) and \"mainly\" (compared to others)."),
  ("b|Needed: teen change ≫ others' change|e", "That's the evidence the claim requires."),
  ("c|A: +18 vs ≤ 3 points|g  d|B: 2023 levels only|x", "Only A provides it."),
 ]), None, None, "Highlight the claim's exact words, then demand data that matches each one.", pill="r")

R3 = dissect("wic", "A rare meaning of a common word",
 q(P("The new treatment did not cure the disease, but in most patients it did <span class=blank></span> its progress for several years, buying time for other therapies.") + "Which choice completes the text with the most logical and precise word?", ["arrest", "accelerate", "document", "reverse"], 0, "Arrest = stop or halt. \"Did not cure\" rules out reverse.", "r"),
 "The right answer is a familiar word used in an unfamiliar sense.",
 "\"Reverse\": it fits the positive tone, but reversing the disease would come close to curing it, which the text denies.",
 steps("Dissection", [
  ("a|did not cure|x  b|but did ___ its progress|s", "Contrast: something less than a cure."),
  ("c|prediction: \"slow\" or \"halt\"|e", "Predict before reading the choices."),
  ("d|arrest = to stop|g", "Second meaning: arrest a decline, arrest bleeding."),
 ]), None, None, "On hard vocab questions, expect a common word with a less common meaning.", pill="r")

W1 = dissect("semis", "Semicolons in a list",
 q(P("The tour stopped in Lagos, Nigeria; Accra, <span class=blank></span> and Dakar, Senegal.") + "Which choice completes the text so that it conforms to the conventions of Standard English?", ["Ghana;", "Ghana,", "Ghana:", "Ghana—"], 0, "List items that contain commas are separated by semicolons. The pattern is set by \"Nigeria;\".", "w"),
 "Most students learn \"semicolons join sentences\" and never learn their second job.",
 "\"Ghana,\": a comma makes it impossible to tell which city goes with which country.",
 steps("Dissection", [
  ("a|Lagos, Nigeria|s  b|;|e  c|Accra, Ghana|s  d|___|x  e|Dakar, Senegal|s", "Each list item has its own comma."),
  ("a|Lagos, Nigeria|s  b|;|e  c|Accra, Ghana|s  f|;|g  e|and Dakar, Senegal|s", "So items are separated by semicolons, matching the first one."),
 ]), None, None, "Match the punctuation already used in the sentence. The test plants the pattern.", pill="w")

W2 = dissect("synth", "Notes question with a sneaky goal",
 q('<div class="passage"><p>While researching a topic, a student has taken the following notes:</p><ul><li>Painter Alma Thomas worked in Washington, D.C.</li><li>She made abstract paintings from small, mosaic-like dabs of color.</li><li>Painter Sam Gilliam also worked in Washington, D.C.</li><li>He draped unstretched canvases from walls and ceilings.</li><li>Both artists were associated with the Washington Color School.</li></ul><p>The student wants to emphasize a similarity between the two artists. Which choice most effectively uses relevant information from the notes to accomplish this goal?</p></div>', ["Alma Thomas and Sam Gilliam both worked in Washington, D.C., and were associated with the Washington Color School.", "While Thomas painted with mosaic-like dabs, Gilliam draped unstretched canvases.", "Gilliam draped unstretched canvases from walls and ceilings.", "Thomas made abstract paintings from small, mosaic-like dabs of color."], 0, "Only A states what they share.", "w"),
 "Most notes describe differences. The most interesting choice (B) contrasts them.",
 "B: vivid and accurate, but it emphasizes a difference.",
 steps("Dissection", [
  ("a|Goal: similarity|e", "Underline the goal."),
  ("b|Shared: D.C. + Color School|g  c|Different: methods|x", "Sort the notes."),
  ("d|Choose the sentence built from shared facts|g", "A."),
 ]), None, None, "The goal is the only thing that matters. Ignore how good a sentence sounds.", pill="w")

INTRO = topic("intro", "How to use this page", f'''
<p>These are original questions built on the exact patterns that make the SAT's hardest questions hard. Try each one before opening its dissection. Every dissection shows <b>why it's hard</b>, <b>the trap answer</b>, a step-by-step breakdown, and a <b>rule</b> you can reuse.</p>
<p>For <b>real</b> official hard questions, use: the full practice tests in the Bluebook app, and College Board's free SAT Suite Question Bank (filter Difficulty: Hard). Run every hard miss through the same dissection: why hard, what trap, which rule.</p>
{box("tip", "What makes SAT questions hard", "Almost never obscure content. It's (1) a phrase you have to translate (\"exactly one point,\" \"infinitely many\"), (2) two steps where students stop after one, (3) a trap answer that results from a predictable mistake, or (4) in reading, choices that are all true but only one answers the exact question.")}
''', pill=("r", "★"))

CH = [chapter("ch-intro", "Start Here", "Start", [INTRO]),
      chapter("ch-alg", "Hard Algebra", "Algebra", [M2, M6]),
      chapter("ch-adv", "Hard Advanced Math", "Adv. Math", [M1, M3, M4, M7]),
      chapter("ch-geo", "Hard Geometry, Trig and Data", "Geo & data", [M5, M9, M10, M8, M11]),
      chapter("ch-rw", "Hard Reading and Writing", "R&W", [R1, R2, R3, W1, W2])]

PQ = [
 g("The line y = 2x + c is tangent to the parabola y = x² − 4x + 13. What is c?", ["4"], "x² − 6x + (13 − c) = 0 → 36 = 4(13 − c) → c = 4.", "m"),
 g("3(kx + 2) − 4x = 5x + m has infinitely many solutions. What is k + m?", ["9"], "3k − 4 = 5 → k = 3; m = 6. Sum 9.", "a"),
 q("For which value of c does x² + 6x + c = 0 have two distinct real solutions?", ["8", "9", "10", "12"], 0, "36 − 4c > 0 → c < 9.", "m"),
 q("f(t) = 500(1.44)^(t/2). Which shows the growth factor per unit of t?", ["500(1.2)ᵗ", "500(1.22)ᵗ", "500(2.88)ᵗ", "500(0.72)ᵗ"], 0, "√1.44 = 1.2.", "m"),
 g("x² + y² + 8x − 6y = k is a circle with radius 6. k = ?", ["11"], "(x + 4)² + (y − 3)² = k + 25 → 36.", "g"),
 g("The system 6x − 4y = 9 and bx + 2y = 1 has no solution. b = ?", ["-3"], "b/6 = 2/(−4) → b = −3.", "a"),
 g("Sum of the solutions to 3x² + 2x = 5x + 12?", ["1"], "3x² − 3x − 12 = 0 → −b/a = 3/3 = 1.", "m"),
 q("Each value in a data set is increased by 10. What happens to the standard deviation?", ["Stays the same", "Increases by 10", "Multiplies by 10", "Decreases"], 0, "Shift only.", "p"),
 g("cos(x°) = sin((2x + 15)°) in a right triangle. x = ?", ["25"], "x + 2x + 15 = 90.", "g"),
 g("a is 25% less than b, and b is 60% more than c. a is what percent of c?", ["120"], "0.75 × 1.6 = 1.2.", "p"),
]
CHAL = [
 g("y = ax² + 4 and y = 2x + 3 intersect at exactly one point. a = ?", ["1"], "ax² − 2x + 1 = 0 → 4 − 4a = 0.", "m"),
 q("The equation kx − 3 = 2(x + 1) + x has no solution. k = ?", ["3", "2", "−3", "5"], 0, "kx − 3 = 3x + 2: same x-coefficient, different constants.", "a"),
 g("A triangle's sides are scaled by 1.5. The original area was 24. New area?", ["54"], "24 × 2.25.", "g"),
 g("The product of the solutions of 4x² − 7x = 2x² + 15 is…", ["-7.5", "-15/2"], "2x² − 7x − 15 = 0 → c/a = −15/2.", "m"),
 q(P("Researchers observed that cities with more bike lanes have fewer traffic deaths. They concluded that bike lanes cause roads to be safer.") + "Which finding would most directly weaken this conclusion?", ["Cities with more bike lanes also have much lower speed limits on average.", "Bike lanes are expensive to build.", "Some cyclists still ride on sidewalks.", "Traffic deaths fell nationwide."], 0, "A confounding factor could explain both.", "r"),
 q(P("Authors traveling to the festival included Chimamanda Ngozi Adichie, author of <i>Americanah</i>; Ocean Vuong, author of <i>On Earth We're Briefly Gorgeous</i><span class=blank></span> and Min Jin Lee, author of <i>Pachinko</i>.") + "Which choice conforms to Standard English?", [";", ",", ":", "—"], 0, "Match the semicolon pattern.", "w"),
]
EX = [
 g("y = −x² + 6 and y = mx + 10 intersect exactly once, m > 0. m = ?", ["4"], "−x² − mx − 4 = 0 → x² + mx + 4 = 0 → m² = 16.", "m"),
 g("5(ax − 2) = 15x + b has infinitely many solutions. a − b = ?", ["13"], "5a = 15 → a = 3; b = −10. 3 − (−10).", "a"),
 q("x² − 4x + c = 0 has no real solutions. Which could be c?", ["5", "4", "0", "−3"], 0, "16 − 4c < 0 → c > 4.", "m"),
 q("V(t) = 9000(0.64)^(t/2). Yearly decay factor?", ["0.8", "0.32", "0.64", "0.82"], 0, "√0.64.", "m"),
 g("x² + y² − 2x + 10y = 10. Radius?", ["6"], "(x − 1)² + (y + 5)² = 36.", "g"),
 g("Data set mean 12, SD 3. Every value doubled, then 4 subtracted. New SD?", ["6"], "Only the ×2 affects SD.", "p"),
 g("sin(3x°) = cos((x + 10)°). x = ?", ["20"], "4x + 10 = 90.", "g"),
 q(P("Researchers hypothesized that a garden's increased bee visits were caused by a new flower variety. However, the garden also stopped using pesticides the same year.") + "What best describes the problem with the hypothesis?", ["Another change could explain the increase.", "Bees don't visit flowers.", "Pesticides attract bees.", "The variety is too new."], 0, "Confound.", "r"),
]
build(C, "sat-hardest", L, 0, "The Hardest Questions, Dissected", 'The hardest questions, <span class="hl">dissected</span>', "Original questions built on the SAT's hardest patterns, each broken down: why it's hard, the trap, the steps, the Desmos route, and the rule to steal.", "Hardest SAT question types dissected step by step: discriminant tricks, infinite solutions, exponential rewrites, circles, data traps, rare vocabulary and more.", CH, PQ, CHAL, EX, TAGS, OUT, minutes=12, exam_name="Gauntlet", extra_data=DATA, rules=["8 hard questions in 12 minutes.", "These are all \"Module 2\" difficulty.", "Desmos button is available."])
