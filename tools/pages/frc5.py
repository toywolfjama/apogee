from fr_common import *

CH = []
CORE = f'''<p>The last college unit is about <b>sounding like an educated writer</b>: restructuring sentences (the passive, the gérondif), reporting what people said, reading literature in the passé simple, and organizing an argument with the right connectors. This is the toolkit for essays, presentations and reading real French texts.</p>
{wa("Active to passive", [
 ("a|Le chat|s  b|a mangé|v  c|la souris.|x", "Active: the subject does the action.", "The cat ate the mouse."),
 ("c|La souris|s  b|a été mangée|n  d|par|gl  a|le chat.|x", "Passive: être (in the same tense) + participle, which agrees with the new subject.", "The mouse was eaten by the cat."),
 ("e|On|s  b2|a mangé|v  c|la souris.|x", "French often prefers on to the passive when no doer is named.", "Someone ate the mouse.")])}'''
CH.append(chapter("overview-c5", "Overview", "Overview", [topic("core-c5", "Le style", CORE)]))

PASS = topic("passive", "The passive voice", f'''
<p>Form: <b>être</b> in the tense of the active verb + past participle (which agrees with the subject) + <b>par</b> for the doer.</p>
{vt([("Le prof corrige les copies.", "Les copies sont corrigées par le prof.", "présent"), ("Le prof a corrigé les copies.", "Les copies ont été corrigées par le prof.", "passé composé"), ("Le prof corrigera les copies.", "Les copies seront corrigées par le prof.", "futur")], head=("Active", "Passive", "Tense"))}
<h3>Avoiding the passive</h3>
<p>French uses the passive less than English. Two common alternatives:</p>
<ul><li><b>on</b> + active verb: {F("On parle français ici.")} (French is spoken here.)</li>
<li>a <b>reflexive</b> verb: {F("Ça se dit comment ?")} (How is that said?) {F("Le vin blanc se boit frais.")} (White wine is drunk chilled.)</li></ul>
{box("trap", "Indirect objects can't become subjects", f"English says <i>I was given a book</i>. French can't: say {F('On m’a donné un livre.')}")}
''', pill=("g", "C5.1"), sub="être + participle, or on.")

GER = topic("gerondif", "The gérondif and present participle", f'''
<p>Present participle: <b>nous</b> stem + <b>-ant</b>: {F("parlant")}, {F("finissant")}, {F("faisant")}, {F("prenant")}. Three irregulars: {F("étant")}, {F("ayant")}, {F("sachant")}.</p>
<p>The <b>gérondif</b> is <b>en + -ant</b>. It describes something the subject does at the same time, or how they do it:</p>
{ex("Il chante en prenant sa douche.", "He sings while taking a shower. (at the same time)")}
{ex("C'est en forgeant qu'on devient forgeron.", "Practice makes perfect. (literally: it's by forging that you become a blacksmith)")}
{ex("Je me suis cassé le bras en tombant de vélo.", "I broke my arm falling off my bike. (how)")}
{box("plain", "Same subject", "The gérondif must refer to the subject of the sentence: <i>En sortant, j'ai vu Paul</i> = when <b>I</b> went out. For Paul going out, say <i>J'ai vu Paul qui sortait.</i>")}
''', pill=("g", "C5.2"), sub="en parlant, en faisant.")
CH.append(chapter("voice-c5", "Passif et gérondif", "Passive", [PASS, GER]))

IND = topic("reported", "Reported speech", f'''
<p>When you report what someone said with a past verb ({F("il a dit que")}, {F("elle a demandé si")}), the tenses shift back, as in English:</p>
<div class="tblwrap"><table><tr><th>Direct speech</th><th>Reported (after a past verb)</th></tr>
<tr><td>présent: « Je suis fatigué. »</td><td>imparfait: {F("Il a dit qu'il était fatigué.")}</td></tr>
<tr><td>passé composé: « J'ai fini. »</td><td>plus-que-parfait: {F("Elle a dit qu'elle avait fini.")}</td></tr>
<tr><td>futur: « Je viendrai. »</td><td>conditionnel: {F("Il a dit qu'il viendrait.")}</td></tr>
<tr><td>futur proche: « Je vais partir. »</td><td>aller in the imparfait: {F("Il a dit qu'il allait partir.")}</td></tr>
<tr><td>imparfait / plus-que-parfait</td><td>no change</td></tr></table></div>
<h3>Reporting questions</h3>
{vt([("« Tu viens ? »", "Il m'a demandé si je venais.", "yes / no → si"), ("« Qu'est-ce que tu fais ? »", "Il m'a demandé ce que je faisais.", "qu'est-ce que → ce que"), ("« Qu'est-ce qui se passe ? »", "Il a demandé ce qui se passait.", "qu'est-ce qui → ce qui"), ("« Où vas-tu ? »", "Il m'a demandé où j'allais.", "question words stay"), ("« Viens ! »", "Il m'a dit de venir.", "command → de + infinitive")], head=("Direct", "Reported", "Rule"))}
<p>Also change pronouns, possessives and time words: {F("aujourd'hui → ce jour-là")}, {F("demain → le lendemain")}, {F("hier → la veille")}, {F("ici → là")}.</p>
''', pill=("g", "C5.3"), sub="Il a dit que… Elle a demandé si…")

PS = topic("passe-simple", "Recognizing the passé simple", f'''
<p>The passé simple is the literary past tense, used in novels, fairy tales and history books instead of the passé composé. You rarely write it, but you must <b>recognize</b> it, mostly in the third person.</p>
{vt([("parler", "il parla, ils parlèrent", "-er: -a, -èrent"), ("finir", "il finit, ils finirent", "-ir: -it, -irent"), ("vendre", "il vendit, ils vendirent", "-re: -it, -irent"), ("être", "il fut, ils furent"), ("avoir", "il eut, ils eurent"), ("faire", "il fit, ils firent"), ("venir", "il vint, ils vinrent"), ("voir", "il vit, ils virent"), ("prendre", "il prit, ils prirent"), ("dire", "il dit, ils dirent")], head=("Verb", "Passé simple", "Pattern"))}
{ex("Il était une fois une princesse qui vivait dans un château. Un jour, un dragon arriva et l'emporta.", "Once upon a time there was a princess who lived in a castle. One day a dragon arrived and carried her off. (imparfait for the setting, passé simple for the events)")}
''', pill=("v", "C5.4"), sub="il fut, il eut, il fit, ils allèrent.")
CH.append(chapter("speech-c5", "Discours et littérature", "Reported speech", [IND, PS]))

CONN = topic("connectors", "Connectors for essays", f'''
<p>Good French writing links ideas explicitly. Learn a few in each category and use them in every essay.</p>
{vt([("tout d'abord, premièrement", "first of all", "introducing"), ("ensuite, de plus, en outre", "next, moreover, furthermore", "adding"), ("cependant, pourtant, néanmoins", "however, yet, nevertheless", "contrasting"), ("en revanche, par contre", "on the other hand", "contrasting"), ("bien que (+ subj.), même si (+ ind.)", "although, even if", "conceding"), ("donc, par conséquent, c'est pourquoi", "so, therefore, that's why", "consequence"), ("car, puisque, étant donné que", "because, since, given that", "cause"), ("par exemple, notamment, ainsi", "for example, in particular, thus", "illustrating"), ("en effet", "indeed, in fact", "confirming"), ("en conclusion, bref, pour conclure", "in conclusion, in short", "concluding")], head=("Connector", "English", "Use"))}
<h3>Structuring an argument</h3>
<ol class="steps"><li><b>Introduction</b>: present the topic, then ask the question you'll answer: {F("Faut-il interdire les téléphones à l'école ?")}</li>
<li><b>Thèse</b>: arguments for, each with an example: {F("D'une part, …")}</li>
<li><b>Antithèse</b>: arguments against: {F("D'autre part, …")} {F("Cependant, …")}</li>
<li><b>Synthèse / conclusion</b>: your balanced position: {F("En conclusion, il me semble que…")}</li></ol>
<h3>Useful phrases for opinions</h3>
{vgrid([("À mon avis…", "In my opinion…"), ("Il me semble que…", "It seems to me that…"), ("Je suis persuadé(e) que…", "I'm convinced that…"), ("Il est vrai que…, mais…", "It's true that…, but…"), ("On pourrait objecter que…", "One could object that…"), ("Il faut reconnaître que…", "One must admit that…")])}
''', pill=("v", "C5.5"), sub="cependant, en revanche, par conséquent…")
CH.append(chapter("essay-c5", "L'essai: Writing", "Writing", [CONN]))

REV = topic("review-c5", "Unit summary", f'''<div class="grid2"><div class="mini"><h4>Passive</h4><p>être (same tense) + agreeing participle + par. Often replaced by on or a reflexive verb.</p></div>
<div class="mini"><h4>Gérondif</h4><p>en + nous stem + -ant (étant, ayant, sachant). Same subject, simultaneous action or manner.</p></div>
<div class="mini"><h4>Reported speech</h4><p>présent → imparfait, PC → PQP, futur → conditionnel. si / ce que / ce qui. Commands → de + infinitive.</p></div>
<div class="mini"><h4>Writing</h4><p>Passé simple for recognition. Connectors: cependant, en revanche, par conséquent, en effet, en conclusion.</p></div></div>''', sub="Everything from this unit on one screen.")
MIS = topic("mistakes-c5", "Common mistakes", '''<ol class="steps">
<li><i>Les lettres ont été écrit</i> → <i>écrites</i> (agreement in the passive).</li>
<li><i>J'ai été donné un livre</i> → <i>On m'a donné un livre</i>.</li>
<li><i>Il a dit qu'il viendra</i> in formal writing → <i>qu'il viendrait</i>.</li>
<li><i>Il m'a demandé qu'est-ce que je faisais</i> → <i>ce que je faisais</i>.</li>
<li><i>En étant fatigué</i> for a different subject: the gérondif must match the subject.</li>
<li>Using <i>même si</i> with the subjunctive: <i>même si</i> takes the indicative; <i>bien que</i> takes the subjunctive.</li></ol>''', sub="Points students lose most often.")
CH.append(chapter("review-ch-c5", "Review", "Review", [REV, MIS]))

PQ = [
 q("Passive: <i>Le chef prépare le repas.</i>", ["Le repas est préparé par le chef.", "Le repas a préparé le chef.", "Le repas est préparer par le chef.", "Le chef est préparé par le repas."], 0, "être (present) + participle.", "g"),
 q("Passive: <i>Victor Hugo a écrit ces romans.</i>", ["Ces romans ont été écrits par Victor Hugo.", "Ces romans sont écrit par Victor Hugo.", "Ces romans ont été écrit par Victor Hugo.", "Ces romans étaient écrits Victor Hugo."], 0, "PC passive: ont été + écrits (agrees).", "g"),
 q("<i>On parle français au Québec</i> means…", ["French is spoken in Quebec.", "One person speaks French in Quebec.", "We will speak French in Quebec.", "French was spoken in Quebec."], 0, "on + active often replaces the passive.", "g"),
 q("<i>I was told the news.</i>", ["On m'a annoncé la nouvelle.", "J'ai été annoncé la nouvelle.", "Je suis annoncé la nouvelle.", "La nouvelle m'a été on."], 0, "Indirect objects can't become passive subjects.", "g"),
 q("Present participle of <i>faire</i>:", ["faisant", "faiant", "fesant", "fait"], 0, "nous faisons → fais- + ant.", "g"),
 q("Present participle of <i>avoir</i>:", ["ayant", "avant", "avoirant", "aiant"], 0, "Irregular: ayant.", "g"),
 q("<i>Il écoute de la musique ______ ses devoirs.</i>", ["en faisant", "en fait", "faisant en", "pour faire"], 0, "Gérondif: en + -ant.", "g"),
 q("<i>C'est en forgeant qu'on devient forgeron</i> means…", ["Practice makes perfect.", "Blacksmiths work hard.", "You become what you eat.", "Don't play with fire."], 0, "A proverb.", "v"),
 q("<i>« Je suis malade. »</i> → Il a dit qu'il ______ malade.", ["était", "est", "sera", "avait été"], 0, "présent → imparfait.", "g"),
 q("<i>« J'ai perdu mes clés. »</i> → Elle a dit qu'elle ______ ses clés.", ["avait perdu", "a perdu", "perdait", "perdrait"], 0, "PC → plus-que-parfait.", "g"),
 q("<i>« Nous partirons demain. »</i> → Ils ont dit qu'ils ______ le lendemain.", ["partiraient", "partiront", "partaient", "étaient partis"], 0, "futur → conditionnel; demain → le lendemain.", "g"),
 q("<i>« Tu as faim ? »</i> → Il m'a demandé ______ j'avais faim.", ["si", "que", "ce que", "qu'est-ce que"], 0, "Yes / no question → si.", "g"),
 q("<i>« Qu'est-ce que tu veux ? »</i> → Elle m'a demandé ______ je voulais.", ["ce que", "qu'est-ce que", "que", "ce qui"], 0, "qu'est-ce que → ce que.", "g"),
 q("<i>« Ferme la porte ! »</i> → Il m'a dit ______ la porte.", ["de fermer", "que je ferme", "fermer", "fermais"], 0, "Command → de + infinitive.", "g"),
 q("<i>demain</i> in reported speech becomes…", ["le lendemain", "la veille", "ce jour-là", "hier"], 0, "the next day.", "v"),
 q("<i>Il fut</i> is the passé simple of…", ["être", "faire", "falloir", "fuir"], 0, "être → il fut.", "v"),
 q("<i>Ils allèrent</i> is the passé simple of…", ["aller", "allumer", "avoir", "lire"], 0, "-er verbs: ils -èrent.", "v"),
 q("<i>Il fit</i> is the passé simple of…", ["faire", "finir", "fuir", "falloir"], 0, "faire → il fit.", "v"),
 q("Which connector introduces a contrast?", ["en revanche", "de plus", "par conséquent", "en effet"], 0, "en revanche = on the other hand.", "v"),
 q("Which connector introduces a consequence?", ["par conséquent", "pourtant", "bien que", "notamment"], 0, "par conséquent = therefore.", "v"),
 q("<i>______ il pleuve, nous sortirons.</i>", ["Bien qu'", "Même s'", "Parce qu'", "Donc"], 0, "pleuve is subjunctive → bien que.", "g"),
 q("<i>______ il pleut, nous sortirons.</i>", ["Même s'", "Bien qu'", "Pour qu'", "Avant qu'"], 0, "pleut is indicative → même si.", "g"),
 q("Which is a balanced opinion phrase?", ["Il est vrai que…, mais…", "Donc", "Notamment", "Tout d'abord"], 0, "Concedes a point before disagreeing.", "v"),
 q(f"{listen('Elle m’a demandé si je viendrais.')} What did she ask?", ["whether the speaker would come", "where the speaker was going", "when the speaker came", "the speaker to come"], 0, "si = whether; viendrais = would come.", "v"),
]
CHAL = [
 q("Passive in the futur: <i>On construira le pont en 2030.</i>", ["Le pont sera construit en 2030.", "Le pont est construit en 2030.", "Le pont serait construit en 2030.", "Le pont a été construit en 2030."], 0, "futur of être + participle.", "g"),
 q("<i>« Je vais déménager. »</i> → Il a dit qu'il ______.", ["allait déménager", "va déménager", "irait déménager", "avait déménagé"], 0, "Futur proche → aller in the imparfait.", "g"),
 q("<i>« Qu'est-ce qui ne va pas ? »</i> → Elle m'a demandé ______ n'allait pas.", ["ce qui", "ce que", "qu'est-ce qui", "si"], 0, "qu'est-ce qui → ce qui.", "g"),
 q("<i>______ la vérité, il n'a rien dit.</i> (Knowing the truth)", ["Sachant", "En savant", "Savant", "Sachent"], 0, "Irregular present participle: sachant.", "g"),
 q("<i>Ça ne se fait pas</i> means…", ["That isn't done (it's not proper).", "That can't be made.", "It doesn't fit.", "That will never happen."], 0, "Reflexive passive meaning.", "v"),
 q("Which sentence is correct?", ["Les décisions ont été prises hier.", "Les décisions ont été pris hier.", "Les décisions sont été prises hier.", "Les décisions ont prises hier."], 0, "ont été + prises (f. pl.).", "g"),
 q("In a fairy tale: <i>Le prince ______ la princesse et ils ______ heureux.</i>", ["épousa … vécurent", "épousait … vivaient", "a épousé … vivent", "épouse … vivront"], 0, "Passé simple for the narrative events.", "v"),
 q("Best connector: <i>Les écrans sont utiles. ______, ils peuvent créer une dépendance.</i>", ["Néanmoins", "Par conséquent", "En effet", "Car"], 0, "Contrast → néanmoins.", "v"),
]
EXQ = [
 q("Passive: <i>La police a arrêté les voleurs.</i>", ["Les voleurs ont été arrêtés par la police.", "Les voleurs ont arrêté par la police.", "Les voleurs sont arrêtés la police.", "Les voleurs avaient arrêtés par la police."], 0, "ont été + arrêtés.", "g", "gram"),
 q("<i>Ce mot ______ comment ?</i> (How is this word pronounced?)", ["se prononce", "est prononcer", "prononce", "se prononcé"], 0, "Reflexive passive.", "g", "gram"),
 q("Gérondif of <i>lire</i>:", ["en lisant", "en lirant", "en lu", "en lisent"], 0, "nous lisons → lisant.", "g", "gram"),
 q("<i>Elle s'est blessée ______ du ski.</i>", ["en faisant", "en fait", "faisant", "à faire"], 0, "How it happened → gérondif.", "g", "gram"),
 q("<i>« J'aime ce film. »</i> → Il a dit qu'il ______ ce film.", ["aimait", "aime", "aimera", "a aimé"], 0, "présent → imparfait.", "g", "gram"),
 q("<i>« Où habites-tu ? »</i> → Elle m'a demandé ______.", ["où j'habitais", "où habites-tu", "si j'habitais", "ce que j'habitais"], 0, "Question word stays; normal word order; tense shifts.", "g", "gram"),
 q("<i>« Viens ici ! »</i> →", ["Il m'a dit de venir là.", "Il m'a dit que je viens ici.", "Il m'a dit viens ici.", "Il m'a demandé si je venais ici."], 0, "Command → de + infinitive; ici → là.", "g", "gram"),
 q("<i>hier</i> in reported speech becomes…", ["la veille", "le lendemain", "ce jour-là", "aujourd'hui"], 0, "the day before.", "v", "vocab"),
 q("<i>Elle eut</i> is the passé simple of…", ["avoir", "être", "aller", "entendre"], 0, "avoir → elle eut.", "v", "vocab"),
 q("<i>Ils vinrent</i> is the passé simple of…", ["venir", "vendre", "vivre", "voir"], 0, "venir → ils vinrent.", "v", "vocab"),
 q("Which means <i>moreover</i>?", ["en outre", "en revanche", "pourtant", "bref"], 0, "en outre = moreover.", "v", "vocab"),
 q("Which takes the subjunctive?", ["bien que", "même si", "parce que", "puisque"], 0, "bien que + subjunctive.", "g", "gram"),
 q(f"{listen('Les résultats seront publiés demain.')} What will happen tomorrow?", ["The results will be published.", "The results were published.", "Someone will publish a book.", "The results are being checked."], 0, "Passive futur: seront publiés.", "v", "listen"),
 q("Read: <i>Certains pensent que les réseaux sociaux isolent les jeunes. Il est vrai qu'ils peuvent remplacer les vraies rencontres. Cependant, ils permettent aussi de garder le contact avec des amis lointains. Par conséquent, tout dépend de l'usage qu'on en fait.</i> The writer's conclusion is…", ["It depends on how they're used.", "Social media always isolates young people.", "Social media should be banned.", "Real meetings are useless."], 0, "Par conséquent, tout dépend de l'usage.", "v", "read"),
 q("Which sentence is correct?", ["En arrivant à la gare, j'ai vu que le train était parti.", "En arrivant à la gare, le train était parti.", "En arrivant à la gare, le train est parti.", "Arrivant en à la gare, j'ai vu le train."], 0, "The gérondif must share the subject (je).", "g", "gram"),
]
FRQS = [
 {"q": "Essay (at least 200 words): Faut-il interdire les téléphones portables au lycée ?",
  "parts": [{"p": "Write an introduction, arguments for and against with examples, and a conclusion with your opinion.",
   "rubric": [["Clear structure: introduction, arguments for and against, conclusion", 2], ["At least six different connectors used correctly", 2], ["At least one subjunctive, one si clause and one passive or gérondif", 3], ["Opinion phrases (à mon avis, il me semble que…)", 1], ["Vocabulary range and accuracy", 2]],
   "answer": f'<div class="ex">{F("Aujourd\'hui, presque tous les lycéens ont un téléphone portable. Faut-il pour autant les interdire en classe ? D\'une part, il est vrai que les téléphones distraient les élèves : en regardant leurs messages, ils n\'écoutent plus le professeur. De plus, les réseaux sociaux peuvent favoriser le harcèlement. D\'autre part, le téléphone est aussi un outil utile. En effet, il permet de chercher une information rapidement ou de contacter ses parents en cas d\'urgence. Si on l\'interdisait complètement, on perdrait ces avantages. En conclusion, il me semble qu\'il faut que les écoles fixent des règles claires plutôt qu\'une interdiction totale : les téléphones pourraient être utilisés seulement quand le professeur le demande.")}<span class="en">A model essay using a gérondif (en regardant), connectors (d\'une part, de plus, d\'autre part, en effet, en conclusion), a si clause (si on l\'interdisait… on perdrait), a subjunctive (il faut que les écoles fixent) and a passive (pourraient être utilisés).</span></div>'}]},
 {"q": "Report this conversation in indirect speech, starting each line with a past reporting verb.",
  "parts": [{"p": "Léa : « Je suis fatiguée. J'ai travaillé toute la nuit. Demain, je dormirai jusqu'à midi. » Paul : « Tu veux un café ? »",
   "rubric": [["était fatiguée (présent → imparfait)", 1], ["avait travaillé (PC → PQP)", 1], ["dormirait jusqu'à midi le lendemain (futur → conditionnel, demain → le lendemain)", 2], ["Paul lui a demandé si elle voulait un café (si + imparfait)", 1]],
   "answer": f'<div class="ex">{F("Léa a dit qu\'elle était fatiguée et qu\'elle avait travaillé toute la nuit. Elle a ajouté que le lendemain, elle dormirait jusqu\'à midi. Paul lui a demandé si elle voulait un café.")}<span class="en">Every tense shifts back one step, and demain becomes le lendemain.</span></div>'}]},
]

if __name__ == "__main__":
    build(5, "college-5", "Le style", 'Le <span class="hl">style</span>',
          "College French: the passive voice, the gérondif, reported speech, recognizing the passé simple, and the connectors and structure of a French essay.",
          "College French Unit 5: passive voice, gérondif, reported speech, passé simple and essay writing, with audio, practice questions and a practice exam.",
          CH, PQ, CHAL, EXQ, FRQS, "/home/claude/ap-physics-study/courses/french-1/college-5.html", college=True)
