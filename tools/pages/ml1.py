from lab_common import *
L = "Machine Learning"
TAGS = {"c": "Concept", "p": "Calculation", "m": "Modeling", "e": "Evaluation"}
OUT = "../../courses/ml/ml-1.html"

WHAT = topic("what", "What machine learning is", f'''
<p>In ordinary programming you write the rules: <i>if the email contains \"FREE MONEY\", mark it as spam</i>. In <b>machine learning</b> you give the computer lots of examples (emails already marked spam or not) and an algorithm finds the rules itself. The result is a <b>model</b>: a function with adjustable numbers, called <b>parameters</b>, that have been tuned to fit the examples.</p>
{eq("traditional: rules + data → answers &nbsp;&nbsp;&nbsp;&nbsp; machine learning: data + answers → rules")}
{table(["Kind of learning", "What the data looks like", "Goal", "Examples"], [
 ["Supervised", "inputs with the correct answer (label)", "predict the label for new inputs", "spam filter, house prices, reading handwritten digits"],
 ["Unsupervised", "inputs only, no labels", "find structure: groups, patterns, compressed versions", "customer segments, anomaly detection"],
 ["Reinforcement", "an agent acts and receives rewards", "learn actions that earn the most reward over time", "game-playing AIs, robot control"],
 ["Self-supervised", "raw data where part of it is hidden and predicted", "learn general-purpose representations", "large language models predicting the next word"],
])}
<p>Supervised problems come in two flavours:</p>
{mini(("Regression", "The answer is a number: tomorrow's temperature, a house price, how many minutes a delivery will take."),
      ("Classification", "The answer is a category: spam or not spam, which of 10 digits, cat / dog / bird. With two categories it's <b>binary</b> classification."))}
{box("tip", "When ML is the right tool", "Use ML when the rules are too complicated to write by hand (recognizing faces), when they change over time (fraud patterns), or when you need to personalize for millions of people. If a simple rule works, use the simple rule.")}
''', pill=("c", "1.1"))

DATA = topic("data", "Data: examples, features and labels", f'''
<p>A dataset is usually a table. Each <b>row</b> is one <b>example</b> (an observation). Each <b>column</b> is a <b>feature</b> (an input variable), except for the <b>label</b> (the thing to predict).</p>
{table(["sq. feet", "bedrooms", "neighbourhood", "age (yrs)", "<b>price ($k)</b> ← label"], [["1400", "3", "North", "12", "310"], ["2100", "4", "South", "3", "455"], ["850", "1", "North", "40", "190"], ["1650", "3", "East", "8", "352"]])}
<p>A model sees each example as a <b>feature vector</b> x = (x₁, x₂, …, x_d), a list of d numbers, and predicts ŷ (\"y-hat\"). The true label is y. Bold letters and subscripts are just bookkeeping for \"the list of numbers\".</p>
<h3>Turning everything into numbers</h3>
{mini(("Categories → one-hot", "A category like neighbourhood ∈ {North, South, East} becomes three 0/1 columns: North = (1, 0, 0), South = (0, 1, 0), East = (0, 0, 1). Don't code them as 1, 2, 3 — that would tell the model East is 'three times' North."),
      ("Text and images", "Images are grids of pixel brightnesses (a 28 × 28 photo is 784 features). Text is split into tokens that are mapped to numbers (unit 6)."),
      ("Missing values", "Drop the rows, fill in the column average (imputation), or add a 'was missing' flag column. Never silently treat missing as 0."),
      ("Outliers", "One house listed at $99,999,999 by mistake can drag a whole model. Plot your data first."))}
''', pill=("m", "1.2"))

SCALE = topic("scaling", "Feature scaling", f'''
<p>Square feet (hundreds to thousands) and bedrooms (1–5) live on very different scales. Many algorithms, including distance-based ones like k-NN and anything trained by gradient descent, behave badly when features have wildly different ranges. Two standard fixes:</p>
{eq("Standardize (z-score): z = (x − μ) / σ &nbsp;&nbsp;&nbsp;&nbsp; Min–max: x′ = (x − min) / (max − min)")}
<p>Standardizing gives every feature mean 0 and standard deviation 1. Min–max squeezes every feature into [0, 1].</p>
{steps("Standardize the values 2, 4, 4, 4, 5, 5, 7, 9", [
 ("a|μ = 40 / 8 = 5|e", "Mean: add them up and divide by the count."),
 ("b|deviations: −3 −1 −1 −1 0 0 2 4|v", "Subtract the mean from each value."),
 ("c|σ² = (9+1+1+1+0+0+4+16)/8 = 4|e  d|σ = 2|g", "Variance = average squared deviation. Standard deviation = √variance."),
 ("e|z = −1.5 −0.5 −0.5 −0.5 0 0 1 2|g", "Divide each deviation by σ. The value 9 is 2 standard deviations above average."),
])}
{box("trap", "Fit the scaler on training data only", "Compute μ and σ from the training set, then apply those same numbers to the validation and test sets. Computing them on all the data lets information about the test set leak into training.")}
''', pill=("p", "1.3"))

SPLIT = topic("splits", "Training, validation and test sets", f'''
<p>A model that memorizes its training data can score 100% on it and still fail on anything new. What we care about is <b>generalization</b>: performance on data the model has never seen. So we split the data before training:</p>
{table(["Set", "Typical share", "Used for"], [["Training", "60–80%", "fitting the model's parameters"], ["Validation", "10–20%", "choosing between models and tuning hyperparameters (settings like k in k-NN)"], ["Test", "10–20%", "one final, honest estimate of real-world performance. Touch it once, at the end."]])}
{mini(("Hyperparameters", "Settings you choose rather than learn: learning rate, number of neighbours k, tree depth, number of layers. You tune them on the validation set."),
      ("Data leakage", "Any route by which test information sneaks into training: scaling on all data, duplicate rows across splits, or a feature that's secretly the answer (a 'refund issued' column when predicting fraud). Leakage gives great scores that collapse in the real world."),
      ("Random vs time split", "Shuffle randomly for ordinary data. For time series (stock prices, sales) train on the past and test on the future, or you'll be 'predicting' with information from tomorrow."),
      ("Class balance", "If 99% of transactions are legit, a model that always says 'legit' is 99% accurate and useless. Check the class proportions; use stratified splits that keep them the same in every set."))}
''', pill=("e", "1.4"))

KNN = topic("knn", "Your first model: k-nearest neighbours", f'''
<p>The simplest learning algorithm there is: to classify a new point, find the <b>k</b> training examples closest to it and take a majority vote. \"Training\" is just storing the data.</p>
{eq("distance between x and x′ = √((x₁ − x′₁)² + (x₂ − x′₂)² + … + (x_d − x′_d)²)")}
{xlab("classify", methods=["knn"], k=5, title="k-NN classifier", sub="Shading shows the prediction at every point. Change k and the data set. Click to add points.")}
{worked("Training points: A at (1, 1) and (2, 1); B at (4, 4) and (5, 3). Classify (2, 2) with k = 1 and with k = 3.", "Distances from (2, 2): to (1, 1) = √2 ≈ 1.41, to (2, 1) = 1, to (4, 4) = √8 ≈ 2.83, to (5, 3) = √10 ≈ 3.16. k = 1: nearest is (2, 1), class A. k = 3: (2, 1) A, (1, 1) A, (4, 4) B → 2 votes to 1, class A.")}
{mini(("Small k", "Follows every training point, including noise. Jagged boundaries. Overfits."), ("Large k", "Averages over many points. Smooth boundaries. If k is too big it underfits, ignoring real structure."),
      ("Cost", "Predicting means measuring the distance to every training example, which gets slow with millions of rows."), ("Curse of dimensionality", "In hundreds of dimensions almost all points are roughly the same distance apart, so 'nearest' stops meaning much."))}
''', pill=("m", "1.5"))

WORK = topic("workflow", "The machine learning workflow", f'''
<ol class="steps"><li><b>Frame the problem.</b> What exactly are you predicting, for whom, and what counts as success? Pick a metric.</li>
<li><b>Get and explore the data.</b> Plot it. Look for missing values, outliers, imbalance, leakage.</li>
<li><b>Prepare features.</b> Encode categories, scale numbers, engineer useful new features.</li>
<li><b>Split</b> into train / validation / test.</li>
<li><b>Start with a baseline</b>: predict the average, or the most common class. Any real model must beat it.</li>
<li><b>Train models</b> and tune hyperparameters on the validation set.</li>
<li><b>Evaluate once</b> on the test set.</li>
<li><b>Deploy and monitor.</b> The world drifts; retrain when performance slips.</li></ol>
{code('''
# The same workflow in Python with scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
scaler = StandardScaler().fit(X_train)        # fit on training data only
model = KNeighborsClassifier(n_neighbors=5)
model.fit(scaler.transform(X_train), y_train)
print(model.score(scaler.transform(X_test), y_test))   # accuracy on unseen data
''')}
''', pill=("m", "1.6"))

SUM = topic("summary-ml1", "Unit summary", mini(
 ("ML", "Learn rules from examples. Supervised (regression: numbers; classification: categories), unsupervised, reinforcement, self-supervised."),
 ("Data", "Rows = examples, columns = features, plus a label. One-hot encode categories. Handle missing values and outliers."),
 ("Scaling and splits", "z = (x − μ)/σ, fit on training data only. Train / validation / test; tune on validation; test once. Watch for leakage and imbalance."),
 ("k-NN", "Vote among the k closest training points. Small k overfits, large k underfits. Start every project with a baseline."),
))

CH = [chapter("ch-what", "What ML Is", "What is ML", [WHAT]),
      chapter("ch-data", "Data", "Data", [DATA, SCALE, SPLIT]),
      chapter("ch-knn", "First Model and Workflow", "k-NN", [KNN, WORK, SUM])]

import statistics as st
close(st.pstdev([2, 4, 4, 4, 5, 5, 7, 9]), 2)
PQ = [
 q("Predicting tomorrow's high temperature in °C is a…", ["regression problem", "classification problem", "clustering problem", "reinforcement learning problem"], 0, "The answer is a number.", "c"),
 q("Sorting customers into groups when nobody has labelled them is…", ["unsupervised learning", "supervised learning", "regression", "reinforcement learning"], 0, "No labels → unsupervised (clustering).", "c"),
 q("A program learns to play chess by playing games and getting +1 for wins and −1 for losses. This is…", ["reinforcement learning", "unsupervised learning", "regression", "k-NN"], 0, "Actions + rewards.", "c"),
 q("In a dataset of houses, the sale price you want to predict is the…", ["label", "feature", "hyperparameter", "parameter"], 0, "The target/label.", "c"),
 q("How should the category color ∈ {red, green, blue} usually be encoded?", ["Three 0/1 columns (one-hot)", "red = 1, green = 2, blue = 3", "Delete the column", "As text"], 0, "Integer codes impose a fake order.", "m"),
 q("A feature has mean 50 and standard deviation 10. What is the z-score of 35?", ["−1.5", "1.5", "−15", "0.35"], 0, "(35 − 50)/10.", "p"),
 q("Min–max scale 30 when the feature ranges from 10 to 60.", ["0.4", "0.5", "0.3", "0.6"], 0, "(30 − 10)/(60 − 10) = 20/50.", "p"),
 q("Which set should be used to choose k in k-NN?", ["Validation set", "Test set", "Training set only", "Any of them"], 0, "The test set must stay untouched until the very end.", "e"),
 q("Why is the test set kept separate until the end?", ["To get an honest estimate of performance on new data", "Because it's too small to train on", "To speed up training", "To make the model bigger"], 0, "Using it for decisions makes it part of training.", "e"),
 q("Euclidean distance between (1, 2) and (4, 6)?", ["5", "7", "25", "√7"], 0, "√(3² + 4²) = 5.", "p"),
 q("In k-NN, what happens with k = 1?", ["Each point takes the label of its single nearest neighbour; the boundary is very jagged", "The model always predicts the majority class", "The model can't classify anything", "Training takes much longer"], 0, "Small k overfits.", "m"),
 q("99% of emails are not spam. A model that always says 'not spam' has accuracy…", ["99%, but it is useless", "1%", "50%", "100%"], 0, "Accuracy misleads on imbalanced data.", "e"),
 q("Standardizing using the mean of the entire dataset (including the test set) is an example of…", ["data leakage", "regularization", "one-hot encoding", "a baseline"], 0, "Test information leaks into training.", "e"),
 q("Something you choose before training (like the learning rate) is called a…", ["hyperparameter", "parameter", "label", "feature"], 0, "Parameters are learned; hyperparameters are set.", "c"),
 q("Sales data from 2015–2024 is used to predict 2025. How should you split it?", ["Train on earlier years, test on later years", "Shuffle randomly", "Test on 2015 only", "Use every year for both"], 0, "Time series: never train on the future.", "e"),
]
CHAL = [
 q("Training points on a line: A at 1.0 and 1.2; B at 2.9, 4.0 and 5.0. A new point is at 2.2. What does k-NN predict with k = 1 and with k = 3?", ["k = 1: B, k = 3: A", "k = 1: A, k = 3: B", "B both times", "A both times"], 0, "Distances: 2.9 → 0.7 (B), 1.2 → 1.0 (A), 1.0 → 1.2 (A), 4.0 → 1.8 (B). k = 1 uses only the B at 0.7. k = 3 gets B, A, A → A. Changing k can flip the answer.", "p"),
 q("Features: income (in dollars, 20,000–200,000) and age (18–90). Without scaling, k-NN distances are dominated by…", ["income", "age", "both equally", "neither"], 0, "Differences of tens of thousands swamp differences of tens.", "m"),
 q("A fraud model scores 99.5% on test data. Later you find a feature 'chargeback_filed' that's only set after fraud is confirmed. What's the problem?", ["Target leakage: the feature reveals the answer", "Overfitting from too few features", "Bad scaling", "Imbalanced classes"], 0, "At prediction time that information doesn't exist yet.", "e"),
 q("You standardize a test value of 130 using training μ = 100, σ = 15. Its z-score is…", ["2", "1.5", "−2", "30"], 0, "(130 − 100)/15 = 2.", "p"),
 q("Which is the best baseline for a regression model predicting delivery time?", ["Always predict the training-set average time", "Always predict 0", "A deep neural network", "The test-set average"], 0, "The mean of the training labels is the simplest honest baseline.", "m"),
 q("In 1000 dimensions with points spread uniformly, why does k-NN struggle?", ["Distances between points become nearly all the same", "The computer runs out of colors", "k must equal the dimension", "Euclidean distance is undefined"], 0, "The curse of dimensionality.", "c"),
]
EXQ = [
 q("Machine learning programs learn…", ["patterns from examples", "only from hand-written rules", "without any data", "by random guessing only"], 0, "Data + answers → rules.", "c"),
 q("Whether a photo shows a cat or a dog is a…", ["binary classification problem", "regression problem", "clustering problem", "dimension reduction problem"], 0, "Two categories.", "c"),
 q("Large language models are mainly trained by…", ["self-supervised learning: predicting the next token", "clustering", "k-NN", "reinforcement learning only"], 0, "The text provides its own labels.", "c"),
 q("A row of a dataset is usually…", ["one example", "one feature", "one label", "one model"], 0, "Columns are features.", "c"),
 q("z-score of x = 70 when μ = 60, σ = 5?", ["2", "10", "0.5", "−2"], 0, "(70 − 60)/5.", "p"),
 q("Variance of 1, 3, 5 (population)?", ["8/3", "2", "4", "3"], 0, "Mean 3; squared deviations 4, 0, 4; average 8/3.", "p"),
 q("Hyperparameters should be tuned on the…", ["validation set", "test set", "label column", "production data"], 0, "Keep the test set clean.", "e"),
 q("k-NN with a very large k tends to…", ["underfit", "overfit", "memorize the data", "fail to run"], 0, "It averages away real structure.", "m"),
 q("Data leakage leads to…", ["test scores that are too optimistic", "slower training", "smaller models", "better real-world performance"], 0, "The model cheats in testing, not in reality.", "e"),
 q("Distance between (0, 0, 0) and (2, 3, 6)?", ["7", "11", "49", "√11"], 0, "√(4 + 9 + 36) = 7.", "p"),
 q("Before training any fancy model you should…", ["build a simple baseline to beat", "tune on the test set", "delete outliers without looking", "use all the data for training"], 0, "Baselines tell you whether the model actually helps.", "m"),
 q("Which encoding is best for 'day of week' in a linear model?", ["One-hot (seven 0/1 columns)", "A single number 1–7", "Drop it", "Its first letter"], 0, "Avoids a fake ordering (Sunday isn't seven times Monday).", "m"),
]
FRQS = [
 {"q": "A school wants to predict which students will need tutoring (yes/no) from last year's grades, attendance and the class they're in.", "parts": [
  {"p": "(a) Is this supervised or unsupervised, regression or classification? What are the features and the label?", "rubric": [["Supervised binary classification", 1], ["Features: grades, attendance, class; label: needs tutoring", 1]], "answer": "Supervised, binary classification. Features: grades, attendance rate, class (one-hot). Label: needed tutoring (yes/no)."},
  {"p": "(b) Describe how you'd split the data and what each part is for.", "rubric": [["Train / validation / test with rough proportions", 1], ["Validation for tuning, test once at the end", 1]], "answer": "e.g. 70/15/15. Fit on training, tune hyperparameters on validation, report test once at the end."},
  {"p": "(c) Only 8% of students needed tutoring. Why is accuracy a poor metric here, and what would you check instead?", "rubric": [["Always 'no' scores 92%", 1], ["Use recall/precision (catching the students who need help)", 1]], "answer": "A model that says 'no' for everyone is 92% accurate but helps nobody. Look at recall (how many needing tutoring are caught) and precision (unit 3)."}]},
 {"q": "k-NN by hand. Training points (x₁, x₂, class): (1, 1, A), (2, 3, A), (4, 2, B), (5, 5, B), (3, 4, B).", "parts": [
  {"p": "(a) Compute the distances from the new point (3, 2) to every training point.", "rubric": [["√5, √2, 1, √13, 2", 2]], "answer": "(1,1): √5 ≈ 2.24. (2,3): √2 ≈ 1.41. (4,2): 1. (5,5): √13 ≈ 3.61. (3,4): 2."},
  {"p": "(b) Classify (3, 2) with k = 1 and with k = 3.", "rubric": [["k = 1: B (nearest is (4,2))", 1], ["k = 3: (4,2) B, (2,3) A, (3,4) B → B", 1]], "answer": "k = 1: B. k = 3: nearest are (4,2) B, (2,3) A, (3,4) B → B."}]},
]
build("ml", "ml-1", L, 1, "Foundations and Data", 'What machine learning <span class="hl">is</span>', "Supervised and unsupervised learning, features and labels, scaling, train/test splits, leakage and your first model: k-nearest neighbours.", "Machine learning unit 1: types of machine learning, features and labels, one-hot encoding, standardization, train/validation/test splits, data leakage and k-nearest neighbours.", CH, PQ, CHAL, EXQ, FRQS, OUT, TAGS)
