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
      { id: "unit-5", name: "Unit 5: Torque and Rotational Dynamics", path: "courses/ap-physics-1/unit-5.html", ready: true },
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
    name: "French",
    blurb: "From your first bonjour to college-level grammar: the basics, then the subjunctive, si clauses and essay writing.",
    units: [
      { id: "unit-1", group: "Level 1 · The basics", name: "Unit 1: Bonjour ! The basics", path: "courses/french-1/unit-1.html", ready: true },
      { id: "unit-2", group: "Level 1 · The basics", name: "Unit 2: People and things", path: "courses/french-1/unit-2.html", ready: true },
      { id: "unit-3", group: "Level 1 · The basics", name: "Unit 3: Verbs in the present", path: "courses/french-1/unit-3.html", ready: true },
      { id: "unit-4", group: "Level 1 · The basics", name: "Unit 4: Everyday life", path: "courses/french-1/unit-4.html", ready: true },
      { id: "unit-5", group: "Level 1 · The basics", name: "Unit 5: Past and future", path: "courses/french-1/unit-5.html", ready: true },
      { id: "unit-6", group: "Level 1 · The basics", name: "Unit 6: At home", path: "courses/french-1/unit-6.html", ready: true },
      { id: "unit-7", group: "Level 1 · The basics", name: "Unit 7: Clothes and shopping", path: "courses/french-1/unit-7.html", ready: true },
      { id: "unit-8", group: "Level 1 · The basics", name: "Unit 8: Travel", path: "courses/french-1/unit-8.html", ready: true },
      { id: "vocab", group: "Level 1 · The basics", name: "Word bank: 1,000 common words", path: "courses/french-1/vocab.html", ready: true },
      { id: "college-1", group: "Level 2 · College French", name: "Unit 1: Le passé", path: "courses/french-1/college-1.html", ready: true },
      { id: "college-2", group: "Level 2 · College French", name: "Unit 2: Les pronoms", path: "courses/french-1/college-2.html", ready: true },
      { id: "college-3", group: "Level 2 · College French", name: "Unit 3: Futur et conditionnel", path: "courses/french-1/college-3.html", ready: true },
      { id: "college-4", group: "Level 2 · College French", name: "Unit 4: Le subjonctif", path: "courses/french-1/college-4.html", ready: true },
      { id: "college-5", group: "Level 2 · College French", name: "Unit 5: Le style", path: "courses/french-1/college-5.html", ready: true }
    ]
  },
  {
    id: "math",
    name: "Math: AP Precalculus",
    blurb: "The algebra you need first, then AP Precalculus: polynomials, exponentials and logs, trig and polar.",
    units: [
      { id: "pre-1", group: "Before Precalc · What to know first", name: "Unit 1: Algebra toolkit", path: "courses/math/pre-1.html", ready: true },
      { id: "pre-2", group: "Before Precalc · What to know first", name: "Unit 2: Linear equations and lines", path: "courses/math/pre-2.html", ready: true },
      { id: "pre-3", group: "Before Precalc · What to know first", name: "Unit 3: Quadratics", path: "courses/math/pre-3.html", ready: true },
      { id: "pre-4", group: "Before Precalc · What to know first", name: "Unit 4: Functions", path: "courses/math/pre-4.html", ready: true },
      { id: "pre-5", group: "Before Precalc · What to know first", name: "Unit 5: Geometry and right-triangle trig", path: "courses/math/pre-5.html", ready: true },
      { id: "precalc-1", group: "AP Precalculus", name: "Unit 1: Polynomial and Rational Functions", path: "courses/math/precalc-1.html", ready: true },
      { id: "precalc-2", group: "AP Precalculus", name: "Unit 2: Exponential and Logarithmic Functions", path: "courses/math/precalc-2.html", ready: true },
      { id: "precalc-3", group: "AP Precalculus", name: "Unit 3: Trigonometric and Polar Functions", path: "courses/math/precalc-3.html", ready: true },
      { id: "precalc-4", group: "AP Precalculus", name: "Unit 4: Functions with Parameters, Vectors and Matrices" }
    ]
  }
  // Example for later:
  // { id: "ap-chemistry", name: "AP Chemistry", blurb: "...", units: [ { id: "unit-1", name: "Unit 1: Atomic Structure" } ] }
];
