/* Flashcards with spaced repetition (Anki-style scheduling). Progress lives in localStorage. */
(function () {
  "use strict";
  const KEY = "apogee-srs-v1";
  const MIN = 60e3, DAY = 864e5;
  const LEARN = [1, 10], RELEARN = [10];          // steps in minutes
  const esc = s => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  const fmt = s => esc(s).replace(/`([^`]+)`/g, "<code>$1</code>");
  const reduce = () => document.body.classList.contains("no-motion") || matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- storage ---------- */
  let S;
  function load() {
    try { S = JSON.parse(localStorage.getItem(KEY)) || {}; } catch (e) { S = {}; }
    S.cards = S.cards || {}; S.days = S.days || {}; S.custom = S.custom || []; S.settings = S.settings || {};
  }
  function save() { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) { } }
  load();

  // a "day" starts at 4 a.m. local time, like Anki
  function dayKey(t = Date.now()) { const d = new Date(t - 4 * 3600e3); return d.getFullYear() + "-" + (d.getMonth() + 1) + "-" + d.getDate(); }
  function dayEnd() { const d = new Date(Date.now() - 4 * 3600e3); d.setHours(24, 0, 0, 0); return d.getTime() + 4 * 3600e3; }
  function today() { const k = dayKey(); return (S.days[k] = S.days[k] || { n: {}, r: 0 }); }

  /* ---------- decks ---------- */
  const DECKS = (window.DECKS || []).slice();
  function customDeck() { return { id: "mine", name: "My cards", sub: "Cards you add yourself", kind: "plain", cards: S.custom }; }
  function allDecks() { return [...DECKS, customDeck()]; }
  const cid = (d, c) => d.id + "::" + c.id;
  function newPerDay(d) { return S.settings[d.id]?.newPerDay ?? (d.id === "mine" ? 50 : 20); }

  function counts(d) {
    const now = Date.now(), end = dayEnd(), t = today();
    let nw = 0, lrn = 0, rev = 0;
    d.cards.forEach(c => {
      const st = S.cards[cid(d, c)];
      if (!st) nw++;
      else if (st.s === "learn" || st.s === "relearn") { if (st.due <= now + 20 * MIN) lrn++; }
      else if (st.due <= end) rev++;
    });
    const left = Math.max(0, newPerDay(d) - (t.n[d.id] || 0));
    return { nw: Math.min(nw, left), lrn, rev, totalNew: nw };
  }

  /* ---------- scheduling ---------- */
  function preview(st, g) {
    // returns the next state for grade g (1 again, 2 hard, 3 good, 4 easy)
    const now = Date.now();
    st = st ? { ...st } : { s: "new", step: 0, ivl: 0, ease: 2.5, reps: 0, lapses: 0 };
    if (st.s === "new" || st.s === "learn") {
      const steps = LEARN;
      if (g === 1) { st.s = "learn"; st.step = 0; st.due = now + steps[0] * MIN; }
      else if (g === 2) { st.s = "learn"; st.due = now + (st.step === 0 ? (steps[0] + (steps[1] || steps[0])) / 2 : steps[st.step]) * MIN; }
      else if (g === 3) {
        if (st.step + 1 >= steps.length) { st.s = "review"; st.ivl = 1; st.due = now + DAY; }
        else { st.s = "learn"; st.step++; st.due = now + steps[st.step] * MIN; }
      } else { st.s = "review"; st.ivl = 4; st.due = now + 4 * DAY; }
    } else if (st.s === "relearn") {
      if (g === 1) { st.step = 0; st.due = now + RELEARN[0] * MIN; }
      else if (g === 2) { st.due = now + RELEARN[0] * 1.5 * MIN; }
      else { st.s = "review"; if (g === 4) st.ivl += 1; st.due = now + st.ivl * DAY; }
    } else {
      const ivl = st.ivl || 1;
      if (g === 1) { st.lapses++; st.ease = Math.max(1.3, st.ease - 0.2); st.s = "relearn"; st.step = 0; st.ivl = Math.max(1, Math.round(ivl * 0.5)); st.due = now + RELEARN[0] * MIN; }
      else if (g === 2) { st.ease = Math.max(1.3, st.ease - 0.15); st.ivl = Math.max(ivl + 1, Math.round(ivl * 1.2)); }
      else if (g === 3) { st.ivl = Math.max(ivl + 1, Math.round(ivl * st.ease)); }
      else { st.ease += 0.15; st.ivl = Math.max(ivl + 1, Math.round(ivl * st.ease * 1.3)); }
      if (g > 1) st.due = now + st.ivl * DAY;
    }
    st.reps++; return st;
  }
  function human(ms) {
    const m = ms / MIN;
    if (m < 60) return Math.max(1, Math.round(m)) + "m";
    if (m < 1440) return Math.round(m / 60) + "h";
    const d = m / 1440;
    if (d < 30) return Math.round(d) + "d";
    if (d < 365) return (d / 30).toFixed(1).replace(/\.0$/, "") + "mo";
    return (d / 365).toFixed(1).replace(/\.0$/, "") + "y";
  }

  /* ---------- card faces ---------- */
  function faces(d, c) {
    const say = t => `<button type="button" class="fc-say" data-say="${esc(t.replace(/\(.*?\)/g, ""))}" aria-label="Hear it"></button>`;
    if (d.kind === "frword") return { front: `<div class="fc-big" lang="fr">${esc(c.f)}</div><div class="fc-tag">${esc(c.t)}</div>${say(c.f)}`, back: `<div class="fc-ans">${esc(c.b)}</div>`, sayFront: c.f };
    if (d.kind === "frword-rev") return { front: `<div class="fc-big">${esc(c.f)}</div><div class="fc-tag">${esc(c.t)}</div>`, back: `<div class="fc-ans fc-big" lang="fr">${esc(c.b)}</div>${say(c.b)}`, sayBack: c.b };
    if (d.kind === "frverb") {
      const F = window.FR && window.FR.conj ? window.FR.conj(c.v, c.tense) : [];
      const rows = [0, 3, 5].map(i => F[i] || "").filter(Boolean);
      return { front: `<div class="fc-big" lang="fr">${esc(c.v)}</div><div class="fc-tag">${esc(c.tn)} · je, nous, ils</div>`,
        back: `<div class="fc-conj" lang="fr">${rows.map(r => `<div>${esc(r)}</div>`).join("")}</div>${say(rows.join(", "))}`, sayBack: rows.join(", ") };
    }
    return { front: `<div class="fc-q">${fmt(c.f)}</div>`, back: `<div class="fc-ans">${fmt(c.b)}</div>` };
  }

  /* ---------- UI ---------- */
  const app = document.getElementById("srs");
  let view = "decks", deck = null, cur = null, shown = false, undo = null, sessionN = 0;

  function streak() {
    let n = 0; const t = new Date(Date.now() - 4 * 3600e3);
    for (; ; ) { const k = t.getFullYear() + "-" + (t.getMonth() + 1) + "-" + t.getDate(); const d = S.days[k]; if (d && (d.r > 0)) { n++; t.setDate(t.getDate() - 1); } else break; }
    return n;
  }
  function renderDecks() {
    view = "decks";
    const t = today(), st = streak();
    const tomorrow = allDecks().reduce((a, d) => a + d.cards.filter(c => { const s = S.cards[cid(d, c)]; return s && s.s === "review" && s.due > dayEnd() && s.due <= dayEnd() + DAY; }).length, 0);
    const learned = Object.keys(S.cards).length;
    app.innerHTML = `
      <div class="srs-stats"><div><b>${t.r}</b><span>reviewed today</span></div><div><b>${st}</b><span>day streak</span></div><div><b>${learned}</b><span>cards started</span></div><div><b>${tomorrow}</b><span>due tomorrow</span></div></div>
      <div class="srs-table" role="table">
        <div class="srs-row head" role="row"><span>Deck</span><span class="c-n">New</span><span class="c-l">Learn</span><span class="c-r">Due</span><span></span></div>
        ${allDecks().map(d => { const c = counts(d); return `<div class="srs-row" role="row">
          <button type="button" class="srs-deck" data-open="${d.id}"><b>${esc(d.name)}</b><span>${esc(d.sub)} · ${d.cards.length} cards</span></button>
          <span class="c-n">${c.nw}</span><span class="c-l">${c.lrn}</span><span class="c-r">${c.rev}</span>
          <button type="button" class="srs-gear" data-set="${d.id}" aria-label="Deck options">⋯</button></div>`; }).join("")}
      </div>
      <div class="srs-tools">
        <button type="button" class="srs-btn" data-act="add">+ Add a card</button>
        <button type="button" class="srs-btn" data-act="export">Export progress</button>
        <label class="srs-btn">Import progress<input type="file" accept="application/json" data-act="import" hidden></label>
        <label class="srs-toggle"><input type="checkbox" data-auto${S.settings.autoAudio ? " checked" : ""}> Auto-play audio</label>
      </div>
      <div class="srs-panel" hidden></div>
      <p class="srs-note">Your progress is saved in this browser only. Use <b>Export</b> to back it up or move it to another device, and <b>Import</b> to load it there.</p>`;
  }
  function panel(html) { const p = app.querySelector(".srs-panel"); p.hidden = false; p.innerHTML = html; p.scrollIntoView({ behavior: reduce() ? "auto" : "smooth", block: "nearest" }); return p; }

  function nextCard() {
    const now = Date.now(), end = dayEnd(), t = today();
    const st = c => S.cards[cid(deck, c)];
    const learning = deck.cards.filter(c => { const s = st(c); return s && (s.s === "learn" || s.s === "relearn") && s.due <= now; }).sort((a, b) => st(a).due - st(b).due);
    if (learning.length) return learning[0];
    const due = deck.cards.filter(c => { const s = st(c); return s && s.s === "review" && s.due <= end; }).sort((a, b) => st(a).due - st(b).due);
    if (due.length) return due[0];
    if ((t.n[deck.id] || 0) < newPerDay(deck)) { const nw = deck.cards.find(c => !st(c)); if (nw) return nw; }
    const soon = deck.cards.filter(c => { const s = st(c); return s && (s.s === "learn" || s.s === "relearn") && s.due <= now + 20 * MIN; }).sort((a, b) => st(a).due - st(b).due);
    return soon[0] || null; // learn ahead
  }
  function renderStudy() {
    view = "study"; shown = false; cur = nextCard();
    const c = counts(deck);
    const head = `<div class="fc-top"><button type="button" class="srs-btn" data-act="back">← Decks</button><b>${esc(deck.name)} <span>${esc(deck.sub)}</span></b>
      <label class="srs-toggle"><input type="checkbox" data-auto${S.settings.autoAudio ? " checked" : ""}> Auto-play audio</label><span class="fc-counts"><i class="c-n">${c.nw}</i><i class="c-l">${c.lrn}</i><i class="c-r">${c.rev}</i></span></div>`;
    if (!cur) {
      const pending = deck.cards.map(x => S.cards[cid(deck, x)]).filter(s => s && (s.s === "learn" || s.s === "relearn")).sort((a, b) => a.due - b.due)[0];
      app.innerHTML = head + `<div class="fc-done"><div class="fc-big">Félicitations !</div><p>You've finished this deck for now.${sessionN ? ` ${sessionN} card${sessionN > 1 ? "s" : ""} this session.` : ""}</p>
        ${pending ? `<p>Next learning card in about ${human(pending.due - Date.now())}.</p>` : ""}${c.nw === 0 && counts(deck).totalNew > 0 ? `<p>You've hit today's new-card limit (${newPerDay(deck)}). Raise it in the deck options (⋯) if you want more.</p>` : ""}
        <button type="button" class="srs-btn solid" data-act="back">Back to decks</button></div>`;
      return;
    }
    const F = faces(deck, cur), stt = S.cards[cid(deck, cur)];
    const isNew = !stt;
    app.innerHTML = head + `<div class="fc-stage"><div class="fc${reduce() ? " nomo" : ""}"><div class="fc-face fc-front">${isNew ? '<span class="fc-new">new</span>' : ""}${F.front}</div><div class="fc-face fc-back">${F.front}<hr>${F.back}</div></div></div>
      <div class="fc-ctl"><button type="button" class="srs-btn solid fc-show" data-act="show">Show answer <kbd>space</kbd></button></div>
      <div class="fc-help">Keys: <kbd>space</kbd> show / good · <kbd>1</kbd>–<kbd>4</kbd> grade · <kbd>U</kbd> undo${undo ? ' · <button type="button" class="linkbtn" data-act="undo">Undo last</button>' : ""}</div>`;
    if (F.sayFront && window.FR && S.settings.autoAudio) setTimeout(() => window.FR.say(F.sayFront), 150);
    if (!reduce()) app.querySelector(".fc").animate([{ opacity: 0, transform: "translateY(14px) scale(.98)" }, { opacity: 1, transform: "none" }], { duration: 260, easing: "cubic-bezier(.2,.8,.2,1)" });
  }
  function show() {
    if (shown || !cur) return; shown = true;
    app.querySelector(".fc").classList.add("flip");
    const st = S.cards[cid(deck, cur)], now = Date.now();
    const lab = ["Again", "Hard", "Good", "Easy"];
    app.querySelector(".fc-ctl").innerHTML = lab.map((l, i) => `<button type="button" class="srs-grade g${i + 1}" data-g="${i + 1}"><span>${human(preview(st, i + 1).due - now)}</span>${l} <kbd>${i + 1}</kbd></button>`).join("");
    const F = faces(deck, cur); if (F.sayBack && window.FR && S.settings.autoAudio) setTimeout(() => window.FR.say(F.sayBack), 250);
  }
  function grade(g) {
    if (!shown || !cur) return;
    const id = cid(deck, cur), before = S.cards[id], t = today();
    undo = { id, before: before ? { ...before } : null, wasNew: !before, deckId: deck.id };
    S.cards[id] = preview(before, g);
    if (!before) t.n[deck.id] = (t.n[deck.id] || 0) + 1;
    t.r++; sessionN++; save(); renderStudy();
  }
  function doUndo() {
    if (!undo) return; const t = today();
    if (undo.before) S.cards[undo.id] = undo.before; else delete S.cards[undo.id];
    if (undo.wasNew) t.n[undo.deckId] = Math.max(0, (t.n[undo.deckId] || 1) - 1);
    t.r = Math.max(0, t.r - 1); sessionN = Math.max(0, sessionN - 1); undo = null; save();
    renderStudy();
  }

  app.addEventListener("click", e => {
    const o = e.target.closest("[data-open]"); if (o) { deck = allDecks().find(d => d.id === o.dataset.open); sessionN = 0; undo = null; renderStudy(); window.scrollTo({ top: app.offsetTop - 90, behavior: reduce() ? "auto" : "smooth" }); return; }
    const gr = e.target.closest("[data-g]"); if (gr) { grade(+gr.dataset.g); return; }
    const sy = e.target.closest("[data-say]"); if (sy) { e.stopPropagation(); window.FR && window.FR.say(sy.dataset.say, sy); return; }
    const s = e.target.closest("[data-set]");
    if (s) {
      const d = allDecks().find(x => x.id === s.dataset.set);
      const p = panel(`<h3>${esc(d.name)} <span>${esc(d.sub)}</span></h3><label>New cards per day <input type="number" min="0" max="500" class="lab-in" value="${newPerDay(d)}" data-np></label>
        <div class="srs-tools"><button type="button" class="srs-btn solid" data-act="saveset" data-d="${d.id}">Save</button><button type="button" class="srs-btn danger" data-act="resetdeck" data-d="${d.id}">Reset progress for this deck</button></div>`);
      return;
    }
    const a = e.target.closest("[data-act]"); if (!a) { if (view === "study" && e.target.closest(".fc")) shown ? null : show(); return; }
    const act = a.dataset.act;
    if (act === "show") show();
    if (act === "back") { renderDecks(); }
    if (act === "undo") doUndo();
    if (act === "saveset") { const v = Math.max(0, Math.min(500, +app.querySelector("[data-np]").value || 0)); S.settings[a.dataset.d] = { ...(S.settings[a.dataset.d] || {}), newPerDay: v }; save(); renderDecks(); }
    if (act === "resetdeck") { if (confirmReset(a)) { Object.keys(S.cards).forEach(k => { if (k.startsWith(a.dataset.d + "::")) delete S.cards[k]; }); save(); renderDecks(); } }
    if (act === "add") {
      panel(`<h3>Add a card <span>to “My cards”</span></h3><label>Front<textarea class="lab-in" data-front rows="2" placeholder="e.g. la bibliothèque"></textarea></label><label>Back<textarea class="lab-in" data-back rows="2" placeholder="e.g. library"></textarea></label>
        <div class="srs-tools"><button type="button" class="srs-btn solid" data-act="savecard">Add card</button><span class="srs-msg"></span></div>
        ${S.custom.length ? `<details class="srs-mine"><summary>Your cards (${S.custom.length})</summary>${S.custom.map((c, i) => `<div class="srs-mc"><span>${esc(c.f)} → ${esc(c.b)}</span><button type="button" class="linkbtn" data-act="delcard" data-i="${i}">delete</button></div>`).join("")}</details>` : ""}`);
    }
    if (act === "savecard") {
      const f = app.querySelector("[data-front]").value.trim(), b = app.querySelector("[data-back]").value.trim();
      if (!f || !b) { app.querySelector(".srs-msg").textContent = "Fill in both sides."; return; }
      S.custom.push({ id: "c" + Date.now().toString(36), f, b }); save();
      app.querySelector("[data-front]").value = ""; app.querySelector("[data-back]").value = "";
      app.querySelector(".srs-msg").textContent = "Added. " + S.custom.length + " card" + (S.custom.length > 1 ? "s" : "") + " in My cards.";
      app.querySelector("[data-front]").focus();
      const row = [...app.querySelectorAll("[data-open='mine']")][0]; if (row) row.querySelector("span").textContent = `Cards you add yourself · ${S.custom.length} cards`;
    }
    if (act === "delcard") { const c = S.custom.splice(+a.dataset.i, 1)[0]; if (c) delete S.cards["mine::" + c.id]; save(); renderDecks(); }
    if (act === "export") {
      const blob = new Blob([JSON.stringify(S)], { type: "application/json" });
      const u = URL.createObjectURL(blob), l = document.createElement("a"); l.href = u; l.download = "apogee-flashcards-" + dayKey() + ".json"; document.body.appendChild(l); l.click(); l.remove(); setTimeout(() => URL.revokeObjectURL(u), 1000);
    }
  });
  function confirmReset(a) {
    if (a.dataset.sure) return true;
    a.dataset.sure = 1; a.textContent = "Tap again to confirm reset"; return false;
  }
  app.addEventListener("change", e => {
    if (e.target.matches("[data-auto]")) { S.settings.autoAudio = e.target.checked; save(); e.target.blur(); if (!e.target.checked && "speechSynthesis" in window) speechSynthesis.cancel(); return; }
    if (e.target.matches('[data-act="import"]')) {
      const f = e.target.files[0]; if (!f) return;
      f.text().then(t => { const d = JSON.parse(t); if (!d || typeof d.cards !== "object") throw 0; localStorage.setItem(KEY, JSON.stringify(d)); load(); renderDecks(); panel("<p>Progress imported.</p>"); })
        .catch(() => panel("<p>That file isn't an Apogee flashcards export.</p>"));
    }
  });
  document.addEventListener("keydown", e => {
    if (view !== "study" || e.target.closest("input,textarea,select")) return;
    if (e.key === " " || e.key === "Enter") { e.preventDefault(); shown ? grade(3) : show(); }
    else if (/^[1-4]$/.test(e.key) && shown) grade(+e.key);
    else if (e.key.toLowerCase() === "u") doUndo();
  });
  renderDecks();
})();
