from fr_common import *

PR = [
 {"s": "Je", "v": "donne", "o": [["do", "le livre", "le"], ["io", "à Marie", "lui"]]},
 {"s": "Tu", "v": "montres", "o": [["do", "les photos", "les"], ["io", "à tes parents", "leur"]]},
 {"s": "Il", "pre": "me", "v": "montre", "o": [["do", "la photo", "la"]]},
 {"s": "Il", "v": "envoie", "o": [["do", "la lettre", "la"], ["io", "à Paul", "lui"]]},
 {"s": "Nous", "v": "mettons", "o": [["do", "les clés", "les"], ["loc", "dans le sac", "y"]]},
 {"s": "Elle", "v": "donne", "o": [["qty", "des bonbons", "en"], ["io", "aux enfants", "leur"]]},
 {"s": "Je", "v": "vais", "o": [["loc", "à Paris", "y"]]},
 {"s": "Tu", "v": "bois", "o": [["qty", "du café", "en"]]},
 {"s": "Vous", "v": "parlez", "o": [["io", "à votre prof", "lui"], ["qty", "de vos projets", "en"]]},
 {"s": "On", "v": "pense", "o": [["loc", "à l'examen", "y"]]},
]

CH = []
CORE = f'''<p>Pronouns let you talk like a native speaker instead of repeating every noun. You know <b>le, la, les</b> already. This unit adds the rest of the system: indirect objects (<b>lui, leur</b>), <b>y</b> and <b>en</b>, the order when you use two at once, and <b>relative pronouns</b> that link clauses together.</p>
{wa("One sentence, three pronouns", [
 ("a|Je|s  b|donne|v  c|des fleurs|x  d|à ma mère.|x", "A direct object (des fleurs, a quantity) and an indirect one (à ma mère).", "I give flowers to my mother."),
 ("a|Je|s  e|lui|n  b|donne|v  c|des fleurs.|x", "à + person → lui, before the verb.", "I give her flowers."),
 ("a|Je|s  e|lui|n  f|en|n  b|donne.|v", "des + noun → en, which always comes last.", "I give her some.")])}'''
CH.append(chapter("overview-c2", "Overview", "Overview", [topic("core-c2", "Les pronoms", CORE)]))

IO = topic("indirect", "Indirect objects: lui and leur", f'''
<p>An <b>indirect object</b> is a person introduced by <b>à</b>: <i>parler à quelqu'un, téléphoner à, donner à, dire à, écrire à, répondre à, demander à</i>.</p>
<div class="tblwrap"><table><tr><th></th><th>Direct (no à)</th><th>Indirect (à + person)</th></tr>
<tr><td>me, you, us, you</td><td colspan="2">{F("me, te, nous, vous")} (the same for both)</td></tr>
<tr><td>him / her / it</td><td>{F("le, la")}</td><td>{F("lui")}</td></tr>
<tr><td>them</td><td>{F("les")}</td><td>{F("leur")}</td></tr></table></div>
{ex("Je téléphone à ma grand-mère. → Je lui téléphone.", "I call my grandmother. → I call her.")}
{ex("Tu as parlé aux profs ? — Oui, je leur ai parlé.", "Did you talk to the teachers? — Yes, I talked to them.")}
{box("trap", "Different from English", f"Some verbs take a direct object in French but not in English, and the other way round. {F('regarder, écouter, chercher, attendre')} are direct ({F('je l’attends')}). {F('téléphoner à, répondre à, obéir à, ressembler à')} are indirect ({F('je lui réponds')}).")}
<p><b>leur</b> as a pronoun never takes an s: {F("je leur parle")}. (The possessive <i>leurs livres</i> is a different word.)</p>
''', pill=("g", "C2.1"), sub="à + person → lui / leur.")

YEN = topic("y-en", "Y and en", f'''
<div class="grid2"><div class="mini"><h4>{F("y")}: there, to it</h4><p>Replaces a place (à, en, dans, chez, sur + place) or <b>à + a thing</b>.<br>{F("Tu vas au cinéma ? — Oui, j'y vais.")}<br>{F("Tu penses à l'examen ? — J'y pense.")}</p></div>
<div class="mini"><h4>{F("en")}: some, of it, from there</h4><p>Replaces <b>de + noun</b>: partitives (du, de la, des), quantities, and verbs with de.<br>{F("Tu veux du café ? — Oui, j'en veux.")}<br>{F("Tu as combien de frères ? — J'en ai deux.")}<br>{F("Il parle de son voyage ? — Il en parle.")}</p></div></div>
{box("trap", "Keep the number", f"With a number or quantity, en replaces the noun but the number stays: {F('J’ai trois chats → J’en ai trois.')} {F('Elle boit beaucoup d’eau → Elle en boit beaucoup.')}")}
{box("plain", "People after à and de", f"For people, use lui / leur with à, and de + stress pronoun with de: {F('Je pense à ma sœur → Je pense à elle')} (not y). {F('Il parle de ses amis → Il parle d’eux')} (not en).")}
''', pill=("g", "C2.2"), sub="Places, things and quantities.")

ORDER = topic("double", "Two pronouns at once", f'''
<p>When two object pronouns go before the verb, they follow a fixed order:</p>
<div class="pr-order" style="font-size:15px"><span class="on">me / te / se / nous / vous</span><i>→</i><span class="on">le / la / les</span><i>→</i><span class="on">lui / leur</span><i>→</i><span class="on">y</span><i>→</i><span class="on">en</span></div>
{lab(type="pron", items=PR)}
{ex("Il me la montre.", "He shows it to me.")}
{ex("Je le lui ai donné.", "I gave it to him / her. (pronouns before avoir in the passé composé)")}
{ex("Il y en a trois.", "There are three of them.")}
<h3>In positive commands</h3>
<p>Pronouns go after the verb with hyphens, direct before indirect, and me / te become moi / toi: {F("Donne-le-moi !")} {F("Montrez-les-leur !")} {F("Vas-y !")} {F("Prends-en !")} In negative commands, normal order: {F("Ne me le donne pas !")}</p>
''', pill=("g", "C2.3"), sub="me le, le lui, y en.",
 det=("Pronouns with compound tenses and infinitives", '''<h4>Passé composé</h4><p>Pronouns go before avoir / être: <i>Je le lui ai dit.</i> With a direct object pronoun before avoir, the participle agrees: <i>Les lettres ? Je les lui ai envoyées.</i> No agreement with lui, leur, y or en.</p>
<h4>Two verbs</h4><p>Pronouns go before the infinitive they belong to: <i>Je vais le lui dire.</i> <i>Tu peux m'en donner ?</i></p>
<h4>Negation</h4><p>ne goes before the whole pronoun group, pas after the conjugated verb: <i>Je ne le lui ai pas dit.</i> <i>Il n'y en a plus.</i></p>'''))
CH.append(chapter("objects-c2", "Lui, leur, y, en", "Object pronouns", [IO, YEN, ORDER]))

REL = topic("relative", "Relative pronouns: qui, que, où, dont", f'''
<p>Relative pronouns join two sentences, like <i>who, which, that, where, whose</i>. French chooses by the pronoun's <b>job</b> in its own clause.</p>
<div class="tblwrap"><table><tr><th>Pronoun</th><th>Job in its clause</th><th>Example</th></tr>
<tr><td>{F("qui")}</td><td>subject (followed by a verb)</td><td>{F("La fille qui chante est ma sœur.")}</td></tr>
<tr><td>{F("que / qu'")}</td><td>direct object (followed by a subject)</td><td>{F("Le film que j'ai vu était génial.")}</td></tr>
<tr><td>{F("où")}</td><td>place or time</td><td>{F("La ville où j'habite est petite.")} {F("Le jour où je suis né…")}</td></tr>
<tr><td>{F("dont")}</td><td>replaces de + noun</td><td>{F("Le livre dont je parle…")} (parler de) {F("La fille dont le père est médecin…")} (whose)</td></tr></table></div>
{wa("Qui or que?", [
 ("a|J'ai un ami.|x  b|Il|s  c|parle|v  d|chinois.|x", "Two sentences. Il is the subject of the second.", ""),
 ("a|J'ai un ami|x  b|qui|n  c|parle|v  d|chinois.|x", "Replace the subject il → qui (a verb follows).", "I have a friend who speaks Chinese."),
 ("e|Le livre|x  f|est super.|x  g|Je|s  h|lis|v  i|ce livre.|x", "Two sentences. ce livre is the object of lis.", ""),
 ("e|Le livre|x  j|que|n  g|je|s  h|lis|v  f|est super.|x", "Replace the object → que (a subject follows).", "The book I'm reading is great.")])}
{box("trap", "English drops it, French never does", f"English can say <i>the book I read</i>. French must say {F('le livre que j’ai lu')}. And qui never elides: {F('l’ami qui arrive')} (not qu'arrive).")}
<h3>After a preposition: lequel</h3>
<p>After prepositions like <i>avec, pour, sur, dans, sans</i>, use <b>qui</b> for people and a form of <b>lequel</b> for things: {F("lequel, laquelle, lesquels, lesquelles")}. With à and de it contracts: {F("auquel, auxquels")}, {F("duquel")}.</p>
{ex("L'ami avec qui je travaille…", "The friend I work with…")}
{ex("La table sur laquelle j'ai mis mon sac…", "The table I put my bag on…")}
{ex("Le projet auquel je pense…", "The project I'm thinking about… (penser à)")}
''', pill=("g", "C2.4"), sub="who, which, that, where, whose.",
 det=("Ce qui, ce que, ce dont", '''<h4>"What" in the middle of a sentence</h4><p>When "what" means "the thing that", use <i>ce qui</i> (subject), <i>ce que</i> (object) or <i>ce dont</i> (with de): <i>Ce qui m'intéresse, c'est l'histoire.</i> <i>Dis-moi ce que tu veux.</i> <i>C'est ce dont j'ai besoin.</i></p>
<h4>Agreement after que</h4><p>In the passé composé with avoir, the participle agrees with que when que stands for a feminine or plural noun: <i>les chansons que j'ai écoutées</i>.</p>
<h4>Où for time</h4><p>English uses "when", but French uses où after a time noun: <i>le jour où</i>, <i>l'année où</i>, <i>au moment où</i>.</p>'''))

STRESS = topic("stress", "Stress pronouns", f'''
<p>{F("moi, toi, lui, elle, nous, vous, eux, elles")} are used:</p>
<ul><li>after prepositions: {F("avec moi")}, {F("chez eux")}, {F("pour elle")}</li>
<li>for emphasis: {F("Moi, je préfère le thé.")}</li>
<li>alone or after c'est: {F("— Qui a fait ça ? — Lui !")} {F("C'est toi ?")}</li>
<li>after que in comparisons: {F("plus grand que moi")}</li>
<li>with -même: {F("moi-même")} (myself), {F("eux-mêmes")}</li></ul>
''', pill=("g", "C2.5"), sub="moi, toi, lui, eux…")
CH.append(chapter("relative-c2", "Les pronoms relatifs", "Relative", [REL, STRESS]))

REV = topic("review-c2", "Unit summary", f'''<div class="grid2"><div class="mini"><h4>Object pronouns</h4><p>Direct: le, la, les. Indirect (à + person): lui, leur. y = place / à + thing. en = de + noun, quantities.</p></div>
<div class="mini"><h4>Order</h4><p>me/te/se/nous/vous → le/la/les → lui/leur → y → en. Positive commands: after the verb, direct before indirect.</p></div>
<div class="mini"><h4>Relatives</h4><p>qui (subject), que (object), où (place / time), dont (de + noun). Preposition + qui (people) / lequel (things).</p></div>
<div class="mini"><h4>Stress pronouns</h4><p>After prepositions, for emphasis, alone, after que. À + person with penser: à lui, à elle.</p></div></div>''', sub="Everything from this unit on one screen.")
MIS = topic("mistakes-c2", "Common mistakes", '''<ol class="steps">
<li><i>Je le téléphone</i> → <i>Je lui téléphone</i> (téléphoner à).</li>
<li><i>Je lui attends</i> → <i>Je l'attends</i> (attendre is direct).</li>
<li><i>Je lui le donne</i> → <i>Je le lui donne</i>.</li>
<li><i>J'en ai</i> instead of <i>J'en ai deux</i>: keep the number.</li>
<li><i>Le film qui j'ai vu</i> → <i>le film que j'ai vu</i> (a subject follows).</li>
<li><i>Le livre que je parle</i> → <i>le livre dont je parle</i> (parler de).</li>
<li><i>leurs</i> as an object pronoun → <i>leur</i>.</li></ol>''', sub="Points students lose most often.")
CH.append(chapter("review-ch-c2", "Review", "Review", [REV, MIS]))

PQ = [
 q("<i>Je parle à mon père.</i> → Je ______ parle.", ["lui", "le", "leur", "y"], 0, "à + one person → lui.", "g"),
 q("<i>Tu écris à tes cousins ?</i> → Tu ______ écris ?", ["leur", "les", "leurs", "eux"], 0, "à + people (plural) → leur.", "g"),
 q("<i>J'attends le bus.</i> → Je ______ attends.", ["l'", "lui", "y", "en"], 0, "attendre takes a direct object.", "g"),
 q("<i>Elle répond au professeur.</i> → Elle ______ répond.", ["lui", "le", "y", "en"], 0, "répondre à + person.", "g"),
 q("<i>Nous allons à la plage.</i> → Nous ______ allons.", ["y", "en", "la", "lui"], 0, "Place with à → y.", "g"),
 q("<i>Tu veux du pain ?</i> → Oui, j'______ veux.", ["en", "y", "le", "lui"], 0, "Partitive → en.", "g"),
 q("<i>J'ai trois sœurs.</i> → J'en ai ______.", ["trois", "—", "des", "les"], 0, "Keep the number with en.", "g"),
 q("<i>Il pense à son examen.</i> → Il ______ pense.", ["y", "lui", "en", "le"], 0, "à + thing → y.", "g"),
 q("<i>Il pense à sa copine.</i> → Il pense ______.", ["à elle", "y", "lui", "à la"], 0, "penser à + person → stress pronoun.", "g"),
 q("<i>Je donne le cadeau à Paul.</i> → Je ______ donne.", ["le lui", "lui le", "le leur", "l'y"], 0, "le before lui.", "g"),
 q("<i>Il me montre la photo.</i> → Il ______ montre.", ["me la", "la me", "me le", "la lui"], 0, "me before la.", "g"),
 q("<i>Elle met les livres sur l'étagère.</i> → Elle ______ met.", ["les y", "y les", "les en", "leur y"], 0, "les before y.", "g"),
 q("<i>Il y a des pommes ?</i> → Oui, il ______ a.", ["y en", "en y", "y les", "les y"], 0, "y before en.", "g"),
 q("<i>Give it to me!</i>", ["Donne-le-moi !", "Donne-moi-le !", "Me le donne !", "Donne-le-me !"], 0, "Positive command: direct before indirect; me → moi.", "g"),
 q("<i>Don't give it to me!</i>", ["Ne me le donne pas !", "Ne donne-le-moi pas !", "Ne le me donne pas !", "Ne donne pas le-moi !"], 0, "Negative command: normal order before the verb.", "g"),
 q("<i>La femme ______ parle est ma prof.</i>", ["qui", "que", "dont", "où"], 0, "A verb follows → subject → qui.", "g"),
 q("<i>Le pull ______ j'ai acheté est bleu.</i>", ["que", "qui", "dont", "où"], 0, "A subject follows → object → que.", "g"),
 q("<i>La ville ______ je suis né est petite.</i>", ["où", "que", "qui", "dont"], 0, "Place → où.", "g"),
 q("<i>Le livre ______ tu as besoin est ici.</i>", ["dont", "que", "qui", "où"], 0, "avoir besoin de → dont.", "g"),
 q("<i>L'ami avec ______ je voyage…</i>", ["qui", "lequel", "que", "dont"], 0, "Preposition + person → qui.", "g"),
 q("<i>La chaise sur ______ il est assis…</i>", ["laquelle", "qui", "lequel", "que"], 0, "Preposition + thing → lequel, agreeing: chaise (f.) → laquelle.", "g"),
 q("<i>Dis-moi ______ tu veux.</i> (what)", ["ce que", "que", "quoi", "ce qui"], 0, "the thing that, object → ce que.", "g"),
 q("<i>Moi, je préfère le thé</i>: moi is used for…", ["emphasis", "a direct object", "a command", "a place"], 0, "Stress pronoun for emphasis.", "g"),
 q(f"{listen('Je le lui ai déjà dit.')} What does the speaker mean?", ["I already told him / her.", "I already told them.", "He already told me.", "I'll tell him tomorrow."], 0, "le lui ai dit = told it to him / her.", "v"),
]
CHAL = [
 q("<i>Les lettres ? Je les lui ai ______.</i>", ["envoyées", "envoyé", "envoyés", "envoyer"], 0, "Agreement with the preceding direct object les (lettres, f. pl.).", "g"),
 q("<i>Je vais parler de mes projets à mon prof.</i> → Je vais ______ parler.", ["lui en", "en lui", "le lui", "lui y"], 0, "lui before en; pronouns before the infinitive.", "g"),
 q("<i>Le projet ______ je pense…</i> (penser à)", ["auquel", "duquel", "dont", "lequel"], 0, "à + lequel → auquel.", "g"),
 q("<i>______ m'étonne, c'est sa réaction.</i>", ["Ce qui", "Ce que", "Qui", "Ce dont"], 0, "Subject of m'étonne → ce qui.", "g"),
 q("<i>La fille ______ le frère est mon ami…</i>", ["dont", "que", "qui", "où"], 0, "whose → dont.", "g"),
 q("<i>Ne ______ parle pas !</i> (don't talk to them about it)", ["leur en", "en leur", "les en", "leur y"], 0, "leur before en.", "g"),
 q("Which is correct?", ["Le jour où je l'ai rencontrée…", "Le jour quand je l'ai rencontrée…", "Le jour que je l'ai rencontrée…", "Le jour dont je l'ai rencontrée…"], 0, "Time noun + où.", "g"),
 q("<i>Montre les photos à tes grands-parents !</i> →", ["Montre-les-leur !", "Montre-leur-les !", "Les leur montre !", "Montre-les-eux !"], 0, "Direct before indirect after the verb.", "g"),
]
EXQ = [
 q("<i>J'obéis à mes parents.</i> → J'______ obéis.", ["leur", "les", "y", "en"], 0, "obéir à + people → leur.", "g", "gram"),
 q("<i>Tu cherches tes clés ?</i> → Tu ______ cherches ?", ["les", "leur", "y", "en"], 0, "chercher is direct.", "g", "gram"),
 q("<i>Elle revient de Paris.</i> → Elle ______ revient.", ["en", "y", "la", "lui"], 0, "de + place → en.", "g", "gram"),
 q("<i>Nous avons beaucoup de travail.</i> → Nous ______ avons beaucoup.", ["en", "y", "le", "les"], 0, "Quantity → en, keep beaucoup.", "g", "gram"),
 q("<i>Je montre mon dessin à ma sœur.</i> →", ["Je le lui montre.", "Je lui le montre.", "Je la lui montre.", "Je le leur montre."], 0, "dessin (m.) → le, à ma sœur → lui.", "g", "gram"),
 q("<i>Il nous envoie des messages.</i> →", ["Il nous en envoie.", "Il en nous envoie.", "Il nous les envoie.", "Il leur en envoie."], 0, "des messages → en; nous stays.", "g", "gram"),
 q("<i>Go there!</i> (tu, aller)", ["Vas-y !", "Va-y !", "Y va !", "Allez-y toi !"], 0, "The s comes back before y.", "g", "gram"),
 q("<i>Les gens ______ habitent ici sont sympas.</i>", ["qui", "que", "dont", "où"], 0, "Subject → qui.", "g", "gram"),
 q("<i>La chanson ______ tu écoutes est française.</i>", ["que", "qui", "dont", "où"], 0, "Object → que.", "g", "gram"),
 q("<i>C'est le prof ______ je t'ai parlé.</i>", ["dont", "que", "qui", "où"], 0, "parler de → dont.", "g", "gram"),
 q("<i>Le restaurant ______ nous avons dîné…</i>", ["où", "que", "dont", "qui"], 0, "Place → où.", "g", "gram"),
 q("<i>Le stylo avec ______ j'écris…</i>", ["lequel", "laquelle", "qui", "que"], 0, "Thing after a preposition: lequel (stylo, m.).", "g", "gram"),
 q("<i>Je ne sais pas ______ s'est passé.</i>", ["ce qui", "ce que", "qui", "que"], 0, "Subject of s'est passé → ce qui.", "g", "gram"),
 q(f"{listen('Tu en veux encore ? — Non merci, j’en ai assez.')} What is being offered?", ["more of something (food or drink)", "a place to go", "a person", "nothing"], 0, "en = some (of it).", "v", "listen"),
 q("Read: <i>Mon ami Hugo, que je connais depuis l'école primaire, habite maintenant à Lyon, où il étudie la médecine. Je lui écris souvent et il m'en parle avec passion.</i> What does Hugo talk about with passion?", ["medicine", "primary school", "the writer", "Lyon's restaurants"], 0, "en = de la médecine (his studies).", "v", "read"),
]
FRQS = [
 {"q": "Answer each question in a full sentence, replacing every object with a pronoun.",
  "parts": [{"p": "1. Tu as donné ton numéro à Léa ?  2. Tu vas à la bibliothèque ce soir ?  3. Combien de cours as-tu ce semestre ?  4. Tu as parlé de tes notes à tes parents ?",
   "rubric": [["1. Oui, je le lui ai donné (le before lui, before avoir)", 1], ["2. Oui, j'y vais (or Non, je n'y vais pas)", 1], ["3. J'en ai quatre (keeps the number)", 1], ["4. Oui, je leur en ai parlé (leur before en)", 1]],
   "answer": f'<div class="ex">{F("Oui, je le lui ai donné.")}<span class="en">Yes, I gave it to her.</span></div><div class="ex">{F("Oui, j\'y vais ce soir.")}<span class="en">Yes, I\'m going there tonight.</span></div><div class="ex">{F("J\'en ai quatre.")}<span class="en">I have four (of them).</span></div><div class="ex">{F("Oui, je leur en ai parlé.")}<span class="en">Yes, I talked to them about it.</span></div>'}]},
 {"q": "Describe a person who matters to you (at least 6 sentences) using at least five relative pronouns.",
  "parts": [{"p": "Use qui, que, où and dont at least once each, and one preposition + qui / lequel.",
   "rubric": [["qui and que used correctly", 2], ["où used correctly (place or time)", 1], ["dont used correctly", 1], ["Preposition + qui / lequel", 1], ["Agreement and overall accuracy", 1]],
   "answer": f'<div class="ex">{F("Ma grand-mère est la personne qui m\'a appris à cuisiner. C\'est une femme que tout le monde adore. Elle habite dans un petit village où je passais tous mes étés. Elle a un jardin dont elle est très fière. C\'est la personne avec qui je parle le plus de mes projets. La recette que je préfère, c\'est sa tarte aux pommes.")}<span class="en">My grandmother is the person who taught me to cook. She\'s a woman everyone loves. She lives in a small village where I spent all my summers. She has a garden she\'s very proud of. She\'s the person I talk with most about my plans. The recipe I like best is her apple tart.</span></div>'}]},
]

if __name__ == "__main__":
    build(2, "college-2", "Les pronoms", 'Les <span class="hl">pronoms</span>',
          "College French: lui / leur, y, en, double object pronouns, relative pronouns (qui, que, où, dont, lequel) and stress pronouns.",
          "College French Unit 2: object pronouns, y, en, pronoun order and relative pronouns, with audio, interactive labs, practice questions and a practice exam.",
          CH, PQ, CHAL, EXQ, FRQS, "/home/claude/ap-physics-study/courses/french-1/college-2.html", college=True)
