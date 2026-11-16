/* ===== AP Study — shared behaviour =====
   Every page sets <body data-root="..."> (relative path to the site root),
   and optionally data-course / data-unit to highlight the current unit.
   Unit pages put each chapter in <div class="chapter" id="..." data-title="...">.
   Quizzes: <div class="quiz" data-src="ID"></div> + <script type="application/json" id="ID">[...]</script>
   Question format: {"t":"tag","q":"question","o":["A","B",...],"a":indexOfCorrect,"x":"explanation"} */
(function () {
  const body = document.body;
  const root = body.dataset.root || "";
  const courses = window.SITE_COURSES || [];

  /* ---------- header with course dropdown ---------- */
  function buildHeader() {
    const header = document.createElement("header");
    header.className = "topbar";
    let menu = "";
    courses.forEach(c => {
      menu += `<div class="course">${c.name}</div>`;
      c.units.forEach(u => {
        const cur = c.id === body.dataset.course && u.id === body.dataset.unit;
        if (u.path && u.ready !== false) {
          menu += `<a href="${root}${u.path}"${cur ? ' class="current"' : ""}>${u.name}</a>`;
        } else {
          menu += `<span class="soon">${u.name}<em>${u.note ? "See Unit 3" : "Soon"}</em></span>`;
        }
      });
    });
    header.innerHTML = `
      <div class="in">
        <a class="brand" href="${root}index.html"><span class="dot"></span><span class="word">AP Study</span></a>
        <span class="spacer"></span>
        <div class="dd">
          <button class="navbtn" aria-expanded="false" aria-haspopup="true">Courses ▾</button>
          <div class="dd-menu" role="menu">${menu}</div>
        </div>
      </div>`;
    body.prepend(header);
    const btn = header.querySelector(".dd .navbtn"), dd = header.querySelector(".dd-menu");
    btn.addEventListener("click", e => {
      e.stopPropagation();
      const open = dd.classList.toggle("open");
      btn.setAttribute("aria-expanded", open);
    });
    document.addEventListener("click", e => {
      if (!dd.contains(e.target)) { dd.classList.remove("open"); btn.setAttribute("aria-expanded", "false"); }
    });
    document.addEventListener("keydown", e => { if (e.key === "Escape") { dd.classList.remove("open"); btn.setAttribute("aria-expanded", "false"); } });
    return header;
  }

  /* ---------- chapter menu (unit pages) ---------- */
  function buildChapters(header) {
    const chapters = [...document.querySelectorAll(".chapter")];
    if (!chapters.length) return;
    const bar = document.createElement("nav");
    bar.className = "chapterbar";
    bar.setAttribute("aria-label", "Chapters");
    const inner = document.createElement("div");
    inner.className = "in";
    bar.appendChild(inner);
    header.appendChild(bar);

    chapters.forEach((ch, i) => {
      const title = ch.dataset.title;
      // chapter heading + tools
      const head = document.createElement("div");
      head.className = "chapter-head";
      head.innerHTML = `<span class="num">${String(i + 1).padStart(2, "0")}</span><h2>${title}</h2>` +
        (ch.querySelector("details.deep") ? `<span class="tools"><button class="linkbtn" data-expand>Expand all deep explanations</button></span>` : "");
      ch.prepend(head);
      const exp = head.querySelector("[data-expand]");
      if (exp) exp.addEventListener("click", () => {
        const ds = ch.querySelectorAll("details.deep");
        const anyClosed = [...ds].some(d => !d.open);
        ds.forEach(d => (d.open = anyClosed));
        exp.textContent = anyClosed ? "Collapse all deep explanations" : "Expand all deep explanations";
      });
      // chip
      const chip = document.createElement("button");
      chip.className = "chip";
      chip.dataset.target = ch.id;
      chip.innerHTML = `<span class="n">${i + 1}</span>${ch.dataset.short || title}`;
      chip.addEventListener("click", () => go(ch.id, true));
      inner.appendChild(chip);
      // pager
      const pager = document.createElement("div");
      pager.className = "pager";
      const prev = chapters[i - 1], next = chapters[i + 1];
      if (prev) pager.innerHTML += `<button class="prev" data-go="${prev.id}"><small>← Previous</small>${prev.dataset.title}</button>`;
      if (next) pager.innerHTML += `<button class="next" data-go="${next.id}"><small>Next →</small>${next.dataset.title}</button>`;
      pager.querySelectorAll("button").forEach(b => b.addEventListener("click", () => go(b.dataset.go, true)));
      ch.appendChild(pager);
    });

    const all = document.createElement("button");
    all.className = "chip all";
    all.textContent = "Show all";
    all.addEventListener("click", () => {
      const on = body.classList.toggle("all-chapters");
      all.classList.toggle("on", on);
      all.textContent = on ? "One at a time" : "Show all";
    });
    inner.appendChild(all);

    function go(id, scroll) {
      const target = document.getElementById(id);
      if (!target) return;
      // allow linking to a topic inside a chapter
      const ch = target.classList.contains("chapter") ? target : target.closest(".chapter");
      if (!ch) return;
      chapters.forEach(c => c.classList.toggle("show", c === ch));
      inner.querySelectorAll(".chip[data-target]").forEach(c => {
        const on = c.dataset.target === ch.id;
        c.classList.toggle("on", on);
        if (on) inner.scrollTo({ left: c.offsetLeft - inner.clientWidth / 2 + c.offsetWidth / 2, behavior: scroll ? "smooth" : "auto" });
      });
      if ((scroll || location.hash) && location.hash.slice(1) !== id) history.replaceState(null, "", "#" + id);
      if (scroll) {
        const y = (target === ch ? document.querySelector(".page") : target).getBoundingClientRect().top + scrollY - header.offsetHeight - 10;
        window.scrollTo({ top: Math.max(0, y), behavior: "smooth" });
      }
    }
    // in-page links like <a href="#work"> switch chapters too
    document.addEventListener("click", e => {
      const a = e.target.closest('a[href^="#"]');
      if (!a) return;
      const id = a.getAttribute("href").slice(1);
      if (document.getElementById(id)) { e.preventDefault(); go(id, true); }
    });
    window.addEventListener("hashchange", () => go(location.hash.slice(1), true));
    const start = location.hash.slice(1);
    go(document.getElementById(start) ? start : chapters[0].id, false);
    if (!start) window.scrollTo(0, 0);
  }

  /* ---------- quizzes ---------- */
  function buildQuizzes() {
    document.querySelectorAll(".quiz[data-src]").forEach(box => {
      let Q;
      try { Q = JSON.parse(document.getElementById(box.dataset.src).textContent); } catch (e) { return; }
      const tags = box.dataset.tags ? JSON.parse(box.dataset.tags) : null; // {"e":"Energy","m":"Momentum"}
      const answered = {};
      let filter = "all";
      box.innerHTML = `
        ${tags ? `<div class="qfilter">${[["all", `All (${Q.length})`], ...Object.entries(tags)].map(([k, v], i) => `<button data-f="${k}"${i ? "" : ' class="on"'}>${v}</button>`).join("")}</div>` : ""}
        <div class="score"><span class="st"></span><div class="bar"><i></i></div><button class="btn reset">Reset</button></div>
        <div class="qs"></div>`;
      const qs = box.querySelector(".qs");
      const letter = j => String.fromCharCode(65 + j);
      function score() {
        const n = Object.keys(answered).length;
        const r = Object.entries(answered).filter(([i, j]) => Q[i].a === j).length;
        box.querySelector(".st").textContent = `${r} correct · ${n} of ${Q.length} answered`;
        box.querySelector(".bar i").style.width = (r / Q.length) * 100 + "%";
      }
      function paint(i, card) {
        const it = Q[i], j = answered[i];
        card.querySelectorAll(".opt").forEach((b, k) => {
          b.disabled = true;
          if (k === it.a) b.classList.add("right"); else if (k === j) b.classList.add("wrong");
        });
        const ex = card.querySelector(".expl");
        ex.innerHTML = (j === it.a ? '<b style="color:var(--good)">Correct.</b> ' : `<b style="color:var(--bad)">Incorrect.</b> The answer is ${letter(it.a)}. `) + it.x;
        ex.classList.add("show");
      }
      function render() {
        qs.innerHTML = "";
        Q.forEach((it, i) => {
          if (filter !== "all" && it.t !== filter) return;
          const card = document.createElement("div");
          card.className = "qcard";
          const tagName = tags && tags[it.t] ? `<span class="pill ${it.t}">${tags[it.t].toUpperCase()}</span>` : "";
          card.innerHTML = `<div class="qh"><span>Question ${i + 1}</span>${tagName}</div><div class="qt">${it.q}</div><div class="opts"></div><div class="expl"></div>`;
          it.o.forEach((o, j) => {
            const b = document.createElement("button");
            b.className = "opt";
            b.textContent = `${letter(j)}. ${o}`;
            b.addEventListener("click", () => { if (answered[i] !== undefined) return; answered[i] = j; paint(i, card); score(); });
            card.querySelector(".opts").appendChild(b);
          });
          qs.appendChild(card);
          if (answered[i] !== undefined) paint(i, card);
        });
      }
      box.querySelectorAll(".qfilter button").forEach(b => b.addEventListener("click", () => {
        box.querySelectorAll(".qfilter button").forEach(x => x.classList.remove("on"));
        b.classList.add("on"); filter = b.dataset.f; render();
      }));
      box.querySelector(".reset").addEventListener("click", () => { Object.keys(answered).forEach(k => delete answered[k]); score(); render(); });
      render(); score();
    });
  }

  /* ---------- home page course list ---------- */
  function buildCourseList() {
    const el = document.getElementById("course-list");
    if (!el) return;
    el.innerHTML = courses.map(c => `
      <div class="course-card">
        <h3>${c.name}</h3><p>${c.blurb || ""}</p>
        <div class="units">${c.units.map(u => u.path && u.ready !== false
          ? `<a href="${root}${u.path}">${u.name}</a>`
          : `<span>${u.name}<em>${u.note ? "See Unit 3" : "Coming soon"}</em></span>`).join("")}</div>
      </div>`).join("");
  }

  // add chevron to every deep-dive summary
  document.querySelectorAll("details.deep > summary").forEach(s => {
    if (!s.querySelector(".chev")) s.insertAdjacentHTML("beforeend", '<span class="chev" aria-hidden="true">▾</span>');
  });

  const header = buildHeader();
  buildChapters(header);
  buildQuizzes();
  buildCourseList();
})();
