/* ===== Apogee — 2D animated examples =====
   Usage in HTML:  <div class="sim" data-sim='{"type":"collide","m1":2,"v1":5,"m2":3,"v2":-2,"mode":"stick"}'></div>
   Quiz questions can carry a "sim" object; the answer values stay hidden until the question is answered.
   Add "reveal":true to a data-sim to show answer values from the start.
   To add a new animation type: add SIMS.yourType = p => ({ D: seconds, hold: seconds, draw(c, t, rev) {...} }). */
(function () {
  const W = 720, H = 270;
  const C = { y: "#FFC857", b: "#7CC4FF", w: "#EEF3FF", m: "#A3B0D0", r: "#FF6B6B", g: "#5BE3A4", o: "#FF9F5A", p: "#C3B5FF",
              line: "rgba(255,255,255,.28)", faint: "rgba(255,255,255,.10)", dark: "#050816" };
  const G = 10;
  const reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- formatting ---------- */
  function f(n, d) {
    if (!isFinite(n)) return "?";
    const a = Math.abs(n);
    if (d === undefined) d = a >= 100 ? 0 : a >= 10 ? 1 : 2;
    let s = n.toFixed(d);
    if (s.includes(".")) s = s.replace(/0+$/, "").replace(/\.$/, "");
    if (a >= 1000) s = Number(s).toLocaleString("en-US");
    return s === "-0" ? "0" : s;
  }
  const fs = n => (n > 0 ? "+" : "") + f(n);

  /* ---------- drawing helpers ---------- */
  function txt(c, s, x, y, o = {}) {
    c.font = `${o.b ? "700 " : "500 "}${o.s || 14}px "Plus Jakarta Sans", system-ui, sans-serif`;
    c.fillStyle = o.c || C.w; c.textAlign = o.a || "left"; c.textBaseline = o.bl || "alphabetic";
    c.fillText(s, x, y);
  }
  function arrow(c, x1, y1, x2, y2, col, lab, o = {}) {
    const L = Math.hypot(x2 - x1, y2 - y1);
    if (L < 3) return;
    c.save();
    c.strokeStyle = col; c.fillStyle = col; c.lineWidth = o.w || 3; c.lineCap = "round";
    if (o.dash) c.setLineDash([6, 5]);
    const a = Math.atan2(y2 - y1, x2 - x1), h = Math.min(12, L * 0.5);
    c.beginPath(); c.moveTo(x1, y1); c.lineTo(x2 - Math.cos(a) * h * 0.6, y2 - Math.sin(a) * h * 0.6); c.stroke();
    c.setLineDash([]);
    c.beginPath(); c.moveTo(x2, y2);
    c.lineTo(x2 - h * Math.cos(a - 0.45), y2 - h * Math.sin(a - 0.45));
    c.lineTo(x2 - h * Math.cos(a + 0.45), y2 - h * Math.sin(a + 0.45));
    c.closePath(); c.fill();
    c.restore();
    if (lab) txt(c, lab, x2 + (o.lx ?? 6), y2 + (o.ly ?? -6), { c: col, s: 13, b: 1, a: o.la || "left" });
  }
  function rr(c, x, y, w, h, r) {
    c.beginPath(); c.moveTo(x + r, y); c.arcTo(x + w, y, x + w, y + h, r); c.arcTo(x + w, y + h, x, y + h, r);
    c.arcTo(x, y + h, x, y, r); c.arcTo(x, y, x + w, y, r); c.closePath();
  }
  function ground(c, y, x0 = 16, x1 = W - 16) {
    c.strokeStyle = C.line; c.lineWidth = 2; c.beginPath(); c.moveTo(x0, y); c.lineTo(x1, y); c.stroke();
    c.strokeStyle = C.faint; c.lineWidth = 1;
    for (let x = x0; x < x1; x += 14) { c.beginPath(); c.moveTo(x, y + 2); c.lineTo(x - 8, y + 10); c.stroke(); }
  }
  function cart(c, x, y, w, h, col, lab, labCol) {
    // x = left edge, y = ground
    c.save();
    c.shadowColor = col; c.shadowBlur = 14;
    c.fillStyle = col; rr(c, x, y - h - 9, w, h, 7); c.fill();
    c.restore();
    c.fillStyle = "#0E1A3A"; c.strokeStyle = C.m; c.lineWidth = 2;
    [x + w * 0.25, x + w * 0.75].forEach(cx => { c.beginPath(); c.arc(cx, y - 6, 6, 0, 7); c.fill(); c.stroke(); });
    if (lab) txt(c, lab, x + w / 2, y - h / 2 - 9, { c: labCol || C.dark, s: 13, b: 1, a: "center", bl: "middle" });
  }
  function box(c, x, y, w, h, col, lab) {
    c.save(); c.shadowColor = col; c.shadowBlur = 12; c.fillStyle = col; rr(c, x, y, w, h, 6); c.fill(); c.restore();
    if (lab) txt(c, lab, x + w / 2, y + h / 2, { c: C.dark, s: 13, b: 1, a: "center", bl: "middle" });
  }
  function ball(c, x, y, r, col, lab) {
    c.save(); c.shadowColor = col; c.shadowBlur = 16;
    const g = c.createRadialGradient(x - r * 0.35, y - r * 0.35, r * 0.1, x, y, r);
    g.addColorStop(0, "#EEF3FF"); g.addColorStop(0.25, col); g.addColorStop(1, col);
    c.fillStyle = g; c.beginPath(); c.arc(x, y, r, 0, 7); c.fill(); c.restore();
    if (lab) txt(c, lab, x, y, { c: C.dark, s: 12, b: 1, a: "center", bl: "middle" });
  }
  // vertical energy bars. items: [{l, v, c}], max = value that fills hMax
  function bars(c, x, yBase, items, max, hMax = 120, title) {
    if (title) txt(c, title, x - 4, yBase - hMax - 18, { c: C.m, s: 12, b: 1 });
    items.forEach((it, i) => {
      const bx = x + i * 44, h = Math.max(0, Math.min(1.05, it.v / max)) * hMax;
      c.fillStyle = C.faint; rr(c, bx, yBase - hMax, 30, hMax, 5); c.fill();
      if (h > 0.5) { c.fillStyle = it.c; rr(c, bx, yBase - h, 30, h, 5); c.fill(); }
      txt(c, it.l, bx + 15, yBase + 16, { c: C.m, s: 13, b: 1, a: "center" });
    });
  }
  // readout panel. lines: [text] or [text, true] (true = answer, hidden until revealed)
  function panel(c, lines, x, y, rev, o = {}) {
    lines.forEach((ln, i) => {
      const [s, ans] = Array.isArray(ln) ? ln : [ln, false];
      const yy = y + i * 21;
      if (ans && !rev) txt(c, s.split("=")[0] + "= ?", x, yy, { c: C.y, s: 15, b: 1, a: o.a });
      else txt(c, s, x, yy, { c: ans ? C.y : C.w, s: 15, b: ans ? 1 : 0, a: o.a });
    });
  }
  function flash(c, x, y, k) {
    if (k <= 0 || k >= 1) return;
    c.save(); c.globalAlpha = 1 - k; c.strokeStyle = C.y; c.lineWidth = 3;
    for (let i = 0; i < 8; i++) {
      const a = (i / 8) * Math.PI * 2, r1 = 10 + k * 18, r2 = 18 + k * 34;
      c.beginPath(); c.moveTo(x + Math.cos(a) * r1, y + Math.sin(a) * r1); c.lineTo(x + Math.cos(a) * r2, y + Math.sin(a) * r2); c.stroke();
    }
    c.restore();
  }
  const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
  const ease = s => s * s * (3 - 2 * s);
  const cartW = (m, mmax) => 54 + 46 * Math.sqrt(m / mmax);

  /* ---------- objects that match the word problems ----------
     thing(c, kind, x, gy, w, h, col, label, dir): x = left edge, gy = ground line, dir = facing (+1 right, -1 left)
     kinds: cart, ball, car, truck, box, crate, sled, person, skater, bullet, rifle, glider, coaster */
  function pill(c, s, x, y) {
    c.font = '700 12px "Plus Jakarta Sans", system-ui, sans-serif';
    const w = c.measureText(s).width + 10;
    c.fillStyle = "rgba(5,8,22,.85)"; rr(c, x - w / 2, y - 9, w, 18, 9); c.fill();
    txt(c, s, x, y + 1, { c: "#EEF3FF", s: 12, b: 1, a: "center", bl: "middle" });
  }
  function wheel(c, x, y, r) { c.fillStyle = "#0E1A3A"; c.strokeStyle = C.m; c.lineWidth = 2; c.beginPath(); c.arc(x, y, r, 0, 7); c.fill(); c.stroke(); c.fillStyle = C.m; c.beginPath(); c.arc(x, y, r * 0.3, 0, 7); c.fill(); }
  function figure(c, cx, gy, H, col, skate, pose) {
    // simple person: H = total height
    const head = H * 0.13, hip = gy - H * 0.47 - (skate ? 6 : 0), sh = gy - H * 0.8 - (skate ? 6 : 0), foot = gy - (skate ? 6 : 0);
    c.save(); c.strokeStyle = col; c.lineWidth = Math.max(3, H * 0.07); c.lineCap = "round"; c.lineJoin = "round";
    const sw = pose || 0;
    c.beginPath();
    c.moveTo(cx, hip); c.lineTo(cx - H * 0.12 - sw, foot); c.moveTo(cx, hip); c.lineTo(cx + H * 0.12 + sw, foot);
    c.moveTo(cx, hip); c.lineTo(cx, sh);
    c.moveTo(cx, sh + H * 0.04); c.lineTo(cx - H * 0.2, sh + H * 0.22); c.moveTo(cx, sh + H * 0.04); c.lineTo(cx + H * 0.2, sh + H * 0.22);
    c.stroke();
    c.fillStyle = col; c.beginPath(); c.arc(cx, sh - head, head, 0, 7); c.fill();
    if (skate) { c.strokeStyle = C.m; c.lineWidth = 2; [[-H * 0.12 - sw], [H * 0.12 + sw]].forEach(([dx]) => { c.beginPath(); c.moveTo(cx + dx - 9, gy - 1); c.lineTo(cx + dx + 9, gy - 1); c.stroke(); }); }
    c.restore();
  }
  function thing(c, kind, x, gy, w, h, col, lab, dir = 1) {
    kind = kind || "cart";
    c.save();
    if (kind === "cart") { c.restore(); return cart(c, x, gy, w, h, col, lab); }
    if (kind === "box" || kind === "crate" || kind === "block") {
      box(c, x, gy - h, w, h, col, "");
      if (kind === "crate") { c.strokeStyle = "rgba(5,8,22,.45)"; c.lineWidth = 3; c.strokeRect(x + 5, gy - h + 5, w - 10, h - 10); c.beginPath(); c.moveTo(x + 5, gy - h + 5); c.lineTo(x + w - 5, gy - 5); c.stroke(); }
      if (lab) txt(c, lab, x + w / 2, gy - h / 2, { c: C.dark, s: 13, b: 1, a: "center", bl: "middle" });
    } else if (kind === "ball") {
      const r = Math.min(w, h + 10) / 2, cx = x + w / 2, cy = gy - r;
      ball(c, cx, cy, r, col);
      c.strokeStyle = "rgba(5,8,22,.35)"; c.lineWidth = 2; const a = x / r;
      c.beginPath(); c.arc(cx, cy, r * 0.75, a, a + 1.2); c.stroke();
      if (lab) txt(c, lab, cx, cy, { c: C.dark, s: 12, b: 1, a: "center", bl: "middle" });
    } else if (kind === "car" || kind === "truck") {
      const bh = h * 0.55, by = gy - 9 - bh;
      c.shadowColor = col; c.shadowBlur = 12; c.fillStyle = col;
      rr(c, x, by, w, bh, 7); c.fill();
      c.beginPath();
      if (kind === "car") {
        const l = dir > 0 ? x + w * 0.18 : x + w * 0.3, r = dir > 0 ? x + w * 0.7 : x + w * 0.82;
        c.moveTo(l, by + 2); c.lineTo(l + w * 0.1, by - h * 0.4); c.lineTo(r - w * 0.12, by - h * 0.4); c.lineTo(r, by + 2); c.closePath(); c.fill();
        c.shadowBlur = 0; c.fillStyle = "rgba(5,8,22,.65)";
        c.beginPath(); c.moveTo(l + w * 0.06, by); c.lineTo(l + w * 0.13, by - h * 0.32); c.lineTo(r - w * 0.15, by - h * 0.32); c.lineTo(r - w * 0.06, by); c.closePath(); c.fill();
      } else {
        const cab = dir > 0 ? x + w * 0.68 : x, cw = w * 0.32;
        rr(c, cab, by - h * 0.5, cw, h * 0.55, 5); c.fill(); c.shadowBlur = 0;
        c.fillStyle = "rgba(5,8,22,.65)"; c.fillRect(cab + cw * 0.2, by - h * 0.42, cw * 0.6, h * 0.22);
      }
      c.shadowBlur = 0; c.fillStyle = "#FFF4D6";
      c.beginPath(); c.arc(dir > 0 ? x + w - 4 : x + 4, by + bh * 0.35, 3, 0, 7); c.fill();
      wheel(c, x + w * 0.22, gy - 8, 8); wheel(c, x + w * 0.78, gy - 8, 8);
      if (lab) txt(c, lab, x + w / 2, by + bh / 2 + 1, { c: C.dark, s: 12, b: 1, a: "center", bl: "middle" });
    } else if (kind === "sled") {
      const bh = h * 0.7;
      box(c, x + 6, gy - 10 - bh, w - 12, bh, col, "");
      c.strokeStyle = C.m; c.lineWidth = 3; c.lineCap = "round";
      c.beginPath(); c.moveTo(x, gy - 2); c.lineTo(x + w - 4, gy - 2); c.quadraticCurveTo(x + w + 8, gy - 2, x + w + 6, gy - 14); c.stroke();
      c.lineWidth = 2; c.beginPath(); c.moveTo(x + 14, gy - 2); c.lineTo(x + 14, gy - 10); c.moveTo(x + w - 18, gy - 2); c.lineTo(x + w - 18, gy - 10); c.stroke();
      if (lab) txt(c, lab, x + w / 2, gy - 10 - bh / 2, { c: C.dark, s: 12, b: 1, a: "center", bl: "middle" });
    } else if (kind === "person" || kind === "skater") {
      const H = clamp(h * 1.9, 60, 92), cx = x + w / 2;
      figure(c, cx, gy, H, col, kind === "skater");
      if (lab) pill(c, lab, cx, gy - H * 0.62);
    } else if (kind === "bullet") {
      const bw = Math.min(w, 34), bh = 11, by = gy - 34;
      c.fillStyle = col; c.shadowColor = col; c.shadowBlur = 10;
      c.beginPath();
      if (dir > 0) { c.moveTo(x, by); c.lineTo(x + bw - 10, by); c.quadraticCurveTo(x + bw + 2, by + bh / 2, x + bw - 10, by + bh); c.lineTo(x, by + bh); }
      else { c.moveTo(x + bw, by); c.lineTo(x + 10, by); c.quadraticCurveTo(x - 2, by + bh / 2, x + 10, by + bh); c.lineTo(x + bw, by + bh); }
      c.closePath(); c.fill();
      if (lab) txt(c, lab, x + bw / 2, by - 8, { c: col, s: 12, b: 1, a: "center" });
    } else if (kind === "rifle") {
      const by = gy - 40; c.fillStyle = col; c.shadowColor = col; c.shadowBlur = 10;
      const f = dir > 0 ? 1 : -1, x0 = dir > 0 ? x : x + w;
      c.beginPath();
      c.moveTo(x0, by + 4); c.lineTo(x0 + f * w * 0.35, by); c.lineTo(x0 + f * w, by); c.lineTo(x0 + f * w, by + 7);
      c.lineTo(x0 + f * w * 0.45, by + 9); c.lineTo(x0 + f * w * 0.4, by + 20); c.lineTo(x0 + f * w * 0.32, by + 20); c.lineTo(x0 + f * w * 0.3, by + 12); c.lineTo(x0, by + 26); c.closePath(); c.fill();
      if (lab) txt(c, lab, x + w / 2, by - 10, { c: col, s: 12, b: 1, a: "center" });
    } else if (kind === "glider") {
      c.fillStyle = C.m; c.fillRect(x - 6, gy - 6, w + 12, 3);
      c.shadowColor = col; c.shadowBlur = 12; c.fillStyle = col;
      c.beginPath(); c.moveTo(x, gy - 8); c.lineTo(x + w * 0.5, gy - 8 - h * 0.8); c.lineTo(x + w, gy - 8); c.lineTo(x + w - 8, gy - 8); c.lineTo(x + w * 0.5, gy - 8 - h * 0.8 + 12); c.lineTo(x + 8, gy - 8); c.closePath(); c.fill();
      c.fillRect(x, gy - 10, w, 5);
      if (lab) pill(c, lab, x + w / 2, gy - h * 0.8 - 18);
    } else if (kind === "coaster") {
      const bh = h * 0.6, by = gy - 9 - bh;
      c.shadowColor = col; c.shadowBlur = 12; c.fillStyle = col;
      c.beginPath(); c.moveTo(x, by); c.lineTo(x + w, by); c.lineTo(x + w - 6, by + bh); c.lineTo(x + 6, by + bh); c.closePath(); c.fill();
      c.shadowBlur = 0; c.fillStyle = C.m;
      [0.3, 0.7].forEach(k => { c.beginPath(); c.arc(x + w * k, by - 7, 6, 0, 7); c.fill(); });
      wheel(c, x + w * 0.25, gy - 6, 6); wheel(c, x + w * 0.75, gy - 6, 6);
      if (lab) txt(c, lab, x + w / 2, by + bh / 2, { c: C.dark, s: 12, b: 1, a: "center", bl: "middle" });
    }
    c.restore();
  }

  /* ---------- animation types ---------- */
  const SIMS = {};

  // single moving object, shows K or p
  SIMS.cart = p => ({
    D: 3, hold: 0.8,
    draw(c, t, rev) {
      ground(c, 200);
      const x = 40 + (520 / 3) * t;
      thing(c, p.obj, x, 200, 90, 46, C.y, f(p.m) + " kg");
      arrow(c, x + 45, 120, x + 45 + 70, 120, C.b, "v = " + f(p.v) + " m/s");
      const res = p.show === "p" ? ["p = mv = " + f(p.m * p.v) + " kg·m/s", true] : ["K = ½mv² = " + f(0.5 * p.m * p.v * p.v) + " J", true];
      panel(c, ["m = " + f(p.m) + " kg", "v = " + f(p.v) + " m/s", res], 24, 36, rev);
    }
  });

  // two lanes, speed v vs k·v, with K bars
  SIMS.compare = p => {
    const v1 = p.v1 || 1, v2 = p.v2 || 2, vmax = Math.max(v1, v2);
    return {
      D: 3, hold: 1,
      draw(c, t, rev) {
        [[v1, 110, "v"], [v2, 220, f(v2 / v1) + "v"]].forEach(([v, y, lab], i) => {
          ground(c, y, 16, 540);
          const x = 30 + (400 / 3) * t * (v / vmax);
          thing(c, p.obj, x, y, 76, 38, i ? C.b : C.y, "m");
          arrow(c, x + 38, y - 64, x + 38 + 34 * (v / vmax) + 18, y - 64, C.w, lab, { w: 2.5 });
        });
        const K1 = v1 * v1, K2 = v2 * v2;
        if (rev) bars(c, 590, 220, [{ l: "K₁", v: K1, c: C.y }, { l: "K₂", v: K2, c: C.b }], K2, 150, "Kinetic energy");
        else { txt(c, "Kinetic energy", 586, 60, { c: C.m, s: 12, b: 1 }); txt(c, "K₂ / K₁ = ?", 586, 130, { c: C.y, s: 16, b: 1 }); }
        if (rev) txt(c, "K₂ = " + f(K2 / K1) + " × K₁", 586, 262, { c: C.y, s: 14, b: 1 });
      }
    };
  };

  // braking distance: same friction, speeds v1 and v2
  SIMS.brake = p => {
    const v1 = p.v1, v2 = p.v2, d1 = p.d1, d2 = d1 * (v2 / v1) ** 2;
    const sc = 560 / d2, T2 = 4, T1 = T2 * (v1 / v2);
    return {
      D: T2, hold: 1.2,
      draw(c, t, rev) {
        [[v1, d1, T1, 105, C.y, "v"], [v2, d2, T2, 225, C.b, f(v2 / v1) + "v"]].forEach(([v, d, T, y, col, lab], i) => {
          ground(c, y);
          const s = clamp(t / T, 0, 1), x = 40 + d * sc * (1 - (1 - s) ** 2);
          const stopX = 40 + d * sc;
          c.strokeStyle = col; c.setLineDash([4, 5]); c.lineWidth = 1.5;
          c.beginPath(); c.moveTo(stopX + 64, y - 70); c.lineTo(stopX + 64, y + 6); c.stroke(); c.setLineDash([]);
          const known = i === 0 || rev;
          txt(c, known ? f(d) + " m" : "? m", stopX + 64, y - 76, { c: col, s: 14, b: 1, a: "center" });
          thing(c, p.obj || "car", x, y, 74, 34, col, "");
          if (s < 1) arrow(c, x + 37, y - 56, x + 37 + 46 * (1 - s) + 6, y - 56, C.w, lab, { w: 2.5 });
          else txt(c, "stopped", x + 37, y - 50, { c: C.m, s: 12, a: "center" });
          if (s < 1) arrow(c, x - 2, y - 22, x - 34, y - 22, C.r, "f", { w: 2.5, la: "right", lx: -4 });
        });
        txt(c, "Same braking force, so d ∝ v²", 24, 262, { c: C.m, s: 13, b: 1 });
      }
    };
  };

  // box lifted at constant speed
  SIMS.lift = p => {
    const hpx = 150;
    return {
      D: 3, hold: 1,
      draw(c, t, rev) {
        ground(c, 230, 120, 420);
        const s = ease(clamp(t / 3, 0, 1)), y = 230 - 44 - s * hpx;
        c.strokeStyle = C.line; c.lineWidth = 1.5; c.beginPath(); c.moveTo(150, 230); c.lineTo(150, 230 - hpx - 44); c.stroke();
        for (let i = 0; i <= 3; i++) { const yy = 186 - (i * hpx) / 3; c.beginPath(); c.moveTo(144, yy); c.lineTo(156, yy); c.stroke(); txt(c, f((p.h * i) / 3) + " m", 138, yy + 4, { c: C.m, s: 11, a: "right" }); }
        thing(c, p.obj || "box", 230, y + 44, 60, 44, C.y, f(p.m) + " kg");
        arrow(c, 260, y, 260, y - 44, C.g, "F = mg", { w: 2.5 });
        arrow(c, 260, y + 44, 260, y + 84, C.r, "mg", { w: 2.5 });
        const U = p.m * G * p.h * s;
        bars(c, 480, 230, [{ l: "Ug", v: U, c: C.b }], p.m * G * p.h, 150, "Energy");
        panel(c, ["m = " + f(p.m) + " kg", "Δy = " + f(p.h) + " m", ["ΔU = mgΔy = " + f(p.m * G * p.h) + " J", true]], 560, 60, rev);
      }
    };
  };

  // pendulum with energy bars
  SIMS.pendulum = p => {
    const L = p.L || 1.2, h = p.h, th0 = Math.acos(1 - h / L), w = Math.sqrt(G / L), Lp = 175, px = 250, py = 28;
    const per = (2 * Math.PI) / w;
    return {
      D: per * 2, hold: 0,
      draw(c, t, rev) {
        const th = th0 * Math.cos(w * t);
        const bx = px + Lp * Math.sin(th), by = py + Lp * Math.cos(th);
        c.strokeStyle = C.faint; c.lineWidth = 2; c.setLineDash([4, 6]);
        c.beginPath(); c.arc(px, py, Lp, Math.PI / 2 - th0, Math.PI / 2 + th0); c.stroke();
        c.beginPath(); c.moveTo(px, py); c.lineTo(px, py + Lp + 20); c.stroke();
        const topY = py + Lp * Math.cos(th0);
        c.strokeStyle = C.o; c.beginPath(); c.moveTo(px - Lp * Math.sin(th0) - 30, topY); c.lineTo(px + Lp * Math.sin(th0) + 30, topY); c.stroke();
        c.beginPath(); c.moveTo(px - 60, py + Lp); c.lineTo(px + 60, py + Lp); c.stroke(); c.setLineDash([]);
        txt(c, "h = " + f(h) + " m", px + Lp * Math.sin(th0) + 36, (topY + py + Lp) / 2 + 4, { c: C.o, s: 14, b: 1 });
        c.fillStyle = C.m; c.fillRect(px - 30, py - 6, 60, 6);
        c.strokeStyle = C.m; c.lineWidth = 2; c.beginPath(); c.moveTo(px, py); c.lineTo(bx, by); c.stroke();
        ball(c, bx, by, 15, C.y);
        const Uh = L * (1 - Math.cos(th)), v = Math.sqrt(Math.max(0, 2 * G * (h - Uh)));
        const dir = -Math.sin(w * t) >= 0 ? 1 : -1;
        if (v > 0.15) arrow(c, bx, by, bx + Math.cos(th) * v * 18 * dir, by - Math.sin(th) * v * 18 * dir, C.b, "", { w: 2.5 });
        bars(c, 500, 225, [{ l: "Ug", v: Uh, c: C.b }, { l: "K", v: h - Uh, c: C.y }], h, 150, "Energy");
        if (rev) txt(c, "v = " + f(v, 1) + " m/s", 620, 120, { c: C.y, s: 15, b: 1 });
        else txt(c, "v at bottom = ?", 600, 120, { c: C.y, s: 15, b: 1 });
        txt(c, "Tension ⟂ motion: no work", 24, 262, { c: C.m, s: 12 });
      }
    };
  };

  // box pulled across the floor by a rope at an angle, with a separate free-body diagram
  SIMS.pull = p => {
    const a = (p.ang * Math.PI) / 180, F = p.F, mg = p.m ? p.m * G : null;
    const N = mg !== null ? mg - F * Math.sin(a) : null;
    const big = Math.max(F, mg || 0), s = 82 / big;
    return {
      D: 3.5, hold: 1,
      draw(c, t, rev) {
        const gy = 200; ground(c, gy, 16, 300);
        const x = 30 + 110 * ease(clamp(t / 3.5, 0, 1)), bw = 70, bh = 48;
        c.strokeStyle = C.m; c.lineWidth = 2; c.beginPath(); c.moveTo(x + bw, gy - bh / 2); c.lineTo(x + bw + 110 * Math.cos(a), gy - bh / 2 - 110 * Math.sin(a)); c.stroke();
        c.fillStyle = C.m; c.beginPath(); c.arc(x + bw + 110 * Math.cos(a), gy - bh / 2 - 110 * Math.sin(a), 5, 0, 7); c.fill();
        thing(c, p.obj || "box", x, gy, bw, bh, C.y, p.m ? f(p.m) + " kg" : "");
        arrow(c, x + 6, gy + 26, x + 56, gy + 26, C.w, "motion", { w: 2, ly: 4 });
        // free-body diagram
        const cx = 410, cy = 140;
        txt(c, "Free-body diagram", cx, 24, { c: C.m, s: 12, b: 1, a: "center" });
        c.fillStyle = C.y; c.beginPath(); c.arc(cx, cy, 6, 0, 7); c.fill();
        const sF = Math.max(s, 80 / F), fx = cx + F * sF * Math.cos(a), fy = cy - F * sF * Math.sin(a);
        if (sF > s * 1.05) txt(c, "(F drawn larger than scale)", cx, 262, { c: C.m, s: 11, a: "center" });
        arrow(c, cx, cy, fx, fy, C.y, "F = " + f(F) + " N", { lx: 10, ly: -8 });
        arrow(c, cx, cy, fx, cy, C.g, "F cos θ", { dash: 1, w: 2, ly: 20, lx: -30 });
        arrow(c, fx, cy, fx, fy, C.o, "F sin θ", { dash: 1, w: 2, lx: 8, ly: 10 + (cy - fy) / 2 });
        c.strokeStyle = C.y; c.lineWidth = 1.5; c.beginPath(); c.arc(cx, cy, 26, -a, 0); c.stroke();
        txt(c, f(p.ang) + "°", cx + 30, cy - 6, { c: C.y, s: 12, b: 1 });
        if (mg !== null) {
          arrow(c, cx, cy, cx, cy + mg * s, C.r, "mg = " + f(mg) + " N", { la: "right", lx: -10, ly: 0 });
          arrow(c, cx - 4, cy, cx - 4, cy - N * s, C.b, rev ? "N = " + f(N) + " N" : "N = ?", { la: "right", lx: -8, ly: 8 });
        }
        const lines = ["F = " + f(F) + " N at " + f(p.ang) + "°"];
        if (p.m) lines.push("m = " + f(p.m) + " kg");
        if (p.d) { lines.push("d = " + f(p.d) + " m"); lines.push(["W = Fd cos θ", false]); lines.push(["W = " + f(F * p.d * Math.cos(a)) + " J", true]); }
        if (mg !== null) { lines.push("N = mg − F sin θ"); lines.push(["N = " + f(N) + " N", true]); }
        panel(c, lines, 545, 50, rev);
      }
    };
  };

  // box sliding to a stop under friction
  SIMS.slide = p => ({
    D: 3, hold: 1,
    draw(c, t, rev) {
      const gy = 210; ground(c, gy, 16, 470);
      const s = clamp(t / 3, 0, 1), x = 40 + 300 * (1 - (1 - s) ** 2), v = 1 - s;
      box(c, x, gy - 50, 70, 50, C.y, "");
      if (v > 0.02) {
        arrow(c, x + 35, gy - 74, x + 35 + 70 * v + 8, gy - 74, C.b, "v", { w: 2.5 });
        arrow(c, x, gy - 8, x - 50, gy - 8, C.r, "f", { w: 3, la: "right", lx: -6 });
      }
      bars(c, 520, 210, [{ l: "K", v: v * v, c: C.y }, { l: "Eth", v: 1 - v * v, c: C.r }], 1, 140, "Energy");
      panel(c, ["Friction opposite motion (θ = 180°)", ["W_friction = −f·d (negative)", true]], 24, 34, rev);
    }
  });

  // carrying a box horizontally: gravity does no work
  SIMS.carry = p => ({
    D: 3.5, hold: 0.6,
    draw(c, t, rev) {
      const gy = 236; ground(c, gy);
      const x = 70 + 340 * (t / 3.5);
      c.strokeStyle = C.m; c.lineWidth = 4; c.lineCap = "round";
      const step = Math.sin(t * 9) * 12;
      c.beginPath(); c.moveTo(x, gy - 60); c.lineTo(x - 10 + step, gy); c.moveTo(x, gy - 60); c.lineTo(x + 10 - step, gy);
      c.moveTo(x, gy - 60); c.lineTo(x, gy - 120); c.moveTo(x, gy - 108); c.lineTo(x + 34, gy - 94); c.stroke();
      c.fillStyle = C.m; c.beginPath(); c.arc(x, gy - 134, 13, 0, 7); c.fill();
      box(c, x + 22, gy - 118, 54, 40, C.y, "");
      arrow(c, x + 49, gy - 78, x + 49, gy - 30, C.r, "mg", { lx: 8, ly: 4 });
      arrow(c, x + 49, gy - 140, x + 109, gy - 140, C.b, "motion", { ly: 4, lx: 8 });
      c.strokeStyle = C.y; c.lineWidth = 1.5; c.strokeRect(x + 49, gy - 140, 12, 12);
      panel(c, ["Angle between mg and motion: 90°", ["W_gravity = mg·d·cos 90° = 0", true]], 470, 40, rev);
    }
  });

  /* roller coaster on a custom track
     pts: [[x, y, "label"?], ...] in meters (ground at y = 0); smooth hills/valleys between points
     loop: {at: index, R: radius, l: "T"}  (vertical loop starting at that valley point)
     v0: start speed · lift: index the chain lift pulls to at constant speed (p.vl m/s)
     vAt: ["B", speed] to set friction so the car has that speed at B · ask: label whose speed is unknown
     lines: extra readout lines [[text, isAnswer], ...] · obj: "coaster" (default), "ball", "skater", "cart" */
  SIMS.rollercoaster = p => {
    const P = [], marks = [];
    const add = (x, y) => P.push([x, y]);
    const pts = p.pts;
    for (let i = 0; i < pts.length; i++) {
      const [x0, y0, l0] = pts[i];
      if (i === 0) add(x0, y0);
      if (l0) marks.push({ l: l0, i: P.length - 1 });
      if (p.loop && p.loop.at === i) {
        const R = p.loop.R, cx = x0, cy = y0 + R;
        for (let k = 1; k <= 120; k++) { const a = -Math.PI / 2 + (k / 120) * Math.PI * 2; add(cx + R * Math.cos(a), cy + R * Math.sin(a)); if (k === 60) marks.push({ l: p.loop.l || "T", i: P.length - 1, top: 1 }); }
      }
      if (i < pts.length - 1) {
        const [x1, y1] = pts[i + 1], n = Math.max(12, Math.round(Math.abs(x1 - x0) * 1.5));
        for (let k = 1; k <= n; k++) { const u = k / n; add(x0 + (x1 - x0) * u, y0 + (y1 - y0) * (1 - Math.cos(Math.PI * u)) / 2); }
      }
    }
    const S = [0]; for (let i = 1; i < P.length; i++) S.push(S[i - 1] + Math.hypot(P[i][0] - P[i - 1][0], P[i][1] - P[i - 1][1]));
    const sT = S[S.length - 1];
    const idxAt = s => { let lo = 0, hi = S.length - 1; while (hi - lo > 1) { const m = (lo + hi) >> 1; if (S[m] <= s) lo = m; else hi = m; } return lo; };
    const yAt = s => { const i = idxAt(s), j = Math.min(i + 1, P.length - 1), u = S[j] > S[i] ? (s - S[i]) / (S[j] - S[i]) : 0; return P[i][1] + (P[j][1] - P[i][1]) * u; };
    const xyAt = s => { const i = idxAt(s), j = Math.min(i + 1, P.length - 1), u = S[j] > S[i] ? (s - S[i]) / (S[j] - S[i]) : 0; return [P[i][0] + (P[j][0] - P[i][0]) * u, P[i][1] + (P[j][1] - P[i][1]) * u, i]; };
    const mk = l => marks.find(m => m.l === l);
    // energy per unit mass
    const sLift = p.lift !== undefined ? S[marks.find(m => m.l === p.lift).i] : 0;
    const vl = p.vl || 2;
    const yS = p.lift !== undefined ? yAt(sLift) : P[0][1];
    const v0 = p.lift !== undefined ? vl : p.v0 || 0;
    let af = 0;
    if (p.vAt) { const m = mk(p.vAt[0]), sB = S[m.i]; af = (0.5 * v0 * v0 + G * (yS - P[m.i][1]) - 0.5 * p.vAt[1] ** 2) / (sB - sLift); }
    const eAt = s => s < sLift ? 0.5 * vl * vl : 0.5 * v0 * v0 + G * (yS - yAt(s)) - af * (s - sLift);
    const vAt = s => Math.sqrt(Math.max(0, 2 * eAt(s)));
    // motion
    let s0 = 0;
    if (p.lift === undefined && !(p.v0 > 0) && marks.length && Math.abs(P[marks[0].i][1] - P[0][1]) < 1e-6) s0 = S[marks[0].i];
    const frames = []; let s = s0, dir = 1, tt = 0, stopped = false;
    while (tt < 60 && frames.length < 6000) {
      frames.push([s, tt]);
      if (s < sLift) { s += vl * 0.02; tt += 0.02; continue; }
      const v = vAt(s), ve = Math.max(v, 1.6);
      const ns = s + dir * ve * 0.02;
      if (eAt(ns) <= 0) { if (af > 0 || p.stopAtRest) { stopped = true; break; } dir = -dir; }
      else s = ns;
      tt += 0.02;
      if (s >= sT || s <= 0) break;
    }
    const T = tt, D = clamp(T, 4, 7), spedUp = T / D > 1.3;
    // layout
    const xs = P.map(q => q[0]), ys = P.map(q => q[1]);
    const xmin = Math.min(...xs), xmax = Math.max(...xs), ymax = Math.max(...ys, 1);
    const sc = Math.min(540 / (xmax - xmin), 150 / ymax), ox = 24 + (540 - (xmax - xmin) * sc) / 2, gyc = 236;
    const X = x => ox + (x - xmin) * sc, Y = y => gyc - y * sc;
    const E0 = 0.5 * v0 * v0 + G * yS;
    const Emax = Math.max(E0, G * ymax + 0.5 * vl * vl);
    return {
      D, hold: 1.2,
      draw(c, t, rev) {
        // ground and supports
        c.strokeStyle = C.line; c.lineWidth = 2; c.beginPath(); c.moveTo(16, gyc); c.lineTo(574, gyc); c.stroke();
        c.strokeStyle = C.faint; c.lineWidth = 1.5;
        const loopStart = p.loop ? marks.find(m => m.top).i - 60 : -1;
        for (let i = 0; i < P.length; i += 6) { if (p.loop && i > loopStart && i < loopStart + 120) continue; c.beginPath(); c.moveTo(X(P[i][0]), Y(P[i][1])); c.lineTo(X(P[i][0]), gyc); c.stroke(); }
        // track
        c.strokeStyle = C.m; c.lineWidth = 4; c.lineJoin = "round"; c.beginPath();
        P.forEach(([x, y], i) => (i ? c.lineTo(X(x), Y(y)) : c.moveTo(X(x), Y(y)))); c.stroke();
        c.strokeStyle = "rgba(5,8,22,.8)"; c.lineWidth = 1.5; c.setLineDash([2, 7]); c.stroke(); c.setLineDash([]);
        if (p.lift !== undefined) { c.strokeStyle = C.o; c.lineWidth = 2; c.setLineDash([3, 4]); c.beginPath(); for (let i = 0; i <= mk(p.lift).i; i++) (i ? c.lineTo : c.moveTo).call(c, X(P[i][0]) - 3, Y(P[i][1]) + 4); c.stroke(); c.setLineDash([]); }
        // marks
        marks.forEach(m => {
          const [x, y] = P[m.i]; c.fillStyle = C.y; c.beginPath(); c.arc(X(x), Y(y), 4, 0, 7); c.fill();
          const ly = m.top ? Y(y) - 12 : Y(y) + (y > ymax * 0.5 || m.i === 0 ? -14 : 20);
          txt(c, m.l + " · " + f(y) + " m", X(x), ly, { c: C.y, s: 12, b: 1, a: "center" });
        });
        // car
        const tr = (t / D) * T; let k = frames.findIndex(q => q[1] >= tr); if (k < 0) k = frames.length - 1;
        const sc_ = frames[k][0], [cx, cy] = xyAt(sc_), [ax, ay] = xyAt(Math.min(sT, sc_ + 0.5)), [bx, by] = xyAt(Math.max(0, sc_ - 0.5));
        let tx = ax - bx, ty = ay - by; const tl = Math.hypot(tx, ty) || 1; tx /= tl; ty /= tl;
        const nx = -ty, ny = tx; // left normal (math coords): the side the car rides on
        const ang = Math.atan2(-ty, tx);
        c.save(); c.translate(X(cx) + nx * 2, Y(cy) - ny * 2); c.rotate(ang);
        const kind = p.obj || "coaster";
        if (kind === "ball") ball(c, 0, -11, 11, C.y);
        else if (kind === "skater") figure(c, 0, 0, 40, C.y, true);
        else thing(c, kind, -19, 0, 38, 26, C.y, "");
        c.restore();
        // speed readout
        const v = sc_ < sLift ? vl : vAt(sc_);
        if (rev || !p.ask) txt(c, "v = " + f(v, 1) + " m/s", X(cx), Y(cy) - (ny >= 0 ? 34 : -40), { c: C.w, s: 13, b: 1, a: "center" });
        // bars
        const U = G * cy, K = 0.5 * v * v, Eth = Math.max(0, af * (sc_ - sLift));
        const items = [{ l: "Ug", v: U, c: C.b }, { l: "K", v: K, c: C.y }];
        if (af > 0) items.push({ l: "Eth", v: Eth, c: C.r });
        bars(c, 596, 236, items, Emax, 110, p.lift !== undefined ? "Energy (per kg)" : "Energy");
        const lines = [];
        if (p.ask) { const m = mk(p.ask); lines.push(["v at " + p.ask + " = " + f(vAt(S[m.i]), 1) + " m/s", true]); }
        (p.lines || []).forEach(l => lines.push(l));
        panel(c, lines, 586, 30, rev);
        const title = p.title || (p.lift !== undefined ? "Chain lift, then frictionless" : af > 0 ? (p.vAt && p.vAt[1] === 0 ? "Brakes / friction" : "With friction") : "Frictionless track");
        txt(c, title + (spedUp ? " · sped up" : ""), 20, 258, { c: C.m, s: 12, b: 1 });
        if (stopped && t >= D) txt(c, "stopped", X(cx), Y(cy) - 34, { c: C.m, s: 12, a: "center" });
      }
    };
  };
  // simple drop (kept for older pages)
  SIMS.coaster = p => SIMS.rollercoaster(Object.assign({ pts: [[0, p.h], [6, p.h, "A"], [30, 0, "B"], [46, 0]], ask: p.reveal ? undefined : "B" }, p));

  // spring launcher
  SIMS.spring = p => {
    const Us = 0.5 * p.k * p.x * p.x, v = Math.sqrt((2 * Us) / p.m);
    return {
      D: 3.4, hold: 0.8,
      draw(c, t, rev) {
        const gy = 210; ground(c, gy, 40);
        c.fillStyle = C.m; c.fillRect(30, gy - 90, 12, 90);
        const rel = 0.9, ext = 0.35;
        let sx, bx;
        const comp = 70, nat = 150;
        if (t < rel) { sx = comp; bx = 42 + comp + 16; }
        else if (t < rel + ext) { const s = (t - rel) / ext; sx = comp + (nat - comp) * Math.sin((s * Math.PI) / 2); bx = 42 + sx + 16; }
        else { sx = nat; bx = Math.min(400, 42 + nat + 16 + (t - rel - ext) * 210); }
        // zigzag spring
        c.strokeStyle = C.o; c.lineWidth = 2.5; c.beginPath(); c.moveTo(42, gy - 20);
        const n = 12; for (let i = 1; i <= n; i++) c.lineTo(42 + (sx * i) / n, gy - 20 + (i === n ? 0 : i % 2 ? -12 : 12)); c.stroke();
        c.fillStyle = C.o; c.fillRect(42 + sx - 3, gy - 36, 6, 32);
        ball(c, Math.min(bx, 680), gy - 18, 16, C.y);
        if (t >= rel + ext && bx < 400) arrow(c, bx, gy - 52, bx + 50, gy - 52, C.b, "v", { w: 2.5 });
        const k = t < rel ? 0 : t < rel + ext ? Math.sin((((t - rel) / ext) * Math.PI) / 2) ** 2 : 1;
        bars(c, 455, 210, [{ l: "Us", v: Us * (1 - k), c: C.o }, { l: "K", v: Us * k, c: C.y }], Us, 120, "Energy");
        panel(c, ["k = " + f(p.k) + " N/m", "x = " + f(p.x) + " m", ["Us = ½kx² = " + f(Us) + " J", true], ...(p.m ? [["v = " + f(v, 1) + " m/s", true]] : [])], 560, 70, rev);
      }
    };
  };

  // climbing stairs: power
  SIMS.stairs = p => ({
    D: 4, hold: 1,
    draw(c, t, rev) {
      const n = 5, sw = 60, sh = 30, x0 = 90, y0 = 230;
      c.fillStyle = "rgba(124,196,255,.18)"; c.strokeStyle = C.m; c.lineWidth = 2;
      c.beginPath(); c.moveTo(x0, y0);
      for (let i = 0; i < n; i++) { c.lineTo(x0 + i * sw, y0 - (i + 1) * sh); c.lineTo(x0 + (i + 1) * sw, y0 - (i + 1) * sh); }
      c.lineTo(x0 + n * sw, y0); c.closePath(); c.fill(); c.stroke();
      const s = clamp(t / 4, 0, 1), pos = s * n, i = Math.min(n - 1, Math.floor(pos)), fr = pos - Math.floor(pos);
      const hop = s >= 1 ? 0 : Math.sin(fr * Math.PI) * 14;
      const bx = x0 - 20 + pos * sw, by = y0 - (s >= 1 ? n : Math.floor(pos) + (fr > 0.5 ? 1 : 0)) * sh - 18 - hop;
      if (p.obj === "ball") ball(c, bx + 20, by, 14, C.y);
      else figure(c, bx + 20, by + 18 + hop * 0, 58, C.y, false, s >= 1 ? 0 : Math.sin(fr * Math.PI * 2) * 4);
      txt(c, "clock: " + f(s * p.t, 1) + " s", 470, 50, { c: C.w, s: 15, b: 1 });
      txt(c, "(animation sped up)", 470, 70, { c: C.m, s: 12 });
      panel(c, ["weight = " + f(p.w) + " N", "height = " + f(p.h) + " m", "time = " + f(p.t) + " s", ["W = mgh = " + f(p.w * p.h) + " J", true], ["P = W/t = " + f((p.w * p.h) / p.t) + " W", true]], 470, 110, rev);
    }
  });

  // area under a force graph (kind "x" = work, kind "t" = impulse)
  SIMS.graph = p => {
    const pts = p.pts, X = pts[pts.length - 1][0], Fm = Math.max(...pts.map(q => q[1]));
    const gx = 60, gy = 210, gw = 330, gh = 150;
    const Fat = u => { for (let i = 1; i < pts.length; i++) if (u <= pts[i][0]) { const [a, fa] = pts[i - 1], [b, fb] = pts[i]; return fa + ((fb - fa) * (u - a)) / (b - a || 1); } return 0; };
    const area = u => { let A = 0, du = X / 400; for (let s = 0; s < u; s += du) A += Fat(s + du / 2) * Math.min(du, u - s); return A; };
    const total = area(X), isT = p.kind === "t";
    return {
      D: 4, hold: 1.2,
      draw(c, t, rev) {
        const u = X * clamp(t / 4, 0, 1);
        c.strokeStyle = C.line; c.lineWidth = 2;
        c.beginPath(); c.moveTo(gx, gy - gh - 10); c.lineTo(gx, gy); c.lineTo(gx + gw + 14, gy); c.stroke();
        txt(c, "F (N)", gx - 8, gy - gh - 18, { c: C.m, s: 12, b: 1 });
        txt(c, isT ? "t (s)" : "x (m)", gx + gw + 18, gy + 4, { c: C.m, s: 12, b: 1 });
        for (let k = 0; k <= X; k++) txt(c, String(k), gx + (k / X) * gw, gy + 18, { c: C.m, s: 11, a: "center" });
        txt(c, f(Fm), gx - 8, gy - gh + 4, { c: C.m, s: 11, a: "right" });
        const PX = q => gx + (q / X) * gw, PY = F => gy - (F / Fm) * gh;
        c.fillStyle = isT ? "rgba(124,196,255,.35)" : "rgba(255,200,87,.28)";
        c.beginPath(); c.moveTo(PX(0), gy);
        for (let q = 0; q <= u; q += X / 200) c.lineTo(PX(q), PY(Fat(q)));
        c.lineTo(PX(u), PY(Fat(u))); c.lineTo(PX(u), gy); c.closePath(); c.fill();
        c.strokeStyle = isT ? C.b : C.y; c.lineWidth = 3; c.beginPath();
        pts.forEach(([q, F], i) => (i ? c.lineTo(PX(q), PY(F)) : c.moveTo(PX(q), PY(F)))); c.stroke();
        c.strokeStyle = C.w; c.lineWidth = 1.5; c.setLineDash([3, 4]); c.beginPath(); c.moveTo(PX(u), gy); c.lineTo(PX(u), gy - gh - 6); c.stroke(); c.setLineDash([]);
        // object being pushed
        const A = area(u), oy = 230; ground(c, oy, 470, 704);
        let ox;
        if (isT && p.m) { const v0 = p.v0 || 0; let xpos = 0, du = X / 200; for (let s = 0; s < u; s += du) xpos += (v0 + area(s) / p.m) * du; const vmax = Math.abs(v0) + total / p.m; ox = 520 + (xpos / (vmax * X || 1)) * 120; }
        else ox = 520 + (u / X) * 120;
        const bx = clamp(ox, 520, 650);
        box(c, bx, oy - 40, 50, 40, isT ? C.b : C.y, p.m ? f(p.m) + " kg" : "");
        if (Fat(u) > 0.01) arrow(c, bx - 6 - (Fat(u) / Fm) * 34, oy - 20, bx - 4, oy - 20, C.o, "F", { w: 2.5, la: "right", lx: -2, ly: -8 });
        const name = isT ? "Impulse = Δp" : "Work";
        const unit = isT ? " kg·m/s" : " J";
        if (rev || u < X) txt(c, name + " so far: " + f(A, 1) + unit, 440, 40, { c: C.w, s: 14, b: 1 });
        if (!rev && u >= X) txt(c, name + " = area = ?", 440, 40, { c: C.y, s: 15, b: 1 });
        if (rev && u >= X) txt(c, name + " = " + f(total) + unit, 440, 64, { c: C.y, s: 15, b: 1 });
        if (rev && isT && p.m && u >= X) txt(c, "Δv = Δp/m = " + f(total / p.m) + " m/s", 440, 86, { c: C.y, s: 14, b: 1 });
        if (!rev && u < X) txt(c, "(final value hidden until you answer)", 440, 62, { c: C.m, s: 12 });
      }
    };
  };

  // two different masses dropped together
  SIMS.drop2 = p => {
    const h = p.h || 20, T = Math.sqrt((2 * h) / G);
    return {
      D: 2.2, hold: 1,
      draw(c, t, rev) {
        const s = clamp(t / 2.2, 0, 1), tr = s * T, y = 40 + (0.5 * G * tr * tr / h) * 170, v = G * tr;
        ground(c, 232, 60, 420);
        ball(c, 160, y, 12, C.y, ""); ball(c, 310, y - 10, 24, C.b, "");
        txt(c, f(p.m1) + " kg", 160, 30, { c: C.y, s: 13, b: 1, a: "center" });
        txt(c, f(p.m2) + " kg", 310, 30, { c: C.b, s: 13, b: 1, a: "center" });
        const vl = rev ? "v = " + f(v, 1) + " m/s" : "v = ?";
        txt(c, vl, 182, y + 4, { c: C.w, s: 13 }); txt(c, vl, 344, y - 6, { c: C.w, s: 13 });
        panel(c, ["Dropped together from " + f(h) + " m", "Mass cancels: v = √(2gh)", ["Same speed: v = " + f(Math.sqrt(2 * G * h), 1) + " m/s", true]], 450, 60, rev);
      }
    };
  };

  // falling ball: gravity changes momentum
  SIMS.fall = p => ({
    D: 2.4, hold: 0.8,
    draw(c, t, rev) {
      const s = clamp(t / 2.4, 0, 1), y = 40 + 170 * s * s, v = s;
      ground(c, 236, 140, 420);
      ball(c, 280, y, 16, C.y);
      arrow(c, 300, y, 300, y + 40, C.r, "Fg (external)", { lx: 8, ly: 6 });
      arrow(c, 256, y, 256, y + 10 + 80 * v, C.b, "p", { la: "right", lx: -6, ly: 4 });
      panel(c, ["System: ball only", "Gravity acts for time Δt", ["Conserved? = no, p increases", true]], 420, 60, rev);
    }
  });

  // 1D collisions: mode "stick", "elastic" or "given" (v1f/v2f supplied); "known" lists final values shown before answering
  SIMS.collide = p => {
    const m1 = p.m1, m2 = p.m2, v1 = p.v1, v2 = p.v2;
    let v1f = p.v1f, v2f = p.v2f;
    if (p.mode === "stick") v1f = v2f = (m1 * v1 + m2 * v2) / (m1 + m2);
    if (p.mode === "elastic") { v1f = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2); v2f = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2); }
    if (v1f === undefined) v1f = (m1 * v1 + m2 * v2 - m2 * v2f) / m1;
    if (v2f === undefined) v2f = (m1 * v1 + m2 * v2 - m1 * v1f) / m2;
    const known = p.known || [];
    const vmax = Math.max(Math.abs(v1), Math.abs(v2), Math.abs(v1f), Math.abs(v2f));
    const tc = 1.6, k = 150 / (vmax * tc), X = 360, mm = Math.max(m1, m2);
    const w1 = cartW(m1, mm), w2 = cartW(m2, mm);
    const P = m1 * v1 + m2 * v2;
    const lbl = (name, v, show) => name + " = " + (show ? fs(v) : "?") + " m/s";
    return {
      D: tc + 2, hold: 1,
      draw(c, t, rev) {
        const gy = 200; ground(c, gy);
        const dt = t - tc, after = dt > 0;
        const r1 = X + (after ? v1f : v1) * k * dt, l2 = X + (after ? v2f : v2) * k * dt;
        const x1 = r1 - w1, x2 = l2;
        thing(c, p.o1, x1, gy, w1, 40, C.y, f(m1) + " kg", (after ? v1f : v1) >= 0 ? 1 : -1);
        thing(c, p.o2, x2, gy, w2, 40, C.b, f(m2) + " kg", (after ? v2f : v2) > 0 ? 1 : -1);
        if (after && p.mode === "stick" && (!p.o1 || p.o1 === "cart")) { c.fillStyle = C.w; c.fillRect(r1 - 3, gy - 38, 6, 18); }
        flash(c, X, gy - 30, dt / 0.5);
        const va = after ? v1f : v1, vb = after ? v2f : v2;
        const ya = 112, yb = 112;
        const s1 = !after || known.includes("v1f") || rev, s2 = !after || known.includes("v2f") || rev;
        if (Math.abs(va) > 0.01) arrow(c, x1 + w1 / 2, ya, x1 + w1 / 2 + Math.sign(va) * (16 + 46 * Math.abs(va) / vmax), ya, C.y, "", { w: 2.5 });
        if (Math.abs(vb) > 0.01) arrow(c, x2 + w2 / 2, yb - 26, x2 + w2 / 2 + Math.sign(vb) * (16 + 46 * Math.abs(vb) / vmax), yb - 26, C.b, "", { w: 2.5 });
        txt(c, lbl(after ? "v₁′" : "v₁", va, s1), x1 + w1 / 2, ya - 12, { c: C.y, s: 13, b: 1, a: "center" });
        txt(c, lbl(after ? "v₂′" : "v₂", vb, s2), x2 + w2 / 2, yb - 38, { c: C.b, s: 13, b: 1, a: "center" });
        const tag = p.mode === "stick" ? "Perfectly inelastic (stick)" : p.mode === "elastic" ? "Elastic (bounce, K conserved)" : "Collision";
        txt(c, tag, 20, 26, { c: C.m, s: 13, b: 1 });
        txt(c, "+ direction →", W - 20, 26, { c: C.m, s: 12, a: "right" });
        txt(c, "Σp before = " + fs(P) + " kg·m/s", 20, 246, { c: C.w, s: 14 });
        if (after) txt(c, "Σp after = " + (rev ? fs(m1 * v1f + m2 * v2f) : "?") + " kg·m/s", W - 20, 246, { c: C.y, s: 14, b: 1, a: "right" });
      }
    };
  };

  // explosion / push-off from a shared velocity v0
  SIMS.explode = p => {
    const m1 = p.m1, m2 = p.m2, v0 = p.v0 || 0, M = m1 + m2;
    let v1f = p.v1f, v2f = p.v2f;
    if (v1f === undefined) v1f = (M * v0 - m2 * v2f) / m1;
    if (v2f === undefined) v2f = (M * v0 - m1 * v1f) / m2;
    const known = p.known || [];
    const vs = [v0, v1f, v2f].map(Math.abs), vmax = Math.max(...vs), vmin = Math.min(...vs.filter(v => v > 0.001));
    const skew = vmax / vmin > 8;
    const disp = v => (skew ? Math.sign(v) * 130 * Math.sqrt(Math.abs(v) / vmax) : (v / vmax) * 130);
    const ts = 1.3, mm = Math.max(m1, m2), w1 = cartW(m1, mm), w2 = cartW(m2, mm);
    const lbl = (n, v, s) => n + " = " + (s ? fs(v) : "?") + " m/s";
    return {
      D: ts + 2, hold: 1,
      draw(c, t, rev) {
        const gy = 200; ground(c, gy);
        const X0 = 360 - disp(v0) * ts;
        if (t < ts) {
          const X = X0 + disp(v0) * t;
          thing(c, p.o1, X - w1, gy, w1, 40, C.y, f(m1) + " kg", p.o1 === "rifle" ? 1 : v0 >= 0 ? 1 : -1);
          thing(c, p.o2, X, gy, w2, 40, C.b, f(m2) + " kg", 1);
          if (Math.abs(v0) > 0.001) { arrow(c, X, 112, X + Math.sign(v0) * 50, 112, C.w, "", { w: 2.5 }); txt(c, "v₀ = " + fs(v0) + " m/s", X, 98, { c: C.w, s: 13, b: 1, a: "center" }); }
          else txt(c, "at rest", X, 112, { c: C.m, s: 13, b: 1, a: "center" });
        } else {
          const dt = t - ts, X = 360;
          const a1 = X + disp(v1f) * dt, a2 = X + disp(v2f) * dt;
          thing(c, p.o1, a1 - w1, gy, w1, 40, C.y, f(m1) + " kg", p.o1 === "rifle" ? 1 : v1f >= 0 ? 1 : -1);
          thing(c, p.o2, a2, gy, w2, 40, C.b, f(m2) + " kg", v2f >= 0 ? 1 : -1);
          flash(c, X, gy - 30, dt / 0.5);
          const s1 = known.includes("v1f") || rev, s2 = known.includes("v2f") || rev;
          arrow(c, a1 - w1 / 2, 112, a1 - w1 / 2 + Math.sign(v1f) * 46, 112, C.y, "", { w: 2.5 });
          arrow(c, a2 + w2 / 2, 86, a2 + w2 / 2 + Math.sign(v2f) * 46, 86, C.b, "", { w: 2.5 });
          txt(c, lbl("v₁′", v1f, s1), a1 - w1 / 2, 100, { c: C.y, s: 13, b: 1, a: "center" });
          txt(c, lbl("v₂′", v2f, s2), a2 + w2 / 2, 74, { c: C.b, s: 13, b: 1, a: "center" });
        }
        txt(c, "Push apart / explosion: Σp stays " + fs(M * v0) + " kg·m/s", 20, 26, { c: C.m, s: 13, b: 1 });
        if (skew) txt(c, "(speeds not to scale)", W - 20, 26, { c: C.m, s: 12, a: "right" });
        txt(c, "+ direction →", W - 20, 246, { c: C.m, s: 12, a: "right" });
      }
    };
  };

  // ball bounces off a wall: momentum change and force
  SIMS.bounce = p => {
    const dp = p.m * (p.vf - p.v);
    return {
      D: 3, hold: 1.2,
      draw(c, t, rev) {
        const wx = 470, gy = 200; ground(c, gy, 16, wx);
        c.fillStyle = C.m; c.fillRect(wx, 60, 16, gy - 60);
        const tc = 1.3, sp = 230 / tc;
        let x, sq = 0;
        if (t < tc) x = wx - 20 - sp * (tc - t);
        else if (t < tc + 0.15) { x = wx - 20; sq = Math.sin(((t - tc) / 0.15) * Math.PI) * 6; }
        else x = wx - 20 - sp * (t - tc - 0.15) * Math.abs(p.vf / p.v);
        c.save(); c.translate(x, gy - 20); c.scale(1 - sq / 20, 1 + sq / 20); ball(c, 0, 0, 20, C.y); c.restore();
        const before = t < tc;
        txt(c, before ? "v = " + fs(p.v) + " m/s" : "v′ = " + fs(p.vf) + " m/s", x, gy - 54, { c: C.y, s: 13, b: 1, a: "center" });
        arrow(c, x, gy - 44, x + (before ? 48 : -48), gy - 44, C.y, "", { w: 2.5 });
        if (t >= tc + 0.15) {
          txt(c, "Δp = m(v′ − v)", 20, 40, { c: C.w, s: 15, b: 1 });
          txt(c, rev ? "= " + f(p.m) + "(" + fs(p.vf) + " − " + fs(p.v) + ") = " + fs(dp) + " kg·m/s" : "= ?", 20, 62, { c: C.y, s: 15, b: 1 });
          if (p.dt) txt(c, rev ? "F = Δp/Δt = " + fs(dp / p.dt) + " N" : "F = Δp/Δt = ?", 20, 86, { c: C.y, s: 15, b: 1 });
        } else txt(c, "m = " + f(p.m) + " kg" + (p.dt ? ",  contact Δt = " + f(p.dt) + " s" : ""), 20, 40, { c: C.w, s: 15 });
        // momentum vectors
        const sc = 48 / Math.max(Math.abs(p.m * p.v), Math.abs(p.m * p.vf)), ox = 610;
        txt(c, "Momentum", 520, 60, { c: C.m, s: 12, b: 1 });
        const vec = (val, y, col, lab) => { if (val >= 0) arrow(c, ox, y, ox + val * sc, y, col, lab, { w: 3 }); else arrow(c, ox + 50, y, ox + 50 + val * sc, y, col, lab, { w: 3, la: "right", lx: -6 }); };
        vec(p.m * p.v, 90, C.b, "p");
        if (!before) vec(p.m * p.vf, 128, C.y, "p′");
        if (!before && rev) vec(dp, 166, C.r, "Δp");
        txt(c, "Bounce: |Δv| = v + v′", 520, 222, { c: C.m, s: 12 });
      }
    };
  };

  // egg hitting a wall vs a soft sheet: same impulse, different force
  SIMS.egg = p => ({
    D: 3.4, hold: 1.2,
    draw(c, t, rev) {
      const lanes = [{ y: 105, stop: 0.08, col: C.r, lab: "Wall: short Δt → big F" }, { y: 225, stop: 0.7, col: C.g, lab: "Sheet: long Δt → small F" }];
      const tc = 1.2;
      lanes.forEach((L, i) => {
        ground(c, L.y, 16, 330);
        const wx = 300;
        if (i === 0) { c.fillStyle = C.m; c.fillRect(wx, L.y - 70, 14, 70); }
        let x, def = 0;
        if (t < tc) x = 50 + (wx - 70) * (t / tc);
        else { const s = clamp((t - tc) / L.stop, 0, 1); def = i ? 40 * Math.sin((s * Math.PI) / 2) : 0; x = 50 + (wx - 70) + (i ? def : 0); }
        if (i === 1) { c.strokeStyle = C.g; c.lineWidth = 3; c.beginPath(); c.moveTo(wx, L.y - 70); c.quadraticCurveTo(wx + def * 1.6, L.y - 35, wx, L.y); c.stroke(); }
        c.save(); c.fillStyle = "#EEF3FF"; c.shadowColor = "#EEF3FF"; c.shadowBlur = 8; c.beginPath(); c.ellipse(x + 20, L.y - 22, 22, 17, 0, 0, 7); c.fill(); c.restore();
        if (i === 0 && t > tc) { c.strokeStyle = C.r; c.lineWidth = 2; c.beginPath(); c.moveTo(x + 30, L.y - 38); c.lineTo(x + 22, L.y - 26); c.lineTo(x + 32, L.y - 18); c.lineTo(x + 24, L.y - 8); c.stroke(); }
        txt(c, L.lab, 20, L.y - 82, { c: L.col, s: 13, b: 1 });
        // mini F-t graph
        const gx = 400, gw = 280, gh = 70, base = L.y - 6;
        c.strokeStyle = C.line; c.lineWidth = 1.5; c.beginPath(); c.moveTo(gx, base - gh - 6); c.lineTo(gx, base); c.lineTo(gx + gw, base); c.stroke();
        txt(c, "F", gx - 12, base - gh, { c: C.m, s: 11 }); txt(c, "t", gx + gw + 6, base + 4, { c: C.m, s: 11 });
        const tt = clamp((t - tc) / 1.0, 0, 1), dur = i ? 0.8 : 0.1, peak = i ? gh * 0.15 : gh;
        const start = gx + 30, width = dur * 220;
        c.fillStyle = i ? "rgba(91,227,164,.35)" : "rgba(255,107,107,.35)"; c.strokeStyle = L.col; c.lineWidth = 2;
        c.beginPath(); c.moveTo(start, base);
        for (let s = 0; s <= tt; s += 0.01) { const u = s / 1; c.lineTo(start + u * width, base - peak * Math.sin(Math.PI * clamp(u, 0, 1))); }
        c.lineTo(start + tt * width, base); c.closePath(); c.fill(); c.stroke();
      });
      txt(c, rev ? "Same Δp = same area. Longer Δt means smaller F." : "Which one feels the smaller force?", 540, 262, { c: C.y, s: 14, b: 1, a: "center" });
    }
  });

  /* ===== Unit 1 and Unit 2 animation types ===== */
  const D2R = Math.PI / 180;
  function axes(c, x, y, w, h, xl, yl) {
    c.strokeStyle = C.line; c.lineWidth = 1.5;
    c.beginPath(); c.moveTo(x, y - h); c.lineTo(x, y); c.lineTo(x + w, y); c.stroke();
    txt(c, yl, x - 4, y - h - 6, { c: C.m, s: 11, b: 1 });
    txt(c, xl, x + w + 4, y + 4, { c: C.m, s: 11, b: 1 });
  }
  function grid(c, x0, y0, x1, y1, step) {
    c.strokeStyle = "rgba(255,255,255,.05)"; c.lineWidth = 1;
    for (let x = x0; x <= x1; x += step) { c.beginPath(); c.moveTo(x, y0); c.lineTo(x, y1); c.stroke(); }
    for (let y = y0; y <= y1; y += step) { c.beginPath(); c.moveTo(x0, y); c.lineTo(x1, y); c.stroke(); }
  }
  const hideOr = (rev, ask, key, s) => (!rev && ask && ask.includes(key) ? s.split("=")[0] + "= ?" : s);

  // 1-D motion with constant acceleration, plus live x-t and v-t graphs
  SIMS.motion = p => {
    const x0 = p.x0 || 0, v0 = p.v0 || 0, a = p.a || 0, T = p.T || 4;
    const X = t => x0 + v0 * t + 0.5 * a * t * t, V = t => v0 + a * t;
    let xs = [X(0), X(T)]; if (a !== 0) { const tt = -v0 / a; if (tt > 0 && tt < T) xs.push(X(tt)); }
    const xmin = Math.min(...xs, 0), xmax = Math.max(...xs, 1);
    const vs = [V(0), V(T), 0], vmin = Math.min(...vs), vmax = Math.max(...vs, 0.1);
    const sx = x => 40 + ((x - xmin) / (xmax - xmin || 1)) * 600;
    return {
      D: 4, hold: 1.2,
      draw(c, t, rev) {
        const tr = (t / 4) * T, ask = p.ask || [];
        // track
        c.strokeStyle = C.line; c.lineWidth = 2; c.beginPath(); c.moveTo(20, 92); c.lineTo(700, 92); c.stroke();
        for (let k = Math.ceil(xmin); k <= xmax; k += Math.max(1, Math.round((xmax - xmin) / 8))) {
          c.beginPath(); c.moveTo(sx(k), 88); c.lineTo(sx(k), 96); c.stroke();
          txt(c, String(k), sx(k), 110, { c: C.m, s: 10, a: "center" });
        }
        const px = sx(X(tr));
        thing(c, p.obj || "car", px - 32, 92, 64, 34, C.y, "", V(tr) >= 0 ? 1 : -1);
        if (Math.abs(V(tr)) > 0.05) arrow(c, px, 40, px + Math.sign(V(tr)) * (14 + 40 * Math.abs(V(tr)) / Math.max(Math.abs(vmax), Math.abs(vmin), 0.1)), 40, C.b, "v", { w: 2.5 });
        if (a !== 0) arrow(c, px, 26, px + Math.sign(a) * 30, 26, C.o, "a", { w: 2 });
        // graphs
        const gy = 248, gh = 90, gw = 270;
        [[46, "x (m)", X, xmin, xmax, C.y], [400, "v (m/s)", V, vmin, vmax, C.b]].forEach(([gx, yl, F, lo, hi, col]) => {
          axes(c, gx, gy, gw, gh, "t", yl);
          const Y = y => gy - ((y - lo) / (hi - lo || 1)) * gh;
          if (lo < 0) { c.strokeStyle = C.faint; c.beginPath(); c.moveTo(gx, Y(0)); c.lineTo(gx + gw, Y(0)); c.stroke(); }
          c.strokeStyle = col; c.lineWidth = 2.5; c.beginPath();
          for (let s = 0; s <= tr + 1e-9; s += T / 120) { const xx = gx + (s / T) * gw, yy = Y(F(s)); s ? c.lineTo(xx, yy) : c.moveTo(xx, yy); }
          c.stroke();
        });
        txt(c, "t = " + f(tr, 2) + " s", 20, 22, { c: C.w, s: 13, b: 1 });
        txt(c, hideOr(rev, ask, "x", "x = " + f(X(tr), 2) + " m"), 140, 22, { c: C.y, s: 13, b: 1 });
        txt(c, hideOr(rev, ask, "v", "v = " + f(V(tr), 2) + " m/s"), 270, 22, { c: C.b, s: 13, b: 1 });
        txt(c, "v₀ = " + f(v0) + " m/s   a = " + f(a) + " m/s²", 700, 22, { c: C.m, s: 12, a: "right" });
      }
    };
  };

  // projectile: launch speed v0 at angle ang (deg) from height h
  SIMS.projectile = p => {
    const v0 = p.v0, ang = (p.ang || 0) * D2R, h = p.h || 0, g = G;
    const vx = v0 * Math.cos(ang), vy = v0 * Math.sin(ang);
    const T = (vy + Math.sqrt(vy * vy + 2 * g * h)) / g, R = vx * T, Hm = h + (vy > 0 ? vy * vy / (2 * g) : 0);
    const sc = Math.min(R > 0.01 ? 560 / R : 1e9, 170 / Math.max(Hm, 0.5));
    const ox = R > 0.01 ? 70 : 360, oy = 236;
    const P = t => [ox + vx * t * sc, oy - (h + vy * t - 0.5 * g * t * t) * sc];
    return {
      D: Math.min(4.5, Math.max(2.5, T)), hold: 1.4,
      draw(c, t, rev) {
        const D = Math.min(4.5, Math.max(2.5, T)), tr = (t / D) * T, ask = p.ask || [];
        c.strokeStyle = C.line; c.lineWidth = 2; c.beginPath(); c.moveTo(16, oy); c.lineTo(704, oy); c.stroke();
        if (h > 0) { c.fillStyle = "rgba(163,176,208,.18)"; c.fillRect(ox - 60, oy - h * sc, 60, h * sc); c.strokeStyle = C.m; c.strokeRect(ox - 60, oy - h * sc, 60, h * sc); txt(c, "h = " + f(h) + " m", ox - 30, oy - h * sc / 2, { c: C.m, s: 12, a: "center" }); }
        c.setLineDash([3, 6]); c.strokeStyle = C.faint; c.lineWidth = 2; c.beginPath();
        for (let s = 0; s <= T; s += T / 80) { const [x, y] = P(s); s ? c.lineTo(x, y) : c.moveTo(x, y); } c.stroke(); c.setLineDash([]);
        c.strokeStyle = C.y; c.lineWidth = 2.5; c.beginPath();
        for (let s = 0; s <= tr; s += T / 80) { const [x, y] = P(s); s ? c.lineTo(x, y) : c.moveTo(x, y); } c.stroke();
        const [bx, by] = P(tr), vyt = vy - g * tr, k = 34 / v0;
        ball(c, bx, by - 8, 9, C.y);
        if (tr < T) {
          if (Math.abs(vx) > 0.01) arrow(c, bx, by - 8, bx + vx * k, by - 8, C.g, "vx", { w: 2, ly: 14 });
          if (Math.abs(vyt) > 0.05) arrow(c, bx, by - 8, bx, by - 8 - vyt * k, C.b, "vy", { w: 2, lx: 6 });
        }
        const lines = ["v₀ = " + f(v0) + " m/s at " + f(p.ang || 0) + "°"];
        if (h) lines.push("launch height " + f(h) + " m");
        lines.push(["time in air = " + f(T, 2) + " s", ask.includes("t")]);
        if (R > 0.01) lines.push(["range = " + f(R, 2) + " m", ask.includes("R")]);
        if (vy > 0) lines.push(["max height = " + f(Hm, 2) + " m", ask.includes("H")]);
        if (ask.includes("v")) lines.push(["impact speed = " + f(Math.hypot(vx, vy - g * T), 2) + " m/s", true]);
        panel(c, lines, 704, 26, rev, { a: "right" });
        txt(c, "vx stays " + f(vx, 2) + " m/s; vy changes by g each second", 20, 262, { c: C.m, s: 12 });
      }
    };
  };

  // boat crossing a river
  SIMS.river = p => {
    const vb = p.vb, vr = p.vr, w = p.w, T = w / vb, d = vr * T;
    const top = 72, bot = 236, scy = (bot - top) / w, scx = Math.min(scy, 420 / Math.max(d, 1));
    return {
      D: 4, hold: 1.2,
      draw(c, t, rev) {
        const s = clamp(t / 4, 0, 1), ask = p.ask || [];
        c.fillStyle = "rgba(124,196,255,.18)"; c.fillRect(16, top, 688, bot - top);
        c.strokeStyle = C.g; c.lineWidth = 3; [top, bot].forEach(y => { c.beginPath(); c.moveTo(16, y); c.lineTo(704, y); c.stroke(); });
        c.strokeStyle = "rgba(255,255,255,.18)"; c.lineWidth = 1.5;
        for (let i = 0; i < 14; i++) { const x = ((i * 60 + t * 50) % 700) + 10, y = top + 18 + (i % 4) * 40; c.beginPath(); c.moveTo(x, y); c.lineTo(x + 26, y); c.stroke(); }
        const x0 = 90, bx = x0 + d * s * scx, by = bot - (bot - top) * s;
        c.setLineDash([4, 5]); c.strokeStyle = C.faint; c.beginPath(); c.moveTo(x0, bot); c.lineTo(x0 + d * scx, top); c.stroke(); c.setLineDash([]);
        c.save(); c.translate(bx, by); c.fillStyle = C.y; c.beginPath(); c.moveTo(0, -16); c.lineTo(9, 8); c.lineTo(-9, 8); c.closePath(); c.fill(); c.restore();
        arrow(c, bx, by, bx, by - 40, C.y, "", { w: 2.5 });
        txt(c, "boat " + f(vb) + " m/s ↑", 20, 58, { c: C.y, s: 12, b: 1 });
        arrow(c, bx, by, bx + 40 * vr / vb, by, C.b, "", { w: 2.5 });
        arrow(c, bx, by, bx + 40 * vr / vb, by - 40, C.w, "", { w: 2, dash: 1 });
        txt(c, "river " + f(vr) + " m/s →", 150, 58, { c: C.b, s: 12, b: 1 });
        panel(c, ["width = " + f(w) + " m", ["crossing time = " + f(T, 2) + " s", ask.includes("t")], ["drift downstream = " + f(d, 2) + " m", ask.includes("d")], ["speed vs shore = " + f(Math.hypot(vb, vr), 2) + " m/s", ask.includes("v")]], 704, 22, rev, { a: "right" });
        
      }
    };
  };

  // vector components, or adding two vectors tip to tail
  SIMS.vector = p => {
    const sc = p.scale || 12;
    return {
      D: 3, hold: 1.5,
      draw(c, t, rev) {
        grid(c, 30, 20, 700, 250, 24);
        const ox = 120, oy = 220, s = ease(clamp(t / 1.4, 0, 1)), s2 = ease(clamp((t - 1.4) / 1.2, 0, 1));
        const comp = (m, a) => [m * Math.cos(a * D2R), m * Math.sin(a * D2R)];
        if (!p.B) {
          const [x, y] = comp(p.mag, p.ang);
          arrow(c, ox, oy, ox + x * sc * s, oy - y * sc * s, C.y, "", { w: 3 });
          if (s > 0.9) txt(c, f(p.mag) + " at " + f(p.ang) + "°", ox + x * sc / 2 - 10, oy - y * sc / 2 - 10, { c: C.y, s: 13, b: 1, a: "right" });
          if (s2 > 0) {
            arrow(c, ox, oy, ox + x * sc * s2, oy, C.g, "", { w: 2.5, dash: 1 });
            arrow(c, ox + x * sc, oy, ox + x * sc, oy - y * sc * s2, C.b, "", { w: 2.5, dash: 1 });
            if (s2 > 0.9) { txt(c, rev || !(p.ask || []).includes("x") ? "x = " + f(x, 2) : "x = ?", ox + x * sc / 2, oy + 18, { c: C.g, s: 13, b: 1, a: "center" }); txt(c, rev || !(p.ask || []).includes("y") ? "y = " + f(y, 2) : "y = ?", ox + x * sc + 8, oy - y * sc / 2, { c: C.b, s: 13, b: 1 }); }
          }
          panel(c, ["x = A cos θ", "y = A sin θ"], 700, 40, rev, { a: "right" });
        } else {
          const [ax, ay] = comp(...p.A), [bx, by] = comp(...p.B), rx = ax + bx, ry = ay + by;
          arrow(c, ox, oy, ox + ax * sc * s, oy - ay * sc * s, C.y, "A", { w: 3 });
          if (s > 0.95) arrow(c, ox + ax * sc, oy - ay * sc, ox + (ax + bx * s2) * sc, oy - (ay + by * s2) * sc, C.b, "B", { w: 3 });
          if (s2 > 0.95) arrow(c, ox, oy, ox + rx * sc, oy - ry * sc, C.w, "R", { w: 3, dash: 1 });
          const m = Math.hypot(rx, ry), a = Math.atan2(ry, rx) / D2R;
          panel(c, ["add x parts and y parts", "Rx = " + f(rx, 2) + "   Ry = " + f(ry, 2), ["|R| = " + f(m, 2), true], ["angle = " + f(a, 1) + "°", true]], 700, 40, rev, { a: "right" });
        }
      }
    };
  };

  // block on an incline (from rest)
  SIMS.incline = p => {
    const m = p.m || 1, th = p.ang * D2R, mus = p.mus ?? 0, muk = p.muk ?? 0;
    const N = m * G * Math.cos(th), down = m * G * Math.sin(th);
    const slides = down > mus * N + 1e-9, fr = slides ? muk * N : down, acc = slides ? (down - fr) / m : 0;
    const L = 470, x0 = 90, y0 = 236, topx = x0, topy = y0 - L * Math.sin(th);
    return {
      D: 3.5, hold: 1.2,
      draw(c, t, rev) {
        const ask = p.ask || [];
        c.fillStyle = "rgba(163,176,208,.15)"; c.beginPath(); c.moveTo(x0, y0); c.lineTo(x0 + L * Math.cos(th), y0); c.lineTo(topx, topy); c.closePath(); c.fill();
        c.strokeStyle = C.m; c.lineWidth = 2.5; c.beginPath(); c.moveTo(topx, topy); c.lineTo(x0 + L * Math.cos(th), y0); c.lineTo(x0, y0); c.stroke();
        txt(c, f(p.ang) + "°", x0 + L * Math.cos(th) - 46, y0 - 8, { c: C.y, s: 13, b: 1 });
        const s = slides ? clamp(0.12 + 0.8 * (t / 3.5) ** 2, 0, 0.92) : 0.25;
        const cx = topx + L * s * Math.cos(th), cy = topy + L * s * Math.sin(th);
        c.save(); c.translate(cx, cy); c.rotate(th); box(c, -26, -44, 52, 40, C.y, f(m) + " kg");
        const k = 70 / (m * G);
        arrow(c, 0, -24, 0, -24 - N * k, C.b, rev || !ask.includes("N") ? "N = " + f(N, 1) : "N = ?", { w: 2.5, lx: 6 });
        if (fr > 0.01) arrow(c, -26, -10, -26 - fr * k, -10, C.r, rev || !ask.includes("f") ? "f = " + f(fr, 1) : "f = ?", { w: 2.5, la: "right", lx: -4 });
        arrow(c, 0, -24, down * k, -24, C.o, "mg sin θ", { w: 2, dash: 1, ly: 16 });
        c.restore();
        arrow(c, cx, cy - 20, cx, cy - 20 + m * G * k, C.w, "mg", { w: 2.5, lx: 6, ly: 10 });
        panel(c, ["μs = " + f(mus) + "   μk = " + f(muk), slides ? "tan θ > μs: it slides" : "tan θ ≤ μs: it stays put", ["a = " + f(acc, 2) + " m/s²", ask.includes("a")]], 704, 30, rev, { a: "right" });
      }
    };
  };

  // pulleys: "atwood" (two hanging masses), "table" (block on table + hanging mass), "push2" (two blocks pushed)
  SIMS.pulley = p => {
    const m1 = p.m1, m2 = p.m2, mu = p.mu || 0, F = p.F || 0;
    let a, T;
    if (p.mode === "table") { a = Math.max(0, (m2 * G - mu * m1 * G) / (m1 + m2)); T = m2 * (G - a); }
    else if (p.mode === "push2") { a = Math.max(0, (F - mu * (m1 + m2) * G) / (m1 + m2)); T = m2 * a + mu * m2 * G; }
    else { a = (m2 - m1) * G / (m1 + m2); T = 2 * m1 * m2 * G / (m1 + m2); }
    return {
      D: 3, hold: 1.2,
      draw(c, t, rev) {
        const ask = p.ask || [], s = Math.min(1, (t / 3) ** 2) * Math.min(1, Math.abs(a) / 4 + 0.15), dirn = Math.sign(a);
        const Tl = rev || !ask.includes("T") ? (p.mode === "push2" ? "contact " : "T = ") + f(T, 1) + " N" : (p.mode === "push2" ? "contact = ?" : "T = ?");
        if (p.mode === "push2") {
          ground(c, 200, 16, 704);
          const x = 120 + 300 * s;
          box(c, x, 140, 90, 60, C.y, f(m1) + " kg"); box(c, x + 90, 150, 80, 50, C.b, f(m2) + " kg");
          arrow(c, x - 70, 170, x - 2, 170, C.w, "F = " + f(F) + " N", { la: "right", lx: -74, ly: -10 });
          arrow(c, x + 90, 128, x + 130, 128, C.g, Tl, { w: 2.5 });
        } else if (p.mode === "table") {
          c.fillStyle = "rgba(163,176,208,.18)"; c.fillRect(40, 120, 420, 14); c.fillRect(60, 134, 10, 110); c.fillRect(430, 134, 10, 110);
          const px = 470, py = 128; c.strokeStyle = C.m; c.lineWidth = 3; c.beginPath(); c.arc(px, py, 12, 0, 7); c.stroke();
          const d = 150 * s, bx = 140 + d, hy = 160 + d;
          box(c, bx, 76, 80, 44, C.y, f(m1) + " kg");
          c.strokeStyle = C.m; c.lineWidth = 2; c.beginPath(); c.moveTo(bx + 80, 98); c.lineTo(px, py - 12); c.moveTo(px + 12, py); c.lineTo(px + 12, hy); c.stroke();
          box(c, px - 14, hy, 52, 44, C.b, f(m2) + " kg");
          arrow(c, bx + 80, 70, bx + 120, 70, C.g, Tl, { w: 2 });
          arrow(c, px + 12, hy + 44, px + 12, hy + 90, C.r, "m₂g", { w: 2, lx: 6 });
        } else {
          const px = 360, py = 40; c.strokeStyle = C.m; c.lineWidth = 3; c.beginPath(); c.arc(px, py, 26, 0, 7); c.stroke();
          c.fillStyle = C.m; c.fillRect(px - 4, 6, 8, 10);
          const d = 60 * s * dirn, y1 = 150 - d, y2 = 150 + d;
          c.lineWidth = 2; c.beginPath(); c.moveTo(px - 26, py); c.lineTo(px - 26, y1); c.moveTo(px + 26, py); c.lineTo(px + 26, y2); c.stroke();
          box(c, px - 56, y1, 60, 46, C.y, f(m1) + " kg"); box(c, px - 4, y2, 60, 46, C.b, f(m2) + " kg");
          arrow(c, px - 26, y1, px - 26, y1 - 34, C.g, Tl, { w: 2, la: "right", lx: -8 });
        }
        panel(c, [p.mode === "push2" ? "F = " + f(F) + " N, μ = " + f(mu) : p.mode === "table" ? "μ on table = " + f(mu) : "m₁ = " + f(m1) + ", m₂ = " + f(m2), ["a = " + f(a, 2) + " m/s²", ask.includes("a")]], 704, 28, rev, { a: "right" });
      }
    };
  };

  // elevator: person standing on a scale, elevator accelerating (a up = +)
  SIMS.elevator = p => {
    const m = p.m, a = p.a, N = m * (G + a);
    return {
      D: 3, hold: 1.2,
      draw(c, t, rev) {
        const s = clamp(t / 3, 0, 1), y = 60 - Math.sign(a) * 40 * s * s + (a === 0 ? 0 : 0);
        c.strokeStyle = C.m; c.lineWidth = 2; c.beginPath(); c.moveTo(300, 0); c.lineTo(300, y); c.stroke();
        c.strokeStyle = C.y; c.lineWidth = 3; c.strokeRect(220, y, 160, 170);
        c.fillStyle = C.faint; c.fillRect(270, y + 156, 60, 10);
        figure(c, 300, y + 156, 90, C.y, false);
        arrow(c, 410, y + 85, 410, y + 85 - Math.sign(a) * 40, C.o, a === 0 ? "" : "a = " + f(Math.abs(a)) + (a > 0 ? " up" : " down"), { w: 2.5, lx: 8 });
        arrow(c, 340, y + 150, 340, y + 150 - N * 0.12, C.b, rev || !(p.ask || []).includes("N") ? "N = " + f(N, 1) + " N" : "N = ?", { w: 2.5, lx: 6 });
        arrow(c, 260, y + 100, 260, y + 100 + m * G * 0.12, C.r, "mg = " + f(m * G) + " N", { w: 2.5, la: "right", lx: -6 });
        panel(c, ["mass = " + f(m) + " kg", "N − mg = ma", ["scale reads " + f(N, 1) + " N", (p.ask || []).includes("N")], N > m * G ? "feels heavier" : N < m * G ? "feels lighter" : "feels normal"], 704, 40, rev, { a: "right" });
      }
    };
  };

  // uniform circular motion (top view); mode "orbit" draws a planet
  SIMS.circle = p => {
    const r = p.r, v = p.v, m = p.m || 1, Tp = 2 * Math.PI * r / v, ac = v * v / r;
    const R = 92, cx = 250, cy = 135;
    return {
      D: p.release ? 4.5 : 4, hold: 0.6,
      draw(c, t, rev) {
        const ask = p.ask || [], lap = p.release ? 3 : 4, ang = (t / lap) * Math.PI * 2;
        c.setLineDash([4, 6]); c.strokeStyle = C.faint; c.lineWidth = 2; c.beginPath(); c.arc(cx, cy, R, 0, 7); c.stroke(); c.setLineDash([]);
        if (p.mode === "orbit") { const g2 = c.createRadialGradient(cx - 14, cy - 14, 4, cx, cy, 44); g2.addColorStop(0, "#7CC4FF"); g2.addColorStop(1, "#1C2F66"); c.fillStyle = g2; c.beginPath(); c.arc(cx, cy, 40, 0, 7); c.fill(); }
        else { c.fillStyle = C.m; c.beginPath(); c.arc(cx, cy, 4, 0, 7); c.fill(); }
        let x, y, vxu, vyu, free = false;
        if (p.release && t > 3) { const a0 = Math.PI * 2; x = cx + R * Math.cos(a0) - Math.sin(a0) * 0; y = cy - R * Math.sin(a0); free = true; const d = (t - 3) * 120; x += 0; y -= d; vxu = 0; vyu = -1; }
        else { x = cx + R * Math.cos(ang); y = cy - R * Math.sin(ang); vxu = -Math.sin(ang); vyu = -Math.cos(ang); }
        if (p.mode === "string" && !free) { c.strokeStyle = C.m; c.lineWidth = 1.5; c.beginPath(); c.moveTo(cx, cy); c.lineTo(x, y); c.stroke(); }
        if (p.mode === "orbit") { c.save(); c.translate(x, y); c.rotate(-ang); c.fillStyle = C.y; c.fillRect(-8, -5, 16, 10); c.fillStyle = C.b; c.fillRect(-20, -3, 10, 6); c.fillRect(10, -3, 10, 6); c.restore(); }
        else if (p.mode === "car") { c.save(); c.translate(x, y); c.rotate(Math.atan2(vyu, vxu)); c.fillStyle = C.y; rr(c, -14, -8, 28, 16, 4); c.fill(); c.restore(); }
        else ball(c, x, y, 10, C.y);
        arrow(c, x, y, x + vxu * 48, y + vyu * 48, C.b, "v", { w: 2.5 });
        if (!free) arrow(c, x, y, x + (cx - x) / R * 40, y + (cy - y) / R * 40, C.r, p.mode === "orbit" ? "Fg" : p.mode === "car" ? "friction" : p.mode === "string" ? "T" : "Fnet", { w: 2.5 });
        else txt(c, "released: moves in a straight line", x + 14, y + 20, { c: C.m, s: 12 });
        panel(c, ["r = " + f(r) + " m   v = " + f(v) + " m/s", ["ac = v²/r = " + f(ac, 2) + " m/s²", ask.includes("a")], ["Fc = mv²/r = " + f(m * ac, 2) + " N", ask.includes("F")], ["period T = 2πr/v = " + f(Tp, 2) + " s", ask.includes("T")]], 704, 40, rev, { a: "right" });
        txt(c, "velocity is tangent; acceleration points to the center", 470, 250, { c: C.m, s: 12, a: "center" });
      }
    };
  };

  // spring scale: hang masses one at a time, F = kx
  SIMS.hooke = p => {
    const k = p.k, ms = p.masses || [1, 2, 3];
    return {
      D: ms.length * 1.4 + 0.4, hold: 1,
      draw(c, t, rev) {
        const i = Math.min(ms.length - 1, Math.floor(t / 1.4)), u = clamp((t - i * 1.4) / 0.7, 0, 1);
        const prev = i ? ms[i - 1] * G / k : 0, x = prev + (ms[i] * G / k - prev) * ease(u);
        const xmax = ms[ms.length - 1] * G / k, sc = 120 / xmax, top = 24, L0 = 60, y = top + L0 + x * sc;
        c.fillStyle = C.m; c.fillRect(180, 10, 140, 10);
        c.strokeStyle = C.o; c.lineWidth = 2.5; c.beginPath(); c.moveTo(250, top);
        for (let j = 1; j <= 14; j++) c.lineTo(250 + (j % 2 ? -12 : 12), top + ((y - top) * j) / 15); c.lineTo(250, y); c.stroke();
        box(c, 222, y, 56, 40, C.y, f(ms[i]) + " kg");
        c.strokeStyle = C.line; c.lineWidth = 1.5; c.beginPath(); c.moveTo(330, top + L0); c.lineTo(330, top + L0 + xmax * sc + 10); c.stroke();
        c.setLineDash([3, 4]); c.beginPath(); c.moveTo(280, y); c.lineTo(340, y); c.moveTo(240, top + L0); c.lineTo(340, top + L0); c.stroke(); c.setLineDash([]);
        txt(c, "x = " + f(x, 3) + " m", 346, (top + L0 + y) / 2, { c: C.y, s: 13, b: 1 });
        // F vs x graph
        axes(c, 470, 240, 210, 180, "x", "F");
        ms.slice(0, i + 1).forEach(mm => { const xx = mm * G / k; c.fillStyle = C.b; c.beginPath(); c.arc(470 + xx * 200 / xmax, 240 - mm * G * 170 / (ms[ms.length - 1] * G), 4, 0, 7); c.fill(); });
        c.strokeStyle = C.b; c.setLineDash([4, 4]); c.beginPath(); c.moveTo(470, 240); c.lineTo(670, 70); c.stroke(); c.setLineDash([]);
        panel(c, ["F = kx", ["k = slope = " + f(k) + " N/m", (p.ask || []).includes("k")]], 704, 28, rev, { a: "right" });
      }
    };
  };

  // free-body diagram: forces [{l, F, dir}] (dir in degrees, 0 = right, 90 = up)
  SIMS.fbd = p => {
    const fs_ = p.forces, m = p.m || 1;
    let nx = 0, ny = 0; fs_.forEach(q => { nx += q.F * Math.cos(q.dir * D2R); ny += q.F * Math.sin(q.dir * D2R); });
    const net = Math.hypot(nx, ny), big = Math.max(...fs_.map(q => q.F), net, 1), sc = 90 / big;
    const cols = [C.y, C.b, C.g, C.o, C.p, C.r];
    return {
      D: 2.6, hold: 1.6,
      draw(c, t, rev) {
        const cx = 230, cy = 140, s = ease(clamp(t / 1.6, 0, 1));
        thing(c, p.obj || "box", cx - 34, cy + 28, 68, 56, "rgba(255,200,87,.85)", f(m) + " kg");
        fs_.forEach((q, i) => {
          const L = q.F * sc * s, ex = cx + Math.cos(q.dir * D2R) * L, ey = cy - Math.sin(q.dir * D2R) * L;
          arrow(c, cx, cy, ex, ey, q.c || cols[i % cols.length], s > 0.9 ? q.l + " = " + f(q.F) + " N" : "", { w: 3, lx: Math.cos(q.dir * D2R) >= 0 ? 6 : -6, la: Math.cos(q.dir * D2R) >= 0 ? "left" : "right" });
        });
        if (t > 1.8 && net > 0.01) arrow(c, cx, cy, cx + nx * sc, cy - ny * sc, C.w, rev ? "Fnet" : "", { w: 2.5, dash: 1 });
        const lines = ["ΣFx = " + f(nx, 2) + " N", "ΣFy = " + f(ny, 2) + " N", ["Fnet = " + f(net, 2) + " N", (p.ask || []).includes("F")], ["a = Fnet/m = " + f(net / m, 2) + " m/s²", (p.ask || []).includes("a")]];
        if (net < 0.01) lines.push("balanced: constant velocity");
        panel(c, lines, 704, 40, rev, { a: "right" });
      }
    };
  };

  /* ---------- runtime ---------- */
  const live = new Set();
  function mount(el, params) {
    const p = params || JSON.parse(el.dataset.sim);
    const make = SIMS[p.type];
    if (!make) return null;
    const sim = make(p);
    const SH = sim.h || H;   // an animation type can ask for a taller canvas
    el.classList.add("sim");
    const stepBtns = sim.marks ? `<button class="sim-btn back" aria-label="Previous step">◀ Step</button><button class="sim-btn fwd" aria-label="Next step">Step ▶</button>` : "";
    el.innerHTML = `<div class="sim-stage"><canvas width="${W}" height="${SH}" aria-label="${p.alt || "Animated example"}" role="img"></canvas></div>
      <div class="sim-ctrl"><button class="sim-btn play" aria-label="Pause">❚❚</button><button class="sim-btn replay">↺ Replay</button>${stepBtns}<button class="sim-btn slow">Slow motion</button>${p.caption ? `<span class="sim-cap">${p.caption}</span>` : ""}</div>`;
    const cv = el.querySelector("canvas"), c = cv.getContext("2d");
    const st = { t: 0, playing: !reduce, rev: !!p.reveal, slow: false, visible: false, last: 0, dpr: 1 };
    function size() {
      const dpr = Math.min(2, window.devicePixelRatio || 1), w = cv.clientWidth || W;
      cv.width = Math.round(w * dpr); cv.height = Math.round((w * SH / W) * dpr);
      st.scale = (w / W) * dpr;
    }
    function render() {
      c.setTransform(1, 0, 0, 1, 0, 0); c.clearRect(0, 0, cv.width, cv.height);
      c.setTransform(st.scale, 0, 0, st.scale, 0, 0);
      try { sim.draw(c, Math.min(st.t, sim.D), st.rev); } catch (e) { console.error(e); }
    }
    function tick(now) {
      const dt = Math.min(0.05, (now - (st.last || now)) / 1000); st.last = now;
      if (st.playing && st.visible) {
        st.t += dt * (st.slow ? 0.35 : 1);
        if (st.t > sim.D + (sim.hold ?? 1)) st.t = 0;
        render();
      }
    }
    const playBtn = el.querySelector(".play");
    playBtn.onclick = () => { st.playing = !st.playing; playBtn.textContent = st.playing ? "❚❚" : "▶"; playBtn.setAttribute("aria-label", st.playing ? "Pause" : "Play"); };
    if (!st.playing) playBtn.textContent = "▶";
    el.querySelector(".replay").onclick = () => { st.t = 0; st.playing = true; playBtn.textContent = "❚❚"; render(); };
    if (sim.marks) {
      // step through: pause and jump to the previous / next step time
      const pause = () => { st.playing = false; playBtn.textContent = "▶"; playBtn.setAttribute("aria-label", "Play"); };
      el.querySelector(".fwd").onclick = () => { pause(); const n = sim.marks.find(m => m > st.t + 1e-3); st.t = n === undefined ? sim.D : n; render(); };
      el.querySelector(".back").onclick = () => { pause(); const ms = sim.marks.filter(m => m < st.t - 1e-3); st.t = ms.length ? ms[ms.length - 1] : 0; render(); };
    }
    const slowBtn = el.querySelector(".slow");
    slowBtn.onclick = () => { st.slow = !st.slow; slowBtn.classList.toggle("on", st.slow); };
    const ctl = { tick, render, size, st, el,
      reveal() { st.rev = true; render(); el.classList.add("revealed"); } };
    el._ctl = ctl;
    size();
    if (reduce) st.t = sim.D;
    render();
    live.add(ctl);
    if ("IntersectionObserver" in window) {
      new IntersectionObserver(es => es.forEach(e => { st.visible = e.isIntersecting; if (e.isIntersecting) { size(); render(); } }), { threshold: 0.15 }).observe(el);
    } else st.visible = true;
    return ctl;
  }
  function loop(now) { live.forEach(s => (s.el.isConnected ? s.tick(now) : live.delete(s))); requestAnimationFrame(loop); }
  requestAnimationFrame(loop);
  window.addEventListener("resize", () => live.forEach(s => { s.size(); s.render(); }));
  // re-size when a hidden chapter becomes visible
  document.addEventListener("chapterchange", () => live.forEach(s => { s.size(); s.render(); }));

  function mountAll(root) { (root || document).querySelectorAll(".sim[data-sim]").forEach(el => { if (!el.dataset.mounted) { el.dataset.mounted = 1; mount(el); } }); }
  window.Sims = { mount, mountAll, types: SIMS };
})();
