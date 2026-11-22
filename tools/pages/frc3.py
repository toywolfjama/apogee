from fr_common import *

SI = [
 {"en": "have time → travel in Europe", "c": ["avoir", "le temps"], "r": ["voyager", "en Europe"]},
 {"en": "study more → pass the exam", "c": ["étudier", "plus"], "r": ["réussir", "l'examen"]},
 {"en": "be rich → buy a house in Paris", "c": ["être", "riche"], "r": ["acheter", "une maison à Paris"]},
 {"en": "go to France → speak French every day", "c": ["aller", "en France"], "r": ["parler", "français tous les jours"]},
 {"en": "know the answer → tell the truth", "c": ["savoir", "la réponse"], "r": ["dire", "la vérité"]},
 {"en": "get up earlier → arrive on time", "c": ["se lever", "plus tôt"], "r": ["arriver", "à l'heure"]},
 {"en": "can → come to the party", "c": ["pouvoir", ""], "r": ["venir", "à la fête"]},
]

CH = []
CORE = f'''<p>This unit covers talking about the future precisely, being polite, and imagining things that aren't (or weren't) true. Both new tenses use the <b>same stem</b>, so learning one gives you most of the other.</p>
{wa("Future, conditional, hypothetical", [
 ("a|Si|gl  b|j'ai|v  c|le temps,|x  d|je|s  e|voyagerai.|n", "Real possibility: si + present → futur.", "If I have time, I'll travel."),
 ("a|Si|gl  b|j'avais|v  c|le temps,|x  d|je|s  e|voyagerais.|n", "Imagining: si + imparfait → conditionnel.", "If I had time, I would travel."),
 ("a|Si|gl  b|j'avais eu|v  c|le temps,|x  d|j'|s  e|aurais voyagé.|n", "Regret: si + plus-que-parfait → conditionnel passé.", "If I had had time, I would have traveled.")])}'''
CH.append(chapter("overview-c3", "Overview", "Overview", [topic("core-c3", "Le futur et le conditionnel", CORE)]))

FUT = topic("futur-simple", "The futur simple", f'''
<p>Stem = the <b>infinitive</b> (drop the final -e of -re verbs). Endings = the present of avoir: <b>-ai, -as, -a, -ons, -ez, -ont</b>.</p>
{ex("Je parlerai, tu finiras, il vendra, nous prendrons, vous écrirez, ils boiront.", "I will speak, you'll finish, he'll sell, we'll take, you'll write, they'll drink.")}
<h3>Irregular stems</h3>
{vgrid([("être → ser-", "je serai"), ("avoir → aur-", "j'aurai"), ("aller → ir-", "j'irai"), ("faire → fer-", "je ferai"), ("venir → viendr-", "je viendrai"), ("pouvoir → pourr-", "je pourrai"), ("vouloir → voudr-", "je voudrai"), ("devoir → devr-", "je devrai"), ("voir → verr-", "je verrai"), ("savoir → saur-", "je saurai"), ("envoyer → enverr-", "j'enverrai"), ("falloir → faudr-", "il faudra"), ("pleuvoir → pleuvr-", "il pleuvra"), ("acheter → achèter-", "j'achèterai")])}
{lab(type="conj", verbs=["parler", "finir", "vendre", "être", "avoir", "aller", "faire", "venir", "pouvoir", "vouloir", "voir", "savoir", "acheter", "se lever"], tenses=["fut", "cond"])}
<h3>Futur simple vs futur proche</h3>
<p>The futur proche ({F("je vais partir")}) is for plans and things about to happen, and is more common in speech. The futur simple ({F("je partirai")}) is more formal, more distant, or used for predictions and promises: {F("Un jour, je serai médecin.")}</p>
<h3>After quand, lorsque, dès que, aussitôt que</h3>
<p>When the main verb is future, these time words are followed by the <b>future</b> too, unlike English: {F("Quand je serai grand, je voyagerai.")} (When I <i>grow up</i>…) {F("Appelle-moi dès que tu arriveras.")}</p>
''', pill=("g", "C3.1"), sub="je parlerai, je serai, j'irai.",
 det=("The futur antérieur", '''<h4>Will have done</h4><p>Form: avoir / être in the futur simple + past participle. <i>J'aurai fini à six heures.</i> (I'll have finished by six.)</p>
<h4>With quand and dès que</h4><p>For an action that will be completed before another future one: <i>Quand tu auras fini tes devoirs, tu pourras sortir.</i> English says "when you have finished".</p>
<h4>Si never takes the future</h4><p>The time words above take the future, but <i>si</i> (if) never does: <i>Si tu viens</i>, not "si tu viendras".</p>'''))

COND = topic("conditionnel", "The conditionnel", f'''
<p>Same stem as the future + the <b>imparfait endings</b>: <b>-ais, -ais, -ait, -ions, -iez, -aient</b>.</p>
{ex("Je parlerais, je serais, j'aurais, j'irais, je ferais, je pourrais, je voudrais.", "I would speak, be, have, go, do, be able to, want.")}
<h3>When to use it</h3>
<div class="grid2"><div class="mini"><h4>Politeness</h4><p>{F("Je voudrais un café.")} {F("Pourriez-vous m'aider ?")} {F("Tu devrais te reposer.")} (You should rest.)</p></div>
<div class="mini"><h4>Wishes and hypotheses</h4><p>{F("J'aimerais vivre à Paris.")} {F("À ta place, je partirais.")} (If I were you, I'd leave.)</p></div>
<div class="mini"><h4>Future in the past</h4><p>{F("Il a dit qu'il viendrait.")} (He said he would come.)</p></div>
<div class="mini"><h4>Unconfirmed news</h4><p>{F("Le président serait malade.")} (The president is reportedly ill.) Common in journalism.</p></div></div>
{box("trap", "Futur vs conditionnel for je", f"{F('je parlerai')} (will) and {F('je parlerais')} (would) sound almost alike in fast speech. In writing, check the ending: -ai = future, -ais = conditional.")}
''', pill=("g", "C3.2"), sub="would, could, should.")
CH.append(chapter("fut-c3", "Futur et conditionnel", "Future & cond.", [FUT, COND]))

SIC = topic("si-clauses", "Si clauses: if … then", f'''
<div class="tblwrap"><table><tr><th>Type</th><th>Si clause</th><th>Result clause</th><th>Example</th></tr>
<tr><td>1. Real</td><td>présent</td><td>futur (or présent, impératif)</td><td>{F("S'il pleut, je resterai chez moi.")}</td></tr>
<tr><td>2. Hypothetical</td><td>imparfait</td><td>conditionnel</td><td>{F("Si j'étais toi, j'accepterais.")}</td></tr>
<tr><td>3. Past unreal</td><td>plus-que-parfait</td><td>conditionnel passé</td><td>{F("Si tu m'avais appelé, je serais venu.")}</td></tr></table></div>
{lab(type="si", items=SI)}
<h3>The conditionnel passé</h3>
<p>avoir / être in the <b>conditionnel</b> + past participle: {F("j'aurais aimé")} (I would have liked), {F("elle serait partie")} (she would have left). Also used for regrets: {F("J'aurais dû étudier.")} (I should have studied.) {F("Tu aurais pu me le dire !")} (You could have told me!)</p>
{box("trap", "The golden rule", f"Never use the futur or the conditionnel right after <b>si</b> meaning <i>if</i>. {F('Si j’aurais su…')} is a famous mistake; it's {F('Si j’avais su…')} (If I had known…).")}
''', pill=("g", "C3.3"), sub="Three patterns that cover almost every if-sentence.",
 det=("Si clause details", '''<h4>Si + il</h4><p>si elides only before il and ils: <i>s'il, s'ils</i>, but <i>si elle, si on</i>.</p>
<h4>Mixed time frames</h4><p>You can mix types when the logic requires it: <i>Si j'avais étudié, je serais médecin aujourd'hui</i> (past condition, present result: plus-que-parfait + conditionnel présent).</p>
<h4>Si meaning whether</h4><p>When si means "whether" (indirect question), the future and conditional are fine: <i>Je ne sais pas s'il viendra.</i></p>'''))
CH.append(chapter("si-c3", "Les phrases avec si", "Si clauses", [SIC]))

REV = topic("review-c3", "Unit summary", f'''<div class="grid2"><div class="mini"><h4>Futur simple</h4><p>infinitive (-re → -r) + ai, as, a, ons, ez, ont. Irregular stems: ser-, aur-, ir-, fer-, viendr-, pourr-, voudr-, devr-, verr-, saur-.</p></div>
<div class="mini"><h4>Conditionnel</h4><p>Future stem + imparfait endings. Politeness, wishes, hypotheses, future in the past.</p></div>
<div class="mini"><h4>Si clauses</h4><p>présent → futur · imparfait → conditionnel · plus-que-parfait → conditionnel passé.</p></div>
<div class="mini"><h4>Quand + futur</h4><p>Quand je serai… Dès que tu auras fini… But never si + futur.</p></div></div>''', sub="Everything from this unit on one screen.")
MIS = topic("mistakes-c3", "Common mistakes", '''<ol class="steps">
<li><i>Si j'aurais</i> → <i>Si j'avais</i>.</li>
<li><i>Quand je suis grand, je serai…</i> → <i>Quand je serai grand…</i></li>
<li><i>je vendreai</i> → <i>je vendrai</i> (drop the -e of -re verbs).</li>
<li><i>j'allerai</i> → <i>j'irai</i>; <i>je fairai</i> → <i>je ferai</i>.</li>
<li>Confusing -ai (future) and -ais (conditional) in writing.</li>
<li><i>J'aurais dû étudier</i> means "I should have studied", not "I would have to".</li></ol>''', sub="Points students lose most often.")
CH.append(chapter("review-ch-c3", "Review", "Review", [REV, MIS]))

PQ = [
 q("Futur of <i>parler</i>, nous:", ["parlerons", "parlons", "parlerions", "parlrons"], 0, "infinitive + ons.", "g"),
 q("Futur of <i>vendre</i>, je:", ["vendrai", "vendreai", "vendrais", "vendai"], 0, "Drop the e: vendr- + ai.", "g"),
 q("Futur of <i>être</i>, ils:", ["seront", "éteront", "seraient", "sont"], 0, "ser- + ont.", "g"),
 q("Futur of <i>aller</i>, tu:", ["iras", "alleras", "vas", "irais"], 0, "ir- + as.", "g"),
 q("Futur of <i>faire</i>, vous:", ["ferez", "fairez", "faisez", "feriez"], 0, "fer- + ez.", "g"),
 q("Futur of <i>venir</i>, elle:", ["viendra", "venira", "viendrait", "vienra"], 0, "viendr- + a.", "g"),
 q("<i>Quand tu ______ à Paris, appelle-moi !</i>", ["arriveras", "arrives", "arriverais", "arrivais"], 0, "quand + future meaning → futur.", "g"),
 q("Conditionnel of <i>vouloir</i>, je:", ["voudrais", "voulerais", "voudrai", "voulais"], 0, "voudr- + ais.", "g"),
 q("Conditionnel of <i>pouvoir</i>, vous (polite request):", ["pourriez", "pouvez", "pourrez", "pouviez"], 0, "pourr- + iez.", "g"),
 q("<i>Tu ______ te reposer.</i> (You should rest.)", ["devrais", "devras", "dois", "devais"], 0, "devoir in the conditionnel = should.", "g"),
 q("<i>Il a dit qu'il ______ demain.</i>", ["viendrait", "viendra", "venait", "vient"], 0, "Future in the past → conditionnel.", "g"),
 q("<i>S'il fait beau, nous ______ à la plage.</i>", ["irons", "irions", "allions", "serions allés"], 0, "Type 1: présent → futur.", "g"),
 q("<i>Si j'______ riche, j'achèterais une île.</i>", ["étais", "serais", "suis", "serai"], 0, "Type 2: si + imparfait.", "g"),
 q("<i>Si tu étudiais plus, tu ______.</i>", ["réussirais", "réussiras", "réussis", "aurais réussi"], 0, "Type 2: imparfait → conditionnel.", "g"),
 q("<i>Si elle avait su, elle ______.</i>", ["serait venue", "viendrait", "viendra", "était venue"], 0, "Type 3: plus-que-parfait → conditionnel passé.", "g"),
 q("<i>Si nous ______ partis plus tôt, nous serions arrivés à l'heure.</i>", ["étions", "serions", "avions", "sommes"], 0, "Type 3: partir + être → étions partis.", "g"),
 q("<i>J'aurais dû étudier</i> means…", ["I should have studied.", "I will have to study.", "I had studied.", "I would study."], 0, "devoir in the conditionnel passé = should have.", "g"),
 q("Which is wrong?", ["Si j'aurais le temps, je viendrais.", "Si j'avais le temps, je viendrais.", "Si j'ai le temps, je viendrai.", "Si j'avais eu le temps, je serais venu."], 0, "Never conditionnel after si.", "g"),
 q("<i>À ta place, je ne ______ pas.</i> (dire)", ["dirais", "dirai", "disais", "dis"], 0, "Advice → conditionnel.", "g"),
 q("<i>Le ministre ______ démissionné.</i> (reportedly)", ["aurait", "a", "avait", "aura"], 0, "Unconfirmed news → conditionnel (passé).", "g"),
 q("<i>Dès que j'______ fini, je t'appellerai.</i> (futur antérieur)", ["aurai", "ai", "aurais", "avais"], 0, "Completed before another future action: aurai fini.", "g"),
 q("Futur of <i>voir</i>, nous:", ["verrons", "voirons", "voyerons", "verrions"], 0, "verr- + ons.", "g"),
 q("<i>Je me demande s'il ______ demain.</i>", ["pleuvra", "pleut", "pleuvait", "pleuvrait"], 0, "si = whether: the future is allowed.", "g"),
 q(f"{listen('Si j’avais su, je serais venu.')} Did the speaker come?", ["No", "Yes", "Yes, later", "We can't tell"], 0, "Type 3 = it didn't happen.", "v"),
]
CHAL = [
 q("<i>Quand vous ______ vos devoirs, vous pourrez sortir.</i>", ["aurez fini", "finissez", "finirez", "auriez fini"], 0, "Completed before the future action → futur antérieur.", "g"),
 q("<i>Si j'avais étudié la médecine, je ______ médecin aujourd'hui.</i>", ["serais", "aurais été", "serai", "étais"], 0, "Past condition, present result → conditionnel présent.", "g"),
 q("Which uses the conditionnel for politeness?", ["Auriez-vous un moment ?", "Si j'avais un moment…", "Il a dit qu'il aurait un moment.", "Le PDG aurait un moment."], 0, "A softened request.", "g"),
 q("<i>Il faudra que…</i> : futur of <i>falloir</i> is…", ["il faudra", "il fallera", "il faudrait", "il faut"], 0, "faudr- + a.", "g"),
 q("<i>Elle m'a promis qu'elle m'______ dès qu'elle ______.</i>", ["appellerait … arriverait", "appellera … arrive", "appelait … arrivait", "appellerait … arrivera"], 0, "Reported future: both conditionnel.", "g"),
 q("Futur of <i>acheter</i>, je:", ["j'achèterai", "j'acheterai", "j'achetrai", "j'achèterais"], 0, "The stem takes è throughout.", "g"),
 q("<i>Tu ______ me prévenir !</i> (You could have warned me!)", ["aurais pu", "pourrais", "pourras", "avais pu"], 0, "Reproach → conditionnel passé of pouvoir.", "g"),
 q("<i>S'ils ______ , ils auraient gagné.</i> (had trained)", ["s'étaient entraînés", "s'entraîneraient", "s'entraînaient", "se seraient entraînés"], 0, "Type 3: plus-que-parfait; reflexive → être + agreement.", "g"),
]
EXQ = [
 q("Futur of <i>finir</i>, tu:", ["finiras", "finisseras", "finirais", "finis"], 0, "finir- + as.", "g", "gram"),
 q("Futur of <i>avoir</i>, nous:", ["aurons", "avrons", "aurions", "avons"], 0, "aur- + ons.", "g", "gram"),
 q("Futur of <i>savoir</i>, je:", ["saurai", "savrai", "saurais", "sais"], 0, "saur- + ai.", "g", "gram"),
 q("<i>Lorsque je ______ vieux, j'habiterai à la campagne.</i>", ["serai", "suis", "serais", "étais"], 0, "lorsque + future → futur.", "g", "gram"),
 q("Conditionnel of <i>aimer</i>, j':", ["aimerais", "aimerai", "aimais", "aime"], 0, "aimer- + ais.", "g", "gram"),
 q("<i>______-vous m'aider ?</i> (polite)", ["Pourriez", "Pourrez", "Pouvez-vous pas", "Pouviez"], 0, "Conditionnel for politeness.", "g", "gram"),
 q("<i>Si tu viens, je ______ content.</i>", ["serai", "serais", "suis été", "étais"], 0, "Type 1.", "g", "gram"),
 q("<i>Si nous avions une voiture, nous ______ plus souvent.</i>", ["voyagerions", "voyagerons", "voyagions", "aurions voyagé"], 0, "Type 2.", "g", "gram"),
 q("<i>Si tu m'avais écouté, tu ______ ce problème.</i>", ["n'aurais pas eu", "n'aurais pas", "n'avais pas eu", "n'auras pas eu"], 0, "Type 3: conditionnel passé, with ne … pas around aurais.", "g", "gram"),
 q("<i>Il a dit qu'il nous ______.</i> (would help)", ["aiderait", "aidera", "aidait", "aide"], 0, "Future in the past.", "g", "gram"),
 q("<i>J'aurais voulu venir</i> means…", ["I would have liked to come.", "I will want to come.", "I wanted to come.", "I had wanted to come."], 0, "conditionnel passé of vouloir.", "v", "vocab"),
 q("Which is the futur antérieur?", ["j'aurai fini", "j'aurais fini", "j'avais fini", "je finirai"], 0, "avoir in the futur + participle.", "g", "gram"),
 q(f"{listen('Je voudrais un croissant, s’il vous plaît.')} The verb is in the…", ["conditionnel", "futur", "imparfait", "présent"], 0, "voudrais = polite conditionnel.", "v", "listen"),
 q("Read: <i>Si je gagnais au loto, je ne travaillerais plus. Je voyagerais partout et j'achèterais une maison au bord de la mer. Mais je joue rarement, alors…</i> The writer is…", ["imagining something unlikely", "describing their life now", "talking about the past", "making a firm plan"], 0, "Type 2: hypothetical.", "v", "read"),
 q("Which sentence is correct?", ["Je te téléphonerai quand j'arriverai.", "Je te téléphonerai quand j'arrive.", "Je te téléphone quand j'arriverais.", "Je te téléphonerais quand j'arriverai."], 0, "quand + futur when the main verb is future.", "g", "gram"),
]
FRQS = [
 {"q": "Write about your future (at least 8 sentences).",
  "parts": [{"p": "Describe where you'll be in ten years using the futur simple (at least five verbs, three with irregular stems) and at least two sentences with quand + futur.",
   "rubric": [["At least five verbs in the futur simple", 2], ["At least three irregular stems used correctly", 2], ["Two sentences with quand / dès que + futur", 2], ["Accuracy and variety", 2]],
   "answer": f'<div class="ex">{F("Dans dix ans, j\'aurai vingt-huit ans. Je serai ingénieure et j\'habiterai à Montréal. Quand j\'aurai assez d\'argent, j\'achèterai un petit appartement. Je ferai du sport tous les matins et je verrai mes amis le week-end. Dès que je pourrai, j\'irai en Afrique de l\'Ouest. Ma famille viendra me voir souvent. Je serai heureuse, j\'espère !")}<span class="en">In ten years I\'ll be 28. I\'ll be an engineer and live in Montreal. When I have enough money, I\'ll buy a small apartment. I\'ll exercise every morning and see my friends on weekends. As soon as I can, I\'ll go to West Africa. My family will come see me often. I\'ll be happy, I hope!</span></div>'}]},
 {"q": "Complete each sentence logically, using the right tense.",
  "parts": [{"p": "1. Si j'ai une bonne note…  2. Si j'étais président(e)…  3. Si j'avais vécu au Moyen Âge…",
   "rubric": [["1. futur (je serai content)", 1], ["2. conditionnel (je changerais…)", 1], ["3. conditionnel passé (j'aurais été…)", 1], ["Logical, grammatical completions", 1]],
   "answer": f'<div class="ex">{F("Si j\'ai une bonne note, mes parents seront fiers.")}<span class="en">If I get a good grade, my parents will be proud.</span></div><div class="ex">{F("Si j\'étais présidente, je rendrais l\'université gratuite.")}<span class="en">If I were president, I\'d make college free.</span></div><div class="ex">{F("Si j\'avais vécu au Moyen Âge, j\'aurais été chevalier.")}<span class="en">If I had lived in the Middle Ages, I would have been a knight.</span></div>'}]},
]

if __name__ == "__main__":
    build(3, "college-3", "Futur et conditionnel", 'Futur <span class="hl">et conditionnel</span>',
          "College French: the futur simple and its irregular stems, quand + futur, the conditionnel, and all three types of si clauses.",
          "College French Unit 3: futur simple, conditionnel and si clauses, with audio, interactive labs, practice questions and a practice exam.",
          CH, PQ, CHAL, EXQ, FRQS, "/home/claude/ap-physics-study/courses/french-1/college-3.html", college=True)
