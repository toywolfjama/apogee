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
      <div class="wa-ctl"><button type="button" class="wa-b" data-a="back" aria-label="Back">◀</button><span class="wa-dots">${frames.map((_, i) => `<i data-i="${i}"></i>`).join("")}</span><button type="button" class="wa-b" data-a="play">Play</button><button type="button" class="wa-b solid" data-a="next">Step ▶</button><button type="button" class="wa-b" data-a="hear">Hear it</button></div>`;
    const row = el.querySelector(".wa-row"), note = el.querySelector(".wa-note"), en = el.querySelector(".wa-en"), dots = el.querySelectorAll(".wa-dots i");
    let i = 0, auto = null;
    const textOf = k => frames[k].t.filter(x => !/\bgl\b/.test(x[2] || "")).map(x => x[1]).join(" ").replace(/' /g, "'").replace(/ -/g, "-").replace(/- /g, "-");
    function render(k, animate) {
      window.WA.render(el, row, frames, k, animate, note, dots);
      en.textContent = frames[k].en;
      if (animate && !reduce()) en.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 500, delay: 250, fill: "backwards" });
    }
    function stop() { if (auto) { clearInterval(auto); auto = null; } el.querySelector('[data-a="play"]').textContent = "Play"; }
    el.addEventListener("click", e => {
      const d = e.target.closest("[data-i]"); if (d) { stop(); i = +d.dataset.i; render(i, true); return; }
      const a = e.target.closest("[data-a]"); if (!a) return;
      if (a.dataset.a === "next") { stop(); i = i === frames.length - 1 ? 0 : i + 1; render(i, i !== 0); }
      if (a.dataset.a === "back" && i > 0) { stop(); i--; render(i, true); }
      if (a.dataset.a === "hear") say(textOf(i), a);
      if (a.dataset.a === "play") {
        if (auto) { stop(); return; }
        a.textContent = "Pause"; if (i === frames.length - 1) { i = 0; render(0, false); }
        auto = setInterval(() => { if (i >= frames.length - 1) { stop(); return; } i++; render(i, true); }, 1900);
      }
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
    acheter: ["to buy", "er", "achète achètes achète achetons achetez achètent", "acheté"],
    porter: ["to wear, carry", "er", "porte portes porte portons portez portent", "porté"],
    ranger: ["to tidy up", "er", "range ranges range rangeons rangez rangent", "rangé"],
    fermer: ["to close", "er", "ferme fermes ferme fermons fermez ferment", "fermé"],
    voyager: ["to travel", "er", "voyage voyages voyage voyageons voyagez voyagent", "voyagé"],
    visiter: ["to visit (a place)", "er", "visite visites visite visitons visitez visitent", "visité"],
    "écouter": ["to listen to", "er", "écoute écoutes écoute écoutons écoutez écoutent", "écouté"],
    ouvrir: ["to open", "irr", "ouvre ouvres ouvre ouvrons ouvrez ouvrent", "ouvert"],
    "se dépêcher": ["to hurry", "refl", "dépêche dépêches dépêche dépêchons dépêchez dépêchent", "dépêché", 1],
    savoir: ["to know (facts, how to)", "irr", "sais sais sait savons savez savent", "su"],
    "connaître": ["to know (people, places)", "irr", "connais connais connaît connaissons connaissez connaissent", "connu"],
    dire: ["to say, tell", "irr", "dis dis dit disons dites disent", "dit"],
    croire: ["to believe", "irr", "crois crois croit croyons croyez croient", "cru"],
    envoyer: ["to send", "irr", "envoie envoies envoie envoyons envoyez envoient", "envoyé"],
    "réussir": ["to succeed", "ir", "réussis réussis réussit réussissons réussissez réussissent", "réussi"],
    "étudier": ["to study", "er", "étudie étudies étudie étudions étudiez étudient", "étudié"],
    travailler: ["to work", "er", "travaille travailles travaille travaillons travaillez travaillent", "travaillé"],
    "se souvenir": ["to remember", "refl", "souviens souviens souvient souvenons souvenez souviennent", "souvenu", 1],
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
  const IMPIRR = { "être": ["sois", "soyons", "soyez"], avoir: ["aie", "ayons", "ayez"] };
  function imper(key) {
    const [, kind, forms] = V[key]; const F = forms.split(" ");
    const isRefl = kind === "refl";
    let tu = F[1], nous = F[3], vous = F[4];
    if (IMPIRR[key]) [tu, nous, vous] = IMPIRR[key];
    else if (/es$/.test(tu) && (kind === "er" || kind === "refl" || key === "ouvrir")) tu = tu.slice(0, -1);
    else if (key === "aller") tu = "va";
    const rows = [["(tu)", tu, "-toi"], ["(nous)", nous, "-nous"], ["(vous)", vous, "-vous"]];
    return rows.map(([pron, f, r]) => ({ pron, lead: "", stem: f + (isRefl ? r : "") + " !", end: "" }));
  }

  /* college tenses */
  const FUT = { "être": "ser", avoir: "aur", aller: "ir", faire: "fer", venir: "viendr", pouvoir: "pourr", vouloir: "voudr", devoir: "devr", voir: "verr", savoir: "saur", envoyer: "enverr", acheter: "achèter", "se lever": "lèver", "se souvenir": "souviendr", courir: "courr" };
  const SUBJ = {
    "être": "sois sois soit soyons soyez soient", avoir: "aie aies ait ayons ayez aient", aller: "aille ailles aille allions alliez aillent",
    faire: "fasse fasses fasse fassions fassiez fassent", pouvoir: "puisse puisses puisse puissions puissiez puissent",
    savoir: "sache saches sache sachions sachiez sachent", vouloir: "veuille veuilles veuille voulions vouliez veuillent"
  };
  const E_IMPF = ["ais", "ais", "ait", "ions", "iez", "aient"], E_FUT = ["ai", "as", "a", "ons", "ez", "ont"], E_SUBJ = ["e", "es", "e", "ions", "iez", "ent"];
  const AUX_I = { a: "avais avais avait avions aviez avaient".split(" "), e: "étais étais était étions étiez étaient".split(" ") };
  const AUX_C = { a: "aurais aurais aurait aurions auriez auraient".split(" "), e: "serais serais serait serions seriez seraient".split(" ") };
  function impfStem(key) { if (key === "être") return "ét"; return V[key][2].split(" ")[3].replace(/ons$/, ""); }
  function futStem(key) { if (FUT[key]) return FUT[key]; const inf = key.replace(/^se |^s'/, ""); return /re$/.test(inf) ? inf.slice(0, -1) : inf; }
  const NEWT = { impf: 1, fut: 1, cond: 1, subj: 1, pqp: 1, cpass: 1 };
  function conj2(key, tense) {
    const [, kind, forms, pp, etre] = V[key]; const F = forms.split(" "); const isRefl = kind === "refl"; const be = etre || isRefl;
    return F.map((f, i) => {
      let stem, end = "", irr = false;
      if (tense === "impf") { stem = impfStem(key); end = E_IMPF[i]; }
      else if (tense === "fut") { stem = futStem(key); end = E_FUT[i]; }
      else if (tense === "cond") { stem = futStem(key); end = E_IMPF[i]; }
      else if (tense === "subj") {
        if (SUBJ[key]) { stem = SUBJ[key].split(" ")[i]; irr = true; }
        else { stem = (i === 3 || i === 4) ? impfStem(key) : F[5].replace(/ent$/, ""); end = E_SUBJ[i]; }
      } else {
        const aux = (tense === "pqp" ? AUX_I : AUX_C)[be ? "e" : "a"][i];
        const r = isRefl ? refl(i, aux) : "";
        let p2 = be ? agree(pp, i) : pp;
        if (i === 2 && be) p2 = pp + " / " + pp + "e";
        if (i === 5 && be) p2 = pp + "s / " + pp + "es";
        return { pron: PR[i], lead: subj(i, isRefl ? r : aux) + r + aux + " ", stem: p2, end: "" };
      }
      if (/^i/.test(end)) stem = stem.replace(/ge$/, "g").replace(/ç$/, "c");
      const word = stem + end;
      const r = isRefl ? refl(i, word) : "";
      let lead = isRefl ? subj(i, r) + r : subj(i, word);
      if (tense === "subj") lead = (/^(il|ils) /.test(lead) ? "qu'" : "que ") + lead;
      return { pron: PR[i], lead, stem, end, irr };
    });
  }
  window.FR.conj = (k, t) => (NEWT[t] ? conj2(k, t) : conj(k, t)).map(r => (r.lead + r.stem + r.end).replace(/ \/ .*$/, ""));
  function conj(key, tense) {
    if (NEWT[tense]) return conj2(key, tense);
    if (tense === "imp") return imper(key);
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
    const TN = { pres: "Present", pc: "Passé composé", fp: "Futur proche", imp: "Imperative (commands)", impf: "Imparfait", fut: "Futur simple", cond: "Conditionnel", subj: "Subjonctif présent", pqp: "Plus-que-parfait", cpass: "Conditionnel passé" };
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
      if (t === "impf") msg += ` · stem from <b>nous ${esc(V[k][2].split(" ")[3])}</b> → <b>${esc(impfStem(k))}-</b>${k === "être" ? " (être is the one exception: ét-)" : ""} + <span class="cj-end">-ais, -ais, -ait, -ions, -iez, -aient</span>`;
      if (t === "fut" || t === "cond") msg += ` · stem <b>${esc(futStem(k))}-</b>${FUT[k] ? " (irregular)" : ""} + <span class="cj-end">${t === "fut" ? "-ai, -as, -a, -ons, -ez, -ont" : "imparfait endings"}</span>`;
      if (t === "subj") msg += SUBJ[k] ? " · irregular subjunctive: learn it by heart" : ` · stem from <b>ils ${esc(V[k][2].split(" ")[5])}</b> → <b>${esc(V[k][2].split(" ")[5].replace(/ent$/, ""))}-</b>; nous / vous use the imparfait stem`;
      if (t === "pqp") msg += ` · <b>${(V[k][4] || V[k][1] === "refl") ? "être" : "avoir"}</b> in the imparfait + past participle <b>${esc(V[k][3])}</b>`;
      if (t === "cpass") msg += ` · <b>${(V[k][4] || V[k][1] === "refl") ? "être" : "avoir"}</b> in the conditionnel + past participle <b>${esc(V[k][3])}</b>`;
      if (t === "imp") msg += IMPIRR[k] ? " · irregular commands: learn these by heart" : d[1] === "er" || d[1] === "refl" || k === "aller" || k === "ouvrir" ? " · present tense without the subject; the tu form drops its <b>-s</b>" + (d[1] === "refl" ? ", and the pronoun goes <b>after</b> with a hyphen" : "") : " · present tense without the subject";
      info.innerHTML = msg;
      grid.innerHTML = rows.map(r => {
        const full = r.lead + r.stem + r.end;
        return `<button type="button" class="cj-row" data-say="${esc(full.replace(/il \/ elle/, "il").replace(/ !$/, ""))}"><span class="cj-p">${esc(r.pron)}</span><span class="cj-f">${esc(r.lead)}<b>${esc(r.stem)}</b><span class="cj-end">${esc(r.end)}</span></span></button>`;
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
    chat: ["m", "cat"], maison: ["f", "house"], chemise: ["f", "shirt"], pantalon: ["m", "pants"], robe: ["f", "dress"], manteau: ["m", "coat", "manteaux"], pull: ["m", "sweater"],
    jupe: ["f", "skirt"], "écharpe": ["f", "scarf"], "imperméable": ["m", "raincoat"], chaussure: ["f", "shoe"], chapeau: ["m", "hat", "chapeaux"], lit: ["m", "bed"], chambre: ["f", "bedroom"],
    salon: ["m", "living room"], cuisine: ["f", "kitchen"], armoire: ["f", "wardrobe"], fauteuil: ["m", "armchair"], lampe: ["f", "lamp"], "ordinateur": ["m", "computer"], "appartement": ["m", "apartment"], "frère": ["m", "brother"], "sœur": ["f", "sister"], "université": ["f", "university"], gâteau: ["m", "cake", "gâteaux"]
  };
  function arts(noun, pl) {
    const [g, , plf] = N[noun], v = vowel(noun), w = pl ? (plf || noun + "s") : noun;
    const def = pl ? "les " : v ? "l'" : g === "m" ? "le " : "la ";
    const ind = pl ? "des " : g === "m" ? "un " : "une ";
    const part = pl ? "des " : v ? "de l'" : g === "m" ? "du " : "de la ";
    const a = pl ? "aux " : v ? "à l'" : g === "m" ? "au " : "à la ";
    const de = pl ? "des " : v ? "de l'" : g === "m" ? "du " : "de la ";
    const poss = pl ? "mes " : g === "f" && !v ? "ma " : "mon ";
    const dem = pl ? "ces " : g === "f" ? "cette " : v ? "cet " : "ce ";
    return [["the", def + w, "le / la / l' / les"], ["a, some", ind + w, "un / une / des"], ["some (part of)", part + w, "du / de la / de l' / des"], ["to / at the", a + w, "à + le = au, à + les = aux"], ["of / from the", de + w, "de + le = du, de + les = des"], ["my", poss + w, "mon / ma / mes"], ["this / that", dem + w, "ce / cet / cette / ces"]];
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


  /* ---------------- countries ---------------- */
  const G = {
    France: ["f", "français", "française"], Canada: ["m", "canadien", "canadienne"], "États-Unis": ["pl", "américain", "américaine"], Mexique: ["m", "mexicain", "mexicaine"],
    Espagne: ["f", "espagnol", "espagnole"], Italie: ["f", "italien", "italienne"], Allemagne: ["f", "allemand", "allemande"], Angleterre: ["f", "anglais", "anglaise"],
    Belgique: ["f", "belge", "belge"], Suisse: ["f", "suisse", "suisse"], "Sénégal": ["m", "sénégalais", "sénégalaise"], Maroc: ["m", "marocain", "marocaine"],
    "Côte d'Ivoire": ["f", "ivoirien", "ivoirienne"], Chine: ["f", "chinois", "chinoise"], Japon: ["m", "japonais", "japonaise"], "Brésil": ["m", "brésilien", "brésilienne"],
    Iran: ["m", "iranien", "iranienne"], "Pays-Bas": ["pl", "néerlandais", "néerlandaise"], "Viêt Nam": ["m", "vietnamien", "vietnamienne"], "Haïti": ["city", "haïtien", "haïtienne"]
  };
  function geoRows(c) {
    const [g, nm, nf] = G[c], v = vowel(c);
    if (g === "city") return [["the place", c, "a few islands work like cities: no article"], ["in / to", "à " + c, "à + city"], ["from", "d'" + c, "de + city"], ["nationality", nm + " / " + nf, "lowercase"]];
    const the = g === "pl" ? "les " + c : v ? "l'" + c : (g === "m" ? "le " : "la ") + c;
    const inn = g === "pl" ? "aux " + c : g === "f" || v ? "en " + c : "au " + c;
    const frm = g === "pl" ? "des " + c : g === "f" || v ? (v ? "d'" : "de ") + c : "du " + c;
    const rule = g === "pl" ? "plural → aux / des" : g === "f" ? "feminine → en / de" : v ? "masculine but starts with a vowel → en / d'" : "masculine → au / du";
    return [["the country", the, rule], ["in / to", inn, "J'habite " + inn + "."], ["from", frm, "Je viens " + frm + "."], ["nationality", nm + " / " + nf, "lowercase as an adjective"]];
  }
  function labGeo(el) {
    el.innerHTML = `<div class="lab-h">Countries lab <span>Pick a country. The little word depends on its gender.</span></div>
      <div class="lab-row"><select class="lab-in" data-k="c">${Object.keys(G).map(k => `<option>${esc(k)}</option>`).join("")}</select><span class="gtag"></span></div><div class="ar-grid"></div>`;
    function upd() {
      const c = el.querySelector("select").value, g = G[c][0];
      el.querySelector(".gtag").innerHTML = g === "pl" ? '<span class="g-m">plural</span>' : g === "city" ? "no article" : `<span class="g-${g}">${g === "m" ? "masculine" : "feminine"}</span>`;
      el.querySelector(".ar-grid").innerHTML = geoRows(c).map(([en, fr, rule]) => `<button type="button" class="ar-row" data-say="${esc(fr.replace(" / ", ", "))}"><span class="ar-en">${esc(en)}</span><b>${esc(fr)}</b><span class="ar-rule">${esc(rule)}</span></button>`).join("");
      if (!reduce()) el.querySelectorAll(".ar-row b").forEach((e, j) => e.animate([{ opacity: 0, transform: "translateX(-8px)" }, { opacity: 1, transform: "none" }], { duration: 300, delay: 40 * j, fill: "backwards" }));
    }
    el.querySelector("select").addEventListener("change", upd); upd();
  }

  /* ---------------- where is the cat? ---------------- */
  const PP = {
    sur: ["sur la table", "on", 205, 92, 1, 1], sous: ["sous la table", "under", 205, 178, 1, 1], devant: ["devant la table", "in front of", 160, 196, 1.18, 1],
    "derrière": ["derrière la table", "behind", 262, 162, .82, 0], "à côté de": ["à côté de la table", "next to", 352, 178, 1, 1],
    dans: ["dans le panier", "in", 462, 150, .9, 2], entre: ["entre la table et le panier", "between", 382, 178, 1, 1], "loin de": ["loin de la table", "far from", 560, 178, .9, 1]
  };
  function labPrep(el) {
    el.innerHTML = `<div class="lab-h">Where's the cat? <span>Tap a preposition and watch the cat move.</span></div>
      <div class="pp-btns">${Object.keys(PP).map((k, i) => `<button type="button" class="wa-b${i ? "" : " solid"}" data-p="${esc(k)}">${esc(k)}</button>`).join("")}</div>
      <svg class="pp-svg" viewBox="0 0 620 240" aria-hidden="true">
        <line x1="10" y1="226" x2="610" y2="226" class="pp-floor"/>
        <g class="pp-cat"><g class="pp-cat-in">
          <ellipse cx="0" cy="-16" rx="26" ry="17"/><circle cx="20" cy="-36" r="13"/><path d="M11 -45l3 -14 9 9zM25 -47l7 -12 3 13z"/>
          <path class="pp-tail" d="M-24 -18c-18 -4 -20 -26 -8 -34" fill="none" stroke-width="6" stroke-linecap="round"/>
          <circle cx="24" cy="-38" r="2" class="pp-eye"/><circle cx="17" cy="-38" r="2" class="pp-eye"/></g></g>
        <g class="pp-table"><rect x="140" y="100" width="150" height="12" rx="3"/><rect x="150" y="112" width="9" height="114"/><rect x="271" y="112" width="9" height="114"/></g>
        <g class="pp-basket"><path d="M420 178h92l-10 48h-72z"/><path class="h" d="M426 178c6 -34 74 -34 80 0"/></g>
      </svg>
      <div class="pp-out"><b class="ad-ph"></b><button type="button" class="saybtn" aria-label="Hear it"></button></div><div class="ad-why"></div>`;
    const svg = el.querySelector("svg"), cat = el.querySelector(".pp-cat"), table = el.querySelector(".pp-table");
    function go(k) {
      const [where, en, x, y, sc, front] = PP[k];
      cat.style.transform = `translate(${x}px,${y + 48}px) scale(${sc})`;
      if (front === 1) svg.insertBefore(cat, null); else svg.insertBefore(cat, front === 2 ? el.querySelector(".pp-basket") : table);
      const t = `Le chat est ${where}.`;
      el.querySelector(".ad-ph").textContent = t; el.querySelector(".saybtn").dataset.say = t;
      el.querySelector(".ad-why").innerHTML = `<b>${esc(k)}</b> = ${en}` + (/de$/.test(k) ? `. de + le = <b>du</b>, de + les = <b>des</b>: ${esc(k.replace(/de$/, "du"))} lit.` : "");
      el.querySelectorAll("[data-p]").forEach(b => b.classList.toggle("solid", b.dataset.p === k));
    }
    el.addEventListener("click", e => { const b = e.target.closest("[data-p]"); if (b) { go(b.dataset.p); say(el.querySelector(".ad-ph").textContent); } });
    go("sur");
  }

  /* ---------------- word bank ---------------- */
  const POS = { v: "verb", nm: "m.", nf: "f.", nmf: "m./f.", nmpl: "m. pl.", nfpl: "f. pl.", a: "adj.", adv: "adv.", pr: "pron.", prep: "prep.", conj: "conj.", det: "det.", num: "num.", int: "expr." };
  const GROUP = { all: () => true, n: p => p[0] === "n", v: p => p === "v", a: p => p === "a", adv: p => p === "adv", other: p => !/^(n|v$|a$|adv$)/.test(p) };
  function labVocab(el) {
    const src = document.getElementById("fr-words"); if (!src) return;
    const W = JSON.parse(src.textContent).map((w, i) => ({ r: i + 1, fr: w[0], p: w[1], en: w[2], key: (w[0] + " " + w[2]).toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "") }));
    const ranges = Math.ceil(W.length / 100);
    el.innerHTML = `<div class="vb-bar">
        <input class="lab-in vb-q" type="search" placeholder="Search French or English…" aria-label="Search words">
        <select class="lab-in vb-r" aria-label="Words by rank"><option value="all">All ${W.length} words</option>${Array.from({ length: ranges }, (_, i) => `<option value="${i}">Words ${i * 100 + 1}–${Math.min(W.length, i * 100 + 100)}</option>`).join("")}</select>
        <label class="tg"><input type="checkbox" class="vb-hide"> Hide English</label>
        <button type="button" class="wa-b solid vb-quiz">Quiz me: 10 words</button></div>
      <div class="vb-types">${[["all", "All"], ["n", "Nouns"], ["v", "Verbs"], ["a", "Adjectives"], ["adv", "Adverbs"], ["other", "Other"]].map(([k, l], i) => `<button type="button" class="wa-b${i ? "" : " solid"}" data-g="${k}">${l}</button>`).join("")}<span class="vb-n"></span></div>
      <div class="vb-qz" hidden></div>
      <div class="vb-list" role="list"></div>`;
    const list = el.querySelector(".vb-list"), qz = el.querySelector(".vb-qz");
    let g = "all", shown = [];
    const norm = s => s.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "");
    function filter() {
      const q = norm(el.querySelector(".vb-q").value.trim()), r = el.querySelector(".vb-r").value;
      return W.filter(w => GROUP[g](w.p) && (r === "all" || Math.floor((w.r - 1) / 100) === +r) && (!q || w.key.includes(q)));
    }
    function draw() {
      shown = filter();
      el.querySelector(".vb-n").textContent = shown.length + (shown.length === 1 ? " word" : " words");
      list.innerHTML = shown.map(w => `<div class="vb-row" role="listitem"><span class="vb-rk">${w.r}</span><button type="button" class="vb-fr" data-say="${esc(w.fr.replace(/\(.*?\)/g, ""))}">${esc(w.fr)}</button><span class="vb-pos p-${w.p.replace(/pl$/, "")}">${POS[w.p] || w.p}</span><span class="vb-en" tabindex="0">${esc(w.en)}</span></div>`).join("") || '<p class="vb-none">No words match.</p>';
    }
    el.querySelector(".vb-q").addEventListener("input", draw);
    el.querySelector(".vb-r").addEventListener("change", draw);
    el.querySelector(".vb-hide").addEventListener("change", e => el.classList.toggle("hide-en", e.target.checked));
    el.addEventListener("click", e => {
      const b = e.target.closest("[data-g]"); if (b) { g = b.dataset.g; el.querySelectorAll("[data-g]").forEach(x => x.classList.toggle("solid", x === b)); draw(); }
      const en = e.target.closest(".vb-en"); if (en && el.classList.contains("hide-en")) en.classList.toggle("show");
    });
    // quiz
    let Q = [], qi = 0, score = 0, missed = [];
    const shuffle = a => { for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
    function ask() {
      if (qi >= Q.length) {
        qz.innerHTML = `<div class="vb-qh">Score: <b>${score} / ${Q.length}</b></div>${missed.length ? `<p>Words to review:</p><div class="vgrid">${missed.map(w => `<div class="vc"><button type="button" class="vb-fr" data-say="${esc(w.fr)}">${esc(w.fr)}</button><span>${esc(w.en)}</span></div>`).join("")}</div>` : "<p>Perfect, every word right!</p>"}<div class="wa-ctl"><button type="button" class="wa-b solid" data-qz="again">Another 10</button><button type="button" class="wa-b" data-qz="close">Close</button></div>`;
        return;
      }
      const w = Q[qi], pool = (shown.length >= 8 ? shown : W).filter(x => x.en !== w.en);
      const opts = shuffle([w, ...shuffle(pool.slice()).slice(0, 3)]);
      qz.innerHTML = `<div class="vb-qh">Word ${qi + 1} of ${Q.length} · ${score} right</div>
        <div class="vb-qw"><button type="button" class="vb-fr big" data-say="${esc(w.fr.replace(/\(.*?\)/g, ""))}">${esc(w.fr)}</button> <span class="vb-pos">${POS[w.p] || ""}</span></div>
        <div class="vb-opts">${opts.map(o => `<button type="button" class="opt" data-ok="${o === w ? 1 : 0}">${esc(o.en)}</button>`).join("")}</div>`;
      say(w.fr.replace(/\(.*?\)/g, ""));
    }
    function start() {
      const base = shown.length >= 4 ? shown : W;
      Q = shuffle(base.slice()).slice(0, 10); qi = 0; score = 0; missed = [];
      qz.hidden = false; ask(); qz.scrollIntoView({ behavior: reduce() ? "auto" : "smooth", block: "center" });
    }
    el.querySelector(".vb-quiz").addEventListener("click", start);
    qz.addEventListener("click", e => {
      const o = e.target.closest(".opt[data-ok]");
      if (o && !qz.querySelector(".opt.right")) {
        const ok = o.dataset.ok === "1";
        o.classList.add(ok ? "right" : "wrong"); qz.querySelector('[data-ok="1"]').classList.add("right");
        if (ok) score++; else missed.push(Q[qi]);
        setTimeout(() => { qi++; ask(); }, ok ? 650 : 1400);
      }
      const c = e.target.closest("[data-qz]");
      if (c) { if (c.dataset.qz === "again") start(); else { qz.hidden = true; qz.innerHTML = ""; } }
    });
    draw();
  }

  /* ---------------- passé composé vs imparfait timeline ---------------- */
  function labTl(el, p) {
    const items = p.items;
    el.innerHTML = `<div class="lab-h">Timeline lab <span>Imparfait = the background (a long stretch). Passé composé = an event (a single point).</span></div>
      <div class="lab-row"><select class="lab-in tl-s">${items.map((x, i) => `<option value="${i}">${esc(x.parts.map(q => q[0]).join(""))}</option>`).join("")}</select></div>
      <div class="tl-sent"></div><svg class="tl-svg" viewBox="0 0 620 150" aria-hidden="true"></svg><div class="ad-why tl-why"></div>`;
    const svg = el.querySelector("svg");
    function upd() {
      const it = items[+el.querySelector(".tl-s").value];
      const text = it.parts.map(q => q[0]).join("");
      el.querySelector(".tl-sent").innerHTML = it.parts.map(([t, k]) => k ? `<span class="tl-${k}">${esc(t)}</span>` : esc(t)).join("") + sayBtn(text) + `<div class="wa-en">${esc(it.en)}</div>`;
      const bg = it.parts.filter(q => q[1] === "i"), ev = it.parts.filter(q => q[1] === "p");
      let h = `<line x1="20" y1="118" x2="600" y2="118" class="tl-axis"/><path d="M600 118l-10-6v12z" class="tl-arrow"/><text x="22" y="140" class="tl-lab">past</text><text x="560" y="140" class="tl-lab">now</text>`;
      bg.forEach((q, j) => { const y = 74 - j * 34; h += `<rect x="40" y="${y}" width="500" height="22" rx="11" class="tl-band"/><path d="M48 ${y + 11}${Array.from({ length: 24 }, (_, k) => `q10 ${k % 2 ? 7 : -7} 20 0`).join("")}" class="tl-wave"/><text x="290" y="${y - 6}" text-anchor="middle" class="tl-bt">${esc(q[0].trim())}</text>`; });
      ev.forEach((q, j) => { const x = ev.length === 1 ? 330 : 170 + j * (300 / Math.max(1, ev.length - 1)); h += `<g class="tl-ev" style="--d:${0.5 + j * 0.35}s"><line x1="${x}" y1="${bg.length ? 30 : 60}" x2="${x}" y2="118" class="tl-pin"/><circle cx="${x}" cy="118" r="7" class="tl-dot"/><text x="${x}" y="${bg.length ? 22 : 52}" text-anchor="middle" class="tl-et">${esc(q[0].trim())}</text></g>`; });
      svg.innerHTML = h;
      el.querySelector(".tl-why").innerHTML = it.why;
    }
    el.querySelector("select").addEventListener("change", upd); upd();
  }

  /* ---------------- pronoun order ---------------- */
  const ORDER = ["me te se nous vous", "le la les", "lui leur", "y", "en"];
  const rank = pr => ORDER.findIndex(g => g.split(" ").includes(pr));
  function elide(tokens) {
    const out = [];
    for (let i = 0; i < tokens.length; i++) {
      const t = tokens[i], n = tokens[i + 1];
      if (n && /^(je|me|te|se|le|la|ne|de)$/i.test(t) && vowel(n)) out.push(t.slice(0, -1) + "'");
      else out.push(t);
    }
    return out.join(" ").replace(/' /g, "'");
  }
  function labPron(el, p) {
    const items = p.items;
    el.innerHTML = `<div class="lab-h">Pronoun lab <span>Replace the objects and watch where the pronouns go.</span></div>
      <div class="lab-row"><select class="lab-in pr-s">${items.map((x, i) => `<option value="${i}">${esc(elide([x.s, ...(x.pre ? [x.pre] : []), x.v]) + " " + x.o.map(o => o[1]).join(" "))}</option>`).join("")}</select><label class="tg"><input type="checkbox" class="pr-neg"> negative</label></div>
      <div class="pr-boxes"></div><div class="ng-out pr-out"></div>
      <div class="pr-order">${ORDER.map((g, i) => `<span data-r="${i}">${esc(g.replace(/ /g, " / "))}</span>`).join('<i>→</i>')}</div><div class="ad-why pr-why"></div>`;
    function boxes() {
      const it = items[+el.querySelector(".pr-s").value];
      el.querySelector(".pr-boxes").innerHTML = it.o.map((o, i) => `<label class="tg pr-b"><input type="checkbox" data-i="${i}" checked> ${esc(o[1])} → <b>${esc(o[2])}</b></label>`).join("");
      el.querySelectorAll(".pr-b input").forEach(c => c.addEventListener("change", upd)); upd();
    }
    function upd() {
      const it = items[+el.querySelector(".pr-s").value], neg = el.querySelector(".pr-neg").checked;
      const on = [...el.querySelectorAll(".pr-b input")].map(c => c.checked);
      const prons = [...(it.pre ? [it.pre] : []), ...it.o.filter((_, i) => on[i]).map(o => o[2])].sort((a, b) => rank(a) - rank(b));
      let rest = it.o.filter((_, i) => !on[i]).map(o => o[1]);
      if (neg) rest = rest.map(r => r.replace(/^(des|du|de la|un|une) (?=[^aeiouhéèêàâîôû])/i, "de ").replace(/^(des|du|de la|de l'|un|une) ?(?=[aeiouhéèêàâîôû])/i, "d'"));
      const toks = [it.s.toLowerCase(), ...(neg ? ["ne"] : []), ...prons, it.v, ...(neg ? ["pas"] : [])];
      let sent = elide(toks) + (rest.length ? " " + rest.join(" ") : "");
      sent = sent[0].toUpperCase() + sent.slice(1) + ".";
      el.querySelector(".pr-out").innerHTML = `<b class="ad-ph">${esc(sent)}</b>${sayBtn(sent)}`;
      el.querySelectorAll(".pr-order span").forEach(s => s.classList.toggle("on", prons.some(pr => rank(pr) === +s.dataset.r)));
      const why = [];
      if (prons.length) why.push("Object pronouns go right <b>before the conjugated verb</b>" + (neg ? ", inside ne … pas" : "") + ".");
      if (prons.length > 1) why.push(`Two pronouns follow the fixed order: <b>${prons.join(" + ")}</b>.`);
      if (prons.includes("en")) why.push("<b>en</b> replaces a noun with du / de la / des or a quantity, and always comes last.");
      if (prons.includes("y")) why.push("<b>y</b> replaces a place (à, en, dans, chez + place) or à + a thing.");
      if (prons.some(x => x === "lui" || x === "leur")) why.push("<b>lui / leur</b> replace à + a person.");
      el.querySelector(".pr-why").innerHTML = why.map(w => `<div>${w}</div>`).join("") || "<div>Tick an object to replace it.</div>";
      if (!reduce()) el.querySelector(".pr-out .ad-ph").animate([{ opacity: .3, transform: "translateY(4px)" }, { opacity: 1, transform: "none" }], { duration: 300 });
    }
    el.querySelector(".pr-s").addEventListener("change", boxes); el.querySelector(".pr-neg").addEventListener("change", upd); boxes();
  }

  /* ---------------- si clauses ---------------- */
  const SUBJS = ["je", "tu", "il", "nous", "vous", "ils"];
  function labSi(el, p) {
    const sc = p.items;
    const T = { 1: ["pres", "fut", "Real possibility", "si + présent → futur"], 2: ["impf", "cond", "Hypothetical (now / future)", "si + imparfait → conditionnel"], 3: ["pqp", "cpass", "Didn't happen (past)", "si + plus-que-parfait → conditionnel passé"] };
    el.innerHTML = `<div class="lab-h">Si clause builder <span>Pick a situation, a subject and how likely it is.</span></div>
      <div class="lab-row"><select class="lab-in si-c">${sc.map((x, i) => `<option value="${i}">${esc(x.en)}</option>`).join("")}</select>
      <select class="lab-in si-p">${SUBJS.map((x, i) => `<option value="${i}">${x}</option>`).join("")}</select></div>
      <div class="pp-btns">${[1, 2, 3].map(t => `<button type="button" class="wa-b${t === 1 ? " solid" : ""}" data-t="${t}">${T[t][2]}</button>`).join("")}</div>
      <div class="si-out"></div><div class="ad-why si-why"></div>`;
    let t = 1;
    function upd() {
      const x = sc[+el.querySelector(".si-c").value], i = +el.querySelector(".si-p").value;
      const c = window.FR.conj(x.c[0], T[t][0])[i] + (x.c[1] ? " " + x.c[1] : ""), r = window.FR.conj(x.r[0], T[t][1])[i] + (x.r[1] ? " " + x.r[1] : "");
      const sent = ("Si " + c).replace(/^Si il/, "S'il") + ", " + r + ".";
      el.querySelector(".si-out").innerHTML = `<div class="si-row"><span class="si-tag a">si + ${{ pres: "présent", impf: "imparfait", pqp: "plus-que-parfait" }[T[t][0]]}</span><span class="si-tag b">${{ fut: "futur", cond: "conditionnel", cpass: "conditionnel passé" }[T[t][1]]}</span></div><b class="ad-ph">${esc(sent)}</b>${sayBtn(sent)}`;
      el.querySelector(".si-why").innerHTML = `<div><b>${T[t][3]}</b>. ${t === 1 ? "It could really happen." : t === 2 ? "Imagining: it isn't true now, or probably won't happen." : "Regret or imagining a different past: it didn't happen."}</div><div>Never put the futur or the conditionnel right after <b>si</b>. You can also flip the halves: the result clause first, then si.</div>`;
      el.querySelectorAll("[data-t]").forEach(b => b.classList.toggle("solid", +b.dataset.t === t));
      if (!reduce()) el.querySelector(".si-out .ad-ph").animate([{ opacity: .2 }, { opacity: 1 }], { duration: 300 });
    }
    el.addEventListener("click", e => { const b = e.target.closest("[data-t]"); if (b) { t = +b.dataset.t; upd(); } });
    el.querySelectorAll("select").forEach(s => s.addEventListener("change", upd)); upd();
  }

  /* ---------------- subjunctive or indicative ---------------- */
  function labMood(el, p) {
    const TR = p.triggers, VB = p.verbs;
    el.innerHTML = `<div class="lab-h">Subjunctive or indicative? <span>The expression before que decides the mood.</span></div>
      <div class="lab-row"><select class="lab-in md-t">${TR.map((x, i) => `<option value="${i}">${esc(x[0])} que…</option>`).join("")}</select>
      <select class="lab-in md-p">${SUBJS.map((x, i) => `<option value="${i}"${i === 1 ? " selected" : ""}>${x}</option>`).join("")}</select>
      <select class="lab-in md-v">${VB.map((x, i) => `<option value="${i}">${esc(x[0] + (x[1] ? " " + x[1] : ""))}</option>`).join("")}</select></div>
      <div class="md-tag"></div><div class="md-out"></div><div class="ad-why md-why"></div>`;
    function upd() {
      const tr = TR[+el.querySelector(".md-t").value], i = +el.querySelector(".md-p").value, vb = VB[+el.querySelector(".md-v").value];
      const subjMood = tr[1] === "s";
      const mainIsJe = /^(Je|J')/.test(tr[0]);
      let sent, why = [`<b>${esc(tr[0])}</b> expresses ${esc(tr[2])} → <b>${subjMood ? "subjunctive" : "indicative"}</b>.`];
      if (subjMood && mainIsJe && i === 0 && tr.length > 3) {
        const prep = tr[3] === "de" && vowel(vb[0]) ? "d'" : tr[3] ? tr[3] + " " : "";
        sent = `${tr[0]} ${prep}${vb[0]}${vb[1] ? " " + vb[1] : ""}.`;
        why.push("Same subject in both halves (je … je): use an <b>infinitive</b> instead of que + subjunctive.");
      } else {
        let f = window.FR.conj(vb[0], subjMood ? "subj" : "pres")[i];
        if (!subjMood) f = (/^(il|ils) /.test(f) ? "qu'" : "que ") + f;
        sent = `${tr[0]} ${f}${vb[1] ? " " + vb[1] : ""}` + (/^(Bien|Pour|Avant|Sans|Parce)$/.test(tr[0]) ? "…" : ".");
      }
      el.querySelector(".md-tag").innerHTML = `<span class="si-tag ${subjMood ? "b" : "a"}">${subjMood ? "subjonctif" : "indicatif"}</span>`;
      el.querySelector(".md-out").innerHTML = `<b class="ad-ph">${esc(sent)}</b>${sayBtn(sent)}`;
      el.querySelector(".md-why").innerHTML = why.map(w => `<div>${w}</div>`).join("");
      if (!reduce()) el.querySelector(".md-out .ad-ph").animate([{ opacity: .2 }, { opacity: 1 }], { duration: 300 });
    }
    el.querySelectorAll("select").forEach(s => s.addEventListener("change", upd)); upd();
  }
  const LABS = { tl: labTl, pron: labPron, si: labSi, mood: labMood, vocab: labVocab, geo: labGeo, prep: labPrep, conj: labConj, num: labNum, clock: labClock, noun: labNoun, adj: labAdj, neg: labNeg };
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
