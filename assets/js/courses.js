/* ===== Course registry =====
   To add a class or unit:
   1. Copy templates/unit-template.html into courses/<course-id>/<unit-id>.html
   2. Add an entry below. Leave out "path" (or set ready:false) to show it as "Coming soon".
   Paths are relative to the site root. */
window.SITE_COURSES = [
  {
    id: "ap-physics-1",
    name: "AP Physics 1",
    blurb: "Algebra-based mechanics: motion, forces, energy, momentum, rotation and fluids.",
    units: [
      { id: "unit-1", name: "Unit 1: Kinematics", path: "courses/ap-physics-1/unit-1.html", ready: true },
      { id: "unit-2", name: "Unit 2: Force and Translational Dynamics", path: "courses/ap-physics-1/unit-2.html", ready: true },
      { id: "unit-3", name: "Unit 3: Work, Energy & Power (+ Momentum)", path: "courses/ap-physics-1/unit-3.html", ready: true },
      { id: "unit-4", name: "Unit 4: Linear Momentum", note: "Covered in Unit 3 page for now" },
      { id: "unit-5", name: "Unit 5: Torque and Rotational Dynamics" },
      { id: "unit-6", name: "Unit 6: Energy and Momentum of Rotating Systems" },
      { id: "unit-7", name: "Unit 7: Oscillations" },
      { id: "unit-8", name: "Unit 8: Fluids" }
    ]
  }
  // Example for later:
  // { id: "ap-chemistry", name: "AP Chemistry", blurb: "...", units: [ { id: "unit-1", name: "Unit 1: Atomic Structure" } ] }
];
