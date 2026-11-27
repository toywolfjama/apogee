from lab_common import *
L = "Machine Learning"
TAGS = {"c": "Concept", "p": "Calculation", "m": "Modeling", "e": "Evaluation"}
OUT = "../../courses/ml/ml-4.html"

FIT = topic("fit", "Underfitting and overfitting", f'''
<p>The goal of machine learning is never to fit the training data; it's to do well on data the model hasn't seen. Two things go wrong:</p>
{mini(("Underfitting (high bias)", "The model is too simple to capture the pattern. Training error and test error are both high. Fix: a more flexible model, better features, train longer."),
      ("Overfitting (high variance)", "The model is so flexible it learns the noise in the training set. Training error is low, test error is high. Fix: more data, a simpler model, regularization, early stopping."))}
{xlab("overfit")}
<p>As model complexity grows, training error keeps falling, but test error falls and then rises again, a U shape. The sweet spot is at the bottom of the test-error curve. That's what the right-hand chart in the lab shows.</p>
<h3>The bias–variance trade-off</h3>
<p>The expected test error of a model can be split into three parts:</p>
{eq("expected error = bias² + variance + irreducible noise")}
<p><b>Bias</b> is error from wrong assumptions (fitting a line to a curve). <b>Variance</b> is how much the model would change if trained on a different sample of data (a degree-11 polynomial swings wildly). <b>Noise</b> is randomness no model can predict. Making a model more flexible lowers bias but raises variance.</p>
{box("tip", "Diagnose with learning curves", "Plot training and validation error as the training set grows. If both are high and close together → high bias: more data won't help, a bigger model will. If there's a big gap that shrinks as data grows → high variance: more data will help.")}
''', pill=("c", "4.1"))

REG = topic("regularization", "Regularization", f'''
<p>Regularization adds a penalty for large weights to the loss, so the model only uses big weights when they really pay off:</p>
{eq("L2 (ridge): loss = MSE + λ Σ wⱼ² &nbsp;&nbsp;&nbsp;&nbsp; L1 (lasso): loss = MSE + λ Σ |wⱼ|")}
{mini(("λ (lambda)", "The regularization strength, a hyperparameter. λ = 0: no penalty. λ huge: all weights forced toward 0 (underfits). Tune it on the validation set."),
      ("L2 / ridge / weight decay", "Shrinks all weights smoothly. Wiggly curves need huge weights, so L2 smooths the fit. In the lab above, slide λ up with degree 11."),
      ("L1 / lasso", "Pushes many weights to exactly 0, so it also does <b>feature selection</b>: the model ends up using only the useful features."),
      ("Bias is not penalized", "The intercept b just shifts predictions up or down; shrinking it would bias every prediction."))}
<h3>Other ways to fight overfitting</h3>
{table(["Technique", "How it works"], [["More data", "The single best fix for variance. Data augmentation (flipping, cropping, rotating images) creates more from what you have."], ["Early stopping", "Watch the validation loss while training and stop when it starts going up."], ["Dropout (neural nets)", "Randomly switch off a fraction of neurons on each training step, so the network can't rely on any single one."], ["Simpler model", "Fewer features, lower polynomial degree, shallower tree."]])}
''', pill=("m", "4.2"))

CV = topic("cv", "Cross-validation and tuning", f'''
<p>One validation split can be lucky or unlucky, especially with small datasets. <b>k-fold cross-validation</b> uses every example for validation exactly once:</p>
<ol class="steps"><li>Shuffle and split the training data into k equal folds (k = 5 or 10 is common).</li>
<li>For each fold: train on the other k − 1 folds, measure the score on this fold.</li>
<li>Average the k scores. Their spread tells you how stable the estimate is.</li></ol>
{worked("5-fold CV scores are 0.82, 0.85, 0.80, 0.84, 0.79. What's the CV estimate, and how many models were trained?", "Mean = 4.10/5 = 0.82. Five models were trained, each on 80% of the data.")}
<h3>Hyperparameter search</h3>
{mini(("Grid search", "Try every combination from a list: λ ∈ {0.01, 0.1, 1} × depth ∈ {3, 5, 7} = 9 combinations, each scored with cross-validation."),
      ("Random search", "Sample combinations at random. With the same budget it usually finds better settings than a grid, because only a few hyperparameters really matter."))}
{box("trap", "The test set is still off-limits", "Cross-validation happens inside the training data. After choosing the hyperparameters, retrain on all the training data and evaluate once on the untouched test set.")}
''', pill=("e", "4.3"))

ENS = topic("ensembles", "Ensembles: many models are better than one", f'''
<p>Average the predictions of many different models and their individual errors partly cancel out. Ensembles win most competitions on tabular data.</p>
{mini(("Bagging", "Bootstrap aggregating: train each model on a random sample of the training data drawn <i>with replacement</i>, then average (regression) or vote (classification). Mainly reduces variance."),
      ("Random forest", "Bagging with decision trees, plus a twist: at each split a tree may only consider a random subset of the features. This makes the trees more different from each other, so averaging helps more. Robust, few hyperparameters, a great default."),
      ("Boosting", "Train models one after another, each focusing on the mistakes of the ones before. Gradient boosting fits each new tree to the remaining errors (residuals). XGBoost, LightGBM and CatBoost are popular implementations. Mainly reduces bias."),
      ("Feature importance", "Tree ensembles can report how much each feature reduced impurity across all splits, a rough guide to what the model relies on."))}
{worked("Three independent classifiers are each right 70% of the time. Majority vote accuracy?", "The vote is right if at least 2 of 3 are right: 3(0.7²)(0.3) + 0.7³ = 0.441 + 0.343 = 0.784. Better than any single model — but only if their errors are independent.")}
''', pill=("m", "4.4"))

SUM = topic("summary-ml4", "Unit summary", mini(
 ("Fit", "Underfit: both errors high (bias). Overfit: low train, high test (variance). Test error is U-shaped in complexity."),
 ("Regularization", "L2: + λΣw² shrinks weights. L1: + λΣ|w| zeroes some (feature selection). Also: more data, augmentation, early stopping, dropout."),
 ("Cross-validation", "k folds, train k models, average. Grid or random search over hyperparameters. Test set used once at the end."),
 ("Ensembles", "Bagging/random forests cut variance; boosting cuts bias. Independent errors cancel in a vote."),
))

CH = [chapter("ch-fit", "Over- and Underfitting", "Fit", [FIT]),
      chapter("ch-reg", "Regularization", "Regularization", [REG, CV]),
      chapter("ch-ens", "Ensembles", "Ensembles", [ENS, SUM])]

close(3 * .7 ** 2 * .3 + .7 ** 3, .784)
PQ = [
 q("Training error 2%, test error 25%. The model is most likely…", ["overfitting", "underfitting", "perfect", "not trained"], 0, "Big gap = high variance.", "e"),
 q("Training error 30%, test error 31%, and a human gets 5%. The model is most likely…", ["underfitting", "overfitting", "well fit", "leaking"], 0, "Both errors high = high bias.", "e"),
 q("Which usually reduces overfitting?", ["Getting more training data", "Adding more polynomial features", "Training with no regularization", "Using the test set for training"], 0, "More data reduces variance.", "m"),
 q("In bias–variance terms, a very deep unpruned decision tree has…", ["low bias, high variance", "high bias, low variance", "high bias, high variance", "low bias, low variance"], 0, "It fits training data perfectly but changes a lot with new samples.", "c"),
 q("L2 regularization adds which term to the loss?", ["λ Σ w²", "λ Σ |w|", "λ Σ w", "λ · b"], 0, "Ridge / weight decay.", "c"),
 q("Which regularization tends to set some weights exactly to zero?", ["L1 (lasso)", "L2 (ridge)", "Early stopping", "Dropout"], 0, "L1 performs feature selection.", "c"),
 q("If λ is set extremely large, the model will…", ["underfit: weights forced near zero", "overfit", "train faster but identically", "ignore the data entirely except the weights"], 0, "The penalty dominates.", "m"),
 q("Early stopping means…", ["halting training when validation loss starts to rise", "stopping when training loss is zero", "stopping after one epoch", "using fewer features"], 0, "Catch the bottom of the U.", "m"),
 q("5-fold cross-validation trains how many models?", ["5", "1", "4", "10"], 0, "One per held-out fold.", "e"),
 q("CV fold scores 0.70, 0.74, 0.72, 0.76, 0.78. CV estimate?", ["0.74", "0.76", "0.72", "0.78"], 0, "Sum 3.70 / 5.", "p"),
 q("Grid search over 4 values of λ and 3 depths with 5-fold CV trains how many models?", ["60", "12", "20", "7"], 0, "4 × 3 combinations × 5 folds.", "p"),
 q("A random forest differs from plain bagged trees because…", ["each split considers only a random subset of features", "it uses one big tree", "it uses no randomness", "it boosts the errors"], 0, "Decorrelates the trees.", "c"),
 q("Boosting trains models…", ["sequentially, each fixing the previous ones' errors", "independently in parallel", "only on the test set", "without labels"], 0, "Gradient boosting fits residuals.", "c"),
 q("Bootstrap sampling draws training examples…", ["at random with replacement", "without replacement", "only the hardest examples", "from the test set"], 0, "Some examples repeat, some are left out (about 37%).", "c"),
 q("Data augmentation for an image classifier could be…", ["random flips, crops and small rotations", "adding the test set", "removing all labels", "shrinking the network"], 0, "New, realistic training variations.", "m"),
]
CHAL = [
 q("Three independent models are each 60% accurate on a binary task. Majority-vote accuracy?", ["0.648", "0.6", "0.784", "0.36"], 0, "3(0.6²)(0.4) + 0.6³ = 0.432 + 0.216.", "p"),
 q("Ridge loss MSE + λ(w₁² + w₂²) with w = (3, −4), MSE = 2, λ = 0.1. Total loss?", ["4.5", "2.5", "27", "2.7"], 0, "Penalty = 0.1 × 25 = 2.5 → 4.5.", "p"),
 q("Lasso with the same w = (3, −4), λ = 0.1, MSE = 2. Total loss?", ["2.7", "4.5", "2.1", "9"], 0, "0.1 × (3 + 4) = 0.7 → 2.7.", "p"),
 q("Learning curves: training error rises from 0% to 8% and validation error falls from 40% to 10% as data grows, still with a gap. Best next step?", ["Collect more data", "Use a simpler model", "Increase λ massively", "Stop training earlier"], 0, "A shrinking gap that hasn't closed means more data will keep helping.", "e"),
 q("A bootstrap sample of size n drawn with replacement leaves out roughly what fraction of the original examples?", ["≈ 37%", "≈ 50%", "0%", "≈ 63%"], 0, "(1 − 1/n)ⁿ → 1/e ≈ 0.368. These 'out-of-bag' examples give a free validation set.", "p"),
 q("You tuned λ by checking test-set accuracy 50 times and picked the best. Your reported test accuracy is likely…", ["too optimistic", "too pessimistic", "exactly right", "unaffected"], 0, "You've fit the test set through your choices; use a validation set or CV.", "e"),
]
EXQ = [
 q("Generalization means…", ["performing well on new, unseen data", "fitting the training data perfectly", "using many features", "training quickly"], 0, "The real goal.", "c"),
 q("High variance shows up as…", ["a big gap between training and test error", "both errors high", "both errors low", "training error higher than test error"], 0, "Overfitting.", "e"),
 q("Increasing the polynomial degree generally…", ["lowers bias and raises variance", "raises bias and lowers variance", "lowers both", "raises both"], 0, "More flexible.", "c"),
 q("Irreducible error comes from…", ["noise in the data no model can predict", "a bad learning rate", "too few features", "overfitting"], 0, "It sets a floor on error.", "c"),
 q("The purpose of λ in ridge regression is to…", ["control how strongly large weights are penalized", "set the learning rate", "choose the number of folds", "scale the features"], 0, "Regularization strength.", "c"),
 q("Dropout is used mainly in…", ["neural networks", "k-NN", "linear regression with the normal equation", "decision trees"], 0, "Randomly disables neurons during training.", "m"),
 q("k-fold CV is especially useful when…", ["the dataset is small", "the dataset has billions of rows", "there are no labels", "the test set is large"], 0, "Uses every example for validation.", "e"),
 q("After choosing hyperparameters with CV you should…", ["retrain on all training data and evaluate once on the test set", "report the best fold score", "tune again on the test set", "throw away the model"], 0, "Standard procedure.", "e"),
 q("Which ensemble method mainly reduces bias?", ["Boosting", "Bagging", "Random forest", "Majority vote of identical models"], 0, "Each new model fixes remaining errors.", "c"),
 q("Averaging many models helps most when their errors are…", ["independent (uncorrelated)", "identical", "all positive", "zero"], 0, "Correlated errors don't cancel.", "c"),
 q("A random forest is a good default model for tabular data because…", ["it's accurate, robust and needs little tuning", "it never overfits under any settings", "it needs feature scaling", "it outputs a formula"], 0, "A strong baseline.", "m"),
 q("Which plot best diagnoses bias vs variance?", ["Learning curves of training and validation error vs data size", "A histogram of labels", "The ROC curve", "A scatter of two features"], 0, "Gaps and levels tell the story.", "e"),
]
FRQS = [
 {"q": "You fit polynomials of degree 1, 4 and 15 to 30 noisy points. Results: degree 1 — train MSE 9.1, validation MSE 9.6; degree 4 — train 2.0, validation 2.4; degree 15 — train 0.3, validation 14.8.", "parts": [
  {"p": "(a) Classify each model as underfitting, a good fit, or overfitting, and explain using the numbers.", "rubric": [["Degree 1 underfits: both errors high and close", 1], ["Degree 4 good: both low", 1], ["Degree 15 overfits: tiny train error, huge validation error", 1]], "answer": "Degree 1: high bias. Degree 4: good. Degree 15: high variance (0.3 vs 14.8)."},
  {"p": "(b) Name two ways to improve the degree-15 model without lowering the degree.", "rubric": [["Regularization (ridge/lasso, tune λ)", 1], ["More data / augmentation (or early stopping)", 1]], "answer": "Add L2 or L1 regularization and tune λ by cross-validation; collect more data."}]},
 {"q": "Ensembles and validation.", "parts": [
  {"p": "(a) Explain the difference between bagging and boosting.", "rubric": [["Bagging: independent models on bootstrap samples, averaged → lowers variance", 1], ["Boosting: sequential models fitting previous errors → lowers bias", 1]], "answer": "Bagging trains models independently on resampled data and averages them, reducing variance. Boosting trains them in sequence, each correcting the last, reducing bias."},
  {"p": "(b) Describe how to use 5-fold cross-validation to choose the number of trees from {50, 100, 200}.", "rubric": [["For each value, 5 folds: train on 4, score the 5th, average", 1], ["Pick the best average; retrain on all training data; test once", 1]], "answer": "For each candidate, run 5-fold CV and average the scores (15 models in all). Choose the best, retrain on the full training set, then evaluate once on the test set."}]},
]
build("ml", "ml-4", L, 4, "Generalization", 'Learning that <span class="hl">generalizes</span>', "Underfitting and overfitting, the bias–variance trade-off, regularization, cross-validation and ensembles like random forests and boosting.", "Machine learning unit 4: overfitting, underfitting, bias-variance trade-off, L1 and L2 regularization, early stopping, k-fold cross-validation, random forests and gradient boosting.", CH, PQ, CHAL, EXQ, FRQS, OUT, TAGS)
