from lab_common import *
L = "Machine Learning"
TAGS = {"c": "Concept", "p": "Calculation", "m": "Modeling", "e": "Evaluation"}
OUT = "../../courses/ml/ml-2.html"

LIN = topic("linear", "The linear model", f'''
<p>Linear regression is the \"hello world\" of machine learning, and the ideas in it (a model with parameters, a loss function, and an optimizer that lowers the loss) are exactly the ideas behind giant neural networks.</p>
{eq("ŷ = w·x + b")}
<p>With one feature this is the equation of a line: <b>w</b> (the <b>weight</b>) is the slope and <b>b</b> (the <b>bias</b>) is the intercept. Learning means finding the w and b that make ŷ as close as possible to the true y across the training data.</p>
<p>With d features each one gets its own weight:</p>
{eq("ŷ = w₁x₁ + w₂x₂ + … + w_dx_d + b = <b>w</b> · <b>x</b> + b")}
<p>The <b>dot product</b> <b>w</b> · <b>x</b> multiplies matching entries and adds them up. Each weight says how much the prediction changes when that feature goes up by 1, holding the others fixed.</p>
{worked("A house-price model is ŷ = 0.15·(sq ft) + 12·(bedrooms) − 1.1·(age) + 40, in $k. Predict a 1,600 sq ft, 3-bedroom, 10-year-old house.", "ŷ = 0.15(1600) + 12(3) − 1.1(10) + 40 = 240 + 36 − 11 + 40 = 305, so about $305k. Each extra square foot adds $150, all else equal.")}
''', pill=("m", "2.1"))

LOSS = topic("loss", "Measuring error: the loss function", f'''
<p>For each example the <b>residual</b> is the error y − ŷ. We need one number that summarizes how wrong the model is over the whole training set. The standard choice for regression is the <b>mean squared error</b>:</p>
{eq("MSE = (1/n) Σ (ŷᵢ − yᵢ)²")}
<p>Squaring makes every error positive and punishes big misses much more than small ones (an error of 4 costs 16, an error of 1 costs 1).</p>
{xlab("regress", title="Fit a line by hand, then let gradient descent do it", sub="Drag w and b to lower the MSE. Red segments are residuals. Then try the gradient-step buttons.")}
{table(["Metric", "Formula", "Notes"], [
 ["MSE", "average of squared errors", "the usual training loss; units are squared"],
 ["RMSE", "√MSE", "same units as y (\"typically off by about RMSE\")"],
 ["MAE", "average of |errors|", "less sensitive to outliers"],
 ["R²", "1 − (SS_residual / SS_total)", "fraction of the variance in y the model explains: 1 is perfect, 0 is no better than predicting the mean"],
])}
{worked("Predictions 3, 5, 9 for true values 2, 5, 12. Find MSE, RMSE and MAE.", "Errors 1, 0, −3. MSE = (1 + 0 + 9)/3 = 10/3 ≈ 3.33. RMSE ≈ 1.83. MAE = (1 + 0 + 3)/3 ≈ 1.33.")}
''', pill=("e", "2.2"))

CLOSED = topic("closed", "The best line, in one step", f'''
<p>For simple linear regression calculus gives the exact minimizer of the MSE, called <b>ordinary least squares</b>:</p>
{eq("w = Σ(xᵢ − x̄)(yᵢ − ȳ) / Σ(xᵢ − x̄)² &nbsp;&nbsp;&nbsp;&nbsp; b = ȳ − w·x̄")}
{steps("Least squares for points (1, 2), (2, 3), (3, 5), (4, 6)", [
 ("a|x̄ = 2.5|e  b|ȳ = 4|e", "Means of x and of y."),
 ("c|x − x̄: −1.5 −0.5 0.5 1.5|v  d|y − ȳ: −2 −1 1 2|v", "Deviations from the means."),
 ("e|Σ products = 3 + 0.5 + 0.5 + 3 = 7|e  f|Σ (x − x̄)² = 5|e", "Multiply matching deviations; square the x deviations."),
 ("g|w = 7 / 5 = 1.4|g  h|b = 4 − 1.4(2.5) = 0.5|g", "The best line is ŷ = 1.4x + 0.5. The line always passes through (x̄, ȳ)."),
])}
<p>With many features the same idea becomes the matrix formula <b>w</b> = (XᵀX)⁻¹Xᵀ<b>y</b>. It's exact, but inverting a matrix gets very expensive with lots of features, and most models (logistic regression, neural networks) have no closed-form answer at all. For those we need an algorithm that improves step by step.</p>
''', pill=("p", "2.3"))

GD = topic("gd", "Gradient descent", f'''
<p>Picture the loss as a landscape over every possible setting of the parameters. Gradient descent starts somewhere and repeatedly takes a small step <b>downhill</b>. The <b>gradient</b> (the vector of partial derivatives) points uphill, so we step against it:</p>
{eq("w ← w − α · ∂L/∂w &nbsp;&nbsp;&nbsp;&nbsp; b ← b − α · ∂L/∂b")}
<p>α is the <b>learning rate</b>, the size of each step. For MSE on a line the derivatives are</p>
{eq("∂L/∂w = (2/n) Σ (ŷᵢ − yᵢ)·xᵢ &nbsp;&nbsp;&nbsp;&nbsp; ∂L/∂b = (2/n) Σ (ŷᵢ − yᵢ)")}
{xlab("gd")}
{mini(("α too small", "Tiny steps: it gets there, but takes forever."), ("α too large", "Each step overshoots the bottom. The loss bounces around or blows up (diverges)."),
      ("Local minima", "On a bumpy loss, gradient descent can settle in a valley that isn't the lowest. Linear regression's MSE is a perfect bowl (convex), so there's only one minimum; neural networks aren't."),
      ("Stochastic GD", "Computing the gradient over millions of examples is slow. <b>Mini-batch SGD</b> estimates it from a small random batch (say 32 examples) per step. Noisier, but far faster, and the noise even helps escape bad spots. One pass over the whole training set is an <b>epoch</b>."))}
{worked("One example (x = 2, y = 7). Start w = 1, b = 0, α = 0.1. Do one gradient step.", "ŷ = 2, error ŷ − y = −5. ∂L/∂w = 2(−5)(2) = −20, ∂L/∂b = 2(−5) = −10. New w = 1 − 0.1(−20) = 3, new b = 0 − 0.1(−10) = 1. Now ŷ = 3(2) + 1 = 7: perfect for this point.")}
{code('''
w, b, lr = 0.0, 0.0, 0.01
for epoch in range(1000):
    pred = w * x + b                    # x, y are NumPy arrays
    err = pred - y
    w -= lr * 2 * (err * x).mean()      # step against the gradient
    b -= lr * 2 * err.mean()
''')}
''', pill=("m", "2.4"), det=("Where the derivatives come from", "<p>L = (1/n) Σ (wxᵢ + b − yᵢ)². By the chain rule, the derivative of (stuff)² is 2·(stuff)·(derivative of stuff). The derivative of (wxᵢ + b − yᵢ) with respect to w is xᵢ, and with respect to b it's 1. So ∂L/∂w = (2/n) Σ (ŷᵢ − yᵢ)xᵢ and ∂L/∂b = (2/n) Σ (ŷᵢ − yᵢ).</p>"))

FEAT = topic("features", "Beyond straight lines", f'''
<p>\"Linear\" means linear in the <b>weights</b>, not necessarily in the original inputs. Add new features made from old ones and a linear model can fit curves:</p>
{mini(("Polynomial features", "Use x, x², x³ as three features: ŷ = w₁x + w₂x² + w₃x³ + b. Still linear regression, but the fit is a cubic curve."),
      ("Interactions", "x₁·x₂ lets the effect of one feature depend on another (sunshine helps ice cream sales more when it's also hot)."),
      ("Logs", "log(income) when doubling matters more than adding a fixed amount."),
      ("Domain knowledge", "Distance from the city center may predict rent better than raw latitude and longitude."))}
{graph(title="Same data, more features", sub="A cubic in x is still a linear model in its weights. Slide the weights.", x=[-3, 3], y=[-6, 6], gx=1, gy=1, params={"a": [-1, 1, .05, .3, "w₃"], "c": [-3, 3, .1, -1.5, "w₁"]}, fns=[fn("a*x^3 + c*x", "ŷ = w₃x³ + w₁x")])}
{box("trap", "Correlation is not causation", "A model can predict well from a feature that doesn't cause the outcome. Ice cream sales predict drownings (both go up in summer). A predictive model answers 'what will happen', not 'what should we change'.")}
''', pill=("m", "2.5"))

SUM = topic("summary-ml2", "Unit summary", mini(
 ("Model", "ŷ = w · x + b. Each weight = change in ŷ per unit of that feature, holding others fixed."),
 ("Loss", "MSE = mean of (ŷ − y)². RMSE in y's units, MAE robust to outliers, R² = share of variance explained."),
 ("Least squares", "w = Σ(x − x̄)(y − ȳ) / Σ(x − x̄)², b = ȳ − w x̄. Line passes through (x̄, ȳ)."),
 ("Gradient descent", "w ← w − α ∂L/∂w. α too small = slow, too big = diverges. Mini-batch SGD; epochs. Feature engineering bends a linear model."),
))

CH = [chapter("ch-lin", "The Linear Model", "Linear model", [LIN, LOSS]),
      chapter("ch-fit", "Fitting the Line", "Fitting", [CLOSED, GD]),
      chapter("ch-feat", "Features", "Features", [FEAT, SUM])]

import numpy as np
xs, ys = np.array([1, 2, 3, 4.]), np.array([2, 3, 5, 6.])
w = ((xs - xs.mean()) * (ys - ys.mean())).sum() / ((xs - xs.mean()) ** 2).sum(); close(w, 1.4); close(ys.mean() - w * xs.mean(), .5)
close(np.mean((np.array([3, 5, 9]) - np.array([2, 5, 12])) ** 2), 10 / 3)
PQ = [
 q("In ŷ = wx + b, what does b represent for a single feature?", ["The intercept: the prediction when x = 0", "The slope", "The learning rate", "The error"], 0, "b shifts the line up or down.", "c"),
 q("ŷ = 3x₁ − 2x₂ + 5. Predict for x₁ = 4, x₂ = 1.", ["15", "13", "19", "10"], 0, "12 − 2 + 5.", "p"),
 q("Compute the dot product (2, −1, 3) · (4, 5, 1).", ["6", "12", "−3", "16"], 0, "8 − 5 + 3 = 6.", "p"),
 q("True values 4, 6; predictions 5, 3. MSE?", ["5", "2", "10", "3.16"], 0, "Errors 1, −3 → (1 + 9)/2 = 5.", "p"),
 q("Why does MSE square the errors?", ["To make them positive and penalize big errors more", "To make the math impossible", "To make outliers matter less", "Because errors are always small"], 0, "Squaring grows fast with error size.", "c"),
 q("Which metric is in the same units as the target?", ["RMSE", "MSE", "R²", "Variance"], 0, "Square root undoes the squaring.", "e"),
 q("A model has R² = 0. It is…", ["no better than always predicting the mean", "perfect", "explaining 100% of the variance", "impossible"], 0, "R² compares to the mean baseline.", "e"),
 q("The least-squares line always passes through…", ["(x̄, ȳ)", "the origin", "the first data point", "the largest y value"], 0, "b = ȳ − w x̄.", "c"),
 q("In gradient descent, we move the parameters…", ["opposite to the gradient", "in the direction of the gradient", "randomly", "toward zero only"], 0, "The gradient points uphill.", "c"),
 q("The learning rate is far too large. What usually happens?", ["The loss bounces or explodes (diverges)", "Training is very slow but stable", "The model underfits slightly", "Nothing changes"], 0, "Steps overshoot the minimum.", "c"),
 q("w = 2, ∂L/∂w = 5, α = 0.1. After one step, w =", ["1.5", "2.5", "−3", "1.9"], 0, "2 − 0.1 × 5.", "p"),
 q("One epoch means…", ["one full pass over the training data", "one gradient step", "one example", "one hour of training"], 0, "In mini-batch SGD an epoch is many steps.", "c"),
 q("Linear regression's MSE loss has how many minima?", ["One (it's convex)", "Many", "None", "Two"], 0, "A bowl shape.", "c"),
 q("Using x and x² as features in linear regression lets the model fit…", ["a parabola", "only straight lines", "only horizontal lines", "categories"], 0, "Linear in weights, curved in x.", "m"),
 q("Ice cream sales predict sunburn cases very well. Banning ice cream would…", ["probably not reduce sunburn: correlation isn't causation", "reduce sunburn", "increase sunburn", "prove the model wrong"], 0, "Both are caused by sunny weather.", "m"),
]
CHAL = [
 q("Least squares for (0, 1), (1, 3), (2, 5). Find w and b.", ["w = 2, b = 1", "w = 2, b = 0", "w = 1.5, b = 1.5", "w = 3, b = 1"], 0, "The points are exactly on y = 2x + 1.", "p"),
 q("Data (1, 1), (2, 2), (3, 6). Least-squares slope w?", ["2.5", "2", "3", "1.5"], 0, "x̄ = 2, ȳ = 3. Σ(x − x̄)(y − ȳ) = (−1)(−2) + 0 + (1)(3) = 5. Σ(x − x̄)² = 2. w = 2.5.", "p"),
 None,
 q("Predictions explain y with SS_residual = 20 and SS_total = 80. R²?", ["0.75", "0.25", "4", "60"], 0, "1 − 20/80.", "e"),
 None,
 q("A feature is measured in millimetres instead of metres (values 1000× larger). In the least-squares model its weight becomes…", ["1000× smaller", "1000× larger", "unchanged", "zero"], 0, "ŷ stays the same, so w must shrink by the same factor. That's why weights can't be compared across features unless the features are scaled.", "m"),
]
CHAL[2] = q("Single example x = 3, y = 10. Start w = 1, b = 1, α = 0.05, loss (ŷ − y)². After one step, w = ?", ["2.8", "1.7", "4.6", "−0.8"], 0, "ŷ = 4, error ŷ − y = −6. ∂L/∂w = 2(−6)(3) = −36. w = 1 − 0.05(−36) = 2.8.", "p")
CHAL[4] = q("Loss L(w) = (w − 4)². Start w = 0, α = 1.0. What happens?", ["w alternates 0, 8, 0, 8, … and never converges", "Converges to 4 in one step", "Converges slowly to 4", "Diverges to infinity"], 0, "Gradient = 2(w − 4). From 0: 0 − 1(−8) = 8. From 8: 8 − 1(8) = 0. It bounces forever. (α = 0.5 would land on 4 in one step.)", "p")
close(1 - 0.05 * -36, 2.8)
EXQ = [
 q("Linear regression predicts…", ["a number", "a category", "a cluster", "a probability only"], 0, "Regression = numeric output.", "c"),
 q("ŷ = 0.5x + 2 at x = 10 gives…", ["7", "12", "5.2", "20"], 0, "5 + 2.", "p"),
 q("Errors 2, −2, 0, 4. MAE?", ["2", "6", "1", "3"], 0, "(2 + 2 + 0 + 4)/4.", "p"),
 q("Errors 2, −2, 0, 4. MSE?", ["6", "2", "24", "4"], 0, "(4 + 4 + 0 + 16)/4.", "p"),
 q("Which loss is least affected by a single huge outlier?", ["MAE", "MSE", "RMSE", "They're identical"], 0, "MAE grows linearly with error, not quadratically.", "e"),
 q("The gradient of a function points…", ["in the direction of steepest increase", "toward the minimum", "toward zero", "sideways"], 0, "So we step the other way.", "c"),
 q("The update rule of gradient descent is…", ["θ ← θ − α ∇L", "θ ← θ + α ∇L", "θ ← α θ", "θ ← ∇L"], 0, "Subtract the scaled gradient.", "c"),
 q("Mini-batch SGD computes each step's gradient from…", ["a small random subset of the data", "the entire dataset", "a single feature", "the test set"], 0, "Faster, noisier steps.", "c"),
 q("If the training loss decreases very slowly but steadily, you might…", ["increase the learning rate a bit", "decrease the learning rate", "delete the bias", "stop using a loss"], 0, "Steps are too small.", "m"),
 q("R² of 0.9 means…", ["the model explains 90% of the variance in y", "90% of predictions are exactly right", "the error is 0.9", "the slope is 0.9"], 0, "Fraction of variance explained.", "e"),
 q("Least squares w for points with Σ(x − x̄)(y − ȳ) = 12 and Σ(x − x̄)² = 4?", ["3", "48", "1/3", "16"], 0, "12/4.", "p"),
 q("Adding x² as a feature to linear regression makes the model…", ["able to fit a curve while staying linear in its weights", "nonlinear in its weights", "a classifier", "unable to train"], 0, "Feature engineering.", "m"),
]
FRQS = [
 {"q": "Hours studied (x) vs score (y): (1, 60), (2, 70), (3, 75), (4, 85), (5, 90).", "parts": [
  {"p": "(a) Find the least-squares line.", "rubric": [["x̄ = 3, ȳ = 76", 1], ["w = 75/10 = 7.5", 1], ["b = 76 − 22.5 = 53.5", 1]], "answer": "Deviations x: −2…2; y: −16, −6, −1, 9, 14. Σ products = 32 + 6 + 0 + 9 + 28 = 75. Σ(x − x̄)² = 10. w = 7.5, b = 76 − 7.5·3 = 53.5. ŷ = 7.5x + 53.5."},
  {"p": "(b) Predict the score for 3.5 hours and interpret the slope.", "rubric": [["ŷ = 79.75", 1], ["Each extra hour is associated with about 7.5 more points", 1]], "answer": "7.5(3.5) + 53.5 = 79.75. Each extra hour studied goes with about 7.5 more points (an association, not proof of cause)."},
  {"p": "(c) Would you trust a prediction for 20 hours? Explain.", "rubric": [["No: extrapolation beyond the data range", 1], ["Scores cap at 100; the line would predict 203.5", 1]], "answer": "No. 20 hours is far outside the training range (1–5). The line predicts 203.5, impossible on a 100-point test."}]},
 {"q": "Gradient descent by hand. Data: (x, y) = (1, 3) and (2, 5). Model ŷ = wx + b, loss = MSE. Start w = 0, b = 0, α = 0.1.", "parts": [
  {"p": "(a) Compute the gradients ∂L/∂w and ∂L/∂b at the start.", "rubric": [["Errors ŷ − y = −3, −5", 1], ["∂L/∂w = (2/2)(−3·1 + −5·2) = −13; ∂L/∂b = −8", 2]], "answer": "Errors −3 and −5. ∂L/∂w = (2/2)(−3 − 10) = −13. ∂L/∂b = (2/2)(−3 − 5) = −8."},
  {"p": "(b) Do one update and compute the new MSE.", "rubric": [["w = 1.3, b = 0.8", 1], ["Predictions 2.1, 3.4 → MSE = (0.81 + 2.56)/2 = 1.685", 1]], "answer": "w = 0 + 1.3 = 1.3, b = 0.8. ŷ = 2.1 and 3.4. MSE = (0.9² + 1.6²)/2 = 1.685 (down from 17)."}]},
]
build("ml", "ml-2", L, 2, "Linear Regression and Gradient Descent", 'Learning a <span class="hl">line</span>', "Models, loss functions, least squares and gradient descent: the core loop of machine learning, worked out on the simplest model there is.", "Machine learning unit 2: linear regression, mean squared error, R², least squares, gradient descent, learning rates, SGD and feature engineering.", CH, PQ, CHAL, EXQ, FRQS, OUT, TAGS)
