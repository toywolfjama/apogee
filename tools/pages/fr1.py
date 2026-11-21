from fr_common import *

CH = []
# ------------------------------------------------------------------ overview
CORE = f'''<p>This course takes you from zero to holding a real conversation in French: greeting people, describing yourself and others, talking about what you do every day, and telling what you did yesterday and what you'll do tomorrow. Every French word on these pages is <b>tappable</b>: tap it to hear it read aloud.</p>
{wa("Your first French sentence", [
 ("s|Je|s  v|suis|v  x|élève|x", "Je = I, suis = am, élève = student. French sentences start like English: subject, then verb.", "I am a student."),
 ("s|Nous|s  v|sommes|v  x|élèves|x", "Change the subject and the verb changes form with it. The s on élèves is silent.", "We are students."),
 ("s|Nous|s  n|ne|n  v|sommes|v  n|pas|n  x|élèves|x", "Negation wraps around the verb: ne … pas. You'll use this in Unit 3.", "We are not students.")])}
<div class="grid2"><div class="mini"><h4>Three things that make French different</h4><p>Every noun is <b>masculine or feminine</b>. Verbs change their ending for each subject. Many final letters are <b>silent</b>.</p></div>
<div class="mini"><h4>How to study</h4><p>Read each topic, tap and repeat every example out loud, play with the labs, then do the Practice and the timed exam. Saying words out loud helps you remember them much better than reading silently.</p></div></div>
<div class="tblwrap"><table><tr><th>Unit</th><th>You'll be able to…</th></tr>
<tr><td>1. Bonjour !</td><td>greet people, spell and pronounce, count to 69, say who you are</td></tr>
<tr><td>2. Les gens et les choses</td><td>use le / la / un / une, describe people, talk about your family, use avoir</td></tr>
<tr><td>3. Au présent</td><td>talk about activities, ask questions, say what you don't do</td></tr>
<tr><td>4. La vie de tous les jours</td><td>tell time, give dates, talk about weather, food and places in town</td></tr>
<tr><td>5. Hier et demain</td><td>say what you did and what you're going to do</td></tr></table></div>'''
CH.append(chapter("overview-f1", "Overview", "Overview", [topic("core-f1", "Bienvenue ! Welcome to French", CORE)]))

# ------------------------------------------------------------------ greetings
GREET = topic("greetings", "Greetings and goodbyes", f'''
<p>French has a <b>formal</b> way and an <b>informal</b> way to say most things. Use the formal one with adults you don't know well, teachers and shopkeepers. Use the informal one with friends, family and people your age.</p>
{vt([("Bonjour !", "Hello / Good morning", "Anytime during the day. Always safe."),
     ("Bonsoir !", "Good evening", "From about 6 p.m."),
     ("Salut !", "Hi! / Bye!", "Informal only. Works for hello and goodbye."),
     ("Au revoir !", "Goodbye", "Polite, always safe."),
     ("À bientôt !", "See you soon"),
     ("À demain !", "See you tomorrow"),
     ("À plus !", "Later!", "Very informal; often written À+"),
     ("Bonne journée !", "Have a good day"),
     ("Bonne nuit !", "Good night", "Only before going to bed.")])}
<h3>How are you?</h3>
{vt([("Comment allez-vous ?", "How are you?", "formal"), ("Comment ça va ? / Ça va ?", "How's it going?", "informal"),
     ("Ça va bien, merci.", "I'm fine, thanks."), ("Très bien !", "Very well!"), ("Pas mal.", "Not bad."),
     ("Comme ci, comme ça.", "So-so."), ("Ça ne va pas.", "Not good."), ("Et toi ? / Et vous ?", "And you?", "toi informal, vous formal")])}
{box("plain", "Culture", "In France people usually say <b>Bonjour</b> when they walk into a shop, and friends often greet each other with <i>la bise</i>, a light kiss on each cheek. Skipping Bonjour comes across as rude.")}
''', pill=("v", "1.1"), sub="Saying hello and goodbye the right way for the situation.",
 det=("Formal vs informal greetings", '''<h4>When in doubt, be formal</h4><p>Bonjour, Au revoir and Comment allez-vous? are never wrong. Salut and Ça va? with a teacher or a stranger sound too casual.</p>
<h4>Ça va is a question and an answer</h4><p>With rising intonation, <i>Ça va ?</i> means "How's it going?". Said flatly, <i>Ça va.</i> means "I'm fine." So a whole conversation can be: — Ça va ? — Ça va, et toi ?</p>
<h4>Spaces before punctuation</h4><p>French puts a space before <b>? ! : ;</b>. That's why you'll see <i>Ça va ?</i> on these pages. It doesn't change the meaning.</p>'''))

INTRO = topic("introductions", "Introducing yourself", f'''
{vt([("Je m'appelle Léa.", "My name is Léa.", "literally: I call myself Léa"),
     ("Comment tu t'appelles ?", "What's your name?", "informal"),
     ("Comment vous appelez-vous ?", "What's your name?", "formal"),
     ("Il s'appelle Hugo.", "His name is Hugo."), ("Elle s'appelle Inès.", "Her name is Inès."),
     ("Enchanté. / Enchantée.", "Nice to meet you.", "add -e if you're female (same sound)"),
     ("Je te présente Paul.", "Let me introduce Paul (to you).", "informal"),
     ("Voici mon amie, Chloé.", "Here's my friend, Chloé."),
     ("J'ai quinze ans.", "I'm 15 years old.", "French uses avoir (to have) for age"),
     ("J'habite à Chicago.", "I live in Chicago.")])}
{wa("A short conversation", [
 ("a|— Salut !|s  b|Je|x  c|m'appelle|v  d|Hugo.|x", "Hugo says hi and gives his name.", "Hi! My name is Hugo."),
 ("a|— Salut !|s  b|Je|x  c|m'appelle|v  d|Hugo.|x  e|Et toi ?|n", "Et toi ? turns the question back to the other person.", "Hi! My name is Hugo. And you?"),
 ("f|— Moi,|s  b|je|x  c|m'appelle|v  g|Léa.|x  h|Enchantée !|n", "Léa answers. Moi adds emphasis: me, I'm Léa. She's female, so she writes enchantée.", "Me, I'm Léa. Nice to meet you!")])}
<h3>Polite words</h3>
{vgrid([("s'il te plaît", "please (informal)"), ("s'il vous plaît", "please (formal)"), ("merci (beaucoup)", "thank you (very much)"), ("de rien", "you're welcome"), ("pardon", "sorry / excuse me"), ("excusez-moi", "excuse me (formal)"), ("oui / non", "yes / no"), ("monsieur / madame", "sir / ma'am")])}
{worked("How do you ask a new adult teacher her name, and then say yours (Sam)?", f'''Use the formal question: {F("Comment vous appelez-vous ?")} Then answer: {F("Je m'appelle Sam.")} With a classmate you'd say {F("Comment tu t'appelles ?")}''')}
''', pill=("v", "1.2"), sub="Names, age, where you live and basic politeness.")

TUVOUS = topic("tu-vous", "Tu or vous?", f'''
<p>English has one word for <i>you</i>. French has two.</p>
<div class="grid2"><div class="mini"><h4>{F("tu")}</h4><p>One person you know well: a friend, a family member, a classmate, a child, a pet.</p></div>
<div class="mini"><h4>{F("vous")}</h4><p>(1) One person you should be polite to: a teacher, a stranger, an older adult. (2) <b>Any</b> group of two or more people, formal or not.</p></div></div>
{ex("Tu es fatigué, Max ?", "Are you tired, Max? (a friend)")}
{ex("Vous êtes prêts, les amis ?", "Are you ready, guys? (a group of friends: vous because it's plural)")}
{ex("Vous êtes Madame Martin ?", "Are you Mrs. Martin? (an adult you don't know)")}
{box("trap", "Common mistake", "Using <b>tu</b> for a group. Talking to two friends at once, you must say <b>vous</b>.")}
''', pill=("g", "1.3"), sub="Choosing the right word for you.")
CH.append(chapter("hello-f1", "Salut ! Greetings", "Greetings", [GREET, INTRO, TUVOUS]))

# ------------------------------------------------------------------ sounds
ALPHA = [("A", "ah"), ("B", "bay"), ("C", "say"), ("D", "day"), ("E", "uh"), ("F", "eff"), ("G", "zhay"), ("H", "ahsh"), ("I", "ee"), ("J", "zhee"), ("K", "kah"), ("L", "ell"), ("M", "em"), ("N", "en"), ("O", "oh"), ("P", "pay"), ("Q", "kü"), ("R", "air"), ("S", "ess"), ("T", "tay"), ("U", "ü"), ("V", "vay"), ("W", "doo-bluh-vay"), ("X", "eeks"), ("Y", "ee-grek"), ("Z", "zed")]
ABC = topic("alphabet", "The alphabet", f'''
<p>The letters are the same as English, but their names are different. Tap each letter to hear it. The ones that trip people up are <b>E</b> (uh), <b>I</b> (ee), <b>G</b> (zhay) and <b>J</b> (zhee), because they feel "swapped" compared to English.</p>
<div class="abc">{"".join(f'<button type="button" class="abc-l" data-say="{l.lower()}"><b>{l}</b><span>{s}</span></button>' for l, s in ALPHA)}</div>
<h3>Spelling out loud</h3>
{vt([("Comment ça s'écrit ?", "How is that spelled?"), ("Ça s'écrit P-A-U-L.", "It's spelled P-A-U-L."), ("deux L", "double L (literally: two L's)")])}
''', pill=("v", "1.4"), sub="Letter names, so you can spell your name.")

ACC = topic("accents", "Accents and special letters", f'''
<p>Accents are part of the spelling. Leaving one off is a spelling mistake, and sometimes it changes the word.</p>
<div class="tblwrap"><table><tr><th>Mark</th><th>Name</th><th>What it does</th><th>Examples</th></tr>
<tr><td><b>é</b></td><td>accent aigu</td><td>sounds like "ay"</td><td>{F("café")}, {F("été")}, {F("élève")}</td></tr>
<tr><td><b>è</b></td><td>accent grave</td><td>sounds like the e in "bet"</td><td>{F("mère")}, {F("très")}</td></tr>
<tr><td><b>à ù</b></td><td>accent grave</td><td>no sound change; tells two words apart</td><td>{F("à")} (to) vs {F("a")} (has), {F("où")} (where) vs {F("ou")} (or)</td></tr>
<tr><td><b>ê â î ô û</b></td><td>accent circonflexe</td><td>often marks a lost s (compare English)</td><td>{F("forêt")} (forest), {F("hôpital")} (hospital), {F("fête")} (feast)</td></tr>
<tr><td><b>ç</b></td><td>cédille</td><td>makes c sound like s before a, o, u</td><td>{F("ça")}, {F("français")}, {F("garçon")}</td></tr>
<tr><td><b>ë ï</b></td><td>tréma</td><td>says the vowel separately</td><td>{F("Noël")}, {F("naïf")}</td></tr></table></div>
''', pill=("v", "1.5"), sub="What each accent mark means.")

SILENT = topic("silent", "Silent letters, liaison and elision", f'''
<p>Most final consonants are <b>silent</b>: {F("petit")}, {F("Paris")}, {F("vous")}, {F("ils parlent")} (the -ent is silent too). The exceptions are usually <b>C, R, F, L</b>; think "CaReFuL": {F("avec")}, {F("bonjour")}, {F("neuf")}, {F("hôtel")}. (Most -er endings are an exception to the exception: {F("parler")} ends in an "ay" sound.)</p>
<h3>Elision: dropping a vowel</h3>
<p>Short words like <b>je, le, la, de, ne, me, te, se</b> drop their vowel and take an apostrophe before a word starting with a vowel or a silent h.</p>
{wa("Elision", [
 ("a|le|x  b|ami|v", "le + ami: two vowels bump into each other…", "the friend"),
 ("a|l'|x  b|ami|v", "…so le loses its e: l'ami.", "the friend"),
 ("c|je|x  d|aime|v", "Same with je + aime…", "I like"),
 ("c|j'|x  d|aime|v", "…which becomes j'aime.", "I like"),
 ("e|la|x  f|heure|v", "A silent h counts as a vowel.", "the hour"),
 ("e|l'|x  f|heure|v", "l'heure.", "the hour")])}
<h3>Liaison: linking words</h3>
<p>A normally silent final consonant is pronounced when the next word starts with a vowel sound, and it links to that word. A final <b>s</b> or <b>x</b> sounds like <b>z</b>.</p>
{ex("les‿amis", "the friends: say lay-za-mee")}
{ex("vous‿êtes", "you are: say voo-zet")}
{ex("un petit‿enfant", "a small child: the t links")}
{box("plain", "Nasal vowels", f"A vowel followed by n or m in the same syllable is often nasal: air goes through your nose and the n isn't fully pronounced. Listen: {F('bon')}, {F('vin')}, {F('blanc')}, {F('un')}.")}
''', pill=("g", "1.6"), sub="Why French sounds the way it does.",
 det=("Pronunciation rules that cover most words", '''<h4>Final e</h4><p>A final unaccented e is silent (<i>table, belle</i>), but it makes the consonant before it pronounced: <i>petit</i> (silent t) vs <i>petite</i> (you hear the t). That's how you often <b>hear</b> the feminine form.</p>
<h4>Useful letter combinations</h4><p><b>ou</b> = "oo" (vous), <b>oi</b> = "wa" (moi), <b>au / eau</b> = "oh" (beau), <b>ai</b> = "eh" (lait), <b>ch</b> = "sh" (chat), <b>gn</b> = "ny" (montagne), <b>qu</b> = "k" (qui), <b>th</b> = "t" (thé).</p>
<h4>The French u and r</h4><p>For <b>u</b>, say "ee" with your lips rounded like for "oo". The <b>r</b> is made in the back of the throat, close to a gentle gargle.</p>
<h4>When not to link</h4><p>Never make a liaison after <i>et</i> (and): <i>un garçon et‿une fille</i> is wrong; say et / une separately. Some words starting with h (called "h aspiré"), like <i>le héros</i>, block both liaison and elision.</p>'''))
CH.append(chapter("sounds-f1", "Les sons: Sounds and spelling", "Sounds", [ABC, ACC, SILENT]))

# ------------------------------------------------------------------ numbers
NUMS = topic("numbers-0-69", "Numbers 0 to 69", f'''
{vgrid([("zéro", "0"), ("un", "1"), ("deux", "2"), ("trois", "3"), ("quatre", "4"), ("cinq", "5"), ("six", "6"), ("sept", "7"), ("huit", "8"), ("neuf", "9"), ("dix", "10"), ("onze", "11"), ("douze", "12"), ("treize", "13"), ("quatorze", "14"), ("quinze", "15"), ("seize", "16"), ("dix-sept", "17"), ("dix-huit", "18"), ("dix-neuf", "19")])}
<h3>Tens</h3>
{vgrid([("vingt", "20"), ("trente", "30"), ("quarante", "40"), ("cinquante", "50"), ("soixante", "60")])}
<p>From 20 to 69 the pattern is regular: tens + hyphen + ones, like {F("vingt-deux")} (22) or {F("quarante-sept")} (47). The only twist: <b>21, 31, 41, 51, 61 use "et un"</b> with no hyphen: {F("vingt et un")}, {F("trente et un")}.</p>
{lab(type="num", n=21, max=69)}
<h3>Using numbers</h3>
{ex("J'ai seize ans.", "I'm sixteen. (literally: I have sixteen years)")}
{ex("Il y a trente élèves.", "There are thirty students.")}
{ex("Mon numéro, c'est le 06 12 45 33 21.", "My number is 06 12 45 33 21. French phone numbers are read in pairs: zéro six, douze, quarante-cinq…")}
{box("trap", "Common mistake", "Don't say <i>je suis quinze</i> for your age. Use avoir: <b>J'ai quinze ans</b>. And keep the word <b>ans</b>.")}
''', pill=("v", "1.7"), sub="Counting, age and phone numbers. Numbers 70 and up come in Unit 4.",
 det=("Number details", '''<h4>Pronunciation changes</h4><p><i>six</i> and <i>dix</i> end in an s sound alone ("sees", "dees"), are silent before a consonant (<i>six livres</i>, "see"), and sound like z before a vowel (<i>six‿ans</i>, "see-zahn"). <i>huit</i> loses its t before a consonant. <i>neuf ans</i> sounds like "neuv‿ahn".</p>
<h4>Un vs une</h4><p>One is <i>un</i> before a masculine noun and <i>une</i> before a feminine one: <i>un livre</i>, <i>une table</i>. The same goes for 21, 31…: <i>vingt et une filles</i>.</p>
<h4>Seventeen to nineteen</h4><p>They are built like "ten-seven": <i>dix-sept</i>, <i>dix-huit</i>, <i>dix-neuf</i>. This "adding" idea comes back in a big way with 70–99.</p>'''))
CH.append(chapter("numbers-f1", "Les nombres: Numbers 0–69", "Numbers", [NUMS]))

# ------------------------------------------------------------------ pronouns and être
PRON = topic("pronouns", "Subject pronouns", f'''
<div class="tblwrap"><table><tr><th></th><th>Singular</th><th>Plural</th></tr>
<tr><td>1st</td><td>{F("je")} (I)</td><td>{F("nous")} (we)</td></tr>
<tr><td>2nd</td><td>{F("tu")} (you, informal)</td><td>{F("vous")} (you, formal or plural)</td></tr>
<tr><td>3rd</td><td>{F("il")} (he / it), {F("elle")} (she / it), {F("on")} (one, we, people)</td><td>{F("ils")} (they, masculine or mixed), {F("elles")} (they, all feminine)</td></tr></table></div>
<ul><li><b>il / elle</b> also mean <i>it</i>: use il for a masculine thing and elle for a feminine one. {F("La voiture ? Elle est rouge.")} (The car? It's red.)</li>
<li><b>ils</b> is used for any group with at least one masculine person or noun, even ten girls and one boy. <b>elles</b> is only for all-feminine groups.</li>
<li><b>on</b> is used all the time in speech to mean <i>we</i>: {F("On va au cinéma ?")} (Are we going to the movies?). It takes the same verb form as il.</li></ul>
''', pill=("g", "1.8"), sub="I, you, he, she, we, they.")

ETRE = topic("etre", "Être: to be", f'''
<p>{F("être")} is the most important irregular verb in French. Learn it by heart, out loud.</p>
<div class="tblwrap"><table class="conj"><tr><td>{F("je suis")}</td><td>I am</td><td>{F("nous sommes")}</td><td>we are</td></tr>
<tr><td>{F("tu es")}</td><td>you are</td><td>{F("vous êtes")}</td><td>you are</td></tr>
<tr><td>{F("il / elle / on est")}</td><td>he / she / one is</td><td>{F("ils / elles sont")}</td><td>they are</td></tr></table></div>
{wa("Être changes with the subject", [
 ("s|Je|s  v|suis|v  x|américain.|x", "je → suis", "I'm American."),
 ("s|Elle|s  v|est|v  x|américaine.|x", "elle → est. Adjectives also add -e for a female subject.", "She's American."),
 ("s|Vous|s  v|êtes|v  x|américains.|x", "vous → êtes, with a liaison: vous‿êtes.", "You're Americans."),
 ("s|Ils|s  v|sont|v  x|américains.|x", "ils → sont. Careful: sont (are) and son (his) sound different.", "They're American.")])}
{lab(type="conj", verbs=["être"], tenses=["pres"])}
<h3>What you can say with être</h3>
{ex("Je suis de Chicago.", "I'm from Chicago. (être de + city)")}
{ex("Nous sommes en classe.", "We're in class.")}
{ex("Tu es sympa !", "You're nice!")}
{ex("Elles sont canadiennes.", "They're Canadian (all women).")}
<h3>C'est vs il est</h3>
<p>Use {F("c'est")} (it is / that is / he is / she is) before a name or a word with an article: {F("C'est Marc.")}, {F("C'est un ami.")}, {F("C'est une bonne idée.")}. Use {F("il est / elle est")} before an adjective alone or a job with no article: {F("Il est grand.")}, {F("Elle est professeur.")}</p>
''', pill=("g", "1.9"), sub="The verb you'll use in almost every conversation.",
 det=("Être in detail", '''<h4>Nationalities and jobs</h4><p>Nationalities are lowercase in French when they're adjectives: <i>Il est français.</i> They take capital letters only as nouns: <i>un Français</i> (a Frenchman). After être, jobs usually have no article: <i>Je suis étudiant</i> (not "un étudiant").</p>
<h4>Where are you from?</h4><p><i>Tu es d'où ?</i> or formally <i>D'où êtes-vous ?</i> Answer with <i>Je suis de…</i>; de becomes d' before a vowel: <i>Je suis d'Atlanta.</i></p>
<h4>C'est with plurals</h4><p>For plurals, c'est becomes <i>ce sont</i>: <i>Ce sont mes amis.</i> In everyday speech many people still say c'est.</p>'''))
CH.append(chapter("etre-f1", "Je suis…: Pronouns and être", "Être", [PRON, ETRE]))

# ------------------------------------------------------------------ review
REV = topic("review-f1", "Unit 1 summary", f'''
<div class="grid2"><div class="mini"><h4>Greetings</h4><p>{F("Bonjour")} / {F("Salut")} / {F("Au revoir")} / {F("À bientôt")}. {F("Ça va ?")} — {F("Ça va bien, merci. Et toi ?")}</p></div>
<div class="mini"><h4>Introductions</h4><p>{F("Je m'appelle…")} {F("J'ai … ans.")} {F("J'habite à…")} {F("Enchanté(e).")}</p></div>
<div class="mini"><h4>Sounds</h4><p>Final consonants are usually silent (except C, R, F, L). Elision: le + ami → l'ami. Liaison: les‿amis.</p></div>
<div class="mini"><h4>Être</h4><p>je suis, tu es, il est, nous sommes, vous êtes, ils sont. Age uses avoir: j'ai quinze ans.</p></div></div>''', sub="Everything from this unit on one screen.")
MIS = topic("mistakes-f1", "Common mistakes", '''<ol class="steps">
<li>Saying <i>Salut</i> or <i>Ça va ?</i> to a teacher or stranger. Use <i>Bonjour</i> and <i>Comment allez-vous ?</i></li>
<li>Using <i>tu</i> for a group of people. Any group is <i>vous</i>.</li>
<li>Age with être: <i>Je suis 15</i> is wrong. Say <i>J'ai quinze ans</i>.</li>
<li>Forgetting elision: <i>je aime</i>, <i>le ami</i>. Write <i>j'aime</i>, <i>l'ami</i>.</li>
<li>Pronouncing final letters: <i>Paris</i> has no s sound, <i>ils parlent</i> sounds like <i>il parle</i>.</li>
<li>Mixing up <i>il est</i> and <i>c'est</i>: <i>C'est un ami</i> but <i>Il est sympa</i>.</li>
<li>Forgetting <i>et</i> in 21, 31, 41, 51, 61: <i>vingt et un</i>, not <i>vingt-un</i>.</li></ol>''', sub="Points students lose most often.")
CH.append(chapter("review-ch-f1", "Review", "Review", [REV, MIS]))

# ------------------------------------------------------------------ questions
PQ = [
 q("You walk into a bakery in Paris at 10 a.m. What do you say first?", ["Bonjour, madame.", "Salut !", "Bonsoir !", "Bonne nuit !"], 0, "Bonjour is the polite greeting for the daytime; it's expected when you enter a shop.", "v"),
 q("Which greeting is <b>informal</b> only?", ["Salut !", "Bonjour !", "Au revoir !", "Bonsoir !"], 0, "Salut is for friends; the others are polite with anyone.", "v"),
 q("A friend asks <i>Ça va ?</i> Which answer fits?", ["Ça va bien, merci. Et toi ?", "Je m'appelle Paul.", "J'ai quinze ans.", "De rien."], 0, "Ça va ? asks how you are. Et toi ? is the informal 'and you?'.", "v"),
 q("How do you ask a new teacher's name?", ["Comment vous appelez-vous ?", "Comment tu t'appelles ?", "Tu t'appelles comment, toi ?", "Ça va ?"], 0, "With an adult you don't know, use the formal vous form.", "v"),
 q("Which means <i>See you tomorrow</i>?", ["À demain !", "À bientôt !", "Bonne journée !", "À plus !"], 0, "demain = tomorrow. À bientôt = see you soon.", "v"),
 q("Complete: <i>— Merci beaucoup ! — ______</i>", ["De rien.", "Pardon.", "S'il vous plaît.", "Enchanté."], 0, "De rien = you're welcome.", "v"),
 q("You're talking to <b>two</b> friends. Which word for <i>you</i>?", ["vous", "tu", "toi", "on"], 0, "Any group of two or more takes vous, even friends.", "g"),
 q("A girl is introduced to someone. How does she write <i>nice to meet you</i>?", ["Enchantée.", "Enchanté.", "Enchantés.", "Enchantées."], 0, "She adds -e because she is female. It sounds the same.", "g"),
 q("How do you say <i>I'm fourteen</i>?", ["J'ai quatorze ans.", "Je suis quatorze.", "Je suis quatorze ans.", "J'ai quatorze."], 0, "Age uses avoir + number + ans.", "g"),
 q("Which number is <b>quarante-huit</b>?", ["48", "38", "58", "84"], 0, "quarante = 40, huit = 8.", "v"),
 q("How do you write 31?", ["trente et un", "trente-un", "treize-un", "trois-dix-un"], 0, "21, 31, 41, 51 and 61 use et un with no hyphens.", "v"),
 q(f"{listen('soixante-cinq')} Which number do you hear?", ["65", "56", "75", "45"], 0, "soixante = 60, cinq = 5.", "v"),
 q("What is 12 + 4? (in French)", ["seize", "quatorze", "treize", "dix-six"], 0, "16 is seize. Only 17, 18 and 19 are built as dix-…", "v"),
 q("Choose the correct form: <i>Nous ______ en classe.</i>", ["sommes", "sont", "êtes", "suis"], 0, "nous → sommes.", "g"),
 q("Choose the correct form: <i>Vous ______ de Paris ?</i>", ["êtes", "est", "es", "sommes"], 0, "vous → êtes.", "g"),
 q("Choose the correct form: <i>Marc et Julie ______ canadiens.</i>", ["sont", "est", "sommes", "son"], 0, "Two people = ils → sont. son means 'his'.", "g"),
 q("Which pronoun replaces <i>Marie et Paul</i>?", ["ils", "elles", "il", "nous"], 0, "A mixed group takes ils.", "g"),
 q("Which pronoun replaces <i>la voiture</i> (the car, feminine)?", ["elle", "il", "on", "la"], 0, "For things, use the pronoun that matches the noun's gender: feminine → elle.", "g"),
 q("Which is spelled correctly?", ["J'aime le chocolat.", "Je aime le chocolat.", "Jaime le chocolat.", "J' aime le chocolat."], 0, "je + aime → j'aime (elision with an apostrophe, no space).", "g"),
 q("In which word is the final consonant pronounced?", ["avec", "petit", "Paris", "vous"], 0, "C, R, F and L are often pronounced at the end (CaReFuL). The others are silent.", "g"),
 q("What does the cédille (ç) do in <i>garçon</i>?", ["Makes the c sound like s", "Makes the c sound like k", "Makes the c silent", "Shows the word is feminine"], 0, "Before a, o or u, c sounds like k; ç keeps the s sound.", "g"),
 q("Choose the best sentence.", ["C'est un ami.", "Il est un ami.", "Elle est un ami.", "C'est ami."], 0, "Before a noun with an article, use c'est.", "g"),
 q("Choose the best sentence about Paul.", ["Il est sympa.", "C'est sympa Paul.", "Il est un sympa.", "C'est un sympa."], 0, "Before an adjective alone describing a person, use il est / elle est.", "g"),
 q("<i>Comment ça s'écrit ?</i> means…", ["How is that spelled?", "How are you?", "What's your name?", "How old are you?"], 0, "s'écrire = to be written.", "v"),
]
CHAL = [
 q("Which sentence uses <b>tu</b> correctly?", ["Maman, tu es fatiguée ?", "Monsieur, tu es le directeur ?", "Les amis, tu es prêts ?", "Madame Petit, tu es professeur ?"], 0, "Tu is for one person you know well, like a parent. A group or a polite adult takes vous.", "g"),
 q("Which pair of words is pronounced with a liaison (a z sound)?", ["les amis", "les garçons", "et une", "vous parlez"], 0, "The s of les links to the vowel of amis: lay-za-mee. Never link after et.", "g"),
 q("Which number is written correctly?", ["soixante et un", "soixante-et-un", "soixante-un", "six-dix-un"], 0, "61 = soixante et un, with no hyphens around et.", "v"),
 q("How many words in this sentence have a silent final letter? <i>Les petits chats sont gris.</i>", ["All five", "Two", "Three", "None"], 0, "Les, petits, chats, sont, gris: every final s or t is silent here.", "g"),
 q(f"{listen('Elles sont de Montréal.')} What did you hear?", ["Elles sont de Montréal.", "Elle est de Montréal.", "Elles sont à Montréal.", "Il sont de Montréal."], 0, "sont (plural) sounds different from est. Elle and elles sound the same, so the verb tells you it's plural.", "v"),
 q("Pick the sentence with <b>no</b> mistakes.", ["Vous êtes de Chicago, monsieur ?", "Vous es de Chicago, monsieur ?", "Tu êtes de Chicago, monsieur ?", "Vous êtes du Chicago, monsieur ?"], 0, "vous → êtes, and de + city.", "g"),
 q("Which response does <b>not</b> answer <i>Comment allez-vous ?</i>", ["Je m'appelle Anne.", "Très bien, merci.", "Pas mal, et vous ?", "Comme ci, comme ça."], 0, "Je m'appelle gives a name; the question asks how you are.", "v"),
 q("What is 35 + 26 in French?", ["soixante et un", "cinquante et un", "soixante-deux", "soixante-un"], 0, "35 + 26 = 61 = soixante et un.", "v"),
]
EXQ = [
 q("It's 8 p.m. You arrive at a dinner with your friend's parents. You say:", ["Bonsoir, monsieur. Bonsoir, madame.", "Salut !", "Bonne nuit !", "À plus !"], 0, "Bonsoir is the evening greeting; with adults, add monsieur / madame.", "v", "vocab"),
 q("Which is the formal way to say <i>please</i>?", ["s'il vous plaît", "s'il te plaît", "merci", "de rien"], 0, "vous = formal, te = informal.", "v", "vocab"),
 q("<i>Je te présente Lucas.</i> What is happening?", ["Someone introduces Lucas to a friend.", "Someone says goodbye to Lucas.", "Someone asks Lucas's age.", "Someone thanks Lucas."], 0, "présenter = to introduce.", "v", "read"),
 q("How do you write 17?", ["dix-sept", "sept-dix", "dix sept", "dixsept"], 0, "17 = dix-sept with a hyphen.", "v", "vocab"),
 q(f"{listen('cinquante-trois')} Which number?", ["53", "43", "63", "35"], 0, "cinquante = 50, trois = 3.", "v", "listen"),
 q("<i>Tu ______ sympa.</i>", ["es", "est", "êtes", "suis"], 0, "tu → es.", "g", "gram"),
 q("<i>Je ______ de Boston.</i>", ["suis", "es", "est", "sommes"], 0, "je → suis.", "g", "gram"),
 q("<i>On ______ en retard !</i> (We're late!)", ["est", "sommes", "sont", "es"], 0, "on takes the il / elle form, even when it means we.", "g", "gram"),
 q("Which pronoun replaces <i>Sophie et Claire</i>?", ["elles", "ils", "elle", "vous"], 0, "Only women → elles.", "g", "gram"),
 q("Which is correct?", ["J'habite à Dallas.", "Je habite à Dallas.", "J'habite Dallas à.", "Je habite Dallas."], 0, "habiter starts with a silent h, so je → j'.", "g", "gram"),
 q("Which sentence is correct?", ["C'est une amie.", "Elle est une amie.", "C'est amie.", "Il est une amie."], 0, "c'est + article + noun.", "g", "gram"),
 q("<i>— Ça va ? — Comme ci, comme ça.</i> How does the person feel?", ["So-so", "Great", "Terrible", "Tired"], 0, "Comme ci, comme ça = so-so.", "v", "read"),
 q("Which accent can change the meaning of a word?", ["The grave accent in à / a", "The accent in café", "The cédille in ça", "None of them"], 0, "a = has, à = to / at. Same letters, different words.", "g", "gram"),
 q("In which phrase do you hear a liaison?", ["vous êtes", "vous parlez", "nous sommes", "tu es"], 0, "vous before a vowel: voo-zet.", "g", "gram"),
 q("Read: <i>Bonjour ! Je m'appelle Karim. J'ai seize ans et j'habite à Lyon. Je suis français.</i> Which is true?", ["Karim is 16 and lives in Lyon.", "Karim is 6 and lives in Paris.", "Karim is Canadian.", "Karim is 60."], 0, "seize = 16, j'habite à Lyon = I live in Lyon.", "v", "read"),
]
FRQS = [
 {"q": "Write a short introduction of yourself (at least 4 sentences) for a new French pen pal.",
  "parts": [{"p": "Include a greeting, your name, your age, where you live, and a goodbye.",
   "rubric": [["Appropriate greeting and goodbye (e.g. Salut / Bonjour, À bientôt)", 1], ["Name with je m'appelle", 1], ["Age with j'ai … ans, number spelled correctly", 1], ["Where you live with j'habite à … (elision j')", 1], ["Spelling and accents mostly correct", 1]],
   "answer": f'<div class="ex">{F("Salut ! Je m\'appelle Sam. J\'ai quinze ans. J\'habite à Denver, aux États-Unis. Je suis américain. À bientôt !")}<span class="en">Hi! My name is Sam. I\'m 15. I live in Denver, in the United States. I\'m American. See you soon!</span></div>'}]},
 {"q": "Complete the dialogue between a student (Inès) and a new teacher (Monsieur Durand). Write 4 lines, two for each person.",
  "parts": [{"p": "The teacher greets Inès and asks her name formally; she answers politely and asks how he is.",
   "rubric": [["Formal greeting from both (Bonjour, monsieur…)", 1], ["Formal name question: Comment vous appelez-vous ? / Vous vous appelez comment ?", 1], ["Inès uses vous with the teacher, not tu", 1], ["Correct answer to how are you (Très bien, merci…)", 1]],
   "answer": f'<div class="ex">{F("— Bonjour ! Comment vous appelez-vous ?")}<span class="en">Hello! What is your name?</span></div><div class="ex">{F("— Bonjour, monsieur. Je m\'appelle Inès. Comment allez-vous ?")}<span class="en">Hello, sir. My name is Inès. How are you?</span></div><div class="ex">{F("— Très bien, merci. Enchanté, Inès.")}<span class="en">Very well, thank you. Nice to meet you, Inès.</span></div><div class="ex">{F("— Enchantée, monsieur.")}<span class="en">Nice to meet you, sir.</span></div>'}]},
]

if __name__ == "__main__":
    build(1, "unit-1", "Bonjour !", 'Bonjour&nbsp;! <span class="hl">Les bases</span>',
          "Greetings and introductions, the sounds of French, numbers 0–69, subject pronouns and the verb être. Tap any French word to hear it, play with the labs, then test yourself.",
          "French 1 Unit 1: greetings, pronunciation, numbers and être, with audio, interactive labs, practice questions and a practice exam.",
          CH, PQ, CHAL, EXQ, FRQS, "/home/claude/ap-physics-study/courses/french-1/unit-1.html")
