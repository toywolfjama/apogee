/* ===== Apogee — practice exam engine =====
   <div class="exam" data-src="exam-data"></div>
   <script type="application/json" id="exam-data">
   { "title": "...",
     "mcqMinutes": 40, "frqMinutes": 30,
     "mcq": [ {"t":"e","k":"concept"|"calc","q":"...","o":["A","B","C","D"],"a":0,"x":"explanation"} ],
     "frq": [ {"q":"setup text", "parts":[ {"p":"(a) ...", "rubric":[["point description", 1], ...], "answer":"model answer"} ]} ],
     "tags": {"e":"Energy","m":"Momentum"} }
   </script>
   Animated models are never shown during an exam. */
(function () {
  const L = j => String.fromCharCode(65 + j);
  /* grid-in (student-produced response): item has g: ["3/2", "1.5"] instead of o */
  const num = v => { v = String(v).replace(/\s+/g, "").replace(/−/g, "-"); const f = v.match(/^(-?\d*\.?\d+)\/(-?\d*\.?\d+)$/); return f ? +f[1] / +f[2] : (v === "" ? NaN : +v); };
  const gridOk = (v, g) => v !== undefined && v !== null && String(v).trim() !== "" && g.some(x => String(x).replace(/\s+/g, "") === String(v).replace(/\s+/g, "") || (isFinite(num(v)) && Math.abs(num(v) - num(x)) < 1e-3 * Math.max(1, Math.abs(num(x)))));
  const isOk = (q, a) => q.g ? gridOk(a, q.g) : a === q.a;
  window.GridCheck = { gridOk, isOk };
  const timed = () => !document.body.classList.contains("no-timer");
  const mmss = s => { s = Math.max(0, Math.round(s)); return String(Math.floor(s / 60)).padStart(2, "0") + ":" + String(s % 60).padStart(2, "0"); };

  function mountExam(box) {
    let E;
    try { E = JSON.parse(document.getElementById(box.dataset.src).textContent); } catch (e) { return; }
    const nM = E.mcq.length, nF = (E.frq || []).length;
    const frqPts = (E.frq || []).reduce((s, f) => s + f.parts.reduce((a, p) => a + p.rubric.reduce((b, r) => b + r[1], 0), 0), 0);
    let st;
    const reset = () => (st = { phase: "intro", cur: 0, ans: {}, flag: {}, frq: {}, rub: {}, end: 0, timer: null, mcqUsed: 0 });
    reset();

    function stopTimer() { if (st.timer) clearInterval(st.timer); st.timer = null; }
    function startTimer(minutes, onEnd) {
      stopTimer();
      st.end = Date.now() + minutes * 60000;
      st.start = Date.now();
      const tick = () => {
        if (!timed()) { st.end = Date.now() + st.left * 1000; return; }
        const left = (st.end - Date.now()) / 1000;
        st.left = left;
        const el = box.querySelector(".ex-timer");
        if (el) { el.textContent = mmss(left); el.classList.toggle("low", left < 300); }
        if (left <= 0) { stopTimer(); onEnd(true); }
      };
      st.left = minutes * 60;
      tick(); st.timer = setInterval(tick, 500);
    }
    function guard(on) { window.onbeforeunload = on ? () => "Your exam is in progress." : null; }
    function top() { const y = box.getBoundingClientRect().top + scrollY - 140; if (Math.abs(scrollY - y) > 60) scrollTo({ top: y, behavior: "smooth" }); }

    function intro() {
      stopTimer(); guard(false);
      box.innerHTML = `
        <div class="ex-intro">
          <div class="ex-badge">Practice exam</div>
          <h3>${E.title || "Practice exam"}</h3>
          <div class="ex-sections">
            ${nM ? `<div><b>${E.mcqName || "Section I"}</b><span>${nM} ${E.mcqKind || "multiple choice"}</span><span>${timed() ? E.mcqMinutes + " minutes" : "Untimed"}</span></div>` : ""}
            ${nF ? `<div><b>${E.frqName || "Section II"}</b><span>${nF} ${E.frqKind || "free response"}</span><span>${timed() ? E.frqMinutes + " minutes" : "Untimed"}</span></div>` : ""}
          </div>
          <ul>${(E.rules || (document.body.classList.contains("th-space") ? ["Mix of conceptual and calculation questions, like the real exam.", "No feedback until you submit. You can flag questions and come back to them.", "Calculator and the AP equation sheet are allowed. Use g = 10 m/s².", "Animated models are hidden during the exam."] : ["No feedback until you submit. You can flag questions and come back to them.", "Work it out on paper first, then pick your answer."])).map(r => `<li>${r}</li>`).join("")}${timed() ? "<li>The timer keeps running if you switch chapters.</li>" : ""}</ul>
          <button class="navbtn solid ex-start">Start exam</button>
        </div>`;
      box.querySelector(".ex-start").onclick = () => { guard(true); if (!nM) { st.phase = "frq"; startTimer(E.frqMinutes, endFrq); frq(); top(); return; } st.phase = "mcq"; startTimer(E.mcqMinutes, endMcq); mcq(); top(); };
    }

    function head(label, count) {
      return `<div class="ex-head"><span class="ex-sec">${label}</span><span class="ex-count">${count}</span><span class="ex-timer">--:--</span></div>`;
    }

    function mcq() {
      const i = st.cur, it = E.mcq[i];
      const done = Object.keys(st.ans).length;
      box.innerHTML = head(E.mcqName || "Section I · Multiple choice", `${done} of ${nM} answered`) + `
        <div class="ex-nav">${E.mcq.map((_, k) => `<button class="ex-dot${k === i ? " cur" : ""}${st.ans[k] !== undefined ? " done" : ""}${st.flag[k] ? " flag" : ""}" data-k="${k}" aria-label="Question ${k + 1}">${k + 1}</button>`).join("")}</div>
        <div class="ex-q">
          <div class="qh"><span>Question ${i + 1} of ${nM}</span><button class="linkbtn ex-flag">${st.flag[i] ? "★ Flagged" : "☆ Flag for review"}</button></div>
          <div class="qt">${it.q}</div>
          ${it.g ? `<div class="grid-in"><label>Your answer <input type="text" inputmode="decimal" autocomplete="off" value="${st.ans[i] !== undefined ? String(st.ans[i]).replace(/"/g, "&quot;") : ""}" aria-label="Your answer"></label><span>Type a number or fraction like 3/4. Don't type units.</span></div>` : `<div class="opts">${it.o.map((o, j) => `<button class="opt${st.ans[i] === j ? " picked" : ""}" data-j="${j}">${L(j)}. ${o}</button>`).join("")}</div>`}
        </div>
        <div class="ex-foot">
          <button class="btn ex-prev"${i === 0 ? " disabled" : ""}>← Previous</button>
          ${i < nM - 1 ? `<button class="btn ex-next">Next →</button>` : `<button class="navbtn solid ex-submit">Submit section</button>`}
        </div>`;
      box.querySelectorAll(".ex-dot").forEach(b => (b.onclick = () => { st.cur = +b.dataset.k; mcq(); }));
      box.querySelectorAll(".opt").forEach(b => (b.onclick = () => { st.ans[i] = +b.dataset.j; mcq(); }));
      const gi = box.querySelector(".grid-in input");
      if (gi) gi.oninput = () => { if (gi.value.trim() === "") delete st.ans[i]; else st.ans[i] = gi.value.trim(); const d = box.querySelector(`.ex-dot[data-k="${i}"]`); if (d) d.classList.toggle("done", st.ans[i] !== undefined); const c = box.querySelector(".ex-count"); if (c) c.textContent = `${Object.keys(st.ans).length} of ${nM} answered`; };
      box.querySelector(".ex-flag").onclick = () => { st.flag[i] = !st.flag[i]; mcq(); };
      const pv = box.querySelector(".ex-prev"); if (pv) pv.onclick = () => { st.cur--; mcq(); };
      const nx = box.querySelector(".ex-next"); if (nx) nx.onclick = () => { st.cur++; mcq(); };
      const sb = box.querySelector(".ex-submit"); if (sb) sb.onclick = () => confirmBox(endMcq);
      const t = box.querySelector(".ex-timer"); if (t) t.textContent = mmss((st.end - Date.now()) / 1000);
      box.querySelectorAll(".ex-q .opt").forEach((b, j) => { b.innerHTML = `<span class="key">${L(j)}</span><span class="ot">` + b.innerHTML.replace(/^[A-Z]\. /, "") + "</span>"; });
    }
    document.addEventListener("keydown", e => {
      if (st.phase !== "mcq" || e.metaKey || e.ctrlKey || e.altKey || /INPUT|TEXTAREA/.test(e.target.tagName || "")) return;
      const r = box.getBoundingClientRect(); if (r.bottom < 0 || r.top > innerHeight) return;
      const k = e.key.toLowerCase(), j = "abcd".indexOf(k);
      if (j >= 0) { const b = box.querySelectorAll(".ex-q .opt")[j]; if (b) { e.preventDefault(); b.click(); } }
      else if (e.key === "ArrowRight" && st.cur < nM - 1) { e.preventDefault(); st.cur++; mcq(); }
      else if (e.key === "ArrowLeft" && st.cur > 0) { e.preventDefault(); st.cur--; mcq(); }
    });

    function confirmBox(go) {
      const left = nM - Object.keys(st.ans).length, flagged = Object.values(st.flag).filter(Boolean).length;
      const d = document.createElement("div");
      d.className = "ex-confirm";
      d.innerHTML = `<p><b>Submit Section I?</b> ${left ? `${left} question${left > 1 ? "s are" : " is"} unanswered. ` : ""}${flagged ? `${flagged} flagged. ` : ""}You can't change answers after submitting.</p>
        <button class="navbtn solid">Submit</button> <button class="btn">Keep working</button>`;
      box.querySelector(".ex-foot").after(d);
      d.querySelector(".navbtn").onclick = () => go(false);
      d.querySelector(".btn").onclick = () => d.remove();
    }

    function endMcq(timeUp) {
      st.mcqUsed = (Date.now() - st.start) / 1000;
      if (nF) { st.phase = "frq"; st.timeUpMcq = timeUp; startTimer(E.frqMinutes, endFrq); frq(); }
      else endFrq(false);
      top();
    }

    function frq() {
      box.innerHTML = head(E.frqName || "Section II · Free response", st.timeUpMcq ? "Section I time ran out" : "") +
        E.frq.map((f, i) => `<div class="ex-frq"><div class="qh"><span>Question ${i + 1}</span></div><div class="qt">${f.q}</div>
          ${f.parts.map((p, j) => `<div class="ex-part"><div>${p.p}</div><textarea data-k="${i}-${j}" rows="4" placeholder="Show your work and reasoning...">${st.frq[i + "-" + j] || ""}</textarea></div>`).join("")}</div>`).join("") +
        `<div class="ex-foot"><span></span><button class="navbtn solid ex-done">Submit exam</button></div>`;
      box.querySelectorAll("textarea").forEach(t => (t.oninput = () => (st.frq[t.dataset.k] = t.value)));
      box.querySelector(".ex-done").onclick = () => endFrq(false);
    }

    function endFrq(timeUp) {
      stopTimer(); guard(false); st.phase = "results"; st.timeUpFrq = timeUp; results(); top();
    }

    function results() {
      if (!st.recorded && window.Crux) { st.recorded = 1; E.mcq.forEach((q, i) => { if (st.ans[i] !== undefined) window.Crux.record(q, isOk(q, st.ans[i])); }); }
      const right = E.mcq.filter((q, i) => isOk(q, st.ans[i])).length;
      const groups = {};
      E.mcq.forEach((q, i) => {
        [E.tags && E.tags[q.t], q.k === "concept" ? "Conceptual" : q.k === "calc" ? "Calculation" : null].forEach(g => {
          if (!g) return; groups[g] = groups[g] || [0, 0]; groups[g][1]++; if (isOk(q, st.ans[i])) groups[g][0]++;
        });
      });
      const rubPts = () => Object.entries(st.rub).reduce((s, [k, v]) => s + (v ? +k.split("|")[1] : 0), 0);
      const pct = nM ? Math.round((right / nM) * 100) : 0;
      box.innerHTML = `
        <div class="ex-result">
          <div class="ex-badge">Results</div>
          ${nM ? `<div class="ex-score"><span class="big">${right}<small>/${nM}</small></span><span>${E.mcqName || "Section I"} · ${pct}%</span></div>` : ""}
          ${nF ? `<div class="ex-score"><span class="big frqpts">0<small>/${frqPts}</small></span><span>${E.frqName || "Section II"} · check the rubric below</span></div>` : ""}
          <div class="ex-groups">${Object.entries(groups).map(([g, [a, b]]) => `<div><span>${g}</span><div class="bar"><i style="width:${(a / b) * 100}%"></i></div><b>${a}/${b}</b></div>`).join("")}</div>
          ${nM ? `<p class="sub">${timed() ? `Time used: ${mmss(st.mcqUsed)}. ` : ""}${pct >= 80 ? "Strong result. Try the harder questions next." : pct >= 60 ? "Solid. Review the questions you missed below." : "Review the explanations below, then revisit those chapters."}</p>` : ""}
          <button class="btn ex-again">Retake exam</button>
        </div>
        ${nM ? `<h3 class="ex-h">${E.mcqName || "Section I"} review</h3>` : ""}
        ${E.mcq.map((q, i) => {
          const a = st.ans[i], ok = isOk(q, a);
          return `<div class="qcard ex-rev ${ok ? "ok" : "no"}"><div class="qh"><span>Question ${i + 1} · ${ok ? "Correct" : a === undefined ? "Unanswered" : "Incorrect"}</span><span>${(E.kinds && E.kinds[q.k]) || (E.tags && E.tags[q.t]) || (q.k === "concept" ? "Conceptual" : "Calculation")}</span></div>
            <div class="qt">${q.q}</div>
            ${q.g ? `<div class="grid-in rev"><span>Your answer: <b>${a === undefined ? "—" : String(a).replace(/</g, "&lt;")}</b></span><span>Accepted: <b>${q.g.join(" or ")}</b></span></div>` : `<div class="opts">${q.o.map((o, j) => `<div class="opt${j === q.a ? " right" : j === a ? " wrong" : ""}"><span class="key">${L(j)}</span><span class="ot">${o}</span></div>`).join("")}</div>`}
            <div class="expl show">${q.x}</div></div>`;
        }).join("")}
        ${nF ? `<h3 class="ex-h">${E.frqName || "Section II"}: score yourself</h3><p class="sub">Compare your answer to the model answer and tick each point you earned.</p>` +
          E.frq.map((f, i) => `<div class="qcard"><div class="qh"><span>Question ${i + 1}</span></div><div class="qt">${f.q}</div>
            ${f.parts.map((p, j) => `<div class="ex-part"><div>${p.p}</div>
              <div class="ex-yours"><b>Your answer</b><div>${st.frq[i + "-" + j] ? st.frq[i + "-" + j].replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/\n/g, "<br>") : "<i>No answer</i>"}</div></div>
              <div class="ex-model"><b>Model answer</b><div>${p.answer}</div></div>
              <div class="ex-rubric">${p.rubric.map((r, k) => `<label><input type="checkbox" data-r="${i}-${j}-${k}|${r[1]}"> ${r[0]} <em>${r[1]} pt${r[1] > 1 ? "s" : ""}</em></label>`).join("")}</div>
            </div>`).join("")}</div>`).join("") : ""}`;
      box.querySelector(".ex-again").onclick = () => { reset(); intro(); top(); };
      if (window.CruxPen) box.querySelectorAll(".ex-rev").forEach((c, ii) => { const q = E.mcq[ii]; if (q && !q.g) window.CruxPen([...c.querySelectorAll(".opt")], q.a, st.ans[ii]); });
      box.querySelectorAll(".ex-rubric input").forEach(c => (c.onchange = () => {
        st.rub[c.dataset.r] = c.checked;
        box.querySelector(".frqpts").innerHTML = rubPts() + `<small>/${frqPts}</small>`;
      }));
    }

    intro();
    document.addEventListener("chapterchange", () => { if (st.phase === "intro") intro(); });
  }
  document.querySelectorAll(".exam[data-src]").forEach(mountExam);
})();
