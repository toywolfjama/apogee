/* Shared word / symbol tile animation: tiles glide along curved paths, new ones drop in, removed ones fade out where they were. */
(function () {
  "use strict";
  const esc = s => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  const reduce = () => document.body.classList.contains("no-motion") || matchMedia("(prefers-reduced-motion: reduce)").matches;
  function render(el, row, frames, k, animate, noteEl, dots, prevIdx) {
    const stage = row.parentElement;
    const old = {}, oldTxt = {};
    const doAnim = animate && !reduce();
    if (doAnim) row.querySelectorAll(".wt").forEach(t => { old[t.dataset.id] = { r: t.getBoundingClientRect(), el: t }; oldTxt[t.dataset.id] = t.textContent; });
    const f = frames[k];
    row.innerHTML = f.t.map(([id, txt, cls]) => `<span class="wt ${cls || ""}" data-id="${esc(id)}">${esc(txt)}</span>`).join("");
    if (noteEl) { noteEl.innerHTML = f.note; if (doAnim) noteEl.animate([{ opacity: 0, transform: "translateY(6px)" }, { opacity: 1, transform: "none" }], { duration: 380, easing: "ease-out" }); }
    if (dots) dots.forEach((d, j) => { d.classList.toggle("on", j <= k); d.classList.toggle("cur", j === k); });
    const next = el.querySelector('[data-a="next"]'); if (next) next.textContent = k === frames.length - 1 ? "Replay ↺" : "Step ▶";
    if (!doAnim) return;
    const sr = stage.getBoundingClientRect(), seen = new Set();
    row.querySelectorAll(".wt").forEach((t, j) => {
      const id = t.dataset.id; seen.add(id);
      const o = old[id], n = t.getBoundingClientRect();
      if (o) {
        const dx = o.r.left - n.left, dy = o.r.top - n.top, sx = o.r.width / n.width;
        if (Math.abs(dx) > 2 || Math.abs(dy) > 2) {
          const lift = Math.min(46, 14 + Math.abs(dx) * 0.18);
          t.animate([{ transform: `translate(${dx}px,${dy}px) scaleX(${sx})`, zIndex: 2 },
            { transform: `translate(${dx * 0.45}px,${dy * 0.45 - lift}px) scale(1.08)`, offset: 0.45, zIndex: 2 },
            { transform: "none" }], { duration: 640, easing: "cubic-bezier(.3,.7,.25,1)" });
        } else if (Math.abs(sx - 1) > 0.02) t.animate([{ transform: `scaleX(${sx})` }, { transform: "none" }], { duration: 400, easing: "ease-out" });
        if (oldTxt[id] !== t.textContent) t.animate([{ boxShadow: "0 0 0 0 rgba(234,179,8,.0)", filter: "brightness(1.25)" }, { boxShadow: "0 0 0 6px rgba(234,179,8,.35)", offset: 0.4 }, { boxShadow: "0 0 0 0 rgba(234,179,8,0)", filter: "none" }], { duration: 700 });
      } else {
        t.animate([{ opacity: 0, transform: "translateY(-26px) scale(.6) rotate(-6deg)" }, { opacity: 1, transform: "translateY(4px) scale(1.04)", offset: 0.7 }, { opacity: 1, transform: "none" }],
          { duration: 560, delay: 180 + j * 40, easing: "cubic-bezier(.2,.9,.3,1.2)", fill: "backwards" });
      }
    });
    // ghosts for removed tiles
    Object.entries(old).forEach(([id, o]) => {
      if (seen.has(id)) return;
      const g = o.el.cloneNode(true); g.classList.add("wt-ghost");
      Object.assign(g.style, { position: "absolute", left: (o.r.left - sr.left) + "px", top: (o.r.top - sr.top) + "px", width: o.r.width + "px", margin: 0, pointerEvents: "none" });
      stage.appendChild(g);
      g.animate([{ opacity: 1, transform: "none" }, { opacity: 0, transform: "translateY(22px) scale(.7) rotate(5deg)" }], { duration: 480, easing: "ease-in", fill: "forwards" }).onfinish = () => g.remove();
    });
  }
  window.WA = { render };
})();
