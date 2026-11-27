from lab_common import *
L = "Machine Learning"
TAGS = {"c": "Concept", "p": "Calculation", "m": "Modeling", "e": "Evaluation"}
OUT = "../../courses/ml/ml-6.html"

TOKS = [
 {"w": "The", "v": [0.1, 0, 0]}, {"w": "animal", "v": [2, 1, 0.2]}, {"w": "didn't", "v": [0, 0.3, 1]}, {"w": "cross", "v": [0.2, -0.5, 1.2]},
 {"w": "the", "v": [0.1, 0, 0]}, {"w": "street", "v": [1.2, -1, 0.3]}, {"w": "because", "v": [0, 0.2, 0.4]},
 {"w": "it", "v": [1.8, 1.2, 0.1], "note": "Here “it” means the animal, so a trained model learns query and key vectors that point the same way for these two words."},
 {"w": "was", "v": [0, 0.4, 0.6]}, {"w": "tired", "v": [1.0, 1.4, 0.2], "note": "“tired” describes the animal, so it attends to it too."},
]

KM = topic("kmeans", "Clustering with k-means", f'''
<p>With no labels, we can still look for <b>structure</b>. Clustering groups examples so that points in the same group are similar. <b>k-means</b> is the classic algorithm:</p>
<ol class="steps"><li>Pick k starting centers (centroids), for example k random data points.</li>
<li><b>Assign</b> every point to its nearest center.</li>
<li><b>Update</b> each center to the mean of the points assigned to it.</li>
<li>Repeat steps 2–3 until no point changes cluster.</li></ol>
{xlab("kmeans")}
{mini(("What it minimizes", "The <b>inertia</b>: the total squared distance from each point to its center. Each step can only lower it, so k-means always stops, but possibly in a poor local minimum. Run it several times from different starts and keep the best (k-means++ picks smart starting centers)."),
      ("Choosing k", "Inertia always drops as k grows (k = n gives 0). Plot inertia against k and look for the 'elbow' where adding clusters stops helping much."),
      ("Limitations", "Assumes round, similar-sized clusters. Fails on moons and rings, where density-based methods like DBSCAN work better. Scale features first: it uses distances."),
      ("Uses", "Customer segments, grouping news articles, compressing an image to k colors, and as a first look at any new dataset."))}
{worked("Points 1, 2, 3, 10, 11, 12 on a line, k = 2, starting centers 1 and 2. Run k-means.", "Assign: 1 → center 1; 2, 3, 10, 11, 12 → center 2. Update: centers 1 and (2+3+10+11+12)/5 = 7.6. Assign: 1, 2, 3 → center 1 (3 is 2 from 1, 4.6 from 7.6); 10, 11, 12 → 7.6. Update: 2 and 11. Assign: nothing changes. Done: {1, 2, 3} and {10, 11, 12}.")}
''', pill=("m", "6.1"))

PCA = topic("pca", "Dimensionality reduction: PCA", f'''
<p>Real data often has hundreds of features, many of them redundant (height in cm and height in inches). <b>Principal component analysis</b> finds new axes, called <b>principal components</b>, along which the data varies the most, and keeps only the top few.</p>
{xlab("pca")}
{mini(("PC1", "The direction of greatest variance. PC2 is the direction of greatest remaining variance at right angles to PC1, and so on."),
      ("Explained variance", "Each component reports the share of the total variance it captures. Keep enough components to explain, say, 95%."),
      ("Uses", "Plotting high-dimensional data in 2D, speeding up other models, removing noise, compressing data."),
      ("Under the hood", "The components are the eigenvectors of the data's covariance matrix, ranked by their eigenvalues (the variance along each)."))}
{box("tip", "Standardize first", "PCA chases variance, so a feature measured in large units (salary in dollars) would dominate one in small units (age). Standardize features before running PCA.")}
''', pill=("c", "6.2"))

EMB = topic("embeddings", "Embeddings: meaning as vectors", f'''
<p>An <b>embedding</b> represents a word, image, song or user as a list of numbers (a vector, often 256–4096 long) learned so that similar things end up close together. Word embeddings famously capture relationships as directions:</p>
{eq("vec(king) − vec(man) + vec(woman) ≈ vec(queen)")}
<p>Closeness is usually measured with <b>cosine similarity</b>, the cosine of the angle between two vectors:</p>
{eq("cos θ = (a · b) / (‖a‖ ‖b‖)")}
<p>1 means pointing the same way, 0 means unrelated (perpendicular), −1 means opposite. Search engines, recommendation systems and \"find similar photos\" all work by embedding things and finding nearest neighbours.</p>
{worked("Cosine similarity of a = (1, 2, 2) and b = (2, 0, 1)?", "a · b = 2 + 0 + 2 = 4. ‖a‖ = 3, ‖b‖ = √5 ≈ 2.236. cos θ = 4 / 6.71 ≈ 0.60.")}
''', pill=("p", "6.3"))

TRANS = topic("transformers", "Transformers and attention", f'''
<p>The <b>transformer</b> (2017, \"Attention Is All You Need\") is the architecture behind modern language, image and audio models. Its key part is <b>self-attention</b>: every token looks at every other token and decides how much to borrow from each.</p>
<ol class="steps"><li>Each token's embedding is turned into three vectors: a <b>query</b> q (what am I looking for?), a <b>key</b> k (what do I contain?) and a <b>value</b> v (what do I pass along?).</li>
<li>The relevance of token j to token i is the dot product qᵢ · kⱼ, scaled by √d (d = vector length).</li>
<li>Softmax turns those scores into weights that add up to 1.</li>
<li>Token i's new representation is the weighted sum of all the values.</li></ol>
{eq("Attention(Q, K, V) = softmax(QKᵀ / √d) · V")}
{xlab("attention", tokens=TOKS, q=7)}
{mini(("Multi-head attention", "Several attention operations run in parallel, each free to track a different relationship (who did what, what modifies what, which words rhyme)."),
      ("Position", "Attention by itself ignores word order, so position information is added to each token's embedding."),
      ("Why it won", "Every token is processed in parallel (unlike RNNs, which go one step at a time), so transformers train efficiently on GPUs and scale to enormous datasets."),
      ("Beyond text", "Vision transformers split images into patches and treat them as tokens; the same idea works for audio, protein sequences and more."))}
''', pill=("m", "6.4"))

LLM = topic("llms", "Large language models", f'''
<p>A <b>large language model</b> is a transformer trained to predict the next <b>token</b> (a word or piece of a word, like \"un\" + \"believ\" + \"able\") given all the tokens before it. Trained on a huge amount of text, getting good at that one task forces it to pick up grammar, facts, reasoning patterns and style.</p>
{table(["Stage", "What happens"], [
 ["Pretraining", "Self-supervised next-token prediction on a vast text corpus. The most expensive stage."],
 ["Fine-tuning", "Further training on curated examples of following instructions and holding conversations."],
 ["Preference training (e.g. RLHF)", "People (or models) compare responses; the model is trained toward the preferred ones, for helpfulness and safety."],
 ["Generation", "Repeatedly predict a probability distribution over the next token, sample one, append it, repeat."],
])}
{mini(("Temperature", "Logits are divided by a temperature T before softmax (the softmax lab in unit 3 has this slider). Low T: nearly always the most likely token, focused and repetitive. High T: more varied and creative, more likely to wander."),
      ("Context window", "The maximum number of tokens the model can attend to at once. Anything outside it is invisible to the model."),
      ("Hallucination", "A model trained to produce plausible text can produce plausible-sounding but false statements. Check important facts against sources."),
      ("Scaling", "Performance has improved smoothly and predictably with more parameters, more data and more compute, which is why models have grown so large."))}
{worked("A model's logits for the next token are (3, 1, 0) for 'cat', 'dog', 'car'. Probabilities at T = 1 and at T = 0.5?", "T = 1: e³ ≈ 20.1, e¹ ≈ 2.72, 1 → (0.84, 0.11, 0.04). T = 0.5: logits become (6, 2, 0): e⁶ ≈ 403, e² ≈ 7.39, 1 → (0.98, 0.02, 0.002). Lower temperature makes 'cat' almost certain.")}
''', pill=("c", "6.5"))

ETH = topic("responsible", "Responsible machine learning", f'''
{mini(("Bias in, bias out", "A model learns whatever patterns are in its data, including unfair ones. A hiring model trained on past decisions can copy past discrimination. Facial recognition trained mostly on some groups works worse on others."),
      ("Measuring fairness", "Compare error rates across groups: false positive and false negative rates, precision and recall per group. Different fairness definitions can conflict, so the choice is a judgement about values, not just math."),
      ("Privacy", "Models can memorize and leak training data. Techniques include removing personal data, aggregating, and differential privacy (adding carefully calibrated noise)."),
      ("Distribution shift", "The world changes: a model trained before an event may fail after it. Monitor live performance and retrain."),
      ("Explainability", "In high-stakes decisions (loans, medicine, justice) people deserve reasons. Simple models, feature importance, and tools like SHAP help explain predictions."),
      ("Human oversight", "Keep a human in the loop for consequential decisions, and design for what happens when the model is wrong."))}
''', pill=("e", "6.6"))

SUM = topic("summary-ml6", "Unit summary", mini(
 ("k-means", "Assign to nearest center, move centers to means, repeat. Minimizes inertia; choose k with the elbow; scale features."),
 ("PCA", "New axes of maximum variance; keep the top components. Standardize first."),
 ("Embeddings and attention", "Vectors where similar = close; cosine similarity. Attention = softmax(QKᵀ/√d)V. Transformers process tokens in parallel."),
 ("LLMs and responsibility", "Next-token prediction → fine-tuning → preference training. Temperature, context window, hallucinations. Check bias, privacy and drift."),
))

CH = [chapter("ch-unsup", "Unsupervised Learning", "Unsupervised", [KM, PCA]),
      chapter("ch-modern", "Embeddings and Transformers", "Transformers", [EMB, TRANS, LLM]),
      chapter("ch-resp", "Responsible ML", "Responsible ML", [ETH, SUM])]

import math
close(4 / (3 * math.sqrt(5)), .596)
ex = [math.exp(v) for v in (3, 1, 0)]; close(ex[0] / sum(ex), .844)
ex2 = [math.exp(v) for v in (6, 2, 0)]; close(ex2[0] / sum(ex2), .9794)
PQ = [
 q("k-means is an example of…", ["unsupervised learning", "supervised classification", "reinforcement learning", "regression"], 0, "No labels.", "c"),
 q("In the k-means update step, each center moves to…", ["the mean of its assigned points", "the nearest data point", "the origin", "a random point"], 0, "Hence 'means'.", "c"),
 q("Points 0, 2 and 7 are assigned to one cluster. Its new center?", ["3", "2", "4.5", "7"], 0, "(0 + 2 + 7)/3.", "p"),
 q("Why might two runs of k-means give different clusters?", ["Different random starting centers can reach different local minima", "The data changes", "k-means is supervised", "It uses dropout"], 0, "Run several times and keep the lowest inertia.", "c"),
 q("The 'elbow method' is used to choose…", ["k in k-means", "the learning rate", "the threshold", "the activation"], 0, "Look for where inertia stops dropping quickly.", "m"),
 q("PCA's first principal component is the direction of…", ["greatest variance", "smallest variance", "the first feature", "the labels"], 0, "PC1 captures the most spread.", "c"),
 q("Before PCA you should usually…", ["standardize the features", "one-hot encode the labels", "add noise", "train a classifier"], 0, "Otherwise big-unit features dominate.", "m"),
 q("Cosine similarity of two vectors pointing in exactly the same direction?", ["1", "0", "−1", "Depends on their lengths"], 0, "cos 0° = 1.", "p"),
 q("Cosine similarity of (1, 0) and (0, 1)?", ["0", "1", "−1", "0.5"], 0, "Perpendicular.", "p"),
 q("In attention, the weights on all the tokens…", ["add up to 1 (they come from a softmax)", "are all equal", "are always 0 or 1", "can be negative"], 0, "Softmax output.", "c"),
 q("The dot products in attention are divided by √d to…", ["keep the softmax from becoming too peaked when vectors are long", "make them integers", "reverse their order", "remove the values"], 0, "Big dot products would saturate the softmax.", "c"),
 q("A large language model is pretrained to…", ["predict the next token", "classify images", "cluster documents", "sort numbers"], 0, "Self-supervised next-token prediction.", "c"),
 q("Raising the sampling temperature makes generated text…", ["more varied and random", "more repetitive", "shorter", "more accurate"], 0, "The distribution flattens.", "c"),
 q("A model confidently states a fake citation. This is called…", ["hallucination", "overfitting", "attention", "regularization"], 0, "Plausible but false output.", "e"),
 q("A loan model has a much higher false-negative rate for one group of applicants. This is a concern about…", ["fairness", "convergence", "learning rate", "dimensionality"], 0, "Compare error rates across groups.", "e"),
]
CHAL = [
 q("1-D points 1, 2, 9, 10, 11 with k = 2 and starting centers 1 and 11. After convergence, the centers are…", ["1.5 and 10", "1 and 11", "2 and 10", "4.6 and 10.5"], 0, "Assign {1, 2} and {9, 10, 11} → means 1.5 and 10; reassigning changes nothing.", "p"),
 q("Cosine similarity of (3, 4) and (4, 3)?", ["0.96", "1", "0.75", "0.5"], 0, "24 / (5 × 5) = 0.96.", "p"),
 q("Attention scores for one query are (2, 0, 0) before softmax. Weights?", ["≈ (0.79, 0.11, 0.11)", "(1, 0, 0)", "(0.67, 0.17, 0.17)", "(0.5, 0.25, 0.25)"], 0, "e² ≈ 7.39; total ≈ 9.39 → 0.787, 0.106, 0.106.", "p"),
 q("Data has 50 features. PCA's first 3 components explain 60%, 25% and 10% of the variance. How much do 3 components keep?", ["95%", "60%", "85%", "3/50"], 0, "60 + 25 + 10.", "p"),
 q("Why can attention-based transformers train faster than RNNs on long sequences?", ["All positions are processed in parallel instead of one step at a time", "They have no parameters", "They don't use gradients", "They skip the softmax"], 0, "RNNs must wait for the previous step.", "c"),
 q("Logits (2, 2, 0) at temperature T → 0 (very small). Sampling will…", ["pick each of the first two tokens about half the time, never the third", "always pick the first token", "pick all three equally", "fail"], 0, "Low T concentrates all probability on the maximum logits; with a tie it splits between them.", "c"),
]
EXQ = [
 q("Clustering groups data by…", ["similarity, without labels", "the labels", "the order of the rows", "the test set"], 0, "Unsupervised.", "c"),
 q("k-means stops when…", ["no point changes cluster", "inertia is zero", "k reaches n", "after exactly 10 steps"], 0, "Convergence.", "c"),
 q("k-means struggles with…", ["ring- or moon-shaped clusters", "round blobs", "scaled data", "small k"], 0, "It assumes round clusters.", "m"),
 q("PCA is mainly used for…", ["reducing the number of features while keeping most of the variance", "classification", "generating text", "labeling data"], 0, "Dimensionality reduction.", "c"),
 q("Embeddings place similar items…", ["close together in vector space", "far apart", "on a line", "in alphabetical order"], 0, "That's what makes them useful for search.", "c"),
 q("vec(Paris) − vec(France) + vec(Italy) ≈", ["vec(Rome)", "vec(Paris)", "vec(Europe)", "vec(Italy)"], 0, "Capital-of relationship as a direction.", "c"),
 q("In self-attention, each token produces…", ["a query, a key and a value", "only a label", "a cluster center", "a gradient"], 0, "Q, K, V.", "c"),
 q("A token in an LLM is…", ["a word or piece of a word", "a whole paragraph", "a single bit", "an image"], 0, "Subword units.", "c"),
 q("The context window limits…", ["how many tokens the model can see at once", "the learning rate", "the vocabulary", "the number of layers"], 0, "Anything outside is invisible.", "c"),
 q("RLHF stands for…", ["reinforcement learning from human feedback", "recurrent learning with high frequency", "random linear hidden features", "regularized logistic heuristic fitting"], 0, "Training toward responses people prefer.", "c"),
 q("A model trained on 2019 shopping data performs badly in 2021. This is…", ["distribution shift", "overfitting to the test set", "a vanishing gradient", "underfitting by design"], 0, "The world changed.", "e"),
 q("Differential privacy protects people by…", ["adding carefully calibrated noise so individuals can't be singled out", "deleting the model", "using more layers", "lowering the temperature"], 0, "Privacy with a mathematical guarantee.", "e"),
]
FRQS = [
 {"q": "k-means by hand. Points: (1, 1), (1, 2), (2, 1), (8, 8), (9, 8), (8, 9). k = 2, starting centers (1, 1) and (2, 1).", "parts": [
  {"p": "(a) Do the first assignment step.", "rubric": [["(1,1), (1,2) → center (1,1)", 1], ["(2,1) and all three far points → center (2,1)", 1]], "answer": "(1,1) and (1,2) are closer to (1,1). (2,1), (8,8), (9,8), (8,9) are closer to (2,1)."},
  {"p": "(b) Update the centers, then reassign.", "rubric": [["Centers (1, 1.5) and (6.75, 6.5)", 1], ["Reassign: (2,1) moves to the first cluster", 1]], "answer": "Centers (1, 1.5) and ((2+8+9+8)/4, (1+8+8+9)/4) = (6.75, 6.5). Now (2,1) is closer to (1, 1.5), so it switches."},
  {"p": "(c) Give the final clusters and centers.", "rubric": [["{(1,1),(1,2),(2,1)} center (4/3, 4/3)", 1], ["{(8,8),(9,8),(8,9)} center (25/3, 25/3)", 1]], "answer": "Cluster 1 = the three small points, center (1.33, 1.33). Cluster 2 = the three large points, center (8.33, 8.33)."}]},
 {"q": "Language models.", "parts": [
  {"p": "(a) Explain what 'next-token prediction' is and why it counts as self-supervised.", "rubric": [["Predict the next token from the previous ones", 1], ["Labels come from the text itself, no human labeling", 1]], "answer": "Given the tokens so far, predict a probability for each possible next token. The correct answer is simply the actual next token in the text, so no human labels are needed."},
  {"p": "(b) Logits for the next token are (2, 1, 0). Compute the probabilities at T = 1 and T = 2.", "rubric": [["T = 1 ≈ (0.665, 0.245, 0.090)", 1], ["T = 2: logits (1, 0.5, 0) → ≈ (0.506, 0.307, 0.186)", 1]], "answer": "T = 1: (0.665, 0.245, 0.090). T = 2: e¹ = 2.718, e^0.5 = 1.649, 1 → total 5.367 → (0.506, 0.307, 0.186)."},
  {"p": "(c) Give one risk of deploying an LLM-based assistant and one mitigation.", "rubric": [["A valid risk (hallucination, bias, privacy leak, misuse)", 1], ["A matching mitigation (citations/fact checks, evaluations by group, data filtering, human review)", 1]], "answer": "e.g. Hallucinated facts → ground answers in retrieved sources and show citations; or biased outputs → evaluate across groups and adjust training data."}]},
]
build("ml", "ml-6", L, 6, "Unsupervised Learning and Modern AI", 'Clusters, embeddings and <span class="hl">transformers</span>', "k-means, PCA, embeddings, attention, large language models and how to use machine learning responsibly.", "Machine learning unit 6: k-means clustering, principal component analysis, embeddings, cosine similarity, transformers, self-attention, large language models and responsible AI.", CH, PQ, CHAL, EXQ, FRQS, OUT, TAGS)
