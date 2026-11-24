from tp_common import *
C = "sat"; L = "SAT"; OUT = "../../courses/sat/sat-3.html"
TAGS = {"b": "Boundaries", "f": "Form & structure", "t": "Transitions", "r": "Rhetorical synthesis"}
P = psg
CONV = "Which choice completes the text so that it conforms to the conventions of Standard English?"
TR = "Which choice completes the text with the most logical transition?"

BOUND = topic("boundaries", "Sentence boundaries: the punctuation rules", f'''
<p>Most grammar questions are about where one sentence ends and the next begins. First decide: is each side of the blank an <b>independent clause</b> (could stand alone as a sentence)?</p>
{table(["Between…", "Use", "Example"], [
 ["two independent clauses", "period, semicolon, or comma + FANBOYS (for, and, nor, but, or, yet, so)", "It rained; the game went on. / It rained, but the game went on."],
 ["independent clause + explanation or list", "colon (the part before it must be a full sentence)", "She needed three things: flour, eggs and time."],
 ["extra information in the middle", "a matching pair: two commas, two dashes, or two parentheses", "The dog — a beagle named Pip — ran off."],
 ["dependent + independent clause", "comma after the dependent clause", "Although it rained, the game went on."],
 ["subject and its verb", "NO punctuation", "The scientists in the lab <b>found</b>… (not \"lab, found\")"]])}
{steps("Fix a comma splice", [
 ("a|The museum reopened|s  b|,|e  c|visitors lined up for hours.|s", "Two complete sentences joined by just a comma: a comma splice."),
 ("a|The museum reopened|s  d|;|g  c|visitors lined up for hours.|s", "Fix 1: a semicolon."),
 ("a|The museum reopened|s  e|, and|g  c|visitors lined up for hours.|s", "Fix 2: comma + FANBOYS."),
 ("f|When|v  a|the museum reopened|s  b|,|g  c|visitors lined up for hours.|s", "Fix 3: make one side dependent with a word like \"when.\" Now the comma is right."),
])}
{steps("Don't split the subject from its verb", [
 ("a|The paintings by the young Dutch artist|s  b|,|e  c|sold within a day.|v", "The subject is long, so it's tempting to pause. But no comma goes between a subject and its verb."),
 ("a|The paintings by the young Dutch artist|s  c|sold within a day.|v", "Remove it. Subject → verb with nothing in between."),
])}
{box("trap", "Colon test", "Cover everything after the colon. If what's left isn't a complete sentence, the colon is wrong. \"The recipe calls for: flour and eggs\" fails.")}
{box("tip", "Apostrophes", "Possessive: the scientist's notes (one scientist), the scientists' notes (many). <b>its</b> = belonging to it; <b>it's</b> = it is. <b>their</b> = belonging to them; <b>they're</b> = they are.")}
''', pill=("b", "3.1"))

FORM = topic("form", "Form, structure and sense", f'''
{mini(("Subject-verb agreement", "Find the real subject; ignore prepositional phrases. \"The <b>list</b> of names <b>is</b> long.\" Each, every, either, neither and collective nouns like team are singular."),
      ("Pronoun agreement", "The pronoun must match its noun. \"The company announced <b>its</b> plan\" (not their). Watch for unclear \"it\" or \"they.\""),
      ("Verb tense", "Match the time frame of the surrounding sentences. A finished event in the past: simple past. Past before past: had + verb."),
      ("Modifiers", "An opening phrase describes whatever comes right after the comma. \"Walking to school, <b>the rain</b> soaked me\" says the rain walked. Fix: \"Walking to school, <b>I</b> got soaked.\""))}
{steps("Find the real subject", [
 ("a|The collection|s  b|of rare coins|x  c|are|e  d|on display.", "Cross out the prepositional phrase \"of rare coins.\""),
 ("a|The collection|s  c|are|e  d|on display.", "The subject is \"collection,\" which is singular."),
 ("a|The collection|s  e|is|g  d|on display.", "Singular subject → singular verb."),
])}
{steps("Fix a dangling modifier", [
 ("a|Having studied all night,|v  b|the test|e  c|seemed easy.|s", "Who studied? Not the test. The modifier dangles."),
 ("a|Having studied all night,|v  d|Maya|g  e|found the test easy.|s", "Put the person who studied right after the comma."),
])}
''', pill=("f", "3.2"))

TRANS = topic("transitions", "Transitions", f'''
<p>Read the sentence before the blank and the sentence with the blank. Name the relationship <b>before</b> you look at the choices.</p>
{table(["Relationship", "Transitions"], [
 ["Same direction / more", "Furthermore, Moreover, In addition, Likewise, Similarly"],
 ["Contrast", "However, Nevertheless, By contrast, Still, Even so, Instead"],
 ["Cause → effect", "Therefore, Thus, Consequently, As a result, Hence"],
 ["Example", "For example, For instance, Specifically"],
 ["Sequence / time", "First, Then, Later, Afterward, Finally, Previously"],
 ["Restating / emphasis", "In other words, That is, Indeed, In fact"],
 ["Conceding", "Granted, Admittedly, Of course"]])}
{worked(P("The new bridge cut the commute from 40 minutes to 15. <span class=blank></span> many residents who had moved away began returning to the town."), "Faster commute → people return: <b>As a result,</b>. \"However\" (contrast) and \"For example\" (illustration) don't fit.")}
''', pill=("t", "3.3"))

SYN = topic("synthesis", "Rhetorical synthesis (the notes questions)", f'''
<p>You get a student's bullet-point notes and a <b>goal</b>. Only the goal matters. Underline it, then choose the sentence that does exactly that, using information from the notes.</p>
<div class="passage"><p>While researching a topic, a student has taken the following notes:</p><ul>
<li>The Great Wall of China is not one wall but many walls built over centuries.</li>
<li>The longest sections were built during the Ming dynasty (1368–1644).</li>
<li>Ming-era walls were made mostly of brick and stone.</li>
<li>Earlier walls were often made of packed earth.</li></ul>
<p>The student wants to <b>contrast the materials used in different periods</b>. Which choice most effectively uses relevant information from the notes to accomplish this goal?</p></div>
{worked("Answer", "\"While earlier sections of the Great Wall were often made of packed earth, Ming-era walls were built mostly of brick and stone.\" <br>A sentence about how long the wall is, even if true and well written, fails the goal.")}
{box("tip", "Goal words", "\"Emphasize a similarity,\" \"introduce the study to an audience unfamiliar with it,\" \"present the conclusion,\" \"specify the date.\" Each word in the goal rules out choices.")}
''', pill=("r", "3.4"))

CH = [chapter("ch-conv", "Standard English Conventions", "Grammar", [BOUND, FORM]), chapter("ch-expr", "Expression of Ideas", "Expression", [TRANS, SYN])]

def notes(items, goal):
    return '<div class="passage"><p>While researching a topic, a student has taken the following notes:</p><ul>' + "".join(f"<li>{i}</li>" for i in items) + f'</ul><p>The student wants to {goal}. Which choice most effectively uses relevant information from the notes to accomplish this goal?</p></div>'

PQ = [
 q(CONV + P("The volcano last erupted in <span class=blank></span> scientists still monitor it closely."), ["1980;", "1980,", "1980", "1980, however,"], 0, "Two independent clauses need a semicolon or period. A comma alone (or with however) creates a comma splice.", "b"),
 q(CONV + P("The team's findings <span class=blank></span> published in a leading journal last spring."), ["were", "was", "is", "has been"], 0, "Plural subject \"findings\" + past time \"last spring.\"", "f"),
 q(CONV + P("The list of approved <span class=blank></span> posted outside the main office."), ["projects is", "projects are", "project's are", "projects' is"], 0, "Subject is \"list\" (singular).", "f"),
 q(CONV + P("Marie Tharp's maps of the ocean <span class=blank></span> revealed a mountain ridge running down the middle of the Atlantic."), ["floor", "floor,", "floor;", "floor:"], 0, "No punctuation between subject (maps of the ocean floor) and verb (revealed).", "b"),
 q(CONV + P("The chef uses only three <span class=blank></span> olive oil, garlic, and lemon."), ["ingredients:", "ingredients;", "ingredients,", "ingredients, such as:"], 0, "Complete sentence + list → colon.", "b"),
 q(CONV + P("Octavia Butler, the science fiction <span class=blank></span> won a MacArthur Fellowship in 1995."), ["author,", "author", "author;", "author—"], 0, "Close the pair of commas around the appositive.", "b"),
 q(CONV + P("The company updated <span class=blank></span> privacy policy after customer complaints."), ["its", "it's", "their", "its'"], 0, "Company is singular; possessive \"its.\"", "f"),
 q(CONV + P("Running along the beach at dawn, <span class=blank></span>"), ["Leo spotted a pod of dolphins.", "a pod of dolphins was spotted by Leo.", "dolphins appeared to Leo.", "the dolphins were seen."], 0, "The runner (Leo) must come right after the comma.", "f"),
 q(TR + P("Cheetahs can reach 100 km/h. <span class=blank></span> they can hold that speed for only about 30 seconds."), ["However,", "Therefore,", "For example,", "Similarly,"], 0, "Fast but short: contrast.", "t"),
 q(TR + P("The town banned plastic bags in 2019. <span class=blank></span> plastic litter on its beaches fell by half within two years."), ["Subsequently,", "Nevertheless,", "For instance,", "In contrast,"], 0, "A later result: subsequently.", "t"),
 q(TR + P("Many insects are pollinators. Bees are the best known. <span class=blank></span> some moths and beetles pollinate flowers too."), ["Moreover,", "Instead,", "Therefore,", "In other words,"], 0, "Adding more examples.", "t"),
 q(notes(["The axolotl is a salamander native to lakes near Mexico City.", "It can regrow lost limbs, parts of its heart, and even parts of its brain.", "Scientists study it to learn about tissue repair."], "explain why scientists study the axolotl"), ["Because axolotls can regrow limbs and even parts of the heart and brain, scientists study them to learn about tissue repair.", "The axolotl is a salamander native to lakes near Mexico City.", "Axolotls live in lakes.", "Many salamanders exist."], 0, "The only choice that states the reason.", "r"),
 q(CONV + P("By the time the rescue team arrived, the hikers <span class=blank></span> for two days."), ["had waited", "wait", "will wait", "have waited"], 0, "Past before another past event: past perfect.", "f"),
 q(CONV + P("The two <span class=blank></span> notebooks were donated to the university library."), ["scientists'", "scientist's", "scientists", "scientists's"], 0, "Two scientists, possessive plural: scientists'.", "f"),
]
CHAL = [
 q(CONV + P("The study's lead author—a geologist who had spent a decade in <span class=blank></span> argued that the rock layers were older than expected."), ["Iceland—", "Iceland,", "Iceland;", "Iceland"], 0, "The interruption opened with a dash, so it must close with a dash.", "b"),
 q(CONV + P("Neither the coach nor the players <span class=blank></span> expecting the storm to cancel the match."), ["were", "was", "is", "has been"], 0, "With neither/nor, the verb agrees with the closer subject: players → were.", "f"),
 q(CONV + P("Sociologist Robert Putnam studied community life in the United States. In his <span class=blank></span> he argued that membership in clubs and leagues had declined sharply."), ["book Bowling Alone,", "book, Bowling Alone", "book, Bowling Alone,", "book; Bowling Alone"], 0, "Restrictive title (he wrote several books): no commas around it; then a comma after the introductory phrase.", "b"),
 q(TR + P("Early studies suggested that the drug had no side effects. <span class=blank></span> trials with larger groups revealed mild headaches in some patients."), ["However,", "Similarly,", "For example,", "Thus,"], 0, "The larger trials contradict the early finding: contrast.", "t"),
 q(notes(["Study 1 (2015) tracked 300 runners for one year.", "Study 2 (2020) tracked 3,000 runners for five years.", "Both found that stretching before running did not reduce injuries."], "emphasize the similarity between the two studies' findings"), ["Despite differing in size and length, both studies found that stretching before running did not reduce injuries.", "Study 2 was larger and longer than Study 1.", "Study 1 tracked 300 runners in 2015.", "Runners often stretch."], 0, "Similarity of findings, exactly.", "r"),
 q(CONV + P("The data, which had been collected over several <span class=blank></span> clear evidence that the river's temperature was rising."), ["decades, provided", "decades provided", "decades; provided", "decades, providing"], 0, "Close the \"which\" clause with a comma, then the main verb \"provided.\" \"providing\" leaves no main verb.", "b"),
]
EX = [
 q(CONV + P("The first public library in the colonies opened in <span class=blank></span> it lent books to anyone who paid a small fee."), ["1731, and", "1731", "1731,", "1731 and,"], 0, "Comma + FANBOYS between two independent clauses.", "b"),
 q(CONV + P("Each of the students <span class=blank></span> required to submit a project."), ["is", "are", "were being", "have been"], 0, "\"Each\" is singular.", "f"),
 q(CONV + P("The festival features music from three <span class=blank></span> Brazil, Ghana and Japan."), ["countries:", "countries;", "countries, such as:", "countries"], 0, "Full sentence + list.", "b"),
 q(CONV + P("The orchestra will perform <span class=blank></span> final concert of the season on Friday."), ["its", "it's", "their", "they're"], 0, "Singular collective noun.", "f"),
 q(CONV + P("Biologist Tyrone Hayes <span class=blank></span> how certain chemicals affect frog development."), ["studies", "study", "studying", "to study"], 0, "Needs a main verb agreeing with a singular subject.", "f"),
 q(TR + P("The town is small. <span class=blank></span> it hosts one of the largest film festivals in the region."), ["Nonetheless,", "Therefore,", "Likewise,", "For example,"], 0, "Contrast.", "t"),
 q(TR + P("Sunflowers track the sun while young. <span class=blank></span> mature sunflowers face east all day."), ["By contrast,", "Similarly,", "Thus,", "For instance,"], 0, "Young vs. mature.", "t"),
 q(TR + P("The recipe calls for butter. <span class=blank></span> it uses 200 grams of it."), ["Specifically,", "However,", "Instead,", "Nevertheless,"], 0, "Adds precise detail.", "t"),
 q(CONV + P("After the storm <span class=blank></span> volunteers helped clear the roads."), ["passed,", "passed;", "passed:", "passed—and"], 0, "Introductory dependent clause → comma.", "b"),
 q(CONV + P("Looking through the telescope, <span class=blank></span>"), ["Ana saw Saturn's rings clearly.", "Saturn's rings were clear.", "the rings of Saturn appeared.", "it was clear to see Saturn's rings."], 0, "The looker must come after the comma.", "f"),
 q(notes(["The Atacama Desert in Chile is one of the driest places on Earth.", "Some weather stations there have never recorded rain.", "Astronomers build telescopes there because the dry, clear air helps viewing."], "explain why astronomers build telescopes in the Atacama"), ["Astronomers build telescopes in the Atacama because its dry, clear air helps viewing.", "The Atacama is in Chile.", "Some stations there have never recorded rain.", "Deserts are dry."], 0, "Gives the reason.", "r"),
 q(CONV + P("The bakery's bread, which is made <span class=blank></span> sells out by noon."), ["daily,", "daily", "daily;", "daily:"], 0, "Close the \"which\" clause.", "b"),
 q(CONV + P("Last year the city <span class=blank></span> a new bus route to the airport."), ["opened", "opens", "will open", "has been opening"], 0, "Last year = simple past.", "f"),
 q(TR + P("The experiment failed three times. <span class=blank></span> on the fourth try, the reaction worked."), ["Finally,", "For example,", "Similarly,", "In other words,"], 0, "Sequence: last in a series.", "t"),
 q(notes(["Zora Neale Hurston was a writer and anthropologist.", "She collected folklore in Florida and the Caribbean.", "Her novel <i>Their Eyes Were Watching God</i> was published in 1937."], "introduce Hurston to an audience unfamiliar with her"), ["Zora Neale Hurston, a writer and anthropologist, collected folklore and wrote the 1937 novel <i>Their Eyes Were Watching God</i>.", "Their Eyes Were Watching God was published in 1937.", "Hurston collected folklore in the Caribbean.", "The novel is set in Florida."], 0, "Identifies who she is for a new audience.", "r"),
]
for it in PQ + CHAL + EX:
    if any("<" in o for o in it["o"]): it["h"] = 1
build(C, "sat-3", L, 3, "Writing: Grammar and Expression", 'Grammar rules <span class="hl">that score</span>', "Punctuation and sentence boundaries, agreement, verbs and modifiers, transitions, and the notes questions.", "SAT Reading and Writing: Standard English Conventions and Expression of Ideas with animated fixes and practice.", CH, PQ, CHAL, EX, TAGS, OUT, minutes=15, exam_name="Writing set")
