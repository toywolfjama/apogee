from fr_common import *

TRIG = [
 ["Il faut", "s", "necessity", "de"], ["Il est important", "s", "an impersonal judgment"], ["Je veux", "s", "will or wanting (different subjects)", ""],
 ["Je suis content(e)", "s", "an emotion", "de"], ["J'ai peur", "s", "fear", "de"], ["Je doute", "s", "doubt"], ["Je ne pense pas", "s", "doubt (a negative opinion)"],
 ["Bien", "s", "concession (bien que = although)"], ["Pour", "s", "purpose (pour que = so that)"], ["Avant", "s", "time before (avant que)"], ["Sans", "s", "without (sans que)"],
 ["Je pense", "i", "an affirmative opinion"], ["Je sais", "i", "certainty"], ["Il est sûr", "i", "certainty"], ["Parce", "i", "cause (parce que)"],
]
VB = [["être", "à l'heure"], ["avoir", "raison"], ["faire", "les devoirs"], ["aller", "au cinéma"], ["pouvoir", "venir"], ["savoir", "la réponse"], ["vouloir", "partir"], ["finir", "le projet"], ["prendre", "le train"], ["venir", "demain"], ["parler", "français"], ["boire", "de l'eau"]]

CH = []
CORE = f'''<p>The <b>subjunctive</b> isn't a tense. It's a <b>mood</b> for things that aren't presented as plain facts: what someone wants, needs, fears or doubts. It almost always appears after <b>que</b>, in a second clause with a different subject.</p>
{wa("Same verb, two moods", [
 ("a|Je sais|s  b|que|gl  c|tu|s  d|es|v  e|là.|x", "Je sais que states a fact → indicative: tu es.", "I know you're here."),
 ("a|Je veux|s  b|que|gl  c|tu|s  d|sois|n  e|là.|x", "Je veux que expresses a wish → subjunctive: tu sois.", "I want you to be here."),
 ("a|Je veux|s  f|être|n  e|là.|x", "Same subject (je … je)? Use an infinitive instead.", "I want to be here.")])}'''
CH.append(chapter("overview-c4", "Overview", "Overview", [topic("core-c4", "Le subjonctif", CORE)]))

FORM = topic("subj-form", "Forming the subjunctive", f'''
<p>Take the <b>ils</b> form of the present, drop <b>-ent</b>, add <b>-e, -es, -e, -ions, -iez, -ent</b>. For verbs with two stems, nous and vous use the <b>imparfait</b> stem.</p>
<div class="tblwrap"><table><tr><th>ils (present)</th><th>que je…</th><th>que nous…</th></tr>
<tr><td>{F("ils parlent")}</td><td>{F("que je parle")}</td><td>{F("que nous parlions")}</td></tr>
<tr><td>{F("ils finissent")}</td><td>{F("que je finisse")}</td><td>{F("que nous finissions")}</td></tr>
<tr><td>{F("ils prennent")}</td><td>{F("que je prenne")}</td><td>{F("que nous prenions")}</td></tr>
<tr><td>{F("ils viennent")}</td><td>{F("que je vienne")}</td><td>{F("que nous venions")}</td></tr>
<tr><td>{F("ils boivent")}</td><td>{F("que je boive")}</td><td>{F("que nous buvions")}</td></tr></table></div>
<h3>Seven irregulars to memorize</h3>
{vt([("être", "que je sois, que tu sois, qu'il soit, que nous soyons, que vous soyez, qu'ils soient"), ("avoir", "que j'aie, que tu aies, qu'il ait, que nous ayons, que vous ayez, qu'ils aient"), ("aller", "que j'aille… que nous allions"), ("faire", "que je fasse… que nous fassions"), ("pouvoir", "que je puisse… que nous puissions"), ("savoir", "que je sache… que nous sachions"), ("vouloir", "que je veuille… que nous voulions")], head=("Verb", "Subjunctive"))}
{lab(type="conj", verbs=["parler", "finir", "vendre", "prendre", "venir", "boire", "voir", "devoir", "être", "avoir", "aller", "faire", "pouvoir", "savoir", "vouloir", "se lever"], tenses=["subj", "pres"])}
''', pill=("g", "C4.1"), sub="From the ils form, with seven irregulars.")

USE = topic("subj-use", "When to use it", f'''
<p>A handy memory aid is <b>WEIRDO</b>: <b>W</b>ishes, <b>E</b>motions, <b>I</b>mpersonal expressions, <b>R</b>ecommendations, <b>D</b>oubt / denial, <b>O</b>rders.</p>
{vt([("vouloir que, souhaiter que, préférer que", "wish, will", "Je veux que tu viennes."), ("être content / triste / surpris que, avoir peur que", "emotion", "Je suis triste que tu partes."), ("il faut que, il est important / nécessaire / possible que", "impersonal", "Il faut que nous partions."), ("conseiller que, suggérer que, recommander que", "recommendation", "Je suggère que vous attendiez."), ("douter que, ne pas penser que, ne pas croire que", "doubt, denial", "Je ne crois pas qu'il ait raison."), ("exiger que, ordonner que, demander que", "orders", "Le prof exige que nous soyons à l'heure.")], head=("Trigger", "Category", "Example"))}
<h3>Conjunctions that require it</h3>
{vgrid([("bien que", "although"), ("pour que", "so that"), ("avant que", "before"), ("à moins que", "unless"), ("sans que", "without"), ("jusqu'à ce que", "until"), ("à condition que", "provided that"), ("de peur que", "for fear that")])}
{lab(type="mood", triggers=TRIG, verbs=VB)}
''', pill=("g", "C4.2"), sub="Wishes, emotions, necessity, doubt.")

NOT = topic("indicatif", "When not to use it", f'''
<div class="grid2"><div class="mini"><h4>Certainty and belief → indicative</h4><p>{F("Je pense qu'il a raison.")} {F("Je sais qu'elle vient.")} {F("Il est sûr / certain / évident / vrai que…")}</p></div>
<div class="mini"><h4>Negative or question → often subjunctive</h4><p>{F("Je ne pense pas qu'il ait raison.")} {F("Penses-tu qu'il ait raison ?")} The doubt switches the mood.</p></div>
<div class="mini"><h4>Same subject → infinitive</h4><p>{F("Je veux partir")}, not que je parte. {F("Je suis content d'être ici.")} {F("Avant de partir…")} {F("Pour réussir…")}</p></div>
<div class="mini"><h4>Après que, pendant que, parce que → indicative</h4><p>{F("Après qu'il est parti…")} (though you'll often hear the subjunctive here in speech). {F("Parce qu'il pleut…")}</p></div></div>
{box("trap", "Espérer", f"{F('espérer que')} takes the <b>indicative</b> (usually the future): {F('J’espère que tu viendras.')} It feels like a wish, but grammar treats it as confidence.")}
''', pill=("g", "C4.3"), sub="Certainty, same subjects, and espérer.",
 det=("The past subjunctive", '''<h4>Form</h4><p>avoir / être in the subjunctive + past participle: <i>que j'aie fini</i>, <i>qu'elle soit partie</i>.</p>
<h4>Use</h4><p>When the action in the que clause happened before the main verb: <i>Je suis content que tu sois venu</i> (I'm glad you came). <i>Bien qu'il ait étudié, il a raté l'examen.</i></p>
<h4>Recognizing it</h4><p>In older or very formal texts you may meet the imperfect subjunctive (<i>qu'il fût, qu'il eût</i>). You only need to recognize it.</p>'''))
CH.append(chapter("subj-c4", "Le subjonctif", "Subjunctive", [FORM, USE, NOT]))

REV = topic("review-c4", "Unit summary", f'''<div class="grid2"><div class="mini"><h4>Formation</h4><p>ils stem + e, es, e, ions, iez, ent. nous / vous from the imparfait stem. Irregulars: être, avoir, aller, faire, pouvoir, savoir, vouloir.</p></div>
<div class="mini"><h4>Triggers</h4><p>Wishes, emotions, impersonal necessity, recommendations, doubt, orders. bien que, pour que, avant que, à moins que, sans que, jusqu'à ce que.</p></div>
<div class="mini"><h4>Indicative instead</h4><p>Certainty, je pense que (affirmative), espérer que, après que, parce que.</p></div>
<div class="mini"><h4>Infinitive instead</h4><p>Same subject: je veux partir, avant de partir, pour réussir.</p></div></div>''', sub="Everything from this unit on one screen.")
MIS = topic("mistakes-c4", "Common mistakes", '''<ol class="steps">
<li><i>Je veux que je parte</i> → <i>Je veux partir</i>.</li>
<li><i>Je pense qu'il soit malade</i> → <i>Je pense qu'il est malade</i>.</li>
<li><i>J'espère que tu sois là</i> → <i>J'espère que tu seras là</i>.</li>
<li><i>Il faut que tu fais</i> → <i>Il faut que tu fasses</i>.</li>
<li><i>que nous prennions</i> → <i>que nous prenions</i> (imparfait stem for nous / vous).</li>
<li><i>que j'aille</i> vs <i>que j'aie</i>: aller vs avoir.</li></ol>''', sub="Points students lose most often.")
CH.append(chapter("review-ch-c4", "Review", "Review", [REV, MIS]))

PQ = [
 q("<i>Il faut que tu ______ tes devoirs.</i> (faire)", ["fasses", "fais", "feras", "faisais"], 0, "faire → fasse (irregular).", "g"),
 q("<i>Je veux que vous ______ à l'heure.</i> (être)", ["soyez", "êtes", "serez", "soyiez"], 0, "être: que vous soyez.", "g"),
 q("<i>Il est important qu'elle ______ raison.</i> (avoir)", ["ait", "a", "aie", "aura"], 0, "avoir: qu'elle ait.", "g"),
 q("<i>Je suis content que tu ______.</i> (venir)", ["viennes", "viens", "venes", "viendras"], 0, "ils viennent → que tu viennes.", "g"),
 q("<i>Il faut que nous ______ le train.</i> (prendre)", ["prenions", "prennions", "prenons", "prendrions"], 0, "nous uses the imparfait stem: pren-.", "g"),
 q("<i>Bien qu'il ______ fatigué, il travaille.</i>", ["soit", "est", "sera", "était"], 0, "bien que + subjunctive.", "g"),
 q("<i>Je parle lentement pour que tu ______.</i> (comprendre)", ["comprennes", "comprends", "comprenes", "comprendras"], 0, "pour que + subjunctive.", "g"),
 q("<i>Je pense qu'il ______ raison.</i>", ["a", "ait", "aie", "aurait eu"], 0, "Affirmative opinion → indicative.", "g"),
 q("<i>Je ne pense pas qu'il ______ raison.</i>", ["ait", "a", "aura", "avait"], 0, "Negative opinion → subjunctive.", "g"),
 q("<i>J'espère que tu ______ demain.</i>", ["viendras", "viennes", "vinsses", "venir"], 0, "espérer que → indicative.", "g"),
 q("<i>Je veux ______ au cinéma.</i> (I want to go)", ["aller", "que j'aille", "que je vais", "allé"], 0, "Same subject → infinitive.", "g"),
 q("<i>Elle a peur que son chien ______.</i> (partir)", ["parte", "part", "partira", "partait"], 0, "Emotion (fear) → subjunctive.", "g"),
 q("<i>Je doute qu'ils ______ la réponse.</i> (savoir)", ["sachent", "savent", "sauront", "sachiez"], 0, "savoir: qu'ils sachent.", "g"),
 q("<i>Il faut que j'______ à la banque.</i> (aller)", ["aille", "aie", "vais", "irai"], 0, "aller: que j'aille.", "g"),
 q("<i>Avant que tu ______, appelle-moi.</i> (partir)", ["partes", "pars", "partiras", "partais"], 0, "avant que + subjunctive.", "g"),
 q("<i>Après qu'il ______, nous avons mangé.</i> (arriver)", ["est arrivé", "soit arrivé", "arrive", "arrivera"], 0, "après que → indicative (in careful French).", "g"),
 q("<i>Il est certain qu'elle ______ au concert.</i> (venir)", ["viendra", "vienne", "venait", "viennes"], 0, "Certainty → indicative.", "g"),
 q("<i>Je cherche quelqu'un qui ______ parler chinois.</i>", ["puisse", "peut", "pourra", "pouvait"], 0, "A person who may not exist → subjunctive (puisse).", "g"),
 q("Subjunctive of <i>vouloir</i>, que nous:", ["voulions", "veuillions", "voulons", "veuillons"], 0, "que nous voulions.", "g"),
 q("<i>À moins qu'il ne ______, on part à 8 h.</i> (pleuvoir)", ["pleuve", "pleut", "pleuvra", "pleuvait"], 0, "à moins que + subjunctive (the ne is optional and not negative).", "g"),
 q("WEIRDO: the <b>D</b> stands for…", ["doubt / denial", "description", "desire to travel", "dates"], 0, "Doubt or denial.", "g"),
 q("<i>Je suis content ______ ici.</i> (to be here, same subject)", ["d'être", "que je sois", "que je suis", "être"], 0, "Same subject → de + infinitive.", "g"),
 q("<i>Le prof exige que nous ______ nos téléphones.</i> (éteindre)", ["éteignions", "éteignons", "éteindrons", "éteindrions"], 0, "exiger que + subjunctive; nous uses the imparfait stem éteign-.", "g"),
 q(f"{listen('Il faut que tu sois prudent.')} The speaker is…", ["telling someone to be careful", "saying someone is careful", "asking if someone was careful", "promising to be careful"], 0, "Il faut que + subjunctive = necessity.", "v"),
]
CHAL = [
 q("<i>Je suis ravi que vous ______ venus.</i>", ["soyez", "êtes", "serez", "ayez"], 0, "Past subjunctive with an être verb: que vous soyez venus.", "g"),
 q("<i>Bien qu'elle ______ beaucoup étudié, elle a échoué.</i>", ["ait", "a", "avait", "aie"], 0, "Past subjunctive: qu'elle ait étudié.", "g"),
 q("<i>Penses-tu qu'il ______ venir ?</i>", ["puisse", "peut", "pourra", "pouvait"], 0, "A question about opinion → subjunctive is standard.", "g"),
 q("Which is correct?", ["Je préfère que tu restes.", "Je préfère que tu restes ici, je reste.", "Je préfère que je reste.", "Je préfère que tu resteras."], 0, "Different subjects + wish → subjunctive.", "g"),
 q("<i>Il n'y a personne qui ______ la réponse.</i>", ["sache", "sait", "saura", "savait"], 0, "Negative antecedent → subjunctive.", "g"),
 q("<i>Attends ici jusqu'à ce que je ______.</i>", ["revienne", "reviens", "reviendrai", "revenais"], 0, "jusqu'à ce que + subjunctive.", "g"),
 q("Which sentence needs the subjunctive?", ["Il est possible qu'il (venir) demain.", "Il est probable qu'il (venir) demain.", "Je sais qu'il (venir) demain.", "J'espère qu'il (venir) demain."], 0, "possible → subjunctive; probable, savoir and espérer → indicative.", "g"),
 q("<i>Je te prête mon livre à condition que tu me le ______ demain.</i>", ["rendes", "rends", "rendras", "rendais"], 0, "à condition que + subjunctive.", "g"),
]
EXQ = [
 q("Subjunctive of <i>parler</i>, que tu:", ["parles", "parlez", "parlais", "parleras"], 0, "ils parlent → parl- + es.", "g", "gram"),
 q("Subjunctive of <i>finir</i>, qu'il:", ["finisse", "finit", "finira", "finissait"], 0, "ils finissent → finiss- + e.", "g", "gram"),
 q("Subjunctive of <i>être</i>, que nous:", ["soyons", "sommes", "soyions", "serons"], 0, "que nous soyons.", "g", "gram"),
 q("Subjunctive of <i>pouvoir</i>, que je:", ["puisse", "peux", "pouve", "pourrai"], 0, "que je puisse.", "g", "gram"),
 q("<i>Il faut que vous ______ ce formulaire.</i> (remplir)", ["remplissiez", "remplissez", "remplirez", "remplissez-vous"], 0, "que vous remplissiez.", "g", "gram"),
 q("<i>Ma mère veut que je ______ médecin.</i>", ["devienne", "deviens", "deviendrai", "devenir"], 0, "Wish + different subject.", "g", "gram"),
 q("<i>Je crois que c'______ une bonne idée.</i>", ["est", "soit", "sois", "serait été"], 0, "Affirmative belief → indicative.", "g", "gram"),
 q("<i>Je ne crois pas que ce ______ une bonne idée.</i>", ["soit", "est", "sera", "serait"], 0, "Negative belief → subjunctive.", "g", "gram"),
 q("<i>Elle est partie sans que je la ______.</i> (voir)", ["voie", "vois", "verrai", "voyais"], 0, "sans que + subjunctive.", "g", "gram"),
 q("<i>Nous espérons que vous ______ un bon voyage.</i>", ["ferez", "fassiez", "faites", "fassez"], 0, "espérer → indicative (future).", "g", "gram"),
 q("<i>Pour ______, il faut travailler.</i>", ["réussir", "que tu réussisses", "réussis", "réussirons"], 0, "General statement, no new subject → infinitive.", "g", "gram"),
 q("<i>Il est dommage que tu ne ______ pas venir.</i>", ["puisses", "peux", "pourras", "pouvais"], 0, "Emotion / judgment → subjunctive.", "g", "gram"),
 q(f"{listen('Je veux que tu fasses attention.')} The speaker wants the listener to…", ["be careful", "pay for something", "make a mistake", "leave"], 0, "faire attention = to be careful.", "v", "listen"),
 q("Read: <i>Chère Julie, je suis si heureuse que tu viennes nous voir cet été ! Il faut que tu prennes le train de 10 h, à moins qu'il ne soit complet. J'espère que tu aimeras notre petite ville.</i> Which verb is NOT in the subjunctive?", ["aimeras", "viennes", "prennes", "soit"], 0, "espérer que → indicative (futur).", "g", "read"),
 q("Which trigger takes the indicative?", ["Je suis sûr que", "Je doute que", "Il faut que", "Bien que"], 0, "Certainty → indicative.", "g", "gram"),
]
FRQS = [
 {"q": "Write advice for a student starting college in France (at least 8 sentences).",
  "parts": [{"p": "Use at least six different subjunctive triggers (il faut que, il est important que, je conseille que, bien que, pour que, avant que…) and one sentence with espérer que.",
   "rubric": [["Six different triggers, each followed by a correct subjunctive", 3], ["At least two irregular subjunctives (soit, aie, aille, fasse, puisse, sache…)", 2], ["espérer que + indicative", 1], ["One same-subject infinitive structure (pour réussir, avant de partir…)", 1], ["Overall accuracy", 1]],
   "answer": f'<div class="ex">{F("Avant de partir, il faut que tu fasses une liste de tout ce dont tu as besoin. Il est important que tu aies ton passeport et ta carte étudiante. Je conseille que tu ailles à la réunion d\'accueil pour que tu puisses rencontrer d\'autres étudiants. Bien que les cours soient difficiles, ne panique pas. Il vaut mieux que tu saches où se trouve la bibliothèque avant que les examens commencent. J\'espère que tu passeras une année géniale !")}<span class="en">Before leaving, you need to make a list of everything you need. It\'s important to have your passport and student card. I suggest you go to the welcome meeting so you can meet other students. Although classes are hard, don\'t panic. Better to know where the library is before exams start. I hope you\'ll have a great year!</span></div>'}]},
 {"q": "Subjunctive, indicative or infinitive? Complete each sentence and explain your choice in one line.",
  "parts": [{"p": "1. Je pense que le français (être) facile.  2. Je ne pense pas que le français (être) facile.  3. Je veux (apprendre) le français.  4. Mon prof veut que nous (apprendre) le subjonctif.",
   "rubric": [["1. est (affirmative opinion → indicative)", 1], ["2. soit (negative opinion → subjunctive)", 1], ["3. apprendre (same subject → infinitive)", 1], ["4. apprenions (wish + different subject → subjunctive)", 1]],
   "answer": f'<div class="ex">{F("Je pense que le français est facile.")}<span class="en">Affirmative belief → indicative.</span></div><div class="ex">{F("Je ne pense pas que le français soit facile.")}<span class="en">Negative belief → subjunctive.</span></div><div class="ex">{F("Je veux apprendre le français.")}<span class="en">Same subject → infinitive.</span></div><div class="ex">{F("Mon prof veut que nous apprenions le subjonctif.")}<span class="en">Wish, different subject → subjunctive.</span></div>'}]},
]

if __name__ == "__main__":
    build(4, "college-4", "Le subjonctif", 'Le <span class="hl">subjonctif</span>',
          "College French: forming the present subjunctive, the triggers that require it, the conjunctions that take it, and when to use the indicative or an infinitive instead.",
          "College French Unit 4: the subjunctive, with audio, a mood lab, practice questions and a practice exam.",
          CH, PQ, CHAL, EXQ, FRQS, "/home/claude/ap-physics-study/courses/french-1/college-4.html", college=True)
