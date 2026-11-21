from fr_common import *

CH = []
CORE = f'''<p>This unit gives you what you need to get through a day in a French-speaking city: big numbers, telling time, dates, the weather, ordering food, and finding your way around town.</p>
{wa("Little words that merge", [
 ("a|Je vais|s  b|à|x  c|le|x  d|cinéma.|v", "aller à + le cinéma…", "I'm going to the movie theater."),
 ("a|Je vais|s  bc|au|n  d|cinéma.|v", "…à + le always merges into au.", "I'm going to the movie theater."),
 ("a|Je mange|s  b|de|x  c|le|x  d|pain.|v", "de + le pain…", "I eat bread."),
 ("a|Je mange|s  bc|du|n  d|pain.|v", "…de + le merges into du.", "I eat (some) bread.")])}
<div class="grid2"><div class="mini"><h4>In this unit</h4><p>Numbers 70–1000 · telling time · days, months and dates · weather · food and the partitive (du, de la) · places in town and à + le = au · the verb venir.</p></div>
<div class="mini"><h4>Habit to build</h4><p>Say the time and date out loud every morning in French: <i>Il est sept heures et quart. Nous sommes le 3 mars.</i></p></div></div>'''
CH.append(chapter("overview-f4", "Overview", "Overview", [topic("core-f4", "La vie de tous les jours", CORE)]))

# ------------------------------------------------------------------ numbers 70+
NUM = topic("numbers-70", "Numbers 70 to 1000", f'''
<p>Above 69, French counts with a little math.</p>
<div class="tblwrap"><table><tr><th>Number</th><th>French</th><th>Literally</th></tr>
<tr><td>70</td><td>{F("soixante-dix")}</td><td>60 + 10</td></tr>
<tr><td>71</td><td>{F("soixante et onze")}</td><td>60 + 11</td></tr>
<tr><td>75</td><td>{F("soixante-quinze")}</td><td>60 + 15</td></tr>
<tr><td>80</td><td>{F("quatre-vingts")}</td><td>4 × 20</td></tr>
<tr><td>81</td><td>{F("quatre-vingt-un")}</td><td>4 × 20 + 1 (no et, no s)</td></tr>
<tr><td>90</td><td>{F("quatre-vingt-dix")}</td><td>4 × 20 + 10</td></tr>
<tr><td>99</td><td>{F("quatre-vingt-dix-neuf")}</td><td>4 × 20 + 19</td></tr>
<tr><td>100</td><td>{F("cent")}</td><td></td></tr>
<tr><td>200, 250</td><td>{F("deux cents")}, {F("deux cent cinquante")}</td><td>cents loses its s when a number follows</td></tr>
<tr><td>1000, 2000</td><td>{F("mille")}, {F("deux mille")}</td><td>mille never takes an s</td></tr></table></div>
{lab(type="num", n=97, max=1000)}
{box("plain", "Belgium and Switzerland", "In Belgium and Switzerland people say <i>septante</i> (70) and <i>nonante</i> (90), and in Switzerland often <i>huitante</i> (80). In France, stick with soixante-dix and quatre-vingt-dix.")}
{ex("Ça coûte quatre-vingt-quinze euros.", "It costs 95 euros.")}
{ex("Ma grand-mère a soixante-dix-huit ans.", "My grandmother is 78.")}
''', pill=("v", "4.1"), sub="soixante-dix, quatre-vingts and beyond.",
 det=("How to read big numbers fast", '''<h4>Split it</h4><p>For 70–79 think "60 and something": 76 = soixante + seize. For 80–99 think "four twenties and something": 93 = quatre-vingt + treize.</p>
<h4>Years</h4><p>Years are said as one big number: 2026 = deux mille vingt-six; 1998 = mille neuf cent quatre-vingt-dix-huit.</p>
<h4>Prices</h4><p>French uses a comma for decimals: 3,50 € = trois euros cinquante. Thousands get a space or a period: 1 500 or 1.500.</p>'''))
CH.append(chapter("num-f4", "Les grands nombres", "Numbers 70+", [NUM]))

# ------------------------------------------------------------------ time and dates
TIME = topic("time", "Telling time", f'''
{vt([("Quelle heure est-il ?", "What time is it?"), ("Il est une heure.", "It's one o'clock."), ("Il est deux heures dix.", "It's 2:10."), ("Il est trois heures et quart.", "It's 3:15. (quarter past)"), ("Il est quatre heures et demie.", "It's 4:30. (half past)"), ("Il est six heures moins le quart.", "It's 5:45. (six minus a quarter)"), ("Il est huit heures moins dix.", "It's 7:50. (eight minus ten)"), ("Il est midi. / Il est minuit.", "It's noon. / It's midnight."), ("À quelle heure… ?", "At what time…?")])}
{lab(type="clock", h=15, m=45)}
<p>After half past, French counts <b>down</b> to the next hour with {F("moins")}. Schedules, TV and trains use the 24-hour clock: {F("Le train part à dix-sept heures quarante.")} (5:40 p.m.)</p>
{box("trap", "Common mistake", "Always say heure(s): <i>Il est trois</i> is incomplete; say <i>Il est trois heures</i>. And it's <i>une heure</i> (feminine), not un heure.")}
''', pill=("v", "4.2"), sub="Quelle heure est-il ?")

CAL = topic("dates", "Days, months, dates and seasons", f'''
<h3>Days of the week</h3>
{vgrid([("lundi", "Monday"), ("mardi", "Tuesday"), ("mercredi", "Wednesday"), ("jeudi", "Thursday"), ("vendredi", "Friday"), ("samedi", "Saturday"), ("dimanche", "Sunday")])}
<h3>Months</h3>
{vgrid([("janvier", "January"), ("février", "February"), ("mars", "March"), ("avril", "April"), ("mai", "May"), ("juin", "June"), ("juillet", "July"), ("août", "August"), ("septembre", "September"), ("octobre", "October"), ("novembre", "November"), ("décembre", "December")])}
<p>Days and months are <b>lowercase</b>. Dates use <b>le + number + month</b>, and the 1st is {F("le premier")}.</p>
{ex("Nous sommes le vendredi 14 juillet.", "It's Friday, July 14th. (Bastille Day)")}
{ex("Mon anniversaire, c'est le premier mai.", "My birthday is May 1st.")}
{ex("Le samedi, je joue au foot.", "On Saturdays I play soccer. (le + day = every week)")}
<h3>Seasons</h3>
{vt([("au printemps", "in (the) spring"), ("en été", "in (the) summer"), ("en automne", "in (the) fall"), ("en hiver", "in (the) winter")])}
''', pill=("v", "4.3"), sub="le lundi, le 3 mars, en été.",
 det=("Date details", '''<h4>Writing dates</h4><p>French writes day / month / year: 03/07/2026 is the 3rd of July, not March 7th.</p>
<h4>le samedi vs samedi</h4><p><i>Samedi, je vais au cinéma</i> = this Saturday (once). <i>Le samedi, je vais au cinéma</i> = on Saturdays (every week).</p>
<h4>Asking the date</h4><p><i>Quelle est la date aujourd'hui ?</i> or <i>On est le combien ?</i> Answer: <i>On est le 12.</i> / <i>C'est le 12 octobre.</i></p>'''))

WEATHER = topic("weather", "Quel temps fait-il ? The weather", f'''
<p>Most weather expressions use {F("il fait")} (literally "it makes").</p>
{vt([("Il fait beau.", "It's nice out."), ("Il fait mauvais.", "The weather's bad."), ("Il fait chaud. / Il fait froid.", "It's hot. / It's cold."), ("Il fait frais.", "It's cool."), ("Il fait 20 degrés.", "It's 20 degrees (Celsius)."), ("Il y a du soleil.", "It's sunny."), ("Il y a du vent.", "It's windy."), ("Il y a des nuages.", "It's cloudy."), ("Il pleut.", "It's raining."), ("Il neige.", "It's snowing.")])}
{ex("En hiver, il fait froid et il neige souvent.", "In winter it's cold and it often snows.")}
{ex("Quand il pleut, je reste à la maison.", "When it rains, I stay home.")}
''', pill=("v", "4.4"), sub="il fait, il y a, il pleut.")
CH.append(chapter("time-f4", "L'heure et la date", "Time & dates", [TIME, CAL, WEATHER]))

# ------------------------------------------------------------------ food & partitive
PART = topic("partitive", "Food and the partitive: du, de la, des", f'''
<p>When you talk about <b>some</b> of something you can't count (bread, water, cheese), French uses the <b>partitive</b> article. English often uses no word at all: "I want bread" → {F("Je veux du pain.")}</p>
<div class="tblwrap"><table><tr><th>Masculine</th><th>Feminine</th><th>Before a vowel</th><th>Plural</th></tr>
<tr><td>{F("du pain")}</td><td>{F("de la confiture")}</td><td>{F("de l'eau")}</td><td>{F("des fraises")}</td></tr></table></div>
{lab(type="noun", rows=[0, 1, 2], nouns=["pain", "fromage", "confiture", "eau", "gâteau"])}
<h3>Which article?</h3>
<div class="grid2"><div class="mini"><h4>le / la / les: in general, likes</h4><p>{F("J'aime le fromage.")} (cheese in general)</p></div>
<div class="mini"><h4>du / de la: some, a portion</h4><p>{F("Je mange du fromage.")} (some cheese)</p></div></div>
<h3>After quantities and negatives: just de</h3>
{vt([("beaucoup de", "a lot of", "beaucoup de sucre"), ("un peu de", "a little", "un peu de lait"), ("assez de / trop de", "enough / too much", "trop de sel"), ("un kilo de", "a kilo of", "un kilo de pommes"), ("une bouteille de", "a bottle of", "une bouteille d'eau"), ("un verre de", "a glass of", "un verre de jus"), ("ne … pas de", "no, not any", "Je ne bois pas de café.")], head=("French", "English", "Example"))}
{wa("de after a quantity", [
 ("a|Je bois|s  b|du|n  c|lait.|v", "Some milk: du lait.", "I drink milk."),
 ("a|Je bois|s  q|beaucoup|x  b|de|n  c|lait.|v", "With a quantity, du shrinks to de.", "I drink a lot of milk."),
 ("a|Je|s  n1|ne|x  a2|bois|s  n2|pas|x  b|de|n  c|lait.|v", "Same after a negative: pas de.", "I don't drink milk.")])}
''', pill=("g", "4.5"), sub="du pain, de la confiture, de l'eau.",
 det=("Choosing the right article for food", '''<h4>Verbs of liking take le / la / les</h4><p>aimer, adorer, préférer, détester talk about things in general: <i>Je déteste les épinards.</i></p>
<h4>Verbs of eating, buying, having often take du / de la</h4><p>manger, boire, prendre, acheter, vouloir talk about a portion: <i>Je prends de la salade.</i> But for a whole countable item, use un / une: <i>Je mange une pomme.</i></p>
<h4>The negative still uses le / la after aimer</h4><p><i>Je n'aime pas le café</i> (le stays: it's still "coffee in general"), but <i>Je ne bois pas de café</i>.</p>'''))

CAFE = topic("cafe", "At the café", f'''
{vgrid([("le pain", "bread"), ("le croissant", "croissant"), ("le fromage", "cheese"), ("le poulet", "chicken"), ("la viande", "meat"), ("le poisson", "fish"), ("les légumes", "vegetables"), ("la salade", "salad, lettuce"), ("les frites", "fries"), ("les fruits", "fruit"), ("la pomme", "apple"), ("la fraise", "strawberry"), ("l'eau", "water"), ("le lait", "milk"), ("le jus d'orange", "orange juice"), ("le café", "coffee"), ("le chocolat chaud", "hot chocolate"), ("le gâteau", "cake")])}
<h3>Ordering</h3>
{vt([("Je voudrais un croissant, s'il vous plaît.", "I'd like a croissant, please.", "je voudrais is the polite way to ask"), ("Pour moi, une limonade.", "For me, a lemonade."), ("Vous désirez ?", "What would you like?", "what the server says"), ("L'addition, s'il vous plaît.", "The check, please."), ("C'est combien ?", "How much is it?")])}
{ex("— Vous désirez ? — Je voudrais un chocolat chaud et une tarte aux pommes, s'il vous plaît.", "— What would you like? — I'd like a hot chocolate and an apple tart, please.")}
''', pill=("v", "4.6"), sub="Food words and ordering politely.")
CH.append(chapter("food-f4", "La nourriture: Food", "Food", [PART, CAFE]))

# ------------------------------------------------------------------ town
TOWN = topic("town", "Places in town and à + article", f'''
{vgrid([("le cinéma", "movie theater"), ("le parc", "park"), ("le musée", "museum"), ("le supermarché", "supermarket"), ("le café", "café"), ("le lycée", "high school"), ("la piscine", "pool"), ("la bibliothèque", "library"), ("la gare", "train station"), ("la plage", "beach"), ("la boulangerie", "bakery"), ("l'école", "school"), ("l'hôpital", "hospital"), ("l'hôtel", "hotel"), ("les magasins", "stores")])}
<p>With {F("aller")} and other verbs of place, <b>à</b> merges with le and les:</p>
<div class="tblwrap"><table><tr><th></th><th>à (to, at)</th><th>de (from, of)</th></tr>
<tr><td>+ le</td><td><b>au</b> parc</td><td><b>du</b> parc</td></tr>
<tr><td>+ la</td><td>à la piscine</td><td>de la piscine</td></tr>
<tr><td>+ l'</td><td>à l'école</td><td>de l'école</td></tr>
<tr><td>+ les</td><td><b>aux</b> magasins</td><td><b>des</b> magasins</td></tr></table></div>
{lab(type="noun", rows=[0, 3, 4], nouns=["parc", "cinéma", "musée", "piscine", "gare", "école", "hôtel", "université"])}
<h3>Where things are</h3>
{vt([("à côté de", "next to"), ("en face de", "across from"), ("près de / loin de", "near / far from"), ("devant / derrière", "in front of / behind"), ("entre", "between"), ("à droite / à gauche", "on the right / left"), ("tout droit", "straight ahead")])}
{ex("La boulangerie est à côté du musée.", "The bakery is next to the museum. (de + le = du)")}
{ex("Le lycée est en face de la gare.", "The high school is across from the train station.")}
''', pill=("g", "4.7"), sub="au, à la, à l', aux.")

VENIR = topic("venir", "Venir: to come", f'''
<div class="tblwrap"><table class="conj"><tr><td>{F("je viens")}</td><td>{F("nous venons")}</td></tr>
<tr><td>{F("tu viens")}</td><td>{F("vous venez")}</td></tr>
<tr><td>{F("il / elle vient")}</td><td>{F("ils / elles viennent")}</td></tr></table></div>
{ex("Tu viens avec nous ?", "Are you coming with us?")}
{ex("Je viens du Canada. / Elle vient de Paris.", "I'm from Canada. / She's from Paris. (venir de = come from)")}
{ex("Je viens de manger.", "I just ate. (venir de + infinitive = to have just done)")}
<p>{F("revenir")} (to come back) and {F("devenir")} (to become) follow the same pattern.</p>
''', pill=("g", "4.8"), sub="Coming from somewhere, and having just done something.")
CH.append(chapter("town-f4", "En ville: Around town", "Town", [TOWN, VENIR]))

REV = topic("review-f4", "Unit 4 summary", f'''<div class="grid2"><div class="mini"><h4>Numbers</h4><p>70 = soixante-dix, 80 = quatre-vingts, 90 = quatre-vingt-dix, 100 = cent, 1000 = mille.</p></div>
<div class="mini"><h4>Time and dates</h4><p>Il est trois heures et quart / et demie / moins le quart. le lundi = on Mondays. le premier mai. en été, au printemps.</p></div>
<div class="mini"><h4>Food</h4><p>du / de la / de l' / des = some. le / la / les after aimer. de after quantities and negatives.</p></div>
<div class="mini"><h4>Town</h4><p>à + le = au, à + les = aux, de + le = du, de + les = des. venir de + place / + infinitive.</p></div></div>''', sub="Everything from this unit on one screen.")
MIS = topic("mistakes-f4", "Common mistakes", '''<ol class="steps">
<li><i>à le</i> and <i>de le</i> never appear: always <i>au</i> and <i>du</i>.</li>
<li>Capitalizing days and months: <i>Lundi</i> → <i>lundi</i> (unless it starts a sentence).</li>
<li><i>le un mai</i> → <i>le premier mai</i>.</li>
<li>Using du after a quantity: <i>beaucoup du sucre</i> → <i>beaucoup de sucre</i>.</li>
<li>Using du after aimer: <i>J'aime du chocolat</i> → <i>J'aime le chocolat</i>.</li>
<li><i>quatre-vingts-un</i> → <i>quatre-vingt-un</i> (the s drops when a number follows).</li>
<li>Weather with être: <i>C'est froid</i> → <i>Il fait froid</i>.</li></ol>''', sub="Points students lose most often.")
CH.append(chapter("review-ch-f4", "Review", "Review", [REV, MIS]))

PQ = [
 q("How do you write 70?", ["soixante-dix", "septante-dix", "soixante et dix", "sept-dix"], 0, "70 = 60 + 10 in France.", "v"),
 q("Which number is <i>quatre-vingt-douze</i>?", ["92", "82", "72", "4202"], 0, "4 × 20 + 12 = 92.", "v"),
 q("How do you write 80?", ["quatre-vingts", "quatre-vingt", "huitante-vingt", "quatre-vingts-zéro"], 0, "80 is quatre-vingts with an s, because nothing follows.", "v"),
 q("How do you write 300?", ["trois cents", "trois cent", "trois-cents", "trois centaines"], 0, "cent takes an s when multiplied and nothing follows.", "v"),
 q(f"{listen('soixante-quatorze')} Which number?", ["74", "64", "94", "84"], 0, "60 + 14 = 74.", "v"),
 q("It's 3:15. <i>Il est trois heures ______.</i>", ["et quart", "et demie", "moins le quart", "quinze et"], 0, "quarter past = et quart.", "v"),
 q("It's 8:45. Which is correct?", ["Il est neuf heures moins le quart.", "Il est huit heures moins le quart.", "Il est huit heures et trois quarts.", "Il est neuf heures et quart."], 0, "After half past, count down from the next hour.", "v"),
 q("It's 12:00 noon.", ["Il est midi.", "Il est minuit.", "Il est douze.", "Il est une heure."], 0, "midi = noon, minuit = midnight.", "v"),
 q("How do you write <i>May 1st</i>?", ["le premier mai", "le un mai", "le 1 Mai", "premier de mai"], 0, "The 1st is le premier; months are lowercase.", "v"),
 q("<i>Le dimanche, je dors tard.</i> means…", ["On Sundays I sleep late.", "This Sunday I'll sleep late.", "Sunday is late.", "I slept late on Sunday."], 0, "le + day = every week.", "v"),
 q("Which season takes <i>au</i>?", ["printemps", "été", "automne", "hiver"], 0, "au printemps; the others use en (en été, en automne, en hiver).", "v"),
 q("<i>Il ______ froid aujourd'hui.</i>", ["fait", "est", "a", "y a"], 0, "Weather: il fait froid.", "v"),
 q("It's raining.", ["Il pleut.", "Il fait pluie.", "Il est pluie.", "Il y a pleut."], 0, "pleuvoir → il pleut.", "v"),
 q("<i>Je voudrais ______ eau, s'il vous plaît.</i>", ["de l'", "du", "de la", "des"], 0, "Partitive before a vowel → de l'.", "g"),
 q("<i>Tu veux ______ confiture ?</i>", ["de la", "du", "de l'", "le"], 0, "confiture is feminine → de la.", "g"),
 q("<i>J'adore ______ fromage.</i>", ["le", "du", "de", "un"], 0, "After adorer (likes), use the definite article.", "g"),
 q("<i>Il mange beaucoup ______ pâtes.</i>", ["de", "des", "du", "les"], 0, "After a quantity, just de.", "g"),
 q("<i>Je ne bois pas ______ café.</i>", ["de", "du", "le", "un"], 0, "After a negative, du → de.", "g"),
 q("<i>Nous allons ______ cinéma.</i>", ["au", "à le", "à la", "du"], 0, "à + le = au.", "g"),
 q("<i>Elle va ______ magasins.</i>", ["aux", "à les", "au", "des"], 0, "à + les = aux.", "g"),
 q("<i>La pharmacie est en face ______ parc.</i>", ["du", "de le", "au", "de"], 0, "en face de + le parc → du parc.", "g"),
 q("<i>Ils ______ du Sénégal.</i> (venir)", ["viennent", "venent", "vient", "venons"], 0, "ils viennent.", "g"),
 q("<i>Je viens de finir mes devoirs</i> means…", ["I just finished my homework.", "I'm going to finish my homework.", "I come from my homework.", "I finish my homework every day."], 0, "venir de + infinitive = just did something.", "g"),
 q("What do you say to get the check?", ["L'addition, s'il vous plaît.", "Le chèque, s'il vous plaît.", "Vous désirez ?", "C'est combien de ?"], 0, "l'addition = the check / bill.", "v"),
]
CHAL = [
 q("Which is correct for 81?", ["quatre-vingt-un", "quatre-vingts-un", "quatre-vingt et un", "huitante et un"], 0, "No et after 80, and the s of vingts drops.", "v"),
 q("<i>Je n'aime pas ______ lait, alors je ne bois jamais ______ lait.</i>", ["le … de", "du … du", "de … le", "le … du"], 0, "aimer → le (stays in the negative); boire + negative → de.", "g"),
 q("It's 23:50 (in conversation).", ["Il est minuit moins dix.", "Il est onze heures moins dix.", "Il est minuit et dix.", "Il est vingt-trois heures moins dix."], 0, "Ten minutes before midnight.", "v"),
 q("Which sentence is correct?", ["Le musée est à côté de l'hôpital et en face du parc.", "Le musée est à côté du l'hôpital et en face de le parc.", "Le musée est à côté de le hôpital et en face du parc.", "Le musée est à côté à l'hôpital et en face au parc."], 0, "de + l' stays de l'; de + le = du.", "g"),
 q("<i>Elle revient ______ États-Unis.</i>", ["des", "de les", "du", "aux"], 0, "de + les États-Unis = des États-Unis.", "g"),
 q("1999 in French:", ["mille neuf cent quatre-vingt-dix-neuf", "mille neuf cents quatre-vingts-dix-neuf", "dix-neuf quatre-vingt-dix-neuf", "mille neuf cent nonante-neuf"], 0, "cent loses its s and vingt loses its s when another number follows.", "v"),
 q("Which uses the partitive correctly?", ["Elle prend de la soupe et du pain.", "Elle prend du soupe et de la pain.", "Elle prend de soupe et de pain.", "Elle prend la soupe et le pain beaucoup."], 0, "soupe is feminine (de la), pain masculine (du).", "g"),
 q("<i>Samedi, je vais à la plage</i> vs <i>Le samedi, je vais à la plage</i>:", ["The first is this Saturday; the second is every Saturday.", "They mean the same thing.", "The first is every Saturday; the second is this Saturday.", "The second is a mistake."], 0, "le + day means a habit.", "v"),
]
EXQ = [
 q("How do you write 95?", ["quatre-vingt-quinze", "quatre-vingts-quinze", "nonante-cinq", "soixante-trente-cinq"], 0, "4 × 20 + 15.", "v", "vocab"),
 q(f"{listen('Il est dix heures et demie.')} What time is it?", ["10:30", "10:15", "9:30", "10:45"], 0, "et demie = half past.", "v", "listen"),
 q("It's 6:40 p.m. (24-hour clock)", ["Il est dix-huit heures quarante.", "Il est six heures quarante du matin.", "Il est seize heures quarante.", "Il est dix-huit heures moins vingt."], 0, "6 p.m. = 18 h.", "v", "vocab"),
 q("Which month is written correctly?", ["août", "Août", "aout", "aôut"], 0, "Lowercase, with a circumflex on the u.", "v", "vocab"),
 q("<i>C'est mon anniversaire ______ 15 mars.</i>", ["le", "en", "au", "à"], 0, "Dates use le.", "g", "gram"),
 q("<i>______ hiver, il neige.</i>", ["En", "Au", "Le", "À"], 0, "en hiver.", "g", "gram"),
 q("<i>Il y a ______ soleil.</i>", ["du", "de la", "le", "un"], 0, "Il y a du soleil (soleil is masculine).", "v", "vocab"),
 q("<i>Je voudrais ______ salade, s'il vous plaît.</i>", ["de la", "du", "des", "le"], 0, "salade is feminine → de la.", "g", "gram"),
 q("<i>Il achète un kilo ______ tomates.</i>", ["de", "des", "du", "les"], 0, "After a quantity: de.", "g", "gram"),
 q("<i>Tu aimes ______ fraises ?</i>", ["les", "des", "de", "du"], 0, "After aimer: les.", "g", "gram"),
 q("<i>On va ______ piscine ?</i>", ["à la", "au", "à l'", "aux"], 0, "piscine is feminine: à la.", "g", "gram"),
 q("<i>Le café est près ______ gare.</i>", ["de la", "du", "à la", "de"], 0, "près de + la gare.", "g", "gram"),
 q("<i>Nous ______ de Montréal.</i> (venir)", ["venons", "viennons", "venez", "viens"], 0, "nous venons.", "g", "gram"),
 q("Read: <i>Aujourd'hui, c'est le mardi 2 avril. Il fait beau mais il fait frais. Ce soir, je vais au restaurant avec ma famille.</i> Which is true?", ["It's nice but cool.", "It's raining.", "It's August.", "The writer is going to the movies."], 0, "Il fait beau mais il fait frais.", "v", "read"),
 q("Which sentence is correct?", ["Je viens de manger un croissant.", "Je viens manger de un croissant.", "Je viens du manger un croissant.", "Je venir de manger un croissant."], 0, "venir de + infinitive: I just ate a croissant.", "g", "gram"),
]
FRQS = [
 {"q": "Write a short plan for a Saturday in town with a friend (at least 5 sentences).",
  "parts": [{"p": "Give the date, the weather, two places you go (with times), and what you eat or drink.",
   "rubric": [["Date with le + number + month (lowercase)", 1], ["A weather expression with il fait / il y a / il pleut", 1], ["Two places with correct à + article (au, à la, à l', aux)", 2], ["Two times told correctly", 1], ["Food or drink with a correct partitive or quantity (du, de la, beaucoup de…)", 1]],
   "answer": f'<div class="ex">{F("Samedi, c\'est le 12 octobre. Il fait beau mais il fait frais. À dix heures, nous allons au musée. À midi et demi, nous mangeons au café : je prends un croque-monsieur et de l\'eau. À trois heures, on va à la bibliothèque.")}<span class="en">Saturday is October 12. It\'s nice but cool. At 10 we go to the museum. At 12:30 we eat at the café: I have a croque-monsieur and water. At 3 we go to the library.</span></div>'}]},
 {"q": "You're at a café in Paris. Write a 4-line dialogue with the server.",
  "parts": [{"p": "Greet the server, order a drink and something to eat politely, and ask for the price or the check.",
   "rubric": [["Polite greeting (Bonjour, monsieur / madame)", 1], ["je voudrais + article", 1], ["Correct gender of the article on food and drink", 1], ["Asks the price or the check (C'est combien ? / L'addition, s'il vous plaît)", 1]],
   "answer": f'<div class="ex">{F("— Bonjour, madame. Vous désirez ?")}<span class="en">Hello. What would you like?</span></div><div class="ex">{F("— Bonjour ! Je voudrais un chocolat chaud et un croissant, s\'il vous plaît.")}<span class="en">Hello! I\'d like a hot chocolate and a croissant, please.</span></div><div class="ex">{F("— Voilà. Et avec ça ?")}<span class="en">Here you go. Anything else?</span></div><div class="ex">{F("— C\'est tout, merci. L\'addition, s\'il vous plaît.")}<span class="en">That\'s all, thanks. The check, please.</span></div>'}]},
]

if __name__ == "__main__":
    build(4, "unit-4", "Everyday life", 'La vie de <span class="hl">tous les jours</span>',
          "Numbers up to 1000, telling time, days, months and dates, the weather, food and the partitive, places in town and the verb venir. Tap any French word to hear it.",
          "French 1 Unit 4: numbers, time, dates, weather, food and places in town, with audio, interactive labs, practice questions and a practice exam.",
          CH, PQ, CHAL, EXQ, FRQS, "/home/claude/ap-physics-study/courses/french-1/unit-4.html")
