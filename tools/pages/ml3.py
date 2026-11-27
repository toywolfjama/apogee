from lab_common import *
L = "Machine Learning"
TAGS = {"c": "Concept", "p": "Calculation", "m": "Modeling", "e": "Evaluation"}
OUT = "../../courses/ml/ml-3.html"

LOG = topic("logistic", "Logistic regression", f'''
<p>For a yes/no question we want a <b>probability</b> between 0 and 1, not any real number. Logistic regression takes the linear score z = <b>w</b> · <b>x</b> + b and squashes it with the <b>sigmoid</b> function:</p>
{eq("σ(z) = 1 / (1 + e<sup>−z</sup>) &nbsp;&nbsp;&nbsp;&nbsp; P(y = 1 | x) = σ(w · x + b)")}
{graph(title="The sigmoid", sub="z = wx + b. Bigger w makes the switch from 0 to 1 sharper; b slides it left and right.", x=[-8, 8], y=[-0.2, 1.2], gx=1, gy=.25, params={"w": [-3, 3, .1, 1, "w"], "b": [-5, 5, .1, 0, "b"]}, fns=[fn("1/(1+exp(-(w*x+b)))", "σ(wx + b)"), fn("0.5", "0.5", dash=True)], read=[["Crosses 0.5 at x =", "-b/w"]])}
{mini(("Reading the output", "σ(z) = 0.83 means the model thinks there's an 83% chance this example is positive. To make a decision, compare with a <b>threshold</b> (usually 0.5)."),
      ("Decision boundary", "σ(z) = 0.5 exactly when z = 0, so the boundary is the set where w · x + b = 0: a straight line in 2D, a flat plane in higher dimensions."),
      ("Log-odds", "z itself is the log of the odds: z = ln(p / (1 − p)). Each unit of a feature changes the log-odds by its weight."),
      ("Key values", "σ(0) = 0.5, σ(2) ≈ 0.88, σ(−2) ≈ 0.12, σ(4) ≈ 0.98."))}
<h3>The loss: cross-entropy</h3>
<p>MSE works poorly with probabilities. Instead logistic regression minimizes <b>binary cross-entropy</b> (log loss):</p>
{eq("L = −[ y · ln(p) + (1 − y) · ln(1 − p) ]")}
<p>If the true label is 1 and the model says p = 0.9, the loss is −ln 0.9 ≈ 0.105. If it confidently says p = 0.01, the loss is −ln 0.01 ≈ 4.6. Confident wrong answers are punished hard. Training uses gradient descent, and the gradient has a beautifully simple form: ∂L/∂w = (p − y)·x.</p>
{xlab("classify", methods=["logreg", "knn"], method="logreg", title="Logistic regression vs k-NN", sub="Train logistic regression on each data set. Then add squared features and train again on Circle.")}
{worked("A spam model has w = (1.2, 0.8) for features (number of links, number of ALL-CAPS words) and b = −4. An email has 2 links and 1 all-caps word. Probability it's spam?", "z = 1.2(2) + 0.8(1) − 4 = −0.8. p = 1/(1 + e^0.8) = 1/(1 + 2.23) ≈ 0.31. Below 0.5, so it's classified not spam.")}
''', pill=("m", "3.1"))

TREE = topic("trees", "Decision trees", f'''
<p>A decision tree is a flowchart of yes/no questions: <i>Is income &gt; $50k? → Is debt &lt; $10k? → approve</i>. Each internal node tests one feature against a threshold, and each leaf gives a prediction. Trees are easy to read and explain, need no feature scaling, and handle mixed feature types.</p>
<p>To grow a tree, at each node try every feature and every threshold, and pick the split that makes the two children <b>purest</b>. Two common impurity measures, for class proportions p₁, p₂, …:</p>
{eq("Gini = 1 − Σ pₖ² &nbsp;&nbsp;&nbsp;&nbsp; Entropy = − Σ pₖ log₂ pₖ")}
{xlab("treesplit")}
{steps("Gini of a node with 6 A's and 2 B's", [
 ("a|p_A = 6/8 = 0.75|e  b|p_B = 0.25|e", "Class proportions."),
 ("c|Gini = 1 − 0.75² − 0.25²|e", "Plug into the formula."),
 ("d|= 1 − 0.5625 − 0.0625 = 0.375|g", "0 would be perfectly pure; 0.5 is the worst for two classes."),
])}
<p>The <b>information gain</b> of a split is the parent's impurity minus the weighted average impurity of the children. Repeat recursively until the leaves are pure or a stopping rule kicks in.</p>
{box("trap", "Trees overfit easily", "Grown all the way, a tree can give every training example its own leaf: 100% training accuracy, poor test accuracy. Limit the maximum depth or the minimum number of examples per leaf, or prune the tree afterwards. Unit 4 shows how forests of trees fix this.")}
''', pill=("m", "3.2"))

MULTI = topic("multiclass", "More than two classes", f'''
<p>For K classes (digits 0–9, or cat / dog / bird) a model outputs K scores called <b>logits</b>, one per class, and the <b>softmax</b> function turns them into probabilities that add up to 1:</p>
{eq("pₖ = e<sup>zₖ</sup> / Σⱼ e<sup>zⱼ</sup>")}
{xlab("softmax", classes=["cat", "dog", "bird"], z=[2.0, 1.0, 0.1])}
<p>The loss is <b>categorical cross-entropy</b>: −ln(p of the correct class). Another approach is <b>one-vs-rest</b>: train K separate binary classifiers (\"cat or not?\", \"dog or not?\") and pick the most confident.</p>
{worked("Logits (2, 1, 0) for (cat, dog, bird). Softmax probabilities?", "e² ≈ 7.39, e¹ ≈ 2.72, e⁰ = 1. Total ≈ 11.11. p = (0.665, 0.245, 0.090). If the photo really is a dog, the loss is −ln 0.245 ≈ 1.41.")}
''', pill=("p", "3.3"))

EVAL = topic("metrics", "Evaluating a classifier", f'''
<p>Accuracy alone hides what kind of mistakes a model makes. The <b>confusion matrix</b> counts all four outcomes:</p>
{table(["", "Predicted positive", "Predicted negative"], [["<b>Actually positive</b>", "True positive (TP)", "False negative (FN) — a miss"], ["<b>Actually negative</b>", "False positive (FP) — a false alarm", "True negative (TN)"]])}
{eq("Precision = TP / (TP + FP) &nbsp;&nbsp; Recall = TP / (TP + FN) &nbsp;&nbsp; F1 = 2·P·R / (P + R)")}
{mini(("Precision", "Of everything flagged positive, how much really was? High precision = few false alarms. Matters for spam filters (don't lose real email)."),
      ("Recall (sensitivity)", "Of all the real positives, how many did we catch? High recall = few misses. Matters for cancer screening and fraud."),
      ("F1", "The harmonic mean of precision and recall; it's high only if both are high."),
      ("Trade-off", "Lower the threshold → more positives flagged → recall up, precision down. Raise it → the opposite."))}
{xlab("threshold")}
<p>The <b>ROC curve</b> plots the true positive rate (recall) against the false positive rate FP / (FP + TN) for every possible threshold. The <b>AUC</b> (area under it) is the probability that a random positive gets a higher score than a random negative: 1.0 is perfect, 0.5 is coin-flipping.</p>
{worked("A disease test on 1,000 people: 50 are sick. It flags 60 people, of whom 45 are sick. Find precision, recall and accuracy.", "TP = 45, FP = 15, FN = 5, TN = 935. Precision = 45/60 = 0.75. Recall = 45/50 = 0.90. Accuracy = (45 + 935)/1000 = 0.98.")}
''', pill=("e", "3.4"))

SUM = topic("summary-ml3", "Unit summary", mini(
 ("Logistic regression", "p = σ(w·x + b), σ(z) = 1/(1 + e⁻ᶻ). Boundary w·x + b = 0. Loss = cross-entropy; gradient (p − y)x."),
 ("Trees", "Split on the feature/threshold that most reduces impurity. Gini = 1 − Σp², entropy = −Σp log₂ p. Limit depth to avoid overfitting."),
 ("Many classes", "Softmax: pₖ = e^zₖ / Σ e^zⱼ. Loss −ln p(correct)."),
 ("Metrics", "Precision = TP/(TP + FP), recall = TP/(TP + FN), F1 = harmonic mean. Threshold trades them off. ROC/AUC summarize all thresholds."),
))

CH = [chapter("ch-log", "Logistic Regression", "Logistic", [LOG]),
      chapter("ch-tree", "Trees and Many Classes", "Trees", [TREE, MULTI]),
      chapter("ch-eval", "Evaluation", "Metrics", [EVAL, SUM])]

import math
sg = lambda z: 1 / (1 + math.exp(-z))
close(sg(-0.8), .31); close(1 - .75 ** 2 - .25 ** 2, .375)
e = [math.exp(v) for v in (2, 1, 0)]; close(e[0] / sum(e), .665); close(-math.log(e[1] / sum(e)), 1.41)
PQ = [
 q("What does the sigmoid function output?", ["A number between 0 and 1", "Any real number", "Only 0 or 1", "A number between −1 and 1"], 0, "σ squashes everything into (0, 1).", "c"),
 q("σ(0) equals…", ["0.5", "0", "1", "e"], 0, "1/(1 + 1).", "p"),
 q("A logistic model gives z = 3 for an email. Approximately what probability of spam?", ["0.95", "0.75", "0.5", "3"], 0, "σ(3) = 1/(1 + e⁻³) ≈ 0.953.", "p"),
 q("Logistic regression's decision boundary (threshold 0.5) is where…", ["w · x + b = 0", "w · x + b = 0.5", "σ(z) = 1", "x = 0"], 0, "σ(z) = 0.5 ⇔ z = 0.", "c"),
 q("True label 1, predicted probability 0.25. Cross-entropy loss?", ["≈ 1.39", "≈ 0.29", "0.75", "0.25"], 0, "−ln 0.25 ≈ 1.386.", "p"),
 q("Why can't plain logistic regression (features x₁, x₂ only) separate points inside a circle from points outside it?", ["Its decision boundary is a straight line", "It needs more data", "The learning rate is wrong", "It only handles regression"], 0, "Add x₁², x₂² features to make curved boundaries.", "m"),
 q("Gini impurity of a node with 5 A and 5 B?", ["0.5", "0", "1", "0.25"], 0, "1 − 0.25 − 0.25.", "p"),
 q("Gini impurity of a node with 10 A and 0 B?", ["0", "0.5", "1", "10"], 0, "Pure node.", "p"),
 q("Entropy of a 50/50 binary node?", ["1 bit", "0", "0.5", "2 bits"], 0, "−0.5 log₂ 0.5 × 2 = 1.", "p"),
 q("A decision tree with no depth limit tends to…", ["overfit", "underfit", "need feature scaling", "output probabilities above 1"], 0, "Leaves can memorize individual examples.", "m"),
 q("Softmax outputs for 4 classes always…", ["add up to 1", "add up to 4", "are 0 or 1", "are negative"], 0, "They're a probability distribution.", "c"),
 q("TP = 30, FP = 10, FN = 20. Precision?", ["0.75", "0.6", "0.5", "0.4"], 0, "30/(30 + 10).", "e"),
 q("TP = 30, FP = 10, FN = 20. Recall?", ["0.6", "0.75", "0.5", "0.33"], 0, "30/(30 + 20).", "e"),
 q("For a cancer screening test, which metric matters most?", ["Recall: missing a real case is very costly", "Precision only", "Accuracy only", "Training loss"], 0, "False negatives are the dangerous error.", "e"),
 q("Lowering the classification threshold from 0.5 to 0.2 usually…", ["raises recall and lowers precision", "raises precision and lowers recall", "changes nothing", "raises both"], 0, "More things get flagged positive.", "e"),
 q("An AUC of 0.5 means the model…", ["ranks positives no better than random", "is perfect", "always predicts positive", "has 50% accuracy at every threshold"], 0, "The diagonal of the ROC plot.", "e"),
]
CHAL = [
 q("A node has 8 examples: 6 A, 2 B. A split gives left (4 A, 0 B) and right (2 A, 2 B). Gini gain?", ["0.125", "0.375", "0.25", "0"], 0, "Parent 0.375. Left 0, right 0.5; weighted = (4/8)(0) + (4/8)(0.5) = 0.25. Gain = 0.125.", "p"),
 q("Logits (1, 1, 1, 1). Softmax probability of class 1?", ["0.25", "1", "0.5", "e/4"], 0, "Equal logits give equal probabilities.", "p"),
 q("Adding the same constant c to every logit changes softmax probabilities by…", ["nothing", "multiplying them by e^c", "adding c", "making them sum to c"], 0, "e^(z + c) = e^c·e^z; the e^c cancels top and bottom. (Libraries subtract the max logit for numerical stability.)", "c"),
 q("A logistic model: z = 2x₁ − x₂ − 1. Which point is on the decision boundary?", ["(1, 1)", "(0, 0)", "(1, 0)", "(2, 1)"], 0, "2 − 1 − 1 = 0.", "p"),
 q("Precision 0.8, recall 0.5. F1?", ["≈ 0.615", "0.65", "0.4", "0.8"], 0, "2(0.8)(0.5)/(1.3) = 0.8/1.3.", "e"),
 q("A fraud model on 10,000 transactions (100 fraudulent) flags 200; 80 of those are fraud. Which statement is right?", ["Precision 0.4, recall 0.8", "Precision 0.8, recall 0.4", "Precision 0.8, recall 0.8", "Accuracy 0.8"], 0, "TP = 80, FP = 120, FN = 20. P = 80/200, R = 80/100.", "e"),
]
EXQ = [
 q("Logistic regression is used for…", ["classification", "clustering", "regression of prices", "dimensionality reduction"], 0, "Despite the name.", "c"),
 q("σ(z) is above 0.5 exactly when…", ["z > 0", "z < 0", "z > 0.5", "z = 1"], 0, "σ is increasing and σ(0) = 0.5.", "c"),
 q("Cross-entropy punishes most heavily…", ["confident wrong predictions", "unconfident right predictions", "correct predictions", "predictions of exactly 0.5"], 0, "−ln p blows up as p → 0.", "c"),
 q("A decision tree split is chosen to…", ["make the child nodes as pure as possible", "make the tree deeper", "use every feature", "balance the number of leaves"], 0, "Largest impurity decrease.", "m"),
 q("Gini impurity of a node with 3 A and 1 B?", ["0.375", "0.25", "0.5", "0.75"], 0, "1 − 0.5625 − 0.0625.", "p"),
 q("Which model needs no feature scaling?", ["Decision tree", "k-NN", "Logistic regression with gradient descent", "Neural network"], 0, "A threshold split doesn't care about units.", "m"),
 q("The softmax of logits (0, ln 3) is…", ["(0.25, 0.75)", "(0.5, 0.5)", "(0, 1)", "(0.33, 0.67)"], 0, "e⁰ = 1, e^ln3 = 3 → 1/4, 3/4.", "p"),
 q("Recall is also called…", ["sensitivity / true positive rate", "specificity", "precision", "accuracy"], 0, "TP/(TP + FN).", "e"),
 q("A spam filter that wrongly blocks a real email made a…", ["false positive", "false negative", "true positive", "true negative"], 0, "Predicted spam (positive), actually not.", "e"),
 q("F1 is high only when…", ["both precision and recall are high", "accuracy is high", "the threshold is 0.5", "recall is high"], 0, "Harmonic mean punishes imbalance.", "e"),
 q("The ROC curve plots…", ["true positive rate vs false positive rate", "precision vs recall", "loss vs epochs", "accuracy vs threshold"], 0, "One point per threshold.", "e"),
 q("TP = 40, TN = 50, FP = 5, FN = 5. Accuracy?", ["0.9", "0.8", "0.95", "0.5"], 0, "90/100.", "e"),
]
FRQS = [
 {"q": "A model predicts whether a loan defaults (1) or not (0): z = 0.04·(debt in $k) − 0.5·(years employed) − 1.", "parts": [
  {"p": "(a) Find the default probability for someone with $50k of debt employed 2 years.", "rubric": [["z = 2 − 1 − 1 = 0", 1], ["p = 0.5", 1]], "answer": "z = 0.04(50) − 0.5(2) − 1 = 0 → σ(0) = 0.5."},
  {"p": "(b) Interpret the weight −0.5.", "rubric": [["Each extra year employed lowers the log-odds of default by 0.5", 1], ["i.e. multiplies the odds by e^(−0.5) ≈ 0.61", 1]], "answer": "Each additional year employed lowers the log-odds of default by 0.5, multiplying the odds by about 0.61 (holding debt fixed)."},
  {"p": "(c) The bank loses far more from a missed default than from rejecting a good customer. Should it raise or lower the threshold? Which metric improves?", "rubric": [["Lower the threshold", 1], ["Recall of defaults improves (at the cost of precision)", 1]], "answer": "Lower it (say to 0.3) so more risky applicants are flagged: recall on defaults goes up, precision goes down."}]},
 {"q": "A classifier is tested on 200 emails (60 spam). It marks 50 as spam, 45 of them correctly.", "parts": [
  {"p": "(a) Fill in the confusion matrix.", "rubric": [["TP 45, FP 5", 1], ["FN 15, TN 135", 1]], "answer": "TP = 45, FP = 5, FN = 15, TN = 135."},
  {"p": "(b) Compute accuracy, precision, recall and F1.", "rubric": [["Accuracy 0.9, precision 0.9", 1], ["Recall 0.75, F1 ≈ 0.818", 1]], "answer": "Accuracy = 180/200 = 0.9. Precision = 45/50 = 0.9. Recall = 45/60 = 0.75. F1 = 2(0.9)(0.75)/1.65 ≈ 0.818."}]},
]
build("ml", "ml-3", L, 3, "Classification", 'Sorting into <span class="hl">classes</span>', "Logistic regression, decision trees, softmax and how to judge a classifier: confusion matrices, precision, recall, F1 and ROC curves.", "Machine learning unit 3: logistic regression, sigmoid, cross-entropy, decision trees, Gini impurity, softmax, confusion matrix, precision, recall, F1, ROC and AUC.", CH, PQ, CHAL, EXQ, FRQS, OUT, TAGS)
