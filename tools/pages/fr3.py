from fr_common import *

CH = []
CORE = f'''<p>Now you start talking about <b>what people do</b>. French verbs change their ending for each subject, but most of them follow one of three patterns. Learn the pattern once and you can use hundreds of verbs.</p>
{wa("Stem + ending", [
 ("s|je|s  a|parl|v  b|er|e", "Start with the infinitive parler (to speak). Take off -er: the stem is parl-.", "to speak"),
 ("s|je|s  a|parl|v  b|e|e", "Add the ending for je: -e. Je parle.", "I speak"),
 ("s|nous|s  a|parl|v  b|ons|e", "For nous the ending is -ons: nous parlons.", "we speak"),
 ("s|vous|s  a|parl|v  b|ez|e", "For vous it's -ez: vous parlez.", "you speak")])}
<div class="grid2"><div class="mini"><h4>In this unit</h4><p>-er verbs · saying what you like to do · negation (ne … pas) · three ways to ask a question · question words · -ir and -re verbs · aller, faire, prendre, vouloir, pouvoir, devoir.</p></div>
<div class="mini"><h4>One present tense</h4><p>French has one present tense for three English ones: <i>je parle</i> = I speak, I'm speaking, I do speak.</p></div></div>'''
CH.append(chapter("overview-f3", "Overview", "Overview", [topic("core-f3", "Au présent", CORE)]))

# ------------------------------------------------------------------ -er verbs
ER = topic("er-verbs", "Regular -er verbs", f'''
<p>About 90% of French verbs end in <b>-er</b>, and almost all of them follow this pattern.</p>
<div class="tblwrap"><table class="conj"><tr><td>{F("je parle")}</td><td>-e</td><td>{F("nous parlons")}</td><td>-ons</td></tr>
<tr><td>{F("tu parles")}</td><td>-es</td><td>{F("vous parlez")}</td><td>-ez</td></tr>
<tr><td>{F("il / elle parle")}</td><td>-e</td><td>{F("ils / elles parlent")}</td><td>-ent (silent!)</td></tr></table></div>
<p>Four of the six forms sound exactly the same: {F("parle, parles, parle, parlent")}. Only the nous and vous forms sound different.</p>
{lab(type="conj", verbs=["parler", "aimer", "habiter", "jouer", "regarder", "manger"], tenses=["pres"])}
<h3>Useful -er verbs</h3>
{vgrid([("parler", "to speak"), ("aimer", "to like, love"), ("adorer", "to love"), ("détester", "to hate"), ("habiter", "to live"), ("travailler", "to work"), ("étudier", "to study"), ("écouter", "to listen to"), ("regarder", "to watch"), ("jouer", "to play"), ("chanter", "to sing"), ("danser", "to dance"), ("nager", "to swim"), ("manger", "to eat"), ("téléphoner (à)", "to call"), ("chercher", "to look for"), ("visiter", "to visit (a place)"), ("arriver", "to arrive")])}
{box("trap", "Spelling changes", f"Verbs in -ger and -cer keep their soft sound before -ons: {F('nous mangeons')}, {F('nous commençons')}. A few verbs change their accent: {F('j\'achète')} (acheter), {F('je préfère')} (préférer), {F('je m\'appelle')} (two l's), but nous achetons, nous préférons.")}
''', pill=("g", "3.1"), sub="One pattern for hundreds of verbs.",
 det=("Why -ent is silent", '''<h4>Spelling vs sound</h4><p>The -ent ending of ils / elles is never pronounced on a verb. <i>Ils parlent</i> sounds like <i>il parle</i>. You can still hear the plural with a liaison: <i>ils‿aiment</i> (il-zem) vs <i>il aime</i>.</p>
<h4>Don't translate "do" and "am"</h4><p>"Do you speak French?" is <i>Tu parles français ?</i> "I'm watching TV" is <i>Je regarde la télé</i>. No extra word for do or am.</p>
<h4>Verbs with built-in prepositions</h4><p><i>écouter</i> = to listen <b>to</b>, <i>regarder</i> = to look <b>at</b>, <i>chercher</i> = to look <b>for</b>: <i>J'écoute la radio.</i> But <i>téléphoner à</i> needs à: <i>Je téléphone à ma mère.</i></p>'''))

LIKE = topic("likes", "Saying what you like to do", f'''
<p>Put an <b>infinitive</b> right after {F("aimer")}, {F("adorer")}, {F("préférer")} or {F("détester")}.</p>
{ex("J'aime nager.", "I like to swim / I like swimming.")}
{ex("Nous adorons danser.", "We love dancing.")}
{ex("Tu préfères lire ou regarder un film ?", "Do you prefer reading or watching a movie?")}
<p>With a noun, use the definite article: {F("J'aime le foot.")} {F("Je déteste les maths.")}</p>
<h3>Jouer à and jouer de</h3>
<p>{F("jouer à")} + a sport or game; {F("jouer de")} + an instrument. Remember the contractions: à + le = <b>au</b>, de + le = <b>du</b>.</p>
{ex("Je joue au foot et au basket.", "I play soccer and basketball.")}
{ex("Elle joue du piano et de la guitare.", "She plays the piano and the guitar.")}
{vgrid([("le foot(ball)", "soccer"), ("le basket", "basketball"), ("le tennis", "tennis"), ("les jeux vidéo", "video games"), ("les cartes", "cards"), ("le piano", "piano"), ("la guitare", "guitar"), ("la batterie", "drums")])}
''', pill=("v", "3.2"), sub="aimer + infinitive, and jouer à / de.")
CH.append(chapter("er-f3", "Les verbes en -er", "-er verbs", [ER, LIKE]))

# ------------------------------------------------------------------ negation
NEGT = topic("negation", "Ne … pas: making a sentence negative", f'''
<p>Put {F("ne")} before the conjugated verb and {F("pas")} after it. Ne becomes <b>n'</b> before a vowel.</p>
{wa("Wrapping the verb", [
 ("s|Je|s  v|parle|v  r|espagnol.|x", "Start with a positive sentence.", "I speak Spanish."),
 ("s|Je|s  n1|ne|n  v|parle|v  n2|pas|n  r|espagnol.|x", "ne goes before the verb, pas right after it.", "I don't speak Spanish."),
 ("s2|Elle|s  v2|aime|v  r2|le foot.|x", "Now a verb starting with a vowel.", "She likes soccer."),
 ("s2|Elle|s  n1|n'|n  v2|aime|v  n2|pas|n  r2|le foot.|x", "ne + aime → n'aime. The definite article le stays.", "She doesn't like soccer.")])}
<h3>Un, une, des become de</h3>
<p>After a negative, the indefinite articles <b>un, une, des</b> (and du / de la, Unit 4) become <b>de</b> (d' before a vowel). <b>le, la, les</b> don't change.</p>
{ex("J'ai un frère. → Je n'ai pas de frère.", "I have a brother. → I don't have a brother.")}
{ex("Il y a des élèves. → Il n'y a pas d'élèves.", "There are students. → There are no students.")}
{ex("J'aime les maths. → Je n'aime pas les maths.", "le / la / les stay.")}
<h3>Other negatives</h3>
{vt([("ne … jamais", "never", "Je ne mange jamais de viande."), ("ne … plus", "no longer, not anymore", "Il n'habite plus ici."), ("ne … rien", "nothing", "Je ne fais rien."), ("ne … personne", "nobody", "Je ne vois personne.")], head=("French", "English", "Example"))}
{lab(type="neg")}
{box("plain", "In conversation", "People often drop the ne when speaking casually: <i>Je sais pas</i> (I dunno). Always write it, and always use it on tests.")}
''', pill=("g", "3.3"), sub="ne … pas, and the de rule.",
 det=("Negation in detail", '''<h4>Where exactly do ne and pas go?</h4><p>Around the <b>conjugated</b> verb only. With two verbs, they wrap the first: <i>Je n'aime pas nager.</i> In the passé composé (Unit 5) they wrap the helper verb: <i>Je n'ai pas mangé.</i></p>
<h4>Why de?</h4><p>"I don't have <i>a</i> brother" really means "I have zero brothers", so the article of quantity becomes de, the "zero" form. Exception: after <i>être</i> the article stays: <i>Ce n'est pas un chat.</i></p>
<h4>Answering a negative question</h4><p>To say "yes" to a negative question, use <b>si</b>: — Tu n'aimes pas le chocolat ? — Si ! (Yes I do!)</p>'''))
CH.append(chapter("neg-f3", "Ne … pas: Negation", "Negation", [NEGT]))

# ------------------------------------------------------------------ questions
QU = topic("questions", "Three ways to ask a yes / no question", f'''
<div class="tblwrap"><table><tr><th>How</th><th>Example</th><th>Style</th></tr>
<tr><td>1. Raise your voice at the end</td><td>{F("Tu parles français ?")}</td><td>everyday speech</td></tr>
<tr><td>2. Start with est-ce que</td><td>{F("Est-ce que tu parles français ?")}</td><td>always correct, speech or writing</td></tr>
<tr><td>3. Swap subject and verb (inversion)</td><td>{F("Parles-tu français ?")}</td><td>formal, written</td></tr></table></div>
{wa("Inversion step by step", [
 ("s|Il|s  v|parle|v  r|français.|x", "A statement.", "He speaks French."),
 ("v|Parle|v  s|il|s  r|français ?|x", "Swap the verb and the subject…", ""),
 ("v|Parle|v  t|-t-|n  s|il|s  r|français ?|x", "…and join them with a hyphen. If the verb ends in a vowel and the subject is il / elle / on, add -t- so you can say it.", "Does he speak French?"),
 ("v2|A|v  t|-t-|n  s2|elle|s  r2|un chien ?|x", "Same with a: A-t-elle un chien ?", "Does she have a dog?")])}
{ex("Est-ce qu'il aime le sport ?", "Does he like sports? (que → qu' before a vowel)")}
{ex("Aimez-vous le cinéma ?", "Do you like the movies?")}
''', pill=("g", "3.4"), sub="Intonation, est-ce que and inversion.")

QW = topic("question-words", "Question words", f'''
{vt([("Qui ?", "Who?", "Qui est-ce ?"), ("Que ? / Qu'est-ce que ?", "What?", "Qu'est-ce que tu fais ?"), ("Quoi ?", "What? (alone or at the end)", "Tu fais quoi ?"), ("Où ?", "Where?", "Où est-ce que tu habites ?"), ("Quand ?", "When?", "Quand est-ce qu'on mange ?"), ("Comment ?", "How?", "Comment vas-tu ?"), ("Pourquoi ?", "Why?", "Pourquoi tu ris ?"), ("Parce que", "Because", "Parce que c'est drôle !"), ("Combien (de) ?", "How much / how many?", "Combien de frères as-tu ?"), ("Quel / Quelle ?", "Which / What?", "Quelle heure est-il ?")], head=("French", "English", "Example"))}
<p>The easiest pattern: <b>question word + est-ce que + statement</b>. {F("Où est-ce que tu travailles ?")} (Where do you work?)</p>
<h3>Quel agrees</h3>
<p>{F("quel")} (which / what) agrees with the noun: {F("quel livre")}, {F("quelle heure")}, {F("quels films")}, {F("quelles chansons")}. All four sound the same.</p>
{box("trap", "Common mistake", "Où (where) has an accent; ou (or) doesn't. And don't confuse <i>qu'est-ce que</i> (what?) with <i>est-ce que</i> (turns a statement into a yes / no question).")}
''', pill=("v", "3.5"), sub="Who, what, where, when, why, how.")
CH.append(chapter("questions-f3", "Les questions", "Questions", [QU, QW]))

# ------------------------------------------------------------------ -ir, -re, irregular
IRRE = topic("ir-re", "Regular -ir and -re verbs", f'''
<div class="grid2"><div class="mini"><h4>-ir: finir (to finish)</h4><p>{F("je finis, tu finis, il finit")}<br>{F("nous finissons, vous finissez, ils finissent")}<br>Notice the <b>-iss-</b> in the plural.</p></div>
<div class="mini"><h4>-re: vendre (to sell)</h4><p>{F("je vends, tu vends, il vend")}<br>{F("nous vendons, vous vendez, ils vendent")}<br>No ending at all for il / elle.</p></div></div>
{lab(type="conj", verbs=["finir", "choisir", "vendre", "attendre"], tenses=["pres"])}
{vgrid([("finir", "to finish"), ("choisir", "to choose"), ("réussir (à)", "to succeed, pass"), ("grandir", "to grow up"), ("rougir", "to blush"), ("vendre", "to sell"), ("attendre", "to wait for"), ("entendre", "to hear"), ("répondre (à)", "to answer"), ("perdre", "to lose")])}
{ex("Nous finissons nos devoirs à huit heures.", "We finish our homework at eight.")}
{ex("Tu attends le bus ?", "Are you waiting for the bus?")}
''', pill=("g", "3.6"), sub="The other two patterns.")

IRR = topic("irregular", "Key irregular verbs", f'''
<p>The verbs used most are irregular. Learn these six by heart; the lab lets you check any of them.</p>
<div class="tblwrap"><table><tr><th></th><th>aller (go)</th><th>faire (do, make)</th><th>prendre (take)</th><th>vouloir (want)</th><th>pouvoir (can)</th><th>devoir (must)</th></tr>
<tr><td>je</td><td>vais</td><td>fais</td><td>prends</td><td>veux</td><td>peux</td><td>dois</td></tr>
<tr><td>tu</td><td>vas</td><td>fais</td><td>prends</td><td>veux</td><td>peux</td><td>dois</td></tr>
<tr><td>il / elle</td><td>va</td><td>fait</td><td>prend</td><td>veut</td><td>peut</td><td>doit</td></tr>
<tr><td>nous</td><td>allons</td><td>faisons</td><td>prenons</td><td>voulons</td><td>pouvons</td><td>devons</td></tr>
<tr><td>vous</td><td>allez</td><td>faites</td><td>prenez</td><td>voulez</td><td>pouvez</td><td>devez</td></tr>
<tr><td>ils / elles</td><td>vont</td><td>font</td><td>prennent</td><td>veulent</td><td>peuvent</td><td>doivent</td></tr></table></div>
{lab(type="conj", verbs=["aller", "faire", "prendre", "vouloir", "pouvoir", "devoir", "venir", "voir", "boire", "lire", "écrire", "dormir", "sortir", "partir", "mettre"], tenses=["pres"])}
<h3>Using them</h3>
{ex("Je vais au lycée en bus.", "I go to high school by bus.")}
{ex("Qu'est-ce que tu fais ce week-end ?", "What are you doing this weekend?")}
{ex("Je veux manger une pizza, mais je dois étudier.", "I want to eat a pizza, but I have to study. (vouloir / pouvoir / devoir + infinitive)")}
{ex("Tu peux m'aider ?", "Can you help me?")}
<h3>Expressions with faire</h3>
{vgrid([("faire du sport", "to play sports"), ("faire du vélo", "to ride a bike"), ("faire une promenade", "to go for a walk"), ("faire les devoirs", "to do homework"), ("faire la cuisine", "to cook"), ("faire les courses", "to go grocery shopping"), ("faire la fête", "to party")])}
''', pill=("g", "3.7"), sub="aller, faire, prendre, vouloir, pouvoir, devoir.",
 det=("Patterns inside the irregulars", '''<h4>Same endings, odd stems</h4><p>Most irregular verbs still end in -s, -s, -t in the singular (je veux, tu veux, il veut) and -ons, -ez, -ent in the plural. What changes is the stem.</p>
<h4>Three special vous forms</h4><p>Only three verbs don't end in -ez for vous: <i>vous êtes</i>, <i>vous faites</i>, <i>vous dites</i> (dire, to say).</p>
<h4>Verbs like prendre</h4><p><i>apprendre</i> (to learn) and <i>comprendre</i> (to understand) work exactly like prendre: <i>je comprends, nous comprenons, ils comprennent</i>.</p>'''))
CH.append(chapter("irr-f3", "-ir, -re et irréguliers", "More verbs", [IRRE, IRR]))

REV = topic("review-f3", "Unit 3 summary", f'''<div class="grid2"><div class="mini"><h4>-er verbs</h4><p>stem + e, es, e, ons, ez, ent. aimer + infinitive. jouer au foot, jouer du piano.</p></div>
<div class="mini"><h4>Negation</h4><p>ne + verb + pas. n' before a vowel. un / une / des → de after a negative. ne … jamais / plus / rien.</p></div>
<div class="mini"><h4>Questions</h4><p>Intonation, est-ce que, inversion (Parle-t-il ?). qui, que, où, quand, comment, pourquoi, combien, quel.</p></div>
<div class="mini"><h4>Other verbs</h4><p>finir (-iss- in the plural), vendre (no il ending). aller, faire, prendre, vouloir, pouvoir, devoir.</p></div></div>''', sub="Everything from this unit on one screen.")
MIS = topic("mistakes-f3", "Common mistakes", '''<ol class="steps">
<li>Pronouncing the -ent of ils parlent. It's silent.</li>
<li>Adding a word for do / am: <i>Je suis regarde</i> → <i>Je regarde</i>.</li>
<li>Forgetting to change the article: <i>Je n'ai pas un chien</i> → <i>Je n'ai pas de chien</i>.</li>
<li>Putting pas in the wrong place with two verbs: <i>Je n'aime nager pas</i> → <i>Je n'aime pas nager</i>.</li>
<li>Forgetting -t- in inversion: <i>Parle il ?</i> → <i>Parle-t-il ?</i></li>
<li>nous mangons → <i>nous mangeons</i>; vous faisez → <i>vous faites</i>.</li>
<li>jouer à for instruments: <i>Je joue au piano</i> → <i>Je joue du piano</i>.</li></ol>''', sub="Points students lose most often.")
CH.append(chapter("review-ch-f3", "Review", "Review", [REV, MIS]))

PQ = [
 q("<i>Nous ______ français.</i> (parler)", ["parlons", "parlez", "parlent", "parle"], 0, "nous → -ons.", "g"),
 q("<i>Ils ______ la télé.</i> (regarder)", ["regardent", "regardons", "regardez", "regards"], 0, "ils → -ent.", "g"),
 q("<i>Tu ______ à Chicago ?</i> (habiter)", ["habites", "habite", "habitez", "habitent"], 0, "tu → -es.", "g"),
 q("<i>Nous ______ une pizza.</i> (manger)", ["mangeons", "mangons", "mangez", "mangent"], 0, "-ger verbs keep the e before -ons.", "g"),
 q("How do you say <i>I like to dance</i>?", ["J'aime danser.", "J'aime danse.", "Je aime danser.", "J'aime à danser."], 0, "aimer + infinitive, and je → j'.", "g"),
 q("<i>Elle joue ______ violon.</i>", ["du", "au", "de", "le"], 0, "jouer de + instrument; de + le = du.", "g"),
 q("<i>Ils jouent ______ tennis.</i>", ["au", "du", "à", "le"], 0, "jouer à + sport; à + le = au.", "g"),
 q("Make it negative: <i>Je travaille.</i>", ["Je ne travaille pas.", "Je ne pas travaille.", "Je travaille ne pas.", "Ne je travaille pas."], 0, "ne before the verb, pas after.", "g"),
 q("Make it negative: <i>J'ai une voiture.</i>", ["Je n'ai pas de voiture.", "Je n'ai pas une voiture.", "Je ne ai pas de voiture.", "Je n'ai pas la voiture."], 0, "ne → n' before ai, and une → de after a negative.", "g"),
 q("Make it negative: <i>Il aime les épinards.</i>", ["Il n'aime pas les épinards.", "Il n'aime pas d'épinards.", "Il ne aime pas les épinards.", "Il n'aime pas de épinards."], 0, "le / la / les stay after a negative.", "g"),
 q("<i>Je ne mange jamais de viande</i> means…", ["I never eat meat.", "I don't eat meat anymore.", "I eat nothing.", "I always eat meat."], 0, "ne … jamais = never.", "v"),
 q("Which is <b>not</b> a correct question?", ["Parle il anglais ?", "Il parle anglais ?", "Est-ce qu'il parle anglais ?", "Parle-t-il anglais ?"], 0, "Inversion needs a hyphen and -t- here: Parle-t-il ?", "g"),
 q("<i>______ tu habites ? — J'habite à Lyon.</i>", ["Où", "Quand", "Qui", "Comment"], 0, "The answer is a place → où.", "v"),
 q("<i>______ frères as-tu ? — Deux.</i>", ["Combien de", "Comment", "Quel", "Pourquoi"], 0, "How many → combien de.", "v"),
 q("<i>______ heure est-il ?</i>", ["Quelle", "Quel", "Quels", "Qu'est-ce que"], 0, "heure is feminine → quelle.", "g"),
 q("<i>Pourquoi tu ris ? — ______ c'est drôle !</i>", ["Parce que", "Pourquoi", "Quand", "Comme"], 0, "parce que = because.", "v"),
 q("<i>Nous ______ nos devoirs.</i> (finir)", ["finissons", "finons", "finissez", "finisons"], 0, "-ir verbs add -iss- in the plural: finissons.", "g"),
 q("<i>Elle ______ sa voiture.</i> (vendre)", ["vend", "vendt", "vende", "vends"], 0, "-re verbs: il / elle has no ending: vend.", "g"),
 q("<i>Je ______ au cinéma ce soir.</i> (aller)", ["vais", "va", "vas", "allons"], 0, "je vais.", "g"),
 q("<i>Vous ______ du sport ?</i> (faire)", ["faites", "faisez", "font", "faisons"], 0, "vous faites is irregular.", "g"),
 q("<i>Ils ______ le bus.</i> (prendre)", ["prennent", "prendent", "prenent", "prenons"], 0, "ils prennent (double n).", "g"),
 q("<i>Je ______ sortir, mais je ______ étudier.</i>", ["veux … dois", "veut … doit", "voulons … devons", "veux … doit"], 0, "je veux, je dois.", "g"),
 q("<i>faire les courses</i> means…", ["to go grocery shopping", "to run a race", "to take classes", "to cook"], 0, "faire les courses = grocery shopping.", "v"),
 q(f"{listen('Ils aiment chanter.')} How many people like to sing?", ["More than one", "One", "Nobody", "You can't tell"], 0, "The liaison in ils‿aiment (z sound) tells you it's plural.", "v"),
]
CHAL = [
 q("Make it negative: <i>Nous avons des devoirs ce soir.</i>", ["Nous n'avons pas de devoirs ce soir.", "Nous n'avons pas des devoirs ce soir.", "Nous ne avons pas de devoirs ce soir.", "Nous n'avons de devoirs pas ce soir."], 0, "n' before avons, and des → de.", "g"),
 q("Make it negative: <i>Elle aime nager.</i>", ["Elle n'aime pas nager.", "Elle aime ne pas nager.", "Elle n'aime nager pas.", "Elle ne aime pas nager."], 0, "Wrap the conjugated verb (aime), not the infinitive.", "g"),
 q("Which inversion is correct?", ["Va-t-elle à la plage ?", "Va-elle à la plage ?", "Vat-elle à la plage ?", "Elle-va à la plage ?"], 0, "va ends in a vowel, so -t- goes between va and elle.", "g"),
 q("<i>— Tu n'aimes pas le fromage ? — ______ ! J'adore ça.</i>", ["Si", "Oui", "Non", "Pas"], 0, "si = yes in answer to a negative question.", "v"),
 q("Which sentence is correct?", ["Nous commençons à huit heures.", "Nous commencons à huit heures.", "Nous commençon à huit heures.", "Nous commence à huit heures."], 0, "-cer verbs take ç before -ons.", "g"),
 q("<i>Qu'est-ce que vous ______ ce soir ?</i>", ["faites", "faisez", "fait", "font"], 0, "vous faites: one of three irregular vous forms.", "g"),
 q("Which sentence means <i>He doesn't live here anymore</i>?", ["Il n'habite plus ici.", "Il n'habite jamais ici.", "Il n'habite rien ici.", "Il habite ne plus ici."], 0, "ne … plus = no longer.", "v"),
 q("<i>Mes amis ______ comprendre l'espagnol.</i> (they can)", ["peuvent", "peut", "pouvent", "peuent"], 0, "ils peuvent.", "g"),
]
EXQ = [
 q("<i>Vous ______ quelle langue ?</i> (parler)", ["parlez", "parlons", "parles", "parlent"], 0, "vous → -ez.", "g", "gram"),
 q("<i>J'______ la musique classique.</i> (écouter)", ["écoute", "écoutes", "écoutons", "écouter"], 0, "j'écoute.", "g", "gram"),
 q("<i>Nous ______ en avance.</i> (arriver)", ["arrivons", "arrivez", "arrivent", "arrive"], 0, "nous → -ons.", "g", "gram"),
 q("Make it negative: <i>Il y a du lait.</i>", ["Il n'y a pas de lait.", "Il n'y a pas du lait.", "Il ne y a pas de lait.", "Il y n'a pas de lait."], 0, "n'y a pas, and du → de.", "g", "gram"),
 q("<i>Je ne fais rien</i> means…", ["I'm doing nothing.", "I never do it.", "I'm not doing it anymore.", "I'm doing everything."], 0, "ne … rien = nothing.", "v", "vocab"),
 q("Choose the correct question.", ["Est-ce que tu as un chien ?", "Est-ce tu as un chien ?", "Est-ce que as-tu un chien ?", "Que est-ce tu as un chien ?"], 0, "est-ce que + normal statement order.", "g", "gram"),
 q("<i>— ______ est-ce ? — C'est mon prof de maths.</i>", ["Qui", "Que", "Où", "Quoi"], 0, "The answer is a person → qui.", "v", "vocab"),
 q("<i>— ______ arrives-tu ? — Demain.</i>", ["Quand", "Où", "Comment", "Combien"], 0, "The answer is a time → quand.", "v", "vocab"),
 q("<i>Ils ______ leurs devoirs.</i> (finir)", ["finissent", "finent", "finisent", "finit"], 0, "ils finissent.", "g", "gram"),
 q("<i>Tu ______ le train ?</i> (attendre)", ["attends", "attend", "attendes", "attendez"], 0, "tu attends.", "g", "gram"),
 q("<i>Elles ______ au parc.</i> (aller)", ["vont", "vais", "allent", "vas"], 0, "elles vont.", "g", "gram"),
 q("<i>On ______ une promenade ?</i> (faire)", ["fait", "fais", "faisons", "font"], 0, "on takes the il form: fait.", "g", "gram"),
 q(f"{listen('Je ne peux pas sortir ce soir.')} The speaker…", ["can't go out tonight", "wants to go out tonight", "must go out tonight", "goes out every night"], 0, "ne peux pas = can't, sortir = go out.", "v", "listen"),
 q("Read: <i>Léo adore le sport. Il joue au foot le samedi et il fait du vélo le dimanche. Mais il ne joue pas d'instrument.</i> Which is true?", ["Léo rides a bike on Sundays.", "Léo plays the piano.", "Léo plays soccer on Sundays.", "Léo doesn't like sports."], 0, "il fait du vélo le dimanche.", "v", "read"),
 q("Which sentence is correct?", ["Elle joue de la guitare.", "Elle joue à la guitare.", "Elle joue la guitare.", "Elle joue du guitare."], 0, "jouer de + instrument; guitare is feminine → de la.", "g", "gram"),
]
FRQS = [
 {"q": "Write an email to a French friend about your typical week (at least 5 sentences).",
  "parts": [{"p": "Say what you do, what you like and don't like to do, and ask your friend two questions.",
   "rubric": [["At least three different verbs correctly conjugated in the present", 2], ["aimer / adorer / détester + infinitive", 1], ["One correct negative sentence (with de if needed)", 1], ["Two questions, correctly formed (est-ce que, inversion or intonation)", 1], ["Spelling and accents mostly correct", 1]],
   "answer": f'<div class="ex">{F("Salut Lucas ! Le lundi, je vais au lycée en bus. Après l\'école, je joue au basket avec mes amis. J\'adore regarder des films, mais je n\'aime pas faire les devoirs ! Le week-end, je ne travaille pas. Et toi, qu\'est-ce que tu fais le samedi ? Est-ce que tu fais du sport ?")}<span class="en">Hi Lucas! On Mondays I go to school by bus. After school I play basketball with my friends. I love watching movies, but I don\'t like doing homework! On weekends I don\'t work. And you, what do you do on Saturdays? Do you play sports?</span></div>'}]},
 {"q": "Answer each question in a full sentence, the first two in the negative.",
  "parts": [{"p": "1. Tu as un chat ?  2. Tu aimes le café ?  3. Qu'est-ce que tu fais ce soir ?",
   "rubric": [["1. Non, je n'ai pas de chat (de, not un)", 1], ["2. Non, je n'aime pas le café (le stays)", 1], ["3. A full sentence with a correctly conjugated verb (Ce soir, je…)", 1], ["Correct n' / ne placement", 1]],
   "answer": f'<div class="ex">{F("Non, je n\'ai pas de chat.")}<span class="en">No, I don\'t have a cat.</span></div><div class="ex">{F("Non, je n\'aime pas le café.")}<span class="en">No, I don\'t like coffee.</span></div><div class="ex">{F("Ce soir, je regarde un film avec ma sœur.")}<span class="en">Tonight I\'m watching a movie with my sister.</span></div>'}]},
]

if __name__ == "__main__":
    build(3, "unit-3", "Verbs in the present", 'Au <span class="hl">présent</span>',
          "Regular -er, -ir and -re verbs, saying what you like to do, negation, asking questions, and the irregular verbs you'll use every day. Tap any French word to hear it.",
          "French 1 Unit 3: present-tense verbs, negation and questions, with audio, interactive labs, practice questions and a practice exam.",
          CH, PQ, CHAL, EXQ, FRQS, "/home/claude/ap-physics-study/courses/french-1/unit-3.html")
