from fr_common import *

CH = []
CORE = f'''<p>So far everything has been in the present. In this unit you learn to talk about <b>tomorrow</b> (the futur proche) and <b>yesterday</b> (the passé composé). Both tenses are built from two words: a helper verb you already know plus a second verb.</p>
{wa("Present, future, past", [
 ("s|Je|s  v|regarde|v  r|un film.|x", "Present: one verb.", "I'm watching a movie."),
 ("s|Je|s  a|vais|n  v|regarder|v  r|un film.|x", "Futur proche: aller + infinitive.", "I'm going to watch a movie."),
 ("s|J'|s  a|ai|n  v|regardé|v  r|un film.|x", "Passé composé: avoir + past participle.", "I watched a movie.")])}
<div class="grid2"><div class="mini"><h4>In this unit</h4><p>The futur proche · the passé composé with avoir · with être · negatives and questions in the past · reflexive verbs and your daily routine · words for telling a story in order.</p></div>
<div class="mini"><h4>Habit to build</h4><p>Every evening, say three sentences out loud about what you did today and one about what you're going to do tomorrow.</p></div></div>'''
CH.append(chapter("overview-f5", "Overview", "Overview", [topic("core-f5", "Hier et demain", CORE)]))

# ------------------------------------------------------------------ futur proche
FP = topic("futur-proche", "The futur proche: going to do something", f'''
<p>Conjugate {F("aller")} in the present and add an <b>infinitive</b>. That's it.</p>
{ex("Je vais étudier ce soir.", "I'm going to study tonight.")}
{ex("Nous allons voyager en France cet été.", "We're going to travel to France this summer.")}
{ex("Ils vont manger au restaurant.", "They're going to eat at the restaurant.")}
{lab(type="conj", verbs=["parler", "finir", "faire", "aller", "prendre", "voir", "se lever"], tenses=["fp"])}
<h3>Negative</h3>
<p>ne … pas wraps <b>aller</b>: {F("Je ne vais pas sortir.")} (I'm not going to go out.)</p>
<h3>Time words for the future</h3>
{vgrid([("demain", "tomorrow"), ("ce soir", "tonight"), ("ce week-end", "this weekend"), ("la semaine prochaine", "next week"), ("le mois prochain", "next month"), ("l'année prochaine", "next year"), ("bientôt", "soon"), ("plus tard", "later")])}
''', pill=("g", "5.1"), sub="aller + infinitive.",
 det=("More on the futur proche", '''<h4>When to use it</h4><p>For plans and things about to happen. French also has a one-word future (je parlerai), which you'll learn in French 2; the futur proche is more common in conversation.</p>
<h4>With reflexive verbs</h4><p>The reflexive pronoun goes with the infinitive and matches the subject: <i>Je vais me lever à 7 h.</i> <i>Tu vas te coucher ?</i></p>
<h4>Don't confuse with aller + place</h4><p><i>Je vais au parc</i> = I'm going to the park (movement). <i>Je vais jouer au parc</i> = I'm going to play in the park (plan).</p>'''))
CH.append(chapter("fp-f5", "Le futur proche", "Future", [FP]))

# ------------------------------------------------------------------ passé composé avoir
PCA = topic("pc-avoir", "The passé composé with avoir", f'''
<p>The passé composé tells what happened: <i>I ate, I have eaten, I did eat</i>. Build it from <b>avoir</b> in the present + a <b>past participle</b>.</p>
<div class="tblwrap"><table><tr><th>Verb type</th><th>Past participle</th><th>Example</th></tr>
<tr><td>-er</td><td>-é</td><td>{F("parler → parlé")}: {F("j'ai parlé")}</td></tr>
<tr><td>-ir</td><td>-i</td><td>{F("finir → fini")}: {F("tu as fini")}</td></tr>
<tr><td>-re</td><td>-u</td><td>{F("vendre → vendu")}: {F("il a vendu")}</td></tr></table></div>
{wa("Building the passé composé", [
 ("s|Nous|s  v|mangeons|v  r|une pizza.|x", "Present: nous mangeons.", "We eat a pizza."),
 ("s|Nous|s  a|avons|n  v|mangé|v  r|une pizza.|x", "Past: avoir (nous avons) + manger → mangé.", "We ate a pizza."),
 ("s|Nous|s  n1|n'|x  a|avons|n  n2|pas|x  v|mangé|v  r2|de pizza.|x", "Negative: ne … pas wraps the helper verb avons. une → de.", "We didn't eat pizza.")])}
<h3>Irregular past participles</h3>
{vt([("avoir → eu", "had", "J'ai eu de la chance."), ("être → été", "been", "Il a été malade."), ("faire → fait", "did, made", "Tu as fait tes devoirs ?"), ("prendre → pris", "took", "Nous avons pris le bus."), ("mettre → mis", "put", "J'ai mis mon manteau."), ("voir → vu", "saw", "Elle a vu un film."), ("boire → bu", "drank", "Ils ont bu du jus."), ("lire → lu", "read", "J'ai lu le livre."), ("vouloir → voulu", "wanted", ""), ("pouvoir → pu", "could", ""), ("devoir → dû", "had to", ""), ("écrire → écrit", "wrote", "Il a écrit une lettre."), ("dire → dit", "said", "Qu'est-ce qu'elle a dit ?")], head=("Verb", "English", "Example"))}
{lab(type="conj", verbs=["parler", "manger", "finir", "choisir", "vendre", "attendre", "faire", "prendre", "voir", "boire", "lire", "écrire", "avoir", "être"], tenses=["pc", "pres"])}
''', pill=("g", "5.2"), sub="j'ai mangé, tu as fini, il a vendu.",
 det=("Using the passé composé", '''<h4>One French tense, three English ones</h4><p><i>J'ai mangé</i> can mean I ate, I have eaten, or I did eat. Don't add words: "I have eaten" is still just <i>j'ai mangé</i>.</p>
<h4>Placement of adverbs</h4><p>Short adverbs go between the helper verb and the participle: <i>J'ai bien dormi</i> (I slept well), <i>Il a déjà mangé</i> (he already ate), <i>Tu as beaucoup travaillé</i>.</p>
<h4>Questions</h4><p>Intonation or est-ce que work as usual: <i>Tu as fini ?</i>, <i>Est-ce que tu as fini ?</i> For inversion, swap the helper verb and subject: <i>As-tu fini ?</i>, <i>A-t-il mangé ?</i></p>'''))
CH.append(chapter("pca-f5", "Le passé composé avec avoir", "Past: avoir", [PCA]))

# ------------------------------------------------------------------ passé composé être
PCE = topic("pc-etre", "The passé composé with être", f'''
<p>About 17 verbs, mostly about <b>movement</b> or <b>change of state</b>, use <b>être</b> instead of avoir. A common memory trick is <b>DR &amp; MRS VANDERTRAMP</b>:</p>
<div class="tblwrap"><table><tr><th></th><th>Verb</th><th>Participle</th><th></th><th>Verb</th><th>Participle</th></tr>
<tr><td>D</td><td>devenir (become)</td><td>devenu</td><td>V</td><td>venir (come)</td><td>venu</td></tr>
<tr><td>R</td><td>revenir (come back)</td><td>revenu</td><td>A</td><td>aller (go)</td><td>allé</td></tr>
<tr><td>M</td><td>monter (go up)</td><td>monté</td><td>N</td><td>naître (be born)</td><td>né</td></tr>
<tr><td>R</td><td>rester (stay)</td><td>resté</td><td>D</td><td>descendre (go down)</td><td>descendu</td></tr>
<tr><td>S</td><td>sortir (go out)</td><td>sorti</td><td>E</td><td>entrer (enter)</td><td>entré</td></tr>
<tr><td></td><td></td><td></td><td>R</td><td>rentrer (go home)</td><td>rentré</td></tr>
<tr><td></td><td></td><td></td><td>T</td><td>tomber (fall)</td><td>tombé</td></tr>
<tr><td></td><td></td><td></td><td>R</td><td>retourner (return)</td><td>retourné</td></tr>
<tr><td></td><td></td><td></td><td>A</td><td>arriver (arrive)</td><td>arrivé</td></tr>
<tr><td></td><td></td><td></td><td>M</td><td>mourir (die)</td><td>mort</td></tr>
<tr><td></td><td></td><td></td><td>P</td><td>partir (leave)</td><td>parti</td></tr></table></div>
<h3>Agreement</h3>
<p>With être, the participle <b>agrees with the subject</b> like an adjective: add -e for feminine, -s for plural.</p>
{wa("The participle agrees", [
 ("s|Il|s  a|est|n  v|allé|v  r|au parc.|x", "Masculine singular: allé.", "He went to the park."),
 ("s|Elle|s  a|est|n  v|allée|v  r|au parc.|x", "Feminine: add -e → allée.", "She went to the park."),
 ("s|Ils|s  a|sont|n  v|allés|v  r|au parc.|x", "Masculine plural: allés.", "They went to the park."),
 ("s|Elles|s  a|sont|n  v|allées|v  r|au parc.|x", "Feminine plural: allées. All four sound the same!", "They (f.) went to the park.")])}
{lab(type="conj", verbs=["aller", "venir", "partir", "sortir", "arriver", "rester", "tomber"], tenses=["pc", "pres"])}
{ex("Ma sœur est née en 2010.", "My sister was born in 2010.")}
{ex("Nous sommes rentrés tard.", "We got home late.")}
''', pill=("g", "5.3"), sub="DR & MRS VANDERTRAMP, and agreement.",
 det=("Être verbs in detail", '''<h4>The house of être</h4><p>Another way to remember them: picture a house. You're born (naître), arrive, enter, go up the stairs (monter), stay, go down (descendre), fall, go out, leave, return, and die (mourir). The verbs describe moving in, out, up and down.</p>
<h4>vous and on</h4><p><i>vous</i> can be one person or several: <i>Vous êtes allé</i> (one man, formal), <i>Vous êtes allées</i> (several women). With <i>on</i> meaning "we", many writers agree in the plural: <i>On est partis.</i></p>
<h4>Not every movement verb</h4><p><i>marcher</i> (walk), <i>courir</i> (run), <i>voyager</i> and <i>nager</i> use avoir: <i>J'ai marché.</i> Only the list verbs take être.</p>'''))
CH.append(chapter("pce-f5", "Le passé composé avec être", "Past: être", [PCE]))

# ------------------------------------------------------------------ routine / reflexives
REFL = topic("reflexive", "Reflexive verbs and your daily routine", f'''
<p>Reflexive verbs have an extra pronoun that refers back to the subject: {F("je me lève")} (I get up, literally "I raise myself").</p>
<div class="tblwrap"><table class="conj"><tr><td>{F("je me lève")}</td><td>{F("nous nous levons")}</td></tr>
<tr><td>{F("tu te lèves")}</td><td>{F("vous vous levez")}</td></tr>
<tr><td>{F("il / elle se lève")}</td><td>{F("ils / elles se lèvent")}</td></tr></table></div>
<p>me, te, se become <b>m', t', s'</b> before a vowel: {F("je m'habille")}, {F("il s'appelle")}.</p>
{vt([("se réveiller", "to wake up"), ("se lever", "to get up"), ("se doucher", "to shower"), ("se brosser les dents", "to brush your teeth"), ("s'habiller", "to get dressed"), ("se dépêcher", "to hurry"), ("se reposer", "to rest"), ("s'amuser", "to have fun"), ("se coucher", "to go to bed"), ("s'appeler", "to be named")])}
{lab(type="conj", verbs=["se lever", "se coucher", "s'habiller"], tenses=["pres", "pc", "fp"])}
<h3>In the past</h3>
<p>All reflexive verbs use <b>être</b> in the passé composé, and the participle usually agrees: {F("Elle s'est levée à sept heures.")} The pronoun stays right before être.</p>
<h3>Negative</h3>
<p>ne goes before the pronoun: {F("Je ne me lève pas tôt.")} {F("Il ne s'est pas douché.")}</p>
{wa("My morning", [
 ("a|D'abord,|gl  s|je|s  p|me|x  v|réveille|v", "First, I wake up.", "First, I wake up."),
 ("a|Ensuite,|gl  s|je|s  p|me|x  v|douche|v", "Then I shower.", "Then I shower."),
 ("a|Puis,|gl  s|je|s  p|m'|x  v|habille|v", "Next, I get dressed: me → m' before a vowel.", "Next, I get dressed."),
 ("a|Enfin,|gl  s|je|s  p|me|x  v|dépêche|v", "Finally, I hurry!", "Finally, I hurry.")])}
''', pill=("g", "5.4"), sub="se lever, s'habiller, se coucher.",
 det=("Reflexive verbs in detail", '''<h4>Same verb, two meanings</h4><p><i>Je lave la voiture</i> (I wash the car) vs <i>Je me lave</i> (I wash myself). Many verbs can be used both ways.</p>
<h4>Body parts</h4><p>With a reflexive verb, use le / la / les for body parts: <i>Je me brosse les dents</i>, not "mes dents".</p>
<h4>Infinitives</h4><p>After another verb, the pronoun still matches the subject: <i>J'aime me promener</i>, <i>Nous devons nous lever tôt</i>.</p>'''))

STORY = topic("story", "Telling a story in order", f'''
{vgrid([("hier", "yesterday"), ("avant-hier", "the day before yesterday"), ("hier soir", "last night"), ("la semaine dernière", "last week"), ("le week-end dernier", "last weekend"), ("il y a deux jours", "two days ago"), ("d'abord", "first"), ("ensuite / puis", "then, next"), ("après", "after"), ("enfin", "finally"), ("déjà", "already"), ("ne … pas encore", "not yet")])}
{ex("Hier, je me suis levé à huit heures. D'abord, j'ai pris le petit-déjeuner. Ensuite, je suis allé au lycée. Le soir, j'ai fait mes devoirs et je me suis couché à dix heures.", "Yesterday I got up at eight. First I had breakfast. Then I went to school. In the evening I did my homework and went to bed at ten.")}
''', pill=("v", "5.5"), sub="hier, d'abord, ensuite, enfin.")
CH.append(chapter("routine-f5", "La routine: Reflexive verbs", "Routine", [REFL, STORY]))

REV = topic("review-f5", "Unit 5 summary", f'''<div class="grid2"><div class="mini"><h4>Futur proche</h4><p>aller + infinitive: je vais manger. Negative: je ne vais pas manger.</p></div>
<div class="mini"><h4>Passé composé (avoir)</h4><p>avoir + participle: -er → é, -ir → i, -re → u. Irregulars: eu, été, fait, pris, mis, vu, bu, lu, écrit.</p></div>
<div class="mini"><h4>Passé composé (être)</h4><p>DR &amp; MRS VANDERTRAMP + all reflexive verbs. The participle agrees: elle est allée, ils sont partis.</p></div>
<div class="mini"><h4>Negatives and order</h4><p>ne … pas wraps the helper verb: je n'ai pas fini, elle n'est pas venue. Time words: hier, d'abord, ensuite, enfin.</p></div></div>''', sub="Everything from this unit on one screen.")
MIS = topic("mistakes-f5", "Common mistakes", '''<ol class="steps">
<li>Using avoir with an être verb: <i>J'ai allé</i> → <i>Je suis allé(e)</i>.</li>
<li>Forgetting agreement with être: <i>Elle est parti</i> → <i>Elle est partie</i>.</li>
<li>Making avoir verbs agree with the subject: <i>Elle a mangée</i> → <i>Elle a mangé</i>.</li>
<li>Putting pas after the participle: <i>Je n'ai mangé pas</i> → <i>Je n'ai pas mangé</i>.</li>
<li>Regular-izing irregulars: <i>j'ai prendu</i> → <i>j'ai pris</i>; <i>j'ai faisé</i> → <i>j'ai fait</i>.</li>
<li>Futur proche with a conjugated second verb: <i>Je vais mange</i> → <i>Je vais manger</i>.</li>
<li>Reflexive pronoun not matching: <i>Nous se levons</i> → <i>Nous nous levons</i>.</li></ol>''', sub="Points students lose most often.")
CH.append(chapter("review-ch-f5", "Review", "Review", [REV, MIS]))

PQ = [
 q("<i>Demain, je ______ jouer au tennis.</i>", ["vais", "va", "vas", "allons"], 0, "Futur proche: je vais + infinitive.", "g"),
 q("<i>Ils vont ______ un film.</i>", ["regarder", "regardent", "regardé", "regardez"], 0, "After aller, use the infinitive.", "g"),
 q("Make it negative: <i>Nous allons partir.</i>", ["Nous n'allons pas partir.", "Nous allons ne pas partir.", "Nous n'allons partir pas.", "Nous ne allons pas partir."], 0, "Wrap aller: n'allons pas.", "g"),
 q("<i>la semaine prochaine</i> means…", ["next week", "last week", "this week", "every week"], 0, "prochain = next, dernier = last.", "v"),
 q("Past participle of <i>finir</i>:", ["fini", "finé", "finu", "finis"], 0, "-ir → -i.", "g"),
 q("Past participle of <i>attendre</i>:", ["attendu", "attendé", "attendi", "attendre"], 0, "-re → -u.", "g"),
 q("Past participle of <i>faire</i>:", ["fait", "faisé", "fai", "faisu"], 0, "faire → fait.", "g"),
 q("Past participle of <i>prendre</i>:", ["pris", "prendu", "prené", "prit"], 0, "prendre → pris.", "g"),
 q("<i>Hier, nous ______ une pizza.</i>", ["avons mangé", "sommes mangés", "avons manger", "mangeons"], 0, "manger takes avoir: nous avons mangé.", "g"),
 q("<i>Tu ______ tes devoirs ?</i> (did you do)", ["as fait", "es fait", "as faire", "a fait"], 0, "tu as + fait.", "g"),
 q("Which verb uses <b>être</b> in the passé composé?", ["arriver", "manger", "regarder", "finir"], 0, "arriver is in DR & MRS VANDERTRAMP.", "g"),
 q("<i>Elle ______ au cinéma.</i> (went)", ["est allée", "a allé", "est allé", "a allée"], 0, "aller takes être, and the participle agrees with elle: allée.", "g"),
 q("<i>Mes parents ______ à huit heures.</i> (left)", ["sont partis", "ont parti", "sont parti", "ont partis"], 0, "partir takes être; masculine plural → partis.", "g"),
 q("<i>Marie et Julie ______ à la maison.</i> (stayed)", ["sont restées", "ont resté", "sont resté", "sont restés"], 0, "être + agreement: feminine plural → restées.", "g"),
 q("Make it negative: <i>J'ai vu le film.</i>", ["Je n'ai pas vu le film.", "Je n'ai vu pas le film.", "Je ne pas ai vu le film.", "J'ai ne pas vu le film."], 0, "Wrap the helper verb: n'ai pas vu.", "g"),
 q("Make it negative: <i>Il est venu.</i>", ["Il n'est pas venu.", "Il n'est venu pas.", "Il ne est pas venu.", "Il est pas venu ne."], 0, "n'est pas venu.", "g"),
 q("<i>Je ______ à sept heures.</i> (I get up)", ["me lève", "lève", "se lève", "me lèves"], 0, "je → me, and the -er ending -e.", "g"),
 q("<i>Nous ______ tard le samedi.</i> (go to bed)", ["nous couchons", "se couchons", "nous couchez", "couchons nous"], 0, "nous → nous + -ons.", "g"),
 q("<i>Tu ______ vite le matin.</i> (get dressed)", ["t'habilles", "te habilles", "s'habilles", "t'habille"], 0, "te → t' before a vowel; tu → -es.", "g"),
 q("<i>Ce matin, elle ______ à six heures.</i> (got up)", ["s'est levée", "a levé", "s'a levée", "s'est levé"], 0, "Reflexive → être, and agreement with elle.", "g"),
 q("<i>il y a trois jours</i> means…", ["three days ago", "there are three days", "in three days", "for three days"], 0, "il y a + time = ago.", "v"),
 q("Put in order: <i>enfin, d'abord, ensuite</i>", ["d'abord, ensuite, enfin", "enfin, ensuite, d'abord", "ensuite, d'abord, enfin", "d'abord, enfin, ensuite"], 0, "first, then, finally.", "v"),
 q("<i>Ils ______ du jus d'orange.</i> (drank)", ["ont bu", "ont buvé", "sont bus", "ont boit"], 0, "boire → bu, with avoir.", "g"),
 q(f"{listen('Elle est née à Paris.')} What does it say?", ["She was born in Paris.", "She lives in Paris.", "She's going to Paris.", "She left Paris."], 0, "naître → née (être + agreement).", "v"),
]
CHAL = [
 q("Which sentence is correct?", ["Elles sont arrivées et elles ont mangé.", "Elles ont arrivé et elles sont mangées.", "Elles sont arrivé et elles ont mangées.", "Elles sont arrivées et elles ont mangées."], 0, "arriver → être + agreement; manger → avoir, no agreement with the subject.", "g"),
 q("<i>Je ne ______ pas ______ ce matin.</i> (I didn't shower)", ["me suis … douché", "suis … me douché", "me ai … douché", "me suis … doucher"], 0, "ne + pronoun + être + pas + participle.", "g"),
 q("Which uses the futur proche correctly with a reflexive verb?", ["Nous allons nous coucher tôt.", "Nous allons se coucher tôt.", "Nous nous allons coucher tôt.", "Nous allons coucher nous tôt."], 0, "The pronoun matches the subject and goes before the infinitive.", "g"),
 q("Which verb takes <b>avoir</b> even though it's about movement?", ["marcher", "sortir", "monter", "tomber"], 0, "Only the list verbs take être; marcher (to walk) takes avoir.", "g"),
 q("<i>Vous ______, Madame ?</i> (Did you come? one woman)", ["êtes venue", "êtes venus", "avez venu", "êtes venu"], 0, "venir → être; one woman → venue.", "g"),
 q("Which sentence is correct?", ["Il a déjà fini ses devoirs.", "Il a fini déjà ses devoirs.", "Il déjà a fini ses devoirs.", "Il est déjà fini ses devoirs."], 0, "Short adverbs go between the helper and the participle.", "g"),
 q("<i>Hier soir, nous ______ au restaurant et nous ______ du poisson.</i>", ["sommes allés … avons pris", "avons allé … sommes pris", "sommes allés … sommes pris", "allons … prenons"], 0, "aller → être; prendre → avoir + pris.", "g"),
 q("Which question is correct?", ["As-tu vu Paul ?", "Avez-tu vu Paul ?", "As tu vu Paul ?", "Tu-as vu Paul ?"], 0, "Inversion with the helper verb and a hyphen: As-tu… ?", "g"),
]
EXQ = [
 q("<i>Ce soir, nous ______ étudier.</i>", ["allons", "allez", "vont", "vais"], 0, "nous allons + infinitive.", "g", "gram"),
 q("<i>Tu vas ______ quoi ce week-end ?</i>", ["faire", "fais", "fait", "faites"], 0, "aller + infinitive.", "g", "gram"),
 q("Past participle of <i>voir</i>:", ["vu", "voi", "voyé", "vit"], 0, "voir → vu.", "g", "gram"),
 q("<i>J'______ une lettre à ma grand-mère.</i> (wrote)", ["ai écrit", "ai écrivé", "suis écrit", "ai écrire"], 0, "écrire → écrit, with avoir.", "g", "gram"),
 q("<i>Ils ______ le bus.</i> (took)", ["ont pris", "sont pris", "ont prendu", "ont pri"], 0, "prendre → pris, with avoir.", "g", "gram"),
 q("Which verb takes être?", ["descendre", "vendre", "attendre", "répondre"], 0, "descendre is in DR & MRS VANDERTRAMP.", "g", "gram"),
 q("<i>Ma grand-mère ______ en 1950.</i> (was born)", ["est née", "a né", "est né", "a née"], 0, "naître → être + née.", "g", "gram"),
 q("<i>Nous ______ chez nous.</i> (went home, two boys)", ["sommes rentrés", "avons rentré", "sommes rentrées", "sommes rentré"], 0, "rentrer → être, masculine plural.", "g", "gram"),
 q("Make it negative: <i>Elle a fini.</i>", ["Elle n'a pas fini.", "Elle n'a fini pas.", "Elle a pas fini ne.", "Elle ne pas a fini."], 0, "Wrap the helper verb.", "g", "gram"),
 q("<i>Le matin, je ______ les dents.</i>", ["me brosse", "brosse", "me brosses", "se brosse"], 0, "se brosser les dents; je → me + -e.", "g", "gram"),
 q("<i>Elles ______ à dix heures hier.</i> (went to bed)", ["se sont couchées", "ont couché", "se sont couché", "se ont couchées"], 0, "Reflexive → être, feminine plural agreement.", "g", "gram"),
 q("<i>le week-end dernier</i> means…", ["last weekend", "next weekend", "every weekend", "the whole weekend"], 0, "dernier = last.", "v", "vocab"),
 q(f"{listen('Je vais partir demain.')} When is the speaker leaving?", ["Tomorrow", "Yesterday", "Today", "Next week"], 0, "vais partir = going to leave; demain = tomorrow.", "v", "listen"),
 q("Read: <i>Samedi, Paul s'est levé tard. Il a mangé un croissant, puis il est allé au parc avec ses amis. Ils ont joué au foot. Le soir, il est resté à la maison.</i> Which is true?", ["Paul played soccer with friends.", "Paul got up early.", "Paul went out in the evening.", "Paul ate a pizza."], 0, "Ils ont joué au foot.", "v", "read"),
 q("Which sentence is correct?", ["Je suis tombé et j'ai eu mal.", "J'ai tombé et je suis eu mal.", "Je suis tombé et je suis eu mal.", "J'ai tombé et j'ai eu mal."], 0, "tomber → être; avoir → avoir + eu.", "g", "gram"),
]
FRQS = [
 {"q": "Write about what you did last weekend (at least 6 sentences).",
  "parts": [{"p": "Use at least two verbs with avoir and two with être, plus sequence words (d'abord, ensuite, enfin…).",
   "rubric": [["At least two passé composé verbs with avoir, correct participles", 2], ["At least two verbs with être, with correct agreement", 2], ["Sequence or time words (hier, d'abord, ensuite, enfin…)", 1], ["One negative in the passé composé placed correctly", 1], ["Spelling and accents mostly correct", 1]],
   "answer": f'<div class="ex">{F("Le week-end dernier, je suis allée chez ma tante. D\'abord, nous avons fait une promenade au parc. Ensuite, nous avons mangé au restaurant et j\'ai pris une salade. L\'après-midi, nous sommes allées au cinéma. Je n\'ai pas aimé le film ! Enfin, je suis rentrée à dix heures et je me suis couchée.")}<span class="en">Last weekend I went to my aunt\'s. First we went for a walk in the park. Then we ate at a restaurant and I had a salad. In the afternoon we went to the movies. I didn\'t like the movie! Finally I got home at ten and went to bed. (Written by a girl: allée, rentrée, couchée.)</span></div>'}]},
 {"q": "Describe your weekday routine and then your plans for tomorrow (at least 5 sentences).",
  "parts": [{"p": "Use at least three reflexive verbs in the present and two sentences in the futur proche.",
   "rubric": [["Three reflexive verbs with the pronoun matching the subject", 2], ["Times told correctly", 1], ["Two futur proche sentences (aller + infinitive)", 2], ["Reflexive pronoun correct in the futur proche (je vais me…)", 1]],
   "answer": f'<div class="ex">{F("D\'habitude, je me réveille à six heures et demie. Je me douche et je m\'habille. Je me couche à dix heures. Demain, je vais me lever tard parce que c\'est samedi. Je vais jouer au foot avec mes amis.")}<span class="en">Usually I wake up at 6:30. I shower and get dressed. I go to bed at ten. Tomorrow I\'m going to get up late because it\'s Saturday. I\'m going to play soccer with my friends.</span></div>'}]},
]

if __name__ == "__main__":
    build(5, "unit-5", "Past and future", 'Hier <span class="hl">et demain</span>',
          "The futur proche, the passé composé with avoir and être, reflexive verbs and your daily routine, and telling a story in order. Tap any French word to hear it.",
          "French 1 Unit 5: futur proche, passé composé and reflexive verbs, with audio, interactive labs, practice questions and a practice exam.",
          CH, PQ, CHAL, EXQ, FRQS, "/home/claude/ap-physics-study/courses/french-1/unit-5.html")
