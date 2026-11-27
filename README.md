# Margin

*Reach your highest point.*

Free AP review pages: explanations, detailed explanations of each idea, worked examples, and self-checking practice questions.

## Current content

- AP Physics 1, AP Computer Science A, French, AP Precalculus, SAT and ACT
- **Intro to Computer Engineering** (6 units) — `courses/comp-eng/`
- **Machine Learning** (6 units) — `courses/ml/`

## Structure

```
index.html                     Home page (course list is built from courses.js)
assets/css/site.css            Shared styles
assets/js/courses.js           Course registry: every course and unit
assets/js/site.js              Header, course menu, chapter menu, quizzes, site animations
assets/js/sims.js              2D animated physics examples (add new types here)
assets/js/exam.js              Timed practice exam engine (MCQ + FRQ with rubric)
assets/js/labs.js              Interactive labs for computer engineering and machine learning
courses/<course>/<unit>.html   One page per unit
templates/unit-template.html   Starting point for new units
```

## Adding a course or unit

1. Copy `templates/unit-template.html` to `courses/<course-id>/<unit-id>.html`.
2. Fill in the chapters, topics, detailed explanations and quiz questions (the template has comments).
3. Add the course/unit to `assets/js/courses.js` with its `path` and `ready: true`.

Animated examples: add `<div class="sim" data-sim='{"type":"collide",...}'></div>` to a page, or a `"sim"` object to a quiz question. Available types are listed in `assets/js/sims.js`.

Practice exams: add `<div class="exam" data-src="ID"></div>` plus a JSON block (format documented at the top of `assets/js/exam.js`).

The course menu, home page list, chapter buttons, previous/next buttons and quizzes are generated automatically.

## Hosting

Served with GitHub Pages from the `main` branch root.

## License

MIT, see `LICENSE`.
