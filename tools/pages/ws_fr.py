from ws_common import M, build_ws

G1 = [
 M("fr-pairs", "Memory match", "Flip two cards at a time and match each French word with its English meaning. You'll hear every French word you turn over.",
   {"type": "pairs", "n": 6, "from": 0, "to": 160}, win="Hearing and seeing a word together makes it stick much faster than reading a list.",
   hints=["Remember where the cards were, even the wrong ones."]),
 M("fr-listen", "Écoute bien", "Listen to each French word and choose what it means. Use “Play again” as often as you like.",
   {"type": "listen", "mode": "meaning", "n": 8, "from": 0, "to": 260, "pass": 0.7}, win="Train your ear early: in real conversations you hear words long before you see them."),
 M("fr-dictee", "Dictée", "Listen and type the French word. Accents count, but you get half credit if only an accent is wrong.",
   {"type": "listen", "mode": "dictee", "n": 8, "from": 0, "to": 200, "pass": 0.6}, win="French spelling often hides silent letters: listen for the sounds, then remember the spelling rules.",
   hints=["You don't need to type le, la or un before the noun.", "Use the accent buttons under the box: é, è, ê, à, ç…"]),
]
G2 = [
 M("fr-pres", "Present tense sprint", "Ten conjugations in the present tense. Type the verb form (the subject is optional).",
   {"type": "conj", "verbs": ["être", "avoir", "aller", "faire", "parler", "finir", "vendre", "prendre"], "tenses": ["pres"], "n": 10, "pass": 7},
   win="Regular -er: e, es, e, ons, ez, ent. Être, avoir, aller and faire are irregular and worth memorizing cold.",
   hints=["parler → je parle, tu parles, il parle, nous parlons, vous parlez, ils parlent.", "être → suis, es, est, sommes, êtes, sont."]),
 M("fr-pc", "Passé composé", "Helper verb + past participle. Watch for verbs that take être.",
   {"type": "conj", "verbs": ["parler", "finir", "aller", "venir", "faire", "prendre", "voir", "partir", "se lever"], "tenses": ["pc"], "n": 10, "pass": 7},
   win="Most verbs use avoir. Movement verbs (aller, venir, partir…) and reflexive verbs use être, and their participle agrees with the subject.",
   hints=["aller, venir, partir and se lever take être: je suis allé, je me suis levé.", "Participles: fait, pris, vu, fini, parlé."]),
 M("fr-gram", "Grammar check", "Eight quick questions on articles, agreement and pronouns.",
   {"type": "calc", "pass": 0.6, "qs": [
    {"q": "Je mange ___ pomme. (pomme is feminine)", "o": ["un", "une", "le", "des"], "a": 1, "x": "Feminine singular indefinite article: une."},
    {"q": "Elle est très ___. (heureux)", "o": ["heureux", "heureuse", "heureuses", "heureuxe"], "a": 1, "x": "-eux becomes -euse in the feminine."},
    {"q": "Nous ___ français. (parler)", "o": ["parlez", "parlons", "parlent", "parle"], "a": 1, "x": "nous → -ons."},
    {"q": "Hier, je ___ au cinéma.", "o": ["ai allé", "suis allé", "vais", "allais allé"], "a": 1, "x": "aller takes être in the passé composé."},
    {"q": "Tu veux du pain ? — Oui, j'___ veux.", "o": ["le", "y", "en", "lui"], "a": 2, "x": "en replaces du / de la / des + noun."},
    {"q": "C'est ___ livre de Marie ? — Oui, c'est son livre.", "o": ["la", "le", "les", "l'"], "a": 1, "x": "livre is masculine: le."},
    {"q": "Si j'avais le temps, je ___. (voyager)", "o": ["voyage", "voyagerai", "voyagerais", "voyageais"], "a": 2, "x": "si + imparfait → conditionnel."},
    {"q": "Il faut que tu ___ tes devoirs. (faire)", "o": ["fais", "fasses", "feras", "faisais"], "a": 1, "x": "il faut que + subjonctif: que tu fasses."}]},
   win="Gender, agreement and the right pronoun are what make French sound natural."),
]
G3 = [
 M("fr-impf", "Imparfait and futur", "Mixed set: describe the past (imparfait) and predict the future (futur simple).",
   {"type": "conj", "verbs": ["être", "avoir", "faire", "aller", "finir", "parler", "pouvoir", "vouloir"], "tenses": ["impf", "fut"], "n": 10, "pass": 7},
   win="Imparfait: nous-stem + ais, ais, ait, ions, iez, aient. Futur: infinitive (or an irregular stem like ser-, aur-, ir-, fer-) + ai, as, a, ons, ez, ont.",
   hints=["Imparfait stem = the nous form minus -ons (nous finissons → finiss-). Only être is different: ét-.", "Irregular future stems: être → ser-, avoir → aur-, aller → ir-, faire → fer-, pouvoir → pourr-, vouloir → voudr-."]),
 M("fr-boss", "Boss level: conditionnel and subjonctif", "The two moods that separate intermediate from advanced French.",
   {"type": "conj", "verbs": ["être", "avoir", "aller", "faire", "pouvoir", "savoir", "vouloir", "parler", "finir"], "tenses": ["cond", "subj"], "n": 10, "pass": 6},
   win="Conditionnel = future stem + imparfait endings. Subjonctif = ils-stem + e, es, e, ions, iez, ent (with a handful of irregulars).",
   hints=["Conditionnel: je serais, j'aurais, j'irais, je ferais.", "Subjonctif irregulars: que je sois, que j'aie, que j'aille, que je fasse, que je puisse, que je sache, que je veuille."]),
 M("fr-pairs2", "Memory match: harder words", "Same game, less common vocabulary.",
   {"type": "pairs", "n": 8, "from": 300, "to": 900}, win="Bien joué ! Review missed words in the flashcards."),
]
build_ws("french-1", "../../courses/french-1/workshop.html", "French", "L'<span class=\"hl\">atelier</span>",
 "Match words, train your ear, take dictation and race through conjugations from the present to the subjunctive. Turn your sound on.",
 [("Words and Sounds", "Words", G1), ("Verbs I", "Verbs I", G2), ("Verbs II", "Verbs II", G3)], ("fr.js", "decks.js"), "Margin · French workshop · Turn on your sound")
