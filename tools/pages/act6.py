from tp_common import *
C = "act"; L = "ACT"; OUT = "../../courses/act/act-6.html"
TAGS = {"d": "Reading data", "e": "Experiments", "v": "Viewpoints", "g": "Engineering"}
T = psg

SKILLS = topic("skills", "The four skills Science really tests", f'''
{mini(("Read the figure", "Check axes, units, legends. Many questions are just \"find the value at x = 30.\""), ("Trends", "As X increases, Y increases / decreases / peaks / levels off. Say it in words."), ("Interpolate / extrapolate", "Between data points: estimate in between. Beyond them: continue the trend (carefully)."), ("Experimental design", "Independent variable = what the scientist changes. Dependent = what's measured. Controls = kept the same. A control group gets no treatment."))}
{lab(title="Interpolation practice", sub="Measured: reaction rate vs temperature. Drag T to estimate the rate between data points.", x=[0, 60], y=[0, 50], gx=10, gy=10, params={"T": [0, 60, 1, 25, "T (°C)"]}, fns=[fn("0.0125*x^2+0.1*x+2", "rate (fitted)")], dots=[["10", "4.25", "", "#EA580C"], ["20", "9", "", "#EA580C"], ["30", "16.25", "", "#EA580C"], ["40", "26", "", "#EA580C"], ["50", "38.25", "", "#EA580C"], ["T", "0.0125*T^2+0.1*T+2", "≈{0.0125*T^2+0.1*T+2}", "#2563EB"]])}
{box("tip", "You don't need to read everything", "Go straight to the question, find the figure it names, answer it. Read the text only when a question asks about methods or viewpoints.")}
''', pill=("d", "6.1"))

D1 = T("Temperature (°C) | Enzyme activity at pH 5 | at pH 7 | at pH 9", "20 | 12 | 20 | 9", "30 | 25 | 41 | 18", "40 | 31 | 58 | 22", "50 | 14 | 30 | 10", "60 | 2 | 4 | 1")
SET1 = topic("set1", "Passage 1: data representation", f'''<p>Researchers measured the activity (in arbitrary units) of a digestive enzyme at different temperatures and pH levels.</p>{D1}''')
Q1 = [
 q("At pH 7, enzyme activity was highest at…", ["40°C", "30°C", "50°C", "60°C"], 0, "58 is the max.", "d"),
 q("At 30°C, the activity at pH 9 was…", ["18", "25", "41", "22"], 0, "Read the table.", "d"),
 q("At every temperature tested, which pH gave the highest activity?", ["pH 7", "pH 5", "pH 9", "It varied"], 0, "pH 7 column is always largest.", "d"),
 q("Based on the table, the activity at pH 7 and 35°C was most likely about…", ["50", "41", "58", "20"], 0, "Between 41 (30°C) and 58 (40°C).", "d"),
 q("Which best describes how activity at pH 5 changed from 20°C to 60°C?", ["It increased, then decreased", "It decreased steadily", "It increased steadily", "It stayed the same"], 0, "12 → 31 → 2.", "d"),
]
E2 = T("Light color | Avg. height after 4 weeks (cm) | Avg. leaves", "Red | 14.2 | 9", "Blue | 11.8 | 12", "Green | 6.1 | 5", "White (all colors) | 15.0 | 11")
SET2 = topic("set2", "Passage 2: research summaries", f'''<p><b>Experiment 1:</b> A student grew 40 bean seedlings, 10 under each of four light colors, all at the same brightness, temperature and watering schedule.</p>{E2}<p><b>Experiment 2:</b> The student repeated Experiment 1 with white light only, at 3 brightness levels: 50%, 100% and 150%. Heights after 4 weeks were 9.4, 15.0 and 17.1 cm.</p>''')
Q2 = [
 q("In Experiment 1, the independent variable was…", ["light color", "plant height", "temperature", "watering schedule"], 0, "What the student changed.", "e"),
 q("Which variable was held constant in Experiment 1?", ["Brightness", "Light color", "Number of leaves", "Plant height"], 0, "Same brightness for all.", "e"),
 q("Under which light color did plants grow the least?", ["Green", "Blue", "Red", "White"], 0, "6.1 cm.", "d"),
 q("Which colored light produced the most leaves?", ["Blue", "Red", "White", "Green"], 0, "12 leaves.", "d"),
 q("Based on Experiment 2, if brightness were 125%, height would most likely be…", ["between 15.0 and 17.1 cm", "less than 9.4 cm", "exactly 15.0 cm", "more than 20 cm"], 0, "Between the 100% and 150% results.", "d"),
 q("Plants absorb little green light. Do the results support this?", ["Yes, plants under green light grew least", "Yes, green light produced the most leaves", "No, green light grew tallest plants", "No, all colors grew equally"], 0, "Green → weakest growth.", "e"),
 q("Why did the student use 10 seedlings per color instead of 1?", ["To reduce the effect of individual plant differences", "To save time", "To use more light", "To change the variable"], 0, "Averages are more reliable.", "e"),
]
SET3 = topic("set3", "Passage 3: conflicting viewpoints", T(
 "In one summer, thousands of fish died in a lake. Two scientists propose explanations.",
 "<b>Scientist 1:</b> Fertilizer from nearby farms washed into the lake after heavy rain, feeding a huge bloom of algae. When the algae died, bacteria decomposed it and used up most of the oxygen in the water. The fish suffocated. Oxygen readings near the lake bottom fell below 2 mg/L during the die-off.",
 "<b>Scientist 2:</b> A record heat wave warmed the lake's surface water to 31°C. Warm water holds less dissolved oxygen, and many of the lake's fish species can't survive above 29°C. The die-off began the week the heat wave peaked, before any algae bloom was observed."))
Q3 = [
 q("Scientist 1 claims the fish died mainly because of…", ["low oxygen from decomposing algae", "high water temperature directly", "disease", "overfishing"], 0, "Algae → decomposition → low oxygen.", "v"),
 q("Both scientists would most likely agree that…", ["low oxygen could have contributed to the die-off", "fertilizer caused it", "the heat wave caused the algae bloom", "the fish died of disease"], 0, "Both mention oxygen.", "v"),
 q("Which finding would most support Scientist 2?", ["Fish also died in a nearby lake with no farms but the same heat wave", "Fertilizer levels in the lake doubled", "Algae covered the lake in June", "Oxygen was normal at the surface"], 0, "Same effect without fertilizer → heat is the cause.", "v"),
 q("Scientist 2 uses the timing of the die-off to argue that…", ["the algae bloom couldn't have caused the start of it", "algae caused it", "fertilizer arrived early", "the heat wave ended first"], 0, "Die-off began before any bloom.", "v"),
 q("Which data would best help decide between the two explanations?", ["Daily oxygen and temperature readings before and during the die-off", "The number of farms in the state", "The color of the fish", "Rainfall in a different year"], 0, "Tests both mechanisms over time.", "e"),
]
ENG = topic("engineering", "Engineering questions (new on the enhanced ACT)", f'''
<p>Some passages describe a design problem: constraints, tradeoffs, and tests of prototypes. Ask: what is being optimized, and what limit can't be broken?</p>
{T("Bridge design | Mass (g) | Max load before failure (N) | Cost ($)", "Truss | 120 | 450 | 18", "Arch | 150 | 520 | 25", "Beam | 90 | 210 | 9", "Suspension | 140 | 600 | 32")}
{worked("Requirement: hold at least 450 N and cost under $20. Which design?", "Only Truss (450 N, $18) meets both. Suspension holds the most but fails the cost limit.")}
''', pill=("g", "6.5"))
data = {"quiz-sc1": balance(check(Q1), 11), "quiz-sc2": balance(check(Q2), 12), "quiz-sc3": balance(check(Q3), 13)}
CH = [chapter("ch-skills", "Skills", "Skills", [SKILLS]),
      chapter("ch-s1", "Data Representation", "Data", [SET1, quiz_section("q-sc1", "Questions: passage 1", "Use the table above.", "quiz-sc1", TAGS)]),
      chapter("ch-s2", "Research Summaries", "Experiments", [SET2, quiz_section("q-sc2", "Questions: passage 2", "Use the experiments above.", "quiz-sc2", TAGS)]),
      chapter("ch-s3", "Conflicting Viewpoints", "Viewpoints", [SET3, quiz_section("q-sc3", "Questions: passage 3", "Use the viewpoints above.", "quiz-sc3", TAGS)]),
      chapter("ch-eng", "Engineering", "Engineering", [ENG])]
D4 = T("Altitude (km) | Air pressure (kPa) | Boiling point of water (°C)", "0 | 101 | 100", "2 | 79 | 93", "4 | 62 | 87", "6 | 47 | 81", "8 | 36 | 75")
BR = T("Bridge design | Mass (g) | Max load (N) | Cost ($)", "Truss | 120 | 450 | 18", "Arch | 150 | 520 | 25", "Beam | 90 | 210 | 9", "Suspension | 140 | 600 | 32")
EX = [
 q(D4 + "As altitude increases, the boiling point of water…", ["decreases", "increases", "stays the same", "increases then decreases"], 0, "100 → 75.", "d"),
 q(D4 + "At 3 km, air pressure is most likely about…", ["70 kPa", "79 kPa", "62 kPa", "85 kPa"], 0, "Between 79 and 62.", "d"),
 q(D4 + "If the trend continues, the boiling point at 10 km would be closest to…", ["69°C", "75°C", "80°C", "50°C"], 0, "Drops about 6°C per 2 km.", "d"),
 q(D4 + "According to the table, as air pressure decreases, boiling point…", ["decreases", "increases", "doesn't change", "can't be determined"], 0, "They fall together.", "d"),
 q(BR + "Which design has the highest load per gram of mass?", ["Suspension", "Arch", "Truss", "Beam"], 0, "600/140 ≈ 4.3; truss 3.75, arch 3.5, beam 2.3.", "g"),
 q(BR + "A design must be under 130 g and hold at least 400 N. Which works?", ["Truss", "Beam", "Arch", "Suspension"], 0, "Truss 120 g, 450 N.", "g"),
 q(T("A student dropped balls of different masses from 2 m and timed the fall. Mass (g): 50, 100, 200. Time (s): 0.64, 0.64, 0.65.") + "The results suggest that fall time…", ["doesn't depend much on mass", "doubles when mass doubles", "decreases with mass", "depends on color"], 0, "Nearly identical times.", "e"),
 q(T("A student dropped balls of different masses from 2 m and timed the fall. Mass (g): 50, 100, 200. Time (s): 0.64, 0.64, 0.65.") + "Which change would test whether drop height affects fall time?", ["Drop the same ball from different heights", "Use balls of different colors", "Use heavier balls from 2 m", "Time with two stopwatches"], 0, "Change only the height.", "e"),
 q(T("<b>Scientist 1:</b> fertilizer → algae → low oxygen killed the fish.", "<b>Scientist 2:</b> a heat wave warmed the water past what the fish could survive.") + "Which observation would weaken Scientist 1's explanation the most?", ["No algae bloom ever formed that summer", "Oxygen was low near the bottom", "Heavy rain fell in spring", "Farms used fertilizer"], 0, "No bloom → no algae decomposition.", "v"),
 q(T("<b>Scientist 1:</b> fertilizer → algae → low oxygen killed the fish.", "<b>Scientist 2:</b> a heat wave warmed the water past what the fish could survive.") + "Scientist 2 would predict that fish die-offs in this lake are most likely…", ["during unusually hot summers", "after every rainstorm", "in winter", "when fertilizer use falls"], 0, "Heat is the cause.", "v"),
]
check(EX)
build(C, "act-6", L, 6, "Science", 'ACT Science: <span class="hl">read the data</span>', "The skills Science really tests: reading figures, experimental design, conflicting viewpoints and the new engineering questions.", "ACT Science section: data representation, research summaries, conflicting viewpoints and engineering design with practice.", CH, [], [], EX, TAGS, OUT, minutes=10, extra_data=data, exam_name="Science set", rules=["10 questions in 10 minutes (ACT Science pace is about 1 per minute).", "No calculator on Science.", "No penalty for guessing."])
