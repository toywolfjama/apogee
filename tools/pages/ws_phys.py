from ws_common import M, build_ws
import math

def landing(a, v, h0=0, g=10):
    th = math.radians(a); vx, vy = v * math.cos(th), v * math.sin(th)
    return vx * (vy + math.sqrt(vy * vy + 2 * g * h0)) / g
assert 28 <= landing(45, math.sqrt(300)) <= 32
assert any(27.3 <= landing(a, 12, 20) <= 28.5 for a in range(5, 86))
assert not 27.3 <= landing(45, 12, 20) <= 28.5   # 45° is not the answer from a cliff

G1 = [
 M("launch-1", "Hit the target", "The launcher is locked at 45°. Choose the launch speed that lands the ball in the green zone.",
   {"type": "launch", "target": [28, 32], "angle": 45, "fixAngle": True, "v": 12, "vmin": 5, "vmax": 30},
   win="At 45° the range is R = v²/g, so R = 30 m needs v = √(30 × 10) ≈ 17.3 m/s. Calculating first gets three stars.",
   hints=["The range of a projectile launched and landing at the same height is R = v² sin(2θ) / g.", "sin(90°) = 1, so R = v²/10. Solve for v with R = 30."]),
 M("launch-2", "Over the wall", "A 12 m wall stands 20 m away. Clear it and land in the target 38–42 m away.",
   {"type": "launch", "target": [38, 42], "wall": {"x": 20, "h": 12}, "angle": 35, "v": 18, "vmin": 5, "vmax": 30},
   win="A steeper launch trades distance for height. Around 60° and 21–22 m/s clears the wall and still reaches 40 m.",
   hints=["At low angles the ball is still low when it reaches the wall.", "Try an angle near 60°, then adjust the speed."]),
 M("launch-3", "Off the cliff", "Now you're on a 20 m cliff and the speed is fixed at 12 m/s. Find an angle that lands in the 27.3–28.5 m zone.",
   {"type": "launch", "target": [27.3, 28.5], "h0": 20, "v": 12, "fixSpeed": True, "angle": 45},
   win="From a height, 45° is no longer the best angle: the ball already has extra fall time, so a flatter launch (about 25–30°) goes furthest.",
   hints=["Try 45° first and see where it lands.", "Lower the angle. The maximum range from a cliff is below 45°."]),
]
G2 = [
 M("col-1", "Sticky carts", "Cart 1 (2 kg) moves at 6 m/s into a cart at rest; they stick. Choose the second cart's mass so they move off together at exactly 2 m/s.",
   {"type": "collide", "init": {"m1": 2, "v1": 6, "m2": 1, "v2": 0}, "sliders": [{"k": "m2", "min": 1, "max": 10, "step": 1}], "kind": "stick", "goal": {"k": "vf", "value": 2, "tol": 0.01, "label": "Final speed"}},
   win="Momentum is conserved: 2 × 6 = (2 + m₂) × 2, so m₂ = 4 kg.",
   hints=["Total momentum before = total momentum after.", "12 kg·m/s = (2 + m₂) × 2."]),
 M("col-2", "Stop dead", "An elastic collision: cart 1 (3 kg, 5 m/s) hits a cart at rest. Choose the second mass so cart 1 stops completely.",
   {"type": "collide", "init": {"m1": 3, "v1": 5, "m2": 1, "v2": 0}, "sliders": [{"k": "m2", "min": 1, "max": 8, "step": 0.5}], "kind": "elastic", "goal": {"k": "v1f", "value": 0, "tol": 0.01, "label": "Cart 1's final velocity"}},
   win="In an elastic head-on collision between equal masses, the carts swap velocities: cart 1 stops and cart 2 leaves at 5 m/s (Newton's cradle).",
   hints=["v₁ after = (m₁ − m₂) v₁ / (m₁ + m₂) when cart 2 starts at rest.", "That's zero when m₁ = m₂."]),
 M("col-3", "Where did the energy go?", "Cart 1 (4 kg, 5 m/s) hits a cart at rest and they stick. Choose the second mass so exactly 30 J of kinetic energy is lost.",
   {"type": "collide", "init": {"m1": 4, "v1": 5, "m2": 1, "v2": 0}, "sliders": [{"k": "m2", "min": 1, "max": 12, "step": 1}], "kind": "stick", "goal": {"k": "KElost", "value": 30, "tol": 0.3, "label": "KE lost"}},
   win="KE before = 50 J. Momentum 20 kg·m/s gives KE after = 20²/(2(4 + m₂)). Losing 30 J leaves 20 J, so 4 + m₂ = 10 and m₂ = 6 kg.",
   hints=["KE before = ½ × 4 × 5² = 50 J, so you want 20 J left afterwards.", "After sticking, KE = p²/(2M) with p = 20 kg·m/s."]),
]
G3 = [
 M("phys-calc", "Quick calculations", "Seven numbers to find. Type the answer (fractions like 3/4 are fine). Use g = 10 m/s².",
   {"type": "calc", "pass": 0.6, "qs": [
    {"q": "A ball is dropped from 45 m. How long until it hits the ground?", "a": 3, "unit": "s", "x": "h = ½gt² → t = √(2 × 45 / 10) = 3 s."},
    {"q": "A car starts from rest and accelerates at 4 m/s² for 5 s. How far does it go?", "a": 50, "unit": "m", "x": "x = ½at² = ½ × 4 × 25 = 50 m."},
    {"q": "A 5 kg box is pushed with 30 N against 10 N of friction. Acceleration?", "a": 4, "unit": "m/s²", "x": "Net force 20 N ÷ 5 kg = 4 m/s²."},
    {"q": "Kinetic energy of a 2 kg ball moving at 6 m/s?", "a": 36, "unit": "J", "x": "½ × 2 × 36 = 36 J."},
    {"q": "A ball is thrown straight up at 20 m/s. Maximum height?", "a": 20, "unit": "m", "x": "v² = 2gh → h = 400 / 20 = 20 m."},
    {"q": "A spring with k = 200 N/m is compressed 0.1 m. Stored energy?", "a": 1, "unit": "J", "x": "½kx² = ½ × 200 × 0.01 = 1 J."},
    {"q": "A 1500 kg car at 20 m/s brakes to a stop in 4 s. Average braking force (magnitude)?", "a": 7500, "unit": "N", "x": "Impulse: F = Δp/Δt = 30,000 / 4 = 7500 N."}]},
   win="Kinematics, Newton's laws, energy and impulse: the four tools behind every AP Physics 1 problem."),
 M("phys-sprint", "Concept sprint", "Eight conceptual questions against the clock. No calculator needed — think about the physics.",
   {"type": "sprint", "time": 240, "pass": 0.75, "qs": [
    {"q": "At the top of a projectile's path, its acceleration is…", "o": ["zero", "10 m/s² downward", "10 m/s² upward", "equal to its horizontal speed"], "a": 1, "x": "Gravity never switches off."},
    {"q": "A heavy truck and a small car collide head-on. Which feels the bigger force?", "o": ["the truck", "the car", "they feel equal forces", "it depends on speed"], "a": 2, "x": "Newton's third law: equal and opposite."},
    {"q": "An object moves at constant velocity. The net force on it is…", "o": ["zero", "in the direction of motion", "opposite to the motion", "equal to its weight"], "a": 0, "x": "Newton's first law."},
    {"q": "Doubling an object's speed multiplies its kinetic energy by…", "o": ["2", "4", "√2", "8"], "a": 1, "x": "KE ∝ v²."},
    {"q": "In a perfectly inelastic collision, what is always conserved (no external forces)?", "o": ["kinetic energy", "momentum", "both", "neither"], "a": 1, "x": "Momentum is conserved; kinetic energy is lost."},
    {"q": "A ball rolls off a table. Compared with a ball dropped at the same moment, it hits the floor…", "o": ["at the same time", "later", "earlier", "it depends on its speed"], "a": 0, "x": "Horizontal motion doesn't affect vertical fall."},
    {"q": "A satellite in a circular orbit moves at constant speed. Its acceleration is…", "o": ["zero", "toward the center", "along its velocity", "outward"], "a": 1, "x": "Centripetal acceleration points to the center."},
    {"q": "Friction does negative work on a sliding box. The box's mechanical energy…", "o": ["increases", "decreases", "stays the same", "becomes zero instantly"], "a": 1, "x": "It's turned into thermal energy."}]},
   win="Concepts first, then equations: most AP Physics 1 multiple-choice questions are decided by an idea, not a calculation."),
]
build_ws("ap-physics-1", "../../courses/ap-physics-1/workshop.html", "AP Physics 1", 'The <span class="hl">physics</span> workshop',
 "Launch projectiles at targets, smash carts together and race the clock. Predict with physics first and you'll hit it in one shot.",
 [("Projectiles", "Projectiles", G1), ("Collisions", "Collisions", G2), ("Predict and Solve", "Solve", G3)], (), "Margin · AP Physics 1 workshop · g = 10 m/s²", keep_sims=True)
