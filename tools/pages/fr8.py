from fr_common import *

CH = []
CORE = f'''<p>The last unit gets you <b>traveling</b>: naming countries and nationalities, saying where you're going and how, getting through the train station and the airport, and using <b>object pronouns</b> so you don't have to repeat yourself.</p>
{wa("Replacing a noun with a pronoun", [
 ("s|Je|s  v|prends|v  o|le train.|x", "le train is the direct object.", "I take the train."),
 ("s|Je|s  o|le|n  v|prends.|v", "Replace it with le, and move it in front of the verb.", "I take it."),
 ("s|Je|s  n1|ne|x  o|le|n  v|prends|v  n2|pas.|x", "In the negative, ne goes before the pronoun.", "I don't take it.")])}
<div class="grid2"><div class="mini"><h4>In this unit</h4><p>Countries and nationalities · en / au / aux · transportation · at the station and airport · partir, sortir, quitter · direct object pronouns le, la, les.</p></div>
<div class="mini"><h4>Course wrap-up</h4><p>The final writing tasks pull everything together: present, past, futur proche, descriptions and pronouns.</p></div></div>'''
CH.append(chapter("overview-f8", "Overview", "Overview", [topic("core-f8", "Les voyages", CORE)]))

GEO = topic("countries", "Countries and prepositions", f'''
<p>Countries have a gender too, and it decides the little word for <i>in / to</i> and <i>from</i>.</p>
<div class="tblwrap"><table><tr><th>Country is…</th><th>in / to</th><th>from</th><th>Examples</th></tr>
<tr><td>feminine (most end in -e)</td><td><b>en</b></td><td><b>de</b> (d')</td><td>{F("en France")}, {F("de Chine")}, {F("d'Italie")}</td></tr>
<tr><td>masculine</td><td><b>au</b></td><td><b>du</b></td><td>{F("au Canada")}, {F("du Japon")}, {F("au Mexique")}</td></tr>
<tr><td>masculine + vowel</td><td><b>en</b></td><td><b>d'</b></td><td>{F("en Iran")}, {F("d'Iran")}</td></tr>
<tr><td>plural</td><td><b>aux</b></td><td><b>des</b></td><td>{F("aux États-Unis")}, {F("des Pays-Bas")}</td></tr>
<tr><td>a city</td><td><b>à</b></td><td><b>de</b></td><td>{F("à Paris")}, {F("de Montréal")}</td></tr></table></div>
{lab(type="geo")}
{box("trap", "Exceptions to the -e rule", f"{F('le Mexique')}, {F('le Cambodge')} and {F('le Mozambique')} end in -e but are masculine: {F('au Mexique')}.")}
<h3>The French-speaking world</h3>
<p>French is spoken on five continents: in {F("la France")}, {F("la Belgique")}, {F("la Suisse")}, {F("le Canada")} (especially {F("le Québec")}), {F("le Sénégal")}, {F("la Côte d'Ivoire")}, {F("le Maroc")}, {F("Haïti")} and many more. Together these countries are called {F("la Francophonie")}.</p>
''', pill=("g", "8.1"), sub="en France, au Canada, aux États-Unis.",
 det=("More on countries", '''<h4>Nationalities</h4><p>As adjectives they're lowercase and agree: <i>Elle est canadienne.</i> As nouns for people they're capitalized: <i>une Canadienne</i>. Languages are lowercase and masculine: <i>le français</i>, <i>l'arabe</i>.</p>
<h4>US states and provinces</h4><p>Feminine states take en: <i>en Californie, en Floride</i>. Most others use <i>dans le</i>: <i>dans le Texas</i> (or <i>au Texas</i>), <i>dans l'Illinois</i>.</p>
<h4>Islands</h4><p>Many islands work like cities: <i>à Haïti, à Cuba, à Madagascar</i>.</p>'''))

TRANS = topic("transport", "Getting around", f'''
{vt([("en voiture", "by car"), ("en bus", "by bus"), ("en train", "by train"), ("en avion", "by plane"), ("en métro", "by subway"), ("en taxi", "by taxi"), ("en bateau", "by boat"), ("à vélo", "by bike"), ("à pied", "on foot"), ("à moto", "by motorcycle")])}
<p>Rule of thumb: <b>en</b> if you ride <i>inside</i> it, <b>à</b> if you sit <i>on</i> it or walk.</p>
{ex("Je vais au lycée à pied, mais mon frère y va en bus.", "I walk to school, but my brother goes by bus.")}
<h3>At the station and the airport</h3>
{vgrid([("la gare", "train station"), ("l'aéroport (m.)", "airport"), ("le billet", "ticket"), ("un aller simple", "one-way ticket"), ("un aller-retour", "round-trip ticket"), ("le quai", "platform"), ("la voie", "track"), ("le vol", "flight"), ("la porte", "gate"), ("l'embarquement (m.)", "boarding"), ("le passeport", "passport"), ("la valise", "suitcase"), ("les bagages (m.)", "luggage"), ("en retard / à l'heure", "late / on time"), ("le départ / l'arrivée (f.)", "departure / arrival"), ("composter", "to validate (a ticket)")])}
{ex("Un aller-retour pour Lyon, s'il vous plaît.", "A round-trip ticket to Lyon, please.")}
{ex("Le train part de la voie 7 à 14 h 32.", "The train leaves from track 7 at 2:32 p.m.")}
{ex("Le vol est en retard d'une heure.", "The flight is an hour late.")}
''', pill=("v", "8.2"), sub="en train, à pied, and travel vocabulary.")
CH.append(chapter("geo-f8", "Pays et transports", "Countries", [GEO, TRANS]))

LEAVE = topic("leaving", "Partir, sortir, quitter", f'''
<p>English uses <i>leave</i> for all three. French doesn't.</p>
<div class="tblwrap"><table><tr><th>Verb</th><th>Means</th><th>Example</th></tr>
<tr><td>{F("partir")}</td><td>to leave, go away (on a trip)</td><td>{F("Je pars en vacances demain.")}</td></tr>
<tr><td>{F("sortir")}</td><td>to go out, exit</td><td>{F("On sort ce soir ?")} {F("Il sort de la classe.")}</td></tr>
<tr><td>{F("quitter")}</td><td>to leave <i>something / someone</i> (always has an object)</td><td>{F("Je quitte la maison à 7 h.")}</td></tr></table></div>
{lab(type="conj", verbs=["partir", "sortir", "dormir", "voyager", "visiter", "prendre", "arriver"], tenses=["pres", "pc", "fp"])}
<p>partir and sortir are irregular (je pars, nous partons; je sors, nous sortons) and take <b>être</b> in the passé composé: {F("Elle est partie.")} quitter is a regular -er verb with avoir: {F("Elle a quitté Paris.")}</p>
''', pill=("g", "8.3"), sub="Three ways to say leave.")

DOP = topic("object-pronouns", "Direct object pronouns: le, la, les", f'''
<p>A direct object is the person or thing a verb acts on directly, with no preposition: <i>I see <b>the train</b></i>. Replace it with a pronoun to avoid repeating.</p>
<div class="tblwrap"><table><tr><th>Replaces</th><th>Pronoun</th><th>Example</th></tr>
<tr><td>masculine singular</td><td>{F("le")} (l')</td><td>{F("Tu as le billet ? — Oui, je l'ai.")}</td></tr>
<tr><td>feminine singular</td><td>{F("la")} (l')</td><td>{F("Tu prends ta valise ? — Oui, je la prends.")}</td></tr>
<tr><td>plural</td><td>{F("les")}</td><td>{F("Tu vois tes parents ? — Je les vois samedi.")}</td></tr>
<tr><td>me, you, us</td><td>{F("me, te, nous, vous")}</td><td>{F("Tu m'attends ?")} {F("Je vous aime.")}</td></tr></table></div>
<h3>Where it goes</h3>
{wa("The pronoun moves in front of the verb", [
 ("s|Je|s  v|regarde|v  o|la carte.|x", "Present tense: one verb.", "I look at the map."),
 ("s|Je|s  o|la|n  v|regarde.|v", "The pronoun goes right before the conjugated verb.", "I look at it."),
 ("s|Je|s  a|vais|x  o|la|n  v|regarder.|v", "With two verbs, it goes before the infinitive it belongs to.", "I'm going to look at it."),
 ("s|Je|s  o|l'|n  a|ai|x  v|regardée.|v", "In the passé composé it goes before avoir, and the participle agrees with a pronoun that comes before it.", "I looked at it."),
 ("v|Regarde-|v  o|la !|n", "In a positive command it goes after, with a hyphen.", "Look at it!")])}
{box("trap", "Not every 'it' is direct", f"Verbs like {F('téléphoner à')} and {F('parler à')} take an <b>indirect</b> object (lui, leur), which you'll learn in French 2: {F('Je lui téléphone.')} (I call him / her). But {F('regarder')}, {F('écouter')}, {F('chercher')} and {F('attendre')} take a direct object in French, even though English uses a preposition: {F('Je l\'attends.')} (I'm waiting for him.)")}
''', pill=("g", "8.4"), sub="Je le prends. Je ne la vois pas. Je vais les acheter.",
 det=("Object pronoun details", '''<h4>le, la → l'</h4><p>Before a vowel or silent h, le and la both become l': <i>Je l'aime</i> could be him, her or it. Context tells you which.</p>
<h4>Negatives</h4><p>ne goes before the pronoun and pas after the verb: <i>Je ne le vois pas.</i> In the passé composé: <i>Je ne l'ai pas vu.</i></p>
<h4>Agreement in the passé composé</h4><p>With avoir, the past participle agrees with a direct object that comes <b>before</b> it: <i>La valise ? Je l'ai prise.</i> <i>Les billets ? Je les ai achetés.</i> You usually can't hear it, except with participles like pris → prise.</p>
<h4>le can also mean "it" for an idea</h4><p><i>Je le sais.</i> (I know it.) <i>Je ne le crois pas !</i> (I don't believe it!)</p>'''))
CH.append(chapter("dop-f8", "Partir et les pronoms", "Pronouns", [LEAVE, DOP]))

TRIP = topic("plan-trip", "Planning a trip", f'''
<p>Put the whole course together to plan and tell about a trip.</p>
{ex("Cet été, je vais aller au Québec avec ma famille. Nous allons partir le 3 juillet et nous allons voyager en avion.", "This summer I'm going to go to Quebec with my family. We're going to leave July 3rd and fly.")}
{ex("L'année dernière, je suis allé en France. J'ai visité Paris et j'ai pris le train pour Nice. J'ai adoré la plage !", "Last year I went to France. I visited Paris and I took the train to Nice. I loved the beach!")}
{vt([("faire un voyage", "to take a trip"), ("faire sa valise", "to pack your suitcase"), ("réserver une chambre", "to book a room"), ("l'auberge de jeunesse (f.)", "youth hostel"), ("visiter un musée", "to visit a museum"), ("rendre visite à quelqu'un", "to visit someone"), ("prendre des photos", "to take pictures"), ("acheter des souvenirs", "to buy souvenirs"), ("Bon voyage !", "Have a good trip!")])}
{box("trap", "visiter vs rendre visite", f"{F('visiter')} is for places ({F('visiter Paris')}); for people use {F('rendre visite à')} ({F('rendre visite à ma tante')}).")}
''', pill=("v", "8.5"), sub="Putting it all together.")
CH.append(chapter("trip-f8", "Le voyage: Planning a trip", "Trip", [TRIP]))

REV = topic("review-f8", "Unit 8 summary", f'''<div class="grid2"><div class="mini"><h4>Countries</h4><p>en + feminine (or vowel), au + masculine, aux + plural, à + city. From: de / d', du, des, de.</p></div>
<div class="mini"><h4>Transport</h4><p>en voiture, en train, en avion… but à pied, à vélo. un aller-retour, le quai, le vol, en retard.</p></div>
<div class="mini"><h4>Leaving</h4><p>partir (go away), sortir (go out), quitter + object. partir / sortir take être.</p></div>
<div class="mini"><h4>Object pronouns</h4><p>le, la, l', les before the conjugated verb; before the infinitive with two verbs; after a positive command.</p></div></div>''', sub="Everything from this unit on one screen.")
MIS = topic("mistakes-f8", "Common mistakes", '''<ol class="steps">
<li><i>à France</i> / <i>en Canada</i> → <i>en France</i> / <i>au Canada</i>.</li>
<li><i>en Mexique</i> → <i>au Mexique</i> (masculine despite the -e).</li>
<li><i>en pied</i> → <i>à pied</i>; <i>à train</i> → <i>en train</i>.</li>
<li><i>Je quitte</i> with nothing after it → <i>Je pars</i>.</li>
<li><i>Je prends le</i> → <i>Je le prends</i> (pronoun before the verb).</li>
<li><i>Je le vais acheter</i> → <i>Je vais l'acheter</i>.</li>
<li><i>visiter ma grand-mère</i> → <i>rendre visite à ma grand-mère</i>.</li></ol>''', sub="Points students lose most often.")
CH.append(chapter("review-ch-f8", "Review", "Review", [REV, MIS]))

PQ = [
 q("<i>J'habite ______ France.</i>", ["en", "au", "à", "aux"], 0, "France is feminine → en.", "g"),
 q("<i>Ils vont ______ Canada.</i>", ["au", "en", "à", "du"], 0, "Canada is masculine → au.", "g"),
 q("<i>Nous habitons ______ États-Unis.</i>", ["aux", "en", "au", "à les"], 0, "Plural → aux.", "g"),
 q("<i>Elle est ______ Paris.</i>", ["à", "en", "au", "dans"], 0, "City → à.", "g"),
 q("<i>Je viens ______ Japon.</i>", ["du", "de", "en", "au"], 0, "Masculine → du.", "g"),
 q("<i>Il vient ______ Italie.</i>", ["d'", "du", "de la", "en"], 0, "Feminine + vowel → d'.", "g"),
 q("<i>On va ______ Mexique cet hiver.</i>", ["au", "en", "à la", "aux"], 0, "le Mexique is masculine.", "g"),
 q("A woman from Senegal is…", ["sénégalaise", "sénégalais", "Sénégale", "sénégalienne"], 0, "sénégalais → sénégalaise.", "v"),
 q("<i>Je vais à l'école ______.</i> (on foot)", ["à pied", "en pied", "par pied", "au pied"], 0, "à pied.", "v"),
 q("<i>Nous voyageons ______ train.</i>", ["en", "à", "par", "au"], 0, "Inside a vehicle → en.", "v"),
 q("<i>un aller-retour</i> is…", ["a round-trip ticket", "a one-way ticket", "a return flight only", "a delay"], 0, "aller-retour = round trip.", "v"),
 q("<i>Le train est en retard</i> means…", ["The train is late.", "The train is early.", "The train is on time.", "The train left."], 0, "en retard = late.", "v"),
 q("<i>Le quai</i> is where you…", ["wait for the train", "buy food", "check bags at the airport", "show your passport"], 0, "le quai = platform.", "v"),
 q("<i>Demain, je ______ en vacances.</i> (leave)", ["pars", "quitte", "sors", "laisse"], 0, "partir = to leave on a trip.", "g"),
 q("<i>Elle ______ la maison à huit heures.</i>", ["quitte", "part", "sort", "pars"], 0, "quitter + a place.", "g"),
 q("<i>Hier soir, nous ______ avec des amis.</i> (went out)", ["sommes sortis", "avons sorti", "sommes sorti", "sortons"], 0, "sortir takes être; agree with nous (masc. plural).", "g"),
 q("<i>Tu as ton passeport ? — Oui, je ______ ai.</i>", ["l'", "le", "la", "les"], 0, "le → l' before a vowel.", "g"),
 q("<i>Tu prends la valise rouge ? — Oui, je ______ prends.</i>", ["la", "le", "les", "lui"], 0, "valise is feminine → la.", "g"),
 q("<i>Tu achètes les billets ? — Oui, je ______ achète.</i>", ["les", "le", "la", "leur"], 0, "Plural → les.", "g"),
 q("Replace the object: <i>Je regarde le plan.</i>", ["Je le regarde.", "Je regarde le.", "Je la regarde.", "Le je regarde."], 0, "Pronoun before the verb.", "g"),
 q("Replace the object: <i>Je vais visiter le musée.</i>", ["Je vais le visiter.", "Je le vais visiter.", "Je vais visiter le.", "Le je vais visiter."], 0, "With two verbs, before the infinitive.", "g"),
 q("Make it negative: <i>Je la vois.</i>", ["Je ne la vois pas.", "Je la ne vois pas.", "Je ne vois la pas.", "Ne je la vois pas."], 0, "ne before the pronoun.", "g"),
 q("<i>Ce week-end, je vais ______ à ma grand-mère.</i>", ["rendre visite", "visiter", "voir visite", "quitter"], 0, "Visiting a person: rendre visite à.", "v"),
 q(f"{listen('Le vol pour Montréal part de la porte douze.')} Where does the flight leave from?", ["Gate 12", "Track 12", "Gate 2", "Platform 10"], 0, "la porte = gate; douze = 12.", "v"),
]
CHAL = [
 q("Which is correct?", ["Je suis allé au Maroc et ensuite en Espagne.", "Je suis allé en Maroc et ensuite à l'Espagne.", "Je suis allé au Maroc et ensuite au Espagne.", "J'ai allé au Maroc et ensuite en Espagne."], 0, "Maroc masculine (au), Espagne feminine (en), aller takes être.", "g"),
 q("<i>La valise ? Je l'ai ______.</i>", ["prise", "pris", "prises", "prendu"], 0, "The participle agrees with a preceding direct object: valise (f.) → prise.", "g"),
 q("<i>Les billets ? Je ne ______ trouve pas !</i>", ["les", "leur", "le", "lui"], 0, "Direct object, plural → les.", "g"),
 q("<i>Écoute la chanson ! → ______</i>", ["Écoute-la !", "La écoute !", "L'écoute !", "Écoute-le !"], 0, "Positive command: pronoun after with a hyphen; chanson is feminine.", "g"),
 q("<i>Je t'attends</i> means…", ["I'm waiting for you.", "I'm listening to you.", "I hear you.", "You're waiting for me."], 0, "attendre takes a direct object: te → t'.", "v"),
 q("<i>Ils ______ Paris en 2020.</i> (left Paris)", ["ont quitté", "sont partis", "sont quittés", "ont parti"], 0, "With a place as object, use quitter (avoir).", "g"),
 q("Which country uses <i>en</i> even though it's masculine?", ["Iran", "Canada", "Japon", "Brésil"], 0, "Masculine countries starting with a vowel take en: en Iran.", "g"),
 q("<i>On ne va pas ______ voir.</i> (them)", ["les", "leur", "lui", "eux"], 0, "Direct object before the infinitive.", "g"),
]
EXQ = [
 q("<i>Mes cousins habitent ______ Belgique.</i>", ["en", "au", "à", "aux"], 0, "la Belgique → en.", "g", "gram"),
 q("<i>Elle est allée ______ Brésil.</i>", ["au", "en", "à", "aux"], 0, "le Brésil → au.", "g", "gram"),
 q("<i>Je viens ______ Pays-Bas.</i>", ["des", "du", "de", "aux"], 0, "Plural → des.", "g", "gram"),
 q("<i>Nous allons ______ Montréal.</i>", ["à", "au", "en", "dans"], 0, "City → à.", "g", "gram"),
 q("<i>Il est ______.</i> (Canadian, he)", ["canadien", "canadienne", "Canadien", "canadian"], 0, "Lowercase adjective, masculine.", "v", "vocab"),
 q("<i>Elle va au travail ______ vélo.</i>", ["à", "en", "par", "au"], 0, "You sit on a bike → à vélo.", "v", "vocab"),
 q("<i>Un aller simple</i> is…", ["a one-way ticket", "a round-trip ticket", "a simple trip", "a direct flight"], 0, "aller simple = one-way.", "v", "vocab"),
 q("<i>Tu ______ ce soir ?</i> (going out)", ["sors", "quittes", "pars", "sortes"], 0, "sortir: tu sors.", "g", "gram"),
 q("<i>Ils ______ pour la Chine hier.</i> (left)", ["sont partis", "ont partis", "ont quitté", "sont quittés"], 0, "partir → être + agreement.", "g", "gram"),
 q("<i>Tu as le billet ? — Non, je ne ______ ai pas.</i>", ["l'", "le", "la", "les"], 0, "le → l' before ai.", "g", "gram"),
 q("<i>Tu aimes ces photos ? — Oui, je ______ adore !</i>", ["les", "la", "le", "leur"], 0, "Plural → les.", "g", "gram"),
 q("Replace: <i>Je vais prendre le métro.</i>", ["Je vais le prendre.", "Je le vais prendre.", "Je vais prendre le.", "Je vais la prendre."], 0, "Before the infinitive; métro is masculine.", "g", "gram"),
 q(f"{listen('Un aller-retour pour Bordeaux, s’il vous plaît.')} What does the traveler want?", ["A round-trip ticket to Bordeaux", "A one-way ticket to Bordeaux", "A seat on the plane", "Directions to Bordeaux"], 0, "aller-retour = round trip.", "v", "listen"),
 q("Read: <i>L'été dernier, Sophie est partie au Sénégal. Elle a pris l'avion à Paris et elle est arrivée à Dakar le soir. Elle a rendu visite à sa tante et elle a visité l'île de Gorée.</i> Which is true?", ["Sophie visited her aunt in Senegal.", "Sophie went by boat.", "Sophie lives in Dakar.", "Sophie went to Senegal next summer."], 0, "Elle a rendu visite à sa tante.", "v", "read"),
 q("Which sentence is correct?", ["Regarde-le !", "Le regarde !", "Regarde-lui !", "Regarde le !"], 0, "Positive command: pronoun after with a hyphen.", "g", "gram"),
]
FRQS = [
 {"q": "Write about a trip: one you took (past) and one you're planning (future). At least 8 sentences total.",
  "parts": [{"p": "Name the countries or cities, the transport, what you did or will do, and use at least two object pronouns.",
   "rubric": [["Correct prepositions with countries and cities (en / au / aux / à)", 2], ["Passé composé with avoir and être, correct agreement", 2], ["Futur proche used correctly", 1], ["Transport with en / à", 1], ["Two direct object pronouns, correctly placed", 2], ["Overall accuracy and variety", 1]],
   "answer": f'<div class="ex">{F("L\'année dernière, je suis allée au Canada avec ma mère. Nous avons pris l\'avion jusqu\'à Montréal, puis nous sommes allées à Québec en train. J\'ai acheté une carte de la ville et je l\'ai regardée tout le temps ! L\'été prochain, je vais aller en France. Je vais visiter Paris et je vais rendre visite à mon correspondant. Je vais prendre le métro, mais je ne vais pas le prendre la nuit. Les musées ? Je vais les visiter tous !")}<span class="en">Last year I went to Canada with my mom. We flew to Montreal, then went to Quebec City by train. I bought a map of the city and looked at it the whole time! Next summer I\'m going to go to France. I\'m going to visit Paris and visit my pen pal. I\'m going to take the subway, but I won\'t take it at night. The museums? I\'m going to visit them all!</span></div>'}]},
 {"q": "Answer each question using a direct object pronoun.",
  "parts": [{"p": "1. Tu regardes la télé le soir ?  2. Tu as fait tes devoirs ?  3. Tu vas inviter tes amis ?  4. Tu aimes le français ?",
   "rubric": [["1. Oui, je la regarde / Non, je ne la regarde pas", 1], ["2. Oui, je les ai faits (agreement) / Non, je ne les ai pas faits", 1], ["3. Oui, je vais les inviter", 1], ["4. Oui, je l'aime (bien) !", 1]],
   "answer": f'<div class="ex">{F("Oui, je la regarde.")}<span class="en">Yes, I watch it.</span></div><div class="ex">{F("Oui, je les ai faits.")}<span class="en">Yes, I did it (them).</span></div><div class="ex">{F("Oui, je vais les inviter.")}<span class="en">Yes, I\'m going to invite them.</span></div><div class="ex">{F("Oui, je l\'aime beaucoup !")}<span class="en">Yes, I like it a lot!</span></div>'}]},
]

if __name__ == "__main__":
    build(8, "unit-8", "Travel", 'Les <span class="hl">voyages</span>',
          "Countries and nationalities, en / au / aux, transportation, the train station and airport, partir / sortir / quitter, and direct object pronouns. Tap any French word to hear it.",
          "French 1 Unit 8: countries, transportation, travel and direct object pronouns, with audio, interactive labs, practice questions and a practice exam.",
          CH, PQ, CHAL, EXQ, FRQS, "/home/claude/ap-physics-study/courses/french-1/unit-8.html")
