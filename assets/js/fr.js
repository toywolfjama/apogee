/* French course: audio, word animations and interactive labs */
(function () {
  "use strict";
  const esc = s => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  const reduce = () => document.body.classList.contains("no-motion") || matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------------- audio ---------------- */
  let voice = null;
  function pickVoice() {
    if (!("speechSynthesis" in window)) return;
    const vs = speechSynthesis.getVoices();
    voice = vs.find(v => /^fr[-_]FR/i.test(v.lang) && /google|amélie|thomas|audrey|marie/i.test(v.name)) || vs.find(v => /^fr[-_]FR/i.test(v.lang)) || vs.find(v => /^fr/i.test(v.lang)) || null;
  }
  if ("speechSynthesis" in window) { pickVoice(); speechSynthesis.onvoiceschanged = pickVoice; }
  function say(text, el) {
    if (!("speechSynthesis" in window)) return;
    const t = String(text).replace(/\(e\)|\(s\)|\(es\)|\(e\)s/g, "").replace(/[\/…]/g, ", ").replace(/\s+/g, " ").trim();
    if (!t) return;
    speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(t);
    u.lang = "fr-FR"; if (voice) u.voice = voice; u.rate = 0.88;
    if (el) { el.classList.add("speaking"); u.onend = u.onerror = () => el.classList.remove("speaking"); }
    speechSynthesis.speak(u);
  }
  window.FR = { say };
  function bindSay(root) {
    (root || document).querySelectorAll(".fr:not([data-bound])").forEach(el => {
      el.dataset.bound = 1;
      if (el.closest(".quiz .opt, .exam .opt, .frlab, .wanim")) return;
      el.classList.add("say"); el.tabIndex = 0; el.setAttribute("role", "button");
      el.title = "Hear it";
    });
  }
  document.addEventListener("click", e => {
    const b = e.target.closest("[data-say]");
    if (b) { e.preventDefault(); say(b.dataset.say, b); return; }
    const s = e.target.closest(".fr.say");
    if (s) say(s.dataset.t || s.textContent, s);
  });
  document.addEventListener("keydown", e => {
    if ((e.key === "Enter" || e.key === " ") && e.target.matches && e.target.matches(".fr.say")) { e.preventDefault(); say(e.target.dataset.t || e.target.textContent, e.target); }
  });
  const sayBtn = (t, label) => `<button type="button" class="saybtn" data-say="${esc(t)}" aria-label="Hear: ${esc(t)}">${label ? esc(label) : ""}</button>`;

  /* ---------------- word-tile animations ---------------- */
  function wanim(el, p) {
    const frames = p.frames.map(f => ({ note: f.note || "", en: f.en || "", t: f.t.map(x => Array.isArray(x) ? x : String(x).split("|")) }));
    el.innerHTML = `${p.title ? `<div class="wa-h">${esc(p.title)}</div>` : ""}
      <div class="wa-stage"><div class="wa-row"></div></div>
      <div class="wa-en"></div>
      <div class="wa-note"></div>
      <div class="wa-ctl"><button type="button" class="wa-b" data-a="back" aria-label="Back">◀</button><span class="wa-dots">${frames.map(() => "<i></i>").join("")}</span><button type="button" class="wa-b solid" data-a="next">Step ▶</button><button type="button" class="wa-b" data-a="hear">Hear it</button></div>`;
    const row = el.querySelector(".wa-row"), note = el.querySelector(".wa-note"), en = el.querySelector(".wa-en"), dots = el.querySelectorAll(".wa-dots i");
    let i = 0;
    function render(k, animate) {
      const old = {};
      if (animate && !reduce()) row.querySelectorAll(".wt").forEach(t => old[t.dataset.id] = t.getBoundingClientRect());
      const f = frames[k];
      row.innerHTML = f.t.map(([id, txt, cls]) => `<span class="wt ${cls || ""}" data-id="${esc(id)}">${esc(txt)}</span>`).join("");
      note.innerHTML = f.note; en.textContent = f.en;
      dots.forEach((d, j) => d.classList.toggle("on", j <= k));
      el.querySelector('[data-a="next"]').textContent = k === frames.length - 1 ? "Replay ↺" : "Step ▶";
      if (!animate || reduce()) return;
      row.querySelectorAll(".wt").forEach(t => {
        const o = old[t.dataset.id], n = t.getBoundingClientRect();
        if (o) {
          const dx = o.left - n.left, dy = o.top - n.top, sx = o.width / n.width;
          t.animate([{ transform: `translate(${dx}px,${dy}px) scaleX(${sx})` }, { transform: "none" }], { duration: 520, easing: "cubic-bezier(.2,.8,.2,1)" });
        } else {
          t.animate([{ opacity: 0, transform: "translateY(-18px) scale(.7)" }, { opacity: 1, transform: "none" }], { duration: 480, delay: 160, easing: "cubic-bezier(.2,1.4,.4,1)", fill: "backwards" });
        }
      });
    }
    el.addEventListener("click", e => {
      const a = e.target.closest("[data-a]"); if (!a) return;
      if (a.dataset.a === "next") { i = i === frames.length - 1 ? 0 : i + 1; render(i, i !== 0); }
      if (a.dataset.a === "back" && i > 0) { i--; render(i, true); }
      if (a.dataset.a === "hear") say(frames[i].t.filter(x => !/\bgl\b/.test(x[2] || "")).map(x => x[1]).join(" ").replace(/' /g, "'").replace(/ -/g, "-").replace(/- /g, "-"), a);
    });
    render(0, false);
  }

  /* ---------------- verbs ---------------- */
  const PR = ["je", "tu", "il / elle / on", "nous", "vous", "ils / elles"];
  const V = {
    parler: ["to speak", "er", "parle parles parle parlons parlez parlent", "parlé"],
    aimer: ["to like, love", "er", "aime aimes aime aimons aimez aiment", "aimé"],
    habiter: ["to live (in)", "er", "habite habites habite habitons habitez habitent", "habité"],
    manger: ["to eat", "er", "mange manges mange mangeons mangez mangent", "mangé"],
    regarder: ["to watch", "er", "regarde regardes regarde regardons regardez regardent", "regardé"],
    jouer: ["to play", "er", "joue joues joue jouons jouez jouent", "joué"],
    finir: ["to finish", "ir", "finis finis finit finissons finissez finissent", "fini"],
    choisir: ["to choose", "ir", "choisis choisis choisit choisissons choisissez choisissent", "choisi"],
    vendre: ["to sell", "re", "vends vends vend vendons vendez vendent", "vendu"],
    attendre: ["to wait (for)", "re", "attends attends attend attendons attendez attendent", "attendu"],
    "être": ["to be", "irr", "suis es est sommes êtes sont", "été"],
    avoir: ["to have", "irr", "ai as a avons avez ont", "eu"],
    aller: ["to go", "irr", "vais vas va allons allez vont", "allé", 1],
    faire: ["to do, make", "irr", "fais fais fait faisons faites font", "fait"],
    venir: ["to come", "irr", "viens viens vient venons venez viennent", "venu", 1],
    prendre: ["to take", "irr", "prends prends prend prenons prenez prennent", "pris"],
    vouloir: ["to want", "irr", "veux veux veut voulons voulez veulent", "voulu"],
    pouvoir: ["to be able to", "irr", "peux peux peut pouvons pouvez peuvent", "pu"],
    devoir: ["to have to", "irr", "dois dois doit devons devez doivent", "dû"],
    voir: ["to see", "irr", "vois vois voit voyons voyez voient", "vu"],
    boire: ["to drink", "irr", "bois bois boit buvons buvez boivent", "bu"],
    lire: ["to read", "irr", "lis lis lit lisons lisez lisent", "lu"],
    "écrire": ["to write", "irr", "écris écris écrit écrivons écrivez écrivent", "écrit"],
    mettre: ["to put", "irr", "mets mets met mettons mettez mettent", "mis"],
    dormir: ["to sleep", "irr", "dors dors dort dormons dormez dorment", "dormi"],
    partir: ["to leave", "irr", "pars pars part partons partez partent", "parti", 1],
    sortir: ["to go out", "irr", "sors sors sort sortons sortez sortent", "sorti", 1],
    arriver: ["to arrive", "er", "arrive arrives arrive arrivons arrivez arrivent", "arrivé", 1],
    rester: ["to stay", "er", "reste restes reste restons restez restent", "resté", 1],
    tomber: ["to fall", "er", "tombe tombes tombe tombons tombez tombent", "tombé", 1],
    "se lever": ["to get up", "refl", "lève lèves lève levons levez lèvent", "levé", 1],
    "se coucher": ["to go to bed", "refl", "couche couches couche couchons couchez couchent", "couché", 1],
    "s'habiller": ["to get dressed", "refl", "habille habilles habille habillons habillez habillent", "habillé", 1]
  };
  const vowel = s => /^[aeiouyhâàéèêëîïôûœ]/i.test(s);
  const REFL = ["me", "te", "se", "nous", "vous", "se"];
  const AUXA = V.avoir[2].split(" "), AUXE = V["être"][2].split(" "), ALLER = V.aller[2].split(" ");
  function subj(i, next) { const p = ["je", "tu", "il", "nous", "vous", "ils"][i]; return i === 0 && vowel(next) ? "j'" : p + " "; }
  function refl(i, next) { const r = REFL[i]; return (i === 0 || i === 1 || i === 2 || i === 5) && vowel(next) ? r[0] + "'" : r + " "; }
  function agree(pp, i) { return ["(e)", "(e)", "", "(e)s", "(e)(s)", "s"][i] ? pp + ["(e)", "(e)", "", "(e)s", "(e)(s)", "s"][i] : pp; }
  function conj(key, tense) {
    const [en, kind, forms, pp, etre] = V[key]; const F = forms.split(" ");
    const isRefl = kind === "refl"; const inf = key.replace(/^se |^s'/, "");
    return F.map((f, i) => {
      let pron = PR[i], form, stem = "", end = "";
      if (tense === "pres") {
        const r = isRefl ? refl(i, f) : "";
        const base = ["er", "ir", "re"].includes(kind) ? inf.slice(0, -2) : (isRefl ? inf.slice(0, -2) : null);
        if (base && f.startsWith(base) && kind !== "irr") { stem = base; end = f.slice(base.length); } else { stem = f; end = ""; }
        form = { lead: (isRefl ? subj(i, r) + r : subj(i, f)), stem, end };
      } else if (tense === "pc") {
        const be = etre || isRefl; const aux = (be ? AUXE : AUXA)[i];
        const r = isRefl ? refl(i, aux) : "";
        const p2 = be ? agree(pp, i) : pp;
        form = { lead: subj(i, isRefl ? r : aux) + r + aux + " ", stem: p2, end: "", aux: be ? "être" : "avoir" };
        if (i === 2 && be) form.stem = pp + " / " + pp + "e";
        if (i === 5 && be) form.stem = pp + "s / " + pp + "es";
      } else {
        const r = isRefl ? refl(i, inf) : "";
        form = { lead: subj(i, ALLER[i]) + ALLER[i] + " " + r, stem: inf, end: "" };
      }
      return { pron, ...form };
    }).map(x => ({ ...x, lead: x.lead.replace(/^ils /, i => i) }));
  }
  function labConj(el, p) {
    const keys = p.verbs || Object.keys(V);
    const tenses = p.tenses || ["pres"];
    const TN = { pres: "Present", pc: "Passé composé", fp: "Futur proche" };
    el.innerHTML = `<div class="lab-h">Verb lab <span>Pick a verb${tenses.length > 1 ? " and a tense" : ""}. Tap a row to hear it.</span></div>
      <div class="lab-row"><select class="lab-in" data-k="v">${keys.map(k => `<option value="${esc(k)}">${esc(k)} (${esc(V[k][0])})</option>`).join("")}</select>
      ${tenses.length > 1 ? `<select class="lab-in" data-k="t">${tenses.map(t => `<option value="${t}">${TN[t]}</option>`).join("")}</select>` : ""}</div>
      <div class="cj-info"></div><div class="cj-grid"></div>`;
    const grid = el.querySelector(".cj-grid"), info = el.querySelector(".cj-info");
    function upd() {
      const k = el.querySelector('[data-k="v"]').value, t = tenses.length > 1 ? el.querySelector('[data-k="t"]').value : tenses[0];
      const d = V[k], rows = conj(k, t);
      const kind = { er: "regular -er verb", ir: "regular -ir verb", re: "regular -re verb", irr: "irregular verb", refl: "reflexive -er verb" }[d[1]];
      let msg = `<b>${esc(k)}</b> · ${esc(d[0])} · ${kind}`;
      if (t === "pres" && ["er", "ir", "re"].includes(d[1])) msg += ` · stem <b>${esc(k.slice(0, -2))}-</b> + the <span class="cj-end">endings</span>`;
      if (t === "pc") msg += ` · helper verb <b>${(d[4] || d[1] === "refl") ? "être" : "avoir"}</b> + past participle <b>${esc(d[3])}</b>${(d[4] || d[1] === "refl") ? " (agrees with the subject)" : ""}`;
      if (t === "fp") msg += " · <b>aller</b> in the present + the infinitive";
      info.innerHTML = msg;
      grid.innerHTML = rows.map(r => {
        const full = r.lead + r.stem + r.end;
        return `<button type="button" class="cj-row" data-say="${esc(full.replace(/il \/ elle/, "il"))}"><span class="cj-p">${esc(r.pron)}</span><span class="cj-f">${esc(r.lead)}<b>${esc(r.stem)}</b><span class="cj-end">${esc(r.end)}</span></span></button>`;
      }).join("");
      if (!reduce()) grid.querySelectorAll(".cj-end").forEach((e, j) => e.animate([{ opacity: 0, transform: "translateY(-8px)" }, { opacity: 1, transform: "none" }], { duration: 380, delay: 60 * j, fill: "backwards" }));
    }
    el.querySelectorAll("select").forEach(s => s.addEventListener("change", upd));
    upd();
  }

  /* ---------------- numbers ---------------- */
  const U = "zéro un deux trois quatre cinq six sept huit neuf dix onze douze treize quatorze quinze seize".split(" ");
  const T = { 2: "vingt", 3: "trente", 4: "quarante", 5: "cinquante", 6: "soixante" };
  function below100(n) {
    if (n <= 16) return U[n];
    if (n < 20) return "dix-" + U[n - 10];
    if (n < 70) { const t = Math.floor(n / 10), u = n % 10; return T[t] + (u === 0 ? "" : u === 1 ? " et un" : "-" + U[u]); }
    if (n < 80) return n === 71 ? "soixante et onze" : "soixante-" + below100(n - 60);
    if (n === 80) return "quatre-vingts";
    return "quatre-vingt-" + below100(n - 80);
  }
  function frNum(n) {
    n = Math.floor(n); if (n < 0) return "moins " + frNum(-n);
    if (n < 100) return below100(n);
    if (n < 1000) {
      const h = Math.floor(n / 100), r = n % 100;
      const head = h === 1 ? "cent" : U[h] + " cent" + (r === 0 ? "s" : "");
      return head + (r ? " " + below100(r) : "");
    }
    if (n < 1000000) {
      const th = Math.floor(n / 1000), r = n % 1000;
      const head = th === 1 ? "mille" : frNum(th).replace(/cents$/, "cent").replace(/vingts$/, "vingt") + " mille";
      return head + (r ? " " + frNum(r) : "");
    }
    return String(n);
  }
  function numMath(n) {
    if (n >= 70 && n < 80) return `${n} = 60 + ${n - 60}: <i>soixante</i> + <i>${below100(n - 60)}</i>`;
    if (n === 80) return "80 = 4 × 20: <i>quatre-vingts</i> (the s drops when another number follows)";
    if (n > 80 && n < 100) return `${n} = 4 × 20 + ${n - 80}: <i>quatre-vingt</i> + <i>${below100(n - 80)}</i>`;
    if (n % 10 === 1 && n > 20 && n < 70) return `${n}: use <i>et un</i> for 21, 31, 41, 51 and 61`;
    if (n >= 100 && n < 1000) return `${Math.floor(n / 100)} × 100${n % 100 ? " + " + (n % 100) : ""}${Math.floor(n / 100) > 1 && n % 100 === 0 ? ": <i>cents</i> takes an s only when nothing follows" : ""}`;
    if (n >= 1000) return "<i>mille</i> never takes an s: deux mille";
    return "";
  }
  window.FR.num = frNum;
  function labNum(el, p) {
    el.innerHTML = `<div class="lab-h">Number lab <span>Type any number up to 9999, or slide.</span></div>
      <div class="lab-row"><input class="lab-in n" data-k="n" type="number" min="0" max="9999" value="${p.n ?? 78}"><input class="nm-sl" type="range" min="0" max="${p.max || 100}" value="${Math.min(p.n ?? 78, p.max || 100)}"></div>
      <div class="nm-out"><span class="nm-w"></span><button type="button" class="saybtn big" aria-label="Hear it"></button></div><div class="nm-math"></div>`;
    const inp = el.querySelector('[data-k="n"]'), sl = el.querySelector(".nm-sl"), w = el.querySelector(".nm-w"), m = el.querySelector(".nm-math"), b = el.querySelector(".saybtn");
    function upd(v) {
      let n = Math.max(0, Math.min(9999, Math.floor(+v || 0)));
      const s = frNum(n); w.textContent = s; b.dataset.say = s; m.innerHTML = numMath(n);
      if (!reduce()) w.animate([{ opacity: .3, transform: "translateY(6px)" }, { opacity: 1, transform: "none" }], { duration: 250 });
    }
    inp.addEventListener("input", () => { sl.value = inp.value; upd(inp.value); });
    sl.addEventListener("input", () => { inp.value = sl.value; upd(sl.value); });
    upd(inp.value);
  }

  /* ---------------- clock ---------------- */
  function heure(h) { return h === 1 ? "une heure" : frNum(h).replace(/^un$/, "une") + " heures"; }
  function telling(h, m) {
    const nameH = x => x === 0 ? "minuit" : x === 12 ? "midi" : heure(x > 12 ? x - 12 : x);
    let s, named = h;
    if (m <= 30) {
      const base = nameH(h);
      s = m === 0 ? base : m === 15 ? base + " et quart" : m === 30 ? base + (h === 0 || h === 12 ? " et demi" : " et demie") : base + " " + frNum(m).replace(/^un$/, "une").replace(/ et un$/, " et une");
    } else {
      const nh = (h + 1) % 24, base = nameH(nh), left = 60 - m; named = nh;
      s = left === 15 ? base + " moins le quart" : base + " moins " + frNum(left).replace(/^un$/, "une");
    }
    const part = named === 0 || named === 12 ? "" : named < 12 ? " du matin" : named < 18 ? " de l'après-midi" : " du soir";
    const official = (h === 1 ? "une heure" : h === 0 ? "zéro heure" : frNum(h).replace(/ et un$/, " et une") + " heures") + (m ? " " + frNum(m).replace(/^un$/, "une").replace(/ et un$/, " et une") : "");
    return { s: "Il est " + s + part + ".", o: "Il est " + official + "." };
  }
  window.FR.time = telling;
  function labClock(el, p) {
    let h = p.h ?? 15, m = p.m ?? 45;
    const ticks = Array.from({ length: 12 }, (_, i) => { const a = i * Math.PI / 6; return `<line x1="${60 + 44 * Math.sin(a)}" y1="${60 - 44 * Math.cos(a)}" x2="${60 + 50 * Math.sin(a)}" y2="${60 - 50 * Math.cos(a)}"/>`; }).join("");
    el.innerHTML = `<div class="lab-h">Clock lab <span>Move the hour and minutes.</span></div>
      <div class="ck"><svg viewBox="0 0 120 120" class="ck-face" aria-hidden="true"><circle cx="60" cy="60" r="56"/><g class="ck-t">${ticks}</g><line class="ck-h" x1="60" y1="60" x2="60" y2="32"/><line class="ck-m" x1="60" y1="60" x2="60" y2="16"/><circle cx="60" cy="60" r="3.5" class="ck-c"/></svg>
      <div class="ck-r"><div class="lab-row"><label>heure <input class="nm-sl" data-k="h" type="range" min="0" max="23" value="${h}"></label><b class="ck-hh"></b></div>
      <div class="lab-row"><label>minutes <input class="nm-sl" data-k="m" type="range" min="0" max="55" step="5" value="${m}"></label></div>
      <div class="ck-say"><span class="ck-s"></span> <button type="button" class="saybtn" aria-label="Hear it"></button></div>
      <div class="ck-o"><span class="lbl">Official / 24-hour:</span> <span class="ck-of"></span> <button type="button" class="saybtn" aria-label="Hear it"></button></div></div></div>`;
    const hh = el.querySelector(".ck-h"), mm = el.querySelector(".ck-m");
    function upd() {
      h = +el.querySelector('[data-k="h"]').value; m = +el.querySelector('[data-k="m"]').value;
      el.querySelector(".ck-hh").textContent = String(h).padStart(2, "0") + ":" + String(m).padStart(2, "0");
      hh.style.transform = `rotate(${(h % 12) * 30 + m / 2}deg)`; mm.style.transform = `rotate(${m * 6}deg)`;
      const t = telling(h, m); el.querySelector(".ck-s").textContent = t.s; el.querySelector(".ck-of").textContent = t.o;
      const bs = el.querySelectorAll(".saybtn"); bs[0].dataset.say = t.s; bs[1].dataset.say = t.o;
    }
    el.querySelectorAll("input").forEach(i => i.addEventListener("input", upd)); upd();
  }

  /* ---------------- nouns and articles ---------------- */
  const N = {
    livre: ["m", "book"], stylo: ["m", "pen"], cahier: ["m", "notebook"], table: ["f", "table"], chaise: ["f", "chair"], "école": ["f", "school"],
    ami: ["m", "friend (m)"], amie: ["f", "friend (f)"], "hôtel": ["m", "hotel"], parc: ["m", "park"], piscine: ["f", "pool"], "cinéma": ["m", "movie theater"],
    gare: ["f", "train station"], "musée": ["m", "museum"], pain: ["m", "bread"], eau: ["f", "water", "eaux"], fromage: ["m", "cheese"], confiture: ["f", "jam"],
    chat: ["m", "cat"], maison: ["f", "house"], "frère": ["m", "brother"], "sœur": ["f", "sister"], "université": ["f", "university"], gâteau: ["m", "cake", "gâteaux"]
  };
  function arts(noun, pl) {
    const [g, , plf] = N[noun], v = vowel(noun), w = pl ? (plf || noun + "s") : noun;
    const def = pl ? "les " : v ? "l'" : g === "m" ? "le " : "la ";
    const ind = pl ? "des " : g === "m" ? "un " : "une ";
    const part = pl ? "des " : v ? "de l'" : g === "m" ? "du " : "de la ";
    const a = pl ? "aux " : v ? "à l'" : g === "m" ? "au " : "à la ";
    const de = pl ? "des " : v ? "de l'" : g === "m" ? "du " : "de la ";
    const poss = pl ? "mes " : g === "f" && !v ? "ma " : "mon ";
    return [["the", def + w, "le / la / l' / les"], ["a, some", ind + w, "un / une / des"], ["some (part of)", part + w, "du / de la / de l' / des"], ["to / at the", a + w, "à + le = au, à + les = aux"], ["of / from the", de + w, "de + le = du, de + les = des"], ["my", poss + w, "mon / ma / mes"]];
  }
  function labNoun(el, p) {
    const keys = p.nouns || Object.keys(N);
    el.innerHTML = `<div class="lab-h">Article lab <span>Pick a noun. Watch every little word change with it.</span></div>
      <div class="lab-row"><select class="lab-in" data-k="n">${keys.map(k => `<option value="${esc(k)}">${esc(k)} (${esc(N[k][1])})</option>`).join("")}</select>
      <label class="tg"><input type="checkbox" data-k="pl"> plural</label><span class="gtag"></span></div><div class="ar-grid"></div>`;
    function upd() {
      const k = el.querySelector('[data-k="n"]').value, pl = el.querySelector('[data-k="pl"]').checked;
      const g = N[k][0]; el.querySelector(".gtag").innerHTML = `<span class="g-${g}">${g === "m" ? "masculine" : "feminine"}</span>${vowel(k) ? ' · starts with a vowel sound' : ""}`;
      const rows = (p.rows ? arts(k, pl).filter((_, i) => p.rows.includes(i)) : arts(k, pl));
      el.querySelector(".ar-grid").innerHTML = rows.map(([en, fr, rule]) => `<button type="button" class="ar-row" data-say="${esc(fr)}"><span class="ar-en">${esc(en)}</span><b>${esc(fr)}</b><span class="ar-rule">${esc(rule)}</span></button>`).join("");
      if (!reduce()) el.querySelectorAll(".ar-row b").forEach((e, j) => e.animate([{ opacity: 0, transform: "translateX(-8px)" }, { opacity: 1, transform: "none" }], { duration: 300, delay: 40 * j, fill: "backwards" }));
    }
    el.querySelectorAll("select,input").forEach(s => s.addEventListener("change", upd)); upd();
  }

  /* ---------------- adjectives ---------------- */
  const A = {
    petit: ["small", "petit petite petits petites", 1], grand: ["big, tall", "grand grande grands grandes", 1], joli: ["pretty", "joli jolie jolis jolies", 1],
    bon: ["good", "bon bonne bons bonnes", 1], beau: ["beautiful", "beau belle beaux belles", 1, "bel"], nouveau: ["new", "nouveau nouvelle nouveaux nouvelles", 1, "nouvel"],
    vieux: ["old", "vieux vieille vieux vieilles", 1, "vieil"], jeune: ["young", "jeune jeune jeunes jeunes", 1],
    noir: ["black", "noir noire noirs noires"], bleu: ["blue", "bleu bleue bleus bleues"], blanc: ["white", "blanc blanche blancs blanches"], rouge: ["red", "rouge rouge rouges rouges"],
    intelligent: ["smart", "intelligent intelligente intelligents intelligentes"], heureux: ["happy", "heureux heureuse heureux heureuses"], sportif: ["athletic", "sportif sportive sportifs sportives"],
    "français": ["French", "français française français françaises"], gentil: ["kind", "gentil gentille gentils gentilles"], "intéressant": ["interesting", "intéressant intéressante intéressants intéressantes"]
  };
  const AN = { "garçon": ["m", "boy"], fille: ["f", "girl"], livre: ["m", "book"], voiture: ["f", "car"], ami: ["m", "friend (m)"], amie: ["f", "friend (f)"], "hôtel": ["m", "hotel"], maison: ["f", "house"], film: ["m", "movie"], "étudiante": ["f", "student (f)"], chien: ["m", "dog"] };
  function labAdj(el, p) {
    el.innerHTML = `<div class="lab-h">Adjective lab <span>The adjective changes to match the noun, and a few go before it.</span></div>
      <div class="lab-row"><select class="lab-in" data-k="n">${Object.keys(AN).map(k => `<option value="${esc(k)}">${esc(k)} (${esc(AN[k][1])})</option>`).join("")}</select>
      <select class="lab-in" data-k="a">${Object.keys(A).map(k => `<option value="${esc(k)}"${k === (p.a || "intelligent") ? " selected" : ""}>${esc(k)} (${esc(A[k][0])})</option>`).join("")}</select>
      <label class="tg"><input type="checkbox" data-k="pl"> plural</label></div>
      <div class="ad-out"></div><div class="ad-why"></div>`;
    function upd() {
      const n = el.querySelector('[data-k="n"]').value, a = el.querySelector('[data-k="a"]').value, pl = el.querySelector('[data-k="pl"]').checked;
      const [g] = AN[n], [, forms, before, alt] = A[a], F = forms.split(" ");
      let adj = F[(g === "f" ? 1 : 0) + (pl ? 2 : 0)];
      let why = [];
      if (alt && g === "m" && !pl && before && vowel(n)) { adj = alt; why.push(`Before a masculine noun starting with a vowel sound, <b>${a}</b> becomes <b>${alt}</b> so the words flow.`); }
      const art = pl ? (before ? "de" : "des") : g === "m" ? "un" : "une";
      const noun = pl ? (n === "hôtel" ? "hôtels" : n + "s") : n;
      const phrase = before ? `${art} ${adj} ${noun}` : `${art} ${noun} ${adj}`;
      why.unshift(`${g === "f" ? "Feminine" : "Masculine"} ${pl ? "plural" : "singular"} noun → <b>${esc(adj)}</b>.`);
      why.push(before ? "This adjective goes <b>before</b> the noun (Beauty, Age, Goodness, Size)." : "Most adjectives go <b>after</b> the noun.");
      if (pl && before) why.push("Formal French uses <b>de</b> instead of <b>des</b> when a plural adjective comes before the noun (many speakers still say des).");
      el.querySelector(".ad-out").innerHTML = `<b class="ad-ph">${esc(phrase)}</b>${sayBtn(phrase)}`;
      el.querySelector(".ad-why").innerHTML = why.map(x => `<div>${x}</div>`).join("");
      if (!reduce()) el.querySelector(".ad-ph").animate([{ opacity: .2, letterSpacing: "4px" }, { opacity: 1, letterSpacing: "0px" }], { duration: 350 });
    }
    el.querySelectorAll("select,input").forEach(s => s.addEventListener("change", upd)); upd();
  }

  /* ---------------- negation ---------------- */
  const S = [
    { s: "je", v: "parle", r: "français", en: "I speak French." },
    { s: "je", v: "ai", r: "un chien", ind: "chien", en: "I have a dog." },
    { s: "elle", v: "aime", r: "le café", en: "She likes coffee." },
    { s: "nous", v: "mangeons", r: "des pommes", ind: "pommes", en: "We eat apples." },
    { s: "tu", v: "es", r: "fatigué", en: "You are tired." },
    { s: "ils", v: "ont", r: "mangé", pc: 1, en: "They ate." },
    { s: "je", v: "suis", r: "allé au cinéma", pc: 1, en: "I went to the movies." },
    { s: "il", v: "boit", r: "de l'eau", ind: "eau", en: "He drinks (some) water." }
  ];
  const NEG = { pas: ["pas", "not"], jamais: ["jamais", "never"], plus: ["plus", "no longer"], rien: ["rien", "nothing"] };
  function labNeg(el, p) {
    el.innerHTML = `<div class="lab-h">Negation lab <span>ne … pas wraps around the conjugated verb.</span></div>
      <div class="lab-row"><select class="lab-in" data-k="s">${S.map((x, i) => `<option value="${i}">${esc(cap(build(x)))} (${esc(x.en)})</option>`).join("")}</select>
      <select class="lab-in" data-k="n">${Object.entries(NEG).map(([k, v]) => `<option value="${k}">ne … ${v[0]} (${v[1]})</option>`).join("")}</select></div>
      <div class="ng-out"></div><div class="ad-why ng-why"></div>`;
    function build(x) { return (x.s === "je" && vowel(x.v) ? "j'" : x.s + " ") + x.v + " " + x.r; }
    function cap(s) { return s[0].toUpperCase() + s.slice(1); }
    function upd() {
      const x = S[+el.querySelector('[data-k="s"]').value], nk = el.querySelector('[data-k="n"]').value;
      let why = [];
      const ne = vowel(x.v) ? "n'" : "ne ";
      if (vowel(x.v)) why.push("<b>ne</b> becomes <b>n'</b> before a vowel sound.");
      let rest = x.r;
      if (nk === "rien") {
        rest = x.pc ? x.r : "";
        if (!x.pc) why.push("<b>rien</b> replaces the object: there is nothing left to name.");
      } else if (x.ind && !x.pc) {
        const before = rest;
        rest = rest.replace(/^(un|une|des|du|de la) /, vowel(x.ind) ? "d'" : "de ").replace(/^de l'/, "d'");
        if (before !== rest) why.push(`After a negative, <b>un / une / des / du / de la</b> become <b>de</b> (or <b>d'</b>): ${esc(before)} → ${esc(rest)}.`);
      }
      if (x.pc) why.push("In the passé composé, the negative wraps the <b>helper verb</b>, not the past participle.");
      if (nk === "rien" && x.pc) why.push("Here <b>rien</b> stands in for the object.");
      const sj = x.s === "je" ? "je" : x.s;
      const out = [`<span class="wt s">${esc(cap(sj))}</span>`, `<span class="wt n">${esc(ne.trim())}</span>`, `<span class="wt v">${esc(x.v)}</span>`, `<span class="wt n">${NEG[nk][0]}</span>`, rest ? `<span class="wt">${esc(rest)}</span>` : ""].join(" ");
      const text = cap(sj) + " " + ne + x.v + " " + NEG[nk][0] + (rest ? " " + rest : "") + ".";
      el.querySelector(".ng-out").innerHTML = `<div class="wa-row">${out}<span class="wt">.</span></div>${sayBtn(text)}`;
      el.querySelector(".ng-why").innerHTML = why.map(w => `<div>${w}</div>`).join("") || "<div>Put <b>ne</b> right before the verb and the second word right after it.</div>";
      if (!reduce()) el.querySelectorAll(".ng-out .wt.n").forEach((t, j) => t.animate([{ opacity: 0, transform: `translateY(${j ? 16 : -16}px)` }, { opacity: 1, transform: "none" }], { duration: 420, easing: "cubic-bezier(.2,1.4,.4,1)" }));
    }
    el.querySelectorAll("select").forEach(s => s.addEventListener("change", upd)); upd();
  }

  const LABS = { conj: labConj, num: labNum, clock: labClock, noun: labNoun, adj: labAdj, neg: labNeg };
  function mount(root) {
    bindSay(root);
    (root || document).querySelectorAll(".frlab[data-lab]").forEach(el => {
      if (el.dataset.mounted) return; el.dataset.mounted = 1;
      try { const p = JSON.parse(el.dataset.lab); LABS[p.type] && LABS[p.type](el, p); } catch (e) { console.error(e); }
    });
    (root || document).querySelectorAll(".wanim[data-w]").forEach(el => {
      if (el.dataset.mounted) return; el.dataset.mounted = 1;
      try { wanim(el, JSON.parse(el.dataset.w)); } catch (e) { console.error(e); }
    });
  }
  window.FR.mount = mount;
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", () => mount()); else mount();
  // quizzes render later; pick up new French text there too
  new MutationObserver(() => bindSay()).observe(document.body, { childList: true, subtree: true });
})();
