from tp_common import *
C = "act"; L = "ACT"; OUT = "../../courses/act/act-7.html"
TAGS = {"w": "Writing"}

TASK = topic("task", "The task", f'''
<p>Optional, 40 minutes, one essay. You get a short description of an issue and <b>three perspectives</b> on it. You write an argument that states your own position and analyzes how it relates to at least one other perspective.</p>
{table(["Domain (each scored 2–12)", "What earns points"], [
 ["Ideas and Analysis", "A clear, precise thesis; engaging with the given perspectives, including the tension between them"],
 ["Development and Support", "Reasons and specific examples that explain <i>why</i> your position holds, plus limits or counterarguments"],
 ["Organization", "A logical structure with transitions; each paragraph has one job"],
 ["Language Use and Conventions", "Clear, varied sentences, precise words, few errors"]])}
<p>Two readers score each domain 1–6; the two scores add to 2–12. Your Writing score is the rounded average of the four domain scores.</p>
''', pill=("w", "7.1"))

PLAN = topic("plan", "A 40-minute plan", f'''
{pace([["Writing essay", 5, 40, "Think of these 5 \"questions\" as: plan (8 min), intro, body 1, body 2–3, conclusion + proofread."]], "Essay clock")}
{table(["Minutes", "Do"], [["0–8", "Read the prompt and perspectives. Choose a position (it can combine perspectives). List 2–3 reasons with one concrete example each. Note one counterargument."], ["8–14", "Introduction: context in one sentence, then a thesis that names your position and your main reasons."], ["14–34", "Body paragraphs: claim → explanation → example → link back to thesis. One paragraph addresses another perspective and shows its limits."], ["34–38", "Conclusion: restate the position more broadly; why it matters."], ["38–40", "Proofread for missing words and unclear sentences."]])}
''', pill=("w", "7.2"))

SAMPLE = topic("sample", "Practice prompt and model outline", f'''
<div class="passage"><p><b>Issue: Automation at work.</b> More jobs are being done by software and machines. Some people welcome the change; others worry about workers left behind.</p>
<p><b>Perspective One:</b> Automation frees people from dull, repetitive work so they can focus on creative and human tasks.</p>
<p><b>Perspective Two:</b> Automation helps companies but harms workers, whose skills become worthless overnight.</p>
<p><b>Perspective Three:</b> Whether automation helps or harms depends on whether society invests in retraining workers.</p></div>
{worked("Model thesis", "Automation can free people from repetitive work, as Perspective One argues, but only when communities pay for retraining; without it, Perspective Two's warning comes true. That's why the investment in Perspective Three decides the outcome.")}
{mini(("Body 1", "Benefit: a factory that automated packing moved workers into maintenance roles, with higher pay, <i>because</i> it trained them."), ("Body 2", "Risk: when a town's mill automated without retraining, workers lost jobs; this shows Perspective Two's concern is real, not inevitable."), ("Body 3 / counter", "Someone might say retraining is too slow or costly. But the cost of unemployment (lost taxes, public aid) is often higher."), ("Conclusion", "Automation itself is neither good nor bad. The choice to invest in people is what decides."))}
''', pill=("w", "7.3"))

PROMPT2 = '<div class="passage"><p><b>Issue: Phones in schools.</b> Many schools are debating whether students should be allowed to carry phones during the school day.</p><p><b>Perspective One:</b> Phones distract students and hurt learning; schools should collect them at the door.</p><p><b>Perspective Two:</b> Phones are tools. Banning them prevents students from learning to use technology responsibly.</p><p><b>Perspective Three:</b> Families need to reach students in emergencies, so any policy must allow contact.</p></div><p>Write a unified, coherent essay about phones in schools. In your essay, state and develop your own perspective, and explain the relationship between your perspective and at least one other perspective given. Then score yourself with the rubric.</p>'
FRQ = [{"q": PROMPT2, "parts": [
 {"p": "Your essay (aim for 4–5 paragraphs).", "rubric": [["Clear thesis that takes a position", 2], ["Engages with at least one other perspective and its limits", 2], ["Each body paragraph has a reason + specific example + explanation", 3], ["Logical order with transitions", 2], ["Clear sentences, few errors", 2], ["Conclusion that extends the argument", 1]], "answer": "See the model outline in the Sample chapter. A top essay names a precise position, explains WHY each reason is true with concrete examples, and shows where other perspectives fall short or fit."}]}]
html, d = exam_box("act-7", "Timed essay", [], 0, TAGS, "Essay", ["You have 40 minutes.", "Plan first. A clear position beats length.", "When time's up, use the rubric to score yourself honestly."], frq=FRQ, frq_minutes=40, desc="One essay, 40 minutes, then self-score with the rubric.")
for v in d.values(): v.update({"frqName": "Essay", "frqKind": "prompt"})
CH = [chapter("ch-task", "The Task", "Task", [TASK]), chapter("ch-plan", "Plan and Sample", "Plan", [PLAN, SAMPLE]), chapter("ch-essay", "Timed Essay", "Timed essay", [html])]
HTML = page("act-7", "ACT: Writing (optional essay)", "ACT · Part 7", 'The essay, <span class="hl">planned</span>', "How the optional ACT Writing essay is scored, a 40-minute plan, a model outline and a timed practice prompt.", "ACT Writing: scoring domains, a 40-minute plan, model outline and timed essay with rubric.", CH, d, course=C, footer="Crux · ACT prep · Not affiliated with ACT", extra_js=("tp.js",))
HTML = HTML.replace('<script src="../../assets/js/sims.js"></script>\n', "")
open(OUT, "w").write(HTML); print("act-7 written")
