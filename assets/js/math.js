/* Math courses: expression parser, interactive grapher, unit circle and step-by-step equation animations. */
(function () {
  "use strict";
  const esc = s => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  const reduce = () => document.body.classList.contains("no-motion") || matchMedia("(prefers-reduced-motion: reduce)").matches;
  const INK = "#0F2A5F", BLUE = "#2563EB", ORANGE = "#EA580C", GREEN = "#059669", PURPLE = "#7C3AED", RED = "#DC2626", GRID = "rgba(37,99,235,.10)", AXIS = "#0F2A5F";
  const COLORS = [BLUE, ORANGE, GREEN, PURPLE, RED];

  /* ---------------- expression parser ---------------- */
  // supports + - * / ^, parentheses, implicit multiplication (2x, 3(x+1)), functions and named user functions
  const FN = { sin: Math.sin, cos: Math.cos, tan: Math.tan, sqrt: Math.sqrt, abs: Math.abs, ln: Math.log, log: Math.log10, exp: Math.exp,
    asin: Math.asin, acos: Math.acos, atan: Math.atan, floor: Math.floor, sec: x => 1 / Math.cos(x), csc: x => 1 / Math.sin(x), cot: x => 1 / Math.tan(x),
    cbrt: Math.cbrt, sign: Math.sign, min: Math.min, max: Math.max, log2: Math.log2 };
  function tokenize(s) {
    const t = []; let i = 0;
    while (i < s.length) {
      const ch = s[i];
      if (/\s/.test(ch)) { i++; continue; }
      if (/[0-9.]/.test(ch)) { let j = i; while (j < s.length && /[0-9.]/.test(s[j])) j++; t.push({ k: "n", v: parseFloat(s.slice(i, j)) }); i = j; continue; }
      if (/[a-zA-Zπθ_]/.test(ch)) { let j = i; while (j < s.length && /[a-zA-Z0-9_πθ]/.test(s[j])) j++; t.push({ k: "id", v: s.slice(i, j) }); i = j; continue; }
      t.push({ k: "op", v: ch }); i++;
    }
    return t;
  }
  function parse(src) {
    const t = tokenize(src); let p = 0;
    const peek = () => t[p], next = () => t[p++];
    const isOp = v => peek() && peek().k === "op" && peek().v === v;
    function expr() { let a = term(); while (isOp("+") || isOp("-")) { const o = next().v, b = term(); a = { o, a, b }; } return a; }
    function startsFactor() { const k = peek(); return k && (k.k === "n" || k.k === "id" || (k.k === "op" && k.v === "(")); }
    function term() {
      let a = unary();
      for (; ;) {
        if (isOp("*") || isOp("/")) { const o = next().v, b = unary(); a = { o, a, b }; }
        else if (startsFactor()) { const b = power(); a = { o: "*", a, b }; }
        else break;
      }
      return a;
    }
    function unary() { if (isOp("-")) { next(); return { o: "neg", a: unary() }; } if (isOp("+")) { next(); return unary(); } return power(); }
    function power() { const a = atom(); if (isOp("^")) { next(); return { o: "^", a, b: unary() }; } return a; }
    function atom() {
      const k = next(); if (!k) throw new Error("unexpected end");
      if (k.k === "n") return { n: k.v };
      if (k.k === "op" && k.v === "(") { const e = expr(); next(); return e; }
      if (k.k === "op" && k.v === "|") { const e = expr(); next(); return { f: "abs", args: [e] }; }
      if (k.k === "id") {
        if (isOp("(")) { next(); const args = [expr()]; while (isOp(",")) { next(); args.push(expr()); } next(); return { f: k.v, args }; }
        return { v: k.v };
      }
      throw new Error("bad token " + k.v);
    }
    const e = expr(); return e;
  }
  function evalAst(n, env) {
    if (n.n !== undefined) return n.n;
    if (n.v !== undefined) { if (n.v === "pi" || n.v === "π") return Math.PI; if (n.v === "e" && !("e" in env)) return Math.E; return env[n.v] ?? NaN; }
    if (n.f) {
      const args = n.args.map(a => evalAst(a, env));
      if (env.__fns && env.__fns[n.f]) return env.__fns[n.f](args[0], env);
      return FN[n.f] ? FN[n.f](...args) : NaN;
    }
    if (n.o === "neg") return -evalAst(n.a, env);
    const a = evalAst(n.a, env), b = evalAst(n.b, env);
    switch (n.o) { case "+": return a + b; case "-": return a - b; case "*": return a * b; case "/": return a / b; case "^": return Math.pow(a, b); }
    return NaN;
  }
  const cache = {};
  function compile(src) { return cache[src] || (cache[src] = parse(src)); }
  function ev(src, env) { try { return evalAst(compile(String(src)), env); } catch (e) { return NaN; } }
  window.MathEval = ev;

  /* ---------------- formatting ---------------- */
  function fm(x, d = 3) {
    if (!isFinite(x)) return x > 0 ? "∞" : x < 0 ? "−∞" : "undefined";
    if (Math.abs(x) < 1e-10) return "0";
    let s = (+x.toFixed(d)).toString();
    return s.replace("-", "−");
  }
  // exact-looking values for common angles
  function piFrac(th) {
    const k = th / Math.PI; for (const d of [1, 2, 3, 4, 6]) { const n = Math.round(k * d); if (Math.abs(n / d - k) < 2e-5) {
      if (n === 0) return "0"; const g = gcd(Math.abs(n), d), N = n / g, D = d / g;
      return (N === 1 ? "" : N === -1 ? "−" : (N + "").replace("-", "−")) + "π" + (D === 1 ? "" : "/" + D); } }
    return null;
  }
  function gcd(a, b) { return b ? gcd(b, a % b) : a; }
  const EXACT = [[0, "0"], [0.5, "1/2"], [Math.SQRT1_2, "√2/2"], [Math.sqrt(3) / 2, "√3/2"], [1, "1"], [Math.sqrt(3) / 3, "√3/3"], [Math.sqrt(3), "√3"]];
  function exact(x) { for (const [v, s] of EXACT) { if (Math.abs(Math.abs(x) - v) < 1e-9) return (x < 0 && s !== "0" ? "−" : "") + s; } return fm(x); }

  /* ---------------- canvas helpers ---------------- */
  function setup(cv, W, H) {
    const dpr = Math.min(2, window.devicePixelRatio || 1), w = cv.clientWidth || W;
    cv.width = Math.round(w * dpr); cv.height = Math.round(w * H / W * dpr);
    const c = cv.getContext("2d"); c.setTransform(cv.width / W, 0, 0, cv.height / H, 0, 0); return c;
  }
  function tween(from, to, ms, step, done) {
    if (reduce()) { step(to); done && done(); return; }
    const t0 = performance.now();
    (function f(now) { const k = Math.min(1, (now - t0) / ms), e = 1 - Math.pow(1 - k, 3); step(from + (to - from) * e); if (k < 1) requestAnimationFrame(f); else done && done(); })(t0);
  }

  /* ---------------- grapher ---------------- */
  function labGraph(el, p) {
    const W = 720, H = p.h || 420;
    const [x0, x1] = p.x || [-10, 10], [y0, y1] = p.y || [-10, 10];
    const params = Object.entries(p.params || {});
    const P = {}; params.forEach(([k, d]) => (P[k] = d[3]));
    el.innerHTML = `${p.title ? `<div class="lab-h">${esc(p.title)} <span>${esc(p.sub || "Move the sliders and watch the graph change.")}</span></div>` : ""}
      ${params.length ? `<div class="mg-sl">${params.map(([k, d]) => `<label><span class="mg-k">${esc(d[4] || k)}</span><input type="range" min="${d[0]}" max="${d[1]}" step="${d[2]}" value="${d[3]}" data-k="${k}"><b data-v="${k}">${d[3]}</b></label>`).join("")}</div>` : ""}
      <div class="mg-fx">${(p.fns || []).map((f, i) => f.hide ? "" : `<span style="--c:${f.c || COLORS[i % 5]}">${esc(f.label || ((f.name || "y") + " = " + f.e))}</span>`).join("")}</div>
      <div class="mg-stage"><canvas width="${W}" height="${H}" role="img" aria-label="${esc(p.alt || "Interactive graph")}"></canvas><div class="mg-tip"></div></div>
      <div class="mg-ctl">${params.length ? `<button type="button" class="mg-b" data-a="anim">▶ Animate ${esc(params[0][1][4] || params[0][0])}</button><button type="button" class="mg-b" data-a="reset">Reset</button>` : ""}<span class="mg-read"></span></div>
      ${p.table ? '<div class="mg-table"></div>' : ""}`;
    const cv = el.querySelector("canvas"), tip = el.querySelector(".mg-tip");
    const X = x => (x - x0) / (x1 - x0) * W, Y = y => H - (y - y0) / (y1 - y0) * H;
    const fns = {}; let hover = null;
    function env(extra) { const e = Object.assign({ __fns: fns }, P, extra || {}); return e; }
    (p.fns || []).forEach((f, i) => { const nm = f.name || "f" + i; fns[nm] = (x, e) => ev(f.e, Object.assign({}, e, { x })); });
    function draw() {
      const c = setup(cv, W, H);
      c.clearRect(0, 0, W, H);
      // grid
      const stepX = p.gx || niceStep(x1 - x0), stepY = p.gy || niceStep(y1 - y0);
      c.lineWidth = 1; c.strokeStyle = GRID;
      for (let x = Math.ceil(x0 / stepX) * stepX; x <= x1; x += stepX) { c.beginPath(); c.moveTo(X(x), 0); c.lineTo(X(x), H); c.stroke(); }
      for (let y = Math.ceil(y0 / stepY) * stepY; y <= y1; y += stepY) { c.beginPath(); c.moveTo(0, Y(y)); c.lineTo(W, Y(y)); c.stroke(); }
      c.strokeStyle = AXIS; c.lineWidth = 1.6;
      if (y0 <= 0 && y1 >= 0) { c.beginPath(); c.moveTo(0, Y(0)); c.lineTo(W, Y(0)); c.stroke(); }
      if (x0 <= 0 && x1 >= 0) { c.beginPath(); c.moveTo(X(0), 0); c.lineTo(X(0), H); c.stroke(); }
      c.fillStyle = "rgba(15,42,95,.65)"; c.font = "600 11px 'JetBrains Mono', monospace"; c.textAlign = "center";
      const ly = clamp(Y(0) + 14, 12, H - 4), lx = clamp(X(0) - 6, 18, W - 4);
      for (let x = Math.ceil(x0 / stepX) * stepX; x <= x1; x += stepX) if (Math.abs(x) > 1e-9) c.fillText(p.xpi ? (piFrac(x) || fm(x, 2)) : fm(x, 2), X(x), ly);
      c.textAlign = "right"; for (let y = Math.ceil(y0 / stepY) * stepY; y <= y1; y += stepY) if (Math.abs(y) > 1e-9) c.fillText(fm(y, 2), lx, Y(y) + 4);
      const E = env();
      // asymptotes
      (p.vasym || []).forEach(s => { const a = ev(s, E); if (isFinite(a)) dashed(c, X(a), 0, X(a), H, RED); });
      (p.hasym || []).forEach(s => { const a = ev(s, E); if (isFinite(a)) dashed(c, 0, Y(a), W, Y(a), RED); });
      // shading between curves or under one: p.shade = {f, from, to}
      // curves
      (p.fns || []).forEach((f, i) => {
        const nm = f.name || "f" + i, col = f.c || COLORS[i % 5];
        c.strokeStyle = col; c.lineWidth = f.w || 3; c.lineJoin = "round"; c.setLineDash(f.dash ? [7, 6] : []);
        c.beginPath(); let pen = false, prev = null;
        const N = 900, dom = f.dom ? f.dom.map(s => ev(s, E)) : [x0, x1];
        for (let k = 0; k <= N; k++) {
          const x = dom[0] + (dom[1] - dom[0]) * k / N, y = fns[nm](x, E);
          if (!isFinite(y) || y > y1 + (y1 - y0) * 3 || y < y0 - (y1 - y0) * 3 || (prev !== null && Math.abs(y - prev) > (y1 - y0) * 1.5)) { pen = false; prev = isFinite(y) ? y : null; continue; }
          if (!pen) { c.moveTo(X(x), Y(y)); pen = true; } else c.lineTo(X(x), Y(y));
          prev = y;
        }
        c.stroke(); c.setLineDash([]);
      });
      // secant / tangent helpers
      if (p.secant) {
        const f = fns[p.secant.f || Object.keys(fns)[0]], a = ev(p.secant.a, E), b = ev(p.secant.b, E), fa = f(a, E), fb = f(b, E), m = (fb - fa) / (b - a);
        c.strokeStyle = PURPLE; c.lineWidth = 2.2; c.beginPath(); c.moveTo(X(x0), Y(fa + m * (x0 - a))); c.lineTo(X(x1), Y(fa + m * (x1 - a))); c.stroke();
        dot(c, X(a), Y(fa), PURPLE); dot(c, X(b), Y(fb), PURPLE);
      }
      (p.dots || []).forEach(([sx, sy, lab, col]) => { const x = ev(sx, E), y = ev(sy, E); if (isFinite(x) && isFinite(y)) { dot(c, X(x), Y(y), col || INK, !!(col && col === "open")); if (lab) { c.fillStyle = INK; c.font = "700 12px 'Plus Jakarta Sans', sans-serif"; c.textAlign = "left"; c.fillText(lab.replace(/\{(.+?)\}/g, (_, q) => fm(ev(q, E), 2)), X(x) + 8, Y(y) - 8); } } });
      if (hover) { const f = fns[Object.keys(fns)[0]]; const y = f(hover, E); if (isFinite(y)) { dot(c, X(hover), Y(y), ORANGE); tip.style.left = (X(hover) / W * 100) + "%"; tip.style.top = (Y(y) / H * 100) + "%"; tip.textContent = `(${fm(hover, 2)}, ${fm(y, 2)})`; tip.hidden = false; } else tip.hidden = true; } else tip.hidden = true;
      // readouts
      if (p.read) el.querySelector(".mg-read").innerHTML = p.read.map(([lab, s]) => `<span>${esc(lab)} <b>${fm(ev(s, E))}</b></span>`).join("");
      if (p.table) {
        const T = p.table;
        el.querySelector(".mg-table").innerHTML = `<table><tr><th>x</th>${T.x.map(x => `<td>${fm(x)}</td>`).join("")}</tr>${T.rows.map(([lab, s]) => `<tr><th>${esc(lab)}</th>${T.x.map(x => `<td>${fm(ev(s, env({ x })), 3)}</td>`).join("")}</tr>`).join("")}${T.diff ? `<tr class="mg-d"><th>${T.diff === "ratio" ? "÷ previous" : "− previous"}</th>${T.x.map((x, i) => { if (!i) return "<td></td>"; const a = ev(T.rows[0][1], env({ x: T.x[i - 1] })), b = ev(T.rows[0][1], env({ x })); return `<td>${T.diff === "ratio" ? "×" + fm(b / a, 3) : (b - a >= 0 ? "+" : "") + fm(b - a, 3)}</td>`; }).join("")}</tr>` : ""}</table>`;
      }
    }
    function niceStep(span) { const r = span / 10, p10 = Math.pow(10, Math.floor(Math.log10(r))), m = r / p10; return (m < 1.5 ? 1 : m < 3.5 ? 2 : m < 7.5 ? 5 : 10) * p10; }
    function dashed(c, a, b, cc, d, col) { c.save(); c.setLineDash([6, 6]); c.strokeStyle = col; c.lineWidth = 1.6; c.beginPath(); c.moveTo(a, b); c.lineTo(cc, d); c.stroke(); c.restore(); }
    function dot(c, x, y, col, open) { c.beginPath(); c.arc(x, y, 5.5, 0, 7); c.fillStyle = open ? "#fff" : col === "open" ? "#fff" : col; c.fill(); c.lineWidth = 2; c.strokeStyle = col === "open" ? INK : "#fff"; c.stroke(); }
    // sliders tween smoothly
    el.querySelectorAll("input[type=range]").forEach(inp => inp.addEventListener("input", () => {
      const k = inp.dataset.k, to = +inp.value; el.querySelector(`[data-v="${k}"]`).textContent = inp.value;
      const from = P[k]; if (Math.abs(to - from) > +inp.step * 1.5 && !animating) tween(from, to, 260, v => { P[k] = v; draw(); }); else { P[k] = to; draw(); }
    }));
    let animating = null;
    el.addEventListener("click", e => {
      const b = e.target.closest("[data-a]"); if (!b) return;
      if (b.dataset.a === "reset") { params.forEach(([k, d]) => { P[k] = d[3]; el.querySelector(`[data-k="${k}"]`).value = d[3]; el.querySelector(`[data-v="${k}"]`).textContent = d[3]; }); draw(); }
      if (b.dataset.a === "anim") {
        if (animating) { cancelAnimationFrame(animating); animating = null; b.textContent = "▶ Animate " + (params[0][1][4] || params[0][0]); return; }
        const [k, d] = params[0], t0 = performance.now(); b.textContent = "❚❚ Stop";
        (function f(now) { const s = (Math.sin((now - t0) / 1400 - Math.PI / 2) + 1) / 2; P[k] = d[0] + (d[1] - d[0]) * s; el.querySelector(`[data-k="${k}"]`).value = P[k]; el.querySelector(`[data-v="${k}"]`).textContent = fm(P[k], 2); draw(); animating = requestAnimationFrame(f); })(t0);
      }
    });
    cv.addEventListener("pointermove", e => { const r = cv.getBoundingClientRect(); hover = x0 + (e.clientX - r.left) / r.width * (x1 - x0); draw(); });
    cv.addEventListener("pointerleave", () => { hover = null; draw(); });
    new ResizeObserver(draw).observe(cv);
    draw();
  }
  const clamp = (v, a, b) => Math.max(a, Math.min(b, v));

  /* ---------------- unit circle ---------------- */
  function labCircle(el, p) {
    const W = 720, H = 330;
    el.innerHTML = `<div class="lab-h">Unit circle <span>The point (cos θ, sin θ) travels around the circle; its height traces the sine wave.</span></div>
      <div class="mg-sl"><label><span class="mg-k">θ</span><input type="range" min="0" max="360" step="1" value="${p.deg ?? 30}" data-k="th"><b data-v="th"></b></label></div>
      <div class="mg-stage"><canvas width="${W}" height="${H}" role="img" aria-label="Unit circle and sine wave"></canvas></div>
      <div class="mg-ctl"><button type="button" class="mg-b" data-a="play">▶ Play</button>${[30, 45, 60, 90, 120, 135, 150, 180, 210, 270, 300, 330].map(d => `<button type="button" class="mg-b sm" data-d="${d}">${d}°</button>`).join("")}</div>
      <div class="mg-read uc-read"></div>`;
    const cv = el.querySelector("canvas"), inp = el.querySelector("input");
    let th = (p.deg ?? 30) * Math.PI / 180, playing = null;
    const cx = 170, cy = 165, R = 120, wx = 340, ww = 360;
    function draw() {
      const c = setup(cv, W, H); c.clearRect(0, 0, W, H);
      c.strokeStyle = GRID; c.lineWidth = 1; for (let i = -1; i <= 1; i += 0.5) { c.beginPath(); c.moveTo(cx - R - 20, cy - i * R); c.lineTo(wx + ww + 10, cy - i * R); c.stroke(); }
      c.strokeStyle = AXIS; c.lineWidth = 1.5;
      c.beginPath(); c.moveTo(cx - R - 20, cy); c.lineTo(cx + R + 20, cy); c.moveTo(cx, cy - R - 20); c.lineTo(cx, cy + R + 20); c.stroke();
      c.beginPath(); c.moveTo(wx, cy); c.lineTo(wx + ww + 10, cy); c.stroke();
      c.strokeStyle = "rgba(15,42,95,.35)"; c.lineWidth = 2; c.beginPath(); c.arc(cx, cy, R, 0, 7); c.stroke();
      // angle arc
      c.strokeStyle = PURPLE; c.lineWidth = 2.5; c.beginPath(); c.arc(cx, cy, 28, 0, -th, true); c.stroke();
      const px = cx + R * Math.cos(th), py = cy - R * Math.sin(th);
      c.strokeStyle = INK; c.lineWidth = 2; c.beginPath(); c.moveTo(cx, cy); c.lineTo(px, py); c.stroke();
      c.strokeStyle = BLUE; c.lineWidth = 4; c.beginPath(); c.moveTo(cx, cy); c.lineTo(px, cy); c.stroke();          // cos
      c.strokeStyle = ORANGE; c.lineWidth = 4; c.beginPath(); c.moveTo(px, cy); c.lineTo(px, py); c.stroke();        // sin
      // sine wave
      c.strokeStyle = "rgba(234,88,12,.25)"; c.lineWidth = 2; c.beginPath();
      for (let k = 0; k <= 200; k++) { const a = k / 200 * 2 * Math.PI, x = wx + a / (2 * Math.PI) * ww, y = cy - R * Math.sin(a); k ? c.lineTo(x, y) : c.moveTo(x, y); } c.stroke();
      c.strokeStyle = ORANGE; c.lineWidth = 3.5; c.beginPath();
      for (let k = 0; k <= 200; k++) { const a = k / 200 * th, x = wx + a / (2 * Math.PI) * ww, y = cy - R * Math.sin(a); k ? c.lineTo(x, y) : c.moveTo(x, y); } c.stroke();
      const wxp = wx + th / (2 * Math.PI) * ww;
      c.save(); c.setLineDash([4, 5]); c.strokeStyle = "rgba(234,88,12,.6)"; c.lineWidth = 1.5; c.beginPath(); c.moveTo(px, py); c.lineTo(wxp, py); c.stroke(); c.restore();
      [[px, py, INK], [wxp, py, ORANGE]].forEach(([x, y, col]) => { c.beginPath(); c.arc(x, y, 6.5, 0, 7); c.fillStyle = col; c.fill(); c.strokeStyle = "#fff"; c.lineWidth = 2; c.stroke(); });
      c.font = "600 11px 'JetBrains Mono', monospace"; c.fillStyle = "rgba(15,42,95,.7)"; c.textAlign = "center";
      [["π/2", 0.25], ["π", 0.5], ["3π/2", 0.75], ["2π", 1]].forEach(([s, k]) => c.fillText(s, wx + k * ww, cy + 16));
      c.font = "700 13px 'Plus Jakarta Sans', sans-serif"; c.fillStyle = BLUE; c.fillText("cos θ", (cx + px) / 2, cy + (Math.sin(th) >= 0 ? 18 : -10));
      c.fillStyle = ORANGE; c.textAlign = Math.cos(th) >= 0 ? "left" : "right"; c.fillText("sin θ", px + (Math.cos(th) >= 0 ? 8 : -8), (cy + py) / 2);
      const deg = Math.round(th * 180 / Math.PI) % 361, pf = piFrac(th);
      el.querySelector('[data-v="th"]').textContent = deg + "°";
      const tn = Math.abs(Math.cos(th)) < 1e-9 ? "undefined" : exact(Math.tan(th));
      el.querySelector(".uc-read").innerHTML = `<span>θ = <b>${deg}°${pf ? " = " + pf : " ≈ " + fm(th, 3) + " rad"}</b></span><span style="color:${BLUE}">cos θ = <b>${exact(Math.cos(th))}</b></span><span style="color:${ORANGE}">sin θ = <b>${exact(Math.sin(th))}</b></span><span>tan θ = <b>${tn}</b></span>`;
    }
    inp.addEventListener("input", () => { th = +inp.value * Math.PI / 180; draw(); });
    el.addEventListener("click", e => {
      const d = e.target.closest("[data-d]");
      if (d) { const to = +d.dataset.d * Math.PI / 180; tween(th, to, 600, v => { th = v; inp.value = Math.round(v * 180 / Math.PI); draw(); }, () => { th = to; draw(); }); }
      const b = e.target.closest('[data-a="play"]');
      if (b) {
        if (playing) { cancelAnimationFrame(playing); playing = null; b.textContent = "▶ Play"; return; }
        b.textContent = "❚❚ Pause"; let last = performance.now();
        (function f(now) { th = (th + (now - last) / 1000 * 0.9) % (2 * Math.PI); last = now; inp.value = Math.round(th * 180 / Math.PI); draw(); playing = requestAnimationFrame(f); })(last);
      }
    });
    new ResizeObserver(draw).observe(cv); draw();
  }


  /* ---------------- polar grapher ---------------- */
  function labPolar(el, p) {
    const W = 720, H = 440, R = p.R || 5, sc = (H / 2 - 16) / R;
    const params = Object.entries(p.params || {}), P = {}; params.forEach(([k, d]) => (P[k] = d[3]));
    el.innerHTML = `<div class="lab-h">${esc(p.title || "Polar graph")} <span>${esc(p.sub || "")}</span></div>
      ${params.length ? `<div class="mg-sl">${params.map(([k, d]) => `<label><span class="mg-k">${esc(d[4] || k)}</span><input type="range" min="${d[0]}" max="${d[1]}" step="${d[2]}" value="${d[3]}" data-k="${k}"><b data-v="${k}">${d[3]}</b></label>`).join("")}</div>` : ""}
      <div class="mg-fx"><span style="--c:${BLUE}">${esc(p.label || "r = " + p.r)}</span><span style="--c:${ORANGE}">r vs θ</span></div>
      <div class="mg-stage"><canvas width="${W}" height="${H}" role="img" aria-label="Polar curve and its r versus theta graph"></canvas></div>
      <div class="mg-ctl"><button type="button" class="mg-b" data-a="sweep">▶ Sweep θ</button><span class="mg-read"></span></div>`;
    const cv = el.querySelector("canvas"); let tmax = 2 * Math.PI * (p.turns || 1), sweeping = null;
    const r = t => ev(p.r, Object.assign({}, P, { t, θ: t }));
    function draw() {
      const c = setup(cv, W, H); c.clearRect(0, 0, W, H);
      const cx = H / 2, cy = H / 2, T = 2 * Math.PI * (p.turns || 1);
      // polar grid
      c.strokeStyle = GRID; c.lineWidth = 1;
      for (let k = 1; k <= R; k++) { c.beginPath(); c.arc(cx, cy, k * sc, 0, 7); c.stroke(); }
      for (let k = 0; k < 12; k++) { const a = k * Math.PI / 6; c.beginPath(); c.moveTo(cx, cy); c.lineTo(cx + R * sc * Math.cos(a), cy - R * sc * Math.sin(a)); c.stroke(); }
      c.strokeStyle = AXIS; c.lineWidth = 1.4; c.beginPath(); c.moveTo(cx - R * sc, cy); c.lineTo(cx + R * sc, cy); c.moveTo(cx, cy - R * sc); c.lineTo(cx, cy + R * sc); c.stroke();
      // curve up to tmax
      c.strokeStyle = BLUE; c.lineWidth = 3; c.lineJoin = "round"; c.beginPath();
      const N = 720; let first = true;
      for (let k = 0; k <= N; k++) { const t = tmax * k / N, rr = r(t); if (!isFinite(rr)) { first = true; continue; } const x = cx + rr * sc * Math.cos(t), y = cy - rr * sc * Math.sin(t); first ? c.moveTo(x, y) : c.lineTo(x, y); first = false; }
      c.stroke();
      const rr = r(tmax), px = cx + rr * sc * Math.cos(tmax), py = cy - rr * sc * Math.sin(tmax);
      c.strokeStyle = "rgba(124,58,237,.7)"; c.lineWidth = 2; c.beginPath(); c.moveTo(cx, cy); c.lineTo(px, py); c.stroke();
      c.beginPath(); c.arc(px, py, 6.5, 0, 7); c.fillStyle = INK; c.fill(); c.strokeStyle = "#fff"; c.lineWidth = 2; c.stroke();
      // r vs theta panel
      const gx = H + 20, gw = W - gx - 12, gy = cy, gs = (H / 2 - 30) / R;
      c.strokeStyle = GRID; c.lineWidth = 1; for (let k = -R; k <= R; k++) { c.beginPath(); c.moveTo(gx, gy - k * gs); c.lineTo(gx + gw, gy - k * gs); c.stroke(); }
      c.strokeStyle = AXIS; c.lineWidth = 1.4; c.beginPath(); c.moveTo(gx, gy); c.lineTo(gx + gw, gy); c.moveTo(gx, gy - R * gs); c.lineTo(gx, gy + R * gs); c.stroke();
      c.fillStyle = "rgba(15,42,95,.7)"; c.font = "600 11px 'JetBrains Mono', monospace"; c.textAlign = "center";
      for (let k = 1; k <= 4; k++) c.fillText(piFrac(k * T / 4) || fm(k * T / 4, 2), gx + gw * k / 4, gy + 15);
      c.fillText("r", gx - 8, gy - R * gs + 4);
      c.strokeStyle = "rgba(234,88,12,.25)"; c.lineWidth = 2; c.beginPath();
      for (let k = 0; k <= 300; k++) { const t = T * k / 300, y = gy - r(t) * gs; k ? c.lineTo(gx + gw * k / 300, y) : c.moveTo(gx, y); } c.stroke();
      c.strokeStyle = ORANGE; c.lineWidth = 3; c.beginPath();
      for (let k = 0; k <= 300; k++) { const t = tmax * k / 300, y = gy - r(t) * gs; k ? c.lineTo(gx + gw * (t / T), y) : c.moveTo(gx, y); } c.stroke();
      c.beginPath(); c.arc(gx + gw * tmax / T, gy - rr * gs, 6, 0, 7); c.fillStyle = ORANGE; c.fill();
      const pf = piFrac(tmax);
      el.querySelector(".mg-read").innerHTML = `<span>θ = <b>${pf || fm(tmax, 2)}</b></span><span>r = <b>${fm(rr, 2)}</b></span><span>(x, y) = <b>(${fm(rr * Math.cos(tmax), 2)}, ${fm(rr * Math.sin(tmax), 2)})</b></span>`;
    }
    el.querySelectorAll("input[type=range]").forEach(inp => inp.addEventListener("input", () => { const k = inp.dataset.k; P[k] = +inp.value; el.querySelector(`[data-v="${k}"]`).textContent = inp.value; draw(); }));
    el.addEventListener("click", e => {
      const b = e.target.closest('[data-a="sweep"]'); if (!b) return;
      if (sweeping) { cancelAnimationFrame(sweeping); sweeping = null; b.textContent = "▶ Sweep θ"; tmax = 2 * Math.PI * (p.turns || 1); draw(); return; }
      if (reduce()) { tmax = 2 * Math.PI * (p.turns || 1); draw(); return; }
      b.textContent = "❚❚ Stop"; const t0 = performance.now(), T = 2 * Math.PI * (p.turns || 1), dur = 5200;
      (function f(now) { const k = Math.min(1, (now - t0) / dur); tmax = Math.max(0.001, T * k); draw(); if (k < 1) sweeping = requestAnimationFrame(f); else { sweeping = null; b.textContent = "▶ Sweep θ"; } })(t0);
    });
    new ResizeObserver(draw).observe(cv); draw();
  }

  /* ---------------- step-by-step equation animation ---------------- */
  function steps(el, p) {
    const frames = p.frames.map(f => ({ note: f.note || "", t: f.t.map(x => Array.isArray(x) ? x : String(x).split("|")) }));
    el.innerHTML = `${p.title ? `<div class="wa-h">${esc(p.title)}</div>` : ""}<div class="wa-stage"><div class="wa-row"></div></div><div class="wa-note"></div>
      <div class="wa-ctl"><button type="button" class="wa-b" data-a="back" aria-label="Back">◀</button><span class="wa-dots">${frames.map((_, i) => `<i data-i="${i}"></i>`).join("")}</span><button type="button" class="wa-b" data-a="play">Play</button><button type="button" class="wa-b solid" data-a="next">Step ▶</button></div>`;
    const row = el.querySelector(".wa-row"), note = el.querySelector(".wa-note"), dots = el.querySelectorAll(".wa-dots i");
    let i = 0, auto = null;
    window.WA.render(el, row, frames, 0, false, note, dots);
    function go(k) { const prev = i; i = k; window.WA.render(el, row, frames, i, prev !== i, note, dots, prev); }
    el.addEventListener("click", e => {
      const a = e.target.closest("[data-a]"), d = e.target.closest("[data-i]");
      if (d) { stop(); go(+d.dataset.i); return; }
      if (!a) return;
      if (a.dataset.a === "next") { stop(); go(i === frames.length - 1 ? 0 : i + 1); }
      if (a.dataset.a === "back") { stop(); if (i > 0) go(i - 1); }
      if (a.dataset.a === "play") { if (auto) { stop(); return; } a.textContent = "Pause"; if (i === frames.length - 1) go(0); auto = setInterval(() => { if (i >= frames.length - 1) { stop(); return; } go(i + 1); }, 1700); }
    });
    function stop() { if (auto) { clearInterval(auto); auto = null; } const b = el.querySelector('[data-a="play"]'); if (b) b.textContent = "Play"; }
  }

  function mount(root) {
    (root || document).querySelectorAll(".mlab[data-lab]").forEach(el => {
      if (el.dataset.mounted) return; el.dataset.mounted = 1;
      try { const p = JSON.parse(el.dataset.lab); ({ graph: labGraph, circle: labCircle, polar: labPolar })[p.type](el, p); } catch (e) { console.error(e); }
    });
    (root || document).querySelectorAll(".msteps[data-w]").forEach(el => {
      if (el.dataset.mounted) return; el.dataset.mounted = 1;
      try { steps(el, JSON.parse(el.dataset.w)); } catch (e) { console.error(e); }
    });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", () => mount()); else mount();
  document.addEventListener("chapterchange", () => document.querySelectorAll(".mlab canvas").forEach(cv => cv.dispatchEvent(new Event("pointerleave"))));
})();
