/* ===== Margin: computer science animations and interactive labs =====
   Animations (load after sims.js; they plug into the same runtime, so they get Play / Replay / Step / Slow motion):
     trace   {code:[...], steps:[[line, {var:val}, "output so far"]], ask:"out"|"vars"}  step through code line by line
     memory  {frames:[{note, vars:[[name,type,value or "@id"]], objs:[[id, cls, fields or "text"]]}], hide:[names]}
     strbox  {s:"computer", ops:[{f:"substring",a:1,b:4}, {f:"substring",a:3}, {f:"indexOf",x:"put"}, {f:"length"}], ask:true}
     grid    {n:4, m:5, mode:"rect"|"tri"|"tri2", outer:"i", inner:"j", ask:true}  nested loops filling a grid
   Interactive labs (plain HTML, no canvas):
     <div class="cslab" data-lab='{"type":"string","s":"computer"}'></div>
     types: string, bool, arith, loop, casting */
(function () {
  if (!window.Sims) return;
  const S = window.Sims.types;
  const W = 720;
  const TERM = document.body.classList.contains("th-term");
  const C = TERM
    ? { y: "#FCE94F", b: "#729FCF", w: "#D3D7CF", m: "#9A9F95", r: "#EF2929", g: "#8AE234", o: "#E9B96E", p: "#34E2E2",
        line: "rgba(255,255,255,.16)", faint: "rgba(255,255,255,.06)", dark: "#0C0C0C", panel: "rgba(20,20,20,.95)", kw: "#729FCF", hl: "252,233,79" }
    : { y: "#FFC857", b: "#7CC4FF", w: "#EEF3FF", m: "#A3B0D0", r: "#FF6B6B", g: "#5BE3A4", o: "#FF9F5A", p: "#C3B5FF",
        line: "rgba(150,180,255,.22)", faint: "rgba(150,180,255,.08)", dark: "#050816", panel: "rgba(14,24,56,.9)", kw: "#7CC4FF", hl: "255,200,87" };
  const MONO = '"JetBrains Mono", ui-monospace, Menlo, Consolas, monospace';
  const KW = new Set("int double boolean char long String if else while for return new public private protected class static void final this null true false break continue".split(" "));
  const ease = x => (x < 0 ? 0 : x > 1 ? 1 : x * x * (3 - 2 * x));

  function txt(c, s, x, y, o = {}) {
    c.font = `${o.b ? "700 " : "500 "}${o.s || 14}px ${o.mono ? MONO : '"Plus Jakarta Sans", system-ui, sans-serif'}`;
    c.fillStyle = o.c || C.w; c.textAlign = o.a || "left"; c.textBaseline = o.bl || "alphabetic";
    c.globalAlpha = o.al ?? 1; c.fillText(s, x, y); c.globalAlpha = 1;
  }
  function rr(c, x, y, w, h, r) {
    c.beginPath(); c.moveTo(x + r, y); c.arcTo(x + w, y, x + w, y + h, r); c.arcTo(x + w, y + h, x, y + h, r);
    c.arcTo(x, y + h, x, y, r); c.arcTo(x, y, x + w, y, r); c.closePath();
  }
  function panel(c, x, y, w, h, title) {
    c.fillStyle = C.panel; rr(c, x, y, w, h, 10); c.fill();
    c.strokeStyle = C.line; c.lineWidth = 1; rr(c, x, y, w, h, 10); c.stroke();
    if (title) txt(c, title.toUpperCase(), x + 12, y + 18, { s: 11, b: 1, c: C.m });
  }
  // light syntax colouring for one line of Java
  function codeLine(c, s, x, y, size, al = 1) {
    c.font = `500 ${size}px ${MONO}`; c.textBaseline = "alphabetic"; c.textAlign = "left";
    const re = /(\/\/.*$)|("(?:[^"\\]|\\.)*")|('(?:[^'\\]|\\.)')|(\b\d+(?:\.\d+)?\b)|([A-Za-z_]\w*)|(\s+)|(.)/g;
    let m, cx = x;
    while ((m = re.exec(s))) {
      const t = m[0];
      let col = C.w;
      if (m[1]) col = C.m; else if (m[2] || m[3]) col = C.g; else if (m[4]) col = C.o;
      else if (m[5] && KW.has(t)) col = C.kw; else if (m[5] && /^[A-Z]/.test(t)) col = C.p;
      c.globalAlpha = al; c.fillStyle = col; c.fillText(t, cx, y); c.globalAlpha = 1;
      cx += c.measureText(t).width;
    }
  }
  function wrapLines(s, max) {
    const out = [];
    String(s).split("\n").forEach(line => {
      while (line.length > max) { out.push(line.slice(0, max)); line = line.slice(max); }
      out.push(line);
    });
    return out;
  }
  function arrowTo(c, x1, y1, x2, y2, col) {
    c.save(); c.strokeStyle = col; c.fillStyle = col; c.lineWidth = 2.2;
    const mx = (x1 + x2) / 2;
    c.beginPath(); c.moveTo(x1, y1); c.bezierCurveTo(mx, y1, mx, y2, x2 - 8, y2); c.stroke();
    c.beginPath(); c.moveTo(x2, y2); c.lineTo(x2 - 11, y2 - 6); c.lineTo(x2 - 11, y2 + 6); c.closePath(); c.fill();
    c.restore();
  }

  /* ---------- trace: step through code ---------- */
  S.trace = p => {
    const code = p.code, steps = p.steps, n = steps.length, STEP = p.step || 1.15;
    const size = code.length > 14 ? 13 : 14, LH = size + 7;
    const h = Math.max(270, 56 + code.length * LH + 18);
    const marks = steps.map((_, i) => i * STEP + 0.4);   // land after the highlight has moved
    return {
      D: n * STEP - 0.3, hold: 2, h, marks,
      draw(c, t, rev) {
        const k = Math.min(n - 1, Math.floor(t / STEP)), f = ease((t - k * STEP) / 0.35);
        const [line, vars, out] = steps[k];
        const prev = k > 0 ? steps[k - 1][1] : {};
        // code panel
        panel(c, 12, 10, 440, h - 20, p.title || "Code");
        txt(c, `STEP ${k + 1} OF ${n}`, 440, 28, { s: 11, b: 1, c: C.y, a: "right" });
        const y0 = 50;
        if (line > 0) {
          const prevLine = k > 0 ? steps[k - 1][0] : line;
          const ly = y0 + ((prevLine > 0 ? prevLine : line) - 1 + ((line - (prevLine > 0 ? prevLine : line)) * f)) * LH;
          c.fillStyle = `rgba(${C.hl},.16)`; rr(c, 18, ly - size - 2, 428, LH, 5); c.fill();
          c.fillStyle = C.y; rr(c, 18, ly - size - 2, 4, LH, 2); c.fill();
        }
        code.forEach((s, i) => {
          txt(c, String(i + 1), 40, y0 + i * LH, { s: 11, c: C.m, a: "right", mono: 1 });
          codeLine(c, s, 50, y0 + i * LH, size, i + 1 === line ? 1 : 0.78);
        });
        // variables
        const names = Object.keys(vars);
        const vh = Math.max(96, 34 + names.length * 24);
        panel(c, 466, 10, 242, vh, "Variables");
        names.forEach((nm, i) => {
          const y = 48 + i * 24, changed = JSON.stringify(prev[nm]) !== JSON.stringify(vars[nm]);
          const hide = !rev && (p.ask === "vars" || p.ask === "both");
          if (changed && !hide) { c.fillStyle = `rgba(${C.hl},${0.22 * (1 - f) + 0.08})`; rr(c, 474, y - 16, 226, 22, 5); c.fill(); }
          txt(c, nm, 484, y, { s: 14, mono: 1, c: C.m });
          let v = hide ? "?" : String(vars[nm]);
          if (v.length > 17) v = v.slice(0, 16) + "…";
          txt(c, v, 692, y, { s: 14, mono: 1, b: 1, c: changed && !hide ? C.y : C.w, a: "right" });
        });
        if (!names.length) txt(c, "(none yet)", 484, 48, { s: 13, c: C.m });
        // console
        const cy = 10 + vh + 10, ch = h - cy - 10;
        panel(c, 466, cy, 242, ch, "Output");
        if (!rev && (p.ask === "out" || p.ask === "both")) {
          txt(c, "Hidden until you answer", 484, cy + 44, { s: 13, c: C.m });
        } else {
          const lines = wrapLines(out || "", 24), maxL = Math.floor((ch - 30) / 19);
          lines.slice(-maxL).forEach((l, i) => txt(c, l, 484, cy + 42 + i * 19, { s: 14, mono: 1, c: C.g }));
        }
      }
    };
  };

  /* ---------- memory: variables, objects and references ---------- */
  S.memory = p => {
    const F = p.frames, n = F.length, STEP = p.step || 2.6;
    const maxRows = Math.max(...F.map(fr => Math.max(fr.vars.length, (fr.objs || []).reduce((s, o) => s + 1 + (Array.isArray(o[2]) ? o[2].length : 0), 0) * 0.62)));
    const h = Math.max(270, 70 + maxRows * 58);
    return {
      D: n * STEP - 0.4, hold: 2, h, marks: F.map((_, i) => i * STEP + 0.55),
      draw(c, t, rev) {
        const k = Math.min(n - 1, Math.floor(t / STEP)), f = ease((t - k * STEP) / 0.5);
        const fr = F[k], pv = k > 0 ? F[k - 1] : { vars: [], objs: [] };
        txt(c, "VARIABLES", 24, 24, { s: 11, b: 1, c: C.m });
        txt(c, "OBJECTS (HEAP)", 400, 24, { s: 11, b: 1, c: C.m });
        txt(c, `${k + 1} / ${n}`, W - 16, 24, { s: 11, b: 1, c: C.y, a: "right" });
        // objects
        const pos = {};
        let oy = 38;
        (fr.objs || []).forEach(o => {
          const [id, cls, fields] = o, isNew = !(pv.objs || []).some(q => q[0] === id);
          const rows = Array.isArray(fields) ? fields.length : 1, bh = 30 + rows * 24;
          const al = isNew ? f : 1;
          c.globalAlpha = al;
          c.fillStyle = TERM ? "rgba(114,159,207,.12)" : "rgba(124,196,255,.12)"; rr(c, 400, oy, 300, bh, TERM ? 2 : 10); c.fill();
          c.strokeStyle = C.b; c.lineWidth = 1.5; rr(c, 400, oy, 300, bh, 10); c.stroke();
          c.globalAlpha = 1;
          txt(c, cls, 414, oy + 20, { s: 13, b: 1, c: C.p, mono: 1, al });
          if (Array.isArray(fields)) fields.forEach(([fn, fv], i) => {
            const old = (pv.objs || []).find(q => q[0] === id);
            const was = old && Array.isArray(old[2]) ? (old[2].find(x => x[0] === fn) || [])[1] : undefined;
            const ch = old && was !== fv;
            if (ch) { c.fillStyle = `rgba(${C.hl},${0.25 * (1 - f) + 0.08})`; rr(c, 408, oy + 28 + i * 24, 284, 22, 5); c.fill(); }
            txt(c, fn, 420, oy + 44 + i * 24, { s: 13, mono: 1, c: C.m, al });
            txt(c, String(fv), 688, oy + 44 + i * 24, { s: 13, mono: 1, b: 1, c: ch ? C.y : C.w, a: "right", al });
          });
          else txt(c, String(fields), 414, oy + 46, { s: 15, mono: 1, b: 1, c: C.g, al });
          pos[id] = [400, oy + 20];
          oy += bh + 14;
        });
        // variables
        fr.vars.forEach(([nm, ty, val], i) => {
          const y = 38 + i * 58, old = pv.vars.find(v => v[0] === nm), isNew = !old, ch = old && old[2] !== val;
          const al = isNew ? f : 1;
          c.globalAlpha = al;
          c.fillStyle = C.panel; rr(c, 20, y, 250, 44, 9); c.fill();
          c.strokeStyle = ch ? C.y : C.line; c.lineWidth = ch ? 2 : 1; rr(c, 20, y, 250, 44, 9); c.stroke();
          c.globalAlpha = 1;
          txt(c, ty, 32, y + 18, { s: 11, c: C.p, mono: 1, al });
          txt(c, nm, 32, y + 36, { s: 15, mono: 1, b: 1, al });
          const hide = !rev && (p.hide || []).includes(nm);
          if (typeof val === "string" && val.startsWith("@")) {
            c.fillStyle = C.b; c.beginPath(); c.arc(244, y + 22, 5, 0, 7); c.fill();
            const tg = pos[val.slice(1)];
            if (tg && !hide) { c.globalAlpha = isNew || ch ? f : 1; arrowTo(c, 249, y + 22, tg[0], tg[1], ch ? C.y : C.b); c.globalAlpha = 1; }
          } else {
            txt(c, hide ? "?" : String(val), 258, y + 30, { s: 16, mono: 1, b: 1, c: val === "null" ? C.m : C.y, a: "right", al });
          }
        });
        if (fr.note) {
          const lines = wrapLines(fr.note, 92);
          lines.forEach((l, i) => txt(c, l, 20, h - 14 - (lines.length - 1 - i) * 18, { s: 13.5, c: C.w, al: f }));
        }
      }
    };
  };

  /* ---------- strbox: String indexes and methods ---------- */
  S.strbox = p => {
    const s = p.s, ops = p.ops || [{ f: "length" }], STEP = 3.2;
    const n = s.length, bw = Math.min(54, Math.floor(640 / Math.max(n, 1))), x0 = (W - bw * n) / 2;
    function run(o) {
      if (o.f === "length") return { lo: 0, hi: n, code: `s.length()`, res: String(n) };
      if (o.f === "substring") {
        const b = o.b === undefined ? n : o.b;
        return { lo: o.a, hi: b, code: o.b === undefined ? `s.substring(${o.a})` : `s.substring(${o.a}, ${o.b})`, res: `"${s.slice(o.a, b)}"` };
      }
      if (o.f === "indexOf") { const i = s.indexOf(o.x); return { lo: i, hi: i < 0 ? -1 : i + o.x.length, code: `s.indexOf("${o.x}")`, res: String(i), scan: o.x }; }
      if (o.f === "equals") return { lo: 0, hi: n, code: `s.equals("${o.x}")`, res: String(s === o.x) };
      return { lo: 0, hi: 0, code: "", res: "" };
    }
    return {
      D: ops.length * STEP - 0.2, hold: 2, marks: ops.map((_, i) => i * STEP + STEP - 0.25),
      draw(c, t, rev) {
        const k = Math.min(ops.length - 1, Math.floor(t / STEP)), lt = t - k * STEP, r = run(ops[k]);
        txt(c, `String s = "${s}";`, 24, 30, { s: 15, mono: 1, c: C.w });
        txt(c, `${k + 1} / ${ops.length}`, W - 16, 30, { s: 11, b: 1, c: C.y, a: "right" });
        // scanning window for indexOf
        let lo = r.lo, hi = r.hi;
        if (r.scan !== undefined) {
          const L = r.scan.length, final = r.lo < 0 ? n - L : r.lo, pos = Math.min(final, Math.floor(lt / 0.32));
          if (lt < (final + 1) * 0.32) { lo = pos; hi = pos + L; }
        }
        for (let i = 0; i < n; i++) {
          const x = x0 + i * bw, inside = i >= lo && i < hi, show = lt > 0.5 || r.scan !== undefined;
          c.fillStyle = inside && show ? `rgba(${C.hl},.22)` : C.panel; rr(c, x + 2, 70, bw - 4, 56, 8); c.fill();
          c.strokeStyle = inside && show ? C.y : C.line; c.lineWidth = inside && show ? 2 : 1; rr(c, x + 2, 70, bw - 4, 56, 8); c.stroke();
          txt(c, s[i] === " " ? "␣" : s[i], x + bw / 2, 106, { s: 22, mono: 1, b: 1, a: "center", c: inside && show ? C.y : C.w });
          txt(c, String(i), x + bw / 2, 146, { s: 13, mono: 1, a: "center", c: C.b });
        }
        txt(c, String(n), x0 + n * bw + 4, 146, { s: 13, mono: 1, c: C.m });
        txt(c, "index", x0 - 10, 146, { s: 12, a: "right", c: C.m });
        if (r.code) {
          const al = ease((lt - 0.2) / 0.4);
          txt(c, r.code, 24, 196, { s: 18, mono: 1, b: 1, c: C.b, al });
          const hide = !rev && p.ask;
          const done = r.scan === undefined || lt > (Math.max(r.lo, 0) + 1) * 0.32 + 0.3 || r.lo < 0 && lt > (n - r.scan.length + 1) * 0.32 + 0.3;
          if (done) txt(c, "→ " + (hide ? "?" : r.res), 24, 234, { s: 20, mono: 1, b: 1, c: C.y, al: ease((lt - 0.9) / 0.4) });
          if (ops[k].f === "substring" && !hide) txt(c, `starts at ${r.lo}, stops before ${r.hi}  (length ${r.hi - r.lo})`, W - 20, 234, { s: 13, c: C.m, a: "right", al: ease((lt - 1.2) / 0.4) });
        }
      }
    };
  };

  /* ---------- grid: nested loops ---------- */
  S.grid = p => {
    const n = p.n, m = p.m || p.n, mode = p.mode || "rect";
    const cells = [];
    for (let i = 0; i < n; i++) {
      const top = mode === "tri" ? i : mode === "tri2" ? i + 1 : m;
      for (let j = 0; j < top; j++) cells.push([i, j]);
    }
    const per = Math.max(0.12, Math.min(0.4, 6 / Math.max(cells.length, 1)));
    const cw = Math.min(40, Math.floor(196 / Math.max(n, m))), gx = 64, gy = 54;
    return {
      D: cells.length * per + 0.3, hold: 2.2,
      draw(c, t, rev) {
        const k = Math.min(cells.length, Math.floor(t / per));
        txt(c, (p.inner || "j") + " →", gx, 20, { s: 13, mono: 1, b: 1, c: C.b });
        txt(c, (p.outer || "i") + " ↓", 14, gy + 4, { s: 13, mono: 1, b: 1, c: C.b });
        for (let i = 0; i < n; i++) {
          txt(c, String(i), gx - 8, gy + i * cw + cw / 2 + 5, { s: 11, mono: 1, c: C.m, a: "right" });
          for (let j = 0; j < m; j++) {
            if (i === 0) txt(c, String(j), gx + j * cw + cw / 2, gy - 6, { s: 11, mono: 1, c: C.m, a: "center" });
            c.strokeStyle = C.faint; c.lineWidth = 1; c.strokeRect(gx + j * cw + 1, gy + i * cw + 1, cw - 2, cw - 2);
          }
        }
        cells.slice(0, k).forEach(([i, j], idx) => {
          const last = idx === k - 1 && k < cells.length;
          c.fillStyle = last ? C.y : (TERM ? "rgba(138,226,52,.75)" : "rgba(124,196,255,.75)");
          rr(c, gx + j * cw + 3, gy + i * cw + 3, cw - 6, cw - 6, 4); c.fill();
        });
        const cur = cells[Math.max(0, k - 1)] || [0, 0];
        const x = gx + m * cw + 50;
        txt(c, "Inner loop body has run", x, 70, { s: 14, c: C.m });
        const done = k >= cells.length;
        txt(c, !rev && p.ask && done ? "? times" : `${k} time${k === 1 ? "" : "s"}`, x, 112, { s: 34, b: 1, c: C.y });
        if (k > 0 && !done) txt(c, `${p.outer || "i"} = ${cur[0]},  ${p.inner || "j"} = ${cur[1]}`, x, 150, { s: 16, mono: 1, c: C.w });
        if (done && (rev || !p.ask)) txt(c, p.note || "", x, 150, { s: 14, c: C.w });
      }
    };
  };

  /* =================== interactive labs =================== */
  const esc = s => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  const LABS = {};

  LABS.string = (el, p) => {
    el.innerHTML = `<div class="lab-h">String lab <span>Change the text or the numbers.</span></div>
      <div class="lab-row"><label>String s = <input class="lab-in w" data-k="s" value="${esc(p.s || "computer")}"></label></div>
      <div class="lab-boxes"></div>
      <div class="lab-row"><label>s.substring(<input class="lab-in n" data-k="a" type="number" value="${p.a ?? 1}">, <input class="lab-in n" data-k="b" type="number" value="${p.b ?? 4}">)</label><b class="lab-out" data-o="sub2"></b></div>
      <div class="lab-row"><label>s.substring(<input class="lab-in n" data-k="c" type="number" value="${p.c ?? 3}">)</label><b class="lab-out" data-o="sub1"></b></div>
      <div class="lab-row"><label>s.indexOf("<input class="lab-in" data-k="x" value="${esc(p.x ?? "put")}">")</label><b class="lab-out" data-o="idx"></b></div>
      <div class="lab-row"><label>s.length()</label><b class="lab-out" data-o="len"></b></div>
      <div class="lab-row"><label>s.compareTo("<input class="lab-in" data-k="t" value="${esc(p.t ?? "cat")}">")</label><b class="lab-out" data-o="cmp"></b></div>`;
    const get = k => el.querySelector(`[data-k="${k}"]`).value;
    function upd(hl) {
      const s = get("s"), n = s.length, a = +get("a"), b = +get("b"), c = +get("c"), x = get("x"), t = get("t");
      const ok2 = a >= 0 && b <= n && a <= b, ok1 = c >= 0 && c <= n;
      const lo = hl === "c" ? c : a, hi = hl === "c" ? n : b;
      el.querySelector(".lab-boxes").innerHTML = [...s].map((ch, i) => `<span class="${(hl === "c" ? ok1 : ok2) && i >= lo && i < hi ? "on" : ""}"><b>${esc(ch === " " ? "␣" : ch)}</b><i>${i}</i></span>`).join("") + `<span class="end"><b></b><i>${n}</i></span>`;
      const set = (o, v, bad) => { const e = el.querySelector(`[data-o="${o}"]`); e.innerHTML = v; e.classList.toggle("bad", !!bad); };
      set("sub2", ok2 ? `→ "${esc(s.slice(a, b))}"` : "→ StringIndexOutOfBoundsException", !ok2);
      set("sub1", ok1 ? `→ "${esc(s.slice(c))}"` : "→ StringIndexOutOfBoundsException", !ok1);
      set("idx", `→ ${s.indexOf(x)}${s.indexOf(x) < 0 ? " (not found)" : ""}`);
      set("len", `→ ${n}`);
      let cmp = 0; const L = Math.min(n, t.length);
      for (let i = 0; i < L && !cmp; i++) cmp = s.charCodeAt(i) - t.charCodeAt(i);
      if (!cmp) cmp = n - t.length;
      set("cmp", `→ ${cmp}${cmp < 0 ? " (negative: s comes first)" : cmp > 0 ? " (positive: s comes after)" : " (zero: same text)"}`);
    }
    el.querySelectorAll(".lab-in").forEach(i => i.addEventListener("input", () => upd(i.dataset.k)));
    el.querySelectorAll(".lab-in").forEach(i => i.addEventListener("focus", () => upd(i.dataset.k)));
    upd("a");
  };

  LABS.bool = (el, p) => {
    const vars = p.vars || ["a", "b"], exprs = p.exprs || ["a && b", "a || b", "!a", "!(a && b)", "!a || !b"];
    el.innerHTML = `<div class="lab-h">Boolean lab <span>Click a variable to flip it.</span></div>
      <div class="lab-row">${vars.map(v => `<button class="lab-tog" data-v="${v}">${v} = <b>true</b></button>`).join("")}</div>
      <div class="lab-table">${exprs.map((e, i) => `<div><code>${esc(e)}</code><b data-e="${i}"></b></div>`).join("")}</div>
      ${p.note ? `<p class="lab-note">${p.note}</p>` : ""}`;
    const val = Object.fromEntries(vars.map(v => [v, true]));
    function upd() {
      el.querySelectorAll(".lab-tog").forEach(b => { b.querySelector("b").textContent = val[b.dataset.v]; b.classList.toggle("off", !val[b.dataset.v]); });
      exprs.forEach((e, i) => {
        const f = new Function(...vars, `return (${e});`);
        const r = f(...vars.map(v => val[v]));
        const b = el.querySelector(`[data-e="${i}"]`); b.textContent = typeof r === "boolean" ? r : r; b.className = r === true ? "t" : r === false ? "f" : "";
      });
    }
    el.querySelectorAll(".lab-tog").forEach(b => b.addEventListener("click", () => { val[b.dataset.v] = !val[b.dataset.v]; upd(); }));
    if (p.nums) {
      // numeric variables for comparisons, e.g. {"x": 5}
      const row = document.createElement("div"); row.className = "lab-row";
      Object.entries(p.nums).forEach(([k, v]) => { row.innerHTML += `<label>int ${k} = <input class="lab-in n" type="number" data-n="${k}" value="${v}"></label>`; vars.push(k); val[k] = v; });
      el.insertBefore(row, el.querySelector(".lab-table"));
      row.querySelectorAll("input").forEach(i => i.addEventListener("input", () => { val[i.dataset.n] = +i.value; upd(); }));
    }
    upd();
  };

  // Java arithmetic with int/double types: + - * / % ( ) casts (int) (double), Math.abs/sqrt/pow
  function javaEval(src) {
    const toks = src.match(/\(\s*(int|double)\s*\)|Math\.(abs|sqrt|pow)|\d+\.\d*|\.\d+|\d+|[-+*/%(),]|\S/g) || [];
    let i = 0;
    const peek = () => toks[i], next = () => toks[i++];
    const I = v => ({ t: "int", v: v | 0 }), D = v => ({ t: "double", v });
    function prim() {
      const k = next();
      if (k === undefined) throw "Expression ends too early";
      if (/^\(\s*int\s*\)$/.test(k)) { const x = prim(); return I(Math.trunc(x.v)); }
      if (/^\(\s*double\s*\)$/.test(k)) { const x = prim(); return D(x.v); }
      if (k === "-") { const x = prim(); return x.t === "int" ? I(-x.v) : D(-x.v); }
      if (k === "+") return prim();
      if (k === "(") { const x = add(); if (next() !== ")") throw "Missing )"; return x; }
      if (k.startsWith("Math.")) {
        if (next() !== "(") throw "Missing ( after " + k;
        const a = add(); let b;
        if (k === "Math.pow") { if (next() !== ",") throw "Math.pow needs two values"; b = add(); }
        if (next() !== ")") throw "Missing )";
        if (k === "Math.abs") return a.t === "int" ? I(Math.abs(a.v)) : D(Math.abs(a.v));
        if (k === "Math.sqrt") return D(Math.sqrt(a.v));
        return D(Math.pow(a.v, b.v));
      }
      if (/^\d+$/.test(k)) { const v = Number(k); if (v > 2147483647) throw "Number too big for int"; return I(v); }
      if (/^[\d.]+$/.test(k)) return D(Number(k));
      throw `Can't read "${k}"`;
    }
    function mul() {
      let x = prim();
      while (["*", "/", "%"].includes(peek())) {
        const op = next(), y = prim();
        if (x.t === "int" && y.t === "int") {
          if ((op === "/" || op === "%") && y.v === 0) throw "ArithmeticException: / by zero";
          x = I(op === "*" ? Math.imul(x.v, y.v) : op === "/" ? Math.trunc(x.v / y.v) : x.v % y.v);
        } else x = D(op === "*" ? x.v * y.v : op === "/" ? x.v / y.v : x.v % y.v);
      }
      return x;
    }
    function add() {
      let x = mul();
      while (["+", "-"].includes(peek())) {
        const op = next(), y = mul();
        x = x.t === "int" && y.t === "int" ? I(op === "+" ? x.v + y.v : x.v - y.v) : D(op === "+" ? x.v + y.v : x.v - y.v);
      }
      return x;
    }
    const r = add();
    if (i < toks.length) throw `Unexpected "${toks[i]}"`;
    return r;
  }
  const showD = v => (Number.isInteger(v) ? v.toFixed(1) : String(v)).replace("Infinity", "Infinity");

  LABS.arith = (el, p) => {
    const ex = p.examples || ["7 / 2", "7 / 2.0", "7 % 3", "(double) 7 / 2", "(double) (7 / 2)", "(int) 3.99", "1 + 2 * 3"];
    el.innerHTML = `<div class="lab-h">Expression lab <span>Type a Java expression with numbers. It follows Java's int and double rules.</span></div>
      <div class="lab-row"><input class="lab-in wide" value="${esc(p.start || ex[0])}" aria-label="Java expression"><b class="lab-out"></b></div>
      <div class="lab-chips">${ex.map(e => `<button class="lab-chip">${esc(e)}</button>`).join("")}</div>`;
    const inp = el.querySelector(".lab-in"), out = el.querySelector(".lab-out");
    function upd() {
      try { const r = javaEval(inp.value); out.classList.remove("bad"); out.innerHTML = `→ ${r.t === "int" ? r.v : showD(r.v)} <small>${r.t}</small>`; }
      catch (e) { out.classList.add("bad"); out.textContent = "→ " + e; }
    }
    inp.addEventListener("input", upd);
    el.querySelectorAll(".lab-chip").forEach(b => b.addEventListener("click", () => { inp.value = b.textContent; upd(); }));
    upd();
  };

  LABS.loop = (el, p) => {
    el.innerHTML = `<div class="lab-h">Loop lab <span>Change the header and watch which values the loop variable takes.</span></div>
      <div class="lab-row code-row">for (int i = <input class="lab-in n" data-k="a" type="number" value="${p.a ?? 0}">; i
        <select class="lab-in" data-k="op"><option>&lt;</option><option>&lt;=</option><option>&gt;</option><option>&gt;=</option><option>!=</option></select>
        <input class="lab-in n" data-k="b" type="number" value="${p.b ?? 5}">; i
        <select class="lab-in" data-k="u"><option value="+=">+=</option><option value="-=">-=</option><option value="*=">*=</option></select>
        <input class="lab-in n" data-k="s" type="number" value="${p.s ?? 1}">)</div>
      <div class="lab-vals"></div><div class="lab-sum"></div>`;
    const g = k => el.querySelector(`[data-k="${k}"]`).value;
    if (p.op) el.querySelector('[data-k="op"]').value = p.op;
    if (p.u) el.querySelector('[data-k="u"]').value = p.u;
    function upd() {
      let i = +g("a"); const b = +g("b"), s = +g("s"), op = g("op"), u = g("u");
      const test = v => (op === "<" ? v < b : op === "<=" ? v <= b : op === ">" ? v > b : op === ">=" ? v >= b : v !== b);
      const vals = []; let guard = 0;
      while (test(i) && guard < 60) { vals.push(i); i = u === "+=" ? i + s : u === "-=" ? i - s : i * s; guard++; }
      el.querySelector(".lab-vals").innerHTML = vals.map((v, k) => `<span style="animation-delay:${k * 40}ms">${v}</span>`).join("") + (guard >= 60 ? '<span class="bad">… never stops (infinite loop)</span>' : "");
      el.querySelector(".lab-sum").innerHTML = guard >= 60 ? "The condition never becomes false." :
        `The body runs <b>${vals.length}</b> time${vals.length === 1 ? "" : "s"}. After the loop, i = <b>${i}</b> (the first value that made the condition false).`;
    }
    el.querySelectorAll(".lab-in").forEach(x => x.addEventListener("input", upd));
    upd();
  };

  LABS.casting = (el, p) => {
    el.innerHTML = `<div class="lab-h">Casting and rounding lab <span>Drag the slider or type a double.</span></div>
      <div class="lab-row"><label>double d = <input class="lab-in n w" type="number" step="0.01" value="${p.d ?? 3.7}"></label><input type="range" min="-10" max="10" step="0.01" value="${p.d ?? 3.7}"></div>
      <div class="lab-table">
        <div><code>(int) d</code><b data-o="a"></b></div>
        <div><code>(int) (d + 0.5)</code><b data-o="b"></b></div>
        <div><code>(int) (d - 0.5)</code><b data-o="c"></b></div>
        <div><code>Math.abs(d)</code><b data-o="d"></b></div></div>
      <p class="lab-note">(int) cuts off the decimal part (toward zero). Adding 0.5 first rounds a positive number to the nearest int; for a negative number, subtract 0.5.</p>`;
    const num = el.querySelector('input[type="number"]'), rng = el.querySelector('input[type="range"]');
    function upd(v) {
      const d = +v;
      el.querySelector('[data-o="a"]').textContent = Math.trunc(d);
      el.querySelector('[data-o="b"]').textContent = Math.trunc(d + 0.5);
      el.querySelector('[data-o="c"]').textContent = Math.trunc(d - 0.5);
      el.querySelector('[data-o="d"]').textContent = showD(Math.abs(d));
    }
    num.addEventListener("input", () => { rng.value = num.value; upd(num.value); });
    rng.addEventListener("input", () => { num.value = rng.value; upd(rng.value); });
    upd(num.value);
  };


  // object playground: call methods on a live object and watch its instance variables
  // {"type":"object","cls":"BankAccount","ctor":"new BankAccount(\"Ana\", 50.0)","fields":{"owner":"\"Ana\"","balance":50.0},
  //  "methods":[{"sig":"deposit(double amount)","ret":"void","params":["amount"],"body":"if (amount > 0) f.balance += amount;"}]}
  LABS.object = (el, p) => {
    const start = JSON.parse(JSON.stringify(p.fields));
    let f = JSON.parse(JSON.stringify(start)), log = [];
    const fmt = v => (typeof v === "number" ? (p.doubles && p.doubles.includes(v) ? v.toFixed(1) : (Number.isInteger(v) && p.dbl ? v.toFixed(1) : String(v))) : String(v));
    el.innerHTML = `<div class="lab-h">Object lab <span>Call methods on a live object. Watch which instance variables change and what each call returns.</span></div>
      <div class="obj-wrap"><div class="obj-card"><div class="obj-cls">${esc(p.cls)} object</div><div class="obj-fields"></div><button class="lab-chip obj-reset">${esc(p.ctor)}</button></div>
      <div class="obj-calls">${p.methods.map((m, i) => `<div class="obj-call"><code>${m.label ? esc(m.label.replace(/\)$/, "")) : esc(p.var || "obj") + "." + esc(m.sig.split("(")[0]) + "("}</code>${(m.params || []).map(pn => `<input class="lab-in n" data-m="${i}" data-p="${pn}" type="${m.str && m.str.includes(pn) ? "text" : "number"}" value="${(m.defaults || {})[pn] ?? 10}" aria-label="${pn}">`).join(", ")}<code>)</code><button class="lab-tog obj-go" data-m="${i}">Call</button><small>${esc(m.ret)}</small></div>`).join("")}</div></div>
      <div class="obj-log"></div>`;
    function draw(changed) {
      el.querySelector(".obj-fields").innerHTML = Object.entries(f).map(([k, v]) => `<div class="${changed && changed.includes(k) ? "chg" : ""}"><span>${p.priv === false ? "" : "private "}${esc(k)}</span><b>${esc(fmt(v))}</b></div>`).join("");
      el.querySelector(".obj-log").innerHTML = log.slice(-5).map(l => `<div>${l}</div>`).join("");
    }
    el.querySelectorAll(".obj-go").forEach(b => b.addEventListener("click", () => {
      const m = p.methods[+b.dataset.m];
      const args = (m.params || []).map(pn => { const inp = el.querySelector(`[data-m="${b.dataset.m}"][data-p="${pn}"]`); return inp.type === "number" ? +inp.value : inp.value; });
      const before = JSON.stringify(f), old = JSON.parse(before);
      let r;
      try { r = new Function("f", ...(m.params || []), m.body)(f, ...args); } catch (e) { r = "error: " + e; }
      const changed = Object.keys(f).filter(k => JSON.stringify(f[k]) !== JSON.stringify(old[k]));
      const call = m.label || `${p.var || "obj"}.${m.sig.split("(")[0]}(${args.map(a => (typeof a === "string" ? `"${a}"` : a)).join(", ")})`;
      log.push(`<code>${esc(call)}</code> ${m.note ? esc(m.note) + " <b>" + esc(fmt(r)) + "</b>" : m.ret === "void" ? "returns nothing" : "returns <b>" + esc(typeof r === "string" && m.ret === "String" ? '"' + r + '"' : fmt(r)) + "</b>"}${changed.length ? ` · changed ${changed.map(esc).join(", ")}` : " · no change to the object"}`);
      draw(changed);
    }));
    el.querySelector(".obj-reset").addEventListener("click", () => { f = JSON.parse(JSON.stringify(start)); log.push(`<code>${esc(p.ctor)}</code> made a fresh object`); draw(Object.keys(f)); });
    draw();
  };


  /* ---------- physics labs (momentum) ---------- */
  const r2 = x => (Math.abs(x) < 1e-9 ? 0 : Math.round(x * 100) / 100);
  function remount(holder, spec) {
    holder.innerHTML = "";
    const d = document.createElement("div"); holder.appendChild(d);
    window.Sims.mount(d, Object.assign({ reveal: true }, spec));
  }
  function sliders(el, defs) {
    return defs.map(([k, lab, min, max, step, v, unit]) =>
      `<label class="sl"><span>${lab}</span><input type="range" data-k="${k}" min="${min}" max="${max}" step="${step}" value="${v}"><b data-v="${k}"></b><small>${unit}</small></label>`).join("");
  }
  LABS.collision = (el, p) => {
    el.innerHTML = `<div class="lab-h">Collision lab <span>Change the masses, velocities and type of collision. The animation reruns with your numbers.</span></div>
      <div class="sl-grid">${sliders(el, [["m1", "m₁", 0.5, 10, 0.5, p.m1 ?? 2, "kg"], ["v1", "v₁", -10, 10, 0.5, p.v1 ?? 5, "m/s"], ["m2", "m₂", 0.5, 10, 0.5, p.m2 ?? 3, "kg"], ["v2", "v₂", -10, 10, 0.5, p.v2 ?? -2, "m/s"]])}</div>
      <div class="lab-row"><label>Type <select class="lab-in" data-k="mode"><option value="stick">Stick together (perfectly inelastic)</option><option value="elastic">Bounce, no energy lost (elastic)</option><option value="given">Inelastic: I choose v₁′</option></select></label>
      <label class="v1f" style="display:none">v₁′ = <input class="lab-in n" type="number" step="0.5" data-k="v1f" value="0"> m/s</label></div>
      <div class="lab-anim"></div><div class="lab-table coll-out"></div>`;
    const g = k => el.querySelector(`[data-k="${k}"]`);
    let timer;
    function upd() {
      const m1 = +g("m1").value, v1 = +g("v1").value, m2 = +g("m2").value, v2 = +g("v2").value, mode = g("mode").value;
      ["m1", "v1", "m2", "v2"].forEach(k => (el.querySelector(`[data-v="${k}"]`).textContent = g(k).value));
      el.querySelector(".v1f").style.display = mode === "given" ? "" : "none";
      const P = m1 * v1 + m2 * v2, K0 = 0.5 * m1 * v1 * v1 + 0.5 * m2 * v2 * v2;
      let a, b;
      if (mode === "stick") a = b = P / (m1 + m2);
      else if (mode === "elastic") { a = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2); b = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2); }
      else { a = +g("v1f").value; b = (P - m1 * a) / m2; }
      const K1 = 0.5 * m1 * a * a + 0.5 * m2 * b * b, closing = v1 > v2;
      const bad = mode === "given" && (K1 > K0 + 1e-9 || a > b + 1e-9);
      el.querySelector(".coll-out").innerHTML =
        `<div><code>Σp before</code><b>${r2(P)} kg·m/s</b></div><div><code>Σp after</code><b>${r2(m1 * a + m2 * b)} kg·m/s</b></div>
         <div><code>v₁′</code><b>${r2(a)} m/s</b></div><div><code>v₂′</code><b>${r2(b)} m/s</b></div>
         <div><code>K before</code><b>${r2(K0)} J</b></div><div><code>K after</code><b class="${K1 < K0 - 1e-9 ? "f" : ""}">${r2(K1)} J</b></div>
         <div><code>K lost</code><b>${K0 > 0 ? r2(100 * (K0 - K1) / K0) : 0}%</b></div>` +
        (!closing ? `<div class="wide"><span class="bad">They never meet: cart 1 isn't catching up to cart 2.</span></div>` : "") +
        (bad ? `<div class="wide"><span class="bad">Not physically possible: ${K1 > K0 + 1e-9 ? "kinetic energy can't increase in a collision" : "cart 1 would pass through cart 2"}.</span></div>` : "");
      clearTimeout(timer);
      if (closing && !bad) timer = setTimeout(() => remount(el.querySelector(".lab-anim"), { type: "collide", m1, v1, m2, v2, mode: mode === "given" ? "given" : mode, v1f: a, v2f: b, o1: p.o1, o2: p.o2 }), 250);
      else el.querySelector(".lab-anim").innerHTML = "";
    }
    el.querySelectorAll("input,select").forEach(i => i.addEventListener("input", upd));
    upd();
  };
  LABS.impulse = (el, p) => {
    el.innerHTML = `<div class="lab-h">Impulse lab <span>A constant force acts on a cart for a time Δt. Impulse is the area under the force–time graph.</span></div>
      <div class="sl-grid">${sliders(el, [["m", "mass", 0.5, 10, 0.5, p.m ?? 2, "kg"], ["v0", "v₀", -10, 10, 0.5, p.v0 ?? 0, "m/s"], ["F", "force", -20, 20, 1, p.F ?? 8, "N"], ["dt", "Δt", 0.5, 5, 0.5, p.dt ?? 2, "s"]])}</div>
      <div class="lab-anim"></div><div class="lab-table imp-out"></div>`;
    const g = k => +el.querySelector(`[data-k="${k}"]`).value;
    let timer;
    function upd() {
      ["m", "v0", "F", "dt"].forEach(k => (el.querySelector(`[data-v="${k}"]`).textContent = el.querySelector(`[data-k="${k}"]`).value));
      const m = g("m"), v0 = g("v0"), F = g("F"), dt = g("dt"), J = F * dt;
      el.querySelector(".imp-out").innerHTML = `<div><code>J = FΔt</code><b>${r2(J)} N·s</b></div><div><code>Δp = J</code><b>${r2(J)} kg·m/s</b></div>
        <div><code>Δv = J/m</code><b>${r2(J / m)} m/s</b></div><div><code>v′ = v₀ + Δv</code><b>${r2(v0 + J / m)} m/s</b></div>`;
      clearTimeout(timer);
      timer = setTimeout(() => { if (F > 0) remount(el.querySelector(".lab-anim"), { type: "graph", kind: "t", pts: [[0, F], [dt, F]], m, v0: Math.max(0, v0) }); else el.querySelector(".lab-anim").innerHTML = '<p class="lab-note">(The animation shows positive forces. The numbers above work for any sign.)</p>'; }, 250);
    }
    el.querySelectorAll("input").forEach(i => i.addEventListener("input", upd));
    upd();
  };
  LABS.stopping = (el, p) => {
    el.innerHTML = `<div class="lab-h">Stopping-time lab <span>Same change in momentum, different stopping times.</span></div>
      <div class="sl-grid">${sliders(el, [["m", "mass", 0.05, 80, 0.05, p.m ?? 70, "kg"], ["v", "speed", 1, 30, 1, p.v ?? 15, "m/s"], ["dt", "stopping time", 0.01, 1, 0.01, p.dt ?? 0.05, "s"]])}</div>
      <div class="stop-bar"><i></i></div><div class="lab-table stop-out"></div>
      <p class="lab-note">Δp is set by the masses and speeds, so it doesn't depend on how the object stops. Stretching Δt (airbags, crumple zones, bending your knees) makes the average force smaller.</p>`;
    const g = k => +el.querySelector(`[data-k="${k}"]`).value;
    function upd() {
      ["m", "v", "dt"].forEach(k => (el.querySelector(`[data-v="${k}"]`).textContent = el.querySelector(`[data-k="${k}"]`).value));
      const dp = g("m") * g("v"), F = dp / g("dt");
      el.querySelector(".stop-out").innerHTML = `<div><code>Δp = mΔv</code><b>${r2(dp)} kg·m/s</b></div><div><code>F = Δp/Δt</code><b>${Math.round(F).toLocaleString()} N</b></div><div><code>F vs. weight mg</code><b>${r2(F / (g("m") * 10))} × mg</b></div>`;
      el.querySelector(".stop-bar i").style.width = Math.min(100, (Math.log10(Math.max(F, 1)) / 6) * 100) + "%";
    }
    el.querySelectorAll("input").forEach(i => i.addEventListener("input", upd));
    upd();
  };


  LABS.balance = (el, p) => {
    el.innerHTML = `<div class="lab-h">Balance lab <span>Move two masses on a beam (pivot in the middle). Make the torques cancel.</span></div>
      <div class="sl-grid">${sliders(el, [["m1", "m₁", 0.5, 5, 0.5, p.m1 ?? 2, "kg"], ["x1", "m₁ position", -2.5, 0, 0.25, p.x1 ?? -1, "m"], ["m2", "m₂", 0.5, 5, 0.5, p.m2 ?? 1, "kg"], ["x2", "m₂ position", 0, 2.5, 0.25, p.x2 ?? 1.5, "m"]])}</div>
      <div class="lab-anim"></div><div class="lab-table bal-out"></div>`;
    const g = k => +el.querySelector(`[data-k="${k}"]`).value; let timer;
    function upd() {
      ["m1", "x1", "m2", "x2"].forEach(k => (el.querySelector(`[data-v="${k}"]`).textContent = el.querySelector(`[data-k="${k}"]`).value));
      const m1 = g("m1"), x1 = g("x1"), m2 = g("m2"), x2 = g("x2"), t1 = -m1 * 10 * x1, t2 = -m2 * 10 * x2, need = m1 * Math.abs(x1) / m2;
      el.querySelector(".bal-out").innerHTML = `<div><code>τ₁ = m₁g·d₁ (ccw)</code><b>${r2(t1)} N·m</b></div><div><code>τ₂ = m₂g·d₂ (cw)</code><b>${r2(t2)} N·m</b></div>
        <div><code>Στ</code><b>${r2(t1 + t2)} N·m</b></div><div><code>balances when x₂ =</code><b>${need <= 2.5 ? r2(need) + " m" : "off the beam"}</b></div>`;
      clearTimeout(timer); timer = setTimeout(() => remount(el.querySelector(".lab-anim"), { type: "seesaw", objs: [[m1, x1], [m2, x2]] }), 200);
    }
    el.querySelectorAll("input").forEach(i => i.addEventListener("input", upd)); upd();
  };
  LABS.torquelab = (el, p) => {
    el.innerHTML = `<div class="lab-h">Torque lab <span>Push a door. Change where you push, how hard, and at what angle.</span></div>
      <div class="sl-grid">${sliders(el, [["r", "distance from hinge r", 0.1, 1, 0.05, p.r ?? 0.8, "m"], ["F", "force F", 0, 40, 1, p.F ?? 20, "N"], ["ang", "angle θ", 0, 180, 5, p.ang ?? 90, "°"]])}</div>
      <div class="lab-anim"></div><div class="lab-table tq-out"></div>`;
    const g = k => +el.querySelector(`[data-k="${k}"]`).value; let timer;
    function upd() {
      ["r", "F", "ang"].forEach(k => (el.querySelector(`[data-v="${k}"]`).textContent = el.querySelector(`[data-k="${k}"]`).value));
      const r = g("r"), F = g("F"), a = g("ang") * Math.PI / 180, tau = r * F * Math.sin(a);
      el.querySelector(".tq-out").innerHTML = `<div><code>sin θ</code><b>${r2(Math.sin(a))}</b></div><div><code>r⊥ = r sin θ</code><b>${r2(r * Math.sin(a))} m</b></div><div><code>τ = rF sin θ</code><b>${r2(tau)} N·m</b></div>`;
      clearTimeout(timer); timer = setTimeout(() => remount(el.querySelector(".lab-anim"), { type: "torque", r, F, ang: g("ang") }), 200);
    }
    el.querySelectorAll("input").forEach(i => i.addEventListener("input", upd)); upd();
  };
  LABS.spinlab = (el, p) => {
    el.innerHTML = `<div class="lab-h">Rotational inertia lab <span>A hanging mass unwinds a string from a hoop and a solid disk with the same mass and radius.</span></div>
      <div class="sl-grid">${sliders(el, [["m", "hanging mass m", 0.2, 5, 0.1, p.m ?? 1, "kg"], ["M", "wheel mass M", 0.5, 10, 0.5, p.M ?? 2, "kg"], ["R", "wheel radius R", 0.05, 0.5, 0.05, p.R ?? 0.2, "m"]])}</div>
      <div class="lab-anim"></div><div class="lab-table sp-out"></div>
      <p class="lab-note">Newton's second law for each piece: mg − T = ma for the hanging mass and TR = Iα for the wheel, with a = αR. Solving gives a = mg / (m + I/R²).</p>`;
    const g = k => +el.querySelector(`[data-k="${k}"]`).value; let timer;
    function upd() {
      ["m", "M", "R"].forEach(k => (el.querySelector(`[data-v="${k}"]`).textContent = el.querySelector(`[data-k="${k}"]`).value));
      const m = g("m"), M = g("M"), R = g("R"), a1 = m * 10 / (m + M), a2 = m * 10 / (m + M / 2);
      el.querySelector(".sp-out").innerHTML = `<div><code>hoop: I = MR²</code><b>a = ${r2(a1)} m/s²</b></div><div><code>disk: I = ½MR²</code><b>a = ${r2(a2)} m/s²</b></div><div><code>tension (disk) T = m(g − a)</code><b>${r2(m * (10 - a2))} N</b></div>`;
      clearTimeout(timer); timer = setTimeout(() => remount(el.querySelector(".lab-anim"), { type: "spin", m, M, R }), 200);
    }
    el.querySelectorAll("input").forEach(i => i.addEventListener("input", upd)); upd();
  };

  function mountLabs(root) {
    (root || document).querySelectorAll(".cslab[data-lab]").forEach(el => {
      if (el.dataset.mounted) return; el.dataset.mounted = 1;
      try { const p = JSON.parse(el.dataset.lab); LABS[p.type] && LABS[p.type](el, p); } catch (e) { console.error(e); }
    });
  }
  window.CSLabs = { mountAll: mountLabs, javaEval };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", () => mountLabs());
  else mountLabs();
})();
