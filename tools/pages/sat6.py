from tp_common import *
import math as M
C = "sat"; L = "SAT"; OUT = "../../courses/sat/sat-6.html"
TAGS = {"r": "Ratios & percents", "d": "Data & statistics", "p": "Probability", "g": "Geometry", "t": "Trig & circles"}

RATE = topic("rates", "Ratios, rates, percents and units", f'''
{mini(("Percent change", "(new − old)/old × 100. From 40 to 50 is +25%; from 50 to 40 is −20%."), ("Percent of a percent", "Two changes multiply: +20% then −20% gives 1.2 × 0.8 = 0.96, a 4% drop."), ("Unit conversions", "Multiply by fractions equal to 1 so units cancel: 90 km/h × (1000 m/1 km) × (1 h/3600 s) = 25 m/s."), ("Proportions", "Set up equal ratios and cross-multiply. Keep units in the same places."))}
{steps("Convert 72 km/h to m/s", [
 ("a|72 km/h|v", "Multiply by 1000 m per km."),
 ("a|72 km/h|v  b|× 1000 m/km|s", "km cancels."),
 ("c|72,000 m/h|v  d|× 1 h/3600 s|s", "Now hours cancel."),
 ("e|20 m/s|g", "72000 / 3600 = 20."),
])}
''', pill=("r", "6.1"))

STATS = topic("stats", "Statistics and data", f'''
<p><b>Mean</b> = sum/count. <b>Median</b> = middle value. <b>Range</b> = max − min. <b>Standard deviation</b> measures spread: data bunched near the mean → small SD.</p>
{box("tip", "Outliers", "Adding a very large value raises the mean a lot but the median only a little. That's why income is usually described by the median.")}
{lab(title="Line of best fit", sub="Scatterplot trend: y ≈ m·x + b. The slope is the predicted change in y per 1 unit of x.", x=[0, 10], y=[0, 100], gx=1, gy=10, params={"m": [2, 12, 0.5, 7, "m"], "b": [0, 40, 1, 20, "b"]}, fns=[fn("m*x+b", "y = mx + b")], dots=[["1", "28", "", "#EA580C"], ["2", "31", "", "#EA580C"], ["3", "42", "", "#EA580C"], ["4", "46", "", "#EA580C"], ["5", "53", "", "#EA580C"], ["6", "62", "", "#EA580C"], ["7", "66", "", "#EA580C"], ["8", "78", "", "#EA580C"], ["9", "82", "", "#EA580C"]], read=[["prediction at x = 12: ", "m*12+b"]])}
<p>Try to get the line through the middle of the dots (about m = 7, b = 20). Hours studied vs score: each extra hour ≈ +7 points.</p>
{mini(("Sampling", "Results from a <b>random sample</b> can be generalized to the population it was drawn from, and no further."), ("Cause vs association", "Only a <b>randomized experiment</b> (random assignment to treatments) supports cause-and-effect conclusions."), ("Margin of error", "An estimate of 42% ± 3% means the true value is plausibly between 39% and 45%. Bigger samples → smaller margin."))}
''', pill=("d", "6.2"))

PROB = topic("prob", "Probability from tables", f'''
<p>P(event) = favorable / total. In a two-way table, the hard part is picking the right <b>total</b>: \"given that\" means restrict to that row or column.</p>
<div class="passage"><table class="dt"><tr><th></th><th>Likes hiking</th><th>Doesn't</th><th>Total</th></tr><tr><th>Grade 11</th><td>30</td><td>50</td><td>80</td></tr><tr><th>Grade 12</th><td>45</td><td>25</td><td>70</td></tr><tr><th>Total</th><td>75</td><td>75</td><td>150</td></tr></table></div>
{worked("If a Grade 12 student is chosen at random, what's the probability they like hiking?", "Restrict to the Grade 12 row: 45/70 = 9/14 ≈ 0.643. <br>(Of all 150 students, P(Grade 12 and likes hiking) = 45/150 = 0.3: a different question.)")}
''', pill=("p", "6.3"))

GEO = topic("geo", "Geometry: angles, triangles, area and volume", f'''
<p>A reference sheet in the app gives area and volume formulas, the special right triangles, and that a circle has 360° (2π radians). You still need to know <b>when</b> to use them.</p>
{mini(("Angles", "Straight line 180°. Triangle angles sum to 180°. Parallel lines cut by a transversal: alternate interior angles are equal."), ("Similar triangles", "Same angles → sides in the same ratio. If sides scale by k, area scales by k² and volume by k³."), ("Right triangles", "a² + b² = c². 30-60-90: x, x√3, 2x. 45-45-90: x, x, x√2."), ("Volume", "Prism/cylinder: base area × height. Cone/pyramid: ⅓ of that. Sphere: ⁴⁄₃πr³."))}
{worked("Two similar triangles have corresponding sides 4 and 10. The smaller has area 12. Area of the larger?", "Scale factor 10/4 = 2.5; area scales by 2.5² = 6.25. 12 × 6.25 = 75.")}
''', pill=("g", "6.4"))

TRIG = topic("trig", "Right-triangle trig and circles", f'''
{lab(type="circle", deg=30)}
{mini(("SOH-CAH-TOA", "sin = opp/hyp, cos = adj/hyp, tan = opp/adj. Favorite SAT fact: sin x° = cos(90 − x)°."), ("Radians", "180° = π radians. Arc length = rθ (θ in radians). Sector area = ½r²θ."), ("Circle equation", "(x − h)² + (y − k)² = r². If it's expanded, complete the square in x and in y to find the center and radius."))}
{steps("Find the center and radius of x² + 6x + y² − 4y = 12", [
 ("a|x² + 6x|v  b|+  c|y² − 4y|s  d|= 12|n", "Complete the square in x: add (6/2)² = 9. In y: add (−4/2)² = 4. Add both to the right side too."),
 ("e|(x + 3)²|v  b|+  f|(y − 2)²|s  g|= 25|n", "12 + 9 + 4 = 25."),
 ("h|center (−3, 2)|g  i|r = 5|g", "Signs flip for the center; r = √25."),
])}
''', pill=("t", "6.5"))

HT = psg("Grade | Likes hiking | Doesn't | Total", "Grade 11 | 30 | 50 | 80", "Grade 12 | 45 | 25 | 70", "Total | 75 | 75 | 150")
CH = [chapter("ch-psda", "Problem-Solving and Data", "Data", [RATE, STATS, PROB]), chapter("ch-geo", "Geometry and Trig", "Geometry", [GEO, TRIG])]
PQ = [
 q("A price rises from $80 to $92. Percent increase?", ["15%", "12%", "13%", "8%"], 0, "12/80.", "r"),
 g("A car travels 150 miles in 2.5 hours. Average speed in mph?", ["60"], "150/2.5.", "r"),
 q("A map scale is 1 cm : 4 km. Two towns are 6.5 cm apart. Real distance?", ["26 km", "24 km", "10.5 km", "16 km"], 0, "6.5 × 4.", "r"),
 g("What is 30% of 30% of 200?", ["18"], "0.3 × 0.3 × 200.", "r"),
 q("Data: 3, 5, 5, 8, 9. What happens to the mean if 30 is added?", ["It increases a lot", "It stays the same", "It decreases", "It increases slightly"], 0, "Outlier pulls the mean up.", "d"),
 g("Median of 7, 2, 9, 4, 6, 10?", ["6.5", "13/2"], "Sorted: 2, 4, 6, 7, 9, 10 → (6 + 7)/2.", "d"),
 q("Set A: 10, 10, 10, 10. Set B: 1, 5, 15, 19. Which has the larger standard deviation?", ["B", "A", "Same", "Can't tell"], 0, "A has no spread.", "d"),
 q("A random sample of 500 voters in Ohio shows 54% support a bill. To which group can this be generalized?", ["Voters in Ohio", "All U.S. voters", "Only the 500 people", "Ohio residents under 18"], 0, "Only the population sampled.", "d"),
 q(HT + "A student is chosen at random from all 150. P(Grade 11 and doesn't like hiking)?", ["1/3", "5/8", "2/3", "5/15"], 0, "50/150.", "p"),
 g("A bag has 4 red and 6 blue marbles. Probability of drawing red?", ["0.4", "2/5", "4/10"], "4/10.", "p"),
 q("Two angles of a triangle are 48° and 67°. The third?", ["65°", "75°", "55°", "115°"], 0, "180 − 115.", "g"),
 g("Volume of a cylinder with radius 3 and height 4, divided by π?", ["36"], "π·9·4 = 36π.", "g"),
 q("In a right triangle, sin A = 3/5. What is cos A?", ["4/5", "3/4", "5/3", "3/5"], 0, "3-4-5 triangle.", "t"),
 q("If sin(x°) = cos(40°), x could be…", ["50", "40", "140", "90"], 0, "Complementary angles: x = 90 − 40.", "t"),
]
CHAL = [
 q("Population: 12,500 in 2020, then up 8%, then down 8%. Final?", ["12,420", "12,500", "12,580", "11,500"], 0, "12500 × 1.08 × 0.92 = 12,420.", "r"),
 g("A circle has equation x² − 8x + y² + 2y = 8. What is its radius?", ["5"], "(x − 4)² + (y + 1)² = 8 + 16 + 1 = 25.", "t"),
 q("A sector has radius 6 and central angle 2π/3 radians. Arc length?", ["4π", "2π", "12π", "6π"], 0, "rθ = 6 · 2π/3.", "t"),
 q("A survey's estimate is 63% with margin of error 4%. Which is supported?", ["The true value is plausibly between 59% and 67%", "Exactly 63% agree", "The true value is definitely above 60%", "4% of people lied"], 0, "Plausible interval only.", "d"),
 g("Two similar cones have heights 3 and 6. The small one holds 20 mL. How much does the large one hold?", ["160"], "Scale 2, volume ×8.", "g"),
 q("Researchers randomly assigned 200 volunteers to drink tea or water daily. The tea group had lower blood pressure. What can be concluded?", ["Tea likely caused lower blood pressure for people like the volunteers", "Tea lowers blood pressure for everyone", "Nothing, because it was an experiment", "Water raises blood pressure"], 0, "Random assignment → cause, but only for the volunteer population.", "d"),
]
close(12500 * 1.08 * .92, 12420)
EX = [
 q("A shirt is $45 after a 25% discount. Original price?", ["$60", "$56.25", "$33.75", "$70"], 0, "0.75p = 45.", "r"),
 g("Convert 3 hours 15 minutes to minutes.", ["195"], "180 + 15.", "r"),
 q("Recipe: 2 cups sugar for 5 cups flour. Sugar for 12 cups flour?", ["4.8 cups", "5 cups", "4 cups", "6 cups"], 0, "2/5 × 12.", "r"),
 g("Mean of 4, 8, 15, 16, 23?", ["13.2"], "66/5.", "d"),
 q("A store's sales grew from 200 to 260 units. Percent increase?", ["30%", "60%", "23%", "26%"], 0, "60/200.", "r"),
 q("Which best describes a scatterplot whose points rise from left to right closely around a line?", ["Strong positive linear association", "Weak negative", "No association", "Strong negative"], 0, "Rising and tight.", "d"),
 q("Line of best fit: y = 2.4x + 15 (x = hours, y = score). Interpret 2.4.", ["Predicted increase in score per extra hour", "Score with zero hours", "Total hours", "Average score"], 0, "Slope = rate.", "d"),
 g("Spinner with 8 equal sections numbered 1–8. P(number > 6)?", ["0.25", "1/4", "2/8"], "7 and 8.", "p"),
 q(HT + "A student who likes hiking is chosen at random. P(the student is in Grade 11)?", ["2/5", "3/8", "1/5", "30/80"], 0, "30/75.", "p"),
 q("Angles x and 3x form a straight line. x = ?", ["45°", "60°", "30°", "90°"], 0, "4x = 180.", "g"),
 g("A right triangle has legs 9 and 12. Hypotenuse?", ["15"], "3-4-5 × 3.", "g"),
 q("Area of a circle with diameter 10?", ["25π", "100π", "10π", "20π"], 0, "r = 5.", "g"),
 q("In a 30-60-90 triangle the short leg is 7. The hypotenuse?", ["14", "7√3", "7√2", "21"], 0, "2 × short leg.", "t"),
 q("Convert 135° to radians.", ["3π/4", "2π/3", "5π/6", "3π/2"], 0, "135/180 = 3/4.", "t"),
 g("Center of (x − 2)² + (y + 7)² = 16 is (2, k). k = ?", ["-7"], "Sign flips.", "t"),
]
build(C, "sat-6", L, 6, "Math: Data, Geometry and Trig", 'Data, shapes and <span class="hl">trig</span>', "Percents, rates and units, statistics and sampling, probability, geometry and right-triangle trig.", "SAT Math Problem-Solving and Data Analysis plus Geometry and Trigonometry with interactive labs.", CH, PQ, CHAL, EX, TAGS, OUT, minutes=20, exam_name="Data & Geometry set")
