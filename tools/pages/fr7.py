from fr_common import *

CH = []
CORE = f'''<p>Time to go shopping. In this unit you learn clothing, how to point things out (<i>this shirt, these shoes</i>), how to compare (<i>cheaper than, the best</i>), and how to handle a conversation in a store.</p>
{wa("Comparing", [
 ("a|Le pull|s  v|est|v  b|cher.|x", "The sweater is expensive.", "The sweater is expensive."),
 ("a|Le pull|s  v|est|v  c|plus|n  b|cher|x  d|que|n  e|le t-shirt.|s", "plus + adjective + que = more … than.", "The sweater is more expensive than the T-shirt."),
 ("a|Le pull|s  v|est|v  c|le plus|n  b|cher|x  e2|du magasin.|s", "le plus + adjective = the most. de + le = du.", "The sweater is the most expensive in the store.")])}
<div class="grid2"><div class="mini"><h4>In this unit</h4><p>Clothing and accessories · porter and mettre · ce, cet, cette, ces · shopping phrases · comparatives and superlatives · meilleur and mieux.</p></div>
<div class="mini"><h4>Practice idea</h4><p>Each morning, say what you're wearing: {F("Aujourd'hui, je porte un jean bleu et un pull gris.")}</p></div></div>'''
CH.append(chapter("overview-f7", "Overview", "Overview", [topic("core-f7", "Les vêtements et les courses", CORE)]))

CLOTHES = topic("clothes", "Clothing", f'''
{vgrid([("le t-shirt", "T-shirt"), ("la chemise", "shirt"), ("le chemisier", "blouse"), ("le pull", "sweater"), ("le sweat", "sweatshirt, hoodie"), ("la veste", "jacket"), ("le manteau", "coat"), ("l'imperméable (m.)", "raincoat"), ("le pantalon", "pants"), ("le jean", "jeans"), ("le short", "shorts"), ("la jupe", "skirt"), ("la robe", "dress"), ("le costume", "suit"), ("la cravate", "tie"), ("le maillot de bain", "swimsuit"), ("le pyjama", "pajamas")])}
<h3>Shoes and accessories</h3>
{vgrid([("les chaussures (f.)", "shoes"), ("les baskets (f.)", "sneakers"), ("les bottes (f.)", "boots"), ("les sandales (f.)", "sandals"), ("les chaussettes (f.)", "socks"), ("le chapeau", "hat"), ("la casquette", "cap"), ("l'écharpe (f.)", "scarf"), ("les gants (m.)", "gloves"), ("la ceinture", "belt"), ("le sac", "bag"), ("les lunettes (f.)", "glasses"), ("la montre", "watch"), ("les boucles d'oreilles (f.)", "earrings")])}
<h3>Describing clothes</h3>
{vgrid([("en coton", "cotton"), ("en laine", "wool"), ("en cuir", "leather"), ("à rayures", "striped"), ("à carreaux", "checked, plaid"), ("à fleurs", "flowered"), ("uni(e)", "solid-colored"), ("serré(e)", "tight"), ("large", "loose, baggy"), ("à la mode", "in style"), ("démodé(e)", "out of style"), ("chic", "stylish")])}
{ex("Il porte un pantalon noir et une chemise à rayures.", "He's wearing black pants and a striped shirt.")}
{box("trap", "Singular in French", f"{F('le pantalon')}, {F('le jean')} and {F('le short')} are singular in French even though English says <i>pants, jeans, shorts</i>: {F('Mon jean est trop grand.')}")}
''', pill=("v", "7.1"), sub="Les vêtements et les accessoires.")

WEAR = topic("porter-mettre", "Porter and mettre", f'''
<p>{F("porter")} means <i>to wear</i> (a regular -er verb). {F("mettre")} means <i>to put on</i> (irregular).</p>
<div class="tblwrap"><table class="conj"><tr><td>{F("je mets")}</td><td>{F("nous mettons")}</td></tr>
<tr><td>{F("tu mets")}</td><td>{F("vous mettez")}</td></tr>
<tr><td>{F("il / elle met")}</td><td>{F("ils / elles mettent")}</td></tr></table></div>
{lab(type="conj", verbs=["porter", "mettre", "acheter", "choisir", "vendre"], tenses=["pres", "pc"])}
{ex("Qu'est-ce que tu portes à la fête ?", "What are you wearing to the party?")}
{ex("Il fait froid : mets ton manteau !", "It's cold: put on your coat!")}
{ex("Hier, j'ai mis ma nouvelle robe.", "Yesterday I put on my new dress. (mettre → mis)")}
<h3>Acheter and préférer</h3>
<p>These -er verbs change their accent in the je, tu, il and ils forms: {F("j'achète, tu achètes, il achète, nous achetons, vous achetez, ils achètent")}. Same idea with {F("je préfère")} / {F("nous préférons")}.</p>
''', pill=("g", "7.2"), sub="What you wear and what you put on.")
CH.append(chapter("clothes-f7", "Les vêtements: Clothes", "Clothes", [CLOTHES, WEAR]))

DEM = topic("demonstratives", "This and that: ce, cet, cette, ces", f'''
<div class="tblwrap"><table><tr><th>Masculine</th><th>Masculine + vowel</th><th>Feminine</th><th>Plural</th></tr>
<tr><td>{F("ce pull")}</td><td>{F("cet imperméable")}</td><td>{F("cette robe")}</td><td>{F("ces chaussures")}</td></tr></table></div>
<p>Like the articles, the demonstrative agrees with the noun. <b>cet</b> exists so the words link smoothly before a vowel sound; it sounds just like cette.</p>
{lab(type="noun", rows=[1, 6, 0], nouns=["chemise", "pantalon", "robe", "manteau", "pull", "jupe", "écharpe", "imperméable", "chaussure", "chapeau", "ordinateur", "hôtel"])}
<h3>This one or that one?</h3>
<p>To contrast, add <b>-ci</b> (here) or <b>-là</b> (there) to the noun: {F("Je préfère cette veste-ci, pas cette veste-là.")} In everyday speech, people usually just say {F("cette veste")} and point.</p>
{ex("Combien coûte ce manteau ?", "How much is this coat?")}
{ex("Ces baskets sont super !", "These sneakers are great!")}
''', pill=("g", "7.3"), sub="Pointing things out.")

SHOP = topic("shopping", "In a store", f'''
{vt([("Je peux vous aider ?", "Can I help you?", "what the salesperson says"), ("Je cherche un pull.", "I'm looking for a sweater."), ("Quelle taille faites-vous ?", "What size are you?", "for clothes"), ("Quelle est votre pointure ?", "What's your shoe size?"), ("Je fais du 38.", "I'm a size 38."), ("Je peux l'essayer ?", "Can I try it on?"), ("Où sont les cabines d'essayage ?", "Where are the fitting rooms?"), ("C'est trop petit / trop grand.", "It's too small / too big."), ("Ça vous va très bien.", "It looks great on you."), ("Ça coûte combien ? / C'est combien ?", "How much is it?"), ("C'est trop cher !", "It's too expensive!"), ("C'est en solde.", "It's on sale."), ("Je le prends. / Je la prends.", "I'll take it."), ("Vous payez comment ?", "How are you paying?"), ("par carte / en espèces", "by card / in cash")])}
{ex("— Je peux vous aider ? — Oui, je cherche une veste en cuir, taille M.", "— Can I help you? — Yes, I'm looking for a leather jacket, size M.")}
{ex("Cette robe coûte quatre-vingt-dix euros. C'est un peu cher, mais elle est en solde.", "This dress costs 90 euros. It's a bit expensive, but it's on sale.")}
{box("plain", "Sizes", "European clothing sizes are different: a US women's size 8 is roughly a French 40, and a US men's shoe size 10 is about a French 43–44. Many stores also use S, M, L.")}
''', pill=("v", "7.4"), sub="Asking for sizes, trying things on, paying.")
CH.append(chapter("shop-f7", "Au magasin: Shopping", "Shopping", [DEM, SHOP]))

COMP = topic("comparisons", "Comparing: plus, moins, aussi", f'''
<div class="tblwrap"><table><tr><th>Pattern</th><th>Meaning</th><th>Example</th></tr>
<tr><td>plus + adj. + que</td><td>more … than</td><td>{F("La robe est plus chère que la jupe.")}</td></tr>
<tr><td>moins + adj. + que</td><td>less … than</td><td>{F("Le t-shirt est moins cher que le pull.")}</td></tr>
<tr><td>aussi + adj. + que</td><td>as … as</td><td>{F("Paul est aussi grand que son père.")}</td></tr></table></div>
<p>The adjective still agrees with the first noun: {F("Ma sœur est plus grande que moi.")} After que, use a stress pronoun (moi, toi, lui, elle…).</p>
<h3>The most: superlatives</h3>
<p>Use <b>le / la / les + plus (or moins) + adjective</b>. "In" after a superlative is <b>de</b>.</p>
{ex("C'est la robe la plus chère du magasin.", "It's the most expensive dress in the store.")}
{ex("Ce sont les chaussures les moins chères.", "These are the cheapest shoes.")}
{ex("C'est le plus beau pull de la boutique.", "It's the nicest sweater in the shop. (BAGS adjectives can stay in front)")}
<h3>Bon and bien are irregular</h3>
<div class="tblwrap"><table><tr><th></th><th>Adjective (good)</th><th>Adverb (well)</th></tr>
<tr><td>better</td><td>{F("meilleur(e)")}</td><td>{F("mieux")}</td></tr>
<tr><td>the best</td><td>{F("le / la meilleur(e)")}</td><td>{F("le mieux")}</td></tr></table></div>
{ex("Ce magasin est meilleur que l'autre.", "This store is better than the other one. (never plus bon)")}
{ex("Elle chante mieux que moi.", "She sings better than me. (mieux describes the verb)")}
''', pill=("g", "7.5"), sub="plus … que, le plus, meilleur, mieux.",
 det=("Comparison details", '''<h4>Comparing quantities</h4><p>Use plus de / moins de / autant de + noun: <i>J'ai plus de chaussures que toi.</i> <i>Il a autant d'argent que moi.</i></p>
<h4>Comparing actions</h4><p>With verbs, put plus / moins / aussi before an adverb: <i>Il court plus vite que moi.</i> Or compare how much: <i>Je travaille plus que toi.</i></p>
<h4>Superlative position</h4><p>If the adjective normally goes after the noun, the superlative also goes after, and the article is repeated: <i>la robe la plus chère</i>. If it goes before (BAGS), the superlative goes before: <i>la plus belle robe</i>.</p>
<h4>pire</h4><p>The worst is usually <i>le plus mauvais</i> or <i>le pire</i>: <i>C'est le pire film de l'année.</i></p>'''))
CH.append(chapter("comp-f7", "Comparer: Comparisons", "Comparing", [COMP]))

REV = topic("review-f7", "Unit 7 summary", f'''<div class="grid2"><div class="mini"><h4>Clothes</h4><p>le pull, la chemise, le pantalon, la robe, les chaussures… porter (wear), mettre (put on: je mets, mis).</p></div>
<div class="mini"><h4>This / these</h4><p>ce pull, cet imperméable, cette robe, ces chaussures. -ci / -là to contrast.</p></div>
<div class="mini"><h4>Shopping</h4><p>Je cherche… Je fais du 38. Je peux l'essayer ? C'est combien ? Je le prends.</p></div>
<div class="mini"><h4>Comparing</h4><p>plus / moins / aussi + adj. + que. le plus … de. meilleur (good → better), mieux (well → better).</p></div></div>''', sub="Everything from this unit on one screen.")
MIS = topic("mistakes-f7", "Common mistakes", '''<ol class="steps">
<li><i>ce imperméable</i> → <i>cet imperméable</i>.</li>
<li><i>mes pantalons</i> for one pair of pants → <i>mon pantalon</i>.</li>
<li><i>plus bon</i> → <i>meilleur</i>.</li>
<li><i>Il chante meilleur que moi</i> → <i>Il chante mieux que moi</i>.</li>
<li><i>le plus cher dans le magasin</i> → <i>le plus cher du magasin</i>.</li>
<li><i>plus grand que je</i> → <i>plus grand que moi</i>.</li>
<li><i>j'acheté</i> / <i>nous achètons</i> → <i>j'achète</i> / <i>nous achetons</i>.</li></ol>''', sub="Points students lose most often.")
CH.append(chapter("review-ch-f7", "Review", "Review", [REV, MIS]))

PQ = [
 q("What do you wear on your feet?", ["des chaussures", "une écharpe", "une ceinture", "un chapeau"], 0, "les chaussures = shoes.", "v"),
 q("<i>une écharpe</i> is…", ["a scarf", "a belt", "a sweater", "a skirt"], 0, "écharpe = scarf.", "v"),
 q("It's raining. You need…", ["un imperméable", "un maillot de bain", "des sandales", "un short"], 0, "imperméable = raincoat.", "v"),
 q("<i>une chemise à rayures</i>", ["a striped shirt", "a flowered shirt", "a plaid shirt", "a leather shirt"], 0, "à rayures = striped.", "v"),
 q("<i>Mon jean ______ trop grand.</i>", ["est", "sont", "es", "ont"], 0, "le jean is singular in French.", "g"),
 q("<i>Il fait froid. Je ______ mon manteau.</i> (mettre)", ["mets", "met", "mettre", "mis"], 0, "je mets.", "g"),
 q("<i>Nous ______ des baskets.</i> (porter)", ["portons", "portez", "portent", "porte"], 0, "nous → -ons.", "g"),
 q("<i>Tu ______ une nouvelle robe ?</i> (acheter)", ["achètes", "achetes", "achètez", "acheté"], 0, "tu achètes (accent grave).", "g"),
 q("<i>Hier, il ______ un costume.</i> (mettre, passé composé)", ["a mis", "a mettu", "a mit", "est mis"], 0, "mettre → mis, with avoir.", "g"),
 q("<i>______ chapeau est joli.</i> (this)", ["Ce", "Cet", "Cette", "Ces"], 0, "chapeau: masculine, consonant → ce.", "g"),
 q("<i>______ écharpe est en laine.</i> (this)", ["Cette", "Cet", "Ce", "Ces"], 0, "écharpe is feminine → cette.", "g"),
 q("<i>______ imperméable</i> (this)", ["cet", "ce", "cette", "ces"], 0, "Masculine + vowel → cet.", "g"),
 q("<i>______ gants sont chauds.</i> (these)", ["Ces", "Ce", "Cettes", "Cet"], 0, "Plural → ces.", "g"),
 q("How do you ask to try something on?", ["Je peux l'essayer ?", "Je peux le payer ?", "C'est combien ?", "Ça vous va ?"], 0, "essayer = to try (on).", "v"),
 q("<i>C'est en solde</i> means…", ["It's on sale.", "It's sold out.", "It's alone.", "It's expensive."], 0, "en solde = on sale.", "v"),
 q("<i>Quelle est votre pointure ?</i> asks about…", ["shoe size", "clothing size", "favorite color", "price"], 0, "la pointure = shoe size.", "v"),
 q("<i>La veste est ______ chère ______ le manteau.</i> (less … than)", ["moins … que", "plus … que", "aussi … que", "moins … de"], 0, "moins + adj. + que.", "g"),
 q("<i>Ma sœur est plus grande que ______.</i>", ["moi", "je", "me", "mon"], 0, "Stress pronoun after que.", "g"),
 q("<i>Marie est aussi ______ que Paul.</i> (sportif)", ["sportive", "sportif", "sportifs", "sportives"], 0, "Agrees with Marie.", "g"),
 q("<i>Ce gâteau est ______ que l'autre.</i> (better)", ["meilleur", "plus bon", "mieux", "bien"], 0, "bon → meilleur.", "g"),
 q("<i>Elle danse ______ que moi.</i> (better)", ["mieux", "meilleur", "meilleure", "plus bien"], 0, "bien → mieux (with a verb).", "g"),
 q("<i>C'est le pull le plus cher ______ magasin.</i>", ["du", "dans le", "de le", "au"], 0, "Superlative + de (de + le = du).", "g"),
 q("<i>Je le prends</i> means…", ["I'll take it.", "I'm taking him out.", "I paid for it.", "I'm wearing it."], 0, "prendre = to take; le = it.", "v"),
 q(f"{listen('Ça coûte quarante-cinq euros.')} How much?", ["45 €", "55 €", "35 €", "40 €"], 0, "quarante-cinq = 45.", "v"),
]
CHAL = [
 q("Which is correct?", ["C'est la plus belle robe du magasin.", "C'est la robe la plus belle dans le magasin.", "C'est la plus bonne robe du magasin.", "C'est le plus belle robe du magasin."], 0, "BAGS adjective before, de for 'in'.", "g"),
 q("Which is correct?", ["Ce sont les chaussures les moins chères.", "Ce sont les moins chères chaussures les.", "Ce sont les chaussures moins chers.", "Ce sont les chaussures les moins cher."], 0, "Repeat the article, agree in feminine plural.", "g"),
 q("<i>J'ai ______ vêtements que ma sœur.</i> (fewer)", ["moins de", "moins des", "moins", "moins que"], 0, "Quantities: moins de + noun.", "g"),
 q("<i>Je préfère cette jupe-______.</i> (this one here)", ["ci", "là", "ce", "cet"], 0, "-ci = here, -là = there.", "g"),
 q("Which sentence is correct?", ["Nous achetons des baskets et vous achetez des bottes.", "Nous achètons des baskets et vous achètez des bottes.", "Nous achetons des baskets et vous achètez des bottes.", "Nous achètons des baskets et vous achetez des bottes."], 0, "No accent change in the nous and vous forms.", "g"),
 q("<i>Ce film est ______ de l'année.</i> (the worst)", ["le pire", "le plus pire", "le mieux", "le moins bon que"], 0, "le pire = the worst.", "g"),
 q("<i>Elles ______ leurs nouvelles robes hier.</i>", ["ont mis", "sont mises", "ont mises", "ont mettu"], 0, "mettre takes avoir, no agreement with the subject.", "g"),
 q("Which is <b>not</b> correct?", ["cet chemise", "cet hôtel", "cette amie", "ces écharpes"], 0, "chemise is feminine: cette chemise.", "g"),
]
EXQ = [
 q("<i>On porte ______ à la plage.</i>", ["un maillot de bain", "un manteau", "des bottes", "une écharpe"], 0, "Swimsuit at the beach.", "v", "vocab"),
 q("<i>la ceinture</i> is…", ["a belt", "a tie", "a watch", "a bag"], 0, "ceinture = belt.", "v", "vocab"),
 q("<i>Qu'est-ce que vous ______ ce soir ?</i> (mettre)", ["mettez", "mettons", "met", "mettent"], 0, "vous mettez.", "g", "gram"),
 q("<i>Ils ______ des lunettes.</i> (porter)", ["portent", "portez", "porte", "portons"], 0, "ils portent.", "g", "gram"),
 q("<i>J'______ un sweat hier.</i> (acheter)", ["ai acheté", "ai achète", "suis acheté", "achetais"], 0, "Passé composé with avoir.", "g", "gram"),
 q("<i>______ ordinateur est trop cher.</i> (this)", ["Cet", "Ce", "Cette", "Ces"], 0, "Masculine + vowel → cet.", "g", "gram"),
 q("<i>______ bottes sont en cuir.</i> (these)", ["Ces", "Cette", "Ce", "Cet"], 0, "Plural → ces.", "g", "gram"),
 q("Salesperson: <i>Quelle taille faites-vous ?</i> You answer:", ["Je fais du M.", "Je fais du sport.", "C'est trop cher.", "Par carte."], 0, "faire du + size.", "v", "vocab"),
 q("<i>Ça vous va très bien</i> means…", ["It looks great on you.", "You're doing very well.", "It's going very well.", "You go very well."], 0, "aller à quelqu'un = to suit someone.", "v", "vocab"),
 q("<i>Le jean est ______ cher ______ le pantalon.</i> (as … as)", ["aussi … que", "autant … que", "aussi … de", "si … comme"], 0, "aussi + adj. + que.", "g", "gram"),
 q("<i>Cette boutique est ______ que l'autre.</i> (better)", ["meilleure", "meilleur", "mieux", "plus bonne"], 0, "boutique is feminine → meilleure.", "g", "gram"),
 q("<i>Tu parles français ______ que moi !</i> (better)", ["mieux", "meilleur", "plus bien", "meilleure"], 0, "Describes the verb → mieux.", "g", "gram"),
 q(f"{listen('Je cherche une veste noire, taille quarante.')} What does the customer want?", ["A black jacket, size 40", "A black dress, size 14", "A white jacket, size 40", "A black coat, size 44"], 0, "une veste noire, taille quarante.", "v", "listen"),
 q("Read: <i>Léa a acheté une robe à fleurs pour la fête. Elle est plus jolie que la robe bleue, mais elle est aussi plus chère. Heureusement, elle était en solde !</i> Which is true?", ["The flowered dress was on sale.", "The blue dress is prettier.", "The flowered dress is cheaper.", "Léa bought a blue dress."], 0, "Heureusement, elle était en solde.", "v", "read"),
 q("Which is correct?", ["C'est le meilleur magasin de la ville.", "C'est le plus bon magasin de la ville.", "C'est le mieux magasin de la ville.", "C'est le meilleur magasin dans la ville."], 0, "le meilleur … de.", "g", "gram"),
]
FRQS = [
 {"q": "Write a dialogue in a clothing store (at least 6 lines).",
  "parts": [{"p": "The customer looks for something, gives a size, tries it on, asks the price, compares two items and buys one.",
   "rubric": [["Clothing vocabulary with correct gender", 1], ["Size and trying on (Je fais du…, Je peux l'essayer ?)", 1], ["Price asked and given with correct numbers", 1], ["A correct comparison (plus / moins / aussi … que or meilleur)", 1], ["A demonstrative (ce / cet / cette / ces) used correctly", 1], ["Polite register (vous, s'il vous plaît)", 1]],
   "answer": f'<div class="ex">{F("— Bonjour, je peux vous aider ?")}<span class="en">Hello, can I help you?</span></div><div class="ex">{F("— Oui, je cherche un pull en laine. Je fais du M.")}<span class="en">Yes, I\'m looking for a wool sweater. I\'m a medium.</span></div><div class="ex">{F("— Ce pull gris est très joli. Vous voulez l\'essayer ?")}<span class="en">This gray sweater is very nice. Do you want to try it on?</span></div><div class="ex">{F("— Oui, merci. Il coûte combien ?")}<span class="en">Yes, thanks. How much is it?</span></div><div class="ex">{F("— Soixante euros. Le pull bleu est moins cher : quarante euros.")}<span class="en">Sixty euros. The blue sweater is cheaper: forty euros.</span></div><div class="ex">{F("— Je préfère le gris, il est plus chaud. Je le prends !")}<span class="en">I prefer the gray one, it\'s warmer. I\'ll take it!</span></div>'}]},
 {"q": "Compare two people you know (at least 4 sentences).",
  "parts": [{"p": "Use plus … que, moins … que, aussi … que, and meilleur or mieux.",
   "rubric": [["Three different comparison structures", 2], ["Adjective agreement in each comparison", 1], ["meilleur or mieux used correctly", 1], ["Stress pronoun after que when comparing with yourself", 1]],
   "answer": f'<div class="ex">{F("Mon frère est plus grand que moi, mais il est moins sportif. Ma mère est aussi drôle que mon père. Ma sœur chante mieux que nous tous. C\'est la meilleure chanteuse de la famille !")}<span class="en">My brother is taller than me, but he\'s less athletic. My mom is as funny as my dad. My sister sings better than all of us. She\'s the best singer in the family!</span></div>'}]},
]

if __name__ == "__main__":
    build(7, "unit-7", "Clothes and shopping", 'Les vêtements <span class="hl">et les courses</span>',
          "Clothing, porter and mettre, ce / cet / cette / ces, shopping conversations, and comparisons with plus, moins, aussi, meilleur and mieux. Tap any French word to hear it.",
          "French 1 Unit 7: clothing, demonstratives, shopping and comparisons, with audio, interactive labs, practice questions and a practice exam.",
          CH, PQ, CHAL, EXQ, FRQS, "/home/claude/ap-physics-study/courses/french-1/unit-7.html")
