from fr_common import *

CH = []
CORE = f'''<p>This unit is about <b>things and people</b>: naming them with the right little word (le, la, un, une…), describing them, and saying what you have. The big idea is <b>gender</b>: every French noun is masculine or feminine, and the words around it change to match.</p>
{wa("Everything agrees with the noun", [
 ("a|un|x  b|chat|s  c|noir|v", "un chat noir: chat is masculine, so un and noir are in their masculine forms.", "a black cat"),
 ("a|une|x  b|voiture|s  c|noire|v", "une voiture noire: voiture is feminine, so we get une and noire with an e.", "a black car"),
 ("a|des|x  b|voitures|s  c|noires|v", "Plural: des, and both noun and adjective add an s (silent).", "black cars")])}
<div class="grid2"><div class="mini"><h4>In this unit</h4><p>Articles and gender · plurals · the verb avoir and il y a · adjectives (agreement and position) · family and possessives (mon, ma, mes…).</p></div>
<div class="mini"><h4>Habit to build</h4><p>Always learn a noun <b>with its article</b>: not "livre" but "un livre", not "table" but "une table". The article tells you the gender.</p></div></div>'''
CH.append(chapter("overview-f2", "Overview", "Overview", [topic("core-f2", "Les gens et les choses", CORE)]))

# ------------------------------------------------------------------ articles
ART = topic("articles", "Gender and articles", f'''
<p>French has two genders, masculine and feminine. For people the gender usually matches (un garçon, une fille). For things it just has to be learned: {F("un livre")} (a book) is masculine, {F("une table")} is feminine.</p>
<div class="tblwrap"><table><tr><th></th><th>Masculine</th><th>Feminine</th><th>Before a vowel or silent h</th><th>Plural</th></tr>
<tr><td><b>the</b> (definite)</td><td>{F("le livre")}</td><td>{F("la table")}</td><td>{F("l'ami")}, {F("l'école")}</td><td>{F("les livres")}</td></tr>
<tr><td><b>a / some</b> (indefinite)</td><td>{F("un livre")}</td><td>{F("une table")}</td><td>{F("un ami")}, {F("une école")}</td><td>{F("des livres")}</td></tr></table></div>
{lab(type="noun", rows=[0, 1], nouns=["livre", "stylo", "cahier", "table", "chaise", "école", "ami", "amie", "hôtel", "chat", "maison", "université", "gâteau", "eau"])}
<h3>Clues to gender</h3>
<div class="grid2"><div class="mini"><h4>Often masculine</h4><p>Words ending in <b>-age</b> (le fromage), <b>-ment</b> (le moment), <b>-eau</b> (le bureau), <b>-isme</b>, and most ending in a consonant.</p></div>
<div class="mini"><h4>Often feminine</h4><p>Words ending in <b>-tion / -sion</b> (la nation), <b>-té</b> (la liberté), <b>-ette</b>, <b>-ure</b> (la voiture), <b>-ence</b>, and many ending in <b>-e</b>.</p></div></div>
{box("trap", "Watch out", "These are only patterns: <i>la plage</i> (beach) and <i>l'eau</i> (water) are feminine, <i>le musée</i> is masculine. When you're not sure, check a dictionary for <b>n.m.</b> or <b>n.f.</b>")}
<h3>Using the definite article</h3>
<p>French uses <b>le / la / les</b> much more than English uses <i>the</i>. Use it for things in general and for likes and dislikes.</p>
{ex("J'aime le chocolat.", "I like chocolate. (chocolate in general)")}
{ex("Les chats sont mignons.", "Cats are cute.")}
''', pill=("g", "2.1"), sub="le, la, l', les and un, une, des.",
 det=("More about articles", '''<h4>Why learn the article with the noun</h4><p>Nouns that start with a vowel hide their gender with the definite article: <i>l'ami</i> could be either. Learn them with un / une: <i>un ami</i>, <i>une école</i>.</p>
<h4>des is the plural of un / une</h4><p>English often uses no word at all: <i>J'ai des amis à Paris</i> = I have friends in Paris. French almost never leaves a noun without an article.</p>
<h4>Some nouns change meaning with gender</h4><p><i>le livre</i> = the book, <i>la livre</i> = the pound. <i>le tour</i> = the tour, <i>la tour</i> = the tower (la tour Eiffel).</p>'''))

PLUR = topic("plurals", "Making nouns plural", f'''
<p>Most nouns add a silent <b>-s</b>, so in speech you often hear the plural only from the article: {F("le livre")} vs {F("les livres")} sound different because of le / les.</p>
<div class="tblwrap"><table><tr><th>Singular ending</th><th>Plural</th><th>Example</th></tr>
<tr><td>most nouns</td><td>+ s</td><td>{F("un ami → des amis")}</td></tr>
<tr><td>-s, -x, -z</td><td>no change</td><td>{F("un bus → des bus")}, {F("un prix → des prix")}</td></tr>
<tr><td>-eau, -eu</td><td>+ x</td><td>{F("un gâteau → des gâteaux")}, {F("un jeu → des jeux")}</td></tr>
<tr><td>-al</td><td>-aux</td><td>{F("un animal → des animaux")}, {F("un journal → des journaux")}</td></tr></table></div>
{ex("Il y a trois gâteaux sur la table.", "There are three cakes on the table.")}
''', pill=("g", "2.2"), sub="Usually just a silent s.")
CH.append(chapter("articles-f2", "Le, la, un, une: Articles", "Articles", [ART, PLUR]))

# ------------------------------------------------------------------ avoir
AVOIR = topic("avoir", "Avoir: to have", f'''
<div class="tblwrap"><table class="conj"><tr><td>{F("j'ai")}</td><td>I have</td><td>{F("nous avons")}</td><td>we have</td></tr>
<tr><td>{F("tu as")}</td><td>you have</td><td>{F("vous avez")}</td><td>you have</td></tr>
<tr><td>{F("il / elle / on a")}</td><td>he / she / one has</td><td>{F("ils / elles ont")}</td><td>they have</td></tr></table></div>
{lab(type="conj", verbs=["avoir", "être"], tenses=["pres"])}
{box("trap", "Sound-alikes", f"{F('ils ont')} (they have) has a <b>z</b> sound from the liaison: il-zon. {F('ils sont')} (they are) has an <b>s</b> sound: il-son. Listen to both.")}
<h3>Expressions with avoir</h3>
<p>Where English says "I <i>am</i> hungry", French says "I <i>have</i> hunger".</p>
{vt([("avoir … ans", "to be … years old"), ("avoir faim", "to be hungry"), ("avoir soif", "to be thirsty"), ("avoir chaud", "to be hot (a person)"), ("avoir froid", "to be cold (a person)"), ("avoir peur (de)", "to be afraid (of)"), ("avoir sommeil", "to be sleepy"), ("avoir raison / tort", "to be right / wrong"), ("avoir besoin de", "to need"), ("avoir envie de", "to feel like, want")])}
{ex("J'ai faim ! On mange ?", "I'm hungry! Shall we eat?")}
{ex("Tu as besoin d'un stylo ?", "Do you need a pen?")}
{ex("Nous avons froid.", "We're cold.")}
<h3>Il y a: there is, there are</h3>
<p>{F("il y a")} never changes for singular or plural.</p>
{ex("Il y a un chat dans la cuisine.", "There's a cat in the kitchen.")}
{ex("Il y a vingt élèves dans la classe.", "There are twenty students in the class.")}
{ex("Qu'est-ce qu'il y a ?", "What's the matter? / What's there?")}
''', pill=("g", "2.3"), sub="The second most important verb, and the expressions that use it.",
 det=("Avoir in detail", '''<h4>Je becomes j'</h4><p>avoir starts with a vowel, so it's always <i>j'ai</i>, never "je ai".</p>
<h4>Être or avoir?</h4><p>English "to be" + hungry, thirsty, hot, cold, afraid, right, wrong, sleepy, X years old → French uses <b>avoir</b>. For descriptions (tall, nice, tired) use être: <i>Je suis fatigué</i>.</p>
<h4>Chaud and froid</h4><p>For a person use avoir: <i>J'ai chaud</i> (I'm hot). For the weather use faire: <i>Il fait chaud</i> (it's hot out). For an object use être: <i>Le café est chaud</i>. Saying "je suis chaud" means something else, so avoid it.</p>'''))
CH.append(chapter("avoir-f2", "Avoir: to have", "Avoir", [AVOIR]))

# ------------------------------------------------------------------ adjectives
ADJ = topic("adjectives", "Describing with adjectives", f'''
<p>Adjectives agree with the noun in <b>gender</b> and <b>number</b>. The usual pattern: add <b>-e</b> for feminine, <b>-s</b> for plural.</p>
<div class="tblwrap"><table><tr><th></th><th>Singular</th><th>Plural</th></tr>
<tr><td>Masculine</td><td>{F("il est grand")}</td><td>{F("ils sont grands")}</td></tr>
<tr><td>Feminine</td><td>{F("elle est grande")}</td><td>{F("elles sont grandes")}</td></tr></table></div>
<p>Listen: in {F("grande")} you hear the d, in {F("grand")} you don't. Adding -e often makes a silent consonant come alive.</p>
<h3>Irregular patterns</h3>
<div class="tblwrap"><table><tr><th>Masculine</th><th>Feminine</th><th>Examples</th></tr>
<tr><td>already ends in -e</td><td>no change</td><td>{F("jeune")}, {F("rouge")}, {F("sympa")} (sympa never changes)</td></tr>
<tr><td>-eux</td><td>-euse</td><td>{F("heureux → heureuse")}, {F("sérieux → sérieuse")}</td></tr>
<tr><td>-if</td><td>-ive</td><td>{F("sportif → sportive")}, {F("actif → active")}</td></tr>
<tr><td>-en, -on, -el</td><td>double + e</td><td>{F("canadien → canadienne")}, {F("bon → bonne")}, {F("cruel → cruelle")}</td></tr>
<tr><td>-er</td><td>-ère</td><td>{F("cher → chère")}</td></tr>
<tr><td>special</td><td></td><td>{F("blanc → blanche")}, {F("gentil → gentille")}, {F("beau → belle")}, {F("nouveau → nouvelle")}, {F("vieux → vieille")}</td></tr></table></div>
<h3>Where adjectives go</h3>
<p>Most adjectives go <b>after</b> the noun: {F("une voiture rouge")}, {F("un livre intéressant")}. A short list goes <b>before</b>. Remember <b>BAGS</b>:</p>
<div class="grid2"><div class="mini"><h4>B · Beauty</h4><p>{F("beau")}, {F("joli")}</p></div><div class="mini"><h4>A · Age</h4><p>{F("jeune")}, {F("vieux")}, {F("nouveau")}</p></div>
<div class="mini"><h4>G · Goodness</h4><p>{F("bon")}, {F("mauvais")}, {F("gentil")}</p></div><div class="mini"><h4>S · Size</h4><p>{F("grand")}, {F("petit")}, {F("gros")}</p></div></div>
{wa("Before or after?", [
 ("a|une|x  b|maison|s  c|blanche|v", "Colors go after the noun.", "a white house"),
 ("a|une|x  c|belle|v  b|maison|s", "beau / belle (Beauty) goes before.", "a beautiful house"),
 ("a|une|x  c|belle|v  b|maison|s  d|blanche|v", "You can have one before and one after.", "a beautiful white house")])}
{lab(type="adj", a="beau")}
''', pill=("g", "2.4"), sub="Agreement and position.",
 det=("Tricky adjective details", '''<h4>bel, nouvel, vieil</h4><p>Before a masculine singular noun starting with a vowel sound, beau, nouveau and vieux have a special form so the words link smoothly: <i>un bel hôtel</i>, <i>un nouvel ami</i>, <i>un vieil homme</i>. They still sound like the feminine forms.</p>
<h4>Mixed groups</h4><p>For a group with masculine and feminine nouns, use the masculine plural: <i>Paul et Marie sont grands.</i></p>
<h4>Plural irregulars</h4><p>Adjectives ending in -s or -x don't change in the masculine plural (<i>heureux</i>, <i>français</i>); -eau becomes -eaux (<i>beaux</i>); -al becomes -aux (<i>normaux</i>).</p>
<h4>Colors that don't change</h4><p>Colors that are also nouns for things, like <i>orange</i> and <i>marron</i> (brown, from the chestnut), never change: <i>des chaussures marron</i>.</p>'''))

DESC = topic("describing-people", "Describing people", f'''
{vt([("grand(e) / petit(e)", "tall / short"), ("blond(e) / brun(e) / roux, rousse", "blond / dark-haired / red-haired"), ("mince / fort(e)", "slim / strong, big"), ("jeune / âgé(e)", "young / elderly"), ("sympa", "nice, friendly", "never changes"), ("gentil(le)", "kind"), ("drôle", "funny"), ("intelligent(e)", "smart"), ("timide", "shy"), ("sportif, sportive", "athletic"), ("paresseux, paresseuse", "lazy"), ("travailleur, travailleuse", "hard-working"), ("sérieux, sérieuse", "serious")])}
<h3>Colors</h3>
{vgrid([("rouge", "red"), ("bleu(e)", "blue"), ("vert(e)", "green"), ("jaune", "yellow"), ("noir(e)", "black"), ("blanc, blanche", "white"), ("gris(e)", "gray"), ("rose", "pink"), ("violet, violette", "purple"), ("orange", "orange (never changes)"), ("marron", "brown (never changes)")])}
{ex("Ma sœur est grande et brune. Elle a les yeux verts.", "My sister is tall and dark-haired. She has green eyes.")}
{ex("Mes amis sont drôles et très sympas.", "My friends are funny and very nice.")}
{box("plain", "Eyes and hair", f"Use avoir + les: {F('Il a les cheveux courts.')} (He has short hair.) {F('J\'ai les yeux bleus.')} (I have blue eyes.)")}
''', pill=("v", "2.5"), sub="Appearance, personality and colors.")
CH.append(chapter("adj-f2", "Les adjectifs: Describing", "Adjectives", [ADJ, DESC]))

# ------------------------------------------------------------------ family & possessives
FAM = topic("family", "La famille", f'''
{vgrid([("la mère / maman", "mother / mom"), ("le père / papa", "father / dad"), ("les parents", "parents"), ("le frère", "brother"), ("la sœur", "sister"), ("le fils", "son (s is said)"), ("la fille", "daughter, girl"), ("le grand-père", "grandfather"), ("la grand-mère", "grandmother"), ("l'oncle", "uncle"), ("la tante", "aunt"), ("le cousin / la cousine", "cousin"), ("le mari / la femme", "husband / wife"), ("l'enfant", "child"), ("le chien / le chat", "dog / cat")])}
{ex("J'ai un frère et deux sœurs.", "I have a brother and two sisters.")}
{ex("Je suis fils unique. / Je suis fille unique.", "I'm an only child (boy / girl).")}
''', pill=("v", "2.6"), sub="Talking about your family.")

POSS = topic("possessives", "My, your, his, her: possessives", f'''
<p>A possessive agrees with the <b>thing owned</b>, not with the owner. {F("sa mère")} can mean <i>his</i> mother or <i>her</i> mother: mère is feminine, so it's sa either way.</p>
<div class="tblwrap"><table><tr><th></th><th>Masculine</th><th>Feminine</th><th>Plural</th></tr>
<tr><td>my</td><td>{F("mon frère")}</td><td>{F("ma sœur")}</td><td>{F("mes parents")}</td></tr>
<tr><td>your (tu)</td><td>{F("ton frère")}</td><td>{F("ta sœur")}</td><td>{F("tes parents")}</td></tr>
<tr><td>his / her / its</td><td>{F("son frère")}</td><td>{F("sa sœur")}</td><td>{F("ses parents")}</td></tr>
<tr><td>our</td><td colspan="2">{F("notre famille")}</td><td>{F("nos parents")}</td></tr>
<tr><td>your (vous)</td><td colspan="2">{F("votre famille")}</td><td>{F("vos parents")}</td></tr>
<tr><td>their</td><td colspan="2">{F("leur famille")}</td><td>{F("leurs parents")}</td></tr></table></div>
{wa("It agrees with the thing, not the owner", [
 ("o|Paul :|gl  a|son|x  b|vélo|s", "Paul's bike: vélo is masculine → son.", "his bike"),
 ("o|Paul :|gl  a|sa|x  b|voiture|s", "Paul's car: voiture is feminine → sa, even though Paul is a man.", "his car"),
 ("o|Julie :|gl  a|son|x  b|vélo|s", "Julie's bike: still son, because vélo is masculine.", "her bike")])}
{box("trap", "Before a vowel", f"Before a feminine word starting with a vowel, use mon / ton / son so the words link: {F('mon amie')}, {F('ton école')}, {F('son histoire')}.")}
{lab(type="noun", rows=[0, 5], nouns=["frère", "sœur", "ami", "amie", "école", "chat", "maison", "livre", "université"])}
<h3>de for possession</h3>
<p>French has no 's. Use <b>de</b>: {F("le livre de Marie")} (Marie's book), {F("la voiture de mon père")} (my father's car).</p>
''', pill=("g", "2.7"), sub="mon, ma, mes and the rest.",
 det=("Possessives in detail", '''<h4>Why "son" for "her"?</h4><p>French looks at the noun after the possessive. <i>son père</i> = his father or her father. Context tells you whose. To be clear, add <i>à lui</i> (his) or <i>à elle</i> (hers): <i>C'est son livre à elle.</i></p>
<h4>Body parts</h4><p>French usually uses le / la / les, not the possessive, for body parts when it's clear whose they are: <i>J'ai les yeux bleus</i>, <i>Il a mal à la tête</i> (his head hurts).</p>
<h4>leur vs leurs</h4><p>leur = their (one thing): <i>leur maison</i>. leurs = their (several things): <i>leurs enfants</i>.</p>'''))
CH.append(chapter("family-f2", "La famille: Family and possessives", "Family", [FAM, POSS]))

REV = topic("review-f2", "Unit 2 summary", f'''<div class="grid2"><div class="mini"><h4>Articles</h4><p>le / la / l' / les (the) · un / une / des (a, some). Learn every noun with un or une.</p></div>
<div class="mini"><h4>Avoir</h4><p>j'ai, tu as, il a, nous avons, vous avez, ils ont. avoir faim / soif / chaud / froid / peur / … ans. il y a = there is / are.</p></div>
<div class="mini"><h4>Adjectives</h4><p>Agree in gender and number (+e, +s). Most go after the noun; BAGS adjectives go before.</p></div>
<div class="mini"><h4>Possessives</h4><p>mon / ma / mes… agree with the thing owned. mon before a vowel. de for 's: le chat de Léa.</p></div></div>''', sub="Everything from this unit on one screen.")
MIS = topic("mistakes-f2", "Common mistakes", '''<ol class="steps">
<li>Making the possessive agree with the owner: <i>Marie et son frère</i> is right (frère is masculine), not "sa frère".</li>
<li>Forgetting agreement: <i>une maison blanc</i> → <i>une maison blanche</i>.</li>
<li>Putting a color before the noun: <i>une rouge voiture</i> → <i>une voiture rouge</i>.</li>
<li>Using être instead of avoir: <i>je suis faim</i> → <i>j'ai faim</i>.</li>
<li>Saying <i>ma amie</i>: before a vowel use <i>mon amie</i>.</li>
<li>Mixing up <i>ils ont</i> (they have, z sound) and <i>ils sont</i> (they are, s sound).</li>
<li>Leaving out the article: <i>J'aime chocolat</i> → <i>J'aime le chocolat</i>.</li></ol>''', sub="Points students lose most often.")
CH.append(chapter("review-ch-f2", "Review", "Review", [REV, MIS]))

PQ = [
 q("Which article goes with <i>table</i> (feminine)?", ["la", "le", "l'", "un"], 0, "Feminine singular, starting with a consonant → la.", "g"),
 q("Choose: <i>______ école</i> (the school)", ["l'", "la", "le", "les"], 0, "école starts with a vowel, so la → l'.", "g"),
 q("Plural of <i>un gâteau</i>:", ["des gâteaux", "des gâteaus", "les gâteau", "des gâteaues"], 0, "-eau nouns take -x in the plural, and un → des.", "g"),
 q("Plural of <i>un animal</i>:", ["des animaux", "des animals", "des animales", "des animal"], 0, "-al → -aux.", "g"),
 q("Which word is most likely <b>feminine</b>?", ["nation", "fromage", "bureau", "moment"], 0, "-tion words are feminine; -age, -eau and -ment are usually masculine.", "g"),
 q("<i>Nous ______ deux chats.</i>", ["avons", "avez", "ont", "sommes"], 0, "nous → avons.", "g"),
 q("<i>Elles ______ quinze ans.</i>", ["ont", "sont", "a", "avons"], 0, "Age uses avoir: elles ont.", "g"),
 q("How do you say <i>I'm thirsty</i>?", ["J'ai soif.", "Je suis soif.", "J'ai faim.", "Je suis soifé."], 0, "avoir soif = to be thirsty.", "v"),
 q("<i>Il y a</i> means…", ["there is / there are", "he has", "he is there", "they have"], 0, "il y a is a fixed expression.", "v"),
 q("Choose: <i>Ma sœur est ______.</i>", ["petite", "petit", "petits", "petites"], 0, "sœur is feminine singular → petite.", "g"),
 q("Choose: <i>Mes frères sont ______.</i>", ["sportifs", "sportives", "sportif", "sportive"], 0, "Masculine plural → sportifs.", "g"),
 q("Feminine of <i>heureux</i>:", ["heureuse", "heureuxe", "heureuze", "heureux"], 0, "-eux → -euse.", "g"),
 q("Which is correct?", ["une voiture rouge", "une rouge voiture", "un voiture rouge", "une voiture rouges"], 0, "Colors go after the noun; voiture is feminine.", "g"),
 q("Which is correct?", ["un petit chien", "un chien petit", "une petite chien", "un petite chien"], 0, "petit is a Size adjective (BAGS), so it goes before.", "g"),
 q("Which is correct?", ["un bel hôtel", "un beau hôtel", "un belle hôtel", "un hôtel bel"], 0, "beau becomes bel before a masculine noun starting with a vowel sound.", "g"),
 q("<i>Marie aime ______ père.</i> (her father)", ["son", "sa", "ses", "leur"], 0, "père is masculine → son, even though Marie is female.", "g"),
 q("<i>Paul cherche ______ clés.</i> (his keys)", ["ses", "son", "sa", "leurs"], 0, "clés is plural → ses.", "g"),
 q("Choose: <i>______ amie s'appelle Zoé.</i> (my friend, female)", ["Mon", "Ma", "Mes", "Ton"], 0, "Before a vowel, ma → mon.", "g"),
 q("<i>Nos parents</i> means…", ["our parents", "your parents", "their parents", "no parents"], 0, "notre / nos = our.", "v"),
 q("How do you say <i>Léa's cat</i>?", ["le chat de Léa", "Léa's chat", "le Léa chat", "la chat de Léa"], 0, "Use de: le chat de Léa.", "g"),
 q("<i>La sœur de mon père</i> is my…", ["tante", "cousine", "grand-mère", "nièce"], 0, "Your father's sister is your aunt: ta tante.", "v"),
 q("Which describes someone who doesn't like to work?", ["paresseux", "travailleur", "sérieux", "sportif"], 0, "paresseux = lazy.", "v"),
 q("<i>Elle a les yeux ______.</i> (blue)", ["bleus", "bleues", "bleu", "bleue"], 0, "yeux is masculine plural → bleus.", "g"),
 q(f"{listen('ils ont')} What did you hear?", ["ils ont (they have)", "ils sont (they are)", "il a (he has)", "il est (he is)"], 0, "The z sound of the liaison (il-zon) means ont.", "v"),
]
CHAL = [
 q("<i>Julie et Thomas sont ______.</i>", ["grands", "grandes", "grand", "grande"], 0, "A mixed group takes the masculine plural.", "g"),
 q("Which sentence is correct?", ["C'est une belle maison blanche.", "C'est une maison belle blanche.", "C'est une blanche belle maison.", "C'est un beau maison blanc."], 0, "belle (Beauty) before, blanche (color) after, both feminine.", "g"),
 q("Which sentence is correct?", ["Il a besoin d'un nouvel ordinateur.", "Il a besoin d'un nouveau ordinateur.", "Il est besoin d'un nouvel ordinateur.", "Il a besoin un nouvel ordinateur."], 0, "avoir besoin de, and nouveau → nouvel before a vowel.", "g"),
 q("<i>Les enfants de M. et Mme Roux</i> → <i>______ enfants</i>", ["leurs", "leur", "ses", "son"], 0, "Their (several owners) + plural thing → leurs.", "g"),
 q("Which has a mistake?", ["Je suis froid.", "J'ai froid.", "Il fait froid.", "L'eau est froide."], 0, "For a person feeling cold, use avoir froid.", "g"),
 q("Which pair is masculine / feminine correctly?", ["gentil / gentille", "gentil / gentile", "gentile / gentil", "gentil / gentil"], 0, "gentil doubles the l: gentille.", "g"),
 q("<i>Chloé parle à ______ oncle et à ______ tante.</i>", ["son … sa", "sa … son", "son … son", "sa … sa"], 0, "oncle is masculine (son), tante is feminine and starts with a consonant (sa).", "g"),
 q("Which sentence is correct?", ["Elles ont des chaussures marron.", "Elles ont des chaussures marronnes.", "Elles ont des marron chaussures.", "Elles sont des chaussures marron."], 0, "marron never changes, goes after the noun, and having = avoir.", "g"),
]
EXQ = [
 q("Which article: <i>______ livres</i> (the books)", ["les", "le", "des", "la"], 0, "Plural definite → les.", "g", "gram"),
 q("<i>J'ai ______ chien et ______ chatte.</i>", ["un … une", "une … un", "un … un", "le … une"], 0, "chien masculine, chatte (female cat) feminine.", "g", "gram"),
 q("Plural of <i>un journal</i>:", ["des journaux", "des journals", "des journales", "les journal"], 0, "-al → -aux.", "g", "gram"),
 q("<i>Vous ______ un stylo ?</i>", ["avez", "avons", "as", "ont"], 0, "vous → avez.", "g", "gram"),
 q("<i>Il est midi et je n'ai pas mangé. J'ai ______ !</i>", ["faim", "soif", "froid", "sommeil"], 0, "Not having eaten → hungry.", "v", "read"),
 q("<i>Mes cousines sont ______.</i>", ["canadiennes", "canadiens", "canadienes", "canadienne"], 0, "Feminine plural: canadien → canadienne → canadiennes.", "g", "gram"),
 q("Which goes <b>before</b> the noun?", ["jeune", "intelligent", "rouge", "drôle"], 0, "Age adjectives (BAGS) go before.", "g", "gram"),
 q("Choose the correct phrase.", ["une vieille maison", "une vieux maison", "une maison vieille", "un vieil maison"], 0, "vieux → vieille (feminine), placed before.", "g", "gram"),
 q("<i>Hugo et ______ sœur</i> (his sister)", ["sa", "son", "ses", "leur"], 0, "sœur is feminine → sa.", "g", "gram"),
 q("<i>______ école est grande.</i> (your school, tu)", ["Ton", "Ta", "Tes", "Votre"], 0, "école is feminine but starts with a vowel → ton.", "g", "gram"),
 q("<i>Le frère de ma mère</i> is my…", ["oncle", "cousin", "grand-père", "neveu"], 0, "Your mother's brother is your uncle.", "v", "vocab"),
 q(f"{listen('Elle est grande et rousse.')} The person is…", ["tall with red hair", "small with red hair", "tall and blond", "big and dark-haired"], 0, "grande = tall, rousse = red-haired.", "v", "listen"),
 q("Read: <i>Je m'appelle Nadia. J'ai un frère, Karim. Il a dix ans. Il est petit et très drôle. Il a les cheveux noirs.</i> Which is true?", ["Karim is ten and funny.", "Karim is tall.", "Nadia has a sister.", "Karim has blond hair."], 0, "dix ans, petit (short), drôle (funny), cheveux noirs.", "v", "read"),
 q("Which sentence is correct?", ["Il y a trois chats dans le jardin.", "Il y ont trois chats dans le jardin.", "Il sont trois chats dans le jardin.", "Il y a trois chat dans le jardin."], 0, "il y a never changes, and chats is plural.", "g", "gram"),
 q("<i>C'est la voiture ______ mon père.</i>", ["de", "à", "du", "le"], 0, "Possession: la voiture de mon père.", "g", "gram"),
]
FRQS = [
 {"q": "Describe a member of your family or a friend in at least 5 sentences.",
  "parts": [{"p": "Say who the person is, their age, what they look like and what they're like. Use at least three adjectives.",
   "rubric": [["Identifies the person with a possessive (mon frère, ma meilleure amie…)", 1], ["Age with avoir … ans", 1], ["At least three adjectives that agree in gender and number", 2], ["Adjectives in the right position (BAGS before, others after)", 1], ["Uses avoir and être correctly", 1]],
   "answer": f'<div class="ex">{F("Ma meilleure amie s\'appelle Emma. Elle a seize ans. Elle est grande et blonde, et elle a les yeux verts. Elle est très drôle et un peu timide. Elle a un petit chien noir.")}<span class="en">My best friend\'s name is Emma. She is 16. She\'s tall and blond, and she has green eyes. She\'s very funny and a little shy. She has a small black dog.</span></div>'}]},
 {"q": "Rewrite each sentence about Luc so it's about his sister Léa (change everything that needs to change).",
  "parts": [{"p": "Luc est grand, sportif et heureux. C'est un bon ami. Il a un nouveau vélo.",
   "rubric": [["grande, sportive, heureuse", 2], ["une bonne amie", 1], ["Elle a…", 1], ["un nouveau vélo stays the same (it describes the bike, which is masculine)", 1]],
   "answer": f'<div class="ex">{F("Léa est grande, sportive et heureuse. C\'est une bonne amie. Elle a un nouveau vélo.")}<span class="en">The adjectives about Léa change; nouveau vélo doesn\'t, because it agrees with vélo.</span></div>'}]},
]

if __name__ == "__main__":
    build(2, "unit-2", "People and things", 'Les gens <span class="hl">et les choses</span>',
          "Gender and articles, plurals, the verb avoir and il y a, adjectives and where they go, family words and possessives. Tap any French word to hear it.",
          "French 1 Unit 2: articles, avoir, adjectives, family and possessives, with audio, interactive labs, practice questions and a practice exam.",
          CH, PQ, CHAL, EXQ, FRQS, "/home/claude/ap-physics-study/courses/french-1/unit-2.html")
