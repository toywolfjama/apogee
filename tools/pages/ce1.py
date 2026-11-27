from lab_common import *
L = "Computer Engineering"
TAGS = {"c": "Concept", "p": "Calculation", "d": "Design", "r": "Reading circuits"}
OUT = "../../courses/comp-eng/ce-1.html"

BASICS = topic("basics", "Charge, voltage, current and resistance", f'''
<p>Every computer is, at the bottom, a machine that pushes electric charge around. Four quantities describe what is going on in any circuit:</p>
{table(["Quantity", "Symbol", "Unit", "What it means", "Water-pipe picture"], [
 ["Charge", "Q", "coulomb (C)", "Amount of electricity. One electron is −1.6 × 10⁻¹⁹ C.", "amount of water"],
 ["Voltage", "V", "volt (V)", "Energy per charge: the push that drives current. Always measured <i>between two points</i>.", "water pressure difference"],
 ["Current", "I", "ampere (A)", "Charge flowing past a point per second: I = Q / t.", "flow rate (litres per second)"],
 ["Resistance", "R", "ohm (Ω)", "How hard it is for current to flow.", "a narrow section of pipe"],
])}
<p>The relationship that ties them together is <b>Ohm's law</b>:</p>
{eq("V = I · R &nbsp;&nbsp;&nbsp; I = V / R &nbsp;&nbsp;&nbsp; R = V / I")}
<p>Power is the rate energy is used, in watts (W). Combine it with Ohm's law to get three versions, and pick the one that uses what you know:</p>
{eq("P = V · I = I² · R = V² / R")}
{worked("A phone charger supplies 5 V and 2 A. What power does it deliver, and how much energy in one hour?", "P = VI = 5 × 2 = 10 W. Energy = P × t = 10 W × 3600 s = 36,000 J (= 10 Wh = 0.01 kWh).")}
{worked("A 9 V battery is connected to a 450 Ω resistor. Find the current and the power turned into heat.", "I = V/R = 9/450 = 0.02 A = 20 mA. P = V²/R = 81/450 = 0.18 W.")}
{box("tip", "Unit prefixes", "m = milli = 10⁻³ (20 mA = 0.020 A), µ = micro = 10⁻⁶, n = nano = 10⁻⁹, k = kilo = 10³ (4.7 kΩ = 4700 Ω), M = mega = 10⁶, G = giga = 10⁹. A 3 GHz processor ticks 3 × 10⁹ times per second.")}
{box("trap", "Conventional current", "Engineers draw current flowing from + to −. Electrons actually drift the other way. Circuit math works the same either way as long as you stay consistent.")}
''', pill=("c", "1.1"))

SERPAR = topic("series-parallel", "Series, parallel and Kirchhoff's laws", f'''
<div class="grid2"><div class="mini"><h4>Series (one path)</h4><p>Same current through everything. Voltages add up to the source.</p><p class="mx">R = R₁ + R₂ + …</p></div>
<div class="mini"><h4>Parallel (several paths)</h4><p>Same voltage across every branch. Currents add up to the total.</p><p class="mx">1/R = 1/R₁ + 1/R₂ + …</p><p>Two resistors: R = R₁R₂ / (R₁ + R₂)</p></div></div>
{xlab("ohm", title="Series vs parallel lab", V=12, R1=20, R2=40)}
<p>Two rules work for <i>every</i> circuit, however tangled:</p>
<ol class="steps"><li><b>Kirchhoff's current law (KCL):</b> the current flowing into any junction equals the current flowing out. Charge doesn't pile up.</li>
<li><b>Kirchhoff's voltage law (KVL):</b> around any closed loop, the voltage rises and drops add to zero. Energy is conserved.</li></ol>
{steps("Voltage divider: 12 V across R₁ = 2 kΩ and R₂ = 4 kΩ in series", [
 ("a|R = 2k + 4k|e  b|= 6 kΩ|g", "Series, so add: total resistance 6 kΩ."),
 ("c|I = 12 / 6000|e  d|= 2 mA|g", "Ohm's law for the whole loop."),
 ("e|V₂ = 2 mA × 4 kΩ|e  f|= 8 V|g", "Voltage across R₂. KVL check: V₁ = 4 V, and 4 + 8 = 12 ✓"),
 ("g|V_out = V · R₂/(R₁ + R₂)|v", "The shortcut: the bigger resistor gets the bigger share of the voltage."),
])}
<p>The <b>voltage divider</b> is everywhere in computer engineering: reading a sensor, setting a reference level, scaling 5 V down to the 3.3 V a microcontroller can take.</p>
{worked("Three 300 Ω resistors are in parallel across 6 V. Total resistance and total current?", "1/R = 3/300, so R = 100 Ω. I = 6/100 = 0.06 A = 60 mA. Each branch carries 20 mA, and 3 × 20 = 60 ✓ (KCL).")}
{box("trap", "Parallel always shrinks", "Adding a resistor in parallel always lowers the total resistance (you've added another path). The total is always smaller than the smallest branch.")}
''', pill=("p", "1.2"), det=("Why the parallel formula works", "<p>Every branch has the same voltage V, so branch k carries Iₖ = V/Rₖ. By KCL the total current is I = V/R₁ + V/R₂ + … . The equivalent resistance is V/I, so 1/R = 1/R₁ + 1/R₂ + … .</p>"))

COMP = topic("components", "Capacitors, diodes and LEDs", f'''
{mini(("Capacitor", "Two plates that store charge: Q = CV, measured in farads (F). It blocks steady current but lets changes through. Charging through a resistor takes about τ = RC seconds to get ~63% of the way. DRAM stores each bit as charge on a tiny capacitor, which leaks, so it must be refreshed thousands of times a second."),
      ("Diode", "A one-way valve for current. It conducts forward (after about 0.7 V for silicon) and blocks reverse current. Used to protect circuits and to turn AC into DC."),
      ("LED", "A diode that glows. Each color has a forward voltage (red ≈ 2 V, blue ≈ 3 V). It always needs a series resistor to limit the current, or it burns out."),
      ("Semiconductor", "Silicon with a few impurity atoms added (doping). n-type has extra electrons, p-type has 'holes'. Where p meets n you get a diode; stack them and you get a transistor."))}
{worked("A red LED (forward voltage 2.0 V) should run at 20 mA from a 5 V pin. What resistor?", "The resistor takes the leftover voltage: 5 − 2 = 3 V. R = V/I = 3 / 0.020 = 150 Ω. Pick the next standard value up (150 Ω exists) so the current never exceeds 20 mA.")}
{worked("A 10 kΩ resistor charges a 100 µF capacitor. What is the time constant?", "τ = RC = 10,000 × 0.0001 = 1 s. After 1 s it's at 63%, after about 5τ = 5 s it's essentially full.")}
''', pill=("c", "1.3"))

TRANS = topic("transistors", "Transistors: the switch that makes computing possible", f'''
<p>A <b>transistor</b> is a switch with no moving parts, controlled by a voltage. Modern chips use <b>MOSFETs</b>, which have three terminals: the <b>gate</b> (the control), and the <b>source</b> and <b>drain</b> (the two ends of the switch).</p>
{table(["Type", "Turns ON when gate is…", "Good at passing", "Drawn with"], [["NMOS", "1 (high voltage)", "a strong 0", "no bubble"], ["PMOS", "0 (low voltage)", "a strong 1", "a bubble on the gate"]])}
<p><b>CMOS</b> (complementary MOS) pairs them up. PMOS transistors form a <b>pull-up network</b> between the output and the supply VDD; NMOS transistors form a <b>pull-down network</b> between the output and ground. For any input, exactly one network conducts.</p>
{xlab("cmos")}
<ol class="steps"><li><b>Inverter (NOT):</b> one PMOS on top, one NMOS on the bottom. A = 0 turns the PMOS on → Y = 1. A = 1 turns the NMOS on → Y = 0.</li>
<li><b>NAND:</b> NMOS in <i>series</i> (both must be on to pull Y down), PMOS in <i>parallel</i>. Y = 0 only when A = B = 1.</li>
<li><b>NOR:</b> NMOS in <i>parallel</i>, PMOS in <i>series</i>. Y = 1 only when A = B = 0.</li></ol>
{box("tip", "Why NAND and NOR, not AND and OR?", "A single CMOS stage naturally inverts. NAND takes 4 transistors; AND is a NAND followed by an inverter, so it takes 6. That's why chip designers think in NANDs and NORs.")}
<h3>Logic levels</h3>
<p>A wire doesn't carry a perfect 0 V or 3.3 V. Chips agree on ranges: anything below about 0.8 V reads as <b>0</b>, anything above about 2 V reads as <b>1</b> (for 3.3 V logic), with a forbidden zone in between. This <b>noise margin</b> is why digital circuits are reliable even when the voltages wobble.</p>
<h3>Power and Moore's law</h3>
<p>A CMOS gate uses almost no power while sitting still; it burns energy when it <b>switches</b>, charging and discharging tiny capacitances. The dynamic power of a chip is</p>
{eq("P ≈ α · C · V² · f")}
<p>where α is the fraction of gates switching each cycle, C the capacitance, V the supply voltage and f the clock frequency. Because power goes with V², lowering the voltage is the strongest lever. Around 2005 chips hit a "power wall": clock speeds stopped climbing past about 4 GHz, and designers switched to putting more cores on each chip.</p>
<p><b>Moore's law</b> is the observation (Gordon Moore, 1965/1975) that the number of transistors on a chip doubles roughly every two years. A modern processor has tens of billions of transistors.</p>
''', pill=("c", "1.4"), det=("Doubling every two years, in numbers", "<p>If a chip had 2,300 transistors in 1971 (the Intel 4004) and doubled every 2 years, after 50 years it would have 2,300 × 2²⁵ ≈ 7.7 × 10¹⁰, about 77 billion. Real chips in the early 2020s were in the tens of billions, so the trend held remarkably well for five decades.</p>"))

SUM = topic("summary-ce1", "Unit summary", mini(
 ("Ohm's law", "V = IR. Power P = VI = I²R = V²/R."),
 ("Series / parallel", "Series: R adds, same current. Parallel: 1/R adds, same voltage. KCL: current in = current out. KVL: voltages around a loop sum to 0."),
 ("Components", "Capacitor stores charge (τ = RC). Diode = one-way valve. LED needs a series resistor: R = (V − V_LED)/I."),
 ("Transistors", "NMOS on with 1, PMOS on with 0. CMOS: PMOS pull-up + NMOS pull-down. NAND = NMOS series + PMOS parallel. P ≈ αCV²f."),
))

CH = [chapter("ch-elec", "Electricity", "Electricity", [BASICS, SERPAR]),
      chapter("ch-comp", "Components", "Components", [COMP]),
      chapter("ch-trans", "Transistors and CMOS", "Transistors", [TRANS, SUM])]

close(9 / 450, .02); close(81 / 450, .18); close(3 / .02, 150); close(12 * 4 / 6, 8)
PQ = [
 q("A 12 V source drives 3 A through a heater. What is its resistance?", ["4 Ω", "36 Ω", "0.25 Ω", "15 Ω"], 0, "R = V/I = 12/3 = 4 Ω.", "p"),
 q("A 220 Ω resistor has 5 V across it. What current flows?", ["≈ 22.7 mA", "≈ 44 A", "≈ 1.1 A", "≈ 2.27 mA"], 0, "I = 5/220 = 0.0227 A ≈ 22.7 mA.", "p"),
 q("Power used by a 100 Ω resistor carrying 0.2 A?", ["4 W", "20 W", "2 W", "0.4 W"], 0, "P = I²R = 0.04 × 100 = 4 W.", "p"),
 q("Two resistors, 30 Ω and 60 Ω, are in series. Total resistance?", ["90 Ω", "20 Ω", "45 Ω", "1800 Ω"], 0, "Series resistances add.", "p"),
 q("The same 30 Ω and 60 Ω are in parallel. Total resistance?", ["20 Ω", "90 Ω", "45 Ω", "30 Ω"], 0, "R₁R₂/(R₁ + R₂) = 1800/90 = 20 Ω.", "p"),
 q("In a series circuit, which quantity is the same for every resistor?", ["Current", "Voltage", "Power", "Resistance"], 0, "There's only one path, so the same charge flows through each one.", "c"),
 q("Three currents enter a junction: 2 A, 3 A and 1 A. One wire leaves. How much current is in it?", ["6 A", "0 A", "2 A", "1 A"], 0, "KCL: current in = current out.", "c"),
 q("A voltage divider has R₁ = 1 kΩ (top) and R₂ = 3 kΩ (bottom) across 8 V. What is V_out across R₂?", ["6 V", "2 V", "4 V", "8 V"], 0, "V·R₂/(R₁ + R₂) = 8 × 3/4 = 6 V.", "p"),
 q("A blue LED (3 V) runs from 5 V at 10 mA. Series resistor?", ["200 Ω", "500 Ω", "300 Ω", "50 Ω"], 0, "(5 − 3)/0.010 = 200 Ω.", "p"),
 q("An NMOS transistor conducts when its gate is…", ["1 (high)", "0 (low)", "floating", "negative"], 0, "NMOS: high gate turns it on. PMOS is the opposite.", "c"),
 q("In a CMOS NAND gate, the NMOS transistors are connected…", ["in series", "in parallel", "one only", "to VDD"], 0, "Both NMOS must be on (A = B = 1) to pull the output to 0, which is a series connection.", "r"),
 q("Why does a CMOS gate use almost no power when its inputs aren't changing?", ["Only one of the pull-up and pull-down networks conducts, so there's no path from VDD to ground", "The transistors turn off the clock", "Resistors limit the current", "CMOS gates store power in capacitors"], 0, "Exactly one network is on, so no steady current flows through the gate.", "c"),
 q("If supply voltage is cut from 1.2 V to 0.9 V (all else equal), dynamic power becomes about…", ["56% of what it was", "75%", "90%", "33%"], 0, "P ∝ V²: (0.9/1.2)² = 0.5625.", "p"),
 q("A 1 MΩ resistor and a 1 µF capacitor make an RC circuit. Time constant?", ["1 s", "1 ms", "1 µs", "1000 s"], 0, "τ = RC = 10⁶ × 10⁻⁶ = 1 s.", "p"),
 q("Which statement about voltage is correct?", ["It is always measured between two points", "It flows through a resistor", "It is the same as current", "It is measured in amperes"], 0, "Voltage is a difference in electric potential, like a pressure difference.", "c"),
]
CHAL = [
 q("R₁ = 10 Ω is in series with a parallel pair R₂ = 20 Ω and R₃ = 20 Ω, across 20 V. Current through R₂?", ["0.5 A", "1 A", "2 A", "0.25 A"], 0, "Parallel pair = 10 Ω, total 20 Ω, so I = 1 A. It splits evenly between the equal branches: 0.5 A each.", "p"),
 q("A 3.3 V microcontroller must read a 5 V sensor through a divider with R₁ on top. If R₂ = 20 kΩ, what R₁ gives exactly 3.3 V?", ["≈ 10.3 kΩ", "≈ 13.3 kΩ", "≈ 6.6 kΩ", "≈ 30 kΩ"], 0, "3.3 = 5·20/(R₁ + 20) → R₁ + 20 = 30.3 → R₁ ≈ 10.3 kΩ.", "d"),
 q("How many transistors does a CMOS 3-input NAND gate need?", ["6", "3", "4", "9"], 0, "One NMOS and one PMOS per input: 3 NMOS in series + 3 PMOS in parallel.", "d"),
 q("A chip runs at 2 GHz and 1.0 V. Engineers raise the clock to 3 GHz but must raise the voltage to 1.2 V. Dynamic power multiplies by about…", ["2.16", "1.5", "1.2", "1.8"], 0, "(3/2) × (1.2/1.0)² = 1.5 × 1.44 = 2.16.", "p"),
 q("In a CMOS NOR gate with inputs A = 1, B = 0, which transistors conduct?", ["NMOS-A and PMOS-B", "PMOS-A and PMOS-B", "NMOS-B and PMOS-A", "All four"], 0, "NMOS turns on with 1 (A), PMOS with 0 (B). PMOS are in series, so the pull-up is broken; the parallel NMOS-A pulls Y to 0.", "r"),
 q("A resistor network draws 0.5 A from 10 V. A second identical network is added in parallel. New total power?", ["10 W", "5 W", "2.5 W", "20 W"], 0, "Each draws 0.5 A at 10 V = 5 W; two in parallel draw 10 W total.", "p"),
]
EXQ = [
 q("Ohm's law says…", ["V = IR", "P = IR", "I = VR", "R = VI"], 0, "Voltage = current × resistance.", "c"),
 q("A 6 V battery lights a bulb drawing 0.5 A. Power?", ["3 W", "12 W", "0.083 W", "6.5 W"], 0, "P = VI = 3 W.", "p"),
 q("Four 40 Ω resistors in parallel have total resistance…", ["10 Ω", "160 Ω", "40 Ω", "4 Ω"], 0, "Identical parallel resistors: R/n = 40/4.", "p"),
 q("Which law expresses conservation of charge at a junction?", ["Kirchhoff's current law", "Kirchhoff's voltage law", "Ohm's law", "Moore's law"], 0, "KCL: in = out.", "c"),
 q("In a parallel circuit every branch has the same…", ["voltage", "current", "resistance", "power"], 0, "All branches connect across the same two points.", "c"),
 q("A 2 kΩ and a 6 kΩ resistor in series across 16 V. Voltage across the 6 kΩ?", ["12 V", "4 V", "8 V", "16 V"], 0, "16 × 6/8 = 12 V.", "p"),
 q("An LED needs a series resistor because…", ["without it the current would grow too large and destroy the LED", "LEDs need a voltage drop of 0 V", "it makes the LED brighter", "it stores charge"], 0, "Once a diode turns on, small voltage increases cause huge current increases.", "c"),
 q("A PMOS transistor turns on when its gate is…", ["0", "1", "either", "neither"], 0, "PMOS is active-low.", "c"),
 q("A CMOS inverter's output is connected to VDD when the input is…", ["0", "1", "floating", "the clock"], 0, "Input 0 turns on the PMOS pull-up.", "r"),
 q("Which term in P ≈ αCV²f has the biggest effect when scaled by the same factor?", ["V", "f", "C", "α"], 0, "Power grows with the square of voltage.", "c"),
 q("Moore's law describes…", ["transistor counts doubling about every two years", "V = IR", "clock speed doubling yearly", "the speed of light in wires"], 0, "An observation about manufacturing, not a law of physics.", "c"),
 q("DRAM must be refreshed because…", ["each bit is stored as charge on a capacitor that leaks away", "transistors wear out", "the clock stops", "diodes reverse"], 0, "Refreshing re-writes each bit before the charge drains.", "c"),
]
FRQS = [
 {"q": "A 9 V battery powers R₁ = 100 Ω in series with a parallel pair R₂ = 300 Ω and R₃ = 150 Ω.", "parts": [
  {"p": "(a) Find the total resistance.", "rubric": [["Parallel pair = 300·150/450 = 100 Ω", 1], ["Total = 200 Ω", 1]], "answer": "R₂ ∥ R₃ = 100 Ω; total = 100 + 100 = 200 Ω."},
  {"p": "(b) Find the current from the battery and the voltage across R₁.", "rubric": [["I = 9/200 = 45 mA", 1], ["V₁ = 4.5 V", 1]], "answer": "I = 0.045 A; V₁ = 0.045 × 100 = 4.5 V."},
  {"p": "(c) Find the current through R₃ and check KCL.", "rubric": [["Parallel voltage 4.5 V", 1], ["I₃ = 30 mA, I₂ = 15 mA, 15 + 30 = 45 ✓", 1]], "answer": "4.5 V across the pair: I₂ = 15 mA, I₃ = 30 mA, total 45 mA ✓."}]},
 {"q": "CMOS design.", "parts": [
  {"p": "(a) Describe the transistor arrangement of a 2-input CMOS NOR gate (which type, series or parallel, and where).", "rubric": [["Two PMOS in series between VDD and Y", 1], ["Two NMOS in parallel between Y and ground", 1]], "answer": "Pull-up: PMOS-A and PMOS-B in series from VDD to Y. Pull-down: NMOS-A and NMOS-B in parallel from Y to ground."},
  {"p": "(b) For A = 0, B = 0 explain which network conducts and give Y.", "rubric": [["Both PMOS on → pull-up connects Y to VDD", 1], ["Both NMOS off; Y = 1", 1]], "answer": "Both PMOS are on (input 0), the series path conducts, both NMOS are off, so Y = 1."},
  {"p": "(c) A chip uses 40 W at 1.1 V. Estimate the power at 0.88 V with the same clock.", "rubric": [["Uses P ∝ V²", 1], ["(0.8)² × 40 = 25.6 W", 1]], "answer": "0.88/1.1 = 0.8; 0.8² = 0.64; 0.64 × 40 = 25.6 W."}]},
]
build("comp-eng", "ce-1", L, 1, "Circuits and Transistors", 'Circuits and <span class="hl">transistors</span>', "Voltage, current and resistance, how series and parallel circuits behave, and how a transistor turns electricity into logic.", "Intro to computer engineering unit 1: Ohm's law, series and parallel circuits, Kirchhoff's laws, LEDs and CMOS transistors with interactive labs.", CH, PQ, CHAL, EXQ, FRQS, OUT, TAGS)
