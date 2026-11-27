/* Interactive workshops: hands-on missions with goals, hints, stars and saved progress.
   Each mission is <section class="mission" data-m='{"id": "...", "type": "...", ...}'>. */
(function () {
  "use strict";
  const KEY = "margin-ws";
  const body = document.body, COURSE = body.dataset.course || "x";
  const esc = s => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  const still = () => body.classList.contains("no-motion") || matchMedia("(prefers-reduced-motion: reduce)").matches;
  const deacc = s => s.normalize("NFD").replace(/[̀-ͯ]/g, "");
  const norm = s => String(s).replace(/[’‘]/g, "'").replace(/\s+/g, " ").trim();
  const fm = (x, d = 2) => (Math.abs(x) < 1e-9 ? "0" : (+x.toFixed(d)).toString().replace("-", "−"));
  const shuffle = (a, r = Math.random) => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(r() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
  const pick = (a, r = Math.random) => a[Math.floor(r() * a.length)];
  const B = (act, label, cls = "") => `<button type="button" class="mg-b ${cls}" data-act="${act}">${label}</button>`;
  function load() { try { return JSON.parse(localStorage.getItem(KEY)) || {}; } catch (e) { return {}; } }
  function save(d) { try { localStorage.setItem(KEY, JSON.stringify(d)); } catch (e) { } }
  const css = n => getComputedStyle(body).getPropertyValue(n).trim();
  const ACC = () => (body.classList.contains("th-space") || body.classList.contains("th-term")) ? "#2563EB" : (css("--lab-a") || css("--sky") || "#2563EB"), ACC2 = () => "#EA580C", INK = () => "#1E293B";
  function canvas(host, W, H) {
    const wrap = document.createElement("div"); wrap.className = "ws-stage"; const cv = document.createElement("canvas"); wrap.appendChild(cv); host.appendChild(wrap);
    const d = Math.min(2, devicePixelRatio || 1); cv.width = W * d; cv.height = H * d; cv.style.aspectRatio = W + " / " + H;
    const c = cv.getContext("2d"); c.setTransform(d, 0, 0, d, 0, 0);
    return { cv, c, W, H, pos(e) { const r = cv.getBoundingClientRect(); return [(e.clientX - r.left) * W / r.width, (e.clientY - r.top) * H / r.height]; } };
  }
  function evalNum(s) {
    s = String(s).trim().replace(/−/g, "-").replace(/×/g, "*").replace(/÷/g, "/").replace(/\^/g, "**").replace(/,/g, "");
    if (!s || !/^[\d\s.+\-*/()eE]+$/.test(s)) return NaN;
    try { const v = Function("return (" + s + ")")(); return typeof v === "number" ? v : NaN; } catch (e) { return NaN; }
  }

  /* ---------------- mission shell ---------------- */
  const P = load(); P[COURSE] = P[COURSE] || {};
  const missions = [...document.querySelectorAll(".mission[data-m]")];
  P[COURSE]._t = missions.length; save(P);
  function meter() {
    const m = document.querySelector(".ws-meter"); if (!m) return;
    const got = missions.filter(s => P[COURSE][JSON.parse(s.dataset.m).id]).length, stars = missions.reduce((a, s) => a + (P[COURSE][JSON.parse(s.dataset.m).id] || 0), 0);
    m.innerHTML = `<div class="ws-ring" style="--p:${missions.length ? got / missions.length : 0}"><b>${got}/${missions.length}</b><small>missions</small></div>
      <div class="ws-mt"><b>${got === missions.length ? "Workshop complete!" : got ? "Keep going" : "Start with mission 1"}</b><span>${stars} of ${missions.length * 3} stars</span>
      <div class="ws-dots">${missions.map((s, i) => { const sp = JSON.parse(s.dataset.m), st = P[COURSE][sp.id] || 0; return `<a href="#${s.id}" class="${st ? "on" : ""}" title="Mission ${i + 1}: ${esc(s.querySelector("h2").textContent.replace(/^Mission \d+/, "").trim())}">${st ? "★".repeat(st) : i + 1}</a>`; }).join("")}</div></div>
      ${got ? `<button type="button" class="mg-b sm ws-reset">Reset progress</button>` : ""}`;
    const r = m.querySelector(".ws-reset"); if (r) r.onclick = () => { if (r.dataset.sure) { P[COURSE] = { _t: missions.length }; save(P); location.reload(); } else { r.dataset.sure = 1; r.textContent = "Click again to reset"; } };
  }
  function starsHTML(n) { return `<span class="ws-stars" aria-label="${n} of 3 stars">${[1, 2, 3].map(i => `<i class="${i <= n ? "on" : ""}">★</i>`).join("")}</span>`; }
  function setup(sec, idx) {
    let spec; try { spec = JSON.parse(sec.dataset.m); } catch (e) { return; }
    const play = sec.querySelector(".m-play"), win = sec.querySelector(".m-win");
    const h2 = sec.querySelector("h2"); const badge = document.createElement("span"); badge.className = "m-badge"; h2.appendChild(badge);
    const status = document.createElement("div"); status.className = "m-status"; play.after(status);
    const hints = spec.hints || []; let used = 0;
    const tools = document.createElement("div"); tools.className = "m-tools"; status.after(tools);
    function paintBadge() { const s = P[COURSE][spec.id] || 0; badge.innerHTML = s ? starsHTML(s) : ""; sec.classList.toggle("is-done", !!s); }
    if (hints.length) {
      tools.innerHTML = `<button type="button" class="mg-b sm m-hint">💡 Hint <span>(${hints.length})</span></button><div class="m-hints"></div>`;
      const hb = tools.querySelector(".m-hint"), hl = tools.querySelector(".m-hints");
      hb.onclick = () => { if (used >= hints.length) return; hl.insertAdjacentHTML("beforeend", `<p>${hints[used++]}</p>`); hb.querySelector("span").textContent = `(${hints.length - used} left)`; if (used >= hints.length) hb.disabled = true; };
    }
    const ctx = {
      spec, sec, play,
      say(html, kind = "") { status.className = "m-status " + kind; status.innerHTML = html; },
      done(stars = 3, note = "") {
        stars = Math.max(1, Math.min(3, stars - Math.min(2, used)));
        const prev = P[COURSE][spec.id] || 0; P[COURSE][spec.id] = Math.max(prev, stars); save(P); paintBadge(); meter();
        const next = missions[idx + 1];
        status.className = "m-status win"; status.innerHTML = `<div class="m-wint"><b>Mission complete!</b> ${starsHTML(stars)}${used ? ` <small>(${used} hint${used > 1 ? "s" : ""} used)</small>` : ""}</div>${note ? `<p>${note}</p>` : ""}
          <div class="m-nav">${B("again", "Play again")}${next ? `<a class="mg-b solid" href="#${next.id}">Next mission →</a>` : `<a class="mg-b solid" href="#top">All missions done ✓</a>`}</div>`;
        status.querySelector('[data-act="again"]').onclick = () => { used = 0; const hl = tools.querySelector(".m-hints"); if (hl) hl.innerHTML = ""; const hb = tools.querySelector(".m-hint"); if (hb) { hb.disabled = false; hb.querySelector("span").textContent = `(${hints.length})`; } status.className = "m-status"; status.innerHTML = ""; if (win) win.hidden = true; play.innerHTML = ""; start(); };
        if (win) win.hidden = false;
        if (!still()) burst(status);
      }
    };
    function start() { const g = GAMES[spec.type]; if (!g) { play.textContent = "Unknown mission type."; return; } try { g(ctx); } catch (e) { console.error(e); play.innerHTML = `<p class="xl-note">This mission could not load.</p>`; } }
    paintBadge(); start();
  }
  function burst(host) {
    const b = document.createElement("div"); b.className = "ws-burst"; b.setAttribute("aria-hidden", "true");
    b.innerHTML = Array.from({ length: 14 }, (_, i) => `<i style="--a:${i * 360 / 14}deg;--d:${(i % 3) * 60}ms"></i>`).join(""); host.prepend(b); setTimeout(() => b.remove(), 1200);
  }

  /* ---------------- physics: projectile launcher ---------------- */
  function launch(c) {
    const p = c.spec, g = 10, h0 = p.h0 || 0, T = p.target, wall = p.wall;
    const xmax = p.xmax || Math.ceil(T[1] * 1.35 / 5) * 5, ymax = p.ymax || Math.max(xmax * .4, (wall ? wall.h : 0) * 1.6, h0 * 1.6);
    const S = { a: p.angle ?? 45, v: p.v ?? 15 }; let shots = [], anim = null, won = false;
    c.play.innerHTML = `<div class="mg-sl">${p.fixAngle ? "" : `<label><span class="mg-k">angle θ</span><input type="range" data-k="a" min="5" max="85" step="1" value="${S.a}"><b data-v="a"></b></label>`}
      ${p.fixSpeed ? "" : `<label><span class="mg-k">speed v</span><input type="range" data-k="v" min="${p.vmin || 5}" max="${p.vmax || 30}" step="0.1" value="${S.v}"><b data-v="v"></b></label>`}</div>
      <div class="ws-fix">${p.fixAngle ? `Angle is fixed at <b>${S.a}°</b>. ` : ""}${p.fixSpeed ? `Speed is fixed at <b>${S.v} m/s</b>. ` : ""}Target: <b>${T[0]}–${T[1]} m</b>${h0 ? ` · launching from a <b>${h0} m</b> cliff` : ""}${wall ? ` · wall <b>${wall.h} m</b> tall at <b>${wall.x} m</b>` : ""} · g = 10 m/s²</div>`;
    const st = canvas(c.play, 680, 300);
    c.play.insertAdjacentHTML("beforeend", `<div class="mg-ctl">${B("fire", "Launch ▸", "solid")}<label class="xl-in">or type speed <input type="number" step="0.1" class="ws-num" value="${S.v}" ${p.fixSpeed ? "disabled" : ""}></label><div class="mg-read ws-rd"></div></div>`);
    const rd = c.play.querySelector(".ws-rd"), num = c.play.querySelector(".ws-num");
    const pad = 26, k = Math.min((st.W - 2 * pad) / xmax, (st.H - 2 * pad) / ymax), X = x => pad + x * k, Y = y => st.H - pad - y * k;
    c.play.querySelectorAll("input[data-k]").forEach(i => { const o = c.play.querySelector(`[data-v="${i.dataset.k}"]`); const sh = () => o.textContent = i.dataset.k === "a" ? S.a + "°" : (+S.v).toFixed(1) + " m/s"; S[i.dataset.k] = +i.value; sh(); i.oninput = () => { S[i.dataset.k] = +i.value; if (i.dataset.k === "v") num.value = S.v; sh(); draw(); }; });
    num.oninput = () => { const v = +num.value; if (v > 0) { S.v = v; const i = c.play.querySelector('input[data-k="v"]'); if (i) { i.value = v; c.play.querySelector('[data-v="v"]').textContent = v.toFixed(1) + " m/s"; } draw(); } };
    function traj(a, v) {
      const th = a * Math.PI / 180, vx = v * Math.cos(th), vy = v * Math.sin(th), tl = (vy + Math.sqrt(vy * vy + 2 * g * h0)) / g;
      let tEnd = tl, hitWall = false;
      if (wall) { const tw = wall.x / vx, yw = h0 + vy * tw - .5 * g * tw * tw; if (tw < tl && yw < wall.h) { tEnd = tw; hitWall = true; } }
      return { vx, vy, tEnd, hitWall, xEnd: vx * tEnd, at: t => [vx * t, h0 + vy * t - .5 * g * t * t] };
    }
    function scene(ball, live) {
      const cx = st.c, A = ACC(); cx.clearRect(0, 0, st.W, st.H);
      cx.fillStyle = "#EEF6FF"; cx.fillRect(0, 0, st.W, st.H);
      cx.strokeStyle = "rgba(100,116,139,.15)"; cx.lineWidth = 1; cx.font = "500 10px JetBrains Mono, monospace"; cx.fillStyle = "#64748B";
      for (let x = 0; x <= xmax; x += xmax > 60 ? 10 : 5) { cx.beginPath(); cx.moveTo(X(x), Y(0)); cx.lineTo(X(x), Y(ymax)); cx.stroke(); cx.fillText(x, X(x) - 4, Y(0) + 14); }
      cx.fillStyle = "#86EFAC"; cx.fillRect(X(T[0]), Y(0) - 6, (T[1] - T[0]) * k, 6); cx.fillStyle = "#16A34A"; cx.fillRect(X(T[0]), Y(0), (T[1] - T[0]) * k, 4);
      cx.font = "700 11px JetBrains Mono, monospace"; cx.fillText("TARGET", X((T[0] + T[1]) / 2) - 22, Y(0) - 12);
      cx.strokeStyle = "#334155"; cx.lineWidth = 2; cx.beginPath(); cx.moveTo(0, Y(0)); cx.lineTo(st.W, Y(0)); cx.stroke();
      if (h0) { cx.fillStyle = "#A8A29E"; cx.fillRect(0, Y(h0), X(0) + 6, Y(0) - Y(h0)); }
      if (wall) { cx.fillStyle = "#78716C"; cx.fillRect(X(wall.x) - 4, Y(wall.h), 8, Y(0) - Y(wall.h)); }
      shots.forEach((s, i) => { cx.strokeStyle = i === shots.length - 1 && !live ? A : "rgba(100,116,139,.35)"; cx.lineWidth = 2; cx.setLineDash([4, 4]); cx.beginPath();
        for (let q = 0; q <= 60; q++) { const [x, y] = s.at(s.tEnd * q / 60); q ? cx.lineTo(X(x), Y(y)) : cx.moveTo(X(x), Y(y)); } cx.stroke(); cx.setLineDash([]); });
      const th = S.a * Math.PI / 180; cx.save(); cx.translate(X(0), Y(h0)); cx.rotate(-th); cx.fillStyle = INK(); cx.fillRect(0, -5, 26, 10); cx.restore();
      cx.beginPath(); cx.arc(X(0), Y(h0), 9, 0, 6.3); cx.fillStyle = INK(); cx.fill();
      if (!live && !shots.length) { const t = traj(S.a, S.v); cx.strokeStyle = "rgba(100,116,139,.0)"; }
      if (ball) { cx.beginPath(); cx.arc(X(ball[0]), Y(ball[1]), 6, 0, 6.3); cx.fillStyle = ACC2(); cx.fill(); cx.strokeStyle = "#fff"; cx.lineWidth = 2; cx.stroke(); }
    }
    function draw() { if (!anim) scene(null, false); }
    function fire() {
      if (anim) return; const t = traj(S.a, S.v); shots.push(t); if (shots.length > 6) shots.shift();
      const t0 = performance.now(), dur = still() ? 1 : Math.min(2600, 700 + t.tEnd * 650);
      const step = now => { const f = Math.min(1, (now - t0) / dur); scene(t.at(t.tEnd * f), true); if (f < 1) anim = requestAnimationFrame(step); else { anim = null; scene(t.at(t.tEnd), false); result(t); } };
      anim = requestAnimationFrame(step);
    }
    let n = 0;
    function result(t) {
      n++; const x = t.xEnd;
      rd.innerHTML = `<span>shots <b>${n}</b></span><span>${t.hitWall ? "hit the wall" : `landed at <b>${fm(x, 1)} m</b>`}</span><span>flight <b>${fm(t.tEnd, 2)} s</b></span>`;
      if (!t.hitWall && x >= T[0] && x <= T[1]) { if (!won) { won = true; c.done(n === 1 ? 3 : n <= 3 ? 2 : 1, p.win || ""); } }
      else c.say(t.hitWall ? "Blocked by the wall. Try a steeper angle or more speed." : x < T[0] ? `Short by ${fm(T[0] - x, 1)} m.` : `Long by ${fm(x - T[1], 1)} m.`, "miss");
    }
    c.play.addEventListener("click", e => { if (e.target.closest('[data-act="fire"]')) fire(); });
    draw();
  }

  /* ---------------- physics: collisions ---------------- */
  function collide(c) {
    const p = c.spec, S = Object.assign({ m1: 2, v1: 4, m2: 2, v2: 0 }, p.init || {}); let busy = false, tries = 0, won = false;
    const NM = { m1: "m₁ (kg)", v1: "v₁ (m/s)", m2: "m₂ (kg)", v2: "v₂ (m/s)" };
    c.play.innerHTML = `<div class="mg-sl">${(p.sliders || []).map(s => `<label><span class="mg-k">${NM[s.k]}</span><input type="range" data-k="${s.k}" min="${s.min}" max="${s.max}" step="${s.step || .5}" value="${S[s.k]}"><b data-v="${s.k}"></b></label>`).join("")}</div>
      <div class="ws-fix">${Object.keys(NM).filter(k => !(p.sliders || []).some(s => s.k === k)).map(k => `${NM[k].split(" ")[0]} = <b>${S[k]}</b>`).join(" · ")} · ${p.kind === "elastic" ? "elastic collision (bounce)" : "the carts stick together"}</div>`;
    const st = canvas(c.play, 680, 190);
    c.play.insertAdjacentHTML("beforeend", `<div class="mg-ctl">${B("go", "Collide ▸", "solid")}<div class="mg-read ws-rd"></div></div>`);
    const rd = c.play.querySelector(".ws-rd");
    c.play.querySelectorAll("input[data-k]").forEach(i => { const o = c.play.querySelector(`[data-v="${i.dataset.k}"]`); const sh = () => o.textContent = S[i.dataset.k]; S[i.dataset.k] = +i.value; sh(); i.oninput = () => { S[i.dataset.k] = +i.value; sh(); if (!busy) scene(140, 470, null); }; });
    function after() {
      const { m1, v1, m2, v2 } = S;
      if (p.kind === "elastic") { const a = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2), b = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2); return { v1f: a, v2f: b, vf: NaN, KElost: 0 }; }
      const vf = (m1 * v1 + m2 * v2) / (m1 + m2); return { vf, v1f: vf, v2f: vf, KElost: .5 * m1 * v1 * v1 + .5 * m2 * v2 * v2 - .5 * (m1 + m2) * vf * vf };
    }
    function cart(x, w, col, lab) { const cx = st.c; cx.fillStyle = col; cx.beginPath(); cx.roundRect ? cx.roundRect(x, 92, w, 52, 8) : cx.rect(x, 92, w, 52); cx.fill(); cx.fillStyle = "#fff"; cx.font = "700 13px JetBrains Mono, monospace"; cx.textAlign = "center"; cx.fillText(lab, x + w / 2, 124); cx.fillStyle = "#1F2937"; cx.beginPath(); cx.arc(x + 12, 150, 7, 0, 6.3); cx.arc(x + w - 12, 150, 7, 0, 6.3); cx.fill(); cx.textAlign = "left"; }
    const w1 = () => 50 + S.m1 * 6, w2 = () => 50 + S.m2 * 6;
    function scene(x1, x2, label) {
      const cx = st.c; cx.clearRect(0, 0, st.W, st.H); cx.fillStyle = "#F8FAFC"; cx.fillRect(0, 0, st.W, st.H); cx.strokeStyle = "#334155"; cx.lineWidth = 2; cx.beginPath(); cx.moveTo(0, 158); cx.lineTo(st.W, 158); cx.stroke();
      cart(x1, w1(), ACC(), S.m1 + " kg"); cart(x2, w2(), ACC2(), S.m2 + " kg");
      cx.font = "600 12px JetBrains Mono, monospace"; cx.fillStyle = "#334155"; if (label) cx.fillText(label, 16, 30);
    }
    function go() {
      if (busy) return; busy = true; tries++; const r = after(), t0 = performance.now(); let phase = 0, xa = 60, xb = 470, sp = 26;
      const vA = S.v1, vB = S.v2, tc = (xb - xa - w1()) / Math.max(.3, (vA - vB) * sp);
      const step = now => {
        const t = still() ? tc + 1.6 : (now - t0) / 1000;
        let x1, x2, lab;
        if (t < tc || !(vA > vB)) { x1 = xa + vA * sp * t; x2 = xb + vB * sp * t; lab = `before: p = ${fm(S.m1 * S.v1 + S.m2 * S.v2)} kg·m/s`; if (!(vA > vB) && t > 2) { busy = false; c.say("The carts never meet: cart 1 must be faster than cart 2.", "miss"); return; } }
        else { const d = t - tc, xc = xa + vA * sp * tc; x1 = xc + r.v1f * sp * d; x2 = xc + w1() + (p.kind === "elastic" ? r.v2f : r.v1f) * sp * d; lab = `after: p = ${fm(S.m1 * r.v1f + S.m2 * r.v2f)} kg·m/s (momentum is conserved)`; }
        scene(x1, x2, lab);
        if (t < tc + 1.6 && x1 < st.W && x2 < st.W + 200) requestAnimationFrame(step); else { busy = false; verdict(r); }
      };
      requestAnimationFrame(step);
    }
    function verdict(r) {
      const G = p.goal, v = r[G.k], ok = Math.abs(v - G.value) <= (G.tol ?? .05);
      rd.innerHTML = p.kind === "elastic" ? `<span>v₁ after <b>${fm(r.v1f)}</b></span><span>v₂ after <b>${fm(r.v2f)}</b></span>` : `<span>v after <b>${fm(r.vf)} m/s</b></span><span>KE lost <b>${fm(r.KElost)} J</b></span>`;
      if (ok && !won) { won = true; c.done(tries === 1 ? 3 : tries <= 3 ? 2 : 1, p.win || ""); } else if (!ok) c.say(`${G.label || G.k} came out ${fm(v)}; the goal is ${G.value}. Adjust and try again.`, "miss");
    }
    c.play.addEventListener("click", e => { if (e.target.closest('[data-act="go"]')) go(); });
    scene(60, 470, null);
  }

  /* ---------------- question sets (numeric, text or multiple choice) ---------------- */
  function calc(c) {
    const qs = c.spec.qs; let i = 0, score = 0, tries = 0;
    function show() {
      const it = qs[i]; tries = 0;
      c.play.innerHTML = `<div class="ws-qn">Question ${i + 1} of ${qs.length}<span class="ws-score">score ${fm(score, 1)}</span></div><div class="ws-q">${it.q}</div>${it.sim ? `<div class="sim" data-sim='${JSON.stringify(it.sim).replace(/'/g, "&#39;")}'></div>` : ""}
        ${it.o ? `<div class="ws-opts">${it.o.map((o, k) => `<button type="button" class="ws-opt" data-k="${k}">${o}</button>`).join("")}</div>` : `<div class="mg-ctl"><input class="ws-ans" type="text" autocomplete="off" spellcheck="false" placeholder="${it.ph || "your answer"}" aria-label="Your answer">${it.unit ? `<span class="ws-unit">${it.unit}</span>` : ""}${B("check", "Check", "solid")}</div>`}<div class="ws-fb"></div>`;
      if (it.sim && window.Sims) window.Sims.mountAll(c.play);
      const inp = c.play.querySelector(".ws-ans"); if (inp) { inp.focus({ preventScroll: true }); inp.onkeydown = e => { if (e.key === "Enter") check(inp.value); }; }
    }
    function right(v) { const it = qs[i]; if (it.o) return +v === it.a; if (typeof it.a === "number") { const x = evalNum(v); if (isNaN(x)) return null; const tol = it.abs != null ? it.abs : Math.abs(it.a) * (it.tol ?? .02) + 1e-9; return Math.abs(x - it.a) <= tol; }
      const a = norm(it.a), u = norm(v); return it.cs ? a === u : a.toLowerCase() === u.toLowerCase() || (it.alt || []).some(x => norm(x).toLowerCase() === u.toLowerCase()); }
    function check(v) {
      const it = qs[i], fb = c.play.querySelector(".ws-fb"), ok = right(v);
      if (ok === null) { fb.className = "ws-fb"; fb.innerHTML = "Type a number (you can use fractions like 3/4)."; return; }
      tries++;
      if (ok || tries >= 2) {
        if (ok) score += tries === 1 ? 1 : .5;
        fb.className = "ws-fb " + (ok ? "ok" : "no"); fb.innerHTML = `${ok ? "<b>Correct.</b>" : `<b>Answer:</b> ${it.o ? it.o[it.a] : esc(String(it.show || it.a))}${it.unit ? " " + it.unit : ""}.`} ${it.x || ""} <div class="mg-ctl">${B("next", i + 1 < qs.length ? "Next question →" : "See results", "solid")}</div>`;
        c.play.querySelectorAll(".ws-opt").forEach(b => { b.disabled = true; if (+b.dataset.k === it.a) b.classList.add("ok"); else if (b.dataset.k === String(v)) b.classList.add("no"); });
        const ip = c.play.querySelector(".ws-ans"); if (ip) ip.disabled = true; const cb = c.play.querySelector('[data-act="check"]'); if (cb) cb.disabled = true;
        const nb = fb.querySelector('[data-act="next"]'); nb.focus({ preventScroll: true });
      } else { fb.className = "ws-fb no"; fb.innerHTML = `Not quite — one more try.${it.h ? " " + it.h : ""}`; c.play.querySelectorAll(".ws-opt").forEach(b => { if (b.dataset.k === String(v)) { b.classList.add("no"); b.disabled = true; } }); }
    }
    function end() {
      const r = score / qs.length;
      if (r >= (c.spec.pass ?? .6)) { c.play.innerHTML = `<div class="ws-res"><b>${fm(score, 1)} / ${qs.length}</b> points</div>`; c.done(r >= .9 ? 3 : r >= .75 ? 2 : 1, c.spec.win || ""); }
      else { c.play.innerHTML = `<div class="ws-res"><b>${fm(score, 1)} / ${qs.length}</b> points — you need ${Math.ceil((c.spec.pass ?? .6) * qs.length)} to pass this mission.</div><div class="mg-ctl">${B("retry", "Try again", "solid")}</div>`; }
    }
    c.play.addEventListener("click", e => {
      const o = e.target.closest(".ws-opt"); if (o && !o.disabled) { check(o.dataset.k); return; }
      const a = e.target.closest("[data-act]"); if (!a) return;
      if (a.dataset.act === "check") check(c.play.querySelector(".ws-ans").value);
      if (a.dataset.act === "next") { i++; if (i < qs.length) show(); else end(); }
      if (a.dataset.act === "retry") { i = 0; score = 0; show(); }
    });
    show();
  }

  /* ---------------- timed sprint ---------------- */
  function sprint(c) {
    const p = c.spec; let qs, i, score, ans, left, timer;
    function intro() { c.play.innerHTML = `<div class="ws-sprint0"><div class="ws-big">${p.qs.length} questions · ${Math.round(p.time / 60 * 10) / 10} minutes</div><p>No feedback until the end. Skip with “Next” if you're stuck — pacing is part of the test.</p>${B("start", "Start the clock ▸", "solid")}</div>`; }
    function start() { qs = p.shuffle === false ? p.qs : shuffle(p.qs); i = 0; score = 0; ans = []; left = p.time; tick(); timer = setInterval(tick, 1000); show(); }
    function tick() { const t = c.play.querySelector(".ws-clock"); if (t) { t.textContent = `${Math.floor(left / 60)}:${String(left % 60).padStart(2, "0")}`; t.classList.toggle("low", left <= 15); } if (left-- <= 0) end(); }
    function show() {
      const it = qs[i];
      c.play.innerHTML = `<div class="ws-qn">Question ${i + 1} of ${qs.length}<span class="ws-clock">--:--</span></div><div class="ws-bar"><i style="width:${i / qs.length * 100}%"></i></div><div class="ws-q">${it.q}</div>
        ${it.o ? `<div class="ws-opts">${it.o.map((o, k) => `<button type="button" class="ws-opt" data-k="${k}">${String.fromCharCode(65 + k)}. ${o}</button>`).join("")}</div>` : `<div class="mg-ctl"><input class="ws-ans" type="text" autocomplete="off" placeholder="type your answer"></div>`}
        <div class="mg-ctl">${B("skip", it.o ? "Skip →" : "Submit →", it.o ? "" : "solid")}</div>`;
      tick(); left++;
      const inp = c.play.querySelector(".ws-ans"); if (inp) { inp.focus({ preventScroll: true }); inp.onkeydown = e => { if (e.key === "Enter") answer(inp.value); }; }
    }
    function isRight(it, v) { if (v == null || v === "") return false; if (it.o) return +v === it.a; if (typeof it.a === "number") { const x = evalNum(v); return !isNaN(x) && Math.abs(x - it.a) <= (it.abs ?? Math.abs(it.a) * .01 + 1e-9); } return norm(v).toLowerCase() === norm(it.a).toLowerCase(); }
    function answer(v) { const it = qs[i]; const ok = isRight(it, v); if (ok) score++; ans.push({ it, v, ok }); i++; if (i < qs.length) show(); else end(); }
    function end() {
      clearInterval(timer); if (!qs) return; while (ans.length < qs.length) ans.push({ it: qs[ans.length], v: null, ok: false });
      const r = score / qs.length, pass = r >= (p.pass ?? .7);
      c.play.innerHTML = `<div class="ws-res"><b>${score} / ${qs.length}</b> ${pass ? "— passed!" : `— you need ${Math.ceil((p.pass ?? .7) * qs.length)} to pass.`}</div>
        <details class="ws-review" ${pass ? "" : "open"}><summary>Review every question</summary>${ans.map((a, k) => `<div class="ws-rv ${a.ok ? "ok" : "no"}"><b>${k + 1}.</b> ${a.it.q}<p>${a.ok ? "✓ Correct" : `✗ ${a.v == null || a.v === "" ? "No answer" : "You answered " + esc(a.it.o ? a.it.o[a.v] : a.v)}. Correct: <b>${a.it.o ? a.it.o[a.it.a] : esc(String(a.it.show || a.it.a))}</b>`}${a.it.x ? " — " + a.it.x : ""}</p></div>`).join("")}</details>
        ${pass ? "" : `<div class="mg-ctl">${B("start", "Try again", "solid")}</div>`}`;
      qs = null; if (pass) c.done(r >= .95 ? 3 : r >= .8 ? 2 : 1, p.win || "");
    }
    c.play.addEventListener("click", e => {
      const o = e.target.closest(".ws-opt"); if (o) { answer(o.dataset.k); return; }
      const a = e.target.closest("[data-act]"); if (!a) return;
      if (a.dataset.act === "start") start(); if (a.dataset.act === "skip") { const inp = c.play.querySelector(".ws-ans"); answer(inp ? inp.value : null); }
    });
    intro();
  }

  /* ---------------- math: match the graph ---------------- */
  function match(c) {
    const p = c.spec, S = {}, ev = window.MathEval || ((e, env) => NaN); let won = false;
    Object.entries(p.params).forEach(([k, d]) => S[k] = d[3]);
    c.play.innerHTML = `<div class="mg-sl">${Object.entries(p.params).map(([k, d]) => `<label><span class="mg-k">${d[4] || k}</span><input type="range" data-k="${k}" min="${d[0]}" max="${d[1]}" step="${d[2]}" value="${d[3]}"><b data-v="${k}"></b></label>`).join("")}</div><div class="ws-eq"></div>`;
    const st = canvas(c.play, 620, 360);
    c.play.insertAdjacentHTML("beforeend", `<div class="ws-close"><span>How close</span><div class="ws-bar"><i></i></div><b></b></div>`);
    const [x0, x1] = p.x, [y0, y1] = p.y, X = x => 30 + (x - x0) / (x1 - x0) * (st.W - 40), Y = y => 10 + (y1 - y) / (y1 - y0) * (st.H - 30);
    const f = (env, x) => ev(p.expr, Object.assign({ x }, env));
    function curve(env, col, dash, w) { const cx = st.c; cx.strokeStyle = col; cx.lineWidth = w; cx.setLineDash(dash ? [8, 6] : []); cx.beginPath(); let pen = false;
      for (let i = 0; i <= 400; i++) { const x = x0 + (x1 - x0) * i / 400, y = f(env, x); if (!isFinite(y) || y > y1 + 50 || y < y0 - 50) { pen = false; continue; } pen ? cx.lineTo(X(x), Y(y)) : cx.moveTo(X(x), Y(y)); pen = true; } cx.stroke(); cx.setLineDash([]); }
    function err() { let s = 0, n = 0; for (let i = 0; i <= 80; i++) { const x = x0 + (x1 - x0) * i / 80, a = f(p.target, x), b = f(S, x); if (!isFinite(a)) continue; const d = Math.max(-40, Math.min(40, (isFinite(b) ? b : 1e3) - a)); s += d * d; n++; } return Math.sqrt(s / n) / (y1 - y0); }
    function draw() {
      const cx = st.c; cx.clearRect(0, 0, st.W, st.H); cx.fillStyle = "#fff"; cx.fillRect(0, 0, st.W, st.H);
      cx.strokeStyle = "rgba(100,116,139,.16)"; cx.lineWidth = 1; cx.font = "500 10px JetBrains Mono, monospace"; cx.fillStyle = "#64748B";
      const sx = p.gx || 1, sy = p.gy || 1;
      for (let x = Math.ceil(x0 / sx) * sx; x <= x1; x += sx) { cx.beginPath(); cx.moveTo(X(x), Y(y0)); cx.lineTo(X(x), Y(y1)); cx.stroke(); }
      for (let y = Math.ceil(y0 / sy) * sy; y <= y1; y += sy) { cx.beginPath(); cx.moveTo(X(x0), Y(y)); cx.lineTo(X(x1), Y(y)); cx.stroke(); }
      cx.strokeStyle = "#334155"; cx.lineWidth = 1.6; cx.beginPath(); cx.moveTo(X(x0), Y(0)); cx.lineTo(X(x1), Y(0)); cx.moveTo(X(0), Y(y0)); cx.lineTo(X(0), Y(y1)); cx.stroke();
      for (let x = Math.ceil(x0 / sx) * sx; x <= x1; x += sx) if (x) cx.fillText(fm(x, 2), X(x) - 4, Y(0) + 13);
      for (let y = Math.ceil(y0 / sy) * sy; y <= y1; y += sy) if (y) cx.fillText(fm(y, 2), X(0) + 4, Y(y) + 4);
      cx.save(); cx.beginPath(); cx.rect(0, 0, st.W, st.H); cx.clip(); curve(p.target, ACC2(), true, 5); curve(S, ACC(), false, 3); cx.restore();
      cx.font = "700 12px JetBrains Mono, monospace"; cx.fillStyle = ACC2(); cx.fillText("- - target", st.W - 110, 24); cx.fillStyle = ACC(); cx.fillText("—— yours", st.W - 110, 40);
      let eq = p.show; Object.keys(S).forEach(k => { eq = eq.split("{" + k + "}").join(fm(S[k], 2)); }); c.play.querySelector(".ws-eq").innerHTML = eq.replace(/\+ −/g, "− ").replace(/− −/g, "+ ");
      const e = err(), close = Math.max(0, 1 - e * 4); const bar = c.play.querySelector(".ws-close");
      bar.querySelector("i").style.width = (close * 100).toFixed(0) + "%"; bar.querySelector("b").textContent = Math.round(close * 100) + "%"; bar.classList.toggle("hot", e < (p.tol || .02));
      if (e < (p.tol || .02) && !won) { won = true; c.done(3, p.win || ""); }
    }
    c.play.querySelectorAll("input[data-k]").forEach(i => { const o = c.play.querySelector(`[data-v="${i.dataset.k}"]`); const sh = () => o.textContent = fm(S[i.dataset.k], 2); sh(); i.oninput = () => { S[i.dataset.k] = +i.value; sh(); draw(); }; });
    draw();
  }

  /* ---------------- code: Parsons puzzle ---------------- */
  function parsons(c) {
    const p = c.spec, sol = p.lines; let order, tries = 0, won = false, drag = null;
    let r = 1; const rr = () => (r = (r * 9301 + 49297) % 233280) / 233280;
    do { order = shuffle(sol.map((_, i) => i), rr); } while (order.every((v, i) => sol[v] === sol[i]));
    c.play.innerHTML = `<p class="ws-task">${p.task || "Put the lines in the right order."}</p><ol class="ws-par"></ol><div class="mg-ctl">${B("check", "Check order", "solid")}<span class="ws-tip">Drag lines, or use the ↑ ↓ buttons.</span></div>`;
    const ol = c.play.querySelector(".ws-par");
    function draw(marks) {
      ol.innerHTML = order.map((li, pos) => `<li draggable="true" data-pos="${pos}" class="${marks ? (sol[li] === sol[pos] ? "ok" : "no") : ""}"><span class="ws-grip" aria-hidden="true">⋮⋮</span><code>${esc(sol[li])}</code><span class="ws-mv"><button type="button" data-up="${pos}" aria-label="Move up">↑</button><button type="button" data-dn="${pos}" aria-label="Move down">↓</button></span></li>`).join("");
    }
    ol.addEventListener("dragstart", e => { const li = e.target.closest("li"); if (!li) return; drag = +li.dataset.pos; li.classList.add("drag"); e.dataTransfer.effectAllowed = "move"; try { e.dataTransfer.setData("text/plain", "x"); } catch (x) { } });
    ol.addEventListener("dragover", e => { e.preventDefault(); const li = e.target.closest("li"); ol.querySelectorAll("li").forEach(x => x.classList.toggle("over", x === li)); });
    ol.addEventListener("drop", e => { e.preventDefault(); const li = e.target.closest("li"); if (!li || drag == null) return; const to = +li.dataset.pos; const [m] = order.splice(drag, 1); order.splice(to, 0, m); drag = null; draw(); });
    ol.addEventListener("dragend", () => { drag = null; ol.querySelectorAll("li").forEach(x => x.classList.remove("drag", "over")); });
    c.play.addEventListener("click", e => {
      const u = e.target.closest("[data-up]"), d = e.target.closest("[data-dn]");
      if (u) { const i = +u.dataset.up; if (i > 0) [order[i - 1], order[i]] = [order[i], order[i - 1]]; draw(); return; }
      if (d) { const i = +d.dataset.dn; if (i < order.length - 1) [order[i + 1], order[i]] = [order[i], order[i + 1]]; draw(); return; }
      if (e.target.closest('[data-act="check"]')) {
        tries++; const n = order.filter((v, i) => sol[v] === sol[i]).length; draw(true);
        if (n === sol.length) { if (!won) { won = true; c.done(tries === 1 ? 3 : tries <= 3 ? 2 : 1, p.win || ""); } }
        else c.say(`${n} of ${sol.length} lines are in the right place (green). Keep going.`, "miss");
      }
    });
    draw();
  }

  /* ---------------- computer engineering: bit target rounds ---------------- */
  function bits(c) {
    const p = c.spec, n = p.n || 8, M = (1 << n) - 1; let v = 0, i = 0, t0 = null, timer, won = false;
    const rounds = p.rounds;
    c.play.innerHTML = `<div class="ws-qn"><span class="ws-rn"></span><span class="ws-clock">0.0 s</span></div><div class="ws-target"></div><div class="xl-bits ws-bitrow" style="--n:${n}"></div><div class="xl-read ws-br"></div>`;
    const box = c.play.querySelector(".ws-bitrow"), tg = c.play.querySelector(".ws-target"), rd = c.play.querySelector(".ws-br"), rn = c.play.querySelector(".ws-rn"), clk = c.play.querySelector(".ws-clock");
    const signed = x => x >= 1 << (n - 1) ? x - (1 << n) : x;
    function label(r) { if (r.as === "hex") return `0x${r.t.toString(16).toUpperCase()}`; if (r.as === "signed") return `${r.t} <small>(two's complement)</small>`; if (r.as === "ascii") return `the ASCII code for '${String.fromCharCode(r.t)}'`; if (r.as === "bin") return r.t.toString(2); return String(r.t); }
    const want = r => r.as === "signed" ? (r.t & M) : r.t;
    function draw() {
      const r = rounds[i];
      rn.textContent = `Round ${Math.min(i + 1, rounds.length)} of ${rounds.length}`;
      tg.innerHTML = i < rounds.length ? `Make <b>${label(r)}</b>` : "Done!";
      box.innerHTML = Array.from({ length: n }, (_, j) => { const k = n - 1 - j, b = (v >> k) & 1; const w = (k === n - 1 && r && r.as === "signed") ? "−" + (1 << k) : 1 << k; return `<button type="button" class="xl-bit ${b ? "on" : ""}" data-k="${k}"><b>${b}</b><small>${w}</small></button>`; }).join("");
      rd.innerHTML = `<span>Decimal <b>${v}</b></span><span>Signed <b>${signed(v)}</b></span><span>Hex <b>0x${v.toString(16).toUpperCase().padStart(Math.ceil(n / 4), "0")}</b></span>`;
    }
    box.addEventListener("click", e => {
      const b = e.target.closest(".xl-bit"); if (!b || i >= rounds.length) return;
      if (!t0) { t0 = performance.now(); timer = setInterval(() => clk.textContent = ((performance.now() - t0) / 1000).toFixed(1) + " s", 100); }
      v ^= 1 << +b.dataset.k;
      if (v === want(rounds[i])) { i++; tg.classList.remove("pop"); void tg.offsetWidth; tg.classList.add("pop"); if (i < rounds.length) { setTimeout(() => { v = 0; draw(); }, 350); }
        else { clearInterval(timer); const s = (performance.now() - t0) / 1000; draw(); if (!won) { won = true; c.done(s <= p.par ? 3 : s <= p.par * 2 ? 2 : 1, `Your time: <b>${s.toFixed(1)} s</b> (3 stars under ${p.par} s). ${p.win || ""}`); } return; } }
      draw();
    });
    draw();
  }

  /* ---------------- computer engineering: gate puzzle ---------------- */
  function gates(c) {
    const p = c.spec, X = window.XLabs, inputs = p.inputs, slots = p.slots, outs = p.outputs, pal = p.palette || ["AND", "OR", "XOR", "NAND", "NOR", "NOT"];
    const cur = {}; slots.forEach(s => cur[s.id] = s.fixed || null); let clicks = 0, won = false;
    c.play.innerHTML = `<p class="ws-task">${p.task || "Click each ? to choose a gate. Make the output column match the target column on every row."}</p><svg class="xl-svg ws-gsvg"></svg><div class="xl-tt ws-gtt"></div>`;
    const sv = c.play.querySelector("svg"), tt = c.play.querySelector(".ws-gtt");
    const byId = {}; slots.forEach(s => byId[s.id] = s);
    const depth = {}; const dep = id => inputs.includes(id) ? 0 : depth[id] != null ? depth[id] : (depth[id] = 1 + Math.max(...byId[id].in.map(dep))); slots.forEach(s => dep(s.id));
    const maxD = Math.max(...slots.map(s => depth[s.id])), cols = {}; slots.forEach(s => (cols[depth[s.id]] = cols[depth[s.id]] || []).push(s));
    const nRows = Math.max(inputs.length, ...Object.values(cols).map(x => x.length)), H = Math.max(170, nRows * 86 + 20), W = 130 + maxD * 140 + 130, pos = {};
    inputs.forEach((nm, i) => pos[nm] = { x: 70, y: (i + .5) * (H - 20) / inputs.length + 10 });
    Object.keys(cols).map(Number).sort((a, b) => a - b).forEach(d => cols[d].forEach((s, i) => pos[s.id] = { x: 70 + d * 140, y: (i + .5) * (H - 20) / cols[d].length + 10 }));
    function evalAll(iv) { const o = Object.assign({}, iv); const ev = id => { if (id in o) return o[id]; const s = byId[id], g = cur[s.id]; return o[id] = g ? (X.G[g](s.in.map(ev)) ? 1 : 0) : null; }; slots.forEach(s => ev(s.id)); return o; }
    const rows = []; for (let r = 0; r < 1 << inputs.length; r++) rows.push(inputs.map((_, i) => (r >> (inputs.length - 1 - i)) & 1));
    function draw() {
      const PAL = X.PAL(); let w = "", b = "";
      slots.forEach(s => { const q = pos[s.id], g = cur[s.id], gp = g ? X.gatePath(g) : { out: 50, extra: "" };
        s.in.forEach((src, k) => { const a = pos[src], sx = inputs.includes(src) ? a.x + 22 : a.x + (cur[src] ? X.gatePath(cur[src]).out : 50) * 1.2, py = s.in.length === 1 ? q.y : q.y - 24 + (k + .5) * 48 / s.in.length, tx = q.x + 2, mx = (sx + tx) / 2;
          w += `<path d="M${sx} ${a.y}C${mx} ${a.y} ${mx} ${py} ${tx} ${py}" fill="none" stroke="#94A3B8" stroke-width="3"/>`; });
        b += `<g class="xl-click ws-slot ${s.fixed ? "fixed" : ""}" data-s="${s.id}">${g ? X.gateSVG(g, q.x, q.y - 24, 1.2, s.fixed ? "#F1F5F9" : "#fff", PAL.ink) : `<rect x="${q.x}" y="${q.y - 24}" width="60" height="48" rx="10" fill="#FEF9C3" stroke="#CA8A04" stroke-width="2" stroke-dasharray="5 4"/><text x="${q.x + 30}" y="${q.y + 7}" text-anchor="middle" font-family="JetBrains Mono" font-weight="800" font-size="20" fill="#A16207">?</text>`}
          <text x="${q.x + 30}" y="${q.y + 40}" text-anchor="middle" font-family="JetBrains Mono" font-size="10.5" fill="${PAL.muted}">${g ? g : "click"}${s.fixed ? " (fixed)" : ""}</text></g>`; });
      Object.entries(outs).forEach(([nm, src], i) => { const a = pos[src], y = a.y, x = W - 50, sx = a.x + (cur[src] ? X.gatePath(cur[src]).out : 50) * 1.2;
        w += `<path d="M${sx} ${a.y}L${x - 18} ${y}" stroke="#94A3B8" stroke-width="3"/>`; const rr = Math.max(17, nm.length * 4.6 + 6); b += `<circle cx="${x}" cy="${y}" r="${rr}" fill="#fff" stroke="${PAL.ink}" stroke-width="2"/><text x="${x}" y="${y + 5}" text-anchor="middle" font-family="JetBrains Mono" font-weight="800" font-size="13" fill="${PAL.ink}">${esc(nm)}</text>`; });
      inputs.forEach(nm => { const a = pos[nm]; b += `<rect x="${a.x - 44}" y="${a.y - 15}" width="66" height="30" rx="8" fill="#fff" stroke="#94A3B8" stroke-width="2"/><text x="${a.x - 11}" y="${a.y + 5}" text-anchor="middle" font-family="JetBrains Mono" font-weight="800" font-size="14" fill="${PAL.ink}">${esc(nm)}</text>`; });
      sv.setAttribute("viewBox", `0 0 ${W} ${H}`); sv.innerHTML = w + b;
      let good = 0; const on = Object.keys(outs);
      tt.innerHTML = `<table><tr>${inputs.map(n => `<th>${esc(n)}</th>`).join("")}${on.map(n => `<th class="o">${esc(n)}</th><th class="tg">target</th>`).join("")}</tr>${rows.map((r, ri) => { const iv = {}; inputs.forEach((n, i) => iv[n] = r[i]); const o = evalAll(iv); const ok = on.every(n => o[outs[n]] === p.target[n][ri]); if (ok) good++;
        return `<tr class="${ok ? "cur" : "bad"}">${r.map(x => `<td>${x}</td>`).join("")}${on.map(n => `<td><b>${o[outs[n]] == null ? "?" : o[outs[n]]}</b></td><td class="tg">${p.target[n][ri]}</td>`).join("")}</tr>`; }).join("")}</table><p class="ws-tip">${good} of ${rows.length} rows match.</p>`;
      if (good === rows.length && !won) { won = true; c.done(clicks <= (p.par || 6) ? 3 : clicks <= (p.par || 6) * 2 ? 2 : 1, p.win || ""); }
    }
    sv.addEventListener("click", e => { const g = e.target.closest("[data-s]"); if (!g) return; const s = byId[g.dataset.s]; if (s.fixed) return; const opts = pal.filter(x => (x === "NOT" || x === "BUF") === (s.in.length === 1)); const k = opts.indexOf(cur[s.id]); cur[s.id] = opts[(k + 1) % opts.length]; clicks++; draw(); });
    draw();
  }

  /* ---------------- computer engineering: write a program ---------------- */
  const OPS = ["", "LOAD", "STORE", "ADD", "SUB", "JMP", "JZ", "JN", "OUT", "HALT"];
  function cpuprog(c) {
    const p = c.spec, N = p.lines || 8, rows = (p.start || []).concat(Array(N).fill(null)).slice(0, N).map(x => x ? { op: x[0], a: x[1] || 0 } : { op: "", a: 0 }); let won = false, runs = 0;
    const data = p.data || {};
    c.play.innerHTML = `<p class="ws-task">${p.task}</p><div class="ws-cpu"><div><table class="ws-code"><tr><th>Addr</th><th>Instruction</th><th>Address</th></tr>${rows.map((r, i) => `<tr><td>${i}</td><td><select data-i="${i}" data-f="op">${OPS.map(o => `<option ${o === r.op ? "selected" : ""}>${o}</option>`).join("")}</select></td><td><select data-i="${i}" data-f="a">${Array.from({ length: 16 }, (_, k) => `<option ${k === r.a ? "selected" : ""}>${k}</option>`).join("")}</select></td></tr>`).join("")}</table></div>
      <div><table class="ws-data"><tr><th>Addr</th><th>Data</th></tr>${Object.entries(data).map(([a, v]) => `<tr><td>${a}</td><td>${v}</td></tr>`).join("")}</table><p class="ws-tip">Target output: <b>${p.target.join(", ")}</b></p><div class="ws-ref">LOAD a: ACC ← M[a] · STORE a: M[a] ← ACC · ADD/SUB a · JMP a · JZ a (if ACC = 0) · JN a (if ACC &lt; 0) · OUT · HALT</div></div></div>
      <div class="mg-ctl">${B("run", "Run program ▸", "solid")}${B("clear", "Clear")}</div><div class="ws-trace"></div>`;
    const tr = c.play.querySelector(".ws-trace");
    c.play.addEventListener("change", e => { const s = e.target.closest("select[data-i]"); if (!s) return; const r = rows[+s.dataset.i]; if (s.dataset.f === "op") r.op = s.value; else r.a = +s.value; });
    function run() {
      runs++; const M = new Array(16).fill(0); Object.entries(data).forEach(([a, v]) => M[+a] = v);
      let pc = 0, acc = 0, out = [], steps = 0, log = [], why = "";
      const s8 = x => ((x + 128) & 255) - 128;
      while (steps++ < 400) {
        if (pc >= N) { why = "ran off the end of the program (add a HALT)"; break; }
        if (Object.prototype.hasOwnProperty.call(data, pc) && !rows[pc].op) { why = "ran into data"; break; }
        const { op, a } = rows[pc]; if (log.length < 60) log.push(`${pc}: ${op || "(empty)"}${["", "OUT", "HALT"].includes(op) ? "" : " " + a}`); pc++;
        if (op === "" || op === "HALT") { why = op ? "" : "hit an empty line (treated as HALT)"; break; }
        if (op === "LOAD") acc = M[a]; else if (op === "STORE") M[a] = acc; else if (op === "ADD") acc = s8(acc + M[a]); else if (op === "SUB") acc = s8(acc - M[a]);
        else if (op === "JMP") pc = a; else if (op === "JZ") { if (acc === 0) pc = a; } else if (op === "JN") { if (acc < 0) pc = a; } else if (op === "OUT") out.push(acc);
        if (out.length > 30) { why = "too many outputs"; break; }
      }
      if (steps >= 400) why = "stopped after 400 steps (infinite loop?)";
      const used = rows.filter(r => r.op).length, ok = out.length === p.target.length && out.every((x, i) => x === p.target[i]);
      tr.innerHTML = `<div class="ws-outrow">Output: <b>${out.length ? out.join(", ") : "(nothing)"}</b> ${ok ? "✓" : ""}${why ? ` · <span class="no">${why}</span>` : ""}</div><details><summary>Execution trace (${Math.min(steps, 400)} steps)</summary><code>${log.map(esc).join("<br>")}${log.length >= 60 ? "<br>…" : ""}</code></details>`;
      if (ok && !won) { won = true; c.done(used <= p.par ? 3 : used <= p.par + 2 ? 2 : 1, `You used <b>${used}</b> instructions (par is ${p.par}). ${p.win || ""}`); } else if (!ok) c.say("Not the target output yet. Check the trace to see what happened.", "miss");
    }
    c.play.addEventListener("click", e => { const a = e.target.closest("[data-act]"); if (!a) return; if (a.dataset.act === "run") run(); if (a.dataset.act === "clear") { rows.forEach(r => { r.op = ""; r.a = 0; }); c.play.querySelectorAll("select").forEach(s => s.selectedIndex = 0); tr.innerHTML = ""; } });
  }

  /* ---------------- ML: draw the boundary yourself ---------------- */
  function boundary(c) {
    const p = c.spec, X = window.XLabs, data = X.makeData(p.set || "blobs", p.seed || 3, p.n || 60); let h = [[.25, .2], [.75, .85]], dragging = -1, won = false, moves = 0;
    c.play.innerHTML = `<p class="ws-task">${p.task || "Drag the two white handles to place a straight line that separates the classes."}</p>`;
    const st = canvas(c.play, 420, 420); st.cv.style.touchAction = "none"; st.cv.parentNode.style.maxWidth = "480px"; st.cv.parentNode.style.margin = "0 auto";
    c.play.insertAdjacentHTML("beforeend", `<div class="mg-read ws-rd" style="justify-content:center"></div>`);
    const rd = c.play.querySelector(".ws-rd");
    function side(a, b) { const [p1, p2] = h; return Math.sign((p2[0] - p1[0]) * (b - p1[1]) - (p2[1] - p1[1]) * (a - p1[0])); }
    function draw() {
      const cx = st.c; let accA = 0; data.forEach(([a, b, y]) => { if ((side(a, b) > 0 ? 1 : 0) === y) accA++; }); const flip = accA < data.length - accA, acc = Math.max(accA, data.length - accA) / data.length;
      const N = 42, cw = st.W / N; for (let i = 0; i < N; i++) for (let j = 0; j < N; j++) { let k = side((i + .5) / N, 1 - (j + .5) / N) > 0 ? 1 : 0; if (flip) k = 1 - k; cx.fillStyle = k ? "#FDE2D2" : "#DBE6FD"; cx.fillRect(Math.floor(i * cw), Math.floor(j * cw), Math.ceil(cw) + 1, Math.ceil(cw) + 1); }
      data.forEach(([a, b, y]) => { let k = side(a, b) > 0 ? 1 : 0; if (flip) k = 1 - k; X.dot(cx, a * st.W, (1 - b) * st.H, 5.5, y ? "#EA580C" : "#2563EB", k === y ? "#fff" : "#111", k === y ? 1.5 : 2.6); });
      const [p1, p2] = h, dx = p2[0] - p1[0], dy = p2[1] - p1[1]; cx.strokeStyle = "#111827"; cx.lineWidth = 3; cx.beginPath(); cx.moveTo((p1[0] - dx * 5) * st.W, (1 - (p1[1] - dy * 5)) * st.H); cx.lineTo((p1[0] + dx * 5) * st.W, (1 - (p1[1] + dy * 5)) * st.H); cx.stroke();
      h.forEach(q => X.dot(cx, q[0] * st.W, (1 - q[1]) * st.H, 10, "#fff", "#111827", 3));
      rd.innerHTML = `<span>Accuracy <b>${Math.round(acc * 100)}%</b></span><span>goal <b>${Math.round(p.target * 100)}%</b></span>`;
      if (acc >= p.target && !won && moves) { won = true; c.done(3, p.win || ""); }
    }
    const near = (x, y) => h.findIndex(q => Math.hypot(q[0] * st.W - x, (1 - q[1]) * st.H - y) < 22);
    st.cv.addEventListener("pointerdown", e => { const [x, y] = st.pos(e); dragging = near(x, y); if (dragging >= 0) st.cv.setPointerCapture(e.pointerId); });
    st.cv.addEventListener("pointermove", e => { const [x, y] = st.pos(e); if (dragging < 0) { st.cv.style.cursor = near(x, y) >= 0 ? "grab" : "default"; return; } h[dragging] = [Math.max(0, Math.min(1, x / st.W)), Math.max(0, Math.min(1, 1 - y / st.H))]; moves++; draw(); });
    st.cv.addEventListener("pointerup", () => dragging = -1);
    draw();
  }

  /* ---------------- any interactive lab with a goal ---------------- */
  function lab(c) {
    const p = c.spec;
    c.play.innerHTML = `<p class="ws-task">${p.task}</p><div class="ws-live"></div><div class="xlab" data-lab='${JSON.stringify(p.lab).replace(/'/g, "&#39;")}'></div>`;
    const live = c.play.querySelector(".ws-live"); let won = false, fn = null, t0 = performance.now();
    c.play.addEventListener("labstate", e => {
      const d = e.detail; if (!fn) fn = Function(...Object.keys(d), "return (" + p.goal + ");");
      let ok = false; try { ok = !!fn(...Object.keys(d).map(k => d[k])); } catch (x) { }
      live.innerHTML = (p.show || []).map(([lab, k, kind]) => { let v = d[k]; v = kind === "pct" ? Math.round(v * 100) + "%" : typeof v === "number" ? fm(v, 3) : esc(String(v)); return `<span>${lab} <b>${v}</b></span>`; }).join("") + `<span class="ws-goal ${ok ? "ok" : ""}">${ok ? "✓ goal reached" : "goal: " + (p.need || "")}</span>`;
      if (ok && !won && performance.now() - t0 > 300) { won = true; c.done(3, p.win || ""); }
    });
    window.XLabs && window.XLabs.boot();
  }

  /* ---------------- French: conjugation sprint ---------------- */
  const TN = { pres: "présent", pc: "passé composé", impf: "imparfait", fut: "futur simple", cond: "conditionnel", subj: "subjonctif", fp: "futur proche" };
  const PRN = ["je", "tu", "il / elle", "nous", "vous", "ils / elles"];
  const ACCENTS = ["é", "è", "ê", "à", "â", "ç", "î", "ï", "ô", "û", "ù", "ë"];
  function accentBar(inp) { const d = document.createElement("div"); d.className = "ws-acc"; d.innerHTML = ACCENTS.map(a => `<button type="button" tabindex="-1">${a}</button>`).join(""); d.onmousedown = e => e.preventDefault(); d.onclick = e => { const b = e.target.closest("button"); if (!b) return; const s = inp.selectionStart ?? inp.value.length; inp.value = inp.value.slice(0, s) + b.textContent + inp.value.slice(inp.selectionEnd ?? s); inp.focus(); inp.setSelectionRange(s + 1, s + 1); }; return d; }
  const stripPron = f => f.replace(/^(que |qu')/i, "").replace(/^(je |j'|tu |il |elle |on |nous |vous |ils |elles )/i, "");
  function conj(c) {
    const p = c.spec; if (!window.FR || !window.FR.conj) { c.play.textContent = "The verb engine didn't load."; return; }
    let qs, i, score, t0;
    function gen() { const out = [], seen = new Set(); let guard = 0; while (out.length < p.n && guard++ < 500) { const v = pick(p.verbs), t = pick(p.tenses), k = Math.floor(Math.random() * 6), key = v + t + k; if (seen.has(key)) continue; seen.add(key); const F = window.FR.conj(v, t); if (!F || !F[k]) continue; out.push({ v, t, k, full: F[k] }); } return out; }
    function intro() { c.play.innerHTML = `<div class="ws-sprint0"><div class="ws-big">${p.n} verbs · ${p.tenses.map(t => TN[t]).join(", ")}</div><p>Type the verb form (with or without the subject). Accent buttons are below the box. Pass with ${p.pass}.</p>${B("go", "Commencer ▸", "solid")}</div>`; }
    function show() {
      const q = qs[i];
      c.play.innerHTML = `<div class="ws-qn">${i + 1} / ${qs.length}<span class="ws-score">${fm(score, 1)} pts</span></div><div class="ws-bar"><i style="width:${i / qs.length * 100}%"></i></div>
        <div class="ws-cj"><span class="ws-pron">${PRN[q.k]}</span><span class="ws-verb" lang="fr">${esc(q.v)}</span><span class="ws-tense">${TN[q.t]}</span></div>
        <div class="mg-ctl"><input class="ws-ans" lang="fr" type="text" autocomplete="off" spellcheck="false" autocapitalize="off" placeholder="${PRN[q.k].split(" ")[0]} …">${B("check", "Check", "solid")}</div><div class="ws-fb"></div>`;
      const inp = c.play.querySelector(".ws-ans"); inp.after(accentBar(inp)); inp.focus({ preventScroll: true }); inp.onkeydown = e => { if (e.key === "Enter") { const nb = c.play.querySelector('[data-act="next"]'); nb ? nb.click() : check(inp.value); } };
    }
    function check(v) {
      const q = qs[i], fb = c.play.querySelector(".ws-fb"), u = norm(v).toLowerCase(); if (!u) return;
      const full = norm(q.full).toLowerCase(), bare = stripPron(full);
      const rx = f => new RegExp("^" + f.split(/(\([^)]*\))/).map(x => x.startsWith("(") ? "(?:" + x.slice(1, -1).replace(/[.*+?^${}|[\]\\]/g, "\\$&") + ")?" : x.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")).join("") + "$");
      const fits = (a, b) => rx(b).test(a) || rx(stripPron(b)).test(stripPron(a));
      const exact = fits(u, full), close = !exact && fits(deacc(u), deacc(full));
      if (exact) score += 1; else if (close) score += .5;
      fb.className = "ws-fb " + (exact ? "ok" : close ? "half" : "no");
      fb.innerHTML = `${exact ? "<b>Exact!</b>" : close ? "<b>Almost — check the accents:</b>" : "<b>Not quite:</b>"} <span lang="fr" class="fr-ans">${esc(q.full)}</span> <button type="button" class="mg-b sm" data-act="say">🔊</button> ${B("next", i + 1 < qs.length ? "Next →" : "Finish", "solid sm")}`;
      c.play.querySelector('[data-act="check"]').disabled = true; c.play.querySelector(".ws-ans").readOnly = true;
      if (window.FR.say && p.audio !== false) try { window.FR.say(q.full); } catch (e) { }
    }
    function end() { const r = score / qs.length, s = (performance.now() - t0) / 1000;
      if (score >= p.pass) { c.play.innerHTML = `<div class="ws-res"><b>${fm(score, 1)} / ${qs.length}</b> in ${s.toFixed(0)} s</div>`; c.done(r >= .95 ? 3 : r >= .8 ? 2 : 1, p.win || ""); }
      else c.play.innerHTML = `<div class="ws-res"><b>${fm(score, 1)} / ${qs.length}</b> — you need ${p.pass}.</div><div class="mg-ctl">${B("go", "Try again", "solid")}</div>`; }
    c.play.addEventListener("click", e => { const a = e.target.closest("[data-act]"); if (!a) return; const k = a.dataset.act;
      if (k === "go") { qs = gen(); i = 0; score = 0; t0 = performance.now(); show(); }
      if (k === "check") check(c.play.querySelector(".ws-ans").value);
      if (k === "say") window.FR.say(qs[i].full);
      if (k === "next") { i++; i < qs.length ? show() : end(); } });
    intro();
  }

  /* ---------------- French: listening ---------------- */
  function frWords(p) { const d = (window.DECKS || []).find(x => x.id === "fr-words"); if (!d) return []; return d.cards.slice(p.from || 0, p.to || 300).filter(c => c.f && c.b && c.f.length < 22); }
  function listen(c) {
    const p = c.spec, pool = frWords(p); let qs, i, score; const tts = "speechSynthesis" in window;
    if (!pool.length) { c.play.textContent = "Word list didn't load."; return; }
    function intro() { c.play.innerHTML = `<div class="ws-sprint0"><div class="ws-big">${p.mode === "dictee" ? "Dictée" : "Listen and choose"} · ${p.n} words</div><p>${p.mode === "dictee" ? "Listen, then type the French word you hear." : "Listen to the French word and pick its meaning."}${tts ? "" : " (Your browser can't speak, so the word is shown in writing instead.)"}</p>${B("go", "Commencer ▸", "solid")}</div>`; }
    function show() {
      const q = qs[i];
      c.play.innerHTML = `<div class="ws-qn">${i + 1} / ${qs.length}<span class="ws-score">${fm(score, 1)} pts</span></div><div class="ws-bar"><i style="width:${i / qs.length * 100}%"></i></div>
        <div class="ws-hear">${B("say", "🔊 Play again")}${tts ? "" : `<span class="ws-verb" lang="fr">${esc(q.f)}</span>`}${p.mode === "dictee" ? `<small>meaning: ${esc(q.b)}</small>` : ""}</div>
        ${p.mode === "dictee" ? `<div class="mg-ctl"><input class="ws-ans" lang="fr" type="text" autocomplete="off" spellcheck="false" autocapitalize="off" placeholder="type what you hear">${B("check", "Check", "solid")}</div>` : `<div class="ws-opts">${q.opts.map((o, k) => `<button type="button" class="ws-opt" data-k="${k}">${esc(o)}</button>`).join("")}</div>`}<div class="ws-fb"></div>`;
      const inp = c.play.querySelector(".ws-ans"); if (inp) { inp.after(accentBar(inp)); inp.focus({ preventScroll: true }); inp.onkeydown = e => { if (e.key === "Enter") { const nb = c.play.querySelector('[data-act="next"]'); nb ? nb.click() : check(inp.value); } }; }
      setTimeout(() => tts && window.FR && window.FR.say(q.f), 250);
    }
    function check(v) {
      const q = qs[i], fb = c.play.querySelector(".ws-fb"); let ok, half = false;
      if (p.mode === "dictee") { const u = norm(v).toLowerCase(), a = norm(q.f).toLowerCase().replace(/^(le |la |les |l'|un |une )/, ""), u2 = u.replace(/^(le |la |les |l'|un |une )/, ""); ok = u2 === a; half = !ok && deacc(u2) === deacc(a); }
      else { ok = +v === q.a; c.play.querySelectorAll(".ws-opt").forEach(b => { b.disabled = true; if (+b.dataset.k === q.a) b.classList.add("ok"); else if (b.dataset.k === String(v)) b.classList.add("no"); }); }
      score += ok ? 1 : half ? .5 : 0;
      fb.className = "ws-fb " + (ok ? "ok" : half ? "half" : "no"); fb.innerHTML = `${ok ? "<b>Oui !</b>" : half ? "<b>Almost — accents:</b>" : "<b>Non :</b>"} <span lang="fr" class="fr-ans">${esc(q.f)}</span> = ${esc(q.b)} ${B("next", i + 1 < qs.length ? "Next →" : "Finish", "solid sm")}`;
      const cb = c.play.querySelector('[data-act="check"]'); if (cb) cb.disabled = true;
    }
    function end() { const r = score / qs.length; if (r >= (p.pass ?? .7)) { c.play.innerHTML = `<div class="ws-res"><b>${fm(score, 1)} / ${qs.length}</b></div>`; c.done(r >= .95 ? 3 : r >= .8 ? 2 : 1, p.win || ""); } else c.play.innerHTML = `<div class="ws-res"><b>${fm(score, 1)} / ${qs.length}</b> — you need ${Math.ceil((p.pass ?? .7) * qs.length)}.</div><div class="mg-ctl">${B("go", "Try again", "solid")}</div>`; }
    c.play.addEventListener("click", e => {
      const o = e.target.closest(".ws-opt"); if (o && !o.disabled) { check(o.dataset.k); return; }
      const a = e.target.closest("[data-act]"); if (!a) return; const k = a.dataset.act;
      if (k === "go") { qs = shuffle(pool).slice(0, p.n).map(w => { const opts = shuffle([w.b, ...shuffle(pool.filter(x => x.b !== w.b)).slice(0, 3).map(x => x.b)]); return { f: w.f, b: w.b, opts, a: opts.indexOf(w.b) }; }); i = 0; score = 0; show(); }
      if (k === "say" && window.FR) window.FR.say(qs[i].f);
      if (k === "check") check(c.play.querySelector(".ws-ans").value);
      if (k === "next") { i++; i < qs.length ? show() : end(); }
    });
    intro();
  }

  /* ---------------- French: memory pairs ---------------- */
  function pairs(c) {
    const p = c.spec, pool = frWords(p); let cards, open = [], matched = 0, moves = 0, lock = false, won = false;
    function deal() { const ws = shuffle(pool).slice(0, p.n || 6); cards = shuffle(ws.flatMap((w, i) => [{ id: i, t: w.f, fr: true }, { id: i, t: w.b, fr: false }])); open = []; matched = 0; moves = 0; won = false; draw(); }
    function draw() {
      c.play.innerHTML = `<div class="ws-qn">Pairs found ${matched} / ${cards.length / 2}<span class="ws-score">${moves} moves</span></div><div class="ws-mem">${cards.map((cd, k) => `<button type="button" class="ws-card ${cd.done ? "done" : ""} ${open.includes(k) || cd.done ? "up" : ""} ${cd.fr ? "fr" : "en"}" data-k="${k}" ${cd.done ? "disabled" : ""}><span class="b">?</span><span class="f" ${cd.fr ? 'lang="fr"' : ""}>${esc(cd.t)}</span></button>`).join("")}</div><div class="mg-ctl">${B("deal", "New cards")}</div>`;
    }
    c.play.addEventListener("click", e => {
      if (e.target.closest('[data-act="deal"]')) { deal(); return; }
      const b = e.target.closest(".ws-card"); if (!b || lock) return; const k = +b.dataset.k; if (open.includes(k) || cards[k].done) return;
      open.push(k); if (cards[k].fr && window.FR) try { window.FR.say(cards[k].t); } catch (x) { }
      if (open.length === 2) { moves++; const [a, d] = open.map(x => cards[x]);
        if (a.id === d.id && a.fr !== d.fr) { a.done = d.done = true; matched++; open = []; draw(); if (matched === cards.length / 2 && !won) { won = true; const n = cards.length / 2; c.done(moves <= n + 3 ? 3 : moves <= n * 2 ? 2 : 1, `${moves} moves. ${p.win || ""}`); } return; }
        draw(); lock = true; setTimeout(() => { open = []; lock = false; draw(); }, still() ? 400 : 1000); return; }
      draw();
    });
    deal();
  }

  const GAMES = { launch, collide, calc, sprint, match, parsons, bits, gates, cpuprog, boundary, lab, conj, listen, pairs };
  function boot() { missions.forEach(setup); meter(); }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot); else boot();
})();
