from tp_common import *
C = "act"; L = "ACT"; OUT = "../../courses/act/act-5.html"
TAGS = {"m": "Main idea", "d": "Details", "i": "Inference", "w": "Word meaning", "p": "Purpose & structure", "c": "Comparing passages"}

def passage(title, kind, paras):
    body = "".join(f'<p><span class="ln">{i + 1}</span>{p}</p>' for i, p in enumerate(paras))
    return f'<div class="passage"><p><b>{kind}:</b> {title}</p>{body}</div>'
def inq(ptxt):  # passage inside a question (for the timed set)
    return f'<details class="qpass" open><summary>Show / hide passage</summary>{ptxt}</details>'

P1 = passage("The Repair Shop", "Literary Narrative", [
 "Every Saturday my grandfather unlocked the shop at seven, though no customer had ever arrived before nine. He said the first two hours belonged to the machines. He would walk the aisles of half-fixed radios and toasters, laying a hand on each one as if checking a fever.",
 "I was twelve the summer my mother sent me to help him. I had expected to be bored. Instead I learned that a broken thing tells you how it broke, if you are patient enough to listen. A scorch mark meant a short; a rattle meant a loose screw that had traveled; silence, the worst sign, meant the problem was somewhere you couldn't see.",
 "Customers rarely understood what he charged for. \"It was one wire,\" a man complained once, holding up his mended lamp. My grandfather nodded. \"The wire was a dollar,\" he said. \"Knowing which wire was the rest.\"",
 "Years later, after the shop closed and the building became a phone store, I stood across the street and watched teenagers carry out bright new devices in plastic bags. None of them, I thought, would ever be laid on a workbench and listened to. I felt something close to grief, and then, unexpectedly, something like gratitude, because I had been taught to listen at all.",
])
Q1 = [
 q("The passage is mainly about…", ["what the narrator learned from working in a grandfather's repair shop", "how to repair radios", "why the shop was sold", "the history of phone stores"], 0, "The narrator's lessons frame the whole passage.", "m"),
 q("According to the passage, a scorch mark indicated…", ["a short", "a loose screw", "a hidden problem", "a broken switch"], 0, "Paragraph 2.", "d"),
 q("The grandfather's reply to the complaining customer suggests that he believed…", ["expertise is the real value of his work", "the customer was dishonest", "wires are expensive", "the lamp couldn't be fixed"], 0, "\"Knowing which wire was the rest.\"", "i"),
 q("As used in paragraph 1, \"belonged to\" most nearly means…", ["were set aside for", "were owned by", "were stolen from", "were similar to"], 0, "The hours were reserved for the machines.", "w"),
 q("The last paragraph shifts from…", ["grief to gratitude", "anger to humor", "confusion to certainty", "excitement to boredom"], 0, "Stated directly.", "p"),
 q("Why does the narrator describe silence as \"the worst sign\"?", ["Because it meant the problem was hidden", "Because it meant the machine was new", "Because customers disliked it", "Because the shop was closing"], 0, "\"somewhere you couldn't see.\"", "d"),
 q("The narrator's attitude toward the summer at the shop, before it began, was…", ["expecting to be bored", "eager excitement", "fear", "indifference to the grandfather"], 0, "\"I had expected to be bored.\"", "d"),
]
P2 = passage("Why Cities Have Heat Islands", "Natural Science", [
 "On a summer afternoon, a downtown street can be several degrees hotter than a park just a few kilometers away. Scientists call this an urban heat island. The main cause is surface: dark asphalt and roofs absorb most of the sunlight that hits them, while grass and trees reflect more of it and cool the air as water evaporates from their leaves.",
 "Buildings make the problem worse at night. Concrete and brick store heat during the day and release it slowly after sunset, so cities cool off less than the countryside. Tall buildings also block wind that would otherwise carry warm air away.",
 "The effects are not just uncomfortable. Hotter nights mean more electricity for air conditioning, and heat waves are more dangerous in neighborhoods with few trees. Because these neighborhoods are often lower-income, researchers increasingly describe heat as a question of fairness as well as of weather.",
 "Some cities are responding with \"cool roofs\" painted white, new tree planting, and pavement that reflects more light. Early measurements are encouraging: one study found that reflective pavement lowered surface temperatures by about 10°C, though the air just above it changed much less.",
])
Q2 = [
 q("The main purpose of the passage is to…", ["explain the causes, effects and possible fixes of urban heat islands", "argue that cities should be abandoned", "describe one city's weather", "compare asphalt to brick"], 0, "Cause, effects, responses.", "m"),
 q("According to the passage, why do cities cool off less at night?", ["Building materials release stored heat slowly", "There are more people at night", "Trees release heat", "Asphalt reflects moonlight"], 0, "Paragraph 2.", "d"),
 q("The passage suggests heat is \"a question of fairness\" because…", ["lower-income neighborhoods often have fewer trees and face more danger", "everyone pays the same for electricity", "rich areas are hotter", "scientists disagree about heat"], 0, "Paragraph 3.", "i"),
 q("The study of reflective pavement found that…", ["surface temperatures fell much more than air temperatures", "air temperatures fell by 10°C", "it made streets hotter", "it was too expensive"], 0, "\"the air just above it changed much less.\"", "d"),
 q("As used in paragraph 4, \"encouraging\" most nearly means…", ["promising", "persuading", "cheering loudly", "required"], 0, "Results look hopeful.", "w"),
 q("Paragraph 2 mainly serves to…", ["add a second cause that works at night", "give the passage's conclusion", "introduce cool roofs", "describe a study's method"], 0, "Builds on paragraph 1's cause.", "p"),
]
P3a = passage("On Practice (Passage A)", "Humanities", [
 "Musicians often speak of \"ten thousand hours\" as the price of mastery. But hours alone teach little. A violinist who plays the same piece badly for an hour has practiced playing it badly. What matters is deliberate practice: slow work on the exact passages that cause trouble, with constant attention to mistakes.",
])
P3b = passage("On Practice (Passage B)", "Humanities", [
 "Deliberate practice is valuable, but it is not the whole story. Many great performers describe long stretches of play: improvising, exploring, playing pieces just for the joy of it. That freedom keeps motivation alive over years. A student who only drills weaknesses may become skilled, but may also stop loving the instrument.",
])
Q3 = [
 q("Passage A's author would most likely agree that…", ["focused work on problem spots matters more than total hours", "ten thousand hours guarantees mastery", "improvising is the best practice", "talent matters more than practice"], 0, "A's whole point.", "m"),
 q("Passage B's author mentions \"playing pieces just for the joy of it\" to…", ["show another valuable part of a musician's growth", "criticize lazy students", "define deliberate practice", "prove A is entirely wrong"], 0, "B adds to A rather than rejecting it.", "p"),
 q("How would the author of Passage B most likely respond to Passage A?", ["Deliberate practice helps, but motivation from free play matters too", "Deliberate practice is useless", "Hours are all that matter", "Only drills create skill"], 0, "\"Valuable, but not the whole story.\"", "c"),
 q("Both passages agree that…", ["deliberate practice has value", "hours alone produce mastery", "students should stop drilling", "free play is the only path"], 0, "B: \"Deliberate practice is valuable.\"", "c"),
]
STRAT = topic("approach", "How to attack a passage", f'''
<ol class="steps"><li><b>Skim with purpose</b> (3 minutes): read the intro blurb, the first and last sentence of each paragraph, and note the main idea and the author's attitude.</li>
<li><b>Answer \"line\" questions first</b>; they're quick and teach you the passage.</li>
<li><b>Go back to the text for every answer.</b> Find the sentence that proves it.</li>
<li><b>Paired passages:</b> do Passage A's questions, then B's, then the questions about both.</li></ol>
{table(["Trap answer", "Looks like"], [["Too extreme", "always, never, completely, proves"], ["True but irrelevant", "a real detail that doesn't answer this question"], ["Twisted detail", "the right words from the passage, wrong relationship"], ["Outside knowledge", "sounds smart but isn't in the passage"]])}
{hl("Find the proof", [
 {"claim": "Question: Why did the grandfather open the shop two hours before customers came?", "sents": ["Every Saturday my grandfather unlocked the shop at seven,", "though no customer had ever arrived before nine.", "He said the first two hours belonged to the machines.", "He would walk the aisles of half-fixed radios and toasters."], "a": 2, "x": "The reason he gives: the hours belonged to the machines."}
])}
''', pill=("p", "5.1"))

PA = topic("set1", "Passage set 1: literary narrative", P1)
PB = topic("set2", "Passage set 2: natural science", P2)
PC = topic("set3", "Passage set 3: paired passages", P3a + P3b)
data = {"quiz-rd1": balance(check(Q1), 1), "quiz-rd2": balance(check(Q2), 2), "quiz-rd3": balance(check(Q3), 3)}
CH = [chapter("ch-approach", "The Approach", "Approach", [STRAT]),
      chapter("ch-set1", "Literary Narrative", "Narrative", [PA, quiz_section("q-set1", "Questions: passage set 1", "Answer from the passage above.", "quiz-rd1", TAGS)]),
      chapter("ch-set2", "Natural Science", "Science passage", [PB, quiz_section("q-set2", "Questions: passage set 2", "Answer from the passage above.", "quiz-rd2", TAGS)]),
      chapter("ch-set3", "Paired Passages", "Paired", [PC, quiz_section("q-set3", "Questions: passage set 3", "Answer from the passages above.", "quiz-rd3", TAGS)])]

P4 = passage("The Postcard Economy", "Social Science", [
 "In the early 1900s, Americans mailed postcards the way people now send text messages. In 1908 alone, the U.S. Post Office handled roughly 700 million postcards, at a time when the country's population was about 89 million. Cards were cheap, mail was delivered up to twice a day in many cities, and a short note could arrive the same afternoon.",
 "Historians argue that the postcard craze changed more than communication. Small-town photographers found a new market selling images of local main streets and train stations, and many families saw pictures of distant places for the first time. Some critics of the era complained that the short messages were making people careless writers, a worry that sounds familiar today.",
 "The craze faded by the 1920s, as telephones spread and the price of postage rose. But the cards remain valuable to researchers, who use them to study how towns looked, what people found worth photographing, and how ordinary people wrote to one another.",
])
EX = [
 q(inq(P4) + "The main idea of the passage is that early-1900s postcards…", ["were a popular, fast form of communication with lasting historical value", "were too expensive for most people", "were invented by photographers", "caused the telephone to be invented"], 0, "Popularity + effects + value to researchers.", "m"),
 q(inq(P4) + "According to the passage, one reason postcards could arrive quickly was that…", ["mail was delivered up to twice a day in many cities", "they were sent by telegraph", "they were carried by train only", "they weighed nothing"], 0, "Paragraph 1.", "d"),
 q(inq(P4) + "The comparison to text messages in paragraph 1 mainly serves to…", ["help modern readers understand how common postcards were", "argue that texting is harmful", "explain how postcards were printed", "criticize the Post Office"], 0, "Familiar analogy.", "p"),
 q(inq(P4) + "The detail about critics who said people were becoming \"careless writers\" suggests that…", ["worries about new forms of communication are not new", "postcards ruined American writing", "critics preferred telephones", "the critics were photographers"], 0, "\"Sounds familiar today.\"", "i"),
 q(inq(P4) + "According to the passage, which factor helped end the postcard craze?", ["The spread of telephones", "A ban on photographs", "A shortage of paper", "The end of mail delivery"], 0, "Paragraph 3.", "d"),
 q(inq(P4) + "As used in paragraph 2, \"market\" most nearly means…", ["group of buyers", "outdoor stall", "stock exchange", "advertisement"], 0, "Photographers found new buyers.", "w"),
 q(inq(P4) + "It can reasonably be inferred that in 1908 the average American received…", ["several postcards a year", "no postcards", "one postcard a decade", "a postcard every day"], 0, "700 million / 89 million ≈ 8 per person.", "i"),
 q(inq(P1) + "The grandfather's habit of laying a hand on each machine is described in a way that compares the machines to…", ["patients", "pets", "students", "customers"], 0, "\"As if checking a fever.\"", "i"),
 q(inq(P1) + "The phone store in the final paragraph mainly represents…", ["a world where things are replaced rather than repaired", "the narrator's new job", "the grandfather's success", "a better kind of shop"], 0, "New devices that will never be \"listened to.\"", "p"),
 q(inq(P2) + "Which of the following is NOT mentioned as a response to heat islands?", ["Banning cars downtown", "Cool roofs", "Tree planting", "Reflective pavement"], 0, "Only cars aren't mentioned.", "d"),
]
check(EX)
build(C, "act-5", L, 5, "Reading", 'ACT Reading: <span class="hl">find the proof</span>', "A passage strategy, the trap answers to avoid, and full passage sets with questions, including paired passages.", "ACT Reading strategy with literary narrative, natural science, social science and paired passages plus practice questions.", CH, [], [], EX, TAGS, OUT, minutes=11, extra_data=data, exam_name="Reading set", rules=["10 questions in 11 minutes (ACT pace).", "Every question shows its passage; hide it once you know it.", "No penalty for guessing."])
