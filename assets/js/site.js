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
  const DEFAULTS = { models: true, motion: true, big: false, timer: true };
  let settings = Object.assign({}, DEFAULTS);
  function applySettings() {
    body.classList.toggle("no-models", !settings.models);
    body.classList.toggle("no-motion", !settings.motion);
    body.classList.toggle("big-text", !!settings.big);
    body.classList.toggle("no-timer", !settings.timer);
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
        <a class="brand" href="${root}index.html"><span class="planet" aria-hidden="true"><i></i><b></b></span><span class="mark" aria-hidden="true"><i></i><i></i></span><span class="tt"><span class="u">student@apogee</span><span class="d">:</span><span class="p" id="tt-path">~/${termPath()}</span><span class="d">$</span></span><span class="word">Apogee</span></a>
        <span class="spacer"></span>
        <div class="dd">
          <button class="navbtn" aria-expanded="false" aria-haspopup="true">Courses ▾</button>
          <div class="dd-menu" role="menu">${menu}</div>
        </div>
        <span class="win" aria-hidden="true"><i>–</i><i>□</i><i>×</i></span>
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
        (ch.querySelector("details.deep") ? `<span class="tools"><button class="linkbtn" data-expand>Expand all detailed explanations</button></span>` : "");
      ch.prepend(head);
      const exp = head.querySelector("[data-expand]");
      if (exp) exp.addEventListener("click", () => {
        const ds = ch.querySelectorAll("details.deep");
        const anyClosed = [...ds].some(d => !d.open);
        ds.forEach(d => (d.open = anyClosed));
        exp.textContent = anyClosed ? "Collapse all detailed explanations" : "Expand all detailed explanations";
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
      const tp = document.getElementById("tt-path"), cur = inner.querySelector(".chip.on");
      if (tp) tp.textContent = "~/" + termPath() + (on || !cur ? "" : "/" + chSlug(cur.dataset.target));
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
            if (it.h) b.innerHTML = `${letter(j)}. ${o}`; else b.textContent = `${letter(j)}. ${o}`;
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
  // smooth open/close for detailed explanations
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


  // add chevron to every deep-dive summary
  document.querySelectorAll("details.deep > summary").forEach(s => {
    if (!s.querySelector(".chev")) s.insertAdjacentHTML("beforeend", '<span class="chev" aria-hidden="true">▾</span>');
  });

  const header = buildHeader();
  buildChapters(header);

  /* ---------- theme decorations ---------- */
  function termPath() {
    const c = body.dataset.course || "", u = body.dataset.unit || "";
    return [c, u].filter(Boolean).join("/");
  }
  let warpAt = -1;
  function chSlug(id) {
    const ch = id && document.getElementById(id);
    const name = ch ? (ch.dataset.short || ch.dataset.title || id) : "";
    return name.toLowerCase().replace(/&/g, " ").replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
  }
  document.addEventListener("chapterchange", ev => {
    const el = document.getElementById("tt-path"); if (!el || !ev.detail) return;
    if (body.classList.contains("all-chapters")) { el.textContent = "~/" + termPath(); return; }
    el.textContent = "~/" + termPath() + "/" + chSlug(ev.detail);
  });
  { const el = document.getElementById("tt-path"), cur = document.querySelector(".chapterbar .chip.on[data-target]");
    if (el && cur && !body.classList.contains("all-chapters")) el.textContent = "~/" + termPath() + "/" + chSlug(cur.dataset.target); }
  function spaceStars() {
    if (!body.classList.contains("th-space")) return;
    const cv = document.createElement("canvas"); cv.className = "stars"; cv.setAttribute("aria-hidden", "true");
    body.prepend(cv);
    const c = cv.getContext("2d");
    let w, h, dpr, stars = [], shoot = null, last = 0;
    function resize() {
      dpr = Math.min(2, window.devicePixelRatio || 1); w = innerWidth; h = innerHeight;
      cv.width = w * dpr; cv.height = h * dpr; c.setTransform(dpr, 0, 0, dpr, 0, 0);
      const n = Math.round((w * h) / 2600);
      stars = Array.from({ length: n }, () => ({ x: Math.random() * w, y: Math.random() * h, z: Math.random(), r: Math.random() * 1.2 + 0.25, p: Math.random() * 6.28, warm: Math.random() < 0.12 }));
    }
    function frame(t) {
      const still = body.classList.contains("no-motion") || matchMedia("(prefers-reduced-motion: reduce)").matches;
      c.clearRect(0, 0, w, h);
      const sy = scrollY;
      const wk = still || warpAt < 0 ? 1 : (t - warpAt) / 900;
      const wi = wk < 1 ? Math.sin(Math.PI * wk) : 0;
      if (wi > 0) {
        c.lineCap = "round";
        for (const s of stars) {
          const y = (((s.y - sy * (0.04 + s.z * 0.12)) % h) + h) % h;
          const dx = s.x - w / 2, dy = y - h / 2, L = wi * (0.08 + s.z * 0.3);
          c.globalAlpha = 0.5 + s.z * 0.5; c.strokeStyle = s.warm ? "#FFE2B0" : "#DCE6FF"; c.lineWidth = s.r * (0.8 + s.z);
          c.beginPath(); c.moveTo(s.x, y); c.lineTo(s.x + dx * L, y + dy * L); c.stroke();
        }
        c.globalAlpha = 1; requestAnimationFrame(frame); return;
      }
      for (const s of stars) {
        const y = (((s.y - sy * (0.04 + s.z * 0.12)) % h) + h) % h;
        const a = 0.35 + 0.65 * (still ? 0.8 : 0.5 + 0.5 * Math.sin(t / 900 + s.p * 3));
        c.globalAlpha = a * (0.4 + s.z * 0.6);
        c.fillStyle = s.warm ? "#FFE2B0" : "#DCE6FF";
        c.beginPath(); c.arc(s.x, y, s.r * (0.6 + s.z * 0.7), 0, 6.283); c.fill();
      }
      if (!still) {
        if (!shoot && t - last > 6000 + Math.random() * 6000) { last = t; shoot = { x: Math.random() * w * 0.7 + w * 0.2, y: Math.random() * h * 0.35, t: 0 }; }
        if (shoot) {
          shoot.t += 16; const k = shoot.t / 700, x = shoot.x - k * 260, y = shoot.y + k * 120;
          const g = c.createLinearGradient(x, y, x + 90, y - 42); g.addColorStop(0, "rgba(255,255,255,.9)"); g.addColorStop(1, "rgba(255,255,255,0)");
          c.globalAlpha = Math.max(0, 1 - k); c.strokeStyle = g; c.lineWidth = 1.6; c.beginPath(); c.moveTo(x, y); c.lineTo(x + 90, y - 42); c.stroke();
          if (k >= 1) shoot = null;
        }
      }
      c.globalAlpha = 1;
      requestAnimationFrame(frame);
    }
    addEventListener("resize", resize); resize(); requestAnimationFrame(frame);
  }
  function spaceHero() {
    const hero = document.querySelector("body.th-space .hero");
    if (!hero || hero.querySelector(".orbit-art")) return;
    const art = document.createElement("div"); art.className = "orbit-art"; art.setAttribute("aria-hidden", "true");
    art.innerHTML = `<svg viewBox="0 0 380 380">
      <defs>
        <radialGradient id="pl" cx="34%" cy="30%" r="75%"><stop offset="0" stop-color="#FFE7B0"/><stop offset=".35" stop-color="#FFB347"/><stop offset=".7" stop-color="#B4501E"/><stop offset="1" stop-color="#2A0E04"/></radialGradient>
        <radialGradient id="glow" cx="50%" cy="50%" r="50%"><stop offset=".55" stop-color="rgba(255,180,80,.35)"/><stop offset="1" stop-color="rgba(255,180,80,0)"/></radialGradient>
        <radialGradient id="mn" cx="35%" cy="30%" r="70%"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#8FA3C8"/></radialGradient>
      </defs>
      <circle cx="190" cy="190" r="150" fill="url(#glow)"/>
      <g fill="none" stroke="rgba(124,196,255,.22)" stroke-dasharray="2 6"><ellipse cx="190" cy="190" rx="176" ry="62" transform="rotate(-18 190 190)"/><ellipse cx="190" cy="190" rx="140" ry="140"/></g>
      <circle cx="190" cy="190" r="86" fill="url(#pl)"/>
      <path d="M118 176c40 10 104 10 144-2M114 204c46 12 108 10 152-4" stroke="rgba(60,20,5,.35)" stroke-width="7" fill="none" stroke-linecap="round"/>
      <ellipse cx="190" cy="190" rx="132" ry="30" fill="none" stroke="rgba(255,226,170,.55)" stroke-width="3" transform="rotate(-18 190 190)"/>
      <g class="sat"><circle r="9" fill="url(#mn)"/><animateMotion dur="11s" repeatCount="indefinite" path="M366 190a176 62 0 1 1-352 0a176 62 0 1 1 352 0" rotate="0"/></g>
      <g transform="rotate(-18 190 190)"></g>
      <g font-family="JetBrains Mono, monospace" font-size="10" fill="#A3B0D0" letter-spacing="1.5">
        <text x="250" y="52">APOGEE</text><line x1="248" y1="56" x2="230" y2="80" stroke="#FFC857" stroke-width="1"/>
        <text x="18" y="338">PERIGEE</text><line x1="72" y1="328" x2="96" y2="300" stroke="#FFC857" stroke-width="1"/>
      </g></svg>`;
    // the moon follows the tilted orbit
    art.querySelector("animateMotion").setAttribute("path", "M366 190a176 62 0 1 1-352 0a176 62 0 1 1 352 0");
    art.querySelector(".sat").setAttribute("transform", "rotate(-18 190 190)");
    hero.appendChild(art);
  }
  function termDecor() {
    if (!body.classList.contains("th-term")) return;
    const path = "~/" + termPath();
    const ps = (p, cmd) => `<span class="pr"><span class="u">student@apogee</span>:<span class="p">${p}</span>$</span> <span class="c">${cmd}</span>`;
    const hero = document.querySelector(".hero");
    if (hero && !hero.querySelector(".cmd")) {
      const d = document.createElement("div"); d.className = "cmd"; d.innerHTML = ps("~", `cd ${termPath()} && cat README.md`);
      hero.prepend(d);
    }
    document.querySelectorAll("section.topic").forEach(sec => {
      if (sec.querySelector(":scope > .ps1")) return;
      const id = sec.id || "notes";
      const d = document.createElement("div"); d.className = "ps1";
      d.innerHTML = ps(path, `cat ${id}.md`) + '<span class="dots" aria-hidden="true"><i></i><i></i><i></i></span>';
      sec.prepend(d);
    });
  }

  // ---------- click animations ----------
  function fx() {
    const still = () => body.classList.contains("no-motion") || matchMedia("(prefers-reduced-motion: reduce)").matches;
    const SPACE = body.classList.contains("th-space"), TERM = body.classList.contains("th-term");
    const isTermEl = el => TERM || !!el.closest(".portal.term");

    function burst(x, y, big) {
      const d = document.createElement("div"); d.className = "fx-burst" + (big ? " big" : "");
      d.style.left = x + "px"; d.style.top = y + "px";
      let h = "<i></i>";
      const n = big ? 12 : 8;
      for (let k = 0; k < n; k++) h += `<b style="--a:${(360 / n) * k + Math.random() * 20}deg;--d:${(big ? 46 : 28) + Math.random() * 18}px"></b>`;
      d.innerHTML = h; body.appendChild(d); setTimeout(() => d.remove(), 800);
    }
    function invert(el) {
      el.classList.remove("fx-inv"); void el.offsetWidth; el.classList.add("fx-inv");
      setTimeout(() => el.classList.remove("fx-inv"), 420);
    }
    document.addEventListener("pointerdown", e => {
      if (still() || e.button > 0) return;
      const el = e.target.closest("button, a, summary, .chip, label.toggle");
      if (!el) return;
      if (isTermEl(el)) invert(el); else burst(e.clientX, e.clientY);
    });

    // chapter switch
    let lastAct = 0;
    ["pointerdown", "keydown"].forEach(t => document.addEventListener(t, () => lastAct = performance.now(), true));
    document.addEventListener("chapterchange", ev => {
      if (performance.now() - lastAct > 1500) return;
      if (still()) return;
      const ch = document.getElementById(ev.detail); if (!ch) return;
      const cls = TERM ? "fx-tty-in" : "fx-warp-in";
      ch.classList.remove(cls); void ch.offsetWidth; ch.classList.add(cls);
      setTimeout(() => ch.classList.remove(cls), 900);
      if (SPACE) warpAt = performance.now();
      if (TERM) {
        const line = document.createElement("div"); line.className = "fx-cdline";
        line.innerHTML = `<span class="u">student@apogee</span>:<span class="p">~/${termPath()}</span>$ <span class="t"></span>`;
        ch.prepend(line);
        const txt = "cd " + chSlug(ev.detail), t = line.querySelector(".t");
        let k = 0; (function type() { t.textContent = txt.slice(0, ++k); if (k < txt.length) setTimeout(type, 14); })();
        setTimeout(() => line.classList.add("out"), 900); setTimeout(() => line.remove(), 1300);
      }
    });

    // right answers get a burst
    document.addEventListener("click", e => {
      const b = e.target.closest(".opt"); if (!b || still()) return;
      setTimeout(() => {
        if (!b.classList.contains("right")) return;
        const r = b.getBoundingClientRect();
        if (!isTermEl(b)) burst(r.left + r.width / 2, r.top + r.height / 2, true);
      }, 30);
    });

    // page-to-page transitions
    function styleFor(href) {
      if (/ap-csa/.test(href)) return "term";
      if (/ap-physics|calculator/.test(href)) return "space";
      return TERM ? "term" : "space";
    }
    document.addEventListener("click", e => {
      const a = e.target.closest("a[href]");
      if (!a || e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
      if (a.target && a.target !== "_self") return;
      if (a.hasAttribute("download")) return;
      const url = new URL(a.href, location.href);
      if (url.origin !== location.origin) return;
      if (url.pathname === location.pathname) return;
      if (!/\.html?$|\/$/.test(url.pathname)) return;
      if (still()) return;
      e.preventDefault();
      const st = styleFor(url.pathname);
      try { sessionStorage.setItem("fx-arrive", st); } catch (er) {}
      (st === "term" ? ttyOut : warpOut)(url, a);
    });
    function warpOut(url) {
      const o = document.createElement("div"); o.className = "fx-warp"; o.innerHTML = "<canvas></canvas>";
      body.appendChild(o);
      const cv = o.firstChild, c = cv.getContext("2d"), W = innerWidth, H = innerHeight, dpr = Math.min(2, devicePixelRatio || 1);
      cv.width = W * dpr; cv.height = H * dpr; c.setTransform(dpr, 0, 0, dpr, 0, 0);
      const P = Array.from({ length: 480 }, () => { const a = Math.random() * 6.283, r = Math.sqrt(Math.random()) * 0.75 + 0.03; return { a, r, z: Math.random() }; });
      const t0 = performance.now();
      (function f(t) {
        const k = Math.min(1, (t - t0) / 650), sp = k * k;
        c.fillStyle = `rgba(5,8,22,${0.35 + 0.4 * k})`; c.fillRect(0, 0, W, H);
        const gl = c.createRadialGradient(W / 2, H / 2, 0, W / 2, H / 2, Math.max(W, H) * (0.15 + 0.35 * sp));
        gl.addColorStop(0, `rgba(180,210,255,${0.35 * sp})`); gl.addColorStop(1, "rgba(5,8,22,0)"); c.fillStyle = gl; c.fillRect(0, 0, W, H);
        c.lineCap = "round";
        for (const p of P) {
          const base = Math.hypot(W, H) / 2 * p.r * 1.3, r0 = base * (1 + 0.5 * sp), R = base * (1 + (0.15 + 3 * p.z) * sp);
          const x0 = W / 2 + Math.cos(p.a) * r0, y0 = H / 2 + Math.sin(p.a) * r0, x1 = W / 2 + Math.cos(p.a) * R, y1 = H / 2 + Math.sin(p.a) * R;
          c.strokeStyle = p.z > 0.85 ? "#FFE2B0" : "#CFE0FF"; c.globalAlpha = 0.55 + 0.45 * k; c.lineWidth = 0.8 + p.z * 2.2;
          c.beginPath(); c.moveTo(x0, y0); c.lineTo(x1, y1); c.stroke();
        }
        c.globalAlpha = 1;
        if (k < 1) requestAnimationFrame(f); else { o.classList.add("flash"); setTimeout(() => location.href = url.href, 120); }
      })(t0);
    }
    function ttyOut(url) {
      const o = document.createElement("div"); o.className = "fx-tty";
      const path = url.pathname.replace(/^.*?(ap-csa|ap-physics-1)\//, "$1/").replace(/\.html$/, "").replace(/^\/.*\/(index)?$/, "");
      const lines = [["cmd", `cd ~/${path || ""}`], ["cmd", "cat README.md"], ["out", "loading..."]];
      o.innerHTML = '<pre></pre>'; body.appendChild(o);
      const pre = o.firstChild; let html = "", li = 0, ci = 0;
      const pr = '<span class="u">student@apogee</span>:<span class="p">~</span>$ ';
      (function step() {
        if (li >= lines.length) { pre.innerHTML = html + '<span class="cur"></span>'; setTimeout(() => { o.classList.add("off"); setTimeout(() => location.href = url.href, 180); }, 120); return; }
        const [k, t] = lines[li];
        if (k === "out") { html += `<span class="g">${t}</span>\n`; li++; pre.innerHTML = html; return setTimeout(step, 90); }
        if (ci === 0) html += pr;
        if (ci < t.length) { html += t[ci++].replace(/</g, "&lt;"); pre.innerHTML = html + '<span class="cur"></span>'; return setTimeout(step, 11); }
        html += "\n"; li++; ci = 0; setTimeout(step, 60);
      })();
    }
    // arriving
    let arr = null; try { arr = sessionStorage.getItem("fx-arrive"); sessionStorage.removeItem("fx-arrive"); } catch (er) {}
    if (arr && !still()) {
      body.classList.add("fx-arrive-" + arr);
      setTimeout(() => body.classList.remove("fx-arrive-" + arr), 1000);
      if (arr === "space" && SPACE) warpAt = performance.now() - 450;
    }
    addEventListener("pageshow", e => { if (e.persisted) document.querySelectorAll(".fx-warp,.fx-tty").forEach(x => x.remove()); });
  }
  spaceStars(); spaceHero(); termDecor(); fx();
  buildQuizzes();
  buildCourseList();
  if (window.Sims) window.Sims.mountAll();
  // checkboxes that remember their state (test review checklist)
  const remember = [...document.querySelectorAll("input[data-remember]")];
  function trUpdate() {
    const n = remember.filter(c => c.checked).length, el = document.getElementById("tr-count"), bar = document.getElementById("tr-bar");
    if (el) el.textContent = n + " of " + remember.length + " ready" + (n === remember.length && n ? ". All points checked." : "");
    if (bar) bar.style.width = (remember.length ? (n / remember.length) * 100 : 0) + "%";
  }
  remember.forEach(c => {
    try { c.checked = localStorage.getItem(c.dataset.remember) === "1"; } catch (e) {}
    c.addEventListener("change", () => { try { localStorage.setItem(c.dataset.remember, c.checked ? "1" : "0"); } catch (e) {} trUpdate(); });
  });
  trUpdate();
  // reveal problem-set animations when their solution is opened
  document.querySelectorAll(".qcard details.reveal").forEach(d => d.addEventListener("toggle", () => {
    if (!d.open) return;
    d.closest(".qcard").querySelectorAll(".sim").forEach(el => el._ctl && el._ctl.reveal());
  }));
  revealIn(document);
  // quiz cards are re-rendered on filter changes
  document.querySelectorAll(".quiz").forEach(q => new MutationObserver(() => revealIn(q)).observe(q, { childList: true, subtree: true }));
})();
