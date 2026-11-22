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
      { id: "unit-4", name: "Unit 4: Linear Momentum", path: "courses/ap-physics-1/unit-4.html", ready: true },
      { id: "unit-5", name: "Unit 5: Torque and Rotational Dynamics" },
      { id: "unit-6", name: "Unit 6: Energy and Momentum of Rotating Systems" },
      { id: "unit-7", name: "Unit 7: Oscillations" },
      { id: "unit-8", name: "Unit 8: Fluids" }
    ]
  },
  {
    id: "ap-csa",
    name: "AP Computer Science A",
    blurb: "Java: objects and methods, selection and iteration, writing classes, and data collections.",
    units: [
      { id: "unit-1", name: "Unit 1: Using Objects and Methods", path: "courses/ap-csa/unit-1.html", ready: true },
      { id: "unit-2", name: "Unit 2: Selection and Iteration", path: "courses/ap-csa/unit-2.html", ready: true },
      { id: "unit-3", name: "Unit 3: Class Creation", path: "courses/ap-csa/unit-3.html", ready: true },
      { id: "unit-4", name: "Unit 4: Data Collections" }
    ]
  },
  {
    id: "french-1",
    name: "French 1",
    blurb: "French from zero: greetings, describing people, everyday life, and talking about the past and future.",
    units: [
      { id: "unit-1", name: "Unit 1: Bonjour ! The basics", path: "courses/french-1/unit-1.html", ready: true },
      { id: "unit-2", name: "Unit 2: People and things", path: "courses/french-1/unit-2.html", ready: true },
      { id: "unit-3", name: "Unit 3: Verbs in the present", path: "courses/french-1/unit-3.html", ready: true },
      { id: "unit-4", name: "Unit 4: Everyday life", path: "courses/french-1/unit-4.html", ready: true },
      { id: "unit-5", name: "Unit 5: Past and future", path: "courses/french-1/unit-5.html", ready: true },
      { id: "unit-6", name: "Unit 6: At home", path: "courses/french-1/unit-6.html", ready: true },
      { id: "unit-7", name: "Unit 7: Clothes and shopping", path: "courses/french-1/unit-7.html", ready: true },
      { id: "unit-8", name: "Unit 8: Travel", path: "courses/french-1/unit-8.html", ready: true },
      { id: "vocab", name: "Word bank: 1,000 common words", path: "courses/french-1/vocab.html", ready: true }
    ]
  }
  // Example for later:
  // { id: "ap-chemistry", name: "AP Chemistry", blurb: "...", units: [ { id: "unit-1", name: "Unit 1: Atomic Structure" } ] }
];
