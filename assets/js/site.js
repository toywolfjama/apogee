/* ===== Apogee — shared behaviour =====
   Every page sets <body data-root="..."> (relative path to the site root),
   and optionally data-course / data-unit to highlight the current unit.
   Unit pages put each chapter in <div class="chapter" id="..." data-title="...">.
   Quizzes: <div class="quiz" data-src="ID"></div> + <script type="application/json" id="ID">[...]</script>
   Question format: {"t":"tag","q":"question","o":["A","B",...],"a":indexOfCorrect,"x":"explanation"} */
(function () {
  const body = document.body;
  const root = body.dataset.root || "";

  /* ---------- settings (saved in this browser) ---------- */
  const DEFAULTS = { models: true, motion: true, big: false };
  let settings = Object.assign({}, DEFAULTS);
  try { Object.assign(settings, JSON.parse(localStorage.getItem("apogee-settings") || "{}")); } catch (e) {}
  function applySettings() {
    body.classList.toggle("no-models", !settings.models);
    body.classList.toggle("no-motion", !settings.motion);
    body.classList.toggle("big-text", !!settings.big);
    try { localStorage.setItem("apogee-settings", JSON.stringify(settings)); } catch (e) {}
    document.dispatchEvent(new CustomEvent("chapterchange"));
  }
  applySettings();
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
        <a class="brand" href="${root}index.html"><span class="dot"></span><span class="word">Apogee</span></a>
        <span class="spacer"></span>
        <div class="dd dd-settings">
          <button class="navbtn icon" aria-expanded="false" aria-haspopup="true" aria-label="Settings" title="Settings">⚙<span class="lbl"> Settings</span></button>
          <div class="dd-menu settings-menu" role="menu">
            <div class="course">Settings</div>
            <label class="set-row"><span><b>Animated models</b><small>Turn off to practice like a real exam</small></span><input type="checkbox" data-set="models"><i class="sw"></i></label>
            <label class="set-row"><span><b>Background &amp; motion effects</b><small>Starfield, fades and transitions</small></span><input type="checkbox" data-set="motion"><i class="sw"></i></label>
            <label class="set-row"><span><b>Larger text</b><small>Easier reading on small screens</small></span><input type="checkbox" data-set="big"><i class="sw"></i></label>
          </div>
        </div>
        <div class="dd">
          <button class="navbtn" aria-expanded="false" aria-haspopup="true">Courses ▾</button>
          <div class="dd-menu" role="menu">${menu}</div>
        </div>
      </div>`;
    body.prepend(header);
    const menus = [...header.querySelectorAll(".dd")].map(d => ({ btn: d.querySelector(".navbtn"), dd: d.querySelector(".dd-menu") }));
    const closeAll = except => menus.forEach(m => { if (m !== except) { m.dd.classList.remove("open"); m.btn.setAttribute("aria-expanded", "false"); } });
    menus.forEach(m => m.btn.addEventListener("click", e => {
      e.stopPropagation(); closeAll(m);
      const open = m.dd.classList.toggle("open");
      m.btn.setAttribute("aria-expanded", open);
    }));
    document.addEventListener("click", e => { if (!e.target.closest(".dd")) closeAll(); });
    document.addEventListener("keydown", e => { if (e.key === "Escape") closeAll(); });
    header.querySelectorAll("[data-set]").forEach(cb => {
      cb.checked = !!settings[cb.dataset.set];
      cb.addEventListener("change", () => { settings[cb.dataset.set] = cb.checked; applySettings(); });
    });
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
      chip.className = "chip" + (ch.dataset.hard ? " hard" : "");
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
      document.dispatchEvent(new CustomEvent("chapterchange", { detail: ch.id }));
      requestAnimationFrame(() => revealIn(ch));
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
        if (card._sim) card._sim.reveal();
      }
      function render() {
        qs.innerHTML = "";
        Q.forEach((it, i) => {
          if (filter !== "all" && it.t !== filter) return;
          const card = document.createElement("div");
          card.className = "qcard";
          const tagName = tags && tags[it.t] ? `<span class="pill ${it.t}">${tags[it.t].toUpperCase()}</span>` : "";
          card.innerHTML = `<div class="qh"><span>Question ${i + 1}</span>${tagName}</div><div class="qt">${it.q}</div>${it.sim ? '<div class="qsim"></div>' : ""}<div class="opts"></div><div class="expl"></div>`;
          if (it.sim && window.Sims) card._sim = window.Sims.mount(card.querySelector(".qsim"), it.sim);
          it.o.forEach((o, j) => {
            const b = document.createElement("button");
            b.className = "opt";
            b.textContent = `${letter(j)}. ${o}`;
            b.addEventListener("click", () => {
              if (answered[i] !== undefined) return;
              answered[i] = j; paint(i, card); score();
              card.classList.add(j === it.a ? "got-it" : "missed");
            });
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

  /* ---------- motion ---------- */
  const reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
  let io = null;
  if (!reduce && settings.motion && "IntersectionObserver" in window) {
    io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }), { threshold: 0, rootMargin: "0px 0px -30px 0px" });
  }
  function revealIn(scope) {
    if (!io) return;
    scope.querySelectorAll(".topic, .course-card, .qcard").forEach((el, k) => {
      if (el.classList.contains("in")) return;
      el.classList.add("rv");
      el.style.transitionDelay = Math.min(k, 4) * 60 + "ms";
      io.observe(el);
    });
  }
  // smooth open/close for deep explanations
  document.querySelectorAll("details.deep").forEach(d => {
    const sum = d.querySelector("summary"), body = d.querySelector(".deep-body");
    if (reduce || !body) return;
    sum.addEventListener("click", e => {
      e.preventDefault();
      if (d.dataset.anim) return;
      d.dataset.anim = 1;
      if (!d.open) {
        d.open = true;
        const h = body.scrollHeight;
        body.animate([{ height: "0px", opacity: 0 }, { height: h + "px", opacity: 1 }], { duration: 320, easing: "cubic-bezier(.2,.7,.2,1)" }).onfinish = () => delete d.dataset.anim;
      } else {
        const h = body.scrollHeight;
        body.animate([{ height: h + "px", opacity: 1 }, { height: "0px", opacity: 0 }], { duration: 240, easing: "ease-in" }).onfinish = () => { d.open = false; delete d.dataset.anim; };
      }
    });
  });
  // starfield background
  function starfield() {
    const cv = document.createElement("canvas");
    cv.className = "stars"; cv.setAttribute("aria-hidden", "true");
    body.prepend(cv);
    const c = cv.getContext("2d");
    let stars = [], w, h, dpr;
    function init() {
      dpr = Math.min(2, devicePixelRatio || 1); w = innerWidth; h = innerHeight;
      cv.width = w * dpr; cv.height = h * dpr; c.setTransform(dpr, 0, 0, dpr, 0, 0);
      const n = Math.round((w * h) / 5200);
      stars = Array.from({ length: n }, () => ({ x: Math.random() * w, y: Math.random() * h, r: Math.random() * 1.3 + 0.2, s: Math.random() * 0.25 + 0.03, p: Math.random() * 6.28, z: Math.random() }));
    }
    let shoot = null, lastShoot = 0;
    function frame(now) {
      const still = body.classList.contains("no-motion");
      if (still && frame.drawn) { requestAnimationFrame(frame); return; }
      frame.drawn = still;
      c.clearRect(0, 0, w, h);
      const par = still ? 0 : scrollY * 0.04;
      for (const st of stars) {
        if (!reduce && !still) { st.x -= st.s * 0.25; if (st.x < -2) st.x = w + 2; }
        const a = still ? 0.6 : 0.35 + 0.55 * (0.5 + 0.5 * Math.sin(now / 900 * (0.5 + st.z) + st.p));
        c.globalAlpha = a; c.fillStyle = st.z > 0.85 ? "#eafe07" : st.z > 0.7 ? "#9fd0ff" : "#ffffff";
        c.beginPath(); c.arc(st.x, (st.y - par * st.z + h) % h, st.r, 0, 7); c.fill();
      }
      if (!reduce && !still) {
        if (!shoot && now - lastShoot > 7000 && Math.random() < 0.01) { shoot = { x: Math.random() * w * 0.7 + w * 0.3, y: Math.random() * h * 0.4, t: 0 }; lastShoot = now; }
        if (shoot) {
          shoot.t += 0.025; const k = shoot.t, x = shoot.x - k * 260, y = shoot.y + k * 120;
          const g = c.createLinearGradient(x, y, x + 90, y - 42); g.addColorStop(0, "rgba(255,255,255,.9)"); g.addColorStop(1, "rgba(255,255,255,0)");
          c.globalAlpha = 1 - k; c.strokeStyle = g; c.lineWidth = 1.6; c.beginPath(); c.moveTo(x, y); c.lineTo(x + 90, y - 42); c.stroke();
          if (k >= 1) shoot = null;
        }
      }
      c.globalAlpha = 1;
      if (!reduce) requestAnimationFrame(frame);
    }
    init(); addEventListener("resize", () => { init(); frame.drawn = false; }); requestAnimationFrame(frame);
  }
  starfield();

  // add chevron to every deep-dive summary
  document.querySelectorAll("details.deep > summary").forEach(s => {
    if (!s.querySelector(".chev")) s.insertAdjacentHTML("beforeend", '<span class="chev" aria-hidden="true">▾</span>');
  });

  const header = buildHeader();
  buildChapters(header);
  buildQuizzes();
  buildCourseList();
  if (window.Sims) window.Sims.mountAll();
  // reveal problem-set animations when their solution is opened
  document.querySelectorAll(".qcard details.reveal").forEach(d => d.addEventListener("toggle", () => {
    if (!d.open) return;
    d.closest(".qcard").querySelectorAll(".sim").forEach(el => el._ctl && el._ctl.reveal());
  }));
  revealIn(document);
  // quiz cards are re-rendered on filter changes
  document.querySelectorAll(".quiz").forEach(q => new MutationObserver(() => revealIn(q)).observe(q, { childList: true, subtree: true }));
})();
