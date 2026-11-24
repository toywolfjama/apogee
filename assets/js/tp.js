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
    examHero();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", mount); else mount();
})();
