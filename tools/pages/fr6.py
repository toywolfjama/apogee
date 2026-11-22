from fr_common import *

CH = []
CORE = f'''<p>This unit is about <b>home</b>: the rooms and furniture, saying where things are, chores, and telling people what to do. You'll also learn the <b>imperative</b>, the verb form for commands and instructions.</p>
{wa("From statement to command", [
 ("s|Tu|s  v|ranges|v  r|ta chambre.|x", "A statement: you tidy your room.", "You tidy your room."),
 ("v|Ranges|v  r|ta chambre !|x", "Drop the subject tu…", ""),
 ("v|Range|v  r|ta chambre !|x", "…and for -er verbs, drop the s too. That's a command.", "Tidy your room!")])}
<div class="grid2"><div class="mini"><h4>In this unit</h4><p>Rooms and furniture · prepositions of place (sur, sous, devant…) · chez · chores with faire · the imperative · commands with reflexive verbs.</p></div>
<div class="mini"><h4>Practice idea</h4><p>Walk through your home and name everything out loud with its article: {F("le lit")}, {F("la lampe")}, {F("l'armoire")}.</p></div></div>'''
CH.append(chapter("overview-f6", "Overview", "Overview", [topic("core-f6", "À la maison", CORE)]))

ROOMS = topic("rooms", "Rooms and furniture", f'''
<h3>Les pièces: rooms</h3>
{vgrid([("la maison", "house"), ("l'appartement (m.)", "apartment"), ("la chambre", "bedroom"), ("le salon", "living room"), ("la cuisine", "kitchen"), ("la salle à manger", "dining room"), ("la salle de bains", "bathroom"), ("les toilettes (f.)", "restroom, toilet"), ("le bureau", "office, study"), ("le garage", "garage"), ("le jardin", "yard, garden"), ("l'escalier (m.)", "stairs"), ("le rez-de-chaussée", "ground floor"), ("le premier étage", "second floor (US)")])}
<h3>Les meubles: furniture</h3>
{vgrid([("le lit", "bed"), ("la table", "table"), ("la chaise", "chair"), ("le canapé", "sofa"), ("le fauteuil", "armchair"), ("l'armoire (f.)", "wardrobe"), ("le placard", "closet, cupboard"), ("l'étagère (f.)", "shelf"), ("la lampe", "lamp"), ("le tapis", "rug"), ("le miroir", "mirror"), ("le bureau", "desk"), ("le frigo", "fridge"), ("le four", "oven"), ("la fenêtre", "window"), ("la porte", "door"), ("le mur", "wall")])}
{lab(type="noun", rows=[0, 1, 5, 6], nouns=["chambre", "salon", "cuisine", "lit", "armoire", "fauteuil", "lampe", "appartement", "maison", "ordinateur"])}
{box("plain", "Floors", "In France, the ground floor is <b>le rez-de-chaussée</b>, and <b>le premier étage</b> is one floor up (the American second floor). An elevator button marked 1 takes you up one level.")}
{ex("Chez moi, il y a trois chambres et une grande cuisine.", "At my place there are three bedrooms and a big kitchen.")}
''', pill=("v", "6.1"), sub="Les pièces et les meubles.")

PREP = topic("place", "Saying where things are", f'''
{lab(type="prep")}
{vt([("sur", "on"), ("sous", "under"), ("dans", "in, inside"), ("devant", "in front of"), ("derrière", "behind"), ("entre … et …", "between … and …"), ("à côté de", "next to"), ("en face de", "across from, facing"), ("près de", "near"), ("loin de", "far from"), ("à gauche de / à droite de", "to the left of / to the right of"), ("au-dessus de / au-dessous de", "above / below")])}
<p>Prepositions that end in <b>de</b> combine with le and les: {F("à côté du lit")} (de + le), {F("près des fenêtres")} (de + les), but {F("à côté de la porte")} and {F("près de l'armoire")} stay the same.</p>
<h3>Chez</h3>
<p>{F("chez")} + a person means <i>at / to someone's place</i>. Use stress pronouns after it: {F("chez moi")}, {F("chez toi")}, {F("chez lui")}, {F("chez elle")}, {F("chez nous")}, {F("chez vous")}, {F("chez eux")}.</p>
{ex("On va chez Marie ce soir ?", "Are we going to Marie's tonight?")}
{ex("Je rentre chez moi.", "I'm going home.")}
''', pill=("g", "6.2"), sub="sur, sous, devant, derrière… and chez.")
CH.append(chapter("home-f6", "La maison: Rooms", "Rooms", [ROOMS, PREP]))

CHORES = topic("chores", "Chores", f'''
{vt([("faire le ménage", "to clean the house"), ("faire la vaisselle", "to do the dishes"), ("faire la lessive", "to do the laundry"), ("faire son lit", "to make your bed"), ("faire la cuisine", "to cook"), ("faire les courses", "to do the grocery shopping"), ("ranger sa chambre", "to tidy your room"), ("passer l'aspirateur", "to vacuum"), ("mettre la table", "to set the table"), ("débarrasser la table", "to clear the table"), ("sortir la poubelle", "to take out the trash"), ("promener le chien", "to walk the dog"), ("arroser les plantes", "to water the plants")])}
<p>Notice how many chores use {F("faire")}. Use a possessive that matches the person: {F("Je fais mon lit")}, {F("Tu fais ton lit")}, {F("Il fait son lit")}.</p>
{ex("Le samedi, je fais la vaisselle et mon frère passe l'aspirateur.", "On Saturdays I do the dishes and my brother vacuums.")}
{ex("Je déteste faire la lessive !", "I hate doing laundry!")}
{ex("Qui sort la poubelle ce soir ?", "Who's taking out the trash tonight?")}
''', pill=("v", "6.3"), sub="Les tâches ménagères.")

IMP = topic("imperative", "The imperative: giving commands", f'''
<p>The imperative has only three forms: <b>tu</b>, <b>nous</b> (let's…) and <b>vous</b>. Take the present tense and drop the subject.</p>
<div class="tblwrap"><table><tr><th></th><th>-er: ranger</th><th>-ir: finir</th><th>-re: attendre</th></tr>
<tr><td>(tu)</td><td>{F("Range !")}</td><td>{F("Finis !")}</td><td>{F("Attends !")}</td></tr>
<tr><td>(nous)</td><td>{F("Rangeons !")}</td><td>{F("Finissons !")}</td><td>{F("Attendons !")}</td></tr>
<tr><td>(vous)</td><td>{F("Rangez !")}</td><td>{F("Finissez !")}</td><td>{F("Attendez !")}</td></tr></table></div>
<p>The only trick: <b>-er verbs</b> (and aller) drop the final s in the tu form: {F("tu ranges → Range !")}, {F("tu vas → Va !")}</p>
<h3>Four irregulars</h3>
<div class="tblwrap"><table><tr><th></th><th>être</th><th>avoir</th><th>savoir</th><th>vouloir</th></tr>
<tr><td>(tu)</td><td>{F("sois")}</td><td>{F("aie")}</td><td>{F("sache")}</td><td>{F("veuille")}</td></tr>
<tr><td>(nous)</td><td>{F("soyons")}</td><td>{F("ayons")}</td><td>{F("sachons")}</td><td></td></tr>
<tr><td>(vous)</td><td>{F("soyez")}</td><td>{F("ayez")}</td><td>{F("sachez")}</td><td>{F("veuillez")}</td></tr></table></div>
{ex("Sois sage !", "Be good! (to a child)")}
{ex("N'aie pas peur.", "Don't be afraid.")}
{ex("Veuillez fermer la porte.", "Please close the door. (very polite, on signs)")}
{lab(type="conj", verbs=["ranger", "fermer", "écouter", "finir", "choisir", "attendre", "aller", "faire", "venir", "prendre", "être", "avoir", "se lever", "s'habiller", "se dépêcher"], tenses=["imp", "pres"])}
<h3>Negative commands</h3>
<p>Wrap the verb as usual: {F("Ne touche pas !")} (Don't touch!), {F("Ne parlez pas !")}</p>
<h3>Reflexive verbs</h3>
{wa("Commands with reflexive verbs", [
 ("s|Tu|s  p|te|x  v|lèves.|v", "Statement: tu te lèves.", "You get up."),
 ("v|Lève|v  p|-toi !|n", "Positive command: the pronoun goes after the verb with a hyphen, and te becomes toi.", "Get up!"),
 ("n1|Ne|n  p|te|x  v|lève|v  n2|pas !|n", "Negative command: the pronoun stays in front, and ne … pas wraps it.", "Don't get up!")])}
''', pill=("g", "6.4"), sub="Range ta chambre ! Allons-y ! Asseyez-vous.",
 det=("Imperative details", '''<h4>Let's…</h4><p>The nous form means "let's": <i>Allons au cinéma !</i> (Let's go to the movies!) <i>Mangeons !</i> (Let's eat!)</p>
<h4>The s comes back before y and en</h4><p>For sound, -er verbs keep their s before y or en: <i>Vas-y !</i> (Go on!), <i>Manges-en !</i> (Eat some!)</p>
<h4>Being polite</h4><p>A bare command can sound bossy. Add <i>s'il te plaît / s'il vous plaît</i>, or ask instead: <i>Tu peux fermer la porte ?</i> <i>Pourriez-vous m'aider ?</i></p>
<h4>Pronouns in commands</h4><p>In positive commands, me and te become moi and toi after the verb: <i>Aide-moi !</i>, <i>Assieds-toi !</i> In negative commands they stay before: <i>Ne me regarde pas !</i></p>'''))
CH.append(chapter("chores-f6", "Les tâches et l'impératif", "Commands", [CHORES, IMP]))

REV = topic("review-f6", "Unit 6 summary", f'''<div class="grid2"><div class="mini"><h4>Home</h4><p>la chambre, le salon, la cuisine, la salle de bains… le lit, l'armoire, le canapé… le rez-de-chaussée = ground floor.</p></div>
<div class="mini"><h4>Where</h4><p>sur, sous, dans, devant, derrière, entre. à côté du / de la / de l' / des. chez moi, chez Paul.</p></div>
<div class="mini"><h4>Chores</h4><p>faire la vaisselle, faire le ménage, faire son lit, ranger, passer l'aspirateur, mettre la table.</p></div>
<div class="mini"><h4>Imperative</h4><p>tu / nous / vous without the subject. -er verbs drop the tu s. sois, aie. Lève-toi ! / Ne te lève pas !</p></div></div>''', sub="Everything from this unit on one screen.")
MIS = topic("mistakes-f6", "Common mistakes", '''<ol class="steps">
<li>Keeping the s in tu commands of -er verbs: <i>Ranges ta chambre !</i> → <i>Range ta chambre !</i></li>
<li>Dropping the s in -ir / -re verbs: <i>Fini !</i> → <i>Finis !</i></li>
<li><i>à côté de le lit</i> → <i>à côté du lit</i>.</li>
<li>Using the subject in a command: <i>Tu mange !</i> → <i>Mange !</i></li>
<li><i>Lève-te !</i> → <i>Lève-toi !</i> (te becomes toi after the verb).</li>
<li><i>Ne lève-toi pas</i> → <i>Ne te lève pas</i> (in the negative, the pronoun goes back in front).</li>
<li>Saying <i>premier étage</i> for the ground floor: that's <i>le rez-de-chaussée</i>.</li></ol>''', sub="Points students lose most often.")
CH.append(chapter("review-ch-f6", "Review", "Review", [REV, MIS]))

PQ = [
 q("Where do you sleep?", ["dans la chambre", "dans la cuisine", "dans le garage", "dans la salle à manger"], 0, "la chambre = bedroom.", "v"),
 q("<i>le frigo</i> is usually in…", ["la cuisine", "la chambre", "le salon", "la salle de bains"], 0, "The fridge is in the kitchen.", "v"),
 q("<i>le rez-de-chaussée</i> means…", ["the ground floor", "the second floor", "the basement", "the roof"], 0, "Ground floor; le premier étage is one floor up.", "v"),
 q("<i>Le chat est ______ le lit.</i> (under)", ["sous", "sur", "dans", "devant"], 0, "sous = under.", "v"),
 q("<i>La lampe est à côté ______ canapé.</i>", ["du", "de le", "de la", "au"], 0, "de + le = du.", "g"),
 q("<i>Le bureau est près ______ fenêtres.</i>", ["des", "de les", "du", "aux"], 0, "de + les = des.", "g"),
 q("<i>Le miroir est ______ l'armoire.</i> (above)", ["au-dessus de", "au-dessous de", "derrière", "loin de"], 0, "au-dessus de = above.", "v"),
 q("How do you say <i>at my place</i>?", ["chez moi", "chez je", "à ma maison chez", "chez mon"], 0, "chez + stress pronoun: chez moi.", "g"),
 q("<i>On va ______ Julien ?</i>", ["chez", "à", "de", "au"], 0, "chez + person.", "g"),
 q("<i>faire la vaisselle</i> means…", ["to do the dishes", "to do the laundry", "to set the table", "to vacuum"], 0, "la vaisselle = the dishes.", "v"),
 q("<i>passer l'aspirateur</i> means…", ["to vacuum", "to dust", "to take out the trash", "to cook"], 0, "un aspirateur = a vacuum cleaner.", "v"),
 q("<i>Je fais ______ lit tous les matins.</i>", ["mon", "le mon", "ma", "faire"], 0, "Possessive matching the subject: je → mon lit.", "g"),
 q("Command (tu): <i>ranger ta chambre</i>", ["Range ta chambre !", "Ranges ta chambre !", "Tu ranges ta chambre !", "Rangez ta chambre, toi !"], 0, "-er verbs drop the s in the tu command.", "g"),
 q("Command (tu): <i>finir tes devoirs</i>", ["Finis tes devoirs !", "Fini tes devoirs !", "Finit tes devoirs !", "Finir tes devoirs !"], 0, "-ir verbs keep the s: finis.", "g"),
 q("Command (vous): <i>attendre ici</i>", ["Attendez ici !", "Attendre ici !", "Attends ici, vous !", "Vous attendez ici !"], 0, "vous form without the subject.", "g"),
 q("<i>Let's go!</i>", ["Allons-y !", "Va-y !", "Allez-y nous !", "Aller !"], 0, "nous form = let's. y = there.", "g"),
 q("Command (tu) of <i>être</i>:", ["sois", "es", "soit", "être"], 0, "être is irregular: sois, soyons, soyez.", "g"),
 q("<i>N'______ pas peur !</i> (tu, avoir)", ["aie", "as", "ai", "avoir"], 0, "avoir: aie, ayons, ayez.", "g"),
 q("Make it negative: <i>Touche !</i>", ["Ne touche pas !", "Touche pas ne !", "Ne pas touche !", "Touche ne pas !"], 0, "ne + verb + pas.", "g"),
 q("<i>Get up!</i> (tu)", ["Lève-toi !", "Te lève !", "Lève-te !", "Toi lève !"], 0, "Pronoun after the verb, and te → toi.", "g"),
 q("<i>Don't get up!</i> (tu)", ["Ne te lève pas !", "Ne lève-toi pas !", "Ne lève pas toi !", "Lève-toi pas !"], 0, "In the negative the pronoun stays in front.", "g"),
 q("<i>mettre la table</i> means…", ["to set the table", "to clear the table", "to buy a table", "to sit at the table"], 0, "mettre = to put; mettre la table = set the table.", "v"),
 q(f"{listen('Sortez la poubelle, s’il vous plaît.')} What should you do?", ["Take out the trash", "Walk the dog", "Leave the room", "Close the door"], 0, "sortir la poubelle = take out the trash.", "v"),
 q("Which is a polite request rather than a command?", ["Tu peux fermer la fenêtre ?", "Ferme la fenêtre !", "Fermez la fenêtre !", "Ne ferme pas la fenêtre !"], 0, "Asking with pouvoir is softer than an imperative.", "g"),
]
CHAL = [
 q("Which command is correct?", ["Va dans ta chambre !", "Vas dans ta chambre !", "Allez dans ta chambre, tu !", "Aller dans ta chambre !"], 0, "aller drops the s in the tu command: Va ! (but Vas-y !).", "g"),
 q("Which is correct?", ["Vas-y !", "Va-y !", "Y va !", "Allez-y toi !"], 0, "Before y, the s comes back for the sound: vas-y.", "g"),
 q("<i>Asseyez-vous</i> means…", ["Sit down (formal or plural)", "Stand up", "Calm down", "Go away"], 0, "s'asseoir = to sit down.", "v"),
 q("Which sentence is correct?", ["Le tapis est entre le canapé et la table.", "Le tapis est entre du canapé et de la table.", "Le tapis est entre le canapé à la table.", "Le tapis est entre au canapé et la table."], 0, "entre … et … takes no de.", "g"),
 q("<i>Help me!</i> (tu)", ["Aide-moi !", "Aide-me !", "Me aide !", "Aides-moi !"], 0, "me becomes moi after a positive command; -er verbs drop the s.", "g"),
 q("<i>Ne ______ pas !</i> (vous, se dépêcher)", ["vous dépêchez", "dépêchez-vous", "se dépêchez", "vous dépêcher"], 0, "Negative: pronoun before the verb.", "g"),
 q("Your friend lives on the <i>deuxième étage</i>. In the US that is the…", ["third floor", "second floor", "ground floor", "fourth floor"], 0, "French counts from the rez-de-chaussée, so 2e étage = US third floor.", "v"),
 q("<i>Soyons ______ !</i> (let's be calm, we)", ["calmes", "calme", "calmez", "calmons"], 0, "Adjectives agree: nous → plural.", "g"),
]
EXQ = [
 q("<i>On prépare les repas dans ______.</i>", ["la cuisine", "la chambre", "le salon", "le garage"], 0, "You cook in the kitchen.", "v", "vocab"),
 q("<i>On regarde la télé dans ______.</i>", ["le salon", "la salle de bains", "le placard", "l'escalier"], 0, "le salon = living room.", "v", "vocab"),
 q("<i>Mes vêtements sont dans ______.</i>", ["l'armoire", "le four", "le frigo", "l'évier"], 0, "l'armoire = wardrobe.", "v", "vocab"),
 q("<i>Le chien dort ______ la table.</i> (under)", ["sous", "sur", "entre", "en face"], 0, "sous = under.", "v", "vocab"),
 q("<i>La salle de bains est en face ______ ma chambre.</i>", ["de", "du", "à", "des"], 0, "en face de + ma chambre (no article to combine).", "g", "gram"),
 q("<i>Le fauteuil est à droite ______ lit.</i>", ["du", "de le", "de la", "au"], 0, "de + le = du.", "g", "gram"),
 q("<i>Je dors ______ mes grands-parents ce week-end.</i>", ["chez", "à", "dans", "de"], 0, "chez + people.", "g", "gram"),
 q("<i>faire la lessive</i> means…", ["to do the laundry", "to do the dishes", "to read", "to vacuum"], 0, "la lessive = laundry.", "v", "vocab"),
 q("Command (tu): <i>écouter</i>", ["Écoute !", "Écoutes !", "Écouter !", "Tu écoute !"], 0, "-er verb: drop the s.", "g", "gram"),
 q("Command (nous): <i>faire la vaisselle</i>", ["Faisons la vaisselle !", "Faites la vaisselle !", "Fais la vaisselle !", "Nous faisons la vaisselle !"], 0, "nous form = let's: faisons.", "g", "gram"),
 q("Command (vous) of <i>être</i>:", ["Soyez", "Êtes", "Soyons", "Sois"], 0, "être: sois, soyons, soyez.", "g", "gram"),
 q("<i>Wake up!</i> (tu, se réveiller)", ["Réveille-toi !", "Te réveille !", "Réveilles-toi !", "Réveille-te !"], 0, "Pronoun after, te → toi, no s on -er verbs.", "g", "gram"),
 q(f"{listen('Ne mets pas tes chaussures sur le canapé !')} What does the speaker want?", ["Shoes off the sofa", "Put your shoes on", "Sit on the sofa", "Buy new shoes"], 0, "Ne mets pas = don't put.", "v", "listen"),
 q("Read: <i>Chez moi, ma chambre est au premier étage. Il y a un lit, un bureau et une grande armoire. Mon ordinateur est sur le bureau, à côté de la fenêtre.</i> Where is the computer?", ["On the desk, next to the window", "On the bed", "In the wardrobe", "On the ground floor"], 0, "sur le bureau, à côté de la fenêtre.", "v", "read"),
 q("Which is <b>not</b> a correct command?", ["Ne lève-toi pas !", "Ne te lève pas !", "Lève-toi !", "Levez-vous !"], 0, "Negative commands keep the pronoun in front: Ne te lève pas !", "g", "gram"),
]
FRQS = [
 {"q": "Describe your bedroom or your dream bedroom (at least 5 sentences).",
  "parts": [{"p": "Name at least five pieces of furniture or objects and say where they are, using at least four different prepositions.",
   "rubric": [["At least five furniture words with correct gender", 2], ["At least four different prepositions of place", 2], ["Correct contractions (du, des) after à côté de / près de / en face de", 1], ["il y a and être used correctly", 1]],
   "answer": f'<div class="ex">{F("Ma chambre est petite mais jolie. Il y a un lit sous la fenêtre. À côté du lit, il y a une lampe sur une petite table. Mon bureau est en face de la porte, et mes livres sont sur l\'étagère au-dessus du bureau. Il y a un tapis bleu entre le lit et l\'armoire.")}<span class="en">My room is small but pretty. There\'s a bed under the window. Next to the bed there\'s a lamp on a little table. My desk is across from the door, and my books are on the shelf above the desk. There\'s a blue rug between the bed and the wardrobe.</span></div>'}]},
 {"q": "Your little brother has to do chores before your parents get home. Write him a note with at least five commands.",
  "parts": [{"p": "Use tu commands, at least one negative command and one reflexive command.",
   "rubric": [["Five tu commands with correct forms (no s on -er verbs)", 2], ["One correct negative command", 1], ["One reflexive command (Dépêche-toi !)", 1], ["Chore vocabulary used correctly", 1]],
   "answer": f'<div class="ex">{F("Salut Max ! Range ta chambre et fais ton lit. Sors la poubelle, s\'il te plaît. Mets la table pour le dîner. Ne joue pas aux jeux vidéo avant ! Et dépêche-toi : papa et maman rentrent à six heures.")}<span class="en">Hi Max! Tidy your room and make your bed. Take out the trash, please. Set the table for dinner. Don\'t play video games first! And hurry up: Mom and Dad get home at six.</span></div>'}]},
]

if __name__ == "__main__":
    build(6, "unit-6", "Home", 'À la <span class="hl">maison</span>',
          "Rooms and furniture, saying where things are, chez, chores and the imperative. Tap any French word to hear it.",
          "French 1 Unit 6: home, prepositions of place, chores and the imperative, with audio, interactive labs, practice questions and a practice exam.",
          CH, PQ, CHAL, EXQ, FRQS, "/home/claude/ap-physics-study/courses/french-1/unit-6.html")
