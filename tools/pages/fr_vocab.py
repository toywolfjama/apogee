import json
from fr_common import *
from fr_words import parse

W = parse()
APP = topic("word-bank", f"The {len(W):,} most common French words", f'''
<p>These words make up most of what you'll hear and read in everyday French. They're listed <b>roughly</b> in order of how often they're used, so the first few hundred give you the most for your effort. Tap any French word to hear it. Nouns show their gender: <span class="vb-pos p-nm">m.</span> masculine, <span class="vb-pos p-nf">f.</span> feminine.</p>
<p>To test yourself, turn on <b>Hide English</b> and tap a meaning to check it, or press <b>Quiz me</b> for 10 multiple-choice questions from whatever you've filtered (a range, a word type or a search).</p>
<div class="cslab frlab vb" data-lab='{{"type":"vocab"}}'></div>
<script type="application/json" id="fr-words">{json.dumps(W, ensure_ascii=False)}</script>
''', sub="Search, filter, listen and quiz yourself.")

TIPS = topic("vocab-tips", "How to actually remember words", f'''
<ol class="steps">
<li><b>Learn nouns with their article.</b> Not "maison" but {F("une maison")}. The gender is part of the word.</li>
<li><b>Say every word out loud</b> after you hear it. Saying words aloud makes them stick much better than reading silently.</li>
<li><b>Small batches, often.</b> Ten words a day for ten days beats a hundred the night before a test. Use the 1–100, 101–200… ranges.</li>
<li><b>Test yourself before you feel ready.</b> Hide the English or take a 10-word quiz. Trying to remember is what makes a word stick.</li>
<li><b>Come back to your misses.</b> The quiz lists the words you got wrong; quiz those again the next day.</li>
<li><b>Use the word in a sentence about you.</b> {F("J'ai besoin d'un nouveau téléphone.")} A word tied to your own life is easier to recall.</li>
<li><b>Watch for cognates and false friends.</b> Many words look like English: {F("important")}, {F("la musique")}, {F("la date")}. But some don't mean what they look like: {F("la librairie")} is a bookstore (a library is {F("la bibliothèque")}), and {F("actuel")} means current, not actual.</li></ol>
''', sub="What works, and what doesn't.")

CH = [chapter("words-fv", "1,000 words", "Word bank", [APP]), chapter("tips-fv", "Study tips", "Tips", [TIPS])]
HTML = page("vocab", "French 1: The 1,000 most common words", "French 1 · Word bank", 'Les mots <span class="hl">essentiels</span>',
            f"The {len(W):,} most common French words with audio, gender and meaning. Search them, filter them by type or by group of 100, and quiz yourself.",
            "The 1,000 most common French words with audio, search, filters and quizzes.", CH, {}, course="french-1", footer=FOOT, extra_js=("wa.js", "fr.js"))
HTML = HTML.replace('<script src="../../assets/js/sims.js"></script>\n', "")
open("/home/claude/ap-physics-study/courses/french-1/vocab.html", "w").write(HTML)
print("vocab page:", len(W))
