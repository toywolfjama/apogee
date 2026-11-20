import math
from gen_unit import *
g = 10
# ---------- numeric checks for every worked example and question ----------
close(0 + 3*5, 15); close(0.5*3*25, 37.5)
close(20/5, 4); close(400/(2*5), 40)
close(math.sqrt(2*45/g), 3); close(g*3, 30)
close(20/g, 2); close(20**2/(2*g), 20)
close((2 + math.sqrt(4 + 12))/2, 3)          # t^2 - 2t - 3 = 0
close(0.5*4*10 + 10*2, 40); close(10/4, 2.5)
close(math.sqrt(2*20/g), 2); close(12*2, 24); close(math.hypot(12, 20), 23.32)
close(20*math.cos(math.radians(30)), 17.32); close(2*10/g, 2); close(17.32*2, 34.64); close(10**2/(2*g), 5)
close(80/4, 20); close(3*20, 60); close(math.hypot(4, 3), 5)
slope = (1.24-0.21)/(0.25-0.04); close(2*slope, 9.81, 0.02)
print("unit 1 examples verified")

INTRO_HTML = (
 '<p>Kinematics describes motion without asking what causes it. Everything in this unit comes down to three quantities and how they change: '
 '<b>position</b> (where it is), <b>velocity</b> (how fast and which way the position changes), and <b>acceleration</b> (how fast and which way the velocity changes).</p>'
 + sim({"type": "motion", "v0": 2, "a": 1.5, "T": 4}, "Position curves upward, velocity rises steadily")
 + '<div class="grid2"><div class="mini"><h4>Equations do the math</h4><p>Four constant-acceleration equations connect v₀, v, a, t and Δx. Pick the one that leaves out the quantity you don\'t know and don\'t need.</p></div>'
 '<div class="mini"><h4>Graphs do the thinking</h4><p>Slope of position-time is velocity; slope of velocity-time is acceleration; area under velocity-time is displacement.</p></div></div>'
 + box("tip", "Summary", "Choose a positive direction, give every vector its sign, and the four equations handle the rest. In two dimensions, do the x and y directions separately; time is the only thing they share.")
)

HOWTO = '''<ol class="steps">
 <li>Read <b>Describing motion</b> first; the sign conventions there are used everywhere else.</li>
 <li>Work through each chapter with the chapter buttons. Try worked examples before reading the solution, and open a <b>detailed explanation</b> for the full reasoning.</li>
 <li>Do the <b>Practice</b> questions, then <b>Challenge</b>, then the timed <b>Practice Exam</b>.</li>
 <li>The class equation sheet lines for this unit are explained in <a href="#review-u1">Review</a>.</li>
</ol>'''

CH = []
CH.append(chapter("overview-u1", "Overview", "Overview", [
  topic("core-u1", "Core ideas", INTRO_HTML),
]))

# ---------------- Describing motion ----------------
SCALARS = topic("scalars", "Scalars, vectors and displacement", f'''
<p>A <b>scalar</b> has only a size: mass, time, distance, speed. A <b>vector</b> has a size and a direction: displacement, velocity, acceleration, force. In one dimension, direction is just a sign: choose one way as positive, and anything pointing the other way is negative.</p>
<div class="grid2">
 <div class="mini"><h4>Distance (scalar)</h4><p>Total path length traveled. Always positive. Walking 3 m east then 3 m west: distance = 6 m.</p></div>
 <div class="mini"><h4>Displacement Δx (vector)</h4><p>Change in position: Δx = x<sub>final</sub> − x<sub>initial</sub>. Same walk: Δx = 0.</p></div>
 <div class="mini"><h4>Speed (scalar)</h4><p>Distance ÷ time. How fast, regardless of direction.</p></div>
 <div class="mini"><h4>Velocity (vector)</h4><p>Displacement ÷ time. How fast <i>and</i> which way. Can be negative.</p></div>
</div>
{worked("A runner goes 400 m around a track in 80 s and finishes where she started. Find her average speed and average velocity.", "Average speed = distance/time = 400/80 = <b>5 m/s</b>. Average velocity = displacement/time = 0/80 = <b>0 m/s</b>, because she ends where she began.")}
{box("trap", "Common mistake", "Treating distance and displacement as the same thing. They're equal only for straight-line motion that never reverses.")}
''', pill=("e", "UNIT 1.1"), sub="The vocabulary every other topic builds on.",
 det=("Why the sign convention matters", '''
<h4>Signs carry direction</h4><p>In one dimension, the + or − on a vector is its direction. Once you pick "right is positive," a velocity of −4 m/s means 4 m/s to the left. The sign isn't optional; dropping it is the most common source of wrong answers in kinematics.</p>
<h4>Position depends on where you put zero</h4><p>Position values change if you move the origin, but displacement doesn't. Starting at x = 2 m and ending at x = 7 m gives Δx = +5 m; with the origin moved, x = 12 m to 17 m, still Δx = +5 m. Physics only cares about changes.</p>
<h4>Scalars from vectors</h4><p>Speed is the magnitude (absolute value) of velocity at an instant. Average speed, though, is not the magnitude of average velocity: a round trip has nonzero average speed and zero average velocity.</p>
<h4>On the exam</h4><p>Many conceptual questions are built on this difference: a ball thrown up and caught at the same height has zero displacement, zero average velocity, but nonzero distance and average speed.</p>'''))

VELACC = topic("vel-acc", "Velocity and acceleration", f'''
<div class="big-eq">v<sub>avg</sub> = Δx/Δt &nbsp;&nbsp;&nbsp;&nbsp; a<sub>avg</sub> = Δv/Δt</div>
<p><b>Velocity</b> is the rate of change of position. <b>Acceleration</b> is the rate of change of velocity: how many m/s the velocity changes each second, so its units are m/s².</p>
<h3>Speeding up or slowing down?</h3>
<p>The sign of acceleration alone doesn't tell you. Compare it with the sign of velocity:</p>
<div class="tblwrap"><table><tr><th>v</th><th>a</th><th>The object is…</th></tr>
<tr><td>+</td><td>+</td><td>speeding up (moving right, faster)</td></tr>
<tr><td>+</td><td>−</td><td>slowing down</td></tr>
<tr><td>−</td><td>−</td><td>speeding up (moving left, faster)</td></tr>
<tr><td>−</td><td>+</td><td>slowing down</td></tr></table></div>
<p><b>Same signs → speeding up. Opposite signs → slowing down.</b></p>
{sim({"type": "motion", "v0": 8, "a": -4, "T": 3, "obj": "ball"}, "v positive, a negative: slows, stops, then speeds up the other way")}
{worked("A car's velocity changes from +20 m/s to +5 m/s in 3.0 s. Find its acceleration.", "a = Δv/Δt = (5 − 20)/3.0 = <b>−5.0 m/s²</b>. Velocity is positive and acceleration negative, so the car is slowing down.")}
{box("trap", "Common mistake", "\"Negative acceleration means slowing down.\" Not always: a car moving left (negative) with negative acceleration is speeding up.")}
''', pill=("e", "UNIT 1.2"), sub="Rates of change, and what their signs tell you.",
 det=("Average vs. instantaneous, and zero velocity", '''
<h4>Instantaneous values</h4><p>Average velocity uses a whole time interval. Instantaneous velocity is the velocity at one moment, which is the slope of the position–time graph at that point (the slope of the tangent line). The speedometer in a car shows instantaneous speed.</p>
<h4>Zero velocity doesn't mean zero acceleration</h4><p>A ball thrown straight up has v = 0 at the top, but its acceleration is still −10 m/s² (gravity never switches off). If acceleration were zero there, the ball would hang in the air forever.</p>
<h4>Constant velocity means zero acceleration</h4><p>If velocity doesn't change (same speed, same direction), a = 0. A car on cruise control along a straight road has zero acceleration even at 30 m/s.</p>
<h4>Units</h4><p>a = 3 m/s² means the velocity changes by 3 m/s every second: 0, 3, 6, 9 m/s after 0, 1, 2, 3 s.</p>'''))

CH.append(chapter("describing", "Describing Motion", "Describing Motion", [SCALARS, VELACC]))

# ---------------- Constant acceleration ----------------
EQS = topic("four-equations", "The four constant-acceleration equations", f'''
<p>When acceleration is constant, five quantities describe the motion: <b>v₀</b> (starting velocity), <b>v</b> (final velocity), <b>a</b>, <b>t</b>, and <b>Δx</b>. Each equation leaves one of them out. These are the lines on your class equation sheet:</p>
<div class="tblwrap"><table><tr><th>Equation (sheet)</th><th>Leaves out</th><th>Use when the problem doesn't mention…</th></tr>
<tr><td><span class="eq">v = v₀ + at</span></td><td>Δx</td><td>distance</td></tr>
<tr><td><span class="eq">Δx = ½(v + v₀)t</span></td><td>a</td><td>acceleration</td></tr>
<tr><td><span class="eq">Δx = v₀t + ½at²</span></td><td>v</td><td>final velocity</td></tr>
<tr><td><span class="eq">v² = v₀² + 2aΔx</span></td><td>t</td><td>time</td></tr></table></div>
<h3>The method</h3>
<ol class="steps"><li>Pick a positive direction.</li><li>List v₀, v, a, t, Δx with signs; mark the unknown and the one you don't care about.</li><li>Use the equation that leaves out the one you don't care about.</li></ol>
{worked("A car starts from rest and accelerates at 3.0 m/s² for 5.0 s. How fast is it going, and how far does it travel?", "v₀ = 0, a = 3, t = 5. Speed: v = v₀ + at = 0 + 3(5) = <b>15 m/s</b>. Distance: Δx = v₀t + ½at² = 0 + ½(3)(25) = <b>37.5 m</b>.")}
{worked("A car moving at 20 m/s brakes at 5.0 m/s². How long and how far does it take to stop?", "Take forward as +: v₀ = 20, v = 0, a = −5. Time: 0 = 20 − 5t → <b>t = 4.0 s</b>. Distance (no time needed): 0 = 20² + 2(−5)Δx → <b>Δx = 40 m</b>.")}
{sim({"type": "motion", "v0": 0, "a": 3, "T": 5, "ask": ["x"]}, "Starts from rest, a = 3 m/s²")}
''', pill=("e", "UNIT 1.2"), sub="The core toolkit of the unit.",
 det=("Where the equations come from, and when they fail", '''
<h4>Derivations</h4><p>Constant acceleration means velocity changes linearly: v = v₀ + at (the definition of a, rearranged). The average velocity is then halfway between v₀ and v, so Δx = ½(v₀ + v)t. Substituting v = v₀ + at gives Δx = v₀t + ½at². Eliminating t between the first two gives v² = v₀² + 2aΔx.</p>
<h4>Only for constant acceleration</h4><p>If acceleration changes (a car that speeds up then cruises), split the motion into pieces where a is constant and solve each piece separately. The final velocity of one piece is the starting velocity of the next.</p>
<h4>Two answers from v²</h4><p>v² = v₀² + 2aΔx gives v², and the square root has a ± sign. Physics decides which: a ball thrown up passes the same height going up (+) and coming down (−).</p>
<h4>Hidden values</h4><p>"Starts from rest" means v₀ = 0. "Comes to a stop" means v = 0. "Dropped" means v₀ = 0 and a = −g (if up is positive). "At the top" of a vertical throw, v = 0.</p>'''))

FREEFALL = topic("free-fall", "Free fall", f'''
<p>Near Earth's surface, anything moving only under gravity has a constant acceleration of <b>g ≈ 10 m/s² downward</b>, whether it's moving up, down, or momentarily stopped. Mass doesn't matter (ignoring air resistance).</p>
{eq("a = −g = −10 m/s² &nbsp;&nbsp;(taking up as positive)")}
{sim({"type": "projectile", "v0": 20, "ang": 90}, "Thrown straight up at 20 m/s")}
{worked("A rock is dropped from a 45 m cliff. How long does it fall, and how fast does it hit?", "Down as +: v₀ = 0, a = 10, Δx = 45. Δx = ½at² → 45 = 5t² → <b>t = 3.0 s</b>. v = at = 10(3) = <b>30 m/s</b>.")}
{worked("A ball is thrown straight up at 20 m/s. Find the time to the top, the maximum height, and the total time until it returns to the launch height.", "Up as +: at the top v = 0. 0 = 20 − 10t → <b>t = 2.0 s</b>. 0 = 20² − 2(10)Δy → <b>Δy = 20 m</b>. Going up and coming down take equal time, so it returns after <b>4.0 s</b>, moving at 20 m/s downward.")}
{worked("A ball is thrown up at 10 m/s from the top of a 15 m cliff. When does it hit the ground below?", "Up as +: Δy = −15 (ends below the start), v₀ = 10, a = −10. −15 = 10t − 5t² → 5t² − 10t − 15 = 0 → t² − 2t − 3 = 0 → (t − 3)(t + 1) = 0 → <b>t = 3.0 s</b> (the negative root is not physical). This is where the quadratic formula on your sheet comes in.")}
{box("trap", "Common mistake", "Saying acceleration is zero at the top. Velocity is zero there; acceleration is still −10 m/s².")}
''', pill=("e", "UNIT 1.2"), sub="Constant acceleration, provided by gravity.",
 det=("Symmetry, signs and the quadratic", '''
<h4>Up-and-down symmetry</h4><p>Without air resistance, the upward trip is a mirror image of the downward trip: same time, and at each height the speed is the same going up and coming down. A ball thrown up at 20 m/s comes back to your hand at 20 m/s.</p>
<h4>Pick one sign convention for the whole trip</h4><p>With up as positive, a = −10 m/s² the entire time, including on the way down. Don't switch signs halfway; the equations handle the turnaround automatically.</p>
<h4>When time appears squared</h4><p>Δx = v₀t + ½at² is quadratic in t. Rearrange to ½at² + v₀t − Δx = 0 and use the quadratic formula. One root is usually negative or describes the wrong part of the motion; choose the one that matches the story.</p>
<h4>Heavier objects don't fall faster</h4><p>Gravity pulls harder on a heavier object, but it also has more inertia, and the two effects cancel exactly. Air resistance is what makes a feather fall slowly; in a vacuum a feather and a hammer land together.</p>'''))
CH.append(chapter("const-accel", "Constant Acceleration", "Equations", [EQS, FREEFALL]))

# ---------------- Graphs ----------------
G1 = '''<svg viewBox="0 0 440 200" role="img" aria-label="Velocity versus time graph: rises from 0 to 10 m/s over 4 s, then constant to 6 s">
<g fill="currentColor" font-size="12"><line x1="40" y1="170" x2="420" y2="170" stroke="currentColor" opacity=".5"/><line x1="40" y1="20" x2="40" y2="170" stroke="currentColor" opacity=".5"/>
<polygon points="40,170 280,50 400,50 400,170" fill="#D9D4CA" opacity=".25"/><polyline points="40,170 280,50 400,50" fill="none" stroke="#D9D4CA" stroke-width="3"/>
<text x="6" y="54">10</text><text x="276" y="186">4</text><text x="396" y="186">6</text><text x="410" y="166">t (s)</text><text x="4" y="16">v (m/s)</text>
<text x="160" y="140">20 m</text><text x="330" y="120">20 m</text></g></svg>'''
GRAPHS = topic("motion-graphs", "Motion graphs", f'''
<div class="tblwrap"><table><tr><th>Graph</th><th>Slope gives</th><th>Area under it gives</th></tr>
<tr><td>position vs. time</td><td>velocity</td><td>(not used)</td></tr>
<tr><td>velocity vs. time</td><td>acceleration</td><td>displacement</td></tr>
<tr><td>acceleration vs. time</td><td>(not used)</td><td>change in velocity</td></tr></table></div>
<h3>Reading shapes</h3>
<ul><li><b>Position–time:</b> straight line = constant velocity; curving upward = positive acceleration; curving downward = negative acceleration; flat = at rest.</li>
<li><b>Velocity–time:</b> flat = constant velocity; straight sloped line = constant acceleration; crossing the axis = turning around.</li>
<li>Area below the time axis counts as negative displacement.</li></ul>
{G1}
{worked("Using the graph above, find the acceleration during the first 4 s and the total displacement.", "Acceleration = slope = (10 − 0)/(4 − 0) = <b>2.5 m/s²</b>. Displacement = area: triangle ½(4)(10) = 20 m plus rectangle (2)(10) = 20 m, total <b>40 m</b>.")}
{sim({"type": "motion", "v0": -6, "a": 3, "T": 4}, "Starts moving left, turns around at t = 2 s")}
{box("trap", "Common mistake", "Reading the value of a graph when the question asks for its slope (or the reverse). On a position–time graph, the height is position; velocity is the steepness.")}
''', pill=("e", "UNIT 1.3"), sub="The most-tested skill in Unit 1.",
 det=("Translating between graphs", '''
<h4>From x–t to v–t</h4><p>At each time, estimate the slope of the x–t graph and plot it as a v value. A parabola on the x–t graph (constant acceleration) becomes a straight line on the v–t graph. The top of a hill on the x–t graph (where the slope is zero) is where the v–t graph crosses zero.</p>
<h4>From v–t to a–t</h4><p>Slope of v–t becomes the a value. A straight sloped v–t line gives a flat a–t line; a flat v–t line gives a = 0.</p>
<h4>Going the other way with areas</h4><p>To get displacement from a v–t graph, add up areas of rectangles and triangles, counting area below the axis as negative. To get distance traveled, count all areas as positive.</p>
<h4>Checking a sketch</h4><p>Exam questions often ask you to sketch a graph from a description. Check: where the object is at rest (v = 0), where it turns around (v changes sign), and whether it's speeding up or slowing down (compare the signs of v and a).</p>
<h4>Curved velocity graphs</h4><p>If the v–t graph is curved, acceleration is changing, and the four equations no longer apply. Slopes and areas still work, though.</p>'''))
CH.append(chapter("graphs-u1", "Motion Graphs", "Graphs", [GRAPHS]))

# ---------------- Vectors and projectiles ----------------
VECT = topic("vectors-2d", "Vectors in two dimensions", f'''
<p>A vector in two dimensions has an x part and a y part, called its <b>components</b>. For a vector of size A at angle θ above the +x axis:</p>
{eq("A<sub>x</sub> = A cos θ &nbsp;&nbsp;&nbsp;&nbsp; A<sub>y</sub> = A sin θ")}
{sim({"type": "vector", "mag": 10, "ang": 37}, "Splitting a vector into components")}
<p>To go back from components to a vector: <span class="eq">A = √(A<sub>x</sub>² + A<sub>y</sub>²)</span> and <span class="eq">θ = tan⁻¹(A<sub>y</sub>/A<sub>x</sub>)</span>.</p>
<p><b>Adding vectors:</b> add all the x components, add all the y components, then rebuild the total.</p>
{sim({"type": "vector", "A": [8, 0], "B": [6, 90]}, "8 east plus 6 north makes 10 at about 37°")}
{worked("A velocity of 10 m/s points 37° above horizontal. Find its components. (cos 37° ≈ 0.80, sin 37° ≈ 0.60)", "v<sub>x</sub> = 10 × 0.80 = <b>8.0 m/s</b>; v<sub>y</sub> = 10 × 0.60 = <b>6.0 m/s</b>. Check: √(8² + 6²) = 10 ✓.")}
''', pill=("e", "UNIT 1.5"), sub="Components turn one 2-D problem into two 1-D problems.",
 det=("Getting components right", '''
<h4>Which one gets cosine?</h4><p>Cosine goes with the side next to (adjacent to) the angle. If θ is measured from the horizontal, the x component uses cos; if θ is measured from the vertical, the y component uses cos. Always check where the angle is measured from.</p>
<h4>Signs</h4><p>Components pointing left or down are negative. A vector at 150° has a negative x component (cos 150° < 0) and a positive y component.</p>
<h4>Quick sanity check</h4><p>Each component must be smaller than the vector itself. If θ is small (nearly horizontal), the x component is nearly the full size; if θ is near 90°, the y component is.</p>
<h4>Useful values</h4><p>sin 30° = cos 60° = 0.5; cos 30° = sin 60° ≈ 0.87; sin 45° = cos 45° ≈ 0.71. The 3-4-5 triangle (37° and 53°) shows up often because its components come out as clean numbers.</p>'''))

PROJ = topic("projectiles", "Projectile motion", f'''
<p>A projectile moves under gravity alone after it's launched. The trick: <b>horizontal and vertical motion are independent</b>.</p>
<div class="grid2"><div class="mini"><h4>Horizontal (x)</h4><p>No acceleration: <span class="eq">v<sub>x</sub> = constant</span>, <span class="eq">Δx = v<sub>x</sub>t</span>.</p></div>
<div class="mini"><h4>Vertical (y)</h4><p>Free fall: a = −10 m/s². Use the four equations with v<sub>y</sub>.</p></div></div>
<p><b>Time is the link.</b> Usually you find the time from the vertical motion, then use it for the horizontal motion.</p>
<h3>Launched horizontally</h3>
{sim({"type": "projectile", "v0": 12, "ang": 0, "h": 20}, "12 m/s off a 20 m cliff")}
{worked("A ball rolls off a 20 m cliff at 12 m/s horizontally. How long is it in the air, how far from the base does it land, and how fast is it moving at impact?", "Vertical: v<sub>y0</sub> = 0, Δy = 20 m down: 20 = ½(10)t² → <b>t = 2.0 s</b>. Horizontal: Δx = 12 × 2.0 = <b>24 m</b>. At impact v<sub>x</sub> = 12, v<sub>y</sub> = 10 × 2 = 20, so speed = √(12² + 20²) ≈ <b>23 m/s</b>.")}
<h3>Launched at an angle</h3>
{sim({"type": "projectile", "v0": 20, "ang": 30}, "20 m/s at 30° from level ground")}
{worked("A ball is kicked at 20 m/s, 30° above level ground. Find the time of flight, range and maximum height.", "v<sub>x</sub> = 20 cos 30° ≈ 17.3 m/s; v<sub>y</sub> = 20 sin 30° = 10 m/s. Time up = 10/10 = 1 s, so <b>time of flight = 2.0 s</b>. <b>Range</b> = 17.3 × 2.0 ≈ <b>34.6 m</b>. <b>Max height</b> = v<sub>y</sub>²/(2g) = 100/20 = <b>5.0 m</b>.")}
{box("tip", "Pattern", "Two objects released from the same height, one dropped and one launched horizontally, hit the ground at the same time. Horizontal speed doesn't affect falling time.")}
''', pill=("e", "UNIT 1.5"), sub="Two independent 1-D motions sharing one clock.",
 det=("Projectile facts the exam tests", '''
<h4>At the top</h4><p>v<sub>y</sub> = 0 but v<sub>x</sub> is unchanged, so the speed at the top is v<sub>x</sub>, not zero. Acceleration is still 10 m/s² downward everywhere.</p>
<h4>Range and angle</h4><p>On level ground, range = (v₀² sin 2θ)/g, largest at 45°. Complementary angles (30° and 60°) give the same range; the higher angle stays in the air longer and goes higher. The formula only works when launch and landing heights are equal.</p>
<h4>Different heights</h4><p>When launch and landing heights differ, find time from Δy = v<sub>y0</sub>t − ½gt² (often a quadratic), then range = v<sub>x</sub>t.</p>
<h4>Velocity at any moment</h4><p>Combine the components: v = √(v<sub>x</sub>² + v<sub>y</sub>²), direction tan⁻¹(v<sub>y</sub>/v<sub>x</sub>) below or above horizontal.</p>
<h4>Air resistance</h4><p>AP Physics 1 problems ignore it unless stated. With it, the range and height are smaller and the path is no longer a symmetric parabola.</p>'''))
CH.append(chapter("vectors-proj", "Vectors & Projectiles", "Projectiles", [VECT, PROJ]))

# ---------------- Relative motion ----------------
REL = topic("relative-motion", "Reference frames and relative motion", f'''
<p>Every velocity is measured relative to something. A passenger sitting on a train is at rest relative to the train but moving at the train's speed relative to the ground.</p>
{eq("v<sub>A rel ground</sub> = v<sub>A rel B</sub> + v<sub>B rel ground</sub>")}
{worked("A train moves at 30 m/s. A passenger walks toward the front at 2 m/s. What is the passenger's velocity relative to the ground? What if she walks toward the back?", "Forward: 2 + 30 = <b>32 m/s</b>. Backward: −2 + 30 = <b>28 m/s</b> (still moving forward relative to the ground).")}
{worked("Two cars drive toward each other at 20 m/s and 25 m/s. How fast does the gap between them close?", "Relative to car A, car B moves at 25 + 20 = <b>45 m/s</b> toward it.")}
<h3>Crossing a river</h3>
<p>The boat's velocity relative to the shore is the vector sum of its velocity relative to the water and the water's velocity.</p>
{sim({"type": "river", "vb": 4, "vr": 3, "w": 80}, "Boat aims straight across at 4 m/s; river flows at 3 m/s")}
{worked("A boat heads straight across an 80 m river at 4 m/s relative to the water. The river flows at 3 m/s. How long does the crossing take, how far downstream does it land, and what is its speed relative to the shore?", "Across: t = 80/4 = <b>20 s</b> (the current doesn't change this). Downstream: 3 × 20 = <b>60 m</b>. Speed: √(4² + 3²) = <b>5 m/s</b>.")}
''', pill=("e", "UNIT 1.4"), sub="Motion looks different depending on who's watching.",
 det=("Reference frames in more depth", '''
<h4>All inertial frames are equally valid</h4><p>A frame moving at constant velocity is as good as one at rest. Someone on a smoothly moving train who drops a ball sees it fall straight down; someone on the ground sees the same ball follow a parabola. Both are correct descriptions.</p>
<h4>Acceleration is the same in all of them</h4><p>Adding a constant velocity to every velocity doesn't change how velocities change, so acceleration is the same in every inertial frame. That's why g = 10 m/s² for the falling ball in both the train and ground frames.</p>
<h4>Subtracting velocities</h4><p>The velocity of A relative to B is v<sub>A</sub> − v<sub>B</sub> (both relative to the ground). Two cars moving the same way at 25 and 20 m/s close at 5 m/s; moving toward each other (+25 and −20), at 45 m/s.</p>
<h4>Aiming upstream</h4><p>To land directly across, the boat must point partly upstream so that its upstream component cancels the current. That leaves less of its speed for crossing, so the trip takes longer.</p>'''))
CH.append(chapter("relative", "Relative Motion", "Relative Motion", [REL]))

# ---------------- Labs & FRQs ----------------
LINU1 = '''<div class="tblwrap"><table><tr><th>Experiment</th><th>Equation</th><th>Graph</th><th>Slope</th></tr>
<tr><td>Drop from rest, measure fall time</td><td>Δy = ½gt²</td><td>Δy vs. t²</td><td>g/2</td></tr>
<tr><td>Cart down a ramp from rest</td><td>Δx = ½at²</td><td>Δx vs. t²</td><td>a/2</td></tr>
<tr><td>Speed after distance d from rest</td><td>v² = 2ad</td><td>v² vs. d</td><td>2a</td></tr>
<tr><td>Horizontal launch from height h</td><td>Δx = v₀√(2h/g)</td><td>Δx vs. √h</td><td>v₀√(2/g)</td></tr>
<tr><td>Constant acceleration, velocity sensor</td><td>v = v₀ + at</td><td>v vs. t</td><td>a</td></tr></table></div>'''
LABS1 = topic("labs-u1", "Experiments and graphs in kinematics", f'''
<p>Experimental design questions in this unit usually ask you to measure g or an acceleration and to linearize the data. Use the same procedure checklist as always: what you change, what you measure and with what, what stays the same, repeated trials, and what you graph.</p>
{LINU1}
{worked("A student drops a ball from several heights and measures fall times with a photogate: t (s) = 0.20, 0.30, 0.40, 0.50; Δy (m) = 0.21, 0.44, 0.81, 1.24. Find g.", "Graph Δy against t² (0.04, 0.09, 0.16, 0.25). Slope ≈ (1.24 − 0.21)/(0.25 − 0.04) ≈ 4.9 m/s². Since slope = g/2, <b>g ≈ 9.8 m/s²</b>.")}
{box("tip", "FRQ habit", "When asked to sketch a graph, label both axes, mark key values (where it crosses zero, where it's maximum), and make the shape match: straight for constant rates, curved where the rate changes.")}
''', sub="What the experimental design question looks like for Unit 1.",
 det=("Common Unit 1 experiments and errors", '''
<h4>Measuring time accurately</h4><p>Stopwatches add human reaction time (about 0.2 s), a random error that's large compared with short fall times. Photogates or video analysis reduce it. Longer drops make the same reaction error a smaller fraction of the time.</p>
<h4>Air resistance as a systematic error</h4><p>Air resistance makes falling objects take longer, so the calculated g comes out smaller than the true value. Using a dense, compact object reduces it.</p>
<h4>Ramp experiments</h4><p>A cart on a ramp accelerates at less than g (roughly g sin θ). Measuring Δx and t at several distances and graphing Δx vs. t² gives a straight line with slope a/2.</p>
<h4>Motion sensors</h4><p>A motion sensor gives position and velocity graphs directly. The slope of its velocity–time graph is the acceleration, and the area under it is the displacement, which you can check against a meter stick.</p>'''))
LQ1 = [
 {"t": "e", "q": "A student measures fall times t for a ball dropped from several heights Δy. To get a straight line, what should be graphed?",
  "o": ["Δy vs. t", "Δy vs. t²", "Δy² vs. t", "√Δy vs. t²"], "a": 1,
  "x": "Δy = ½gt², so Δy is proportional to t². A graph of Δy against t² is a straight line through the origin with slope g/2."},
 {"t": "e", "q": "The slope of a Δy vs. t² graph for falling objects is 4.8 m/s². What value of g does this give?",
  "o": ["2.4 m/s²", "4.8 m/s²", "9.6 m/s²", "19.2 m/s²"], "a": 2,
  "x": "Slope = g/2, so g = 2 × 4.8 = 9.6 m/s²."},
 {"t": "e", "q": "Students time a falling ball with a handheld stopwatch. Which change most reduces random error?",
  "o": ["Using a lighter ball", "Using a photogate and averaging several trials", "Dropping from a lower height", "Measuring only once, carefully"], "a": 1,
  "x": "Human reaction time is the main random error. A photogate removes it, and averaging trials reduces whatever remains."},
]
CH.append(chapter("labs-frq-u1", "Labs & FRQs", "Labs & FRQs", [LABS1, quiz_section("labs-quiz-u1", "Practice: experiments", "3 questions.", "quiz-labs-u1", {"e": "Kinematics"})]))

# ---------------- Review ----------------
REV1 = topic("review-u1", "Your equation sheet (Unit 1 lines)", f'''
<div class="tblwrap"><table><tr><th>On the sheet</th><th>In words</th><th>Use it when</th></tr>
<tr><td><span class="eq">v = v₀ + at</span></td><td>final velocity = start + acceleration × time</td><td>no distance involved</td></tr>
<tr><td><span class="eq">Δx = ½(v + v₀)t</span></td><td>distance = average velocity × time</td><td>no acceleration given or needed</td></tr>
<tr><td><span class="eq">Δx = v₀t + ½at²</span></td><td>distance with acceleration</td><td>no final velocity</td></tr>
<tr><td><span class="eq">v² = v₀² + 2aΔx</span></td><td>velocity and distance, no time</td><td>no time given or needed</td></tr>
<tr><td><span class="eq">x = (−b ± √(b² − 4ac))/2a</span></td><td>quadratic formula</td><td>solving Δx = v₀t + ½at² for t</td></tr></table></div>
<h3>Not on the sheet</h3>
<div class="tblwrap"><table><tr><th>Equation</th><th>Meaning</th></tr>
<tr><td><span class="eq">v<sub>avg</sub> = Δx/Δt</span>, <span class="eq">a = Δv/Δt</span></td><td>definitions</td></tr>
<tr><td><span class="eq">A<sub>x</sub> = A cos θ, A<sub>y</sub> = A sin θ</span></td><td>vector components</td></tr>
<tr><td><span class="eq">v = √(2gh)</span>, <span class="eq">t = √(2h/g)</span></td><td>dropped from height h</td></tr>
<tr><td><span class="eq">t<sub>top</sub> = v₀/g</span>, <span class="eq">h<sub>max</sub> = v₀²/(2g)</span></td><td>thrown straight up</td></tr></table></div>
''', sub="The lines you'll use for kinematics.")
MIST1 = topic("mistakes-u1", "Common mistakes", '''<ol class="steps">
<li>Dropping the sign on a velocity or acceleration.</li>
<li>Saying acceleration is zero at the top of a throw.</li>
<li>Using the four equations when acceleration isn't constant.</li>
<li>Mixing x and y components in projectile problems (only time is shared).</li>
<li>Giving the speed at the top of a projectile's path as zero (it's v<sub>x</sub>).</li>
<li>Reading a graph's value when the question asks for its slope or area.</li>
<li>Forgetting that "dropped" means v₀ = 0 and "stops" means v = 0.</li></ol>''', sub="Points students lose most often.")
CH.append(chapter("review-ch-u1", "Review & Equation Sheet", "Review", [REV1, MIST1]))

# ---------------- Practice ----------------
close(5*4, 20); close((25-5)/4, 5); close(0.5*2*36, 36); close(math.sqrt(2*g*80), 40); close(math.sqrt(2*80/g), 4)
close(15/g, 1.5); close(15**2/(2*g), 11.25); close(math.sqrt(2*5/g), 1); close(15*1, 15)
close(30*math.cos(math.radians(53)), 18.05, 0.01); close(10*math.sin(math.radians(30)), 5)
close(0.5*6*12, 36); close((12-(-6))/6, 3); close(math.hypot(6, 8), 10); close(60/5, 12)
close(12+ 0.5*(-4)*0, 12)
close(20 + 0.5*2*25, 45); close(math.sqrt(0 + 2*4*50), 20); close(0.5*(10+30)*5, 100)
PQ = [
 {"t": "e", "q": "A car travels 3 km north and then 4 km south. What are its distance traveled and displacement?",
  "o": ["7 km; 1 km south", "7 km; 7 km south", "1 km; 1 km south", "7 km; 0 km"], "a": 0,
  "x": "Distance adds path lengths: 3 + 4 = 7 km. Displacement: +3 − 4 = −1 km, i.e. 1 km south."},
 {"t": "e", "q": "An object has a negative velocity and a positive acceleration. What is happening?",
  "o": ["It is speeding up in the negative direction", "It is slowing down", "It is at rest", "It is moving at constant speed"], "a": 1,
  "x": "Opposite signs of v and a mean the object is slowing down."},
 {"t": "e", "q": "A cart starts from rest with a = 5.0 m/s². What is its velocity after 4.0 s?",
  "o": ["1.25 m/s", "9 m/s", "20 m/s", "40 m/s"], "a": 2, "x": "v = v₀ + at = 0 + 5(4) = 20 m/s.",
  "sim": {"type": "motion", "v0": 0, "a": 5, "T": 4, "ask": ["v"]}},
 {"t": "e", "q": "A car speeds up from 5 m/s to 25 m/s in 4.0 s. What is its acceleration?",
  "o": ["5 m/s²", "6.25 m/s²", "7.5 m/s²", "20 m/s²"], "a": 0, "x": "a = Δv/Δt = (25 − 5)/4 = 5 m/s²."},
 {"t": "e", "q": "A cart starts from rest and accelerates at 2.0 m/s² for 6.0 s. How far does it go?",
  "o": ["12 m", "24 m", "36 m", "72 m"], "a": 2, "x": "Δx = v₀t + ½at² = 0 + ½(2)(36) = 36 m.",
  "sim": {"type": "motion", "v0": 0, "a": 2, "T": 6, "ask": ["x"]}},
 {"t": "e", "q": "A car moving at 20 m/s brakes to a stop with an acceleration of −5 m/s². How far does it travel while stopping?",
  "o": ["4 m", "20 m", "40 m", "80 m"], "a": 2, "x": "No time given: v² = v₀² + 2aΔx → 0 = 400 + 2(−5)Δx → Δx = 40 m.",
  "sim": {"type": "motion", "v0": 20, "a": -5, "T": 4, "obj": "car", "ask": ["x"]}},
 {"t": "e", "q": "A stone is dropped from rest from a height of 80 m. How long does it take to reach the ground?",
  "o": ["2 s", "4 s", "8 s", "16 s"], "a": 1, "x": "80 = ½(10)t² → t² = 16 → t = 4 s."},
 {"t": "e", "q": "The same stone (dropped from 80 m) hits the ground at what speed?",
  "o": ["20 m/s", "40 m/s", "80 m/s", "800 m/s"], "a": 1, "x": "v = √(2gh) = √(2·10·80) = √1600 = 40 m/s. (Or v = gt = 10 × 4 = 40 m/s.)"},
 {"t": "e", "q": "A ball is thrown straight up at 15 m/s. How long does it take to reach its highest point?",
  "o": ["0.67 s", "1.5 s", "3.0 s", "15 s"], "a": 1, "x": "At the top v = 0: 0 = 15 − 10t → t = 1.5 s.",
  "sim": {"type": "projectile", "v0": 15, "ang": 90, "ask": ["H"]}},
 {"t": "e", "q": "How high does a ball thrown straight up at 15 m/s rise?",
  "o": ["1.5 m", "7.5 m", "11.25 m", "22.5 m"], "a": 2, "x": "0 = 15² − 2(10)h → h = 225/20 = 11.25 m."},
 {"t": "e", "q": "At the highest point of a ball thrown straight up, which is true?",
  "o": ["v = 0 and a = 0", "v = 0 and a = 10 m/s² downward", "v = 10 m/s and a = 0", "Both v and a point up"], "a": 1,
  "x": "Velocity is momentarily zero, but gravity still accelerates the ball at 10 m/s² downward."},
 {"t": "e", "q": "On a position-time graph, what does the slope represent?",
  "o": ["Acceleration", "Velocity", "Displacement", "Distance"], "a": 1, "x": "Slope = Δx/Δt = velocity."},
 {"t": "e", "q": "On a velocity-time graph, what does the area under the line represent?",
  "o": ["Acceleration", "Velocity", "Displacement", "Jerk"], "a": 2, "x": "Area = v × t = displacement (area below the axis counts as negative)."},
 {"t": "e", "q": "A velocity-time graph is a straight line from 10 m/s at t = 0 to 30 m/s at t = 5 s. How far does the object travel in those 5 s?",
  "o": ["50 m", "100 m", "150 m", "200 m"], "a": 1, "x": "Area of the trapezoid = ½(10 + 30)(5) = 100 m. Equivalently Δx = ½(v + v₀)t from the sheet."},
 {"t": "e", "q": "A position-time graph is a straight horizontal line. What is the object doing?",
  "o": ["Moving at constant velocity", "Accelerating", "At rest", "Slowing down"], "a": 2, "x": "Zero slope means zero velocity: the object is at rest."},
 {"t": "e", "q": "An object's velocity-time graph crosses from positive to negative values. What happens at the crossing?",
  "o": ["It stops permanently", "It turns around", "Its acceleration becomes zero", "It speeds up"], "a": 1,
  "x": "Velocity changes sign, so the object momentarily stops and reverses direction.",
  "sim": {"type": "motion", "v0": 6, "a": -3, "T": 4}},
 {"t": "e", "q": "A vector of size 10 points 30° above the +x axis. What is its y component?",
  "o": ["5.0", "8.7", "10", "0.5"], "a": 0, "x": "A<sub>y</sub> = A sin θ = 10 sin 30° = 10(0.5) = 5.0.",
  "sim": {"type": "vector", "mag": 10, "ang": 30, "ask": ["y"]}},
 {"t": "e", "q": "Vectors of 6 east and 8 north are added. What is the size of the result?",
  "o": ["2", "10", "14", "48"], "a": 1, "x": "√(6² + 8²) = √100 = 10.", "sim": {"type": "vector", "A": [6, 0], "B": [8, 90], "scale": 14}},
 {"t": "e", "q": "A ball rolls off a table 5.0 m high at 15 m/s horizontally. How long is it in the air?",
  "o": ["0.33 s", "1.0 s", "2.0 s", "3.0 s"], "a": 1, "x": "Only the vertical motion matters for time: 5 = ½(10)t² → t = 1.0 s.",
  "sim": {"type": "projectile", "v0": 15, "ang": 0, "h": 5, "ask": ["t", "R"]}},
 {"t": "e", "q": "How far from the base of the 5.0 m table does that ball land?",
  "o": ["5 m", "10 m", "15 m", "30 m"], "a": 2, "x": "Δx = v<sub>x</sub>t = 15 × 1.0 = 15 m."},
 {"t": "e", "q": "One ball is dropped and an identical ball is launched horizontally from the same height at the same moment. Which lands first?",
  "o": ["The dropped ball", "The launched ball", "They land at the same time", "It depends on the launch speed"], "a": 2,
  "x": "Both start with zero vertical velocity and have the same vertical acceleration, so they fall for the same time."},
 {"t": "e", "q": "At the top of its path, a projectile launched at an angle has…",
  "o": ["zero velocity", "only a horizontal velocity", "only a vertical velocity", "zero acceleration"], "a": 1,
  "x": "v<sub>y</sub> = 0 at the top, but v<sub>x</sub> stays constant the whole flight."},
 {"t": "e", "q": "A ball is kicked at 10 m/s, 30° above level ground. What is its initial vertical velocity?",
  "o": ["5.0 m/s", "8.7 m/s", "10 m/s", "0 m/s"], "a": 0, "x": "v<sub>y</sub> = 10 sin 30° = 5.0 m/s."},
 {"t": "e", "q": "Which launch angle gives the greatest range on level ground (no air resistance)?",
  "o": ["30°", "45°", "60°", "90°"], "a": 1, "x": "Range ∝ sin 2θ, which is largest at 2θ = 90°, so θ = 45°."},
 {"t": "e", "q": "A train moves at 25 m/s. A passenger walks toward the back of the train at 1.5 m/s. What is the passenger's speed relative to the ground?",
  "o": ["1.5 m/s", "23.5 m/s", "25 m/s", "26.5 m/s"], "a": 1, "x": "Relative to the ground: 25 + (−1.5) = 23.5 m/s, still in the train's direction."},
 {"t": "e", "q": "A boat heads straight across a river at 6 m/s relative to the water; the current is 8 m/s. What is the boat's speed relative to the shore?",
  "o": ["2 m/s", "10 m/s", "14 m/s", "48 m/s"], "a": 1, "x": "The velocities are perpendicular: √(6² + 8²) = 10 m/s.",
  "sim": {"type": "river", "vb": 6, "vr": 8, "w": 60, "ask": ["v"]}},
 {"t": "e", "q": "The river in the previous question is 60 m wide. How long does the crossing take?",
  "o": ["6 s", "7.5 s", "10 s", "12 s"], "a": 2, "x": "Only the across component matters: t = 60/6 = 10 s."},
 {"t": "e", "q": "A car moving at 20 m/s accelerates at 2.0 m/s² for 5.0 s. How far does it travel during that time?",
  "o": ["25 m", "100 m", "125 m", "45 m"], "a": 2, "x": "Δx = v₀t + ½at² = 20(5) + ½(2)(25) = 100 + 25 = 125 m."},
 {"t": "e", "q": "A cart starts from rest and accelerates at 4.0 m/s² over 50 m. How fast is it moving at the end?",
  "o": ["10 m/s", "14 m/s", "20 m/s", "200 m/s"], "a": 2, "x": "No time: v² = 0 + 2(4)(50) = 400 → v = 20 m/s."},
 {"t": "e", "q": "A car speeds up uniformly from 10 m/s to 30 m/s in 5.0 s. How far does it travel?",
  "o": ["50 m", "100 m", "150 m", "200 m"], "a": 1, "x": "No acceleration needed: Δx = ½(v + v₀)t = ½(30 + 10)(5) = 100 m."},
]
CHAL1 = [
 {"t": "e", "q": "A ball is thrown up at 10 m/s from the edge of a 15 m cliff and lands at the bottom. How long is it in the air?",
  "o": ["1.0 s", "2.0 s", "3.0 s", "1.7 s"], "a": 2,
  "x": "Up as +: −15 = 10t − 5t² → t² − 2t − 3 = 0 → (t − 3)(t + 1) = 0 → t = 3.0 s. Answer 2.0 s is only the time to return to the launch height.",
  "sim": {"type": "projectile", "v0": 10, "ang": 90, "h": 15}},
 {"t": "e", "q": "A ball is launched at 20 m/s at 30° above horizontal from a 15 m cliff. How long until it lands on the ground below?",
  "o": ["2.0 s", "3.0 s", "1.0 s", "4.0 s"], "a": 1,
  "x": "v<sub>y0</sub> = 10 m/s. −15 = 10t − 5t² → t² − 2t − 3 = 0 → t = 3.0 s. (The extra 1 s beyond the level-ground flight time is the fall below the launch height.)",
  "sim": {"type": "projectile", "v0": 20, "ang": 30, "h": 15, "ask": ["t", "R"]}},
 {"t": "e", "q": "Car A starts from rest with a = 2.0 m/s² just as car B passes it at a constant 10 m/s. When does A catch B?",
  "o": ["5 s", "10 s", "20 s", "Never"], "a": 1,
  "x": "Same position: ½(2)t² = 10t → t² = 10t → t = 10 s (t = 0 is when they start side by side). At that moment A is moving at 20 m/s, twice B's speed."},
 {"t": "e", "q": "A stone is dropped into a well and the splash is heard 3.0 s later. Ignoring the travel time of sound, how deep is the well? If sound's travel time were included, would the true depth be larger or smaller?",
  "o": ["45 m; smaller", "45 m; larger", "30 m; smaller", "90 m; larger"], "a": 0,
  "x": "Δy = ½(10)(3²) = 45 m. Part of the 3.0 s was spent by the sound coming back up, so the stone actually fell for less than 3.0 s: the true depth is smaller."},
 {"t": "e", "q": "Two balls are launched from level ground at the same speed, one at 30° and one at 60°. Which statement is correct?",
  "o": ["The 60° ball has the larger range", "They have the same range; the 60° ball stays in the air longer", "They have the same range and the same time of flight", "The 30° ball goes higher"], "a": 1,
  "x": "Range ∝ sin 2θ, and sin 60° = sin 120°, so the ranges match. Time of flight ∝ sin θ, so the 60° ball stays up longer and goes higher."},
 {"t": "e", "q": "A velocity-time graph goes from +6 m/s to −6 m/s at a constant rate over 4 s. What are the displacement and the distance traveled?",
  "o": ["0 m and 12 m", "12 m and 12 m", "0 m and 0 m", "24 m and 12 m"], "a": 0,
  "x": "The line crosses zero at t = 2 s. Area above: ½(2)(6) = 6 m; below: −6 m. Displacement = 0; distance = 6 + 6 = 12 m.",
  "sim": {"type": "motion", "v0": 6, "a": -3, "T": 4, "obj": "cart"}},
 {"t": "e", "q": "A boat that moves at 5 m/s relative to the water must land directly across a river flowing at 3 m/s. What is its speed across the river?",
  "o": ["2 m/s", "4 m/s", "5 m/s", "8 m/s"], "a": 1,
  "x": "Aim partly upstream so the upstream component cancels the current: 3 m/s upstream. The across component is √(5² − 3²) = 4 m/s."},
 {"t": "e", "q": "A ball is thrown horizontally from a 45 m tower and lands 60 m from the base. What was its launch speed?",
  "o": ["10 m/s", "20 m/s", "30 m/s", "60 m/s"], "a": 1,
  "x": "Fall time: 45 = 5t² → t = 3 s. Launch speed = 60/3 = 20 m/s.",
  "sim": {"type": "projectile", "v0": 20, "ang": 0, "h": 45, "ask": ["t"]}},
]
close(math.sqrt(25-9), 4); close(60/3, 20)
EX1 = {
 "title": "Unit 1 Practice Exam: Kinematics", "mcqMinutes": 30, "frqMinutes": 25, "tags": {"e": "Kinematics"},
 "mcq": [
  {"t": "e", "k": "concept", "q": "Which quantity is a scalar?", "o": ["Displacement", "Velocity", "Speed", "Acceleration"], "a": 2, "x": "Speed has only magnitude."},
  {"t": "e", "k": "calc", "q": "A cyclist goes from 4 m/s to 10 m/s in 3 s. What is her acceleration?", "o": ["2 m/s²", "3.3 m/s²", "4.7 m/s²", "6 m/s²"], "a": 0, "x": "(10 − 4)/3 = 2 m/s²."},
  {"t": "e", "k": "calc", "q": "A car at rest accelerates at 4 m/s² for 3 s. How far does it go?", "o": ["6 m", "12 m", "18 m", "36 m"], "a": 2, "x": "½(4)(9) = 18 m."},
  {"t": "e", "k": "concept", "q": "A ball is thrown straight up. Ignoring air resistance, its acceleration on the way up is…", "o": ["zero", "10 m/s² up", "10 m/s² down", "increasing"], "a": 2, "x": "Gravity always accelerates it at 10 m/s² downward."},
  {"t": "e", "k": "calc", "q": "An object is dropped from rest from 20 m. With what speed does it hit the ground?", "o": ["10 m/s", "14 m/s", "20 m/s", "40 m/s"], "a": 2, "x": "v = √(2·10·20) = 20 m/s."},
  {"t": "e", "k": "concept", "q": "On a velocity-time graph, a straight line sloping downward that stays above the axis means the object is…", "o": ["moving backward", "slowing down while moving forward", "at rest", "speeding up"], "a": 1, "x": "v positive and decreasing: moving forward and slowing."},
  {"t": "e", "k": "calc", "q": "A velocity-time graph is flat at 8 m/s from t = 0 to t = 5 s. What is the displacement?", "o": ["1.6 m", "13 m", "40 m", "0 m"], "a": 2, "x": "Area = 8 × 5 = 40 m."},
  {"t": "e", "k": "calc", "q": "A car going 30 m/s stops in 6.0 s with constant acceleration. How far does it travel while stopping?", "o": ["45 m", "90 m", "180 m", "5 m"], "a": 1, "x": "Δx = ½(v + v₀)t = ½(0 + 30)(6) = 90 m."},
  {"t": "e", "k": "concept", "q": "A position-time graph curves upward with increasing slope. The object is…", "o": ["at rest", "moving at constant velocity", "speeding up", "slowing down"], "a": 2, "x": "Increasing slope means increasing velocity."},
  {"t": "e", "k": "calc", "q": "A vector of 20 N acts at 60° above horizontal. Its horizontal component is…", "o": ["10 N", "17.3 N", "20 N", "34.6 N"], "a": 0, "x": "20 cos 60° = 10 N."},
  {"t": "e", "k": "calc", "q": "A ball rolls off a 1.25 m table at 4 m/s. How far from the table does it land?", "o": ["0.5 m", "2.0 m", "4.0 m", "5.0 m"], "a": 1, "x": "t: 1.25 = 5t² → t = 0.5 s. Δx = 4 × 0.5 = 2.0 m."},
  {"t": "e", "k": "concept", "q": "For a projectile with no air resistance, which quantity stays constant during the flight?", "o": ["Vertical velocity", "Horizontal velocity", "Speed", "Height"], "a": 1, "x": "No horizontal force means constant v<sub>x</sub>."},
  {"t": "e", "k": "calc", "q": "A projectile is launched at 20 m/s at 30°. How long is it in the air on level ground?", "o": ["1 s", "2 s", "3.5 s", "4 s"], "a": 1, "x": "v<sub>y</sub> = 10 m/s; time up 1 s, total 2 s."},
  {"t": "e", "k": "concept", "q": "Two runners move in the same direction at 6 m/s and 4 m/s. What is the speed of the faster runner relative to the slower one?", "o": ["2 m/s", "5 m/s", "10 m/s", "24 m/s"], "a": 0, "x": "6 − 4 = 2 m/s."},
  {"t": "e", "k": "calc", "q": "A boat moves at 3 m/s straight across a river with a 4 m/s current. How fast is it moving relative to the bank?", "o": ["1 m/s", "5 m/s", "7 m/s", "12 m/s"], "a": 1, "x": "√(3² + 4²) = 5 m/s."},
 ],
 "frq": [
  {"q": "A cart starts from rest at t = 0 and accelerates uniformly at 2.0 m/s² for 4.0 s. It then moves at constant velocity for 3.0 s.",
   "parts": [
    {"p": "(a) Calculate the cart's speed at t = 4.0 s.", "rubric": [["Uses v = v₀ + at", 1], ["Gets 8.0 m/s", 1]], "answer": "v = 0 + 2(4) = 8.0 m/s."},
    {"p": "(b) Calculate the total distance traveled from t = 0 to t = 7.0 s.", "rubric": [["Finds 16 m for the accelerating part", 1], ["Finds 24 m for the constant part and adds to 40 m", 1]], "answer": "First part: ½(2)(4²) = 16 m. Second part: 8.0 × 3.0 = 24 m. Total 40 m."},
    {"p": "(c) Sketch the velocity-time graph from t = 0 to 7.0 s and explain how it confirms your answer to (b).", "rubric": [["Straight line from 0 to 8 m/s over 0–4 s, then flat at 8 m/s", 1], ["States that the area under the graph equals the displacement (16 + 24 = 40 m)", 1]], "answer": "A straight line rising from (0, 0) to (4 s, 8 m/s), then a horizontal line to 7 s. The area under it is a triangle (16 m) plus a rectangle (24 m) = 40 m, matching (b)."},
   ]},
  {"q": "A ball is thrown horizontally at speed v₀ from the top of a building of height h.",
   "parts": [
    {"p": "(a) Derive an expression for the horizontal distance the ball travels before landing, in terms of v₀, h and g.", "rubric": [["Uses h = ½gt² to get t = √(2h/g)", 1], ["Writes Δx = v₀√(2h/g)", 1]], "answer": "Vertical: h = ½gt² → t = √(2h/g). Horizontal: Δx = v₀t = v₀√(2h/g)."},
    {"p": "(b) If the building were 4 times as tall, by what factor would the landing distance change? Justify using your expression.", "rubric": [["Factor of 2", 1], ["Justifies with Δx ∝ √h", 1]], "answer": "Δx ∝ √h, so 4 times the height gives √4 = 2 times the distance."},
    {"p": "(c) A second ball is dropped from the same height at the same moment. Which lands first? Explain.", "rubric": [["They land at the same time", 1], ["Explains that vertical motion is independent of horizontal motion: same vertical starting velocity (0) and same acceleration", 1]], "answer": "Same time. Both start with zero vertical velocity and accelerate downward at g; horizontal velocity doesn't affect the vertical motion."},
   ]},
 ]}
close(math.sqrt(2*1.25/g), 0.5); close(0.5*30*6, 90)

CH.append(chapter("practice-u1", "Practice Questions", "Practice", [quiz_section("practice-quiz-u1", "Practice questions", f"{len(PQ)} questions with animated models. Click an answer to check it. Use g = 10 m/s².", "quiz-u1", {"e": "Kinematics"})]))
CH.append(chapter("challenge-u1", "Challenge Questions", "Challenge", [quiz_section("challenge-quiz-u1", "Challenge questions", "Multi-step problems and traps at the hardest level of the exam. Turn off animated models in ⚙ Settings for a real exam feel.", "quiz-challenge-u1", {"e": "Kinematics"})], hard=True))
CH.append(chapter("exam-ch-u1", "Practice Exam", "Practice Exam", ['<section class="topic" id="exam-box-u1"><h2>Practice exam</h2><p class="sub">15 multiple-choice questions (30 minutes) and 2 free-response questions (25 minutes). No feedback until you submit.</p><div class="exam" data-src="exam-u1"></div></section>']))
CH.append(chapter("calc-u1", "Calculator Program", "Calculator", [calc_section("P1MOTION", "Unit 1", [
  "<b>Find what?</b> menus: final velocity, displacement, acceleration, time (including the quadratic case)",
  "Free fall: dropped, thrown up, thrown up from a height",
  "Projectiles: launched horizontally or at an angle, from the ground or a height",
  "Vectors: components and adding two vectors; relative motion and river crossings",
  "Graphs: slope and area helpers",
  "Show work for every answer, plus notes slides for the whole unit"])]))

shuffle(PQ, 101); shuffle(CHAL1, 102); shuffle(EX1["mcq"], 103); shuffle(LQ1, 104)
DATA = {"quiz-u1": PQ, "quiz-challenge-u1": CHAL1, "quiz-labs-u1": LQ1, "exam-u1": EX1}
HTML = page("unit-1", "AP Physics 1 Unit 1: Kinematics", "AP Physics 1 · Unit 1",
            'Kinematics<br><span class="hl">Motion</span> in 1-D and 2-D',
            f"Displacement, velocity and acceleration, the four constant-acceleration equations, free fall, motion graphs, vectors, projectiles and relative motion: explanations, worked examples, detailed explanations, animated models, {len(PQ)+len(CHAL1)+len(LQ1)} practice questions and a timed practice exam.",
            "AP Physics 1 Unit 1 kinematics review with animations, practice questions and a practice exam.", CH, DATA)
if __name__ == "__main__":
    open("/home/claude/ap-physics-study/courses/ap-physics-1/unit-1.html", "w").write(HTML)
    print("unit 1 written:", len(PQ), len(CHAL1), len(EX1["mcq"]))
