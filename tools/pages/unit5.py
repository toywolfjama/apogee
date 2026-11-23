import math
from gen_unit import *
from cs_common import lab

g = 10
# ---------- checks for worked examples ----------
close(2 + 3 * 4, 14); close(2 * 4 + 0.5 * 3 * 16, 32)               # rotational kinematics
close(math.sqrt(0 + 2 * 2 * 25), 10)                                 # ω² = ω0² + 2αΔθ
close(0.3 * 8, 2.4); close(0.3 * 64, 19.2); close(0.3 * 2, 0.6)     # v = rω, ac = ω²r, at = rα
close(0.8 * 25 * math.sin(math.radians(30)), 10)                     # τ = rF sinθ
close(2 * 1 ** 2 + 3 * 0.5 ** 2, 2.75)                               # I = Σmr²
close(0.5 * 4 * 0.5 ** 2, 0.5); close(0.5 + 4 * 0.5 ** 2, 1.5)      # disk, parallel axis
close(3 * 1.2 / 2, 1.8)                                              # balance position
close(40 * 0.2 / 0.5, 16)                                            # α = τ/I
close(2 * 10 / (2 + 0.5 * 4), 5)                                     # disk pulley a
close(2 * (10 - 5), 10); close(10 * 0.2 / (0.5 * 4 * 0.04), 25)     # tension, α
close((400 * 1 + 600 * 2.5) / 5, 380)                                # beam support forces
print("unit 5 examples verified")

CORE = ('<p>Everything you learned about straight-line motion has a rotational twin. Position becomes angle, velocity becomes angular velocity, force becomes <b>torque</b>, and mass becomes <b>rotational inertia</b>. The big idea: <b>a net torque causes angular acceleration, and how much depends on how the mass is spread out around the axis.</b></p>'
 + eq("θ, ω, α &nbsp;&nbsp;&nbsp;&nbsp; τ = rF sin θ &nbsp;&nbsp;&nbsp;&nbsp; α = Στ / I")
 + sim({"type": "rotkin", "w0": 1, "al": 0.8, "T": 4, "r1": 0.4, "r2": 1}, "Every point turns through the same angle, but outer points move faster")
 + '<div class="tblwrap"><table><tr><th>Linear</th><th>Rotational</th><th>Link</th></tr>'
 '<tr><td>position x</td><td>angle θ (rad)</td><td>s = rθ</td></tr>'
 '<tr><td>velocity v</td><td>angular velocity ω (rad/s)</td><td>v = rω</td></tr>'
 '<tr><td>acceleration a</td><td>angular acceleration α (rad/s²)</td><td>a<sub>t</sub> = rα</td></tr>'
 '<tr><td>force F</td><td>torque τ (N·m)</td><td>τ = r⊥F</td></tr>'
 '<tr><td>mass m</td><td>rotational inertia I (kg·m²)</td><td>I = Σmr²</td></tr>'
 '<tr><td>ΣF = ma</td><td>Στ = Iα</td><td></td></tr></table></div>')
CH = [chapter("overview-u5", "Overview", "Overview", [topic("core-u5", "Core ideas", CORE)])]

# ---------- 5.1 rotational kinematics ----------
KIN = topic("rotkin-u5", "Rotational kinematics", f'''
<p>Angles are measured in <b>radians</b>: one full turn = 2π rad. <b>Counterclockwise is positive</b> by convention.</p>
<div class="grid2"><div class="mini"><h4>Angular velocity ω</h4><p>How fast the angle changes: ω = Δθ/Δt, in rad/s.</p></div>
<div class="mini"><h4>Angular acceleration α</h4><p>How fast ω changes: α = Δω/Δt, in rad/s².</p></div></div>
<p>With constant α, the kinematics equations work exactly like the linear ones, with x → θ, v → ω, a → α:</p>
{eq("ω = ω₀ + αt &nbsp;&nbsp;&nbsp; θ = θ₀ + ω₀t + ½αt² &nbsp;&nbsp;&nbsp; ω² = ω₀² + 2α(θ − θ₀)")}
{sim({"type": "rotkin", "w0": 2, "al": 3, "T": 4, "r1": 0.5, "r2": 1, "ask": ["w", "th"]}, "ω₀ = 2 rad/s, α = 3 rad/s²: find ω and Δθ at each second")}
{worked("A wheel turning at 2 rad/s speeds up at 3 rad/s² for 4 s. Find its final angular velocity and the angle it turns through.", "ω = 2 + 3(4) = <b>14 rad/s</b>. Δθ = 2(4) + ½(3)(4²) = 8 + 24 = <b>32 rad</b> (about 5.1 revolutions).")}
{worked("A fan starts from rest with α = 2 rad/s². How fast is it spinning after 25 rad?", "ω² = 0 + 2(2)(25) = 100, so <b>ω = 10 rad/s</b>.")}
<h3>Graphs</h3>
<p>Same rules as Unit 1: the slope of θ vs. t is ω, the slope of ω vs. t is α, and the area under ω vs. t is Δθ.</p>
{box("trap", "Common mistake", "Mixing revolutions, degrees and radians. Convert first: 1 rev = 2π rad = 360°. And rpm means revolutions per minute: 60 rpm = 1 rev/s = 2π rad/s.")}
''', pill=("r", "UNIT 5.1"), sub="θ, ω and α: kinematics for things that spin.")

LINK = topic("link-u5", "Connecting linear and rotational motion", f'''
{eq("s = rθ &nbsp;&nbsp;&nbsp; v = rω &nbsp;&nbsp;&nbsp; a<sub>t</sub> = rα &nbsp;&nbsp;&nbsp; a<sub>c</sub> = v²/r = ω²r")}
<p>Every point on a rigid object has the <b>same</b> θ, ω and α. But a point farther from the axis travels a bigger circle, so its <b>linear</b> distance, speed and tangential acceleration are bigger, in proportion to r.</p>
{sim({"type": "rotkin", "w0": 0, "al": 2, "T": 4, "r1": 0.3, "r2": 0.9, "ask": ["v"]}, "Same ω for both points; v = rω is three times bigger at three times the radius")}
{worked("A point 0.3 m from the axis of a wheel spinning at 8 rad/s, speeding up at 2 rad/s². Find its speed, its tangential acceleration and its centripetal acceleration.", "v = rω = 0.3 × 8 = <b>2.4 m/s</b>. a<sub>t</sub> = rα = 0.3 × 2 = <b>0.6 m/s²</b>. a<sub>c</sub> = ω²r = 64 × 0.3 = <b>19.2 m/s²</b> toward the axis.")}
<h3>Rolling without slipping</h3>
<p>For a wheel that rolls without slipping, the distance the center moves equals the arc length turned: <b>v<sub>cm</sub> = Rω</b> and <b>a<sub>cm</sub> = Rα</b>. The contact point is momentarily at rest.</p>
''', pill=("r", "UNIT 5.2"), sub="s = rθ, v = rω, a = rα.",
 det=("Two kinds of acceleration", '''<h4>Tangential vs. centripetal</h4><p>A point on a spinning wheel can have two acceleration components. The tangential one (a<sub>t</sub> = rα) changes its speed; it's zero if ω is constant. The centripetal one (a<sub>c</sub> = ω²r) changes its direction; it's never zero while the wheel turns.</p>
<h4>Why radians?</h4><p>s = rθ only works when θ is in radians, because a radian is defined as the angle where the arc length equals the radius. That's what makes v = rω and a = rα work too.</p>
<h4>Gears and belts</h4><p>Two gears that mesh (or wheels joined by a belt) have the same speed at the edge: r₁ω₁ = r₂ω₂. The smaller gear spins faster.</p>'''))
CH.append(chapter("kin-ch-u5", "Rotational Kinematics", "Kinematics", [KIN, LINK]))

# ---------- 5.3 torque ----------
TQ = topic("torque-u5", "Torque", f'''
{eq("τ = r⊥F = rF sin θ")}
<p><b>Torque</b> measures how effectively a force makes something rotate about an axis. It depends on three things: how big the force is, <b>how far from the axis</b> it's applied (r), and the <b>angle</b> θ between r and F. Units: N·m. Counterclockwise torques are positive, clockwise negative.</p>
{lab(type="torquelab", r=0.8, F=20, ang=90)}
<p>The <b>lever arm</b> r⊥ = r sin θ is the perpendicular distance from the axis to the force's line of action. A force pointed straight at (or away from) the axis has zero lever arm and makes zero torque, however big it is.</p>
{worked("You push a door 0.8 m from its hinges with 25 N at 30° to the door's surface. Find the torque.", "τ = rF sin θ = 0.8 × 25 × sin 30° = 0.8 × 25 × 0.5 = <b>10 N·m</b>. Pushing perpendicular (90°) would give 20 N·m.")}
{box("tip", "Why door handles are far from the hinges", "Same force, bigger r, bigger torque. That's also why a longer wrench loosens a stuck bolt more easily.")}
''', pill=("r", "UNIT 5.3"), sub="The rotational version of force.")
CH.append(chapter("torque-ch-u5", "Torque", "Torque", [TQ]))

# ---------- 5.4 rotational inertia ----------
INR = topic("inertia-u5", "Rotational inertia", f'''
{eq("I = Σmr² &nbsp;&nbsp;&nbsp; I′ = I<sub>cm</sub> + Md²")}
<p><b>Rotational inertia</b> (I) is resistance to changes in rotation. It depends on the mass <b>and how far that mass is from the axis</b>. Because r is squared, mass far from the axis counts much more.</p>
{worked("A light rod has a 2 kg mass 1 m from the axis and a 3 kg mass 0.5 m from it. Find I.", "I = Σmr² = 2(1²) + 3(0.5²) = 2 + 0.75 = <b>2.75 kg·m²</b>.")}
<h3>Common shapes (given on the exam when needed)</h3>
<div class="tblwrap"><table><tr><th>Object (axis through center)</th><th>I</th></tr>
<tr><td>Hoop or thin ring</td><td>MR²</td></tr><tr><td>Solid disk or cylinder</td><td>½MR²</td></tr><tr><td>Solid sphere</td><td>⅖MR²</td></tr>
<tr><td>Thin rod about its center</td><td>¹⁄₁₂ML²</td></tr><tr><td>Thin rod about one end</td><td>⅓ML²</td></tr></table></div>
<p>A hoop has all its mass at R, so it has the most rotational inertia for its mass and radius. A solid disk has mass spread inward, so less.</p>
{lab(type="spinlab", m=1, M=2, R=0.2)}
<h3>Changing the axis: the parallel-axis theorem</h3>
<p>If you know I about the center of mass, the rotational inertia about a parallel axis a distance d away is I′ = I<sub>cm</sub> + Md². It's always larger.</p>
{worked("A 4 kg solid disk of radius 0.5 m. Find I about its center, then about a parallel axis at its edge.", "I<sub>cm</sub> = ½(4)(0.5²) = <b>0.5 kg·m²</b>. At the edge: I′ = 0.5 + 4(0.5²) = <b>1.5 kg·m²</b>.")}
''', pill=("r", "UNIT 5.4"), sub="The rotational version of mass.",
 det=("Thinking about rotational inertia", '''<h4>Same object, different I</h4><p>Rotational inertia is about an axis, not just about the object. A rod is much harder to spin about one end (⅓ML²) than about its middle (¹⁄₁₂ML²).</p>
<h4>Ranking problems</h4><p>To rank shapes with the same M and R, look at the coefficient: hoop (1) > disk (½) > sphere (⅖). More mass far from the axis means more I.</p>
<h4>Ice skaters and tightrope walkers</h4><p>A tightrope walker carries a long pole to increase I, so a wobble produces a smaller α and they have time to correct it.</p>'''))
CH.append(chapter("inertia-ch-u5", "Rotational Inertia", "Inertia", [INR]))

# ---------- 5.5 equilibrium ----------
EQ = topic("equilibrium-u5", "Rotational equilibrium", f'''
{eq("Στ = 0 &nbsp;&nbsp; and &nbsp;&nbsp; ΣF = 0")}
<p>An object is in <b>static equilibrium</b> when it doesn't accelerate and doesn't start rotating. That takes two conditions: the forces balance <b>and</b> the torques balance about any axis you choose. This is Newton's first law in rotational form: with zero net torque, ω stays constant.</p>
{lab(type="balance", m1=3, x1=-1.25, m2=2, x2=2)}
{worked("A 3 kg mass sits 1.2 m left of a seesaw's pivot. Where should a 2 kg mass go to balance it?", "Counterclockwise torque = clockwise torque: (3)(10)(1.2) = (2)(10)d → d = <b>1.8 m right of the pivot</b>.")}
<h3>Choosing the pivot</h3>
<p>In equilibrium, Στ = 0 about <b>every</b> point, so choose the point that makes the algebra easiest: put it where an unknown force acts, and that force's torque disappears.</p>
{sim({"type": "seesaw", "objs": [[4, 1], [6, 2.5]], "L": 3, "pivot": 0}, "A beam with loads: not balanced on its middle")}
{worked("A light 5 m beam rests on supports at each end (x = 0 and x = 5 m). A 400 N load sits at x = 1 m and a 600 N load at x = 2.5 m. Find the force from the right-hand support.", "Take torques about the left support (its force has no torque there): F<sub>R</sub>(5) = 400(1) + 600(2.5) = 1900, so <b>F<sub>R</sub> = 380 N</b>. Then ΣF = 0 gives F<sub>L</sub> = 1000 − 380 = <b>620 N</b>.")}
{box("trap", "Common mistake", "Forgetting the beam's own weight. A uniform beam's weight acts at its center.")}
''', pill=("r", "UNIT 5.5"), sub="Newton's first law for rotation: Στ = 0.")
CH.append(chapter("eq-ch-u5", "Rotational Equilibrium", "Equilibrium", [EQ]))

# ---------- 5.6 Newton's second law ----------
N2 = topic("n2-u5", "Newton's second law for rotation", f'''
{eq("α = Στ / I")}
<p>A net torque causes an angular acceleration, in the direction of the net torque, inversely proportional to the rotational inertia.</p>
{worked("A 40 N force is applied tangentially 0.2 m from the axis of a wheel with I = 0.5 kg·m². Find α.", "τ = rF = 0.2 × 40 = 8 N·m. α = τ/I = 8/0.5 = <b>16 rad/s²</b>.")}
<h3>Pulleys with mass</h3>
<p>Until now pulleys were massless, so the tension was the same on both sides. A real pulley has rotational inertia, so it takes a net torque to speed it up, and the tensions on the two sides differ.</p>
{sim({"type": "spin", "m": 2, "M": 4, "R": 0.2, "shapes": ["disk", "ring"], "ask": ["a"]}, "A 2 kg mass unwinds string from a 4 kg pulley: disk vs. hoop")}
{worked("A 2 kg mass hangs from a string wrapped around a 4 kg solid-disk pulley (R = 0.2 m). Find the mass's acceleration, the tension, and the pulley's α.", "Hanging mass: mg − T = ma. Pulley: TR = Iα = (½MR²)(a/R), so T = ½Ma. Add them: mg = (m + ½M)a → a = 20/(2 + 2) = <b>5 m/s²</b>. T = 2(10 − 5) = <b>10 N</b>. α = a/R = 5/0.2 = <b>25 rad/s²</b>.")}
{box("tip", "The method", "Draw a free-body diagram for each object that moves in a line and an extended diagram for each object that rotates. Write ΣF = ma or Στ = Iα for each, connect them with a = rα, and solve.")}
''', pill=("r", "UNIT 5.6"), sub="Στ = Iα.",
 det=("Common setups", '''<h4>Atwood machine with a massive pulley</h4><p>For masses m₁ > m₂ over a pulley with rotational inertia I: a = (m₁ − m₂)g / (m₁ + m₂ + I/R²). With a massless pulley the I/R² term disappears and you get the Unit 2 result.</p>
<h4>Rod pivoted at one end</h4><p>A uniform rod of length L held horizontal and released: gravity acts at L/2, so τ = MgL/2 and I = ⅓ML², giving α = 3g/(2L) at the start. The torque shrinks as it swings down.</p>
<h4>Sign check</h4><p>The tension on the side the pulley is turning toward is the larger one; the difference T₁ − T₂ times R is the net torque on the pulley.</p>'''))
CH.append(chapter("n2-ch-u5", "Newton's Second Law (Rotation)", "Στ = Iα", [N2]))

# ---------- review ----------
REV = topic("review-u5", "Your equation sheet (Unit 5 lines)", '''<div class="tblwrap"><table><tr><th>On the sheet</th><th>In words</th><th>Use it when</th></tr>
<tr><td><span class="eq">ω = ω₀ + αt</span>, <span class="eq">θ = θ₀ + ω₀t + ½αt²</span>, <span class="eq">ω² = ω₀² + 2α(θ − θ₀)</span></td><td>rotational kinematics</td><td>constant α, spinning objects</td></tr>
<tr><td><span class="eq">v = rω</span>, <span class="eq">a<sub>T</sub> = rα</span>, <span class="eq">Δx = rΔθ</span></td><td>link a point's motion to the rotation</td><td>rolling, string unwinding, points on a wheel</td></tr>
<tr><td><span class="eq">τ = r⊥F = rF sin θ</span></td><td>torque</td><td>any force that can turn something</td></tr>
<tr><td><span class="eq">I = Σmr²</span>, <span class="eq">I′ = I<sub>cm</sub> + Md²</span></td><td>rotational inertia</td><td>point masses, changing the axis</td></tr>
<tr><td><span class="eq">α = Στ/I</span></td><td>Newton's second law for rotation</td><td>a net torque, pulleys with mass</td></tr></table></div>''', sub="Every Unit 5 equation and when to use it.")
MIS = topic("mistakes-u5", "Common mistakes", '''<ol class="steps">
<li>Using degrees or revolutions in v = rω or s = rθ. Convert to radians.</li>
<li>Using r instead of the lever arm when the force isn't perpendicular: τ = rF sin θ.</li>
<li>Thinking a bigger force always gives a bigger torque. A force aimed at the axis gives zero torque.</li>
<li>Forgetting the beam's own weight at its center in equilibrium problems.</li>
<li>Assuming equal tensions on both sides of a pulley that has mass.</li>
<li>Saying every point on a wheel has the same speed. Same ω, different v = rω.</li>
<li>Treating rotational inertia as just mass. Where the mass sits matters: hoop > disk > sphere.</li></ol>''', sub="Points students lose most often.")
CH.append(chapter("review-ch-u5", "Review", "Review", [REV, MIS]))

# ---------- questions ----------
PQ = [
 {"t": "r", "q": "A wheel turns through 3 complete revolutions. How many radians is that?", "o": ["6π rad", "3 rad", "3π rad", "1080 rad"], "a": 0, "x": "1 rev = 2π rad, so 3 rev = 6π ≈ 18.8 rad."},
 {"t": "r", "q": "A wheel at rest speeds up at 4 rad/s² for 3 s. What is its angular velocity?", "o": ["12 rad/s", "7 rad/s", "18 rad/s", "1.3 rad/s"], "a": 0, "x": "ω = ω₀ + αt = 0 + 4(3) = 12 rad/s.", "sim": {"type": "rotkin", "w0": 0, "al": 4, "T": 3, "r1": 0.5, "r2": 1, "ask": ["w"]}},
 {"t": "r", "q": "A disk spinning at 10 rad/s slows uniformly to rest in 5 s. Through what angle does it turn while stopping?", "o": ["25 rad", "50 rad", "10 rad", "2 rad"], "a": 0, "x": "Δθ = average ω × t = (10 + 0)/2 × 5 = 25 rad."},
 {"t": "r", "q": "Two children sit on a spinning merry-go-round, one at the edge and one halfway to the center. Compared with the inner child, the outer child has…", "o": ["the same ω and twice the speed", "twice the ω and the same speed", "the same ω and the same speed", "half the ω and twice the speed"], "a": 0, "x": "All points share ω; v = rω doubles with r.", "sim": {"type": "rotkin", "w0": 1.5, "al": 0, "T": 3, "r1": 0.5, "r2": 1, "ask": ["v"]}},
 {"t": "r", "q": "A point 0.5 m from the axis of a wheel turning at 6 rad/s. What is its speed?", "o": ["3 m/s", "12 m/s", "0.083 m/s", "18 m/s"], "a": 0, "x": "v = rω = 0.5 × 6 = 3 m/s."},
 {"t": "r", "q": "A bicycle wheel of radius 0.35 m rolls without slipping at 7 m/s. What is its angular velocity?", "o": ["20 rad/s", "2.45 rad/s", "7 rad/s", "0.05 rad/s"], "a": 0, "x": "ω = v/R = 7/0.35 = 20 rad/s."},
 {"t": "r", "q": "Which force produces the largest torque on a door about its hinges? All forces are 10 N.", "o": ["Perpendicular to the door at the handle, far from the hinges", "Perpendicular to the door near the hinges", "At the handle, pushing straight toward the hinges", "At 30° to the door at the handle"], "a": 0, "x": "Largest r and sin θ = 1 give the largest τ = rF sin θ. Pushing toward the hinge gives zero torque."},
 {"t": "r", "q": "A 30 N force is applied perpendicular to a wrench, 0.25 m from the bolt. What is the torque?", "o": ["7.5 N·m", "120 N·m", "30 N·m", "0.0083 N·m"], "a": 0, "x": "τ = rF = 0.25 × 30 = 7.5 N·m."},
 {"t": "r", "q": "A 20 N force acts 0.5 m from an axis at 30° to the line from the axis. What is the torque?", "o": ["5 N·m", "10 N·m", "8.7 N·m", "20 N·m"], "a": 0, "x": "τ = rF sin θ = 0.5 × 20 × 0.5 = 5 N·m.", "sim": {"type": "torque", "r": 0.5, "F": 20, "ang": 30, "ask": ["tau"]}},
 {"t": "r", "q": "Two 1 kg masses are on a light rod, each 0.4 m from the axis in the middle. What is the rotational inertia?", "o": ["0.32 kg·m²", "0.16 kg·m²", "0.8 kg·m²", "0.4 kg·m²"], "a": 0, "x": "I = Σmr² = 2 × 1 × 0.4² = 0.32 kg·m²."},
 {"t": "r", "q": "A hoop, a solid disk and a solid sphere have the same mass and radius. Rank their rotational inertias about their centers, greatest first.", "o": ["hoop, disk, sphere", "sphere, disk, hoop", "disk, hoop, sphere", "all equal"], "a": 0, "x": "MR² > ½MR² > ⅖MR²: the hoop has all its mass far from the axis."},
 {"t": "r", "q": "The masses on a spinning rod are moved twice as far from the axis. The rod's rotational inertia (ignoring the rod) becomes…", "o": ["4 times as large", "2 times as large", "the same", "half as large"], "a": 0, "x": "I = Σmr², so doubling r multiplies I by 4."},
 {"t": "r", "q": "A 2 kg mass sits 1.5 m left of a seesaw's pivot. How far right of the pivot must a 3 kg mass sit to balance it?", "o": ["1 m", "1.5 m", "2.25 m", "0.67 m"], "a": 0, "x": "2(10)(1.5) = 3(10)d → d = 1 m.", "sim": {"type": "seesaw", "objs": [[2, -1.5], [3, 1]], "ask": ["net"]}},
 {"t": "r", "q": "For an object to be in static equilibrium…", "o": ["the net force and the net torque must both be zero", "only the net force must be zero", "only the net torque must be zero", "it must have no forces on it"], "a": 0, "x": "Both conditions: no linear and no angular acceleration."},
 {"t": "r", "q": "A seesaw has a 4 kg mass 1 m left of the pivot and a 1 kg mass 2 m right of it. What happens?", "o": ["It tips left side down (counterclockwise)", "It tips right side down", "It balances", "It can't be determined"], "a": 0, "x": "Left: 40 N·m counterclockwise. Right: 20 N·m clockwise. Net 20 N·m counterclockwise.", "sim": {"type": "seesaw", "objs": [[4, -1], [1, 2]]}},
 {"t": "r", "q": "A net torque of 12 N·m acts on a wheel with I = 3 kg·m². What is its angular acceleration?", "o": ["4 rad/s²", "36 rad/s²", "0.25 rad/s²", "15 rad/s²"], "a": 0, "x": "α = τ/I = 12/3 = 4 rad/s²."},
 {"t": "r", "q": "The same torque is applied to a hoop and a solid disk of equal mass and radius. Which has the greater angular acceleration?", "o": ["The disk", "The hoop", "They're equal", "It depends on the torque"], "a": 0, "x": "Smaller I → larger α = τ/I. The disk has half the hoop's I.", "sim": {"type": "spin", "m": 1, "M": 2, "R": 0.2}},
 {"t": "r", "q": "A mass hangs from a string over a pulley that has mass. Compared with the tension on the other side of the pulley, the tension on the side going down is…", "o": ["larger", "smaller", "the same", "zero"], "a": 0, "x": "The pulley needs a net torque to speed up, so the tensions on its two sides differ, and the larger one is on the side it turns toward."},
 {"t": "r", "q": "A wheel spins at a constant 5 rad/s. A point on its rim has…", "o": ["centripetal acceleration only", "tangential acceleration only", "no acceleration", "both tangential and centripetal acceleration"], "a": 0, "x": "Constant ω means α = 0, so a<sub>t</sub> = 0. It's still turning, so a<sub>c</sub> = ω²r."},
 {"t": "r", "q": "Which unit matches torque?", "o": ["N·m", "N/m", "kg·m²", "rad/s²"], "a": 0, "x": "τ = rF, so newtons times meters (not the same as a joule, even though the units match)."},
]
CHAL = [
 {"t": "r", "q": "A uniform 2 m, 10 kg beam is supported at its left end and at a point 0.5 m from its right end. What is the force from the second support?", "o": ["≈ 66.7 N", "50 N", "100 N", "33.3 N"], "a": 0, "x": "About the left end: F(1.5) = 100(1) → F ≈ 66.7 N. (Weight acts at the center, 1 m.)"},
 {"t": "r", "q": "A 1 kg mass hangs from a string wrapped around a 2 kg solid-disk pulley of radius 0.1 m. What is the mass's acceleration?", "o": ["5 m/s²", "10 m/s²", "3.3 m/s²", "6.7 m/s²"], "a": 0, "x": "a = mg/(m + ½M) = 10/(1 + 1) = 5 m/s².", "sim": {"type": "spin", "m": 1, "M": 2, "R": 0.1, "shapes": ["disk", "ring"], "ask": ["a"]}},
 {"t": "r", "q": "A uniform rod of mass M and length L is pivoted at one end and held horizontal, then released. What is its initial angular acceleration? (I = ⅓ML²)", "o": ["3g/(2L)", "g/L", "g/(2L)", "3g/L"], "a": 0, "x": "τ = Mg(L/2), α = τ/I = (MgL/2)/(⅓ML²) = 3g/(2L)."},
 {"t": "r", "q": "A 3 kg solid sphere of radius 0.2 m (I<sub>cm</sub> = ⅖MR²). What is its rotational inertia about an axis tangent to its surface?", "o": ["0.168 kg·m²", "0.048 kg·m²", "0.12 kg·m²", "0.072 kg·m²"], "a": 0, "x": "I<sub>cm</sub> = 0.4 × 3 × 0.04 = 0.048. Parallel axis: + 3 × 0.04 = 0.12 → 0.168 kg·m²."},
 {"t": "r", "q": "Two gears mesh. Gear A (radius 3 cm) turns at 20 rad/s. Gear B has radius 6 cm. How fast does B turn?", "o": ["10 rad/s", "40 rad/s", "20 rad/s", "5 rad/s"], "a": 0, "x": "Meshing teeth share edge speed: r<sub>A</sub>ω<sub>A</sub> = r<sub>B</sub>ω<sub>B</sub> → 3(20) = 6ω → 10 rad/s."},
 {"t": "r", "q": "A 600 N painter stands 1 m from the left end of a 4 m, 200 N uniform plank supported at both ends. Force from the left support?", "o": ["550 N", "250 N", "400 N", "800 N"], "a": 0, "x": "About the right end: F<sub>L</sub>(4) = 600(3) + 200(2) = 2200 → 550 N."},
 {"t": "r", "q": "A wheel's ω–t graph is a straight line from 8 rad/s to 2 rad/s over 3 s. Through what angle does it turn?", "o": ["15 rad", "6 rad", "24 rad", "30 rad"], "a": 0, "x": "Area under ω–t = average ω × t = 5 × 3 = 15 rad."},
 {"t": "r", "q": "Masses of 3 kg and 1 kg hang on either side of a pulley with I/R² = 2 kg (Atwood machine). What is the acceleration?", "o": ["3.33 m/s²", "5 m/s²", "2.5 m/s²", "6.67 m/s²"], "a": 0, "x": "a = (m₁ − m₂)g/(m₁ + m₂ + I/R²) = 20/6 ≈ 3.33 m/s²."},
]
close(100 * 1 / 1.5, 66.7, 0.1); close(1 * 10 / (1 + 1), 5); close(0.4 * 3 * 0.04 + 3 * 0.04, 0.168)
close(3 * 20 / 6, 10); close((600 * 3 + 200 * 2) / 4, 550); close(5 * 3, 15); close(20 / 6, 3.33, 0.01)

EX = {"title": "Unit 5 Practice Exam: Torque and Rotational Dynamics", "mcqMinutes": 30, "frqMinutes": 25, "tags": {"r": "Rotation"},
 "mcq": [
  {"t": "r", "k": "calc", "q": "A turntable goes from rest to 4 rad/s in 2 s. What is its angular acceleration?", "o": ["2 rad/s²", "8 rad/s²", "0.5 rad/s²", "4 rad/s²"], "a": 0, "x": "α = Δω/Δt = 4/2."},
  {"t": "r", "k": "calc", "q": "A wheel turning at 3 rad/s speeds up at 2 rad/s² for 4 s. Angle turned?", "o": ["28 rad", "16 rad", "12 rad", "44 rad"], "a": 0, "x": "3(4) + ½(2)(16) = 12 + 16 = 28 rad."},
  {"t": "r", "k": "concept", "q": "On a rotating rigid disk, which quantity is the same for all points?", "o": ["angular velocity", "linear speed", "centripetal acceleration", "distance traveled"], "a": 0, "x": "Every point turns through the same angle in the same time."},
  {"t": "r", "k": "calc", "q": "A 0.4 m wrench, 50 N force at 90°. Torque?", "o": ["20 N·m", "125 N·m", "12.5 N·m", "200 N·m"], "a": 0, "x": "0.4 × 50."},
  {"t": "r", "k": "concept", "q": "A force applied to a door produces no torque. The force must…", "o": ["point along the line through the hinge", "be very small", "be perpendicular to the door", "be applied at the handle"], "a": 0, "x": "sin θ = 0: zero lever arm."},
  {"t": "r", "k": "calc", "q": "Masses: 1 kg at 0.2 m, 1 kg at 0.4 m from an axis. I = ?", "o": ["0.2 kg·m²", "0.6 kg·m²", "0.36 kg·m²", "0.04 kg·m²"], "a": 0, "x": "0.04 + 0.16 = 0.2 kg·m²."},
  {"t": "r", "k": "concept", "q": "Why does a hoop have more rotational inertia than a disk of the same mass and radius?", "o": ["All of its mass is at the maximum distance from the axis", "It has more mass", "It's hollow, so it's lighter", "It spins faster"], "a": 0, "x": "I depends on how far the mass is from the axis."},
  {"t": "r", "k": "calc", "q": "A 5 kg mass is 0.8 m left of a pivot. Where must a 4 kg mass go to balance?", "o": ["1 m right", "0.64 m right", "1.25 m right", "0.8 m right"], "a": 0, "x": "5(0.8) = 4d → d = 1 m."},
  {"t": "r", "k": "calc", "q": "A net torque of 6 N·m acts on an object with I = 0.2 kg·m². α = ?", "o": ["30 rad/s²", "1.2 rad/s²", "0.033 rad/s²", "6.2 rad/s²"], "a": 0, "x": "6/0.2."},
  {"t": "r", "k": "concept", "q": "A uniform meter stick balances at its 50 cm mark. A mass is hung at the 80 cm mark. To rebalance, the pivot must move…", "o": ["toward the 80 cm mark", "toward the 0 cm mark", "nowhere: it still balances", "to the 100 cm mark"], "a": 0, "x": "The new center of mass of the system is closer to the added mass."},
  {"t": "r", "k": "calc", "q": "A wheel of radius 0.25 m rolls without slipping with ω = 12 rad/s. Speed of its center?", "o": ["3 m/s", "48 m/s", "12 m/s", "0.25 m/s"], "a": 0, "x": "v = Rω."},
  {"t": "r", "k": "concept", "q": "A figure skater spins with constant ω. What is the net torque on her?", "o": ["zero", "positive", "negative", "equal to her weight"], "a": 0, "x": "Constant ω means α = 0, so Στ = 0 (Newton's first law for rotation)."},
  {"t": "r", "k": "calc", "q": "A 2 kg mass unwinds a string from a 2 kg hoop pulley (I = MR²). Acceleration of the mass?", "o": ["5 m/s²", "10 m/s²", "6.7 m/s²", "2.5 m/s²"], "a": 0, "x": "a = mg/(m + M) = 20/4."},
  {"t": "r", "k": "calc", "q": "A solid disk (M = 2 kg, R = 0.3 m) about a parallel axis at its edge. I = ?", "o": ["0.27 kg·m²", "0.09 kg·m²", "0.18 kg·m²", "0.36 kg·m²"], "a": 0, "x": "½(2)(0.09) + 2(0.09) = 0.09 + 0.18 = 0.27."},
  {"t": "r", "k": "concept", "q": "A point on the rim of a wheel that is speeding up has an acceleration that points…", "o": ["partly toward the center and partly along the direction of motion", "straight toward the center", "straight along the direction of motion", "away from the center"], "a": 0, "x": "Both a<sub>c</sub> (inward) and a<sub>t</sub> (along v) are nonzero."},
 ],
 "frq": [
  {"q": "A uniform 4.0 m beam of mass 20 kg rests horizontally on two supports: one at its left end and one 1.0 m from its right end. A 30 kg box sits on the beam 0.5 m from the right end. Use g = 10 m/s².",
   "parts": [
    {"p": "(a) Draw a free-body diagram of the beam showing where each force acts.", "rubric": [["Weight of beam (200 N) at the center, 2.0 m from the left", 1], ["Box's force (300 N) at 3.5 m; support forces at 0 m and 3.0 m, upward", 1]], "answer": "Upward: F<sub>L</sub> at x = 0 and F<sub>R</sub> at x = 3.0 m. Downward: 200 N at x = 2.0 m and 300 N at x = 3.5 m."},
    {"p": "(b) Calculate the force from each support.", "rubric": [["Torques about the left end: F<sub>R</sub>(3.0) = 200(2.0) + 300(3.5)", 1], ["F<sub>R</sub> ≈ 483 N", 1], ["F<sub>L</sub> = 500 − 483 ≈ 17 N", 1]], "answer": "About x = 0: 3.0F<sub>R</sub> = 400 + 1050 = 1450 → F<sub>R</sub> ≈ 483 N. ΣF = 0: F<sub>L</sub> = 500 − 483 ≈ 17 N."},
    {"p": "(c) The box slides toward the right end. Explain what happens to F<sub>L</sub>, and what happens when the box gets far enough.", "rubric": [["F<sub>L</sub> decreases as the box moves right", 1], ["When F<sub>L</sub> would become negative, the beam tips about the right support", 1]], "answer": "Moving the box right increases its torque about the right support, so F<sub>L</sub> decreases. When the box's torque about the right support exceeds the beam's, F<sub>L</sub> reaches zero and the beam tips (rotates) about the right support."},
   ]},
  {"q": "A 1.0 kg block hangs from a light string wrapped around a solid-disk pulley of mass 4.0 kg and radius 0.10 m (I = ½MR²). The block is released from rest.",
   "parts": [
    {"p": "(a) Write Newton's second law for the block and for the pulley.", "rubric": [["Block: mg − T = ma", 1], ["Pulley: TR = Iα with α = a/R", 1]], "answer": "Block: mg − T = ma. Pulley: TR = (½MR²)(a/R), so T = ½Ma."},
    {"p": "(b) Calculate the block's acceleration and the tension.", "rubric": [["a = mg/(m + ½M) = 10/3 ≈ 3.3 m/s²", 1], ["T = ½Ma ≈ 6.7 N", 1]], "answer": "a = 10/(1 + 2) ≈ 3.3 m/s². T = ½(4)(3.33) ≈ 6.7 N."},
    {"p": "(c) The disk is replaced by a hoop of the same mass and radius. Is the block's acceleration greater, less or the same? Justify without calculating.", "rubric": [["Less", 1], ["The hoop has greater I, so the same torque gives smaller α and the block speeds up more slowly", 1]], "answer": "Less. The hoop's mass is all at R, so I is larger; it resists speeding up more, so a = mg/(m + I/R²) is smaller (2.0 m/s² here)."},
   ]},
 ]}
close(1450 / 3, 483.3, 0.1); close(500 - 483.33, 16.7, 0.1); close(10 / 3, 3.33, 0.01); close(0.5 * 4 * 10 / 3, 6.67, 0.01); close(10 / (1 + 4), 2)
close(3 * 4 + 0.5 * 2 * 16, 28); close(5 * 0.8 / 4, 1); close(0.5 * 2 * 0.09 + 2 * 0.09, 0.27)

LABS = topic("labs-u5", "Experiments with rotation", f'''
<div class="tblwrap"><table><tr><th>Experiment</th><th>Measure</th><th>Graph / check</th></tr>
<tr><td>Balance a meter stick with hanging masses</td><td>masses and their distances from the pivot</td><td>Στ = 0; plot d₂ vs. 1/m₂ (linear)</td></tr>
<tr><td>Hanging mass unwinds a string from a spinning platform</td><td>hanging mass, radius of the spool, time to fall a height</td><td>a from Δy = ½at²; α = a/r; τ = r·T; I = τ/α</td></tr>
<tr><td>Find I of an unknown object</td><td>angular acceleration for several known torques</td><td>τ vs. α is a straight line with slope I</td></tr></table></div>
{box("tip", "Sources of error", "Friction at the axle adds an unwanted torque; measure it by finding the hanging mass that keeps the platform turning at constant speed and subtract. The string must leave the spool tangentially so that r⊥ = r.")}
''', sub="What the experimental design questions look like.")
LQ = [
 {"t": "r", "q": "Students plot net torque (y-axis) vs. angular acceleration (x-axis) for a spinning platform. The slope of the best-fit line is…", "o": ["the platform's rotational inertia", "its mass", "its angular velocity", "the radius of the spool"], "a": 0, "x": "Στ = Iα, so τ vs. α has slope I."},
 {"t": "r", "q": "A meter stick balances with 0.2 kg at 20 cm from the pivot on one side. Students vary the mass m on the other side and record its distance d for balance. Which graph is linear?", "o": ["d vs. 1/m", "d vs. m", "d vs. m²", "d² vs. m"], "a": 0, "x": "m·d = constant, so d = constant × (1/m)."},
 {"t": "r", "q": "In an experiment measuring I with a falling mass, friction at the axle was ignored. The calculated I will be…", "o": ["too large", "too small", "correct", "zero"], "a": 0, "x": "Friction reduces α. Using τ from the tension alone and a smaller α gives I = τ/α that is too large."},
]
CH.append(chapter("labs-frq-u5", "Labs & FRQs", "Labs & FRQs", [LABS, quiz_section("labs-quiz-u5", "Practice: experiments", "3 questions.", "quiz-labs-u5", {"r": "Rotation"})]))
CH.append(chapter("practice-u5", "Practice Questions", "Practice", [quiz_section("practice-quiz-u5", "Practice questions", f"{len(PQ)} questions with animated models. Click an answer to check it. Use g = 10 m/s².", "quiz-u5", {"r": "Rotation"})]))
CH.append(chapter("challenge-u5", "Challenge Questions", "Challenge", [quiz_section("challenge-quiz-u5", "Challenge questions", "Multi-step torque, equilibrium and pulley problems at the hardest level of the exam.", "quiz-challenge-u5", {"r": "Rotation"})], hard=True))
CH.append(chapter("exam-ch-u5", "Practice Exam", "Practice Exam", ['<section class="topic" id="exam-box-u5"><h2>Practice exam</h2><p class="sub">15 multiple-choice questions (30 minutes) and 2 free-response questions (25 minutes). No feedback until you submit.</p><div class="exam" data-src="exam-u5"></div></section>']))

shuffle(PQ, 501); shuffle(CHAL, 502); shuffle(EX["mcq"], 503); shuffle(LQ, 504)
DATA = {"quiz-u5": PQ, "quiz-challenge-u5": CHAL, "quiz-labs-u5": LQ, "exam-u5": EX}
HTML = page("unit-5", "AP Physics 1 Unit 5: Torque and Rotational Dynamics", "AP Physics 1 · Unit 5",
            'Torque and<br><span class="hl">Rotational Dynamics</span>',
            f"Rotational kinematics, linking linear and rotational motion, torque, rotational inertia, rotational equilibrium and Newton's second law for rotation: explanations, worked examples, animations, interactive torque, balance and rotational-inertia labs, {len(PQ)+len(CHAL)+len(LQ)} practice questions and a timed practice exam.",
            "AP Physics 1 Unit 5 torque and rotational dynamics review with animations, interactive labs, practice questions and a practice exam.", CH, DATA, extra_js=("cs-sims.js",))
if __name__ == "__main__":
    open("/home/claude/ap-physics-study/courses/ap-physics-1/unit-5.html", "w").write(HTML)
    print("unit 5 written:", len(PQ), len(CHAL), len(EX["mcq"]))
