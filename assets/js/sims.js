/* ===== Apogee — 2D animated examples =====
   Usage in HTML:  <div class="sim" data-sim='{"type":"collide","m1":2,"v1":5,"m2":3,"v2":-2,"mode":"stick"}'></div>
   Quiz questions can carry a "sim" object; the answer values stay hidden until the question is answered.
   Add "reveal":true to a data-sim to show answer values from the start.
   To add a new animation type: add SIMS.yourType = p => ({ D: seconds, hold: seconds, draw(c, t, rev) {...} }). */
(function () {
  const W = 720, H = 270;
  const C = { y: "#eafe07", b: "#2e96f5", w: "#ffffff", m: "#b7c3e0", r: "#ff6b5b", g: "#3ee39a", o: "#ff9d57", p: "#c49bff",
              line: "rgba(255,255,255,.28)", faint: "rgba(255,255,255,.10)", dark: "#07173f" };
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
    c.font = `${o.b ? "700 " : "500 "}${o.s || 14}px "Fira Sans", system-ui, sans-serif`;
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
    c.fillStyle = "#0b1f52"; c.strokeStyle = C.m; c.lineWidth = 2;
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
    g.addColorStop(0, "#fff"); g.addColorStop(0.25, col); g.addColorStop(1, col);
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

  /* ---------- animation types ---------- */
  const SIMS = {};

  // single moving object, shows K or p
  SIMS.cart = p => ({
    D: 3, hold: 0.8,
    draw(c, t, rev) {
      ground(c, 200);
      const x = 40 + (520 / 3) * t;
      cart(c, x, 200, 90, 46, C.y, f(p.m) + " kg");
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
          cart(c, x, y, 76, 38, i ? C.b : C.y, "m");
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
          cart(c, x, y, 64, 32, col, "");
          if (s < 1) arrow(c, x + 32, y - 52, x + 32 + 46 * (1 - s) + 6, y - 52, C.w, lab, { w: 2.5 });
          else txt(c, "stopped", x + 32, y - 48, { c: C.m, s: 12, a: "center" });
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
        box(c, 230, y, 60, 44, C.y, f(p.m) + " kg");
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
        box(c, x, gy - bh, bw, bh, C.y, p.m ? f(p.m) + " kg" : "");
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

  // frictionless track drop
  SIMS.coaster = p => {
    const h = p.h, top = 54, bot = 214, x0 = 70, xa = 130, xb = 420, x1 = 680;
    const yOf = x => x < xa ? top : x > xb ? bot : top + (bot - top) * (1 - Math.cos(Math.PI * (x - xa) / (xb - xa))) / 2;
    const mpp = h / (bot - top);
    // precompute motion with v = sqrt(2 g drop)
    const path = []; let x = xa + 1, tt = 0;
    while (x < x1 - 50 && path.length < 5000) {
      const drop = (yOf(x) - top) * mpp, v = Math.sqrt(2 * G * drop) + 0.4;
      const dydx = (yOf(x + 0.5) - yOf(x - 0.5)), dsdx = Math.sqrt(1 + dydx * dydx) * mpp;
      path.push([x, tt, v - 0.4]); x += (v * 0.01) / dsdx; tt += 0.01;
    }
    const T = tt;
    return {
      D: 4, hold: 1,
      draw(c, t, rev) {
        c.strokeStyle = C.m; c.lineWidth = 3; c.beginPath(); c.moveTo(x0, top);
        for (let xx = x0; xx <= x1; xx += 4) c.lineTo(xx, yOf(xx)); c.stroke();
        c.strokeStyle = C.faint; c.lineWidth = 1;
        for (let xx = x0 + 10; xx <= x1; xx += 30) { c.beginPath(); c.moveTo(xx, yOf(xx)); c.lineTo(xx, 250); c.stroke(); }
        c.setLineDash([4, 6]); c.strokeStyle = C.o; c.beginPath(); c.moveTo(450, top); c.lineTo(450, bot); c.stroke(); c.setLineDash([]);
        arrow(c, 450, top, 450, bot, C.o, "", { w: 1.5 }); txt(c, "h = " + f(h) + " m", 458, (top + bot) / 2, { c: C.o, s: 14, b: 1 });
        const tr = (t / 4) * T; let i = path.findIndex(q => q[1] >= tr); if (i < 0) i = path.length - 1;
        const [bx, , v] = path[i], by = yOf(bx);
        ball(c, bx, by - 13, 13, C.y);
        const drop = (by - top) * mpp;
        bars(c, 560, 120, [{ l: "Ug", v: h - drop, c: C.b }, { l: "K", v: drop, c: C.y }], h, 80);
        txt(c, rev ? "v = " + f(v, 1) + " m/s" : "v at bottom = ?", 560, 172, { c: C.y, s: 15, b: 1 });
        txt(c, "Frictionless: Ug → K", 24, 30, { c: C.m, s: 13, b: 1 });
      }
    };
  };

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
      c.fillStyle = "rgba(46,150,245,.18)"; c.strokeStyle = C.m; c.lineWidth = 2;
      c.beginPath(); c.moveTo(x0, y0);
      for (let i = 0; i < n; i++) { c.lineTo(x0 + i * sw, y0 - (i + 1) * sh); c.lineTo(x0 + (i + 1) * sw, y0 - (i + 1) * sh); }
      c.lineTo(x0 + n * sw, y0); c.closePath(); c.fill(); c.stroke();
      const s = clamp(t / 4, 0, 1), pos = s * n, i = Math.min(n - 1, Math.floor(pos)), fr = pos - Math.floor(pos);
      const hop = s >= 1 ? 0 : Math.sin(fr * Math.PI) * 14;
      const bx = x0 - 20 + pos * sw, by = y0 - (s >= 1 ? n : Math.floor(pos) + (fr > 0.5 ? 1 : 0)) * sh - 18 - hop;
      ball(c, bx + 20, by, 14, C.y);
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
        c.fillStyle = isT ? "rgba(46,150,245,.35)" : "rgba(234,254,7,.28)";
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
        cart(c, x1, gy, w1, 40, C.y, f(m1) + " kg");
        cart(c, x2, gy, w2, 40, C.b, f(m2) + " kg");
        if (after && p.mode === "stick") { c.fillStyle = C.w; c.fillRect(r1 - 3, gy - 38, 6, 18); }
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
          cart(c, X - w1, gy, w1, 40, C.y, f(m1) + " kg");
          cart(c, X, gy, w2, 40, C.b, f(m2) + " kg");
          if (Math.abs(v0) > 0.001) { arrow(c, X, 112, X + Math.sign(v0) * 50, 112, C.w, "", { w: 2.5 }); txt(c, "v₀ = " + fs(v0) + " m/s", X, 98, { c: C.w, s: 13, b: 1, a: "center" }); }
          else txt(c, "at rest", X, 112, { c: C.m, s: 13, b: 1, a: "center" });
        } else {
          const dt = t - ts, X = 360;
          const a1 = X + disp(v1f) * dt, a2 = X + disp(v2f) * dt;
          cart(c, a1 - w1, gy, w1, 40, C.y, f(m1) + " kg");
          cart(c, a2, gy, w2, 40, C.b, f(m2) + " kg");
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
        c.save(); c.fillStyle = "#fff7e6"; c.shadowColor = "#fff"; c.shadowBlur = 8; c.beginPath(); c.ellipse(x + 20, L.y - 22, 22, 17, 0, 0, 7); c.fill(); c.restore();
        if (i === 0 && t > tc) { c.strokeStyle = C.r; c.lineWidth = 2; c.beginPath(); c.moveTo(x + 30, L.y - 38); c.lineTo(x + 22, L.y - 26); c.lineTo(x + 32, L.y - 18); c.lineTo(x + 24, L.y - 8); c.stroke(); }
        txt(c, L.lab, 20, L.y - 82, { c: L.col, s: 13, b: 1 });
        // mini F-t graph
        const gx = 400, gw = 280, gh = 70, base = L.y - 6;
        c.strokeStyle = C.line; c.lineWidth = 1.5; c.beginPath(); c.moveTo(gx, base - gh - 6); c.lineTo(gx, base); c.lineTo(gx + gw, base); c.stroke();
        txt(c, "F", gx - 12, base - gh, { c: C.m, s: 11 }); txt(c, "t", gx + gw + 6, base + 4, { c: C.m, s: 11 });
        const tt = clamp((t - tc) / 1.0, 0, 1), dur = i ? 0.8 : 0.1, peak = i ? gh * 0.15 : gh;
        const start = gx + 30, width = dur * 220;
        c.fillStyle = i ? "rgba(62,227,154,.35)" : "rgba(255,107,91,.35)"; c.strokeStyle = L.col; c.lineWidth = 2;
        c.beginPath(); c.moveTo(start, base);
        for (let s = 0; s <= tt; s += 0.01) { const u = s / 1; c.lineTo(start + u * width, base - peak * Math.sin(Math.PI * clamp(u, 0, 1))); }
        c.lineTo(start + tt * width, base); c.closePath(); c.fill(); c.stroke();
      });
      txt(c, rev ? "Same Δp = same area. Longer Δt means smaller F." : "Which one feels the smaller force?", 540, 262, { c: C.y, s: 14, b: 1, a: "center" });
    }
  });

  /* ---------- runtime ---------- */
  const live = new Set();
  function mount(el, params) {
    const p = params || JSON.parse(el.dataset.sim);
    const make = SIMS[p.type];
    if (!make) return null;
    const sim = make(p);
    el.classList.add("sim");
    el.innerHTML = `<div class="sim-stage"><canvas width="${W}" height="${H}" aria-label="${p.alt || "Animated example"}" role="img"></canvas></div>
      <div class="sim-ctrl"><button class="sim-btn play" aria-label="Pause">❚❚</button><button class="sim-btn replay">↺ Replay</button><button class="sim-btn slow">Slow motion</button>${p.caption ? `<span class="sim-cap">${p.caption}</span>` : ""}</div>`;
    const cv = el.querySelector("canvas"), c = cv.getContext("2d");
    const st = { t: 0, playing: !reduce, rev: !!p.reveal, slow: false, visible: false, last: 0, dpr: 1 };
    function size() {
      const dpr = Math.min(2, window.devicePixelRatio || 1), w = cv.clientWidth || W;
      cv.width = Math.round(w * dpr); cv.height = Math.round((w * H / W) * dpr);
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
