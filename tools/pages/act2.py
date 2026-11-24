from tp_common import *
C = "act"; L = "ACT"; OUT = "../../courses/act/act-2.html"
TAGS = {"p": "Punctuation", "u": "Grammar & usage", "s": "Sentence structure", "r": "Strategy & style"}
NC = "NO CHANGE"
def u(before, under, after=""):
    return psg(f"{before}<u>{under}</u>{after}")
B = "Which choice is best?"

INTRO = topic("how-english", "How ACT English works", f'''
<p>You read passages with parts underlined. For each, pick the best version; choice A is usually <b>NO CHANGE</b>. Some questions ask about the whole passage: adding or deleting a sentence, ordering paragraphs, or whether the essay met a goal.</p>
{mini(("Three checks, in order", "1) Is it grammatically correct? 2) Is it clear and concise? 3) Does it fit the paragraph's meaning and tone?"), ("Scan the choices first", "What changes between them tells you the rule being tested: commas? verb tense? wordiness?"))}
''', pill=("r", "2.0"))

PUNCT = topic("punct", "Punctuation", f'''
{table(["Mark", "Rule", "Example"], [
 ["Comma", "after intro elements; around nonessential info; before FANBOYS joining two sentences; between list items", "After lunch, we left. / My sister, a pilot, flew home."],
 ["Semicolon", "between two complete sentences (works like a period)", "I was late; the bus broke down."],
 ["Colon", "after a complete sentence, introducing a list, explanation or quote", "She had one goal: to win."],
 ["Dash", "like commas or a colon, but in matching pairs for interruptions", "The answer — surprisingly — was no."],
 ["Apostrophe", "possession or contraction (no apostrophe for plain plurals)", "the dog's bowl, the dogs' bowls, it's = it is"]])}
{steps("Is the info essential? Comma test", [
 ("a|My brother|s  b|,|e  c|Sam|v  d|,|e  e|lives in Ohio.", "If you have one brother, \"Sam\" is extra info → commas."),
 ("a|My brother|s  c|Sam|v  e|lives in Ohio.", "If you have several brothers, \"Sam\" tells which one → no commas."),
 ("f|The student|s  g|who won|v  e2|gets a prize.|s", "\"who won\" identifies which student: essential, no commas."),
])}
''', pill=("p", "2.1"))

GRAM = topic("grammar", "Grammar and usage", f'''
{mini(("Agreement", "Subject ↔ verb, pronoun ↔ noun. Skip the prepositional phrase to find the subject."),
      ("Verb tense", "Match the passage's time frame. Don't switch from past to present mid-paragraph without a reason."),
      ("Pronoun case", "Subject: I, he, she, we, they, who. Object: me, him, her, us, them, whom. \"Between you and me.\""),
      ("Comparisons", "Two things: -er / more. Three or more: -est / most. Compare like with like: \"Her score was higher than <b>Jo's</b>\" (not \"than Jo\")."),
      ("Idioms", "Preposition pairs: capable <b>of</b>, interested <b>in</b>, different <b>from</b>, comply <b>with</b>."),
      ("Adjective vs adverb", "Adverbs describe verbs: she sang <b>beautifully</b>, not beautiful."))}
{steps("Who vs whom", [
 ("a|The coach|s  b|who/whom|e  c|we admired|v  d|retired.", "Rewrite the clause as a sentence: \"we admired ___.\""),
 ("c|We admired|v  e|him|g", "It's \"him\" (object), so use whom."),
 ("a|The coach|s  f|whom|g  c|we admired|v  d|retired.", "him → whom, he → who."),
])}
''', pill=("u", "2.2"))

STRUCT = topic("structure", "Sentence structure", f'''
{mini(("Run-ons and splices", "Two sentences need a period, semicolon, or comma + FANBOYS."), ("Fragments", "Every sentence needs a subject and a main verb. \"Because it rained.\" is a fragment."), ("Modifiers", "Put describing phrases next to what they describe."), ("Parallelism", "Lists match in form: \"to run, to swim, and <b>to bike</b>,\" not \"and biking.\""))}
{steps("Make the list parallel", [
 ("a|She likes|s  b|hiking,|v  c|to swim,|e  d|and biking.|v", "Two -ing words and one \"to\" verb: not parallel."),
 ("a|She likes|s  b|hiking,|v  e|swimming,|g  d|and biking.|v", "All -ing. Parallel."),
])}
''', pill=("s", "2.3"))

STYLE = topic("style", "Strategy, organization and style", f'''
<p>These are most of the English section. They ask what the writer <b>should do</b>.</p>
{table(["Question type", "How to answer"], [
 ["\"Should the writer add this sentence?\"", "Yes only if it directly supports the paragraph's point. Pick the choice with the right reason."],
 ["\"If the writer deleted this, the paragraph would lose…\"", "Name exactly what the sentence does (an example, a transition, a definition)."],
 ["\"Which choice best introduces/concludes the paragraph?\"", "Read the whole paragraph; the right choice previews or sums up its main idea."],
 ["\"Where should sentence 4 be placed?\"", "Look for pronouns and time words that link sentences: \"this,\" \"then,\" \"after that.\""],
 ["\"Which choice is most concise?\" / redundancy", "Cut repeated meanings: \"in my opinion I think,\" \"annual yearly.\""],
 ["Transitions", "Name the relationship first: contrast, cause, example, addition, time."],
 ["\"Suppose the writer's goal was…\"", "Did the essay do exactly that? Choose yes/no + the reason that matches the essay."]])}
{steps("Cut the redundancy", [
 ("a|The annual festival|s  b|is held every year|e  c|in July.", "\"Annual\" already means every year."),
 ("a|The annual festival|s  d|is held|g  c|in July.", "Shorter, same meaning. On the ACT, that usually wins."),
])}
''', pill=("r", "2.4"))

CH = [chapter("ch-how", "How It Works", "Basics", [INTRO]), chapter("ch-conv", "Conventions", "Grammar", [PUNCT, GRAM, STRUCT]), chapter("ch-style", "Writing Strategy and Style", "Style", [STYLE])]

PQ = [
 q(u("The old lighthouse ", "which was built in 1871", " still guides ships."), [NC, ", which was built in 1871,", ", which was built in 1871", "which was built in 1871,"], 1, "Nonessential info: commas on both sides.", "p"),
 q(u("We packed everything we needed for the ", "trip; tents,", " food, and maps."), [NC, "trip: tents,", "trip, tents,", "trip. Tents,"], 1, "Complete sentence + list → colon.", "p"),
 q(u("The ", "players's", " uniforms were washed after the game."), [NC, "players'", "player's", "players"], 1, "Plural possessive.", "p"),
 q(u("A box of old letters ", "were found", " in the attic."), [NC, "was found", "have been found", "are found"], 1, "Subject: box.", "u"),
 q(u("Last summer, my cousin ", "visits", " us for two weeks."), [NC, "visited", "will visit", "is visiting"], 1, "Past time.", "u"),
 q(u("The prize was split between Ana and ", "I", "."), [NC, "me", "myself", "mine"], 1, "Object of \"between.\"", "u"),
 q(u("The new phone is ", "more faster than", " the old one."), [NC, "faster than", "more fast then", "fastest than"], 1, "Faster already compares.", "u"),
 q(u("The bakery opened at ", "dawn the", " line already stretched around the block."), [NC, "dawn, and the", "dawn the,", "dawn, the"], 1, "Two sentences: comma + and.", "s"),
 q(u("", "Because the road was icy.", " We drove slowly."), [NC, "Because the road was icy, we", "The road was icy, we", "Because the road was icy; we"], 1, "Fix the fragment by joining it.", "s"),
 q(u("The program teaches students to code, to design, and ", "how they can present", " their work."), [NC, "to present", "presenting", "for presenting"], 1, "Parallel \"to\" verbs.", "s"),
 q(u("In my opinion, ", "I think that", " the rule is unfair."), [NC, "it seems to me that I think", "I personally think that", "DELETE the underlined portion."], 3, "\"In my opinion\" already says it.", "r"),
 q(u("The volcano erupted without warning. ", "Similarly,", " nearby towns had no time to evacuate."), [NC, "As a result,", "For example,", "However,"], 1, "Cause → effect.", "r"),
 q(psg("[1] Marta opened a small bakery in 2015. [2] At first, she baked only bread. [3] Today the bakery sells pastries, cakes and coffee. [4] Over time, customers asked for sweets, so she added them.") + "For the paragraph to be most logical, sentence 4 should be placed…", ["after sentence 2", "where it is now", "before sentence 1", "after sentence 1"], 0, "\"Over time\" bridges \"at first\" and \"today.\"", "r"),
 q(psg("The writer is considering adding this sentence to a paragraph about how bees pollinate crops: \"My uncle is allergic to bee stings.\"") + "Should the writer add it?", ["No, because it's unrelated to pollination", "Yes, because it adds a personal detail", "Yes, because it explains pollination", "No, because it's too long"], 0, "Off-topic.", "r"),
]
CHAL = [
 q(u("The scientist ", "whom", " the committee believed had made the discovery declined the award."), [NC, "who", "which", "whose"], 1, "\"the committee believed ___ had made\": he had made → who.", "u"),
 q(u("Neither the manager nor the employees ", "was", " told about the change."), [NC, "were", "has been", "is"], 1, "Closer subject: employees → were.", "u"),
 q(u("Walking into the gym, ", "the smell of popcorn surprised us.", ""), [NC, "we were surprised by the smell of popcorn.", "the popcorn smell was surprising to us.", "surprising us was the smell of popcorn."], 1, "We walked in, so \"we\" follows the comma.", "s"),
 q(u("The study, published in ", "2019 found", " that teens sleep less than they need."), [NC, "2019, found", "2019; found", "2019 — found"], 1, "Close the pair of commas.", "p"),
 q(psg("Suppose the writer's goal was to write an essay explaining how a bill becomes a law. The essay describes the writer's visit to the state capitol and the building's architecture.") + "Does the essay accomplish this goal?", ["No, because it focuses on a visit and architecture, not the lawmaking process", "Yes, because it mentions the capitol", "Yes, because it describes the building in detail", "No, because it's too short"], 0, "Goal not met; give the matching reason.", "r"),
 q(u("Her research focused on the migration of monarch butterflies, ", "insects that", " travel up to 4,800 km each fall."), [NC, "insects, they", "insects who", "they are insects that"], 0, "Appositive \"insects that travel…\" correctly renames the butterflies.", "s"),
]
EX = [
 q(u("Despite the ", "rain the", " game continued."), [NC, "rain, the", "rain; the", "rain: the"], 1, "Comma after an introductory phrase.", "p"),
 q(u("The ", "childrens'", " books were on the lowest shelf."), [NC, "children's", "childrens", "childs'"], 1, "Children is already plural: children's.", "p"),
 q(u("The team ", "celebrated their", " victory with a parade."), [NC, "celebrated its", "celebrates their", "celebrating its"], 1, "Team (one unit) → its.", "u"),
 q(u("She runs ", "quicker", " than anyone on the team."), [NC, "more quickly", "more quicker", "quickest"], 1, "Adverb describing runs.", "u"),
 q(u("The results were different ", "than", " what we expected."), [NC, "from", "then", "to"], 1, "Idiom: different from.", "u"),
 q(u("I studied all night, ", "I", " still felt unprepared."), [NC, "but I", "however I", "I, however,"], 1, "Comma splice → add FANBOYS.", "s"),
 q(u("The museum offers tours, workshops, and ", "you can attend lectures", "."), [NC, "lectures", "attending lectures", "lectures can be attended"], 1, "Parallel nouns.", "s"),
 q(u("The ", "final end", " of the movie surprised everyone."), [NC, "end", "final ending conclusion", "ultimate final end"], 1, "Redundant.", "r"),
 q(u("Many birds migrate south in winter. ", "For example,", " the Arctic tern flies from pole to pole each year."), [NC, "However,", "Therefore,", "In contrast,"], 0, "An example follows.", "r"),
 q(psg("A paragraph explains why the town built a new library. The writer considers ending it with: \"The library now serves 5,000 visitors a month, showing how much the town needed it.\"") + "Should the writer add this sentence?", ["Yes, because it shows the result that supports the paragraph's point", "No, because it introduces a new topic", "No, because numbers don't belong in essays", "Yes, because it describes the building"], 0, "Supports why it was needed.", "r"),
 q(u("It's important to give the dog ", "it's", " medicine on time."), [NC, "its", "its'", "their"], 1, "Possessive its.", "p"),
 q(u("The concert, which lasted three hours, ", "were", " a huge success."), [NC, "was", "have been", "being"], 1, "Subject: concert.", "u"),
 q(u("The recipe, ", "passed down from my grandmother", " uses only five ingredients."), [NC, "passed down from my grandmother,", "passed down, from my grandmother", "passed down from my grandmother;"], 1, "Close the commas.", "p"),
 q(u("The proposal was ", "approved by the council unanimously with everyone voting yes", "."), [NC, "unanimously approved by the council", "approved by the council, unanimously, all yes", "approved with all council members unanimously agreeing"], 1, "Unanimously already means everyone voted yes.", "r"),
 q(u("Before the storm hit, the farmers ", "had harvested", " most of the corn."), [NC, "harvest", "will harvest", "have harvest"], 0, "Past before past: had harvested is correct.", "u"),
]
build(C, "act-2", L, 2, "English", 'ACT English, <span class="hl">rule by rule</span>', "Punctuation, grammar and usage, sentence structure, and the strategy and style questions that make up most of the section.", "ACT English: punctuation, grammar, sentence structure, rhetorical skills with animated fixes and practice.", CH, PQ, CHAL, EX, TAGS, OUT, minutes=11)
