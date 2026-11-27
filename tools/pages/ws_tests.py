from ws_common import M, build_ws

def tbl(head, rows):
    return '<table class="dt"><tr>' + "".join(f"<th>{h}</th>" for h in head) + "</tr>" + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</table>"

# ---------------- SAT ----------------
SAT1 = [
 M("sat-grid", "Grid-in warm-up", "Student-produced responses: no answer choices, just type the number. Fractions are fine.",
   {"type": "calc", "pass": 0.6, "qs": [
    {"q": "If 4x + 3 = 2x + 15, what is the value of x?", "a": 6, "abs": 0, "x": "2x = 12."},
    {"q": "A line passes through (0, 3) and (4, 11). What is its slope?", "a": 2, "abs": 0, "x": "(11 − 3)/4."},
    {"q": "If x² = 49 and x < 0, what is x?", "a": -7, "abs": 0, "x": "The negative square root."},
    {"q": "A shirt costs $40 and is on sale for 15% off. What is the sale price, in dollars?", "a": 34, "abs": 0.001, "x": "40 × 0.85."},
    {"q": "What is the value of 3/4 + 5/6? (Enter a fraction or decimal.)", "a": 19 / 12, "tol": 0.003, "show": "19/12", "x": "9/12 + 10/12 = 19/12 ≈ 1.583."},
    {"q": "The system y = 2x + 1 and y = −x + 7 meets at (a, b). What is a + b?", "a": 7, "abs": 0, "x": "2x + 1 = −x + 7 → x = 2, y = 5."}]},
   win="On grid-ins there's no answer to check against, so plug your result back into the original equation.",
   hints=["You can type fractions like 19/12 or decimals like 1.583."]),
 M("sat-rw", "Reading and Writing sprint", "Eight short Reading and Writing questions in six minutes. One question per passage, just like the digital SAT.",
   {"type": "sprint", "time": 360, "pass": 0.75, "qs": [
    {"q": "The new bridge was expected to ease traffic. ______, congestion grew worse in its first year.<br>Which choice completes the text with the most logical transition?", "o": ["Similarly", "However", "For example", "Therefore"], "a": 1, "x": "The second sentence contradicts the expectation."},
    {"q": "The researchers collected samples from three ______ the river delta, the mountain lake, and the coastal marsh.", "o": ["sites:", "sites;", "sites,", "sites"], "a": 0, "x": "A colon introduces a list after a complete clause."},
    {"q": "Each of the volunteers ______ trained before the event.", "o": ["were", "was", "are", "have been"], "a": 1, "x": "The subject is \"each\", which is singular."},
    {"q": "The author's tone toward the new policy is <i>measured</i>: she lists both its benefits and its costs. As used here, \"measured\" most nearly means…", "o": ["calculated in units", "careful and balanced", "slow and rhythmic", "limited in amount"], "a": 1, "x": "Weighing benefits and costs is balanced."},
    {"q": "Bees rely on flowers for food; ______ many flowers rely on bees for pollination.", "o": ["in contrast,", "in turn,", "for instance,", "nevertheless,"], "a": 1, "x": "A reciprocal relationship: in turn."},
    {"q": "Dr. Lin's study, which followed 400 students over five ______ that sleep strongly predicts grades.", "o": ["years, found", "years found", "years; found", "years. Found"], "a": 0, "x": "Close the nonessential clause with a comma before the verb."},
    {"q": "A scientist claims coral reefs recover faster when fishing is banned nearby. Which finding would most directly support the claim?", "o": ["Reefs in no-fishing zones regrew 40% faster than nearby fished reefs", "Many people enjoy snorkeling near reefs", "Coral is made of tiny animals", "Fishing is popular in many countries"], "a": 0, "x": "It directly compares recovery with and without fishing."},
    {"q": "The committee will announce ______ decision on Monday.", "o": ["it's", "its", "their's", "its'"], "a": 1, "x": "Possessive its has no apostrophe."}]},
   win="Transitions, punctuation around clauses, subject–verb agreement and evidence questions make up a big share of the section."),
]
SAT2 = [
 M("sat-alg", "Algebra sprint", "Eight algebra and advanced-math questions in eight minutes. Type your answers.",
   {"type": "sprint", "time": 480, "pass": 0.75, "qs": [
    {"q": "If 3(x − 2) = 2x + 5, what is x?", "a": 11, "x": "3x − 6 = 2x + 5."},
    {"q": "f(x) = 2x² − 3x. What is f(4)?", "a": 20, "x": "32 − 12."},
    {"q": "What is the y-intercept of 6x + 3y = 12?", "a": 4, "x": "Set x = 0: 3y = 12."},
    {"q": "x² − 10x + 21 = 0. What is the larger solution?", "a": 7, "x": "(x − 3)(x − 7)."},
    {"q": "If 2ˣ = 64, what is x?", "a": 6, "x": "2⁶ = 64."},
    {"q": "A gym charges a $30 sign-up fee plus $25 per month. How many months does $205 cover?", "a": 7, "x": "(205 − 30)/25."},
    {"q": "For what value of k does x² + 6x + k have exactly one real root?", "a": 9, "x": "Discriminant 36 − 4k = 0."},
    {"q": "If (x + 3)² = x² + bx + 9 for all x, what is b?", "a": 6, "x": "Expand: x² + 6x + 9."}]},
   win="On the SAT, the fastest route is often recognizing structure: perfect squares, discriminants, intercepts."),
 M("sat-data", "Data, geometry and trig", "Six problem-solving and geometry questions. Type exact answers.",
   {"type": "calc", "pass": 0.6, "qs": [
    {"q": "A price rises from $80 to $100. By what percent did it increase?", "a": 25, "abs": 0, "unit": "%", "x": "20/80 = 0.25."},
    {"q": "The mean of 5 numbers is 12. Four of them are 10, 11, 13 and 14. What is the fifth?", "a": 12, "abs": 0, "x": "Total 60 − 48."},
    {"q": "A right triangle has legs 9 and 12. Length of the hypotenuse?", "a": 15, "abs": 0, "x": "3-4-5 scaled by 3."},
    {"q": "A circle has area 49π. What is its radius?", "a": 7, "abs": 0, "x": "πr² = 49π."},
    {"q": "In a right triangle, sin A = 3/5. What is cos A? (fraction or decimal)", "a": 0.8, "abs": 0.001, "show": "4/5", "x": "3-4-5 triangle: adjacent 4."},
    {"q": "A map scale is 1 cm : 25 km. Two towns are 7.2 cm apart on the map. Real distance in km?", "a": 180, "abs": 0, "x": "7.2 × 25."}]},
   win="Percent change, means, special right triangles and circle formulas — high-frequency SAT topics."),
 M("sat-mini", "Mini module", "Ten mixed questions, twelve minutes. Pace yourself: about 70 seconds each.",
   {"type": "sprint", "time": 720, "pass": 0.7, "qs": [
    {"q": "If 5x − 2 = 3x + 8, what is 2x?", "a": 10, "x": "2x = 10 directly."},
    {"q": "Which choice best combines the sentences? <i>The museum opened in 1990. It has welcomed millions of visitors.</i>", "o": ["The museum opened in 1990, it has welcomed millions of visitors.", "Since opening in 1990, the museum has welcomed millions of visitors.", "The museum, opened in 1990, and it has welcomed millions of visitors.", "Opening in 1990, millions of visitors have been welcomed by the museum."], "a": 1, "x": "B is grammatical with no dangling modifier."},
    {"q": "The ratio of cats to dogs at a shelter is 3:5. There are 40 animals. How many are cats?", "a": 15, "x": "3/8 × 40."},
    {"q": "Which equation has the same solutions as x² − 4 = 0?", "o": ["(x − 2)² = 0", "(x − 2)(x + 2) = 0", "x − 4 = 0", "x² = −4"], "a": 1, "x": "Difference of squares."},
    {"q": "What is 40% of 65?", "a": 26, "x": "0.4 × 65."},
    {"q": "A function is defined by g(x) = 3x − 1. What is g(g(2))?", "a": 14, "x": "g(2) = 5, g(5) = 14."},
    {"q": "Neither the players nor the coach ______ happy with the result.", "o": ["were", "was", "are being", "have been"], "a": 1, "x": "With neither/nor, the verb agrees with the nearer subject (coach)."},
    {"q": "A rectangle's length is twice its width and its perimeter is 36. What is its area?", "a": 72, "x": "6w = 36 → w = 6, l = 12."},
    {"q": "If y varies directly with x and y = 12 when x = 4, what is y when x = 7?", "a": 21, "x": "y = 3x."},
    {"q": "Which transition best fits? <i>Solar panels are cheaper than ever. ______, adoption has tripled since 2015.</i>", "o": ["Consequently", "Nevertheless", "In contrast", "For instance"], "a": 0, "x": "Cause → effect."}]},
   win="That's the feel of a real module: mixed difficulty, steady pacing, no getting stuck."),
]
build_ws("sat", "../../courses/sat/workshop.html", "SAT", 'The <span class="hl">SAT</span> workshop',
 "Timed sprints and grid-ins that feel like the real digital SAT. The clock is part of the training.",
 [("Warm-up", "Warm-up", SAT1), ("Under Pressure", "Timed", SAT2)], (), "Margin · SAT workshop · Not affiliated with the College Board")

# ---------------- ACT ----------------
SCI = tbl(["Temperature (°C)", "10", "20", "30", "40", "50"], [["Dissolved O₂ (mg/L)", "11.3", "9.1", "7.6", "6.4", "5.6"]])
SCI2 = tbl(["Trial", "Ramp angle (°)", "Time to roll 2 m (s)"], [["1", "10", "1.53"], ["2", "20", "1.09"], ["3", "30", "0.90"], ["4", "40", "0.79"]])
PASS = ('<div class="passage"><p>When the city planted 4,000 trees along its busiest streets, officials promised cooler summers. Three years later, sensors showed that shaded blocks were on average 4°C cooler at street level than unshaded ones. '
        'Residents, however, noticed something the sensors didn\'t record: people lingered. Shop owners reported more foot traffic, and benches that once sat empty filled up by mid-morning. '
        'The planners had set out to fix the temperature; almost by accident, they changed how the street was used.</p></div>')
ACT1 = [
 M("act-eng", "English sprint", "Eight English questions in five minutes: punctuation, grammar and concision.",
   {"type": "sprint", "time": 300, "pass": 0.75, "qs": [
    {"q": "The team finished the project early, they celebrated with pizza.", "o": ["NO CHANGE", "early; they", "early they", "early, and, they"], "a": 1, "x": "Two independent clauses: semicolon (or comma + and)."},
    {"q": "Which choice is most concise? <i>At this point in time, the store is currently closed.</i>", "o": ["NO CHANGE", "The store is closed now.", "At this point in time, the store is closed now.", "Currently, at this time, the store is closed."], "a": 1, "x": "Remove the redundancy."},
    {"q": "The flock of geese ______ south every fall.", "o": ["fly", "flies", "are flying", "have flown"], "a": 1, "x": "\"Flock\" is singular."},
    {"q": "My sister, who lives in Denver ______ a pilot.", "o": ["is", ", is", "; is", "— is"], "a": 1, "x": "Close the nonessential clause with a matching comma."},
    {"q": "Between you and ______, the plan won't work.", "o": ["I", "me", "myself", "mine"], "a": 1, "x": "Object of a preposition: me."},
    {"q": "The novel's themes include loss, hope, and ______.", "o": ["finding redemption", "redemption", "to redeem", "how people redeem"], "a": 1, "x": "Parallel nouns."},
    {"q": "If the writer deleted the sentence giving the bridge's length, the paragraph would lose…", "o": ["a detail that supports its claim about the bridge's size", "its main argument", "a transition", "nothing"], "a": 0, "x": "Specific numbers usually support a claim."},
    {"q": "The dogs wagged ______ tails.", "o": ["they're", "their", "there", "its"], "a": 1, "x": "Plural possessive pronoun."}]},
   win="ACT English rewards short, clear and grammatical. When in doubt, the shortest correct choice usually wins."),
 M("act-sci", "Science: read the data", "Answer from the tables. Type numbers.",
   {"type": "calc", "pass": 0.6, "qs": [
    {"q": SCI + "<br>How much dissolved oxygen (mg/L) is in water at 30°C?", "a": 7.6, "abs": 0.01, "x": "Read it straight from the table."},
    {"q": SCI + "<br>By how much (mg/L) does dissolved oxygen fall from 10°C to 50°C?", "a": 5.7, "abs": 0.01, "x": "11.3 − 5.6."},
    {"q": SCI + "<br>Estimate the dissolved oxygen at 25°C (to one decimal place).", "a": 8.35, "abs": 0.2, "show": "about 8.3–8.4", "x": "Halfway between 9.1 and 7.6."},
    {"q": SCI2 + "<br>Predict the time (s) at 50°, assuming the pattern continues (answer within 0.05 s).", "a": 0.72, "abs": 0.05, "show": "about 0.71–0.73", "x": "The drops shrink (0.44, 0.19, 0.11), so the next is a bit smaller: about 0.72 s."},
    {"q": SCI2 + "<br>Which trial number had the shortest time?", "a": 4, "abs": 0, "x": "Steepest ramp, fastest roll."}]},
   win="ACT Science is mostly reading tables and spotting trends. You rarely need outside science knowledge."),
]
ACT2 = [
 M("act-read", "Reading: one passage", "Read the passage, then answer five questions in four minutes.",
   {"type": "sprint", "time": 240, "pass": 0.8, "shuffle": False, "qs": [
    {"q": PASS + "The main idea of the passage is that the trees…", "o": ["failed to cool the streets", "cooled the streets and also changed how people used them", "were mainly planted for shop owners", "were too expensive"], "a": 1, "x": "Both effects are the point of the last sentence."},
    {"q": PASS + "According to the passage, shaded blocks were how much cooler at street level?", "o": ["2°C", "3°C", "4°C", "40°C"], "a": 2, "x": "Stated directly."},
    {"q": PASS + "The word \"lingered\" most nearly means…", "o": ["stayed longer", "complained", "hurried", "left"], "a": 0, "x": "Benches filled up: people stayed."},
    {"q": PASS + "The word \"however\" signals a shift from…", "o": ["data the sensors measured to effects people observed", "past to future", "cost to benefit", "one city to another"], "a": 0, "x": "From temperature data to human behaviour."},
    {"q": PASS + "The phrase \"almost by accident\" suggests the change in street use was…", "o": ["planned from the start", "an unintended result", "unwelcome", "temporary"], "a": 1, "x": "Not what the planners set out to do."}]},
   win="Find the main idea first, then go back to the text for every detail question."),
 M("act-math", "Math sprint", "Eight ACT math questions in eight minutes.",
   {"type": "sprint", "time": 480, "pass": 0.75, "qs": [
    {"q": "What is 15% of 240?", "o": ["24", "36", "30", "32"], "a": 1, "x": "0.15 × 240."},
    {"q": "Solve for x: 7 − 2x = 15.", "o": ["4", "−4", "11", "−11"], "a": 1, "x": "−2x = 8."},
    {"q": "Slope of the line 2y − 6x = 4?", "o": ["2", "3", "−3", "6"], "a": 1, "x": "y = 3x + 2."},
    {"q": "A triangle has angles 40° and 75°. The third angle?", "o": ["55°", "65°", "75°", "85°"], "a": 1, "x": "180 − 115."},
    {"q": "Which is equivalent to (x²)³ · x?", "o": ["x⁶", "x⁷", "x⁸", "x⁵"], "a": 1, "x": "x⁶ · x."},
    {"q": "The median of 3, 9, 4, 12, 7?", "o": ["4", "7", "8", "9"], "a": 1, "x": "Sorted: 3, 4, 7, 9, 12."},
    {"q": "log₁₀ 1000 = ?", "o": ["2", "3", "10", "100"], "a": 1, "x": "10³ = 1000."},
    {"q": "Area of a circle with diameter 10?", "o": ["10π", "25π", "100π", "5π"], "a": 1, "x": "r = 5, πr² = 25π."}]},
   win="Write down every intermediate step: ACT math traps are almost always careless slips, not hard ideas."),
]
build_ws("act", "../../courses/act/workshop.html", "ACT", 'The <span class="hl">ACT</span> workshop',
 "English, Math, Reading and Science sprints with real time pressure, plus data-reading practice for the Science section.",
 [("English and Science", "Eng & Sci", ACT1), ("Reading and Math", "Read & Math", ACT2)], (), "Margin · ACT workshop · Not affiliated with ACT, Inc.")
