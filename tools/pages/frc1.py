from fr_common import *

TL = [
 {"parts": [["Il pleuvait", "i"], [" quand ", ""], ["je suis sorti", "p"], [".", ""]], "en": "It was raining when I went out.",
  "why": "<div>The rain is the <b>background</b>, already going on: imparfait. Going out is the <b>event</b> that happened at one moment: passé composé.</div>"},
 {"parts": [["Je lisais", "i"], [" quand ", ""], ["le téléphone a sonné", "p"], [".", ""]], "en": "I was reading when the phone rang.",
  "why": "<div>An action in progress (<i>was reading</i>) is interrupted by an event (<i>rang</i>). English \"was …-ing\" is almost always imparfait.</div>"},
 {"parts": [["Elle s'est levée", "p"], [", ", ""], ["a pris", "p"], [" un café et ", ""], ["est partie", "p"], [".", ""]], "en": "She got up, had a coffee and left.",
  "why": "<div>A <b>chain of completed events</b>, one after another: all passé composé. Each one moves the story forward.</div>"},
 {"parts": [["Quand j'étais petit", "i"], [", ", ""], ["j'allais", "i"], [" à la plage tous les étés.", ""]], "en": "When I was little, I used to go to the beach every summer.",
  "why": "<div><b>Description</b> (age, being little) and a <b>habit</b> (used to, every summer): both imparfait. Words like <i>tous les étés, d'habitude, souvent</i> point to the imparfait.</div>"},
 {"parts": [["Il faisait beau", "i"], [", ", ""], ["les enfants jouaient", "i"], [" et soudain, ", ""], ["un chien est arrivé", "p"], [".", ""]], "en": "The weather was nice, the children were playing, and suddenly a dog showed up.",
  "why": "<div>Two background descriptions set the scene (imparfait), then <i>soudain</i> (suddenly) signals the event (passé composé).</div>"},
 {"parts": [["J'ai habité", "p"], [" à Lyon pendant trois ans.", ""]], "en": "I lived in Lyon for three years.",
  "why": "<div>Even a long action is passé composé when it has a <b>clear start and end</b> (<i>pendant trois ans</i>) and is seen as finished. Duration alone doesn't make it imparfait.</div>"},
]

CH = []
CORE = f'''<p>Welcome to <b>College French</b>. This level assumes you know the basics (present tense, passé composé, futur proche, articles and adjectives) and takes you to where a second- or third-semester university course ends. Explanations get more precise, examples get longer, and the exams expect real accuracy.</p>
<div class="tblwrap"><table><tr><th>Unit</th><th>Main goals</th></tr>
<tr><td>1. Le passé</td><td>choose between passé composé and imparfait; use the plus-que-parfait</td></tr>
<tr><td>2. Les pronoms</td><td>y, en, lui / leur, double pronouns, relative pronouns qui / que / où / dont / lequel</td></tr>
<tr><td>3. Futur et conditionnel</td><td>futur simple, conditionnel, the three types of si clauses</td></tr>
<tr><td>4. Le subjonctif</td><td>form it, know when it's required, and when it's wrong</td></tr>
<tr><td>5. Le style</td><td>passive voice, gérondif, reported speech, passé simple, connectors for essays</td></tr></table></div>
{wa("Two past tenses, two jobs", [
 ("a|Il|s  b|faisait|v  c|nuit.|x", "Imparfait: the setting. What things were like.", "It was dark."),
 ("a|Il|s  b|faisait|v  c|nuit|x  d|quand|gl  e|on|s  f|a frappé|n  g|à la porte.|x", "Passé composé: what happened. The event that moves the story.", "It was dark when someone knocked at the door."),
 ("a|Il|s  b|faisait|v  c|nuit|x  d|quand|gl  e|on|s  f|a frappé|n  g|à la porte.|x  h|J'avais oublié|e  i|de fermer à clé.|x", "Plus-que-parfait: something that had happened even earlier.", "It was dark when someone knocked. I had forgotten to lock it.")])}'''
CH.append(chapter("overview-c1", "Overview", "Overview", [topic("core-c1", "College French: Le passé", CORE)]))

IMPF = topic("imparfait", "Forming the imparfait", f'''
<p>Take the <b>nous</b> form of the present, drop <b>-ons</b>, add the endings. This works for every verb except être.</p>
<div class="tblwrap"><table><tr><th>nous (present)</th><th>stem</th><th>imparfait</th></tr>
<tr><td>{F("nous parlons")}</td><td>parl-</td><td>{F("je parlais")}</td></tr>
<tr><td>{F("nous finissons")}</td><td>finiss-</td><td>{F("je finissais")}</td></tr>
<tr><td>{F("nous faisons")}</td><td>fais-</td><td>{F("je faisais")}</td></tr>
<tr><td>{F("nous prenons")}</td><td>pren-</td><td>{F("je prenais")}</td></tr>
<tr><td>{F("nous sommes")}</td><td>ét- (exception)</td><td>{F("j'étais")}</td></tr></table></div>
<p>Endings: <b>-ais, -ais, -ait, -ions, -iez, -aient</b>. Four of the six sound the same ("-è").</p>
{lab(type="conj", verbs=["parler", "finir", "attendre", "être", "avoir", "faire", "aller", "prendre", "manger", "étudier", "se lever", "voir", "boire"], tenses=["impf", "pres"])}
{box("trap", "Spelling", f"-ger verbs keep the e before a: {F('je mangeais')} but {F('nous mangions')}. -cer verbs use ç before a: {F('je commençais')}. Verbs in -ier get a double i in nous / vous: {F('nous étudiions')}.")}
''', pill=("g", "C1.1"), sub="One rule, one exception.")

USES = topic("pc-vs-imparfait", "Passé composé or imparfait?", f'''
<div class="grid2"><div class="mini"><h4>Imparfait: the background</h4><p>Descriptions (weather, time, age, appearance, feelings) · actions in progress (<i>was doing</i>) · habits (<i>used to, would</i>) · states of mind.</p></div>
<div class="mini"><h4>Passé composé: the events</h4><p>Completed actions · a series of events · something that interrupts · actions with a set length or number of times (<i>three times, for two hours</i>) · sudden changes.</p></div></div>
{lab(type="tl", items=TL)}
<h3>Signal words</h3>
{vt([("d'habitude, souvent, tous les jours, chaque été, autrefois, le lundi", "usually, often, every day, every summer, in the past, on Mondays", "→ imparfait (habit)"), ("pendant que", "while", "→ imparfait (in progress)"), ("soudain, tout à coup, un jour, une fois, ce jour-là", "suddenly, all of a sudden, one day, once, that day", "→ passé composé (event)"), ("hier, l'année dernière, en 2019", "yesterday, last year, in 2019", "→ usually passé composé, but descriptions still use the imparfait")], head=("Words", "Meaning", "Usually"))}
<h3>Verbs that change meaning</h3>
<p>Some verbs mean something slightly different in each tense:</p>
{vt([("je savais / j'ai su", "I knew / I found out"), ("je connaissais / j'ai connu", "I knew (someone) / I met (for the first time)"), ("je voulais / j'ai voulu", "I wanted / I tried to, decided to"), ("je pouvais / j'ai pu", "I could, was able / I managed to"), ("j'avais / j'ai eu", "I had / I got, received")])}
''', pill=("g", "C1.2"), sub="Background vs events.",
 det=("Telling a story in the past", '''<h4>The film camera test</h4><p>Imagine filming the scene. Anything you'd show as the <i>set</i> or the ongoing <i>action in the background</i> is imparfait. Anything that would be a <i>cut</i> to something new happening is passé composé.</p>
<h4>Feelings and thoughts</h4><p>States of mind are usually imparfait (<i>j'étais content, je pensais que…</i>), but a sudden reaction is passé composé: <i>J'ai eu peur</i> (I got scared).</p>
<h4>The same verb, both tenses</h4><p><i>Il était malade</i> describes the state; <i>il a été malade pendant une semaine</i> sums up a finished period.</p>
<h4>Venir de in the past</h4><p><i>Je venais de partir quand il est arrivé</i> = I had just left when he arrived (venir de in the imparfait).</p>'''))

PQP = topic("plus-que-parfait", "The plus-que-parfait: had done", f'''
<p>For something that happened <b>before another past action</b>. Form it like the passé composé, but put avoir / être in the <b>imparfait</b>.</p>
{ex("Quand je suis arrivé, le film avait déjà commencé.", "When I arrived, the movie had already started.")}
{ex("Elle était fatiguée parce qu'elle n'avait pas dormi.", "She was tired because she hadn't slept.")}
{ex("Ils m'ont dit qu'ils étaient partis à midi.", "They told me they had left at noon. (être verb, so étaient partis)")}
{lab(type="conj", verbs=["finir", "partir", "voir", "faire", "manger", "arriver", "se lever"], tenses=["pqp", "pc"])}
{wa("Ordering events", [
 ("a|Je|s  b|suis arrivé|n  c|à la gare.|x", "Event 2: I arrived.", "I arrived at the station."),
 ("a|Je|s  b|suis arrivé|n  c|à la gare,|x  d|mais|gl  e|le train|s  f|était parti.|e", "Event 1 happened before that: plus-que-parfait.", "I arrived at the station, but the train had left.")])}
''', pill=("g", "C1.3"), sub="One step further back in time.")
CH.append(chapter("past-c1", "L'imparfait et le passé composé", "Past tenses", [IMPF, USES, PQP]))

STORY = topic("narration", "Putting a story together", f'''
<p>Here is a short narrative. Read it out loud, then look at how each verb was chosen.</p>
<div class="ex">{F("C'était un samedi d'octobre. Il faisait froid et il pleuvait. J'attendais le bus depuis vingt minutes quand une voiture s'est arrêtée devant moi. C'était Léa, une amie que je n'avais pas vue depuis le lycée. Elle m'a proposé de me déposer, et nous avons parlé pendant tout le trajet.")}
<span class="en">It was a Saturday in October. It was cold and raining. I had been waiting for the bus for twenty minutes when a car stopped in front of me. It was Léa, a friend I hadn't seen since high school. She offered me a ride, and we talked the whole way.</span></div>
<ul><li><b>Imparfait:</b> C'était, faisait, pleuvait, attendais (had been waiting: depuis + imparfait), C'était.</li>
<li><b>Passé composé:</b> s'est arrêtée, a proposé, avons parlé (pendant tout le trajet = a defined length).</li>
<li><b>Plus-que-parfait:</b> n'avais pas vue (before the story began; the participle agrees with que = Léa).</li></ul>
{box("plain", "Depuis + imparfait", "<i>J'attendais depuis vingt minutes</i> = I had been waiting for twenty minutes. In the present: <i>J'attends depuis vingt minutes</i> = I've been waiting for twenty minutes.")}
''', pill=("v", "C1.4"), sub="A model narrative, annotated.")
CH.append(chapter("story-c1", "Raconter: Narration", "Narration", [STORY]))

REV = topic("review-c1", "Unit summary", f'''<div class="grid2"><div class="mini"><h4>Imparfait</h4><p>nous stem + ais, ais, ait, ions, iez, aient. être → ét-. Description, background, habits, in progress.</p></div>
<div class="mini"><h4>Passé composé</h4><p>Completed events, sequences, interruptions, defined duration, sudden changes.</p></div>
<div class="mini"><h4>Plus-que-parfait</h4><p>avoir / être in the imparfait + participle. An action before another past action.</p></div>
<div class="mini"><h4>Meaning shifts</h4><p>savais / ai su, connaissais / ai connu, voulais / ai voulu, pouvais / ai pu.</p></div></div>''', sub="Everything from this unit on one screen.")
MIS = topic("mistakes-c1", "Common mistakes", '''<ol class="steps">
<li>Using the imparfait for every long action: <i>J'habitais à Paris pendant deux ans</i> → <i>J'ai habité</i> (defined length, finished).</li>
<li>Using the passé composé for descriptions: <i>Il a fait beau et j'ai été content</i> when setting the scene → <i>Il faisait beau et j'étais content</i>.</li>
<li><i>nous mangeions</i> → <i>nous mangions</i>.</li>
<li><i>j'étais allé</i> vs <i>j'avais allé</i>: être verbs keep être in the plus-que-parfait.</li>
<li>Translating "was" automatically as <i>a été</i>: in descriptions it's <i>était</i>.</li>
<li>Forgetting depuis + imparfait for "had been …-ing".</li></ol>''', sub="Points students lose most often.")
CH.append(chapter("review-ch-c1", "Review", "Review", [REV, MIS]))

PQ = [
 q("Imparfait of <i>nous finissons</i> → je…", ["finissais", "finirais", "finais", "finissai"], 0, "nous finiss-ons → finiss- + ais.", "g"),
 q("Imparfait of <i>être</i>, nous:", ["étions", "sommions", "êtions", "étaient"], 0, "être uses ét-: nous étions.", "g"),
 q("<i>Quand j'étais petit, je ______ au parc tous les jours.</i>", ["jouais", "ai joué", "jouerai", "avais joué"], 0, "Habit (tous les jours) → imparfait.", "g"),
 q("<i>Il ______ quand je suis sorti.</i> (pleuvoir)", ["pleuvait", "a plu", "pleut", "avait plu"], 0, "Background weather → imparfait.", "g"),
 q("<i>Je regardais la télé quand mon frère ______.</i>", ["est rentré", "rentrait", "rentre", "rentrerait"], 0, "Interrupting event → passé composé.", "g"),
 q("<i>Hier, je ______ à 7 h, j'ai mangé et je suis parti.</i>", ["me suis levé", "me levais", "me lève", "m'étais levé"], 0, "Sequence of events → passé composé.", "g"),
 q("<i>Nous ______ à Montréal pendant cinq ans.</i>", ["avons habité", "habitions", "habiterons", "avions habité"], 0, "Defined, finished period → passé composé.", "g"),
 q("<i>D'habitude, elle ______ le bus.</i>", ["prenait", "a pris", "prendra", "avait pris"], 0, "d'habitude → imparfait.", "g"),
 q("<i>Soudain, la lumière ______.</i>", ["s'est éteinte", "s'éteignait", "s'éteint", "s'était éteinte"], 0, "soudain signals an event.", "g"),
 q("<i>J'ai su la vérité</i> means…", ["I found out the truth.", "I knew the truth (all along).", "I will know the truth.", "I would know the truth."], 0, "savoir in the passé composé = found out.", "g"),
 q("<i>J'ai connu Marc en 2020</i> means…", ["I met Marc in 2020.", "I used to know Marc in 2020.", "I recognized Marc in 2020.", "I had known Marc since 2020."], 0, "connaître in the passé composé = met for the first time.", "g"),
 q("<i>Quand je suis arrivé, ils ______ déjà.</i> (manger)", ["avaient mangé", "mangeaient", "ont mangé", "mangeront"], 0, "Before another past action → plus-que-parfait.", "g"),
 q("<i>Elle était triste parce que son chat ______.</i> (partir)", ["était parti", "avait parti", "partait", "est parti"], 0, "partir uses être: était parti.", "g"),
 q("Plus-que-parfait of <i>je vois</i>:", ["j'avais vu", "j'ai vu", "je voyais", "j'étais vu"], 0, "avoir in the imparfait + vu.", "g"),
 q("<i>J'attendais depuis une heure</i> means…", ["I had been waiting for an hour.", "I waited an hour ago.", "I've been waiting for an hour.", "I will wait an hour."], 0, "depuis + imparfait = had been …-ing.", "g"),
 q("Which describes the <b>setting</b> of a story?", ["C'était l'hiver et il neigeait.", "Il a neigé une fois.", "Il est tombé.", "Elle a ouvert la porte."], 0, "Description → imparfait.", "g"),
 q("<i>Nous ______ beaucoup quand nous étions jeunes.</i> (voyager)", ["voyagions", "voyageions", "avons voyagé", "voyagerions"], 0, "Habit; -ger verbs drop the e before i: voyagions.", "g"),
 q("<i>Pendant que tu ______, j'ai fait la cuisine.</i>", ["dormais", "as dormi", "dors", "avais dormi"], 0, "pendant que + action in progress → imparfait.", "g"),
 q("<i>Je voulais venir, mais je n'ai pas pu</i> means…", ["I wanted to come, but I couldn't (didn't manage to).", "I came, but I didn't want to.", "I want to come, but I can't.", "I had wanted to come and I could."], 0, "ai pu = managed (here: didn't manage).", "g"),
 q("<i>Il avait seize ans quand il ______ son premier job.</i>", ["a trouvé", "trouvait", "avait trouvé", "trouve"], 0, "Age is background (imparfait); finding the job is the event.", "g"),
 q("<i>Elle ______ le livre trois fois.</i>", ["a lu", "lisait", "lit", "lirait"], 0, "A set number of times → passé composé.", "g"),
 q("<i>J'avais faim parce que je ______ le petit-déjeuner.</i>", ["n'avais pas pris", "ne prenais pas", "n'ai pas pris", "ne prendrai pas"], 0, "Earlier than being hungry → plus-que-parfait.", "g"),
 q(f"{listen('Il faisait nuit quand nous sommes arrivés.')} Which part is the background?", ["It was dark", "we arrived", "both", "neither"], 0, "faisait (imparfait) = background.", "v"),
 q("Which sentence is correct?", ["Quand j'avais dix ans, j'ai déménagé à Chicago.", "Quand j'ai eu dix ans, je déménageais à Chicago.", "Quand j'avais dix ans, je déménageais à Chicago une fois.", "Quand j'aurais dix ans, j'ai déménagé à Chicago."], 0, "Age = background (avais); moving = one event (ai déménagé).", "g"),
]
CHAL = [
 q("Choose the best pair: <i>Il ______ minuit. Tout le monde ______ quand le téléphone a sonné.</i>", ["était … dormait", "a été … a dormi", "était … a dormi", "a été … dormait"], 0, "Both are background.", "g"),
 q("<i>J'ai habité à Paris</i> vs <i>J'habitais à Paris</i>:", ["The first sums up a finished period; the second describes the situation at the time.", "They mean exactly the same.", "The first is a habit; the second is a single event.", "The first is wrong."], 0, "Point of view: finished whole vs ongoing background.", "g"),
 q("<i>La maison que nous ______ était à vendre.</i> (had visited)", ["avions visitée", "avions visité", "étions visitée", "avons visitée"], 0, "Plus-que-parfait with avoir; the participle agrees with que (maison, f.).", "g"),
 q("Which sentence uses <i>vouloir</i> to mean \"tried / decided\"?", ["J'ai voulu l'appeler, mais il ne répondait pas.", "Je voulais un chien quand j'étais petit.", "Il voulait partir.", "Nous voulions savoir."], 0, "Passé composé of vouloir = a specific attempt.", "g"),
 q("<i>Ils ______ depuis deux heures quand nous sommes arrivés.</i>", ["jouaient", "ont joué", "avaient joué", "joueraient"], 0, "depuis + imparfait = had been doing.", "g"),
 q("Imparfait of <i>commencer</i>, je:", ["commençais", "commencais", "commenceais", "commençait"], 0, "ç before a.", "g"),
 q("<i>Quand elle est entrée, je ______ que je l'______ déjà ______.</i>", ["ai compris … avais … vue", "comprenais … ai … vue", "ai compris … ai … vu", "comprenais … avais … vu"], 0, "Realizing = event; having seen her = earlier (agrees with l' = her).", "g"),
 q("Which sentence is correct?", ["Il a eu peur quand il a entendu le bruit.", "Il avait peur quand il entendait le bruit soudain.", "Il a eu peur quand il entendait le bruit soudain une fois.", "Il aurait peur quand il a entendu le bruit."], 0, "A sudden reaction to an event: passé composé.", "g"),
]
EXQ = [
 q("Imparfait of <i>faire</i>, ils:", ["faisaient", "fesaient", "faisient", "font"], 0, "nous faisons → fais- + aient.", "g", "gram"),
 q("<i>Quand j'étais jeune, nous ______ à la campagne.</i>", ["habitions", "avons habité", "habiterons", "avions habité"], 0, "Description of how things were.", "g", "gram"),
 q("<i>Elle lisait quand quelqu'un ______ à la porte.</i>", ["a frappé", "frappait", "avait frappé", "frappe"], 0, "Interruption → passé composé.", "g", "gram"),
 q("<i>Le matin, il ______ toujours du café.</i>", ["buvait", "a bu", "boira", "avait bu"], 0, "toujours (habit) → imparfait.", "g", "gram"),
 q("<i>Nous ______ le film deux fois.</i>", ["avons vu", "voyions", "avions vu", "verrons"], 0, "Counted repetitions → passé composé.", "g", "gram"),
 q("<i>Il était content parce qu'il ______ son examen.</i>", ["avait réussi", "réussissait", "a réussi", "réussira"], 0, "Earlier than being happy → plus-que-parfait.", "g", "gram"),
 q("<i>Je suis allé chez elle, mais elle ______.</i> (had gone out)", ["était sortie", "avait sorti", "sortait", "est sortie"], 0, "sortir + être; elle → sortie.", "g", "gram"),
 q("<i>J'ai connu ma meilleure amie au lycée</i> means…", ["I met my best friend in high school.", "I knew my best friend in high school.", "I know my best friend from high school.", "I had known my best friend in high school."], 0, "connaître (PC) = met.", "v", "vocab"),
 q("<i>Tout à coup</i> signals…", ["a sudden event (passé composé)", "a habit (imparfait)", "the future", "a description"], 0, "tout à coup = all of a sudden.", "v", "vocab"),
 q("<i>J'attendais depuis dix minutes quand…</i> means…", ["I had been waiting for ten minutes when…", "I waited ten minutes ago when…", "I'll wait ten minutes when…", "I have waited ten minutes since…"], 0, "depuis + imparfait.", "g", "gram"),
 q("<i>Hier, il ______ froid, alors j'ai mis un manteau.</i>", ["faisait", "a fait", "fera", "avait fait"], 0, "Weather as background.", "g", "gram"),
 q("Which verb form is wrong?", ["nous mangeions", "nous étudiions", "je commençais", "ils finissaient"], 0, "nous mangions (no e before i).", "g", "gram"),
 q(f"{listen('Je dormais quand le réveil a sonné.')} What happened?", ["The alarm went off while the speaker was sleeping.", "The speaker woke up before the alarm.", "The speaker set the alarm.", "The alarm never rang."], 0, "dormais (background) + a sonné (event).", "v", "listen"),
 q("Read: <i>Quand Hugo avait douze ans, il passait tous ses étés chez ses grands-parents. Un jour, il a trouvé une vieille boîte dans le grenier. Son grand-père l'avait cachée là quarante ans plus tôt.</i> Which is true?", ["The grandfather hid the box long before Hugo found it.", "Hugo found a box every summer.", "Hugo hid the box.", "Hugo was forty."], 0, "l'avait cachée: plus-que-parfait, earlier.", "v", "read"),
 q("Which is the best English for <i>Je pouvais nager à cinq ans</i>?", ["I could swim when I was five.", "I managed to swim once at five.", "I can swim at five.", "I will be able to swim at five."], 0, "pouvoir (imparfait) = was able to, in general.", "g", "gram"),
]
FRQS = [
 {"q": "Tell a story about a memorable day (at least 10 sentences).",
  "parts": [{"p": "Set the scene with the imparfait, tell the events with the passé composé, and include at least two verbs in the plus-que-parfait.",
   "rubric": [["Imparfait used for setting, description and actions in progress", 2], ["Passé composé used for the main events, in order", 2], ["Two correct plus-que-parfait verbs", 2], ["Correct auxiliaries and agreement with être verbs", 1], ["Time and sequence words (un jour, soudain, ensuite, pendant que…)", 1], ["Accuracy and variety overall", 2]],
   "answer": f'<div class="ex">{F("C\'était le premier jour des vacances. Il faisait très chaud et le ciel était bleu. Mes amis et moi, nous avions décidé d\'aller à la plage. Quand nous sommes arrivés, il y avait déjà beaucoup de monde. Pendant que mes amis nageaient, je lisais sous un parasol. Soudain, j\'ai entendu des cris : un petit garçon avait perdu ses parents. Je l\'ai aidé à les chercher et nous les avons trouvés dix minutes plus tard. Ils étaient très reconnaissants. Le soir, nous sommes rentrés fatigués mais contents.")}<span class="en">It was the first day of vacation. It was very hot and the sky was blue. My friends and I had decided to go to the beach. When we arrived, there were already a lot of people. While my friends were swimming, I was reading under an umbrella. Suddenly I heard shouting: a little boy had lost his parents. I helped him look for them and we found them ten minutes later. They were very grateful. In the evening we went home tired but happy.</span></div>'}]},
 {"q": "Rewrite this paragraph in the past, choosing passé composé or imparfait for each verb.",
  "parts": [{"p": "Il est 8 h. Il pleut. Marie attend le bus. Elle est fatiguée. Le bus arrive. Elle monte et elle s'assied près de la fenêtre.",
   "rubric": [["Background verbs in the imparfait: Il était, il pleuvait, attendait, était fatiguée", 2], ["Events in the passé composé: est arrivé, est montée, s'est assise", 2], ["Agreement: montée, assise", 1]],
   "answer": f'<div class="ex">{F("Il était 8 h. Il pleuvait. Marie attendait le bus. Elle était fatiguée. Le bus est arrivé. Elle est montée et elle s\'est assise près de la fenêtre.")}<span class="en">Background → imparfait; events → passé composé.</span></div>'}]},
]

if __name__ == "__main__":
    build(1, "college-1", "Le passé", 'Le <span class="hl">passé</span>',
          "College French: passé composé vs imparfait, the plus-que-parfait, and how to tell a story in the past. Tap any French word to hear it.",
          "College French Unit 1: passé composé, imparfait and plus-que-parfait, with audio, timeline labs, practice questions and a practice exam.",
          CH, PQ, CHAL, EXQ, FRQS, "/home/claude/ap-physics-study/courses/french-1/college-1.html", college=True)
