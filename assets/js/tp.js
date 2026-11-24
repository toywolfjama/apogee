/* ===== Apogee: test-prep widgets (SAT / ACT) =====
   .tp[data-hl]   evidence highlighter: click the sentence that proves the claim
   .tp[data-pace] pacing clock for a timed module
*/
(function () {
  const reduce = () => matchMedia("(prefers-reduced-motion: reduce)").matches || document.body.classList.contains("no-motion");
  const esc = s => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;");

  function hl(el, p) {
    let k = 0;
    const items = p.items;
    function show() {
      const it = items[k], want = [].concat(it.a);
      el.innerHTML = `<div class="tp-h">${esc(p.title || "Find the evidence")} <span>${esc(p.sub || "Click the sentence that best supports the claim.")}</span></div>
        <div class="tp-claim">${it.claim}</div>
        <div class="tp-sents">${it.sents.map((s, i) => `<span data-i="${i}" tabindex="0" role="button">${s}</span>`).join(" ")}</div>
        <div class="tp-fb" aria-live="polite"></div>
        <div class="mg-ctl">${items.length > 1 ? `<span class="tp-n">${k + 1} / ${items.length}</span>` : ""}<button class="mg-b tp-reset">Try again</button>${items.length > 1 ? `<button class="mg-b tp-next">Next passage →</button>` : ""}</div>`;
      let done = false;
      const fb = el.querySelector(".tp-fb");
      const pick = sp => {
        if (done) return;
        const i = +sp.dataset.i;
        if (want.includes(i)) {
          done = true; sp.classList.add("hit");
          fb.innerHTML = `<b class="g">Yes.</b> ${it.x}`;
        } else {
          sp.classList.remove("miss"); void sp.offsetWidth; sp.classList.add("miss");
          fb.innerHTML = `<b class="r">Not quite.</b> ${(it.why && it.why[i]) || "That sentence is related, but it doesn't prove the claim. Look for the one that states it directly."}`;
        }
      };
      el.querySelectorAll(".tp-sents span").forEach(sp => { sp.onclick = () => pick(sp); sp.onkeydown = e => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); pick(sp); } }; });
      el.querySelector(".tp-reset").onclick = show;
      const nx = el.querySelector(".tp-next"); if (nx) nx.onclick = () => { k = (k + 1) % items.length; show(); };
    }
    show();
  }

  function pace(el, p) {
    const mods = p.modules; let m = 0, t = 0, raf = null;
    el.innerHTML = `<div class="tp-h">${esc(p.title || "Pacing clock")} <span>${esc(p.sub || "Where should you be when the clock says this?")}</span></div>
      <div class="pace-ctl"><select aria-label="Section">${mods.map((x, i) => `<option value="${i}">${esc(x[0])} · ${x[1]} questions · ${x[2]} min</option>`).join("")}</select>
      <button class="mg-b pace-play">▶ Run the clock</button></div>
      <label class="mg-sl" style="margin-top:10px"><span style="display:flex;gap:10px;align-items:center;font-weight:600">Minutes used <input type="range" min="0" max="100" step="0.5" value="0" class="pace-t"><b class="pace-tv">0</b></span></label>
      <div class="pace">
        <div class="pace-row"><span>Time used</span><div class="pace-bar"><div class="pace-ticks"></div><i class="pb-t"></i></div><span class="pb-tl"></span></div>
        <div class="pace-row"><span>Be on question</span><div class="pace-bar"><div class="pace-ticks"></div><i class="pb-q" style="background:linear-gradient(90deg,#F5B700,#FCD34D)"></i></div><span class="pb-ql"></span></div>
      </div>
      <p class="pace-out"></p>`;
    const sel = el.querySelector("select"), rng = el.querySelector(".pace-t"), play = el.querySelector(".pace-play");
    function draw() {
      const [name, n, min, note] = mods[m], f = Math.min(1, t / min), q = Math.min(n, Math.floor(f * n * 1.08) + 1);
      rng.max = min; el.querySelector(".pace-tv").textContent = t.toFixed(1);
      el.querySelector(".pb-t").style.width = f * 100 + "%"; el.querySelector(".pb-tl").textContent = `${t.toFixed(0)}/${min}m`;
      el.querySelector(".pb-q").style.width = (q / n) * 100 + "%"; el.querySelector(".pb-ql").textContent = `Q${q}/${n}`;
      const sec = Math.round(min * 60 / n);
      el.querySelector(".pace-out").innerHTML = `<b>${name}:</b> about <b>${sec} seconds</b> per question. ${f >= 1 ? "Time's up: every question should have an answer, even a guess." : f > 0.9 ? "Final minutes: fill in every blank. There's no penalty for guessing." : `Aim to have about <b>${Math.max(0, q - 1)}</b> done, leaving ~${Math.round(min * 0.08)} minutes at the end to revisit flagged ones.`} ${note || ""}`;
    }
    sel.onchange = () => { m = +sel.value; t = 0; rng.value = 0; draw(); };
    rng.oninput = () => { t = +rng.value; draw(); };
    play.onclick = () => {
      if (raf) { cancelAnimationFrame(raf); raf = null; play.textContent = "▶ Run the clock"; return; }
      const min = mods[m][2]; if (t >= min) t = 0;
      if (reduce()) { t = min; draw(); return; }
      play.textContent = "❚❚ Pause"; let last = performance.now();
      (function f(now) { t = Math.min(min, t + (now - last) / 1000 * (min / 8)); last = now; rng.value = t; draw(); if (t < min) raf = requestAnimationFrame(f); else { raf = null; play.textContent = "▶ Run the clock"; } })(last);
    };
    draw();
  }


  /* ---------- regression lab: what Desmos's y1 ~ ... does ---------- */
  function solve3(A, b) { // Gaussian elimination, 3x3
    const M = A.map((r, i) => [...r, b[i]]);
    for (let c = 0; c < 3; c++) {
      let p = c; for (let r = c + 1; r < 3; r++) if (Math.abs(M[r][c]) > Math.abs(M[p][c])) p = r;
      [M[c], M[p]] = [M[p], M[c]]; if (Math.abs(M[c][c]) < 1e-12) return null;
      for (let r = 0; r < 3; r++) if (r !== c) { const f = M[r][c] / M[c][c]; for (let k = c; k < 4; k++) M[r][k] -= f * M[c][k]; }
    }
    return [0, 1, 2].map(i => M[i][3] / M[i][i]);
  }
  function fit(pts, model) {
    const n = pts.length; if (n < 2) return null;
    const X = pts.map(p => p[0]), Y = pts.map(p => p[1]), sum = a => a.reduce((s, v) => s + v, 0);
    let f, par, txt;
    if (model === "lin") {
      const sx = sum(X), sy = sum(Y), sxx = sum(X.map(x => x * x)), sxy = sum(X.map((x, i) => x * Y[i])), d = n * sxx - sx * sx;
      if (Math.abs(d) < 1e-12) return null;
      const m = (n * sxy - sx * sy) / d, b = (sy - m * sx) / n; f = x => m * x + b; par = [["m", m], ["b", b]]; txt = "y₁ ~ m·x₁ + b";
    } else if (model === "quad") {
      if (n < 3) return null;
      const S = k => sum(X.map(x => x ** k)), T = k => sum(X.map((x, i) => x ** k * Y[i]));
      const r = solve3([[S(4), S(3), S(2)], [S(3), S(2), S(1)], [S(2), S(1), n]], [T(2), T(1), T(0)]); if (!r) return null;
      const [a, b, c] = r; f = x => a * x * x + b * x + c; par = [["a", a], ["b", b], ["c", c]]; txt = "y₁ ~ a·x₁² + b·x₁ + c";
    } else {
      if (Y.some(y => y <= 0)) return { err: "Exponential fits need all y-values above 0." };
      const L = pts.map(p => [p[0], Math.log(p[1])]), l = fit(L, "lin"); if (!l) return null;
      const a = Math.exp(l.par[1][1]), b = Math.exp(l.par[0][1]); f = x => a * b ** x; par = [["a", a], ["b", b]]; txt = "y₁ ~ a·b^x₁";
    }
    const my = sum(Y) / n, ssr = sum(Y.map((y, i) => (y - f(X[i])) ** 2)), sst = sum(Y.map(y => (y - my) ** 2));
    return { f, par, txt, r2: sst ? 1 - ssr / sst : 1 };
  }
  const nf = v => { if (!isFinite(v)) return "—"; const r = Math.round(v * 1000) / 1000; return (Object.is(r, -0) ? 0 : r).toString().replace("-", "−"); };
  function pretty(model, v) {
    const co = (c, t, first) => { const r = Math.round(c * 1000) / 1000; if (r === 0) return ""; const sgn = r < 0 ? (first ? "−" : " − ") : (first ? "" : " + "); const a = Math.abs(r); return sgn + (t && a === 1 ? "" : nf(a)) + t; };
    if (model === "lin") return "y = " + ((co(v[0], "x", true) + co(v[1], "", !co(v[0], "x", true))) || "0");
    if (model === "quad") { let s = co(v[0], "x²", true); s += co(v[1], "x", !s); s += co(v[2], "", !s); return "y = " + (s || "0"); }
    return `y = ${nf(v[0])}·(${nf(v[1])})ˣ`;
  }
  function reg(el, p) {
    let pts = p.points.map(x => x.slice()), model = p.model || "lin";
    el.innerHTML = `<div class="tp-h">${esc(p.title || "Regression lab")} <span>${esc(p.sub || "Edit the table or drag points. This is exactly what Desmos does when you type y₁ ~ …")}</span></div>
      <div class="rg-wrap"><div class="rg-left"><table class="rg-t"><thead><tr><th>x₁</th><th>y₁</th><th></th></tr></thead><tbody></tbody></table>
      <button class="mg-b sm rg-add">+ row</button>
      <div class="rg-models">${[["lin", "Linear"], ["quad", "Quadratic"], ["exp", "Exponential"]].map(([k, l]) => `<button class="mg-b sm${k === model ? " on" : ""}" data-m="${k}">${l}</button>`).join("")}</div>
      ${p.presets ? `<div class="rg-pre">${p.presets.map((x, i) => `<button class="mg-b sm" data-p="${i}">${esc(x.name)}</button>`).join("")}</div>` : ""}</div>
      <div class="rg-right"><canvas width="560" height="340"></canvas><div class="rg-out"></div></div></div>`;
    const tb = el.querySelector("tbody"), cv = el.querySelector("canvas"), out = el.querySelector(".rg-out");
    let view, drag = -1;
    function table() {
      tb.innerHTML = pts.map((q, i) => `<tr><td><input value="${q[0]}" data-i="${i}" data-k="0" inputmode="decimal"></td><td><input value="${q[1]}" data-i="${i}" data-k="1" inputmode="decimal"></td><td><button class="rg-x" data-i="${i}" aria-label="Remove row">×</button></td></tr>`).join("");
      tb.querySelectorAll("input").forEach(inp => inp.oninput = () => { const v = parseFloat(inp.value.replace("−", "-")); if (isFinite(v)) { pts[+inp.dataset.i][+inp.dataset.k] = v; draw(false); } });
      tb.querySelectorAll(".rg-x").forEach(b => b.onclick = () => { pts.splice(+b.dataset.i, 1); table(); draw(true); });
    }
    function draw(rescale) {
      const dpr = Math.min(2, devicePixelRatio || 1), W = 560, H = 340; cv.width = W * dpr; cv.height = H * dpr;
      const c = cv.getContext("2d"); c.setTransform(dpr, 0, 0, dpr, 0, 0); c.clearRect(0, 0, W, H);
      if (rescale || !view) {
        const xs = pts.map(q => q[0]), ys = pts.map(q => q[1]);
        let x0 = Math.min(0, ...xs), x1 = Math.max(...xs), y0 = Math.min(0, ...ys), y1 = Math.max(...ys);
        const px = (x1 - x0) * 0.15 || 1, py = (y1 - y0) * 0.15 || 1; view = [x0 - px, x1 + px, y0 - py, y1 + py];
      }
      const [x0, x1, y0, y1] = view, X = x => 40 + (x - x0) / (x1 - x0) * (W - 56), Y = y => H - 28 - (y - y0) / (y1 - y0) * (H - 44);
      el._inv = [x => x0 + (x - 40) / (W - 56) * (x1 - x0), y => y0 + (H - 28 - y) / (H - 44) * (y1 - y0), X, Y];
      c.strokeStyle = "#E5E7EB"; c.lineWidth = 1; const step = (a, b) => { const r = (b - a) / 8, m = 10 ** Math.floor(Math.log10(r)); return [1, 2, 5, 10].map(k => k * m).find(k => k >= r); };
      const sx = step(x0, x1), sy = step(y0, y1); c.fillStyle = "#6B7280"; c.font = "11px JetBrains Mono, monospace"; c.textAlign = "center";
      for (let x = Math.ceil(x0 / sx) * sx; x <= x1; x += sx) { c.beginPath(); c.moveTo(X(x), 16); c.lineTo(X(x), H - 28); c.stroke(); c.fillText(nf(x), X(x), H - 12); }
      c.textAlign = "right"; for (let y = Math.ceil(y0 / sy) * sy; y <= y1; y += sy) { c.beginPath(); c.moveTo(40, Y(y)); c.lineTo(W - 16, Y(y)); c.stroke(); c.fillText(nf(y), 34, Y(y) + 4); }
      c.strokeStyle = "#374151"; c.lineWidth = 1.4; if (y0 < 0 && y1 > 0) { c.beginPath(); c.moveTo(40, Y(0)); c.lineTo(W - 16, Y(0)); c.stroke(); } if (x0 < 0 && x1 > 0) { c.beginPath(); c.moveTo(X(0), 16); c.lineTo(X(0), H - 28); c.stroke(); }
      const F = fit(pts, model);
      if (F && F.f) { c.strokeStyle = "#2563EB"; c.lineWidth = 3; c.beginPath(); let first = true; for (let k = 0; k <= 200; k++) { const x = x0 + (x1 - x0) * k / 200, y = F.f(x); if (!isFinite(y) || y < y0 - (y1 - y0) || y > y1 + (y1 - y0)) { first = true; continue; } first ? c.moveTo(X(x), Y(y)) : c.lineTo(X(x), Y(y)); first = false; } c.stroke(); }
      pts.forEach(q => { c.beginPath(); c.arc(X(q[0]), Y(q[1]), 6.5, 0, 7); c.fillStyle = "#EA580C"; c.fill(); c.strokeStyle = "#fff"; c.lineWidth = 2; c.stroke(); });
      out.innerHTML = !F ? "Add more points for this model." : F.err ? F.err : `<code>${F.txt}</code><div class="rg-par">${F.par.map(([k, v]) => `<span>${k} = <b>${nf(v)}</b></span>`).join("")}<span>r² = <b>${nf(F.r2)}</b></span></div><div class="rg-eq">${pretty(model, F.par.map(q => q[1]))}</div>${F.r2 > 0.99999 ? '<div class="rg-ok">r² = 1: the model passes through every point exactly. On the test, that means you\'ve found THE equation.</div>' : ""}`;
    }
    const pos = e => { const r = cv.getBoundingClientRect(); return [(e.clientX - r.left) * 560 / r.width, (e.clientY - r.top) * 340 / r.height]; };
    cv.addEventListener("pointerdown", e => { const [mx, my] = pos(e), [, , X, Y] = el._inv; drag = pts.findIndex(q => Math.hypot(X(q[0]) - mx, Y(q[1]) - my) < 12); if (drag >= 0) cv.setPointerCapture(e.pointerId); });
    cv.addEventListener("pointermove", e => { if (drag < 0) return; const [mx, my] = pos(e), [ix, iy] = el._inv; pts[drag] = [Math.round(ix(mx) * 10) / 10, Math.round(iy(my) * 10) / 10]; const ins = tb.querySelectorAll("tr")[drag].querySelectorAll("input"); ins[0].value = pts[drag][0]; ins[1].value = pts[drag][1]; draw(false); });
    cv.addEventListener("pointerup", () => { drag = -1; });
    el.querySelector(".rg-add").onclick = () => { const l = pts[pts.length - 1] || [0, 0]; pts.push([l[0] + 1, l[1]]); table(); draw(true); };
    el.querySelectorAll("[data-m]").forEach(b => b.onclick = () => { model = b.dataset.m; el.querySelectorAll("[data-m]").forEach(x => x.classList.toggle("on", x === b)); draw(false); });
    el.querySelectorAll("[data-p]").forEach(b => b.onclick = () => { const pr = p.presets[+b.dataset.p]; pts = pr.points.map(x => x.slice()); model = pr.model; el.querySelectorAll("[data-m]").forEach(x => x.classList.toggle("on", x.dataset.m === model)); table(); draw(true); });
    table(); draw(true);
  }

  /* ---------- copy-to-clipboard chips for Desmos input ---------- */
  function chips() {
    document.querySelectorAll("code.dz:not([data-mounted])").forEach(c => {
      c.dataset.mounted = 1; c.title = "Click to copy"; c.tabIndex = 0;
      const go = () => { const t = c.dataset.copy || c.textContent; (navigator.clipboard ? navigator.clipboard.writeText(t) : Promise.reject()).then(() => { c.classList.add("ok"); setTimeout(() => c.classList.remove("ok"), 900); }).catch(() => {}); if (window.__dzOpen) window.__dzOpen(); };
      c.onclick = go; c.onkeydown = e => { if (e.key === "Enter") go(); };
    });
  }

  /* ---------- Desmos drawer: the real calculator, embedded ---------- */
  function drawer() {
    const b = document.body;
    const want = b.classList.contains("th-exam") || b.dataset.course === "math";
    if (!want || document.querySelector(".dz-fab")) return;
    const fab = document.createElement("button"); fab.className = "dz-fab"; fab.innerHTML = '<span class="dz-i">ƒ</span> Desmos';
    fab.setAttribute("aria-label", "Open the Desmos graphing calculator");
    const pane = document.createElement("aside"); pane.className = "dz-pane"; pane.setAttribute("aria-label", "Desmos graphing calculator");
    const act = b.classList.contains("th-act");
    pane.innerHTML = `<div class="dz-top"><b>Desmos graphing calculator</b><span>${act ? "Built into the digital ACT Math section" : "Same calculator as the SAT"}</span><a href="https://www.desmos.com/calculator" target="_blank" rel="noopener">New tab ↗</a><button class="dz-close" aria-label="Close">×</button></div><div class="dz-body"></div>`;
    b.append(fab, pane);
    const open = () => { if (!pane.querySelector("iframe")) pane.querySelector(".dz-body").innerHTML = '<iframe src="https://www.desmos.com/calculator" title="Desmos graphing calculator" loading="lazy" allow="clipboard-read; clipboard-write"></iframe>'; pane.classList.add("on"); b.classList.add("dz-on"); };
    window.__dzOpen = open;
    fab.onclick = () => pane.classList.contains("on") ? (pane.classList.remove("on"), b.classList.remove("dz-on")) : open();
    pane.querySelector(".dz-close").onclick = () => { pane.classList.remove("on"); b.classList.remove("dz-on"); };
    document.querySelectorAll(".dz-embed:not([data-mounted])").forEach(e => { e.dataset.mounted = 1; e.innerHTML = '<iframe src="https://www.desmos.com/calculator" title="Desmos graphing calculator" loading="lazy"></iframe><p class="dz-cap">Can\'t see it? <a href="https://www.desmos.com/calculator" target="_blank" rel="noopener">Open Desmos in a new tab</a>.</p>'; });
  }

  function examHero() {
    const hero = document.querySelector("body.th-exam .hero");
    if (!hero || hero.querySelector(".exam-art")) return;
    const a = document.createElement("div"); a.className = "exam-art"; a.setAttribute("aria-hidden", "true");
    const fill = [1, 3, 0, 2, 1, 3, 2, 0, 1, 2];
    let b = "";
    fill.forEach((c, r) => {
      b += `<text x="18" y="${44 + r * 22}" font-family="JetBrains Mono, monospace" font-size="11" fill="#6B7280">${r + 1}</text>`;
      for (let k = 0; k < 4; k++) {
        const cx = 54 + k * 34, cy = 40 + r * 22;
        b += `<circle class="bb" cx="${cx}" cy="${cy}" r="8"/><text x="${cx}" y="${cy + 3.5}" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="9" fill="#9CA3AF">${"ABCD"[k]}</text>`;
        if (k === c) b += `<circle class="bf" cx="${cx}" cy="${cy}" r="8" style="animation-delay:${0.4 + r * 0.35}s"/>`;
      }
    });
    a.innerHTML = `<svg viewBox="0 0 300 270"><rect x="1" y="1" width="220" height="268" rx="8" fill="#fff" stroke="#D6D3C9"/>
      <rect x="1" y="1" width="220" height="22" rx="8" fill="#1F2937"/><text x="14" y="16" font-family="JetBrains Mono, monospace" font-size="10" fill="#F5B700" letter-spacing="2">ANSWER SHEET</text>${b}
      <g class="pencil"><g transform="translate(232 40) rotate(35)"><rect x="0" y="0" width="14" height="120" fill="#F5B700" stroke="#92400E" stroke-width="1"/><rect x="0" y="0" width="14" height="14" fill="#F9A8D4"/><rect x="0" y="14" width="14" height="8" fill="#9CA3AF"/><path d="M0 120 L7 140 L14 120Z" fill="#FDE68A" stroke="#92400E" stroke-width="1"/><path d="M4.5 133 L7 140 L9.5 133Z" fill="#1F2937"/></g></g></svg>`;
    hero.appendChild(a);
  }

  function mount() {
    document.querySelectorAll(".tp[data-hl]:not([data-mounted])").forEach(el => { el.dataset.mounted = 1; try { hl(el, JSON.parse(el.dataset.hl)); } catch (e) { console.error(e); } });
    document.querySelectorAll(".tp[data-pace]:not([data-mounted])").forEach(el => { el.dataset.mounted = 1; try { pace(el, JSON.parse(el.dataset.pace)); } catch (e) { console.error(e); } });
    document.querySelectorAll(".tp[data-reg]:not([data-mounted])").forEach(el => { el.dataset.mounted = 1; try { reg(el, JSON.parse(el.dataset.reg)); } catch (e) { console.error(e); } });
    chips(); drawer(); examHero();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", mount); else mount();
})();
