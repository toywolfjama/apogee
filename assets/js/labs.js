/* Interactive labs for Computer Engineering and Machine Learning.
   Each lab is <div class="xlab" data-lab='{"type": "...", ...}'>. */
(function () {
  "use strict";
  const esc = s => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  const still = () => document.body.classList.contains("no-motion") || matchMedia("(prefers-reduced-motion: reduce)").matches;
  const css = n => getComputedStyle(document.body).getPropertyValue(n).trim();
  function PAL() {
    return { ink: css("--ink") || "#0F2A5F", a: css("--lab-a") || "#2563EB", b: css("--lab-b") || "#EA580C", c: css("--lab-c") || "#059669",
      on: css("--lab-on") || "#16A34A", off: "#CBD5E1", line: css("--line") || "#DCE3F0", muted: css("--muted") || "#4B5B7A", soft: css("--well") || "#F8FAFE" };
  }
  const emit = (el, d) => el.dispatchEvent(new CustomEvent("labstate", { detail: d, bubbles: true }));
  const CL = ["#2563EB", "#EA580C", "#059669", "#9333EA", "#DB2777", "#CA8A04", "#0891B2", "#DC2626"];
  const fm = (x, d = 3) => { if (!isFinite(x)) return x > 0 ? "∞" : "−∞"; if (Math.abs(x) < 1e-12) return "0"; return (+x.toFixed(d)).toString().replace("-", "−"); };
  function rng(seed) { let a = seed >>> 0; return () => { a |= 0; a = a + 0x6D2B79F5 | 0; let t = Math.imul(a ^ a >>> 15, 1 | a); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; }
  function gauss(r) { let u = 0, v = 0; while (u === 0) u = r(); while (v === 0) v = r(); return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v); }
  const head = (p, t, s) => `<div class="lab-h">${esc(p.title || t)} <span>${esc(p.sub || s || "")}</span></div>`;
  const B = (act, label, extra = "") => `<button type="button" class="mg-b ${extra}" data-act="${act}">${label}</button>`;
  function slider(key, label, min, max, step, val) {
    return `<label><span class="mg-k">${label}</span><input type="range" data-k="${key}" min="${min}" max="${max}" step="${step}" value="${val}"><b data-v="${key}"></b></label>`;
  }
  function stage(host, W, H) {
    const wrap = document.createElement("div"); wrap.className = "mg-stage"; wrap.style.maxWidth = Math.round(W * 1.2) + "px"; wrap.style.margin = "0 auto";
    const cv = document.createElement("canvas"); wrap.appendChild(cv); host.appendChild(wrap);
    const d = Math.min(2, window.devicePixelRatio || 1);
    cv.width = W * d; cv.height = H * d; cv.style.aspectRatio = W + " / " + H;
    const c = cv.getContext("2d"); c.setTransform(d, 0, 0, d, 0, 0);
    return { cv, c, W, H, pos(e) { const r = cv.getBoundingClientRect(); return [(e.clientX - r.left) * W / r.width, (e.clientY - r.top) * H / r.height]; } };
  }
  function nice(range) { const raw = range / 6, p = Math.pow(10, Math.floor(Math.log10(raw))), m = raw / p; return (m < 1.5 ? 1 : m < 3.5 ? 2 : m < 7.5 ? 5 : 10) * p; }
  function plot(st, xr, yr, pad) {
    pad = Object.assign({ l: 42, r: 14, t: 12, b: 28 }, pad || {});
    const pw = st.W - pad.l - pad.r, ph = st.H - pad.t - pad.b;
    const m = {
      X: x => pad.l + (x - xr[0]) / (xr[1] - xr[0]) * pw, Y: y => pad.t + (yr[1] - y) / (yr[1] - yr[0]) * ph,
      ix: px => xr[0] + (px - pad.l) / pw * (xr[1] - xr[0]), iy: py => yr[1] - (py - pad.t) / ph * (yr[1] - yr[0]), pad, pw, ph, xr, yr,
      axes(o = {}) {
        const c = st.c, P = PAL();
        c.save(); c.font = "500 11px JetBrains Mono, monospace"; c.fillStyle = P.muted; c.lineWidth = 1;
        const sx = o.sx || nice(xr[1] - xr[0]), sy = o.sy || nice(yr[1] - yr[0]);
        for (let x = Math.ceil(xr[0] / sx) * sx; x <= xr[1] + 1e-9; x += sx) { c.strokeStyle = "rgba(100,116,139,.15)"; c.beginPath(); c.moveTo(m.X(x), pad.t); c.lineTo(m.X(x), pad.t + ph); c.stroke(); c.textAlign = "center"; c.fillText(fm(x, 2), m.X(x), pad.t + ph + 16); }
        for (let y = Math.ceil(yr[0] / sy) * sy; y <= yr[1] + 1e-9; y += sy) { c.strokeStyle = "rgba(100,116,139,.15)"; c.beginPath(); c.moveTo(pad.l, m.Y(y)); c.lineTo(pad.l + pw, m.Y(y)); c.stroke(); c.textAlign = "right"; c.fillText(fm(y, 2), pad.l - 6, m.Y(y) + 4); }
        c.strokeStyle = P.ink; c.lineWidth = 1.4; c.strokeRect(pad.l, pad.t, pw, ph);
        if (o.xl) { c.textAlign = "right"; c.fillStyle = P.ink; c.fillText(o.xl, pad.l + pw - 4, pad.t + ph - 6); }
        if (o.yl) { c.textAlign = "left"; c.fillStyle = P.ink; c.fillText(o.yl, pad.l + 6, pad.t + 14); }
        c.restore();
      }
    };
    return m;
  }
  function dot(c, x, y, r, fill, stroke, lw = 2) { c.beginPath(); c.arc(x, y, r, 0, 6.2832); if (fill) { c.fillStyle = fill; c.fill(); } if (stroke) { c.strokeStyle = stroke; c.lineWidth = lw; c.stroke(); } }
  function bindSliders(el, S, cb, fmt = {}) {
    el.querySelectorAll("input[type=range][data-k]").forEach(inp => {
      const k = inp.dataset.k, out = el.querySelector(`[data-v="${k}"]`);
      const show = () => { if (out) out.textContent = fmt[k] ? fmt[k](S[k]) : fm(S[k], 3); };
      S[k] = +inp.value; show();
      inp.addEventListener("input", () => { S[k] = +inp.value; show(); cb(k); });
      inp._set = v => { inp.value = v; S[k] = +v; show(); };
    });
  }
  const setSl = (el, k, v) => { const i = el.querySelector(`input[data-k="${k}"]`); if (i && i._set) i._set(v); };

  /* =========================================================
     COMPUTER ENGINEERING
     ========================================================= */

  /* ---- binary / hex / two's complement ---- */
  function bits(el, p) {
    const n = p.n || 8; let v = (p.value || 0) & ((1 << n) - 1);
    el.innerHTML = head(p, `${n}-bit number`, "Click bits to flip them. Every bit is worth twice the one to its right.") +
      `<div class="xl-bits" style="--n:${n}"></div><div class="xl-read xl-bitread"></div>
      <div class="mg-ctl"><label class="xl-in">Type a decimal <input type="number" class="xl-num" value="${v}"></label>${B("inc", "+1")}${B("dec", "−1")}${B("not", "Invert (NOT)")}${B("neg", "Negate (two's complement)")}${B("shl", "Shift left ≪")}${B("shr", "Shift right ≫")}${B("clr", "Clear")}</div>`;
    const box = el.querySelector(".xl-bits"), rd = el.querySelector(".xl-bitread"), num = el.querySelector(".xl-num"), M = (1 << n) - 1;
    function draw() {
      const signed = v >= 1 << (n - 1) ? v - (1 << n) : v;
      box.innerHTML = Array.from({ length: n }, (_, i) => { const k = n - 1 - i, b = (v >> k) & 1;
        const w = (k === n - 1 && p.signed !== false) ? "−" + (1 << k) : (1 << k);
        return `<button type="button" class="xl-bit ${b ? "on" : ""}" data-k="${k}"><b>${b}</b><small>${w}</small></button>`; }).join("");
      const hex = v.toString(16).toUpperCase().padStart(Math.ceil(n / 4), "0");
      const groups = v.toString(2).padStart(n, "0").replace(/(.{4})(?=.)/g, "$1 ");
      const sum = Array.from({ length: n }, (_, i) => n - 1 - i).filter(k => (v >> k) & 1).map(k => (k === n - 1 && p.signed !== false) ? "−" + (1 << k) : (1 << k));
      rd.innerHTML = `<span>Binary <b>${groups}</b></span><span>Unsigned <b>${v}</b></span>${p.signed !== false ? `<span>Signed (two's complement) <b>${signed}</b></span>` : ""}<span>Hex <b>0x${hex}</b></span>
        <span class="xl-sum">${sum.length ? sum.join(" + ").replace("+ −", "− ") + " = " + (p.signed !== false ? String(signed).replace("-", "−") : v) : "all bits 0 → 0"}</span>`;
      emit(el, { value: v, signed });
      num.value = p.signed !== false && document.activeElement !== num ? (num.dataset.s === "1" ? signed : v) : num.value;
    }
    box.addEventListener("click", e => { const b = e.target.closest(".xl-bit"); if (!b) return; v ^= 1 << +b.dataset.k; draw(); });
    num.addEventListener("input", () => { let x = parseInt(num.value, 10); if (isNaN(x)) return; num.dataset.s = x < 0 ? "1" : "0"; v = ((x % (M + 1)) + (M + 1)) & M; draw(); });
    el.querySelector(".mg-ctl").addEventListener("click", e => {
      const a = e.target.closest("[data-act]"); if (!a) return;
      const k = a.dataset.act;
      if (k === "inc") v = (v + 1) & M; if (k === "dec") v = (v - 1) & M; if (k === "not") v = ~v & M; if (k === "neg") v = (~v + 1) & M;
      if (k === "shl") v = (v << 1) & M; if (k === "shr") v = v >>> 1; if (k === "clr") v = 0; draw();
    });
    draw();
  }

  /* ---- IEEE 754 single precision ---- */
  function float32(el, p) {
    const dv = new DataView(new ArrayBuffer(4)); dv.setFloat32(0, p.value ?? 6.5);
    el.innerHTML = head(p, "IEEE 754 float (32 bits)", "1 sign bit, 8 exponent bits (bias 127), 23 fraction bits. Click any bit or type a number.") +
      `<div class="xl-fbits"></div><div class="xl-read xl-fread"></div><div class="mg-ctl"><label class="xl-in">Number <input type="text" class="xl-num" value="${p.value ?? 6.5}"></label>${B("0.1", "0.1")}${B("-2.75", "−2.75")}${B("1e-45", "Smallest")}${B("Infinity", "∞")}${B("NaN", "NaN")}</div>`;
    const box = el.querySelector(".xl-fbits"), rd = el.querySelector(".xl-fread"), num = el.querySelector(".xl-num");
    function draw() {
      const u = dv.getUint32(0), s = u >>> 31, e = (u >>> 23) & 255, f = u & 0x7FFFFF;
      box.innerHTML = Array.from({ length: 32 }, (_, i) => { const k = 31 - i, b = (u >>> k) & 1, cls = k === 31 ? "s" : k >= 23 ? "e" : "f";
        return `<button type="button" class="xl-fb ${cls} ${b ? "on" : ""}" data-k="${k}">${b}</button>`; }).join("");
      const val = dv.getFloat32(0);
      let how;
      if (e === 255) how = f ? "Exponent all 1s and fraction ≠ 0 → NaN" : `Exponent all 1s, fraction 0 → ${s ? "−" : "+"}∞`;
      else if (e === 0) how = `Exponent 0 → subnormal: (−1)<sup>${s}</sup> × 0.${f.toString(2).padStart(23, "0").replace(/0+$/, "") || "0"}₂ × 2<sup>−126</sup>`;
      else how = `(−1)<sup>${s}</sup> × 1.${f.toString(2).padStart(23, "0").replace(/0+$/, "") || "0"}₂ × 2<sup>${e} − 127 = ${e - 127}</sup>`;
      rd.innerHTML = `<span><i class="sw s"></i>Sign <b>${s}</b> (${s ? "negative" : "positive"})</span><span><i class="sw e"></i>Exponent <b>${e.toString(2).padStart(8, "0")}₂ = ${e}</b></span><span><i class="sw f"></i>Fraction <b>${f.toString(2).padStart(23, "0")}</b></span>
        <span class="xl-sum">${how}</span><span class="xl-sum">Stored value: <b>${isNaN(val) ? "NaN" : val === Infinity ? "∞" : val === -Infinity ? "−∞" : String(val)}</b>${p.showErr !== false && document.activeElement === num && isFinite(+num.value) && +num.value !== val ? ` &nbsp;(you typed ${esc(num.value)}, error ${fm(val - +num.value, 12)})` : ""}</span>`;
    }
    box.addEventListener("click", e => { const b = e.target.closest(".xl-fb"); if (!b) return; dv.setUint32(0, (dv.getUint32(0) ^ (1 << +b.dataset.k)) >>> 0); num.value = dv.getFloat32(0); draw(); });
    num.addEventListener("input", () => { const x = Number(num.value); if (num.value.trim() === "" || (isNaN(x) && num.value.trim() !== "NaN")) return; dv.setFloat32(0, x); draw(); });
    el.querySelector(".mg-ctl").addEventListener("click", e => { const a = e.target.closest("[data-act]"); if (!a) return; num.value = a.dataset.act; dv.setFloat32(0, Number(a.dataset.act)); num.focus(); draw(); });
    draw();
  }

  /* ---- gates ---- */
  const G = {
    AND: a => a.every(Boolean), OR: a => a.some(Boolean), NOT: a => !a[0], BUF: a => !!a[0],
    NAND: a => !a.every(Boolean), NOR: a => !a.some(Boolean), XOR: a => a.filter(Boolean).length % 2 === 1, XNOR: a => a.filter(Boolean).length % 2 === 0
  };
  const SYM = { AND: "A · B", OR: "A + B", NOT: "A′", NAND: "(A · B)′", NOR: "(A + B)′", XOR: "A ⊕ B", XNOR: "(A ⊕ B)′" };
  // gate body drawn in a 50x40 box; output pin at x=60 (with bubble) or 50
  function gatePath(t) {
    const base = t.replace(/^N(?=AND|OR)/, "").replace(/^XN/, "X");
    let d = "", extra = "";
    if (base === "AND") d = "M0 0H26A20 20 0 0 1 26 40H0Z";
    else if (base === "OR") d = "M0 0Q16 20 0 40Q34 40 50 20Q34 0 0 0Z";
    else if (base === "XOR") { d = "M0 0Q16 20 0 40Q34 40 50 20Q34 0 0 0Z"; extra = "M-7 0Q9 20 -7 40"; }
    else if (base === "NOT" || base === "BUF") d = "M2 0L44 20L2 40Z";
    const bubble = /^N|XNOR|NOT/.test(t) && t !== "BUF";
    return { d, extra, bubble, out: base === "NOT" || base === "BUF" ? (bubble ? 54 : 44) : (bubble ? 60 : 50) };
  }
  function gateSVG(t, x, y, s, fill, stroke) {
    const g = gatePath(t);
    return `<g transform="translate(${x} ${y}) scale(${s})"><path d="${g.d}" fill="${fill}" stroke="${stroke}" stroke-width="${2 / s}"/>${g.extra ? `<path d="${g.extra}" fill="none" stroke="${stroke}" stroke-width="${2 / s}"/>` : ""}${g.bubble ? `<circle cx="${g.out - 5}" cy="20" r="5" fill="#fff" stroke="${stroke}" stroke-width="${2 / s}"/>` : ""}</g>`;
  }
  function gate(el, p) {
    const list = p.gates || ["AND", "OR", "NOT", "NAND", "NOR", "XOR", "XNOR"];
    let cur = p.gate || list[0], A = 0, Bv = 0;
    el.innerHTML = head(p, "Logic gate playground", "Pick a gate, then click the inputs. The truth table row lights up.") +
      `<div class="xl-tabs">${list.map(g => `<button type="button" class="mg-b sm" data-g="${g}">${g}</button>`).join("")}</div>
       <div class="xl-gate"><svg viewBox="0 0 320 150" class="xl-svg"></svg><div class="xl-tt"></div></div><p class="xl-note"></p>`;
    const sv = el.querySelector("svg"), tt = el.querySelector(".xl-tt"), note = el.querySelector(".xl-note");
    const NOTE = { AND: "Output is 1 only when every input is 1.", OR: "Output is 1 when at least one input is 1.", NOT: "Flips the input: 0 → 1, 1 → 0.",
      NAND: "AND followed by NOT. Output is 0 only when every input is 1. NAND alone can build any circuit.", NOR: "OR followed by NOT. Output is 1 only when every input is 0. Also universal.",
      XOR: "Exclusive OR: 1 when the inputs are different. It is a 1-bit adder without the carry.", XNOR: "1 when the inputs are the same. It is a 1-bit equality checker." };
    function draw() {
      const P = PAL(), one = cur === "NOT", ins = one ? [A] : [A, Bv], out = G[cur](ins) ? 1 : 0, g = gatePath(cur);
      const wc = v => v ? P.on : "#94A3B8", gx = 130, gy = 45, s = 1.5, oy = gy + 30, ox = gx + g.out * s;
      const pins = one ? [oy] : [gy + 12, gy + 48];
      let h = "";
      pins.forEach((py, i) => { const v = ins[i];
        h += `<path d="M58 ${py}H${gx + (g.extra ? -2 : 3)}" stroke="${wc(v)}" stroke-width="4" stroke-linecap="round"/>
          <g class="xl-click" data-in="${i}"><rect x="12" y="${py - 17}" width="46" height="34" rx="9" fill="${v ? P.on : "#fff"}" stroke="${v ? P.on : "#94A3B8"}" stroke-width="2"/>
          <text x="35" y="${py + 6}" text-anchor="middle" font-family="JetBrains Mono" font-weight="800" font-size="17" fill="${v ? "#fff" : P.ink}">${"AB"[i]}=${v}</text></g>`; });
      h += gateSVG(cur, gx, gy, s, "#fff", P.ink);
      h += `<path d="M${ox} ${oy}H262" stroke="${wc(out)}" stroke-width="4" stroke-linecap="round"/><circle cx="282" cy="${oy}" r="20" fill="${out ? P.on : "#fff"}" stroke="${out ? P.on : "#94A3B8"}" stroke-width="2.5" class="${out ? "xl-glow" : ""}"/>
        <text x="282" y="${oy + 6}" text-anchor="middle" font-family="JetBrains Mono" font-weight="800" font-size="17" fill="${out ? "#fff" : P.ink}">${out}</text>
        <text x="${gx + 40}" y="${gy + 84}" text-anchor="middle" font-family="JetBrains Mono" font-size="13" fill="${P.muted}">${cur} · Y = ${SYM[cur]}</text>`;
      sv.innerHTML = h;
      const rows = one ? [[0], [1]] : [[0, 0], [0, 1], [1, 0], [1, 1]];
      tt.innerHTML = `<table><tr>${one ? "<th>A</th>" : "<th>A</th><th>B</th>"}<th>Y</th></tr>${rows.map(r => `<tr class="${r.every((x, i) => x === ins[i]) ? "cur" : ""}">${r.map(x => `<td>${x}</td>`).join("")}<td><b>${G[cur](r) ? 1 : 0}</b></td></tr>`).join("")}</table>`;
      note.textContent = NOTE[cur] || "";
      el.querySelectorAll("[data-g]").forEach(b => b.classList.toggle("on", b.dataset.g === cur));
    }
    sv.addEventListener("click", e => { const g = e.target.closest("[data-in]"); if (!g) return; if (g.dataset.in === "0") A ^= 1; else Bv ^= 1; draw(); });
    el.querySelector(".xl-tabs").addEventListener("click", e => { const b = e.target.closest("[data-g]"); if (b) { cur = b.dataset.g; draw(); } });
    draw();
  }

  /* ---- combinational circuit simulator ---- */
  function circuit(el, p) {
    const inputs = p.inputs, gates = p.gates, outs = p.outputs; const val = {}; inputs.forEach((n, i) => val[n] = (p.init || [])[i] || 0);
    el.innerHTML = head(p, "Circuit", "Click an input to flip it. Green wires carry 1, grey wires carry 0.") + `<svg class="xl-svg xl-circ"></svg><div class="xl-tt"></div>${p.note ? `<p class="xl-note">${p.note}</p>` : ""}`;
    const sv = el.querySelector("svg"), tt = el.querySelector(".xl-tt");
    const byId = {}; gates.forEach(g => byId[g.id] = g);
    const depth = {}; const dep = id => { if (inputs.includes(id)) return 0; if (depth[id] != null) return depth[id]; return depth[id] = 1 + Math.max(...byId[id].in.map(dep)); };
    gates.forEach(g => dep(g.id));
    const maxD = Math.max(...gates.map(g => depth[g.id]));
    const col = {}, users = {}; gates.forEach(g => g.in.forEach(s => (users[s] = users[s] || []).push(g.id)));
    const order = gates.slice().sort((a, b) => depth[b.id] - depth[a.id]);
    order.forEach(g => { const u = users[g.id] || []; col[g.id] = g.col != null ? g.col : u.length ? Math.max(depth[g.id], Math.min(...u.map(x => col[x])) - 1) : maxD; });
    const colW = 130, rowH = 78, cols = {};
    gates.forEach(g => (cols[col[g.id]] = cols[col[g.id]] || []).push(g));
    const nRows = Math.max(inputs.length, ...Object.values(cols).map(c => c.length), Object.keys(outs).length);
    const H = Math.max(160, nRows * rowH + 30), W = 110 + maxD * colW + 120;
    const pos = {};
    inputs.forEach((n, i) => pos[n] = { x: 70, y: (i + .5) * (H - 20) / inputs.length + 10 });
    Object.keys(cols).map(Number).sort((a, b) => a - b).forEach(d => { const list = cols[d];
      list.forEach(g => g._k = g.in.reduce((s, x) => s + (pos[x] ? pos[x].y : H / 2), 0) / g.in.length);
      if (!p.keepOrder) list.sort((a, b) => a._k - b._k);
      list.forEach((g, i) => { const gp = gatePath(g.t); pos[g.id] = { x: 60 + d * colW, y: g.y != null ? g.y * H : (i + .5) * (H - 20) / list.length + 10, out: gp.out * 1.2 }; }); });
    function evaluate(v) { const o = Object.assign({}, v); const ev = id => { if (id in o) return o[id]; const g = byId[id]; return o[id] = G[g.t](g.in.map(ev)) ? 1 : 0; }; gates.forEach(g => ev(g.id)); return o; }
    function draw() {
      const P = PAL(), v = evaluate(val), wc = x => x ? P.on : "#A8B3C4";
      sv.setAttribute("viewBox", `0 0 ${W} ${H}`);
      let wires = "", body = "";
      gates.forEach(g => { const q = pos[g.id], n = g.in.length, gp = gatePath(g.t);
        g.in.forEach((src, k) => { const s = pos[src], sx = inputs.includes(src) ? s.x + 22 : s.x + s.out, sy = s.y;
          const py = n === 1 ? q.y : q.y - 24 + (k + .5) * 48 / n, tx = q.x + (gp.extra ? -4 : 2), mx = (sx + tx) / 2;
          wires += `<path d="M${sx} ${sy}C${mx} ${sy} ${mx} ${py} ${tx} ${py}" fill="none" stroke="${wc(v[src])}" stroke-width="3.2"/>`; });
        body += gateSVG(g.t, q.x, q.y - 24, 1.2, "#fff", P.ink) + `<text x="${q.x + 26}" y="${q.y + 38}" text-anchor="middle" font-family="JetBrains Mono" font-size="10.5" fill="${P.muted}">${g.label || g.t}</text>`; });
      const outNames = Object.keys(outs);
      const outSorted = p.keepOrder ? outNames : outNames.slice().sort((a, b) => pos[outs[a]].y - pos[outs[b]].y);
      outSorted.forEach((name, i) => { const src = outs[name], s = pos[src], y = (i + .5) * (H - 20) / outNames.length + 10, x = W - 50, on = v[src];
        wires += `<path d="M${s.x + s.out} ${s.y}C${(s.x + s.out + x) / 2} ${s.y} ${(s.x + s.out + x) / 2} ${y} ${x - 18} ${y}" fill="none" stroke="${wc(on)}" stroke-width="3.2"/>`;
        body += `<circle cx="${x}" cy="${y}" r="17" fill="${on ? P.on : "#fff"}" stroke="${on ? P.on : "#94A3B8"}" stroke-width="2.5"/><text x="${x}" y="${y + 5}" text-anchor="middle" font-family="JetBrains Mono" font-weight="800" font-size="14" fill="${on ? "#fff" : P.ink}">${on}</text>
          <text x="${x}" y="${y - 23}" text-anchor="middle" font-family="JetBrains Mono" font-weight="700" font-size="12" fill="${P.ink}">${esc(name)}</text>`; });
      inputs.forEach(n => { const s = pos[n], on = val[n];
        body += `<g class="xl-click" data-in="${esc(n)}"><rect x="${s.x - 50}" y="${s.y - 16}" width="72" height="32" rx="9" fill="${on ? P.on : "#fff"}" stroke="${on ? P.on : "#94A3B8"}" stroke-width="2"/>
          <text x="${s.x - 14}" y="${s.y + 5}" text-anchor="middle" font-family="JetBrains Mono" font-weight="800" font-size="14" fill="${on ? "#fff" : P.ink}">${esc(n)}=${on}</text></g>`; });
      sv.innerHTML = wires + body;
      if (inputs.length <= 4 && p.table !== false) {
        const rows = []; for (let r = 0; r < 1 << inputs.length; r++) rows.push(inputs.map((_, i) => (r >> (inputs.length - 1 - i)) & 1));
        tt.innerHTML = `<table><tr>${inputs.map(n => `<th>${esc(n)}</th>`).join("")}${outNames.map(n => `<th class="o">${esc(n)}</th>`).join("")}</tr>${rows.map(r => {
          const iv = {}; inputs.forEach((n, i) => iv[n] = r[i]); const o = evaluate(iv); const curRow = inputs.every(n => iv[n] === val[n]);
          return `<tr class="${curRow ? "cur" : ""}" data-row="${r.join("")}">${r.map(x => `<td>${x}</td>`).join("")}${outNames.map(n => `<td><b>${o[outs[n]]}</b></td>`).join("")}</tr>`; }).join("")}</table>`;
      }
    }
    sv.addEventListener("click", e => { const g = e.target.closest("[data-in]"); if (!g) return; val[g.dataset.in] ^= 1; draw(); });
    tt.addEventListener("click", e => { const r = e.target.closest("[data-row]"); if (!r) return; inputs.forEach((n, i) => val[n] = +r.dataset.row[i]); draw(); });
    draw();
  }

  /* ---- Karnaugh map with automatic minimization ---- */
  function kmap(el, p) {
    const V = p.vars || ["A", "B", "C", "D"], n = V.length, N = 1 << n;
    const cells = new Array(N).fill(0); (p.ones || []).forEach(m => cells[m] = 1); (p.dc || []).forEach(m => cells[m] = 2);
    const gray = k => k === 1 ? [0, 1] : [0, 1, 3, 2];
    const rv = Math.floor(n / 2), cv = n - rv, R = gray(rv), C = gray(cv);
    const bin = (x, w) => x.toString(2).padStart(w, "0");
    el.innerHTML = head(p, `${n}-variable Karnaugh map`, "Click a cell: 0 → 1 → X (don't care) → 0. The map finds the simplest sum of products.") +
      `<div class="xl-kwrap"><div class="xl-km"></div><div class="xl-kout"></div></div><div class="mg-ctl">${B("clear", "All 0")}${B("rand", "Random function")}</div>`;
    const km = el.querySelector(".xl-km"), ko = el.querySelector(".xl-kout");
    function solve() {
      const ones = [], dcs = []; cells.forEach((c, i) => { if (c === 1) ones.push(i); if (c === 2) dcs.push(i); });
      if (!ones.length) return { expr: "0", groups: [] };
      let cur = [...ones, ...dcs].map(m => ({ v: m, m: 0, ms: [m] })); const primes = [];
      while (cur.length) {
        const next = [], used = new Set(), seen = new Set();
        for (let i = 0; i < cur.length; i++) for (let j = i + 1; j < cur.length; j++) {
          const a = cur[i], b = cur[j]; if (a.m !== b.m) continue; const d = a.v ^ b.v; if (d & (d - 1)) continue;
          used.add(i); used.add(j); const t = { v: a.v & ~d, m: a.m | d, ms: [...new Set([...a.ms, ...b.ms])].sort((x, y) => x - y) }; const key = t.v + "/" + t.m;
          if (!seen.has(key)) { seen.add(key); next.push(t); }
        }
        cur.forEach((t, i) => { if (!used.has(i)) primes.push(t); }); cur = next;
      }
      const left = new Set(ones), chosen = [];
      for (; ;) { let changed = false;
        for (const m of [...left]) { const cov = primes.filter(pi => pi.ms.includes(m)); if (cov.length === 1 && !chosen.includes(cov[0])) { chosen.push(cov[0]); cov[0].ms.forEach(x => left.delete(x)); changed = true; } }
        if (!changed) break; }
      while (left.size) { let best = null, bc = -1; primes.forEach(pi => { if (chosen.includes(pi)) return; const c = pi.ms.filter(x => left.has(x)).length; const lits = n - bitc(pi.m); if (c > bc || (c === bc && best && lits < n - bitc(best.m))) { bc = c; best = pi; } }); chosen.push(best); best.ms.forEach(x => left.delete(x)); }
      const term = t => { let s = ""; for (let i = 0; i < n; i++) { const bit = 1 << (n - 1 - i); if (t.m & bit) continue; s += V[i] + (t.v & bit ? "" : "′"); } return s || "1"; };
      const terms = chosen.map(term);
      return { expr: terms.includes("1") ? "1" : terms.join(" + "), groups: chosen.map((t, i) => ({ t: terms[i], ms: t.ms })) };
    }
    function bitc(x) { let c = 0; while (x) { c += x & 1; x >>= 1; } return c; }
    function draw() {
      const s = solve();
      const idx = (r, c) => (R[r] << cv) | C[c];
      let h = `<table class="xl-ktab"><tr><th class="corner">${V.slice(0, rv).join("")}<span>\\</span>${V.slice(rv).join("")}</th>${C.map(c => `<th>${bin(c, cv)}</th>`).join("")}</tr>`;
      R.forEach((r, ri) => { h += `<tr><th>${bin(r, rv)}</th>`; C.forEach((c, ci) => { const m = idx(ri, ci), v = cells[m];
        const dots = s.groups.map((g, gi) => g.ms.includes(m) ? `<i style="background:${CL[gi % CL.length]}"></i>` : "").join("");
        h += `<td class="k${v}" data-m="${m}"><b>${v === 2 ? "X" : v}</b><small>m${m}</small><span class="gd">${dots}</span></td>`; }); h += "</tr>"; });
      km.innerHTML = h + "</table>";
      const ones = cells.map((c, i) => c === 1 ? i : -1).filter(i => i >= 0), dc = cells.map((c, i) => c === 2 ? i : -1).filter(i => i >= 0);
      ko.innerHTML = `<div class="xl-k1">F(${V.join(",")}) = Σm(${ones.join(", ") || "–"})${dc.length ? ` + d(${dc.join(", ")})` : ""}</div>
        <div class="xl-k2">Simplest: <b>F = ${s.expr}</b></div>
        <ul class="xl-kg" data-e="${esc(s.expr)}">${s.groups.map((g, gi) => `<li data-g="${gi}"><i style="background:${CL[gi % CL.length]}"></i><b>${g.t}</b> covers m${g.ms.join(", m")} <small>(group of ${g.ms.length})</small></li>`).join("")}</ul>`;
    }
    const _kd = draw; draw = function () { _kd(); emit(el, { expr: solve().expr, ones: cells.map((c, i) => c === 1 ? i : -1).filter(i => i >= 0) }); };
    km.addEventListener("click", e => { const td = e.target.closest("td[data-m]"); if (!td) return; const m = +td.dataset.m; cells[m] = (cells[m] + 1) % 3; draw(); });
    ko.addEventListener("mouseover", e => { const li = e.target.closest("[data-g]"); km.querySelectorAll("td").forEach(td => td.classList.remove("hi")); if (!li) return; const s = solve().groups[+li.dataset.g]; s && s.ms.forEach(m => { const td = km.querySelector(`td[data-m="${m}"]`); td && td.classList.add("hi"); }); });
    ko.addEventListener("mouseleave", () => km.querySelectorAll("td").forEach(td => td.classList.remove("hi")));
    el.querySelector(".mg-ctl").addEventListener("click", e => { const a = e.target.closest("[data-act]"); if (!a) return; if (a.dataset.act === "clear") cells.fill(0); else for (let i = 0; i < N; i++) cells[i] = Math.random() < .45 ? 1 : 0; draw(); });
    draw();
  }

  /* ---- flip-flops with timing diagram ---- */
  function flipflop(el, p) {
    const types = p.types || ["D", "T", "JK", "SR"]; let type = p.ff || types[0], Q = 0; const inp = { D: 0, T: 0, J: 0, K: 0, S: 0, R: 0 }; let hist = [], timer = null;
    const IN = { D: ["D"], T: ["T"], JK: ["J", "K"], SR: ["S", "R"] };
    const next = () => { if (type === "D") return inp.D; if (type === "T") return inp.T ? 1 - Q : Q; if (type === "JK") return inp.J && inp.K ? 1 - Q : inp.J ? 1 : inp.K ? 0 : Q; if (type === "SR") return inp.S && inp.R ? "?" : inp.S ? 1 : inp.R ? 0 : Q; };
    const TABLE = { D: [["D=0", "0"], ["D=1", "1"]], T: [["T=0", "Q (hold)"], ["T=1", "Q′ (toggle)"]], JK: [["J=0 K=0", "Q (hold)"], ["J=0 K=1", "0 (reset)"], ["J=1 K=0", "1 (set)"], ["J=1 K=1", "Q′ (toggle)"]], SR: [["S=0 R=0", "Q (hold)"], ["S=0 R=1", "0 (reset)"], ["S=1 R=0", "1 (set)"], ["S=1 R=1", "not allowed"]] };
    el.innerHTML = head(p, "Flip-flops and the clock", "Set the inputs, then send a clock pulse. Q only changes on the rising edge.") +
      `<div class="xl-tabs">${types.map(t => `<button type="button" class="mg-b sm" data-t="${t}">${t} flip-flop</button>`).join("")}</div>
      <div class="xl-ffrow"><div class="xl-ffin"></div><div class="xl-ffq"></div><div class="xl-tt"></div></div><svg class="xl-svg xl-wave"></svg>
      <div class="mg-ctl">${B("clk", "Clock pulse ⎍", "solid")}${B("auto", "Auto clock")}${B("reset", "Clear")}</div>`;
    const fin = el.querySelector(".xl-ffin"), fq = el.querySelector(".xl-ffq"), tt = el.querySelector(".xl-tt"), wv = el.querySelector(".xl-wave");
    function draw() {
      const P = PAL(), names = IN[type];
      fin.innerHTML = names.map(n => `<button type="button" class="xl-bit sm ${inp[n] ? "on" : ""}" data-n="${n}"><b>${inp[n]}</b><small>${n}</small></button>`).join("");
      fq.innerHTML = `<div class="xl-q ${Q === 1 ? "on" : ""}"><small>Q</small><b>${Q}</b></div><div class="xl-q ${Q === 0 ? "on" : ""} inv"><small>Q′</small><b>${Q === "?" ? "?" : 1 - Q}</b></div>`;
      const cur = type === "D" ? inp.D : type === "T" ? inp.T : type === "JK" ? inp.J * 2 + inp.K : inp.S * 2 + inp.R;
      tt.innerHTML = `<table><tr><th>Inputs at edge</th><th>Next Q</th></tr>${TABLE[type].map((r, i) => `<tr class="${i === cur ? "cur" : ""}"><td>${r[0]}</td><td><b>${r[1]}</b></td></tr>`).join("")}</table>`;
      const sig = ["CLK", ...names, "Q"], cols = 12, cw = 46, rh = 34, W = 70 + cols * cw, H = sig.length * rh + 10, h0 = hist.slice(-cols);
      let s = "";
      sig.forEach((nm, si) => { const y0 = 8 + si * rh, hi = y0 + 4, lo = y0 + 24; s += `<text x="8" y="${y0 + 20}" font-family="JetBrains Mono" font-weight="700" font-size="12" fill="${P.ink}">${nm}</text>`;
        let d = "", px = 70, py = null;
        h0.forEach((rec, k) => { const x = 70 + k * cw;
          if (nm === "CLK") { d += `${k ? "L" : "M"}${x} ${lo}L${x} ${hi}L${x + cw / 2} ${hi}L${x + cw / 2} ${lo}L${x + cw} ${lo}`; return; }
          const v = nm === "Q" ? rec.q : rec.i[nm], y = v === "?" ? (hi + lo) / 2 : v ? hi : lo;
          d += py == null ? `M${x} ${y}` : `L${x} ${py}L${x} ${y}`; d += `L${x + cw} ${y}`; py = y; px = x + cw; });
        s += `<path d="${d}" fill="none" stroke="${nm === "Q" ? P.a : nm === "CLK" ? P.ink : P.b}" stroke-width="2.4"/>`; });
      h0.forEach((_, k) => { s += `<line x1="${70 + k * cw}" y1="4" x2="${70 + k * cw}" y2="${H - 4}" stroke="rgba(100,116,139,.25)" stroke-dasharray="3 4"/>`; });
      if (!h0.length) s += `<text x="${W / 2}" y="${H / 2}" text-anchor="middle" font-family="Plus Jakarta Sans" font-size="14" fill="${P.muted}">Press “Clock pulse” to draw the timing diagram.</text>`;
      wv.setAttribute("viewBox", `0 0 ${W} ${H}`); wv.innerHTML = s;
      el.querySelectorAll("[data-t]").forEach(b => b.classList.toggle("on", b.dataset.t === type));
    }
    function pulse() { const q = next(); const rec = { i: Object.assign({}, inp), q }; Q = q === "?" ? "?" : q; hist.push(rec); if (Q === "?") Q = 0; draw(); }
    fin.addEventListener("click", e => { const b = e.target.closest("[data-n]"); if (b) { inp[b.dataset.n] ^= 1; draw(); } });
    el.querySelector(".xl-tabs").addEventListener("click", e => { const b = e.target.closest("[data-t]"); if (b) { type = b.dataset.t; hist = []; Q = 0; draw(); } });
    el.querySelector(".mg-ctl").addEventListener("click", e => { const a = e.target.closest("[data-act]"); if (!a) return;
      if (a.dataset.act === "clk") pulse(); if (a.dataset.act === "reset") { hist = []; Q = 0; draw(); }
      if (a.dataset.act === "auto") { if (timer) { clearInterval(timer); timer = null; a.classList.remove("on"); } else { timer = setInterval(pulse, 900); a.classList.add("on"); } } });
    draw();
  }

  /* ---- finite state machine ---- */
  function fsm(el, p) {
    const S = p.states, T = p.trans, ins = p.inputs; let cur = p.start || S[0].id, hist = [];
    el.innerHTML = head(p, "State machine", "Feed it inputs one at a time and watch the state change.") +
      `<svg class="xl-svg xl-fsm"></svg><div class="mg-ctl">${ins.map(i => B("in:" + i, "Input " + esc(i), "solid")).join("")}${B("reset", "Reset")}</div><div class="xl-hist"></div>`;
    const sv = el.querySelector("svg"), hs = el.querySelector(".xl-hist");
    const W = 560, H = p.h || 300, cx = W / 2, cy = H / 2, rad = Math.min(W, H) / 2 - 56, pos = {};
    S.forEach((s, i) => { const a = -Math.PI / 2 + i * 2 * Math.PI / S.length; pos[s.id] = s.xy ? { x: s.xy[0] * W, y: s.xy[1] * H } : { x: cx + rad * 1.35 * Math.cos(a), y: cy + rad * Math.sin(a) }; });
    function draw(lastEdge) {
      const P = PAL(); let s = `<defs><marker id="ah${el._id}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="${P.ink}"/></marker><marker id="ahh${el._id}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="${P.a}"/></marker></defs>`;
      const grouped = {}; T.forEach((t, i) => { const k = t[0] + ">" + t[2]; (grouped[k] = grouped[k] || []).push([t, i]); });
      Object.values(grouped).forEach(list => { const [t] = list[0], a = pos[t[0]], b = pos[t[2]], hot = list.some(([, i]) => i === lastEdge), col = hot ? P.a : P.ink, mk = hot ? `ahh${el._id}` : `ah${el._id}`;
        const lbl = list.map(([t]) => t[1] + (t[3] != null ? "/" + t[3] : "")).join(", ");
        if (t[0] === t[2]) { const so = S.find(x => x.id === t[0]), mx0 = S.reduce((s2, x) => s2 + pos[x.id].x, 0) / S.length, my0 = S.reduce((s2, x) => s2 + pos[x.id].y, 0) / S.length; const ang = so.loop != null ? so.loop * Math.PI / 180 : (Math.atan2(a.y - my0, a.x - mx0) || -Math.PI / 2), ux = Math.cos(ang), uy = Math.sin(ang), bx = a.x + ux * 30, by = a.y + uy * 30;
          const p1x = a.x + Math.cos(ang - .5) * 30, p1y = a.y + Math.sin(ang - .5) * 30, p2x = a.x + Math.cos(ang + .5) * 30, p2y = a.y + Math.sin(ang + .5) * 30;
          s += `<path d="M${p1x} ${p1y}C${bx + ux * 40 - uy * 30} ${by + uy * 40 + ux * 30} ${bx + ux * 40 + uy * 30} ${by + uy * 40 - ux * 30} ${p2x} ${p2y}" fill="none" stroke="${col}" stroke-width="${hot ? 3 : 1.8}" marker-end="url(#${mk})"/>
            <text x="${bx + ux * 44}" y="${by + uy * 44 + 4}" text-anchor="middle" font-family="JetBrains Mono" font-size="12.5" font-weight="700" fill="${col}" class="xl-lb">${esc(lbl)}</text>`; return; }
        const both = T.some(x => x[0] === t[2] && x[2] === t[0]), dx = b.x - a.x, dy = b.y - a.y, L = Math.hypot(dx, dy), nx = -dy / L, ny = dx / L, off = both ? 34 : 0;
        const mx = (a.x + b.x) / 2 + nx * off, my = (a.y + b.y) / 2 + ny * off;
        const sx = a.x + dx / L * 30 + nx * (both ? 8 : 0), sy = a.y + dy / L * 30 + ny * (both ? 8 : 0), ex = b.x - dx / L * 31 + nx * (both ? 8 : 0), ey = b.y - dy / L * 31 + ny * (both ? 8 : 0);
        s += `<path d="M${sx} ${sy}Q${mx} ${my} ${ex} ${ey}" fill="none" stroke="${col}" stroke-width="${hot ? 3 : 1.8}" marker-end="url(#${mk})"/>
          <text x="${(sx + 2 * mx + ex) / 4 + nx * (both ? 13 : 12)}" y="${(sy + 2 * my + ey) / 4 + ny * (both ? 13 : 12) + 4}" text-anchor="middle" font-family="JetBrains Mono" font-size="12.5" font-weight="700" fill="${col}" class="xl-lb">${esc(lbl)}</text>`; });
      S.forEach(st => { const q = pos[st.id], on = st.id === cur;
        s += `<circle cx="${q.x}" cy="${q.y}" r="28" fill="${on ? P.a : "#fff"}" stroke="${on ? P.a : P.ink}" stroke-width="2.2" class="${on ? "xl-glow" : ""}"/>${st.accept ? `<circle cx="${q.x}" cy="${q.y}" r="23" fill="none" stroke="${on ? "#fff" : P.ink}" stroke-width="1.5"/>` : ""}
          <text x="${q.x}" y="${q.y + (st.out != null ? 0 : 5)}" text-anchor="middle" font-family="JetBrains Mono" font-weight="800" font-size="14" fill="${on ? "#fff" : P.ink}">${esc(st.label || st.id)}</text>
          ${st.out != null ? `<text x="${q.x}" y="${q.y + 15}" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="${on ? "#fff" : P.muted}">out ${esc(st.out)}</text>` : ""}`; });
      const st0 = pos[p.start || S[0].id], sa = (p.startAng ?? 225) * Math.PI / 180, sux = Math.cos(sa), suy = Math.sin(sa); s += `<path d="M${st0.x + sux * 70} ${st0.y + suy * 70}L${st0.x + sux * 31} ${st0.y + suy * 31}" stroke="${P.ink}" stroke-width="1.8" marker-end="url(#ah${el._id})"/><text x="${st0.x + sux * 72}" y="${st0.y + suy * 72 - 5}" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="${P.muted}">start</text>`;
      sv.setAttribute("viewBox", `0 0 ${W} ${H}`); sv.innerHTML = s;
      const so = S.find(x => x.id === cur); emit(el, { state: cur, ins: hist.map(h => h.i).join(""), outs: hist.map(h => h.o).join("") });
      hs.innerHTML = hist.length ? `<span>Inputs: <b>${hist.map(h => esc(h.i)).join(" ")}</b></span><span>Outputs: <b>${hist.map(h => esc(h.o)).join(" ")}</b></span>` : `<span>Current state <b>${esc(so.label || so.id)}</b>${so.out != null ? `, output <b>${esc(so.out)}</b>` : ""}</span>`;
    }
    el._id = Math.random().toString(36).slice(2, 7);
    el.querySelector(".mg-ctl").addEventListener("click", e => { const a = e.target.closest("[data-act]"); if (!a) return;
      if (a.dataset.act === "reset") { cur = p.start || S[0].id; hist = []; draw(); return; }
      const i = a.dataset.act.slice(3), k = T.findIndex(t => t[0] === cur && String(t[1]) === i); if (k < 0) return;
      cur = T[k][2]; const st = S.find(x => x.id === cur); hist.push({ i, o: T[k][3] != null ? T[k][3] : st.out != null ? st.out : st.label || st.id }); if (hist.length > 24) hist.shift(); draw(k); });
    draw();
  }

  /* ---- tiny accumulator CPU ---- */
  const OPS = { HALT: 0, LOAD: 1, STORE: 2, ADD: 3, SUB: 4, JMP: 5, JZ: 6, OUT: 7, JN: 8 };
  const OPN = Object.fromEntries(Object.entries(OPS).map(([k, v]) => [v, k]));
  function cpu(el, p) {
    const progs = p.progs; let pi = 0, M, R, phase, log, done, timer = null;
    function load() { const pr = progs[pi]; M = new Array(16).fill(0); pr.code.forEach((ins, a) => { M[a] = (OPS[ins[0]] << 4) | ((ins[1] || 0) & 15); }); Object.entries(pr.data || {}).forEach(([a, v]) => M[+a] = v & 255); R = { PC: 0, IR: 0, ACC: 0, MAR: 0, MDR: 0 }; phase = 0; log = []; done = false; }
    el.innerHTML = head(p, "Inside the CPU: fetch, decode, execute", "Step through one phase at a time. Highlighted cells are being read (blue) or written (orange).") +
      `<div class="xl-tabs">${progs.map((pr, i) => `<button type="button" class="mg-b sm" data-p="${i}">${esc(pr.name)}</button>`).join("")}</div>
      <div class="xl-cpu"><div class="xl-regs"></div><div class="xl-mem"></div></div><div class="xl-phase"></div><div class="xl-outlog"></div>
      <div class="mg-ctl">${B("step", "Step ▸", "solid")}${B("ins", "Whole instruction ▸▸")}${B("run", "Run")}${B("reset", "Reset")}</div>`;
    const rg = el.querySelector(".xl-regs"), mem = el.querySelector(".xl-mem"), ph = el.querySelector(".xl-phase"), ol = el.querySelector(".xl-outlog");
    const sgn = v => v > 127 ? v - 256 : v;
    function dis(w) { const o = OPN[w >> 4], a = w & 15; return o ? (["HALT", "OUT"].includes(o) ? o : `${o} ${a}`) : "?"; }
    let hl = {}, msg = "Press Step to fetch the first instruction.";
    function step() {
      if (done) return; hl = {};
      if (phase === 0) { R.MAR = R.PC; hl.r = R.PC; msg = `<b>Fetch 1.</b> Copy the program counter into the memory address register: MAR ← PC = ${R.PC}.`; phase = 1; }
      else if (phase === 1) { R.MDR = M[R.MAR]; R.IR = R.MDR; R.PC = (R.PC + 1) & 15; hl.r = R.MAR; msg = `<b>Fetch 2.</b> Read memory[${R.MAR}] = ${bn(R.IR)} into the instruction register, then PC ← PC + 1 = ${R.PC}.`; phase = 2; }
      else if (phase === 2) { const o = OPN[R.IR >> 4] || "?"; msg = `<b>Decode.</b> Top 4 bits ${bn(R.IR >> 4, 4)} = opcode <b>${o}</b>; bottom 4 bits ${bn(R.IR & 15, 4)} = address <b>${R.IR & 15}</b>.`; phase = 3; }
      else {
        const o = OPN[R.IR >> 4], a = R.IR & 15;
        if (o === "LOAD") { R.MAR = a; R.MDR = M[a]; R.ACC = M[a]; hl.r = a; msg = `<b>Execute LOAD.</b> ACC ← memory[${a}] = ${sgn(M[a])}.`; }
        else if (o === "STORE") { R.MAR = a; R.MDR = R.ACC; M[a] = R.ACC; hl.w = a; msg = `<b>Execute STORE.</b> memory[${a}] ← ACC = ${sgn(R.ACC)}.`; }
        else if (o === "ADD") { R.MAR = a; R.MDR = M[a]; const r = (R.ACC + M[a]) & 255; msg = `<b>Execute ADD.</b> ACC ← ${sgn(R.ACC)} + ${sgn(M[a])} = ${sgn(r)} (the ALU does the adding).`; R.ACC = r; hl.r = a; }
        else if (o === "SUB") { R.MAR = a; R.MDR = M[a]; const r = (R.ACC - M[a]) & 255; msg = `<b>Execute SUB.</b> ACC ← ${sgn(R.ACC)} − ${sgn(M[a])} = ${sgn(r)}.`; R.ACC = r; hl.r = a; }
        else if (o === "JMP") { R.PC = a; msg = `<b>Execute JMP.</b> PC ← ${a}, so the next fetch comes from address ${a}.`; }
        else if (o === "JZ") { if (R.ACC === 0) { R.PC = a; msg = `<b>Execute JZ.</b> ACC is 0, so jump: PC ← ${a}.`; } else msg = `<b>Execute JZ.</b> ACC is ${sgn(R.ACC)}, not 0, so don't jump. PC stays ${R.PC}.`; }
        else if (o === "JN") { if (R.ACC > 127) { R.PC = a; msg = `<b>Execute JN.</b> ACC is negative, so jump: PC ← ${a}.`; } else msg = `<b>Execute JN.</b> ACC is not negative, so don't jump.`; }
        else if (o === "OUT") { log.push(sgn(R.ACC)); msg = `<b>Execute OUT.</b> Send ACC = ${sgn(R.ACC)} to the output.`; }
        else { done = true; msg = `<b>HALT.</b> The program is finished.`; stop(); }
        if (log.length > 40) { done = true; msg += " Stopped after 40 outputs."; stop(); }
        phase = 0;
      }
      draw();
    }
    const bn = (v, w = 8) => v.toString(2).padStart(w, "0");
    function draw() {
      rg.innerHTML = [["PC", "Program counter", R.PC, 4], ["MAR", "Memory address reg.", R.MAR, 4], ["MDR", "Memory data reg.", R.MDR, 8], ["IR", "Instruction reg.", R.IR, 8], ["ACC", "Accumulator", R.ACC, 8]].map(([k, d, v, w]) =>
        `<div class="xl-reg"><small>${d}</small><b>${k}</b><code>${bn(v, w)}</code><em>${k === "IR" ? dis(v) : k === "ACC" || k === "MDR" ? sgn(v) : v}</em></div>`).join("") +
        `<div class="xl-reg alu ${phase === 0 && /ADD|SUB/.test(OPN[R.IR >> 4] || "") ? "on" : ""}"><small>Flags</small><b>Z</b><code>${R.ACC === 0 ? 1 : 0}</code><em>${R.ACC === 0 ? "ACC is zero" : "ACC ≠ 0"}</em></div>`;
      mem.innerHTML = `<table><tr><th>Addr</th><th>Binary</th><th>As code</th><th>As data</th></tr>${M.map((w, a) => `<tr class="${a === R.PC && !done ? "pc" : ""} ${hl.r === a ? "rd" : ""} ${hl.w === a ? "wr" : ""}"><td>${a}</td><td><code>${bn(w)}</code></td><td>${dis(w)}</td><td>${sgn(w)}</td></tr>`).join("")}</table>`;
      ph.innerHTML = `<div class="xl-pills">${["Fetch 1", "Fetch 2", "Decode", "Execute"].map((n, i) => `<span class="${(phase + 3) % 4 === i && msg.indexOf("Press") < 0 ? "on" : ""}">${n}</span>`).join("")}</div><p>${msg}</p>`;
      ol.innerHTML = `Output: <b>${log.length ? log.join(", ") : "(nothing yet)"}</b>`;
      el.querySelectorAll("[data-p]").forEach(b => b.classList.toggle("on", +b.dataset.p === pi));
      emit(el, { out: log.slice(), done, prog: pi });
    }
    function stop() { if (timer) { clearInterval(timer); timer = null; const b = el.querySelector('[data-act="run"]'); b && b.classList.remove("on"); } }
    el.querySelector(".mg-ctl").addEventListener("click", e => { const a = e.target.closest("[data-act]"); if (!a) return; const k = a.dataset.act;
      if (k === "step") step(); if (k === "ins") { do step(); while (phase !== 0 && !done); }
      if (k === "reset") { stop(); load(); hl = {}; msg = "Press Step to fetch the first instruction."; draw(); }
      if (k === "run") { if (timer) stop(); else { timer = setInterval(() => { step(); if (done) stop(); }, still() ? 60 : 380); a.classList.add("on"); } } });
    el.querySelector(".xl-tabs").addEventListener("click", e => { const b = e.target.closest("[data-p]"); if (!b) return; stop(); pi = +b.dataset.p; load(); hl = {}; msg = esc(progs[pi].desc || "Press Step to fetch the first instruction."); draw(); });
    load(); msg = esc(progs[0].desc || msg); draw();
  }

  /* ---- cache simulator ---- */
  function cache(el, p) {
    const addrBits = p.addrBits || 6; let lines = p.lines || 4, block = p.block || 1, ways = p.ways || 1, seqs = p.seqs || [];
    let sets, hits = 0, miss = 0, t = 0, hist = [], qi = 0, seq = (seqs[0] || {}).a || [];
    function reset() { const ns = lines / ways; sets = Array.from({ length: ns }, () => Array.from({ length: ways }, () => ({ v: 0, tag: 0, used: 0 }))); hits = 0; miss = 0; t = 0; hist = []; qi = 0; }
    el.innerHTML = head(p, "Cache simulator", "Each memory access is a hit (already in the cache) or a miss (has to be loaded). Watch how the address splits into tag, index and offset.") +
      `<div class="mg-ctl xl-cfg"><span>Layout</span>${B("w1", "Direct-mapped", "sm")}${B("w2", "2-way set associative", "sm")}<span>Block size</span>${B("b1", "1 byte", "sm")}${B("b2", "2 bytes", "sm")}${B("b4", "4 bytes", "sm")}</div>
      <div class="xl-split"></div><div class="xl-cwrap"><div class="xl-ctab"></div><div class="xl-clog"></div></div>
      <div class="mg-ctl"><label class="xl-in">Address <input type="number" class="xl-num" min="0" max="${(1 << addrBits) - 1}" value="${seq[0] ?? 0}"></label>${B("go", "Access", "solid")}${seqs.map((s, i) => B("seq" + i, "Play: " + esc(s.name))).join("")}${B("reset", "Clear cache")}</div>`;
    const sp = el.querySelector(".xl-split"), ct = el.querySelector(".xl-ctab"), lg = el.querySelector(".xl-clog"), num = el.querySelector(".xl-num");
    const lg2 = x => Math.round(Math.log2(x));
    function split(a) { const ob = lg2(block), ib = lg2(lines / ways); return { off: a & (block - 1), idx: (a >> ob) & ((1 << ib) - 1), tag: a >> (ob + ib), ob, ib, tb: addrBits - ob - ib }; }
    let last = null;
    function access(a) {
      a = Math.max(0, Math.min((1 << addrBits) - 1, a | 0)); const s = split(a), set = sets[s.idx]; t++;
      let w = set.findIndex(l => l.v && l.tag === s.tag), hit = w >= 0;
      if (hit) hits++; else { miss++; w = set.findIndex(l => !l.v); if (w < 0) w = set.reduce((bi, l, i) => l.used < set[bi].used ? i : bi, 0); const ev = set[w].v ? set[w].tag : null; set[w] = { v: 1, tag: s.tag, used: 0 }; s.ev = ev; }
      set[w].used = t; last = { a, s, hit, w }; hist.push(last); draw();
    }
    function draw() {
      const s = split(last ? last.a : +num.value || 0), a = last ? last.a : +num.value || 0, b = a.toString(2).padStart(addrBits, "0");
      sp.innerHTML = `<div class="xl-abits">${[...b].map((c, i) => `<span class="${i < s.tb ? "t" : i < s.tb + s.ib ? "i" : "o"}">${c}</span>`).join("")}</div>
        <div class="xl-alab"><span class="t">tag ${s.tb} bits = ${s.tag}</span>${s.ib ? `<span class="i">index ${s.ib} bits = set ${s.idx}</span>` : `<span class="i">no index bits (1 set)</span>`}${s.ob ? `<span class="o">offset ${s.ob} bits = byte ${s.off}</span>` : `<span class="o">no offset (1-byte blocks)</span>`}</div>
        ${last ? `<div class="xl-verdict ${last.hit ? "hit" : "miss"}">Address ${last.a}: <b>${last.hit ? "HIT" : "MISS"}</b>${!last.hit ? (last.s.ev != null ? ` — evicted tag ${last.s.ev} from set ${last.s.idx}` : ` — loaded into empty line in set ${last.s.idx}`) : ` — tag ${last.s.tag} is already in set ${last.s.idx}`}</div>` : ""}`;
      ct.innerHTML = `<table><tr><th>Set</th>${ways > 1 ? "<th>Way</th>" : ""}<th>Valid</th><th>Tag</th><th>Holds addresses</th></tr>${sets.map((set, si) => set.map((l, wi) => {
        const lo = ((l.tag << lg2(lines / ways)) | si) << lg2(block); const on = last && last.s.idx === si && last.w === wi;
        return `<tr class="${on ? (last.hit ? "hit" : "miss") : ""}">${wi === 0 ? `<td rowspan="${ways}">${si}</td>` : ""}${ways > 1 ? `<td>${wi}</td>` : ""}<td>${l.v}</td><td>${l.v ? l.tag : "–"}</td><td>${l.v ? (block > 1 ? `${lo}–${lo + block - 1}` : lo) : "empty"}</td></tr>`; }).join("")).join("")}</table>`;
      const tot = hits + miss;
      lg.innerHTML = `<div class="xl-hr"><span>Hits <b>${hits}</b></span><span>Misses <b>${miss}</b></span><span>Hit rate <b>${tot ? Math.round(hits / tot * 100) + "%" : "–"}</b></span></div><div class="xl-seq">${hist.slice(-28).map(h => `<span class="${h.hit ? "hit" : "miss"}">${h.a}</span>`).join("")}</div>`;
      el.querySelectorAll("[data-act^=w],[data-act^=b]").forEach(x => x.classList.toggle("on", x.dataset.act === "w" + ways || x.dataset.act === "b" + block));
      emit(el, { hits, miss, total: tot, rate: tot ? hits / tot : 0, ways, block, seq: hist.map(h => h.a) });
    }
    let timer = null;
    el.addEventListener("click", e => { const x = e.target.closest("[data-act]"); if (!x) return; const k = x.dataset.act;
      if (k === "go") { access(+num.value); return; }
      if (k === "reset") { clearInterval(timer); reset(); last = null; draw(); return; }
      if (k[0] === "w") { ways = +k.slice(1); reset(); last = null; draw(); return; }
      if (k[0] === "b" && k.length === 2) { block = +k.slice(1); reset(); last = null; draw(); return; }
      if (k.startsWith("seq")) { clearInterval(timer); reset(); last = null; const list = seqs[+k.slice(3)].a; let i = 0; const go = () => { if (i >= list.length) { clearInterval(timer); return; } num.value = list[i]; access(list[i++]); }; go(); timer = setInterval(go, still() ? 80 : 650); } });
    num.addEventListener("keydown", e => { if (e.key === "Enter") access(+num.value); });
    reset(); draw();
  }

  /* ---- Ohm's law: series and parallel ---- */
  function ohm(el, p) {
    const S = {}; let mode = p.mode || "series", raf = 0, ph = 0;
    el.innerHTML = head(p, "Ohm's law circuit", "Change the battery and resistors. Dots show the current: faster dots mean more amps.") +
      `<div class="mg-ctl">${B("series", "Series", "sm")}${B("parallel", "Parallel", "sm")}</div><div class="mg-sl">${slider("V", "V", 1, 24, 1, p.V || 12)}${slider("R1", "R₁", 1, 100, 1, p.R1 || 20)}${slider("R2", "R₂", 1, 100, 1, p.R2 || 40)}</div>
      <svg class="xl-svg xl-ohm" viewBox="0 0 560 250"></svg><div class="xl-read xl-ohmr"></div>`;
    const sv = el.querySelector("svg"), rd = el.querySelector(".xl-ohmr");
    const fmt = { V: v => v + " V", R1: v => v + " Ω", R2: v => v + " Ω" };
    function calc() { const { V, R1, R2 } = S; if (mode === "series") { const R = R1 + R2, I = V / R; return { R, I, I1: I, I2: I, V1: I * R1, V2: I * R2 }; } const R = R1 * R2 / (R1 + R2), I = V / R; return { R, I, I1: V / R1, I2: V / R2, V1: V, V2: V }; }
    function res(x, y, vert) { return vert ? `<path d="M${x} ${y}l0 8l-9 5l18 8l-18 8l18 8l-18 8l18 8l-9 5l0 8" fill="none" stroke-width="3" stroke-linejoin="round"/>` : `<path d="M${x} ${y}l8 0l5 -9l8 18l8 -18l8 18l8 -18l8 18l5 -9l8 0" fill="none" stroke-width="3" stroke-linejoin="round"/>`; }
    function draw() {
      const P = PAL(), c = calc(); let s = `<g stroke="${P.ink}" fill="none" stroke-width="3">`;
      // battery
      s += `<path d="M60 200V140M60 110V50"/><path d="M40 140H80" stroke-width="4"/><path d="M48 110H72" stroke-width="7"/>`;
      s += `<text x="20" y="130" fill="${P.ink}" stroke="none" font-family="JetBrains Mono" font-weight="700" font-size="14">${S.V}V</text>`;
      let path;
      if (mode === "series") {
        s += `<path d="M60 50H180"/>${res(180, 50)}<path d="M254 50H400"/>${res(400, 50)}<path d="M474 50H510V200H60"/>`;
        s += `<text x="220" y="30" fill="${P.ink}" stroke="none" font-family="JetBrains Mono" font-weight="700" font-size="13" text-anchor="middle">R₁ ${S.R1}Ω · ${fm(c.V1, 2)}V</text><text x="440" y="30" fill="${P.ink}" stroke="none" font-family="JetBrains Mono" font-weight="700" font-size="13" text-anchor="middle">R₂ ${S.R2}Ω · ${fm(c.V2, 2)}V</text>`;
        path = [[60, 50], [510, 50], [510, 200], [60, 200], [60, 50]];
      } else {
        s += `<path d="M60 50H300M300 50H460M60 200H460"/><path d="M300 50V85"/>${res(300, 85, true)}<path d="M300 159V200"/><path d="M460 50V85"/>${res(460, 85, true)}<path d="M460 159V200"/>`;
        s += `<text x="318" y="130" fill="${P.ink}" stroke="none" font-family="JetBrains Mono" font-weight="700" font-size="13">R₁ ${S.R1}Ω</text><text x="318" y="148" fill="${P.muted}" stroke="none" font-family="JetBrains Mono" font-size="12">${fm(c.I1 * 1000, 0)} mA</text>
          <text x="478" y="130" fill="${P.ink}" stroke="none" font-family="JetBrains Mono" font-weight="700" font-size="13">R₂ ${S.R2}Ω</text><text x="478" y="148" fill="${P.muted}" stroke="none" font-family="JetBrains Mono" font-size="12">${fm(c.I2 * 1000, 0)} mA</text>`;
      }
      s += `</g><g class="xl-dots"></g>`;
      sv.innerHTML = s;
      rd.innerHTML = `<span>Total resistance <b>${fm(c.R, 2)} Ω</b></span><span>Total current <b>${fm(c.I, 3)} A</b></span><span>Power <b>${fm(S.V * c.I, 2)} W</b></span>
        <span class="xl-sum">${mode === "series" ? `Series: R = R₁ + R₂ = ${S.R1} + ${S.R2} = ${S.R1 + S.R2} Ω. Same current everywhere; the voltage splits ${fm(c.V1, 2)} V + ${fm(c.V2, 2)} V = ${S.V} V.` : `Parallel: 1/R = 1/${S.R1} + 1/${S.R2}, so R = ${fm(c.R, 2)} Ω. Same voltage on each branch; the currents add: ${fm(c.I1, 3)} + ${fm(c.I2, 3)} = ${fm(c.I, 3)} A.`}</span>`;
      el.querySelectorAll("[data-act]").forEach(b => b.classList.toggle("on", b.dataset.act === mode));
    }
    function anim() {
      const g = sv.querySelector(".xl-dots"); if (!g) return; const P = PAL(), c = calc(); ph += still() ? 0 : c.I * 6; let s = "";
      const loop = mode === "series" ? [[60, 50], [510, 50], [510, 200], [60, 200], [60, 50]] : null;
      const along = (pts, d) => { let L = 0; const seg = []; for (let i = 1; i < pts.length; i++) { const l = Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]); seg.push(l); L += l; } d = ((d % L) + L) % L; for (let i = 0; i < seg.length; i++) { if (d <= seg[i]) { const f = d / seg[i]; return [pts[i][0] + (pts[i + 1][0] - pts[i][0]) * f, pts[i][1] + (pts[i + 1][1] - pts[i][1]) * f]; } d -= seg[i]; } return pts[0]; };
      if (loop) for (let k = 0; k < 18; k++) { const [x, y] = along(loop, ph + k * 54); s += `<circle cx="${x}" cy="${y}" r="4" fill="${P.b}"/>`; }
      else { const b1 = [[60, 50], [300, 50], [300, 200], [60, 200], [60, 50]], b2 = [[60, 50], [460, 50], [460, 200], [60, 200], [60, 50]];
        for (let k = 0; k < 10; k++) { const [x, y] = along(b1, ph * c.I1 / c.I + k * 61); s += `<circle cx="${x}" cy="${y}" r="4" fill="${P.b}"/>`; const [x2, y2] = along(b2, ph * c.I2 / c.I + k * 77 + 30); s += `<circle cx="${x2}" cy="${y2}" r="4" fill="${P.a}"/>`; } }
      g.innerHTML = s; raf = requestAnimationFrame(anim);
    }
    bindSliders(el, S, draw, fmt);
    el.addEventListener("click", e => { const b = e.target.closest("[data-act]"); if (b) { mode = b.dataset.act; draw(); } });
    draw(); anim();
  }

  /* ---- CMOS gates ---- */
  function cmos(el, p) {
    const list = p.gates || ["NOT", "NAND", "NOR"]; let cur = list[0], A = 0, Bv = 0;
    el.innerHTML = head(p, "CMOS transistors", "PMOS transistors (top) turn on when their input is 0. NMOS transistors (bottom) turn on when their input is 1.") +
      `<div class="xl-tabs">${list.map(g => `<button type="button" class="mg-b sm" data-g="${g}">${g}</button>`).join("")}</div><div class="mg-ctl">${B("A", "Toggle A")}${B("B", "Toggle B")}</div><svg class="xl-svg xl-cmos" viewBox="0 0 520 330"></svg><p class="xl-note"></p>`;
    const sv = el.querySelector("svg"), note = el.querySelector(".xl-note");
    function tr(x, y, kind, inp, on, P) {
      const col = on ? P.on : "#94A3B8";
      return `<g><rect x="${x - 34}" y="${y - 22}" width="68" height="44" rx="8" fill="${on ? "rgba(22,163,74,.12)" : "#fff"}" stroke="${col}" stroke-width="2.4"/>
        <text x="${x}" y="${y - 3}" text-anchor="middle" font-family="JetBrains Mono" font-weight="800" font-size="13" fill="${P.ink}">${kind} ${inp}</text>
        <text x="${x}" y="${y + 14}" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="${col}">${on ? "ON" : "off"}</text>${kind === "P" ? `<circle cx="${x - 40}" cy="${y}" r="4" fill="#fff" stroke="${P.ink}" stroke-width="1.6"/>` : ""}</g>`;
    }
    function draw() {
      const P = PAL(), a = A, b = Bv, out = cur === "NOT" ? !a : cur === "NAND" ? !(a && b) : !(a || b), W = (on) => on ? P.on : "#A8B3C4";
      let s = `<text x="260" y="22" text-anchor="middle" font-family="JetBrains Mono" font-weight="700" font-size="13" fill="${P.ink}">VDD (1)</text><path d="M120 32H400" stroke="${P.b}" stroke-width="4"/>
        <path d="M120 310H400" stroke="${P.ink}" stroke-width="4"/><text x="260" y="328" text-anchor="middle" font-family="JetBrains Mono" font-weight="700" font-size="13" fill="${P.ink}">GND (0)</text>`;
      const pa = !a, pb = !b, na = !!a, nb = !!b;
      if (cur === "NOT") { s += `<path d="M260 32V68M260 112V145M260 175V208M260 252V310" fill="none" stroke="${P.ink}" stroke-width="2.4"/>` + tr(260, 90, "P", "A", pa, P) + tr(260, 230, "N", "A", na, P); }
      else if (cur === "NAND") {
        s += `<path d="M200 32V68M320 32V68M200 112V145H320V112M260 145V175M260 175V188M260 232V246M260 290V310" fill="none" stroke="${P.ink}" stroke-width="2.4"/>` + tr(200, 90, "P", "A", pa, P) + tr(320, 90, "P", "B", pb, P) + tr(260, 210, "N", "A", na, P) + tr(260, 268, "N", "B", nb, P);
      } else {
        s += `<path d="M260 32V52M260 96V112M260 156V175M260 175V200H200V214M260 200H320V214M200 258V310M320 258V310" fill="none" stroke="${P.ink}" stroke-width="2.4"/>` + tr(260, 74, "P", "A", pa, P) + tr(260, 134, "P", "B", pb, P) + tr(200, 236, "N", "A", na, P) + tr(320, 236, "N", "B", nb, P);
      }
      s += `<path d="M260 ${cur === "NOR" ? 175 : 160}H440" stroke="${W(out)}" stroke-width="4"/><circle cx="460" cy="${cur === "NOR" ? 175 : 160}" r="20" fill="${out ? P.on : "#fff"}" stroke="${out ? P.on : "#94A3B8"}" stroke-width="2.5"/><text x="460" y="${(cur === "NOR" ? 175 : 160) + 6}" text-anchor="middle" font-family="JetBrains Mono" font-weight="800" font-size="16" fill="${out ? "#fff" : P.ink}">${out ? 1 : 0}</text>
        <text x="460" y="${(cur === "NOR" ? 175 : 160) - 28}" text-anchor="middle" font-family="JetBrains Mono" font-weight="700" font-size="12" fill="${P.ink}">Y</text>
        <text x="40" y="160" font-family="JetBrains Mono" font-weight="800" font-size="15" fill="${a ? P.on : P.ink}">A = ${a}</text>${cur !== "NOT" ? `<text x="40" y="184" font-family="JetBrains Mono" font-weight="800" font-size="15" fill="${b ? P.on : P.ink}">B = ${b}</text>` : ""}`;
      sv.innerHTML = s;
      const pull = { NOT: "one PMOS on top, one NMOS below", NAND: "two PMOS in parallel on top, two NMOS in series below", NOR: "two PMOS in series on top, two NMOS in parallel below" }[cur];
      note.innerHTML = `<b>${cur}</b> uses ${pull}. Right now the ${out ? "top (pull-up) network connects Y to VDD, so Y = 1" : "bottom (pull-down) network connects Y to ground, so Y = 0"}. Exactly one network conducts at a time, so almost no current flows when the gate is not switching. That is why CMOS chips stay cool.`;
      el.querySelectorAll("[data-g]").forEach(x => x.classList.toggle("on", x.dataset.g === cur)); el.querySelector('[data-act="B"]').style.display = cur === "NOT" ? "none" : "";
    }
    el.addEventListener("click", e => { const g = e.target.closest("[data-g]"); if (g) { cur = g.dataset.g; draw(); return; } const a = e.target.closest("[data-act]"); if (!a) return; if (a.dataset.act === "A") A ^= 1; else Bv ^= 1; draw(); });
    draw();
  }

  /* ---- 5-stage pipeline ---- */
  function pipeline(el, p) {
    const ins = p.ins, ST = ["IF", "ID", "EX", "MEM", "WB"]; let mode = "none", cyc = 0;
    el.innerHTML = head(p, "Pipelining", "Five instructions move through five stages. Pick how the CPU handles the data hazard and step through the clock cycles.") +
      `<div class="mg-ctl xl-cfg"><span>Hazard handling</span>${B("ideal", "Ignore (wrong answers!)", "sm")}${B("none", "Stall", "sm")}${B("fwd", "Forwarding", "sm")}</div><div class="xl-pipe"></div><div class="xl-read xl-pr"></div>
      <div class="mg-ctl">${B("prev", "◂ Cycle")}${B("next", "Cycle ▸", "solid")}${B("all", "Show all")}</div>`;
    const box = el.querySelector(".xl-pipe"), rd = el.querySelector(".xl-pr");
    function sched() {
      const st = [];
      ins.forEach((it, i) => { const r = [];
        r[0] = i ? Math.max(st[i - 1][0] + 1, st[i - 1][1]) : 1; r[1] = r[0] + 1;
        if (i && mode !== "ideal" && it.dep) { const pr = st[i - 1], ld = ins[i - 1].load;
          if (mode === "none") r[1] = Math.max(r[1], pr[4]); else if (ld) r[1] = Math.max(r[1], pr[3]); }
        if (i) r[1] = Math.max(r[1], st[i - 1][1] + 1);
        for (let s = 2; s < 5; s++) r[s] = Math.max(r[s - 1] + 1, i ? st[i - 1][s] + 1 : 0);
        st.push(r); });
      return st;
    }
    function draw() {
      const st = sched(), total = st[st.length - 1][4], C = Math.max(total, 9); if (cyc > total) cyc = total;
      let h = `<table><tr><th>Instruction</th>${Array.from({ length: C }, (_, k) => `<th class="${k + 1 === cyc ? "now" : ""}">${k + 1}</th>`).join("")}</tr>`;
      ins.forEach((it, i) => { h += `<tr><td class="ins"><code>${esc(it.t)}</code></td>`;
        for (let k = 1; k <= C; k++) { const s = st[i].indexOf(k); let cell = "", cls = "";
          if (s >= 0) { cell = ST[s]; cls = "s" + s; } else if (k > st[i][0] && k < st[i][1]) { cell = "stall"; cls = "stall"; }
          const show = k <= cyc; h += `<td class="${show ? cls : ""} ${k === cyc ? "now" : ""}">${show ? cell : ""}</td>`; }
        h += "</tr>"; });
      box.innerHTML = h + "</table>";
      const stalls = total - (ins.length + 4);
      rd.innerHTML = `<span>Total cycles <b>${total}</b></span><span>Stall cycles <b>${stalls}</b></span><span>Without pipelining <b>${ins.length * 5}</b></span><span>Average CPI <b>${fm(total / ins.length, 2)}</b></span>
        <span class="xl-sum">${mode === "ideal" ? "With no hazard handling, an instruction reads a register before the previous one has written it, so it gets the old value. Fast but wrong." : mode === "none" ? "Stalling: the dependent instruction waits in decode until the earlier one writes its result back to the register file." : "Forwarding: the ALU result is sent straight to the next instruction's EX stage, so most stalls disappear. A load followed by a use still needs one stall, because the data arrives at the end of MEM."}</span>`;
      el.querySelectorAll("[data-act=ideal],[data-act=none],[data-act=fwd]").forEach(b => b.classList.toggle("on", b.dataset.act === mode));
    }
    el.addEventListener("click", e => { const a = e.target.closest("[data-act]"); if (!a) return; const k = a.dataset.act;
      if (k === "next") cyc++; else if (k === "prev") cyc = Math.max(0, cyc - 1); else if (k === "all") cyc = 99; else { mode = k; } draw(); });
    draw();
  }

  /* =========================================================
     MACHINE LEARNING
     ========================================================= */

  const DATA = {
    study: [[1, 2.1], [2, 3.9], [2.5, 3.2], [3, 5.1], [4, 5.4], [4.5, 6.8], [5, 6.1], [6, 7.9], [6.5, 7.2], [7, 8.8], [8, 8.9], [9, 9.6]]
  };

  /* ---- linear regression with gradient descent ---- */
  function regress(el, p) {
    let pts = (p.pts || DATA.study).map(x => x.slice()); const S = {}; let hist = [];
    el.innerHTML = head(p, "Fit a line", "Drag the sliders or click the plot to add points. Red segments are the errors (residuals).") +
      `<div class="mg-sl">${slider("w", "w (slope)", -2, 3, .01, p.w ?? .3)}${slider("b", "b (intercept)", -4, 8, .01, p.b ?? 1)}${slider("lr", "learning rate", .001, .05, .001, .01)}</div>`;
    const st = stage(el, 640, 380), m = plot(st, [0, 10], [0, 12]);
    el.insertAdjacentHTML("beforeend", `<div class="mg-ctl">${B("gd", "1 gradient step", "solid")}${B("gd20", "20 steps")}${p.noFit ? "" : B("fit", "Jump to best fit")}${B("clear", "Clear points")}${B("reset", "Reset data")}<div class="mg-read xl-rr"></div></div><div class="xl-loss"></div>`);
    const rr = el.querySelector(".xl-rr"), lh = el.querySelector(".xl-loss");
    const mse = (w, b) => pts.reduce((s, [x, y]) => s + (w * x + b - y) ** 2, 0) / Math.max(1, pts.length);
    function grad() { const n = Math.max(1, pts.length); let gw = 0, gb = 0; pts.forEach(([x, y]) => { const e = S.w * x + S.b - y; gw += 2 * e * x / n; gb += 2 * e / n; }); return [gw, gb]; }
    function best() { const n = pts.length; if (n < 2) return [S.w, S.b]; const mx = pts.reduce((s, q) => s + q[0], 0) / n, my = pts.reduce((s, q) => s + q[1], 0) / n; let sxy = 0, sxx = 0; pts.forEach(([x, y]) => { sxy += (x - mx) * (y - my); sxx += (x - mx) ** 2; }); const w = sxx ? sxy / sxx : 0; return [w, my - w * mx]; }
    function draw() {
      const c = st.c, P = PAL(); c.clearRect(0, 0, st.W, st.H); m.axes({ xl: "x (hours studied)", yl: "y (score)" });
      c.save(); c.beginPath(); c.rect(m.pad.l, m.pad.t, m.pw, m.ph); c.clip();
      pts.forEach(([x, y]) => { c.strokeStyle = "rgba(220,38,38,.75)"; c.lineWidth = 2; c.beginPath(); c.moveTo(m.X(x), m.Y(y)); c.lineTo(m.X(x), m.Y(S.w * x + S.b)); c.stroke(); });
      c.strokeStyle = P.a; c.lineWidth = 3.5; c.beginPath(); c.moveTo(m.X(0), m.Y(S.b)); c.lineTo(m.X(10), m.Y(S.w * 10 + S.b)); c.stroke();
      pts.forEach(([x, y]) => dot(c, m.X(x), m.Y(y), 6, "#fff", P.ink, 2.4)); c.restore();
      const [gw, gb] = grad();
      emit(el, { mse: mse(S.w, S.b), w: S.w, b: S.b, steps: Math.max(0, hist.length - 1), n: pts.length });
      rr.innerHTML = `<span>MSE <b>${fm(mse(S.w, S.b), 3)}</b></span><span>∂L/∂w <b>${fm(gw, 3)}</b></span><span>∂L/∂b <b>${fm(gb, 3)}</b></span>`;
      if (hist.length > 1) { const mx = Math.max(...hist), W = 300, H = 50; lh.innerHTML = `<small>Loss after each step</small><svg viewBox="0 0 ${W} ${H}" preserveAspectRatio="none"><polyline fill="none" stroke="${P.b}" stroke-width="2" points="${hist.map((v, i) => `${i / (hist.length - 1) * W},${H - 4 - (v / mx) * (H - 8)}`).join(" ")}"/></svg><small>${hist.length - 1} steps · now ${fm(hist[hist.length - 1], 3)}</small>`; } else lh.innerHTML = "";
    }
    function stepGD(k) { for (let i = 0; i < k; i++) { if (!hist.length) hist.push(mse(S.w, S.b)); const [gw, gb] = grad(); setSl(el, "w", Math.max(-2, Math.min(3, S.w - S.lr * gw))); setSl(el, "b", Math.max(-4, Math.min(8, S.b - S.lr * gb))); hist.push(mse(S.w, S.b)); if (hist.length > 200) hist.shift(); } draw(); }
    bindSliders(el, S, k => { if (k !== "lr") hist = []; draw(); }, { lr: v => v.toFixed(3) });
    st.cv.addEventListener("click", e => { const [px, py] = st.pos(e), x = m.ix(px), y = m.iy(py); if (x < 0 || x > 10 || y < 0 || y > 12) return; pts.push([x, y]); hist = []; draw(); });
    el.addEventListener("click", e => { const a = e.target.closest("[data-act]"); if (!a) return; const k = a.dataset.act;
      if (k === "gd") stepGD(1); if (k === "gd20") stepGD(20);
      if (k === "fit") { const [w, b] = best(), w0 = S.w, b0 = S.b, t0 = performance.now(); hist = []; const go = now => { const f = still() ? 1 : Math.min(1, (now - t0) / 600), e2 = 1 - (1 - f) ** 3; setSl(el, "w", w0 + (w - w0) * e2); setSl(el, "b", b0 + (b - b0) * e2); draw(); if (f < 1) requestAnimationFrame(go); }; requestAnimationFrame(go); }
      if (k === "clear") { pts = []; hist = []; draw(); } if (k === "reset") { pts = (p.pts || DATA.study).map(x => x.slice()); hist = []; draw(); } });
    draw();
  }

  /* ---- gradient descent on a 1-D loss ---- */
  const LOSS = {
    bowl: { f: w => (w - 3) ** 2 / 2 + 1, r: [-2, 8], y: [0, 14], s: 0 },
    bumpy: { f: w => .12 * (w - 3) ** 2 + Math.sin(2.2 * w) * .9 + 2, r: [-3, 9], y: [0, 9], s: -2 },
    steep: { f: w => 2.5 * (w - 3) ** 2 + 1, r: [-1, 7], y: [0, 40], s: 0 }
  };
  function gd(el, p) {
    const keys = p.curves || ["bowl", "bumpy", "steep"]; let L = LOSS[keys[0]], path = [], timer = null; const S = {};
    el.innerHTML = head(p, "Gradient descent", "The ball rolls downhill: each step moves w by −(learning rate × slope).") +
      `<div class="xl-tabs">${keys.map(k => `<button type="button" class="mg-b sm" data-c="${k}">${{ bowl: "Smooth bowl", bumpy: "Bumpy (local minima)", steep: "Steep valley" }[k]}</button>`).join("")}</div>
      <div class="mg-sl">${slider("lr", "learning rate α", .01, 1.2, .01, p.lr ?? .2)}${slider("w0", "start w", -2, 8, .1, L.s)}</div>`;
    const st = stage(el, 640, 340);
    el.insertAdjacentHTML("beforeend", `<div class="mg-ctl">${B("step", "1 step", "solid")}${B("run", "Run 25 steps")}${B("reset", "Reset")}<div class="mg-read xl-gr"></div></div><p class="xl-note"></p>`);
    const gr = el.querySelector(".xl-gr"), note = el.querySelector(".xl-note");
    const d = w => (L.f(w + 1e-4) - L.f(w - 1e-4)) / 2e-4;
    function draw() {
      const c = st.c, P = PAL(), m = plot(st, L.r, L.y); c.clearRect(0, 0, st.W, st.H); m.axes({ xl: "w (parameter)", yl: "loss L(w)" });
      c.save(); c.beginPath(); c.rect(m.pad.l, m.pad.t, m.pw, m.ph); c.clip();
      c.strokeStyle = P.ink; c.lineWidth = 3; c.beginPath(); for (let i = 0; i <= 300; i++) { const w = L.r[0] + (L.r[1] - L.r[0]) * i / 300; i ? c.lineTo(m.X(w), m.Y(L.f(w))) : c.moveTo(m.X(w), m.Y(L.f(w))); } c.stroke();
      c.strokeStyle = P.b; c.lineWidth = 2; c.setLineDash([5, 4]); c.beginPath(); path.forEach((w, i) => { const x = m.X(w), y = m.Y(L.f(w)); i ? c.lineTo(x, y) : c.moveTo(x, y); }); c.stroke(); c.setLineDash([]);
      path.forEach((w, i) => dot(c, m.X(w), m.Y(L.f(w)), i === path.length - 1 ? 9 : 4.5, i === path.length - 1 ? P.b : "rgba(234,88,12,.5)", i === path.length - 1 ? "#fff" : null, 2.5));
      const w = path[path.length - 1], sl = d(w); c.strokeStyle = P.a; c.lineWidth = 2; c.beginPath(); c.moveTo(m.X(w - 1), m.Y(L.f(w) - sl)); c.lineTo(m.X(w + 1), m.Y(L.f(w) + sl)); c.stroke(); c.restore();
      gr.innerHTML = `<span>step <b>${path.length - 1}</b></span><span>w <b>${fm(w, 3)}</b></span><span>L(w) <b>${fm(L.f(w), 3)}</b></span><span>slope <b>${fm(sl, 3)}</b></span>`;
      const div = !isFinite(w) || Math.abs(w) > 1e3 || (path.length > 3 && L.f(w) > L.f(path[0]) * 1.5);
      note.textContent = div ? "Diverging! The learning rate is so big that each step overshoots the bottom by more than it started. Turn α down." :
        path.length > 1 && Math.abs(sl) < .02 ? (keys[0] === "bumpy" || L === LOSS.bumpy) && L.f(w) > 1.6 ? "Stuck in a local minimum: the slope is 0 but this isn't the lowest valley. Try a different start." : "Converged: the slope is almost 0, so the steps become tiny." :
          `Next step: w − α·slope = ${fm(w, 3)} − ${fm(S.lr, 2)} × ${fm(sl, 3)} = ${fm(w - S.lr * sl, 3)}`;
      el.querySelectorAll("[data-c]").forEach(b => b.classList.toggle("on", LOSS[b.dataset.c] === L));
      emit(el, { w, loss: L.f(w), slope: sl, steps: path.length - 1, diverged: div, lr: S.lr, curve: Object.keys(LOSS).find(k => LOSS[k] === L), start: path[0] });
    }
    function step() { const w = path[path.length - 1]; if (!isFinite(w) || Math.abs(w) > 1e3) return; path.push(w - S.lr * d(w)); draw(); }
    function stop() { if (timer) { clearInterval(timer); timer = null; } }
    bindSliders(el, S, k => { if (k === "w0") { stop(); path = [S.w0]; } draw(); });
    path = [S.w0];
    el.addEventListener("click", e => { const c = e.target.closest("[data-c]"); if (c) { stop(); L = LOSS[c.dataset.c]; setSl(el, "w0", L.s); path = [S.w0]; draw(); return; }
      const a = e.target.closest("[data-act]"); if (!a) return; const k = a.dataset.act;
      if (k === "step") step(); if (k === "reset") { stop(); path = [S.w0]; draw(); }
      if (k === "run") { stop(); let n = 0; timer = setInterval(() => { step(); if (++n >= 25) stop(); }, still() ? 10 : 120); } });
    draw();
  }

  /* ---- datasets for classification ---- */
  function makeData(kind, seed, n = 80) {
    const r = rng(seed), out = [];
    for (let i = 0; i < n; i++) {
      const y = i % 2; let a, b;
      if (kind === "blobs") { a = (y ? .68 : .32) + gauss(r) * .11; b = (y ? .62 : .36) + gauss(r) * .11; }
      else if (kind === "xor") { const qx = r() < .5, qy = r() < .5; a = (qx ? .72 : .28) + gauss(r) * .09; b = (qy ? .72 : .28) + gauss(r) * .09; out.push([a, b, qx !== qy ? 1 : 0]); continue; }
      else if (kind === "circle") { const ang = r() * 6.283, rad = y ? .08 + r() * .16 : .3 + r() * .14; a = .5 + rad * Math.cos(ang); b = .5 + rad * Math.sin(ang); }
      else { const t = r() * Math.PI; if (y) { a = .3 + .3 * Math.cos(t); b = .42 + .3 * Math.sin(t); } else { a = .6 - .3 * Math.cos(t); b = .58 - .3 * Math.sin(t); } a += gauss(r) * .04; b += gauss(r) * .04; }
      out.push([a, b, y]);
    }
    return out.map(([a, b, y]) => [Math.min(.98, Math.max(.02, a)), Math.min(.98, Math.max(.02, b)), y]);
  }
  const CA = "#2563EB", CB = "#EA580C";
  function shade(pr) { const t = Math.min(1, Math.abs(pr - .5) * 2), a = .1 + .32 * t, c = pr > .5 ? [234, 88, 12] : [37, 99, 235]; return `rgb(${Math.round(255 - (255 - c[0]) * a)},${Math.round(255 - (255 - c[1]) * a)},${Math.round(255 - (255 - c[2]) * a)})`; }

  /* ---- classifier: kNN and logistic regression ---- */
  function classify(el, p) {
    const sets = p.sets || ["blobs", "moons", "circle", "xor"]; let set = sets[0], data = makeData(set, 7), method = p.method || "knn", cls = 0, wts = null, feats = "lin", timer = null, epochs = 0; const S = {};
    const NM = { blobs: "Two blobs", moons: "Moons", circle: "Circle", xor: "XOR" };
    el.innerHTML = head(p, "Classifier playground", "Shaded regions show what the model would predict at every point. Click to add a point of the selected class.") +
      `<div class="xl-tabs">${sets.map(s => `<button type="button" class="mg-b sm" data-s="${s}">${NM[s]}</button>`).join("")}<span class="xl-sp"></span>${(p.methods || ["knn", "logreg"]).map(m => `<button type="button" class="mg-b sm" data-m="${m}">${m === "knn" ? "k-nearest neighbors" : "Logistic regression"}</button>`).join("")}</div>
      <div class="mg-sl xl-knn">${slider("k", "k", 1, 31, 2, p.k || 5)}</div><div class="mg-ctl xl-lr">${B("train", "Train 200 steps", "solid")}${B("feat", "Features: x₁, x₂")}${B("rw", "Reset weights")}</div>`;
    const st = stage(el, 420, 420);
    el.insertAdjacentHTML("beforeend", `<div class="mg-ctl"><span class="xl-in">Add points as</span><button type="button" class="mg-b sm xl-ca" data-c="0"><i class="dotc" style="background:${CA}"></i>class A</button><button type="button" class="mg-b sm xl-cb" data-c="1"><i class="dotc" style="background:${CB}"></i>class B</button>${B("clear", "Clear points")}<div class="mg-read xl-cr"></div></div><p class="xl-note"></p>`);
    const cr = el.querySelector(".xl-cr"), note = el.querySelector(".xl-note");
    const phi = (a, b) => feats === "lin" ? [1, a - .5, b - .5] : [1, a - .5, b - .5, (a - .5) ** 2, (b - .5) ** 2, (a - .5) * (b - .5)];
    const sig = z => 1 / (1 + Math.exp(-z));
    function predict(a, b) {
      if (method === "knn") { if (!data.length) return .5; const ds = data.map(q => [(q[0] - a) ** 2 + (q[1] - b) ** 2, q[2]]).sort((u, v) => u[0] - v[0]).slice(0, S.k); return ds.reduce((s, q) => s + q[1], 0) / ds.length; }
      const f = phi(a, b); if (!wts || wts.length !== f.length) wts = new Array(f.length).fill(0); return sig(f.reduce((s, x, i) => s + x * wts[i] * 1, 0));
    }
    function train(steps) { const lr = 2.5; for (let t = 0; t < steps; t++) { const f0 = phi(.5, .5); if (!wts || wts.length !== f0.length) wts = new Array(f0.length).fill(0); const g = new Array(wts.length).fill(0);
      data.forEach(([a, b, y]) => { const f = phi(a, b), e = sig(f.reduce((s, x, i) => s + x * wts[i], 0)) - y; f.forEach((x, i) => g[i] += e * x / data.length); }); wts = wts.map((w, i) => w - lr * g[i] * 4); epochs++; } }
    function draw() {
      const c = st.c, P = PAL(), N = 60, cw = st.W / N; c.clearRect(0, 0, st.W, st.H);
      for (let i = 0; i < N; i++) for (let j = 0; j < N; j++) { const pr = predict((i + .5) / N, 1 - (j + .5) / N);
        c.fillStyle = shade(pr); c.fillRect(Math.floor(i * cw), Math.floor(j * cw), Math.ceil(cw) + 1, Math.ceil(cw) + 1); }
      let right = 0; data.forEach(([a, b, y]) => { const pr = predict(a, b) > .5 ? 1 : 0; if (pr === y) right++; dot(c, a * st.W, (1 - b) * st.H, 5.5, y ? CB : CA, pr === y ? "#fff" : "#111", pr === y ? 1.5 : 2.5); });
      c.strokeStyle = P.ink; c.lineWidth = 1.5; c.strokeRect(.75, .75, st.W - 1.5, st.H - 1.5);
      emit(el, { acc: data.length ? right / data.length : 0, method, k: S.k, set, feats, steps: epochs, n: data.length });
      cr.innerHTML = `<span>Training accuracy <b>${data.length ? Math.round(right / data.length * 100) : 0}%</b></span>${method === "logreg" ? `<span>steps <b>${epochs}</b></span>` : ""}`;
      el.querySelector(".xl-knn").style.display = method === "knn" ? "" : "none"; el.querySelector(".xl-lr").style.display = method === "logreg" ? "" : "none";
      el.querySelector('[data-act="feat"]').textContent = feats === "lin" ? "Features: x₁, x₂ (linear)" : "Features: + x₁², x₂², x₁x₂";
      note.innerHTML = method === "knn" ? `k-NN looks at the <b>${S.k}</b> closest training points and takes a vote. Small k follows every point (overfits, jagged edges); large k smooths everything out (underfits). Points with black outlines are misclassified.` :
        feats === "lin" ? "Logistic regression draws a single straight boundary where σ(w·x) = 0.5. It can't separate circles or XOR with only x₁ and x₂ — try adding squared features." : "With squared and product features the boundary can curve into circles and ellipses, while the model is still linear in its weights.";
      el.querySelectorAll("[data-s]").forEach(b => b.classList.toggle("on", b.dataset.s === set)); el.querySelectorAll("[data-m]").forEach(b => b.classList.toggle("on", b.dataset.m === method)); el.querySelectorAll("[data-c]").forEach(b => b.classList.toggle("on", +b.dataset.c === cls));
    }
    bindSliders(el, S, draw, { k: v => String(v) });
    st.cv.addEventListener("click", e => { const [px, py] = st.pos(e); data.push([px / st.W, 1 - py / st.H, cls]); draw(); });
    el.addEventListener("click", e => { const t = e.target.closest("[data-s],[data-m],[data-c],[data-act]"); if (!t || t.tagName === "CANVAS") return;
      if (t.dataset.s) { set = t.dataset.s; data = makeData(set, 7); wts = null; epochs = 0; }
      else if (t.dataset.m) method = t.dataset.m; else if (t.dataset.c) cls = +t.dataset.c;
      else { const k = t.dataset.act;
        if (k === "train") { clearInterval(timer); let n = 0; timer = setInterval(() => { train(10); draw(); if ((n += 10) >= 200) clearInterval(timer); }, still() ? 0 : 30); return; }
        if (k === "feat") { feats = feats === "lin" ? "quad" : "lin"; wts = null; epochs = 0; } if (k === "rw") { wts = null; epochs = 0; } if (k === "clear") { data = []; wts = null; epochs = 0; } }
      draw(); });
    draw();
  }

  /* ---- k-means ---- */
  function kmeans(el, p) {
    const S = {}; let pts = [], cents = [], asg = [], phase = "place", it = 0, seed = 3, timer = null, trueK = 4, ref = 1;
    function gen() { const r = rng(seed++ * 7919), K = 3 + Math.floor(r() * 2), base = [[.27, .28], [.73, .3], [.3, .74], [.72, .72]].sort(() => r() - .5).slice(0, K), ctr = base.map(([x, y]) => [x + (r() - .5) * .14, y + (r() - .5) * .14]); pts = Array.from({ length: 150 }, (_, i) => { const q = ctr[i % K]; return [Math.min(.98, Math.max(.02, q[0] + gauss(r) * .07)), Math.min(.98, Math.max(.02, q[1] + gauss(r) * .07))]; }); asg = pts.map(() => -1); cents = []; it = 0; phase = "place"; trueK = K; ref = Infinity;
      const rr = rng(77); for (let t = 0; t < 12; t++) { let C = Array.from({ length: K }, () => pts[Math.floor(rr() * pts.length)].slice()), A = []; for (let s2 = 0; s2 < 30; s2++) { A = pts.map(q => { let bi = 0; C.forEach((c2, j) => { if (d2(q, c2) < d2(q, C[bi])) bi = j; }); return bi; }); C = C.map((c2, j) => { const mine = pts.filter((_, i) => A[i] === j); return mine.length ? [mine.reduce((a, q) => a + q[0], 0) / mine.length, mine.reduce((a, q) => a + q[1], 0) / mine.length] : c2; }); } ref = Math.min(ref, pts.reduce((a, q, i) => a + d2(q, C[A[i]]), 0)); } }
    el.innerHTML = head(p, "k-means clustering", "No labels here: the algorithm groups points by itself. Alternate the two steps until nothing moves.") + `<div class="mg-sl">${slider("k", "k (clusters)", 2, 7, 1, p.k || 4)}</div>`;
    const st = stage(el, 420, 420);
    el.insertAdjacentHTML("beforeend", `<div class="mg-ctl">${B("place", "1. Drop k random centers")}${B("assign", "2. Assign each point")}${B("move", "3. Move centers to the mean")}${B("run", "Run to the end", "solid")}${B("new", "New data")}<div class="mg-read xl-kr"></div></div><p class="xl-note"></p>`);
    const kr = el.querySelector(".xl-kr"), note = el.querySelector(".xl-note");
    const d2 = (a, b) => (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2;
    function inertia() { return asg[0] < 0 ? NaN : pts.reduce((s, q, i) => s + d2(q, cents[asg[i]]), 0); }
    function place() { const r = rng(Date.now() & 0xffff); cents = Array.from({ length: S.k }, () => pts[Math.floor(r() * pts.length)].slice()); asg = pts.map(() => -1); it = 0; phase = "assign"; }
    function assign() { if (!cents.length) place(); let ch = 0; el._conv = false; pts.forEach((q, i) => { let bi = 0; cents.forEach((c, j) => { if (d2(q, c) < d2(q, cents[bi])) bi = j; }); if (asg[i] !== bi) ch++; asg[i] = bi; }); phase = "move"; if (!ch && it > 0) el._conv = true; return ch; }
    function move() { if (asg[0] < 0) assign(); let mv = 0; cents = cents.map((c, j) => { const mine = pts.filter((_, i) => asg[i] === j); if (!mine.length) return c; const n = [mine.reduce((s, q) => s + q[0], 0) / mine.length, mine.reduce((s, q) => s + q[1], 0) / mine.length]; mv += Math.sqrt(d2(n, c)); return n; }); it++; phase = "assign"; return mv; }
    function draw() {
      const c = st.c, P = PAL(); c.clearRect(0, 0, st.W, st.H); c.fillStyle = "#fff"; c.fillRect(0, 0, st.W, st.H);
      if (asg[0] >= 0) pts.forEach((q, i) => { const cc = cents[asg[i]]; c.strokeStyle = CL[asg[i] % CL.length] + "33"; c.lineWidth = 1; c.beginPath(); c.moveTo(q[0] * st.W, (1 - q[1]) * st.H); c.lineTo(cc[0] * st.W, (1 - cc[1]) * st.H); c.stroke(); });
      pts.forEach((q, i) => dot(c, q[0] * st.W, (1 - q[1]) * st.H, 4.5, asg[i] < 0 ? "#94A3B8" : CL[asg[i] % CL.length], "#fff", 1));
      cents.forEach((q, j) => { const x = q[0] * st.W, y = (1 - q[1]) * st.H; c.save(); c.translate(x, y); c.rotate(Math.PI / 4); c.fillStyle = CL[j % CL.length]; c.strokeStyle = "#111"; c.lineWidth = 2.5; c.fillRect(-9, -9, 18, 18); c.strokeRect(-9, -9, 18, 18); c.restore(); });
      c.strokeStyle = P.ink; c.lineWidth = 1.5; c.strokeRect(.75, .75, st.W - 1.5, st.H - 1.5);
      const I = inertia(); emit(el, { it, inertia: I, k: S.k, converged: el._conv || false, phase, trueK, ref });
      kr.innerHTML = `<span>iterations <b>${it}</b></span><span>inertia (sum of squared distances) <b>${isNaN(I) ? "–" : fm(I, 3)}</b></span>`;
      note.textContent = !cents.length ? "Start by dropping k random centers (diamonds)." : phase === "move" ? "Each point now belongs to its closest center. Next: move every center to the average of its points." : "Centers moved. Re-assign the points: some may switch clusters. When no point switches, k-means has converged.";
    }
    bindSliders(el, S, () => { cents = []; asg = pts.map(() => -1); it = 0; phase = "place"; draw(); }, { k: v => String(v) });
    el.addEventListener("click", e => { const a = e.target.closest("[data-act]"); if (!a) return; const k = a.dataset.act; clearInterval(timer);
      if (k === "new") gen(); if (k === "place") place(); if (k === "assign") assign(); if (k === "move") move();
      if (k === "run") { if (!cents.length) place(); timer = setInterval(() => { const ch = assign(); draw(); setTimeout(() => { move(); draw(); }, still() ? 0 : 200); if (!ch && it > 0) clearInterval(timer); }, still() ? 20 : 450); }
      draw(); });
    gen(); draw();
  }

  /* ---- neural network playground ---- */
  function nnet(el, p) {
    const sets = p.sets || ["xor", "circle", "moons", "blobs"]; let set = p.set || sets[0], data = makeData(set, 11, 120), S = {}, act = p.act || "tanh", net, epoch = 0, timer = null, loss = NaN;
    const NM = { blobs: "Two blobs", moons: "Moons", circle: "Circle", xor: "XOR" };
    const A = { tanh: [Math.tanh, y => 1 - y * y], relu: [x => Math.max(0, x), y => y > 0 ? 1 : 0], sigmoid: [x => 1 / (1 + Math.exp(-x)), y => y * (1 - y)] };
    el.innerHTML = head(p, "Neural network playground", "Train a tiny network and watch the hidden neurons carve up the plane. Line color: blue = positive weight, orange = negative; thickness = size.") +
      `<div class="xl-tabs">${sets.map(s => `<button type="button" class="mg-b sm" data-s="${s}">${NM[s]}</button>`).join("")}<span class="xl-sp"></span>${Object.keys(A).map(a => `<button type="button" class="mg-b sm" data-a="${a}">${a}</button>`).join("")}</div>
      <div class="mg-sl">${slider("h", "hidden neurons", 1, 8, 1, p.h || 4)}${slider("lr", "learning rate", .05, 2, .05, .6)}</div><div class="xl-nn"><svg class="xl-svg xl-net" viewBox="0 0 360 300"></svg><div class="xl-nnc"></div></div>
      <div class="mg-ctl">${B("train", "Train ▸", "solid")}${B("step", "1 epoch")}${B("reset", "New random weights")}<div class="mg-read xl-nr"></div></div><p class="xl-note"></p>`;
    const sv = el.querySelector(".xl-net"), host = el.querySelector(".xl-nnc"), st = stage(host, 300, 300), nr = el.querySelector(".xl-nr"), note = el.querySelector(".xl-note");
    function init() { const r = rng(Math.floor(Math.random() * 1e6)), H = S.h, s = 1.2; net = { W1: Array.from({ length: H }, () => [gauss(r) * s, gauss(r) * s]), b1: Array.from({ length: H }, () => gauss(r) * .3), W2: Array.from({ length: H }, () => gauss(r) * s), b2: 0 }; epoch = 0; loss = NaN; }
    function fwd(x1, x2) { const f = A[act][0]; const h = net.W1.map((w, j) => f(w[0] * x1 + w[1] * x2 + net.b1[j])); const z = h.reduce((s, v, j) => s + v * net.W2[j], net.b2); return { h, o: 1 / (1 + Math.exp(-z)) }; }
    function train(n) { const df = A[act][1], H = net.W1.length;
      for (let e = 0; e < n; e++) { const gW1 = net.W1.map(() => [0, 0]), gb1 = new Array(H).fill(0), gW2 = new Array(H).fill(0); let gb2 = 0, L = 0;
        data.forEach(([a, b, y]) => { const x1 = a * 2 - 1, x2 = b * 2 - 1, { h, o } = fwd(x1, x2), d = o - y; L += -(y * Math.log(o + 1e-9) + (1 - y) * Math.log(1 - o + 1e-9));
          for (let j = 0; j < H; j++) { gW2[j] += d * h[j]; const dh = d * net.W2[j] * df(h[j]); gW1[j][0] += dh * x1; gW1[j][1] += dh * x2; gb1[j] += dh; } gb2 += d; });
        const k = S.lr / data.length; for (let j = 0; j < H; j++) { net.W2[j] -= k * gW2[j]; net.W1[j][0] -= k * gW1[j][0]; net.W1[j][1] -= k * gW1[j][1]; net.b1[j] -= k * gb1[j]; } net.b2 -= k * gb2; loss = L / data.length; epoch++; } }
    function draw() {
      const P = PAL(), c = st.c, N = 50, cw = st.W / N; c.clearRect(0, 0, st.W, st.H);
      for (let i = 0; i < N; i++) for (let j = 0; j < N; j++) { const o = fwd(((i + .5) / N) * 2 - 1, (1 - (j + .5) / N) * 2 - 1).o; c.fillStyle = shade(o); c.fillRect(Math.floor(i * cw), Math.floor(j * cw), Math.ceil(cw) + 1, Math.ceil(cw) + 1); }
      let right = 0; data.forEach(([a, b, y]) => { const ok = (fwd(a * 2 - 1, b * 2 - 1).o > .5 ? 1 : 0) === y; right += ok; dot(c, a * st.W, (1 - b) * st.H, 4.2, y ? CB : CA, ok ? "#fff" : "#111", ok ? 1.2 : 2.2); });
      c.strokeStyle = P.ink; c.lineWidth = 1.5; c.strokeRect(.75, .75, st.W - 1.5, st.H - 1.5);
      const H = net.W1.length, hy = j => 150 + (j - (H - 1) / 2) * Math.min(36, 260 / H), ix = 40, hx = 180, ox = 320, iy = [110, 190];
      const ln = (x1, y1, x2, y2, w) => `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${w >= 0 ? CA : CB}" stroke-opacity="${Math.min(.95, .2 + Math.abs(w) / 3)}" stroke-width="${Math.min(7, .6 + Math.abs(w) * 1.3)}"/>`;
      let s = ""; for (let j = 0; j < H; j++) { s += ln(ix, iy[0], hx, hy(j), net.W1[j][0]) + ln(ix, iy[1], hx, hy(j), net.W1[j][1]) + ln(hx, hy(j), ox, 150, net.W2[j]); }
      s += `<circle cx="${ix}" cy="${iy[0]}" r="17" fill="#fff" stroke="${P.ink}" stroke-width="2"/><text x="${ix}" y="${iy[0] + 5}" text-anchor="middle" font-family="JetBrains Mono" font-weight="700" font-size="13">x₁</text><circle cx="${ix}" cy="${iy[1]}" r="17" fill="#fff" stroke="${P.ink}" stroke-width="2"/><text x="${ix}" y="${iy[1] + 5}" text-anchor="middle" font-family="JetBrains Mono" font-weight="700" font-size="13">x₂</text>`;
      for (let j = 0; j < H; j++) s += `<circle cx="${hx}" cy="${hy(j)}" r="13" fill="#fff" stroke="${P.ink}" stroke-width="2"/><text x="${hx}" y="${hy(j) + 4}" text-anchor="middle" font-family="JetBrains Mono" font-size="10">h${j + 1}</text>`;
      s += `<circle cx="${ox}" cy="150" r="19" fill="#fff" stroke="${P.ink}" stroke-width="2"/><text x="${ox}" y="155" text-anchor="middle" font-family="JetBrains Mono" font-weight="700" font-size="12">ŷ</text>
        <text x="${ix}" y="280" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="${P.muted}">input</text><text x="${hx}" y="290" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="${P.muted}">hidden (${act})</text><text x="${ox}" y="280" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="${P.muted}">sigmoid</text>`;
      sv.innerHTML = s;
      emit(el, { acc: right / data.length, epoch, loss, set, h: S.h, act });
      nr.innerHTML = `<span>epoch <b>${epoch}</b></span><span>loss <b>${isNaN(loss) ? "–" : fm(loss, 3)}</b></span><span>accuracy <b>${Math.round(right / data.length * 100)}%</b></span>`;
      note.textContent = S.h === 1 ? "With one hidden neuron the network can only draw one straight-ish boundary, just like logistic regression." : set === "xor" && S.h < 3 ? "XOR needs at least 2 hidden neurons — and 3 or 4 train far more reliably." : "Each hidden neuron makes one soft straight cut through the plane; the output neuron combines the cuts into a curved boundary.";
      el.querySelectorAll("[data-s]").forEach(b => b.classList.toggle("on", b.dataset.s === set)); el.querySelectorAll("[data-a]").forEach(b => b.classList.toggle("on", b.dataset.a === act));
    }
    function stop() { if (timer) { clearInterval(timer); timer = null; const b = el.querySelector('[data-act="train"]'); b.classList.remove("on"); b.textContent = "Train ▸"; } }
    bindSliders(el, S, k => { if (k === "h") { stop(); init(); } draw(); }, { h: v => String(v), lr: v => v.toFixed(2) });
    el.addEventListener("click", e => { const t = e.target.closest("[data-s],[data-a],[data-act]"); if (!t) return;
      if (t.dataset.s) { stop(); set = t.dataset.s; data = makeData(set, 11, 120); init(); }
      else if (t.dataset.a) { stop(); act = t.dataset.a; init(); }
      else { const k = t.dataset.act; if (k === "reset") { stop(); init(); } if (k === "step") train(1);
        if (k === "train") { if (timer) { stop(); return; } t.classList.add("on"); t.textContent = "Pause ❚❚"; timer = setInterval(() => { train(still() ? 40 : 8); draw(); if (epoch > 3000) stop(); }, 40); return; } }
      draw(); });
    init(); draw();
  }

  /* ---- decision threshold, confusion matrix and ROC ---- */
  function threshold(el, p) {
    const S = {}; const r = rng(5); const base = Array.from({ length: 200 }, (_, i) => [gauss(r), i % 2]);
    el.innerHTML = head(p, "Thresholds, confusion matrix and ROC", "A model outputs a score from 0 to 1. Everything above the threshold is called positive. Move it and watch the trade-off.") +
      `<div class="mg-sl">${slider("t", "threshold", .02, .98, .01, .5)}${slider("sep", "how well the model separates", 0, 3, .05, 1.4)}</div><div class="xl-thr"><div class="xl-th1"></div><div class="xl-th2"></div></div><div class="xl-cm"></div>`;
    const h1 = el.querySelector(".xl-th1"), h2 = el.querySelector(".xl-th2"), s1 = stage(h1, 420, 230), s2 = stage(h2, 230, 230), cm = el.querySelector(".xl-cm");
    const scores = () => base.map(([z, y]) => [1 / (1 + Math.exp(-(z * 1.1 + (y ? S.sep : -S.sep) * .9))), y]);
    function counts(sc, t) { let tp = 0, fp = 0, tn = 0, fn = 0; sc.forEach(([s, y]) => { if (s >= t) y ? tp++ : fp++; else y ? fn++ : tn++; }); return { tp, fp, tn, fn }; }
    function draw() {
      const P = PAL(), sc = scores(), c = s1.c, m = plot(s1, [0, 1], [0, 26], { l: 34, b: 26 }); c.clearRect(0, 0, s1.W, s1.H); m.axes({ xl: "model score", sy: 5 });
      const bins = 20, hp = new Array(bins).fill(0), hn = new Array(bins).fill(0); sc.forEach(([s, y]) => (y ? hp : hn)[Math.min(bins - 1, Math.floor(s * bins))]++);
      for (let i = 0; i < bins; i++) { const x0 = m.X(i / bins), x1 = m.X((i + 1) / bins), w = (x1 - x0) / 2 - 1;
        c.fillStyle = "rgba(37,99,235,.75)"; c.fillRect(x0 + 1, m.Y(hn[i]), w, m.Y(0) - m.Y(hn[i])); c.fillStyle = "rgba(234,88,12,.8)"; c.fillRect(x0 + w + 2, m.Y(hp[i]), w, m.Y(0) - m.Y(hp[i])); }
      c.strokeStyle = P.ink; c.lineWidth = 2.5; c.setLineDash([6, 4]); c.beginPath(); c.moveTo(m.X(S.t), m.pad.t); c.lineTo(m.X(S.t), m.pad.t + m.ph); c.stroke(); c.setLineDash([]);
      c.font = "600 11px \"Plus Jakarta Sans\", sans-serif"; c.fillStyle = CA; c.fillText("■ actually negative", m.pad.l + 8, m.pad.t + 30); c.fillStyle = CB; c.fillText("■ actually positive", m.pad.l + 8, m.pad.t + 46);
      const q = counts(sc, S.t), prec = q.tp / Math.max(1, q.tp + q.fp), rec = q.tp / Math.max(1, q.tp + q.fn), fpr = q.fp / Math.max(1, q.fp + q.tn), acc = (q.tp + q.tn) / sc.length, f1 = prec + rec ? 2 * prec * rec / (prec + rec) : 0;
      const c2 = s2.c, m2 = plot(s2, [0, 1], [0, 1], { l: 40, b: 26, r: 10 }); c2.clearRect(0, 0, s2.W, s2.H); m2.axes({ xl: "FPR", yl: "TPR", sx: .25, sy: .25 });
      const roc = []; for (let t = 1.001; t >= -0.001; t -= .01) { const k = counts(sc, t); roc.push([k.fp / Math.max(1, k.fp + k.tn), k.tp / Math.max(1, k.tp + k.fn)]); }
      let auc = 0; for (let i = 1; i < roc.length; i++) auc += (roc[i][0] - roc[i - 1][0]) * (roc[i][1] + roc[i - 1][1]) / 2;
      c2.strokeStyle = "rgba(100,116,139,.5)"; c2.setLineDash([4, 4]); c2.beginPath(); c2.moveTo(m2.X(0), m2.Y(0)); c2.lineTo(m2.X(1), m2.Y(1)); c2.stroke(); c2.setLineDash([]);
      c2.strokeStyle = P.a; c2.lineWidth = 3; c2.beginPath(); roc.forEach(([x, y], i) => i ? c2.lineTo(m2.X(x), m2.Y(y)) : c2.moveTo(m2.X(x), m2.Y(y))); c2.stroke();
      dot(c2, m2.X(fpr), m2.Y(rec), 7, P.b, "#fff", 2.5); c2.font = "700 11px \"JetBrains Mono\", monospace"; c2.fillStyle = P.ink; c2.fillText("AUC " + auc.toFixed(2), m2.X(.45), m2.Y(.12));
      emit(el, { prec, rec, f1, acc, fpr, t: S.t, sep: S.sep, auc });
      cm.innerHTML = `<table class="xl-cmt"><tr><th></th><th>Predicted +</th><th>Predicted −</th></tr><tr><th>Actually +</th><td class="g">TP <b>${q.tp}</b></td><td class="r">FN <b>${q.fn}</b></td></tr><tr><th>Actually −</th><td class="r">FP <b>${q.fp}</b></td><td class="g">TN <b>${q.tn}</b></td></tr></table>
        <div class="xl-read"><span>Accuracy <b>${fm(acc, 3)}</b></span><span>Precision TP/(TP+FP) <b>${fm(prec, 3)}</b></span><span>Recall TP/(TP+FN) <b>${fm(rec, 3)}</b></span><span>F1 <b>${fm(f1, 3)}</b></span><span>False positive rate <b>${fm(fpr, 3)}</b></span></div>`;
    }
    bindSliders(el, S, draw, { t: v => v.toFixed(2), sep: v => v.toFixed(2) }); draw();
  }

  /* ---- polynomial fit: overfitting and regularization ---- */
  function overfit(el, p) {
    const S = {}; const r = rng(p.seed || 21), f = x => Math.sin(2.6 * x) * .8 + .3 * x;
    const tr = Array.from({ length: p.n || 12 }, (_, i) => { const x = -1 + 2 * (i + .5) / (p.n || 12) + (r() - .5) * .1; return [x, f(x) + gauss(r) * .22]; });
    const te = Array.from({ length: 40 }, () => { const x = -1 + 2 * r(); return [x, f(x) + gauss(r) * .22]; });
    el.innerHTML = head(p, "Underfitting vs overfitting", "Fit a polynomial to the filled training points. Hollow points are new test data the model never saw.") +
      `<div class="mg-sl">${slider("deg", "degree", 0, 11, 1, p.deg ?? 1)}${slider("lam", "regularization λ (log₁₀)", -8, 1, .1, -8)}</div><div class="xl-ofw"><div class="xl-of1"></div><div class="xl-of2"></div></div><div class="xl-read xl-or"></div>`;
    const s1 = stage(el.querySelector(".xl-of1"), 440, 300), s2 = stage(el.querySelector(".xl-of2"), 240, 300), rd = el.querySelector(".xl-or");
    function fit(deg, lam) {
      const n = deg + 1, A = Array.from({ length: n }, () => new Array(n).fill(0)), bv = new Array(n).fill(0);
      tr.forEach(([x, y]) => { const ph = Array.from({ length: n }, (_, k) => x ** k); for (let i = 0; i < n; i++) { bv[i] += ph[i] * y; for (let j = 0; j < n; j++) A[i][j] += ph[i] * ph[j]; } });
      for (let i = 1; i < n; i++) A[i][i] += lam * tr.length; A[0][0] += 1e-10;
      for (let i = 0; i < n; i++) { let mx = i; for (let k = i + 1; k < n; k++) if (Math.abs(A[k][i]) > Math.abs(A[mx][i])) mx = k; [A[i], A[mx]] = [A[mx], A[i]]; [bv[i], bv[mx]] = [bv[mx], bv[i]];
        for (let k = i + 1; k < n; k++) { const fct = A[k][i] / A[i][i]; for (let j = i; j < n; j++) A[k][j] -= fct * A[i][j]; bv[k] -= fct * bv[i]; } }
      const w = new Array(n).fill(0); for (let i = n - 1; i >= 0; i--) { let s = bv[i]; for (let j = i + 1; j < n; j++) s -= A[i][j] * w[j]; w[i] = s / A[i][i]; } return w;
    }
    const ev = (w, x) => w.reduce((s, c, k) => s + c * x ** k, 0), mse = (w, set) => set.reduce((s, [x, y]) => s + (ev(w, x) - y) ** 2, 0) / set.length;
    function draw() {
      const P = PAL(), lam = 10 ** S.lam, w = fit(S.deg, lam), c = s1.c, m = plot(s1, [-1.05, 1.05], [-1.8, 1.8], { l: 36 }); c.clearRect(0, 0, s1.W, s1.H); m.axes({ sx: .5, sy: .5 });
      c.save(); c.beginPath(); c.rect(m.pad.l, m.pad.t, m.pw, m.ph); c.clip();
      c.strokeStyle = "rgba(100,116,139,.45)"; c.setLineDash([5, 5]); c.lineWidth = 2; c.beginPath(); for (let i = 0; i <= 200; i++) { const x = -1.05 + 2.1 * i / 200; i ? c.lineTo(m.X(x), m.Y(f(x))) : c.moveTo(m.X(x), m.Y(f(x))); } c.stroke(); c.setLineDash([]);
      c.strokeStyle = P.a; c.lineWidth = 3.2; c.beginPath(); for (let i = 0; i <= 300; i++) { const x = -1.05 + 2.1 * i / 300; i ? c.lineTo(m.X(x), m.Y(ev(w, x))) : c.moveTo(m.X(x), m.Y(ev(w, x))); } c.stroke();
      te.forEach(([x, y]) => dot(c, m.X(x), m.Y(y), 4, "#fff", P.b, 1.6)); tr.forEach(([x, y]) => dot(c, m.X(x), m.Y(y), 5.5, P.ink, "#fff", 1.5)); c.restore();
      const errs = Array.from({ length: 12 }, (_, d) => { const ww = fit(d, lam); return [mse(ww, tr), mse(ww, te)]; });
      const c2 = s2.c, m2 = plot(s2, [0, 11], [0, 1], { l: 40, b: 26, r: 8 }); c2.clearRect(0, 0, s2.W, s2.H); m2.axes({ xl: "degree", sx: 2, sy: .25 });
      [[0, P.ink, "train"], [1, P.b, "test"]].forEach(([k, col, nm]) => { c2.strokeStyle = col; c2.lineWidth = 2.6; c2.beginPath(); errs.forEach((e, d) => { const y = m2.Y(Math.min(1, e[k])); d ? c2.lineTo(m2.X(d), y) : c2.moveTo(m2.X(d), y); }); c2.stroke();
        c2.fillStyle = col; c2.font = "700 11px \"JetBrains Mono\", monospace"; c2.fillText(nm, m2.X(.3), m2.Y(k ? .9 : .78)); });
      c2.strokeStyle = P.a; c2.setLineDash([4, 3]); c2.beginPath(); c2.moveTo(m2.X(S.deg), m2.pad.t); c2.lineTo(m2.X(S.deg), m2.pad.t + m2.ph); c2.stroke(); c2.setLineDash([]);
      const [etr, ete] = [mse(w, tr), mse(w, te)]; emit(el, { deg: S.deg, lam: S.lam, etr, ete });
      rd.innerHTML = `<span>Training error <b>${fm(etr, 4)}</b></span><span>Test error <b>${fm(ete, 4)}</b></span><span>Weights <b>${w.length}</b>, biggest |w| <b>${fm(Math.max(...w.map(Math.abs)), 1)}</b></span>
        <span class="xl-sum">${S.deg <= 1 ? "Underfitting (high bias): too simple to follow the curve, so both errors are high." : ete > etr * 3 && S.deg >= 7 ? "Overfitting (high variance): the curve threads every training point but swings wildly between them, so test error shoots up." : "A good balance: low training error and low test error."}${S.lam > -4 ? " Regularization is shrinking the weights, which smooths the curve." : ""}</span>`;
    }
    bindSliders(el, S, draw, { deg: v => String(v), lam: v => v <= -7.95 ? "off" : "10^" + v.toFixed(1) }); draw();
  }

  /* ---- softmax with temperature ---- */
  function softmax(el, p) {
    const names = p.classes || ["cat", "dog", "fox", "owl"], S = {}; let truth = 0;
    el.innerHTML = head(p, "Softmax", "Logits (raw scores) become probabilities that add to 1. Click a bar to mark the true class.") +
      `<div class="mg-sl">${names.map((n, i) => slider("z" + i, "z<sub>" + esc(n) + "</sub>", -4, 6, .1, (p.z || [2, 1, .2, -1])[i] ?? 0)).join("")}${slider("T", "temperature T", .1, 5, .05, 1)}</div><div class="xl-bars"></div><div class="xl-read xl-sr"></div>`;
    const bars = el.querySelector(".xl-bars"), sr = el.querySelector(".xl-sr");
    function draw() {
      const z = names.map((_, i) => S["z" + i] / S.T), mx = Math.max(...z), e = z.map(v => Math.exp(v - mx)), sum = e.reduce((a, b) => a + b, 0), pr = e.map(v => v / sum);
      emit(el, { probs: pr, truth, T: S.T, top: pr.indexOf(Math.max(...pr)) });
      bars.innerHTML = names.map((n, i) => `<div class="xl-bar ${i === truth ? "true" : ""}" data-i="${i}"><span>${esc(n)}</span><i style="width:${(pr[i] * 100).toFixed(1)}%;background:${CL[i % CL.length]}"></i><b>${(pr[i] * 100).toFixed(1)}%</b></div>`).join("");
      sr.innerHTML = `<span>Σ probabilities <b>${fm(pr.reduce((a, b) => a + b, 0), 3)}</b></span><span>Cross-entropy loss −ln p(${esc(names[truth])}) <b>${fm(-Math.log(pr[truth]), 3)}</b></span><span class="xl-sum">p<sub>i</sub> = e<sup>z<sub>i</sub>/T</sup> / Σ e<sup>z<sub>j</sub>/T</sup>. Low T makes the biggest logit win almost everything; high T flattens toward ${fm(1 / names.length * 100, 1)}% each.</span>`;
    }
    bindSliders(el, S, draw); bars.addEventListener("click", e => { const b = e.target.closest("[data-i]"); if (b) { truth = +b.dataset.i; draw(); } }); draw();
  }

  /* ---- attention weights ---- */
  function attention(el, p) {
    const toks = p.tokens; let q = p.q ?? toks.length - 1; const S = {};
    el.innerHTML = head(p, "Self-attention", "Click a word to make it the query. Its attention weights are softmax(q·k / √d) over every word.") +
      `<div class="xl-toks"></div><div class="mg-sl">${slider("T", "sharpness (1/√d scale)", .2, 3, .05, 1)}</div><svg class="xl-svg xl-att"></svg><p class="xl-note"></p>`;
    const tk = el.querySelector(".xl-toks"), sv = el.querySelector(".xl-att"), note = el.querySelector(".xl-note");
    function draw() {
      const P = PAL(), qv = toks[q].v, sc = toks.map(t => t.v.reduce((s, x, i) => s + x * qv[i], 0) / Math.sqrt(qv.length) * S.T), mx = Math.max(...sc), e = sc.map(s => Math.exp(s - mx)), sum = e.reduce((a, b) => a + b, 0), w = e.map(x => x / sum);
      tk.innerHTML = toks.map((t, i) => `<button type="button" class="xl-tok ${i === q ? "q" : ""}" data-i="${i}" style="--w:${w[i].toFixed(3)}">${esc(t.w)}<small>${(w[i] * 100).toFixed(0)}%</small></button>`).join("");
      const W = 620, H = 120, n = toks.length, X = i => 30 + i * (W - 60) / Math.max(1, n - 1);
      let s = ""; toks.forEach((t, i) => { if (i === q) return; const x1 = X(q), x2 = X(i), mid = (x1 + x2) / 2, hgt = 18 + Math.abs(x2 - x1) * .25;
        s += `<path d="M${x1} 100Q${mid} ${100 - hgt * 1.4} ${x2} 100" fill="none" stroke="${P.a}" stroke-width="${(1 + w[i] * 16).toFixed(1)}" stroke-opacity="${(.15 + w[i] * 1.6).toFixed(2)}" stroke-linecap="round"/>`; });
      toks.forEach((t, i) => s += `<circle cx="${X(i)}" cy="100" r="${i === q ? 7 : 4}" fill="${i === q ? P.b : P.ink}"/>`);
      sv.setAttribute("viewBox", `0 0 ${W} ${H}`); sv.innerHTML = s;
      const top = w.map((x, i) => [x, i]).filter(([, i]) => i !== q).sort((a, b) => b[0] - a[0])[0];
      note.innerHTML = `“<b>${esc(toks[q].w)}</b>” pays the most attention to “<b>${esc(toks[top[1]].w)}</b>” (${(top[0] * 100).toFixed(0)}%). ${esc(toks[q].note || "")}`;
    }
    bindSliders(el, S, draw); tk.addEventListener("click", e => { const b = e.target.closest("[data-i]"); if (b) { q = +b.dataset.i; draw(); } }); draw();
  }

  /* ---- decision tree split explorer ---- */
  function treesplit(el, p) {
    const data = makeData(p.set || "blobs", 4, 60); const S = {}; let feat = 0;
    el.innerHTML = head(p, "Choosing a decision-tree split", "A tree asks a yes/no question like “is x₁ < 0.5?”. A good question makes each side as pure (one class) as possible.") +
      `<div class="mg-ctl">${B("f0", "Split on x₁", "sm")}${B("f1", "Split on x₂", "sm")}${B("best", "Find the best split", "solid")}</div><div class="mg-sl">${slider("t", "threshold", .02, .98, .01, .5)}</div><div class="xl-tsw"><div class="xl-ts1"></div><div class="xl-ts2"></div></div>`;
    const st = stage(el.querySelector(".xl-ts1"), 360, 360), out = el.querySelector(".xl-ts2");
    const gini = (a, b) => { const n = a + b; return n ? 1 - (a / n) ** 2 - (b / n) ** 2 : 0; };
    function score(f, t) { let la = 0, lb = 0, ra = 0, rb = 0; data.forEach(q => { if (q[f] < t) q[2] ? lb++ : la++; else q[2] ? rb++ : ra++; }); const n = data.length, gl = gini(la, lb), gr = gini(ra, rb); return { la, lb, ra, rb, gl, gr, w: ((la + lb) * gl + (ra + rb) * gr) / n }; }
    function draw() {
      const P = PAL(), c = st.c; c.clearRect(0, 0, st.W, st.H); const t = S.t;
      c.fillStyle = "rgba(100,116,139,.07)"; if (feat === 0) c.fillRect(0, 0, t * st.W, st.H); else c.fillRect(0, (1 - t) * st.H, st.W, t * st.H);
      data.forEach(([a, b, y]) => dot(c, a * st.W, (1 - b) * st.H, 5.5, y ? CB : CA, "#fff", 1.5));
      c.strokeStyle = P.ink; c.lineWidth = 3; c.setLineDash([7, 5]); c.beginPath(); if (feat === 0) { c.moveTo(t * st.W, 0); c.lineTo(t * st.W, st.H); } else { c.moveTo(0, (1 - t) * st.H); c.lineTo(st.W, (1 - t) * st.H); } c.stroke(); c.setLineDash([]);
      c.lineWidth = 1.5; c.strokeRect(.75, .75, st.W - 1.5, st.H - 1.5);
      const s = score(feat, t), root = gini(data.filter(q => !q[2]).length, data.filter(q => q[2]).length), nm = feat ? "x₂" : "x₁";
      const side = (lab, a, b, g) => `<div class="xl-node"><b>${lab}</b><span><i style="background:${CA}"></i>${a} A &nbsp; <i style="background:${CB}"></i>${b} B</span><span>Gini = 1 − (${a}/${a + b || 1})² − (${b}/${a + b || 1})² = <b>${fm(g, 3)}</b></span></div>`;
      emit(el, { gain: root - s.w, feat, t, weighted: s.w });
      out.innerHTML = `<div class="xl-node root"><b>Is ${nm} &lt; ${t.toFixed(2)}?</b><span>Gini before the split: <b>${fm(root, 3)}</b></span></div><div class="xl-kids">${side("Yes", s.la, s.lb, s.gl)}${side("No", s.ra, s.rb, s.gr)}</div>
        <div class="xl-read"><span>Weighted Gini after <b>${fm(s.w, 3)}</b></span><span>Gini gain <b>${fm(root - s.w, 3)}</b></span></div><p class="xl-note">Gini impurity is 0 for a pure group and 0.5 for a 50/50 mix. The tree tries every feature and threshold and keeps the one with the biggest gain.</p>`;
      el.querySelectorAll("[data-act=f0],[data-act=f1]").forEach(b => b.classList.toggle("on", b.dataset.act === "f" + feat));
    }
    bindSliders(el, S, draw, { t: v => v.toFixed(2) });
    el.addEventListener("click", e => { const a = e.target.closest("[data-act]"); if (!a) return; if (a.dataset.act === "best") { let bst = [1, 0, .5]; for (const f of [0, 1]) for (let t = .02; t <= .98; t += .01) { const w = score(f, t).w; if (w < bst[0]) bst = [w, f, t]; } feat = bst[1]; setSl(el, "t", bst[2].toFixed(2)); } else feat = +a.dataset.act[1]; draw(); });
    draw();
  }

  /* ---- PCA ---- */
  function pca(el, p) {
    const r = rng(9), S = {}; const pts = Array.from({ length: 90 }, () => { const u = gauss(r) * 1.6, v = gauss(r) * .45; return [u * .82 - v * .57, u * .57 + v * .82]; });
    el.innerHTML = head(p, "Principal component analysis", "Rotate the line. Each point is projected onto it (the short segments). PC1 is the direction where the projections spread out the most.") +
      `<div class="mg-sl">${slider("ang", "direction (degrees)", 0, 180, 1, 100)}</div>`;
    const st = stage(el, 440, 380);
    el.insertAdjacentHTML("beforeend", `<div class="mg-ctl">${B("pc1", "Snap to PC1", "solid")}<div class="mg-read xl-pr2"></div></div>`);
    const rd = el.querySelector(".xl-pr2");
    const mean = [pts.reduce((s, q) => s + q[0], 0) / pts.length, pts.reduce((s, q) => s + q[1], 0) / pts.length];
    let cxx = 0, cyy = 0, cxy = 0; pts.forEach(([x, y]) => { cxx += (x - mean[0]) ** 2; cyy += (y - mean[1]) ** 2; cxy += (x - mean[0]) * (y - mean[1]); }); cxx /= pts.length; cyy /= pts.length; cxy /= pts.length;
    const best = (Math.atan2(2 * cxy, cxx - cyy) / 2 * 180 / Math.PI + 180) % 180, total = cxx + cyy;
    function draw() {
      const P = PAL(), c = st.c, m = plot(st, [-4.4, 4.4], [-3.8, 3.8], { l: 30 }); c.clearRect(0, 0, st.W, st.H); m.axes({ sx: 1, sy: 1 });
      const a = S.ang * Math.PI / 180, u = [Math.cos(a), Math.sin(a)]; let v = 0;
      c.save(); c.beginPath(); c.rect(m.pad.l, m.pad.t, m.pw, m.ph); c.clip();
      c.strokeStyle = P.a; c.lineWidth = 3; c.beginPath(); c.moveTo(m.X(mean[0] - u[0] * 8), m.Y(mean[1] - u[1] * 8)); c.lineTo(m.X(mean[0] + u[0] * 8), m.Y(mean[1] + u[1] * 8)); c.stroke();
      pts.forEach(([x, y]) => { const d = (x - mean[0]) * u[0] + (y - mean[1]) * u[1], px = mean[0] + d * u[0], py = mean[1] + d * u[1]; v += d * d;
        c.strokeStyle = "rgba(234,88,12,.45)"; c.lineWidth = 1.2; c.beginPath(); c.moveTo(m.X(x), m.Y(y)); c.lineTo(m.X(px), m.Y(py)); c.stroke(); dot(c, m.X(px), m.Y(py), 2.6, P.b); });
      pts.forEach(([x, y]) => dot(c, m.X(x), m.Y(y), 4.2, P.ink + "cc")); c.restore(); v /= pts.length;
      emit(el, { share: v / total, ang: S.ang, best });
      rd.innerHTML = `<span>Variance along the line <b>${fm(v, 3)}</b></span><span>Share of total variance <b>${Math.round(v / total * 100)}%</b></span><span>PC1 is at <b>${Math.round(best)}°</b></span>`;
    }
    bindSliders(el, S, draw, { ang: v => v + "°" });
    el.addEventListener("click", e => { const a = e.target.closest("[data-act]"); if (!a) return; const a0 = S.ang, t0 = performance.now(); const go = now => { const f = still() ? 1 : Math.min(1, (now - t0) / 600); setSl(el, "ang", Math.round(a0 + (best - a0) * (1 - (1 - f) ** 3))); draw(); if (f < 1) requestAnimationFrame(go); }; requestAnimationFrame(go); });
    draw();
  }

  /* ---- perceptron / single neuron ---- */
  function neuron(el, p) {
    const S = {};
    el.innerHTML = head(p, "One artificial neuron", "Weighted sum, add the bias, then the activation function. Change any number.") +
      `<div class="mg-sl">${slider("x1", "x₁", -2, 2, .1, 1)}${slider("x2", "x₂", -2, 2, .1, .5)}${slider("w1", "w₁", -3, 3, .1, 1.5)}${slider("w2", "w₂", -3, 3, .1, -1)}${slider("b", "b", -3, 3, .1, .2)}</div>
      <div class="xl-tabs">${["step", "sigmoid", "tanh", "relu"].map(a => `<button type="button" class="mg-b sm" data-a="${a}">${a}</button>`).join("")}</div><svg class="xl-svg xl-neu" viewBox="0 0 600 220"></svg>`;
    let act = "sigmoid"; const sv = el.querySelector("svg");
    const F = { step: z => z >= 0 ? 1 : 0, sigmoid: z => 1 / (1 + Math.exp(-z)), tanh: Math.tanh, relu: z => Math.max(0, z) };
    function draw() {
      const P = PAL(), z = S.w1 * S.x1 + S.w2 * S.x2 + S.b, y = F[act](z);
      let curve = ""; for (let i = 0; i <= 60; i++) { const zz = -4 + 8 * i / 60, yy = F[act](zz), ys = act === "relu" ? yy / 4 : act === "tanh" ? (yy + 1) / 2 : yy; curve += (i ? "L" : "M") + (430 + i * 1.6) + " " + (150 - ys * 80); }
      const zc = Math.max(-4, Math.min(4, z)), yc = act === "relu" ? Math.min(4, y) / 4 : act === "tanh" ? (y + 1) / 2 : y;
      sv.innerHTML = `<g font-family="JetBrains Mono" font-size="14" font-weight="700" fill="${P.ink}">
        <circle cx="50" cy="60" r="24" fill="#fff" stroke="${P.ink}" stroke-width="2"/><text x="50" y="65" text-anchor="middle">${fm(S.x1, 1)}</text><text x="50" y="25" text-anchor="middle" font-size="12">x₁</text>
        <circle cx="50" cy="160" r="24" fill="#fff" stroke="${P.ink}" stroke-width="2"/><text x="50" y="165" text-anchor="middle">${fm(S.x2, 1)}</text><text x="50" y="205" text-anchor="middle" font-size="12">x₂</text>
        <line x1="74" y1="66" x2="220" y2="102" stroke="${S.w1 >= 0 ? CA : CB}" stroke-width="${1 + Math.abs(S.w1) * 2}"/><text x="140" y="70" font-size="13">× ${fm(S.w1, 1)}</text>
        <line x1="74" y1="154" x2="220" y2="118" stroke="${S.w2 >= 0 ? CA : CB}" stroke-width="${1 + Math.abs(S.w2) * 2}"/><text x="140" y="162" font-size="13">× ${fm(S.w2, 1)}</text>
        <circle cx="250" cy="110" r="32" fill="#fff" stroke="${P.ink}" stroke-width="2.4"/><text x="250" y="106" text-anchor="middle" font-size="18">Σ</text><text x="250" y="126" text-anchor="middle" font-size="11">+ ${fm(S.b, 1)}</text>
        <line x1="282" y1="110" x2="400" y2="110" stroke="${P.ink}" stroke-width="2.4"/><text x="340" y="100" text-anchor="middle" font-size="13">z = ${fm(z, 2)}</text>
        <rect x="420" y="60" width="116" height="100" rx="10" fill="#fff" stroke="${P.line}"/><path d="${curve}" fill="none" stroke="${P.a}" stroke-width="2.6"/><circle cx="${430 + (zc + 4) / 8 * 96}" cy="${150 - yc * 80}" r="5.5" fill="${P.b}"/>
        <text x="478" y="178" text-anchor="middle" font-size="12">${act}(z)</text><line x1="536" y1="110" x2="560" y2="110" stroke="${P.ink}" stroke-width="2.4"/>
        <text x="575" y="104" text-anchor="middle" font-size="12">ŷ</text><text x="575" y="124" text-anchor="middle" font-size="16" fill="${P.b}">${fm(y, 3)}</text></g>
        <text x="300" y="212" text-anchor="middle" font-family="JetBrains Mono" font-size="12.5" fill="${P.muted}">z = ${fm(S.w1, 1)}·${fm(S.x1, 1)} + ${fm(S.w2, 1)}·${fm(S.x2, 1)} + ${fm(S.b, 1)} = ${fm(z, 3)}   →   ŷ = ${act}(${fm(z, 2)}) = ${fm(y, 3)}</text>`;
      el.querySelectorAll("[data-a]").forEach(b => b.classList.toggle("on", b.dataset.a === act));
    }
    bindSliders(el, S, draw, Object.fromEntries(["x1", "x2", "w1", "w2", "b"].map(k => [k, v => v.toFixed(1)])));
    el.addEventListener("click", e => { const b = e.target.closest("[data-a]"); if (b) { act = b.dataset.a; draw(); } }); draw();
  }

  /* ---- convolution ---- */
  function conv(el, p) {
    const img = p.img || ["0000000000", "0000110000", "0001111000", "0011111100", "0011111100", "0001111000", "0000110000", "0000000000"].map(r => [...r].map(Number));
    const K = { "Vertical edges": [[1, 0, -1], [1, 0, -1], [1, 0, -1]], "Horizontal edges": [[1, 1, 1], [0, 0, 0], [-1, -1, -1]], "Blur": [[1, 1, 1], [1, 1, 1], [1, 1, 1]].map(r => r.map(v => v / 9)), "Sharpen": [[0, -1, 0], [-1, 5, -1], [0, -1, 0]] };
    let kn = Object.keys(K)[0], pos = 0, timer = null; const H = img.length, W = img[0].length, oh = H - 2, ow = W - 2;
    el.innerHTML = head(p, "Convolution", "A 3×3 filter slides over the image. Each output pixel is the sum of (pixel × filter weight) under the window. Click a pixel to paint it.") +
      `<div class="xl-tabs">${Object.keys(K).map(k => `<button type="button" class="mg-b sm" data-k="${k}">${k}</button>`).join("")}</div><div class="xl-conv"><div class="xl-ci"></div><div class="xl-ck"></div><div class="xl-co"></div></div><p class="xl-note"></p>
      <div class="mg-ctl">${B("step", "Slide ▸", "solid")}${B("play", "Play")}${B("all", "Compute all")}</div>`;
    const ci = el.querySelector(".xl-ci"), ck = el.querySelector(".xl-ck"), co = el.querySelector(".xl-co"), note = el.querySelector(".xl-note"); let shown = 0;
    const out = (r, c) => { let s = 0; for (let i = 0; i < 3; i++) for (let j = 0; j < 3; j++) s += img[r + i][c + j] * K[kn][i][j]; return s; };
    function draw() {
      const r0 = Math.floor(pos / ow), c0 = pos % ow;
      ci.innerHTML = `<small>Input</small><div class="xl-grid" style="--c:${W}">${img.map((row, r) => row.map((v, c) => `<i data-r="${r}" data-c="${c}" class="${r >= r0 && r < r0 + 3 && c >= c0 && c < c0 + 3 ? "win" : ""}" style="background:${v ? "#0F172A" : "#fff"}"></i>`).join("")).join("")}</div>`;
      ck.innerHTML = `<small>Filter</small><div class="xl-grid k" style="--c:3">${K[kn].flat().map(v => `<i>${fm(v, 2)}</i>`).join("")}</div>`;
      let mx = 0; for (let r = 0; r < oh; r++) for (let c = 0; c < ow; c++) mx = Math.max(mx, Math.abs(out(r, c)));
      co.innerHTML = `<small>Output (feature map)</small><div class="xl-grid" style="--c:${ow}">${Array.from({ length: oh * ow }, (_, k) => { const r = Math.floor(k / ow), c = k % ow, v = out(r, c), t = mx ? v / mx : 0;
        return `<i class="${k === pos ? "win" : ""}" style="background:${k <= shown ? (t >= 0 ? `rgba(37,99,235,${Math.abs(t)})` : `rgba(234,88,12,${Math.abs(t)})`) : "#F1F5F9"}">${k <= shown && ow <= 10 ? `<em>${fm(v, 1)}</em>` : ""}</i>`; }).join("")}</div>`;
      const terms = []; for (let i = 0; i < 3; i++) for (let j = 0; j < 3; j++) if (K[kn][i][j] && img[r0 + i][c0 + j]) terms.push(fm(K[kn][i][j], 2));
      note.innerHTML = `Window at row ${r0}, column ${c0}: sum of weights under the dark pixels = ${terms.length ? terms.join(" + ").replace(/\+ −/g, "− ") : "0"} = <b>${fm(out(r0, c0), 2)}</b>. Blue = strong positive response, orange = strong negative.`;
      el.querySelectorAll("[data-k]").forEach(b => b.classList.toggle("on", b.dataset.k === kn));
    }
    el.addEventListener("click", e => { const k = e.target.closest("[data-k]"); if (k) { kn = k.dataset.k; draw(); return; }
      const px = e.target.closest(".xl-ci i[data-r]"); if (px) { img[+px.dataset.r][+px.dataset.c] ^= 1; draw(); return; }
      const a = e.target.closest("[data-act]"); if (!a) return; clearInterval(timer);
      if (a.dataset.act === "step") { pos = (pos + 1) % (oh * ow); shown = Math.max(shown, pos); if (pos === 0) shown = 0; }
      if (a.dataset.act === "all") { shown = oh * ow; }
      if (a.dataset.act === "play") { timer = setInterval(() => { pos = (pos + 1) % (oh * ow); shown = Math.max(shown, pos); draw(); if (pos === oh * ow - 1) clearInterval(timer); }, still() ? 10 : 140); }
      draw(); });
    draw();
  }

  function heroArt() {
    const hero = document.querySelector(".hero"); if (!hero || hero.querySelector(".lab-art")) return;
    const b = document.body; let svg = "";
    if (b.classList.contains("th-ce")) {
      const tr = ["M20 60H90L110 80H140", "M20 120H140", "M20 180H70L100 150H140", "M180 80H210L230 50H290", "M180 120H290", "M180 160H220L240 190H290", "M150 40V20", "M170 40V20", "M150 200V222", "M170 200V222"];
      svg = `<svg viewBox="0 0 310 240"><rect width="310" height="240" rx="14" fill="#0E3B2F"/>${Array.from({ length: 60 }, (_, i) => `<circle cx="${12 + (i % 15) * 20.5}" cy="${12 + Math.floor(i / 15) * 72}" r="1.6" fill="rgba(255,255,255,.12)"/>`).join("")}
        ${tr.map(d => `<path class="tr" d="${d}"/>`).join("")}${tr.map((d, i) => `<path class="pulse" d="${d}" style="animation-delay:${(i * .37).toFixed(2)}s"/>`).join("")}
        ${[[20, 60], [20, 120], [20, 180], [290, 50], [290, 120], [290, 190]].map(([x, y]) => `<circle cx="${x}" cy="${y}" r="6" fill="#C08A3E"/><circle cx="${x}" cy="${y}" r="2.4" fill="#0E3B2F"/>`).join("")}
        <rect x="140" y="40" width="40" height="160" rx="6" fill="#111827" stroke="#334155"/>${Array.from({ length: 6 }, (_, i) => `<rect x="134" y="${54 + i * 24}" width="6" height="8" fill="#C0C7D0"/><rect x="180" y="${54 + i * 24}" width="6" height="8" fill="#C0C7D0"/>`).join("")}
        <circle cx="152" cy="52" r="3" fill="#334155"/><text x="160" y="126" text-anchor="middle" font-family="JetBrains Mono" font-weight="800" font-size="12" fill="#E5E7EB" transform="rotate(-90 160 120)">CPU · 8-BIT</text></svg>`;
    } else if (b.classList.contains("th-ml")) {
      const L = [[3, 60], [5, 150], [5, 240], [2, 300]].map(([n, x]) => Array.from({ length: n }, (_, i) => [x - 20, 120 + (i - (n - 1) / 2) * 40]));
      let e = "", n = "", k = 0;
      for (let l = 0; l < 3; l++) L[l].forEach(a => L[l + 1].forEach(c => { const f = (k++ * 7) % 5 === 0; e += `<line class="edge${f ? " f" : ""}" x1="${a[0]}" y1="${a[1]}" x2="${c[0]}" y2="${c[1]}" style="animation-delay:${(l * .5 + (k % 4) * .2).toFixed(2)}s"/>`; }));
      L.forEach((ly, l) => ly.forEach(([x, y], i) => n += `<circle class="nd${(i + l) % 2 ? " on" : ""}" cx="${x}" cy="${y}" r="11" style="animation-delay:${(l * .5).toFixed(2)}s"/>`));
      svg = `<svg viewBox="0 0 310 240"><rect width="310" height="240" rx="14" fill="#fff" stroke="#DDD3F7"/>${e}${n}
        <text x="40" y="226" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="#6D28D9">x</text><text x="280" y="226" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="#EA580C">ŷ</text></svg>`;
    } else return;
    const a = document.createElement("div"); a.className = "lab-art"; a.setAttribute("aria-hidden", "true"); a.innerHTML = svg; hero.appendChild(a);
  }
  const LABS = { bits, float32, gate, circuit, kmap, flipflop, fsm, cpu, cache, ohm, cmos, pipeline, regress, gd, classify, kmeans, nnet, threshold, overfit, softmax, attention, treesplit, pca, neuron, conv };
  function boot() {
    heroArt();
    document.querySelectorAll(".xlab[data-lab]").forEach(el => {
      if (el.dataset.ready) return; el.dataset.ready = "1";
      let p; try { p = JSON.parse(el.dataset.lab); } catch (e) { return; }
      const f = LABS[p.type]; if (!f) return;
      try { f(el, p); } catch (err) { el.innerHTML = `<p class="xl-note">This lab could not load.</p>`; console.error(err); }
    });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot); else boot();
  window.XLabs = { boot, gatePath, gateSVG, G, makeData, rng, gauss, emit, stage, plot, dot, PAL, CL, shade: typeof shade !== "undefined" ? shade : null };
})();
