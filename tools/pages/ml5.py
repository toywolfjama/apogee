from lab_common import *
L = "Machine Learning"
TAGS = {"c": "Concept", "p": "Calculation", "m": "Modeling", "e": "Evaluation"}
OUT = "../../courses/ml/ml-5.html"

NEURON = topic("neuron", "The artificial neuron", f'''
<p>An artificial neuron is logistic regression wearing a different hat: it multiplies each input by a weight, adds them up with a bias, and passes the total through an <b>activation function</b>.</p>
{eq("a = f(w₁x₁ + w₂x₂ + … + b) = f(w · x + b)")}
{xlab("neuron")}
{table(["Activation", "Formula", "Range", "Notes"], [
 ["Sigmoid", "1/(1 + e⁻ᶻ)", "(0, 1)", "good for a probability output; slow to train in hidden layers"],
 ["tanh", "(eᶻ − e⁻ᶻ)/(eᶻ + e⁻ᶻ)", "(−1, 1)", "centred at 0"],
 ["ReLU", "max(0, z)", "[0, ∞)", "the default for hidden layers: cheap, and gradients don't fade for z > 0"],
 ["Step", "1 if z ≥ 0 else 0", "{0, 1}", "the original 1958 perceptron; can't be trained by gradient descent"],
])}
{box("tip", "Why we need nonlinear activations", "Stack two linear layers and you get W₂(W₁x) = (W₂W₁)x: still just one linear layer. Without a nonlinear activation between layers, a 100-layer network is no more powerful than logistic regression.")}
''', pill=("c", "5.1"))

NET = topic("networks", "Layers and the forward pass", f'''
<p>A <b>neural network</b> (multilayer perceptron) arranges neurons in layers. Every neuron in one layer feeds every neuron in the next (<b>fully connected</b> or <b>dense</b>). The layers between input and output are <b>hidden layers</b>; \"deep\" learning just means many of them.</p>
{eq("h = f(W₁x + b₁) &nbsp;&nbsp;&nbsp;&nbsp; ŷ = g(W₂h + b₂)")}
<p>Each layer is a matrix multiply, plus a bias vector, then an activation. A layer with 3 inputs and 4 outputs has a 4 × 3 weight matrix (12 weights) and 4 biases: 16 parameters.</p>
{steps("Forward pass: x = (1, 2), hidden ReLU layer with 2 neurons, linear output", [
 ("a|z₁ = 1·1 + (−1)·2 + 0.5 = −0.5|e", "Neuron 1 has weights (1, −1) and bias 0.5."),
 ("b|z₂ = 0.5·1 + 1·2 − 1 = 1.5|e", "Neuron 2 has weights (0.5, 1) and bias −1."),
 ("c|h = ReLU(−0.5, 1.5) = (0, 1.5)|v", "ReLU zeroes the negative one: neuron 1 is 'off' for this input."),
 ("d|ŷ = 2·0 + 3·1.5 + 0.1 = 4.6|g", "Output weights (2, 3), bias 0.1."),
])}
{xlab("nnet")}
<p>The <b>universal approximation theorem</b> says a network with one hidden layer and enough neurons can approximate any continuous function as closely as you like. In practice, deeper networks learn the same functions with far fewer neurons, building complex features out of simpler ones layer by layer.</p>
''', pill=("m", "5.2"))

BACK = topic("backprop", "Training: backpropagation", f'''
<p>Training a network is gradient descent again: compute the loss, compute the gradient of the loss with respect to every weight, step downhill. The trick is computing millions of gradients efficiently. <b>Backpropagation</b> does it with the chain rule, working backwards from the loss, reusing each layer's result for the layer before.</p>
{eq("∂L/∂w = ∂L/∂ŷ · ∂ŷ/∂z · ∂z/∂w")}
{steps("Backprop through one neuron: x = 2, w = 0.5, b = 0, sigmoid, target y = 1, loss = (ŷ − y)²", [
 ("a|z = 0.5·2 + 0 = 1|e  b|ŷ = σ(1) ≈ 0.731|e", "Forward pass."),
 ("c|∂L/∂ŷ = 2(ŷ − y) = −0.538|v", "How the loss changes with the output."),
 ("d|∂ŷ/∂z = ŷ(1 − ŷ) ≈ 0.197|v", "The derivative of the sigmoid."),
 ("e|∂z/∂w = x = 2|v", "How z changes with w."),
 ("f|∂L/∂w ≈ −0.538 × 0.197 × 2 ≈ −0.212|g", "Multiply along the chain. Negative: increasing w lowers the loss, so gradient descent will raise w."),
])}
<h3>The training loop</h3>
<ol class="steps"><li>Take a mini-batch of examples.</li><li><b>Forward pass:</b> compute predictions and the loss.</li><li><b>Backward pass:</b> backpropagate to get every gradient.</li><li><b>Update:</b> the optimizer adjusts every weight.</li><li>Repeat for many epochs, watching the validation loss.</li></ol>
{code('''
import torch, torch.nn as nn
model = nn.Sequential(nn.Linear(2, 8), nn.ReLU(), nn.Linear(8, 1))
opt = torch.optim.Adam(model.parameters(), lr=0.01)
loss_fn = nn.BCEWithLogitsLoss()
for epoch in range(200):
    for xb, yb in loader:              # mini-batches
        loss = loss_fn(model(xb), yb)  # forward pass
        opt.zero_grad()
        loss.backward()                # backpropagation
        opt.step()                     # gradient descent update
''')}
{mini(("Optimizers", "Plain SGD, SGD with momentum (keeps rolling in a consistent direction), and Adam (adapts the step size for each weight) are the common choices. Adam is the usual default."),
      ("Vanishing gradients", "Sigmoid's slope is at most 0.25, so multiplying many of them in a deep network shrinks gradients toward 0 and early layers stop learning. ReLU, careful weight initialization and residual connections fix this."),
      ("Initialization", "Weights start as small random numbers. If they all started equal, every neuron in a layer would compute the same thing and get the same update forever."),
      ("Hardware", "Training is mostly huge matrix multiplications, which GPUs and TPUs do thousands at a time in parallel."))}
''', pill=("p", "5.3"), det=("Why backprop is efficient", "<p>Computing each weight's gradient separately would repeat the same work over and over. Backprop computes ∂L/∂(layer output) once per layer, then reuses it for all of that layer's weights and to pass the gradient further back. The backward pass costs about the same as roughly two forward passes, no matter how many weights there are.</p>"))

CNN = topic("cnn", "Convolutional networks for images", f'''
<p>A 1000 × 1000 color photo has 3 million inputs. A dense layer with 1000 neurons would need 3 billion weights, and it would have to learn \"cat ear\" separately for every position in the image. <b>Convolutional neural networks (CNNs)</b> solve both problems with small filters that slide across the image, sharing the same weights everywhere.</p>
{xlab("conv")}
{mini(("Convolution layer", "Learns many small filters (3 × 3, 5 × 5). Early layers learn edges and colors; deeper layers combine them into textures, parts (eyes, wheels) and whole objects."),
      ("Pooling", "Max pooling keeps the largest value in each 2 × 2 patch, halving the width and height. It makes the network cheaper and less sensitive to small shifts."),
      ("Parameters", "A 3 × 3 filter on a 3-channel image has 3 × 3 × 3 = 27 weights + 1 bias, whatever the image size."),
      ("Output size", "An n × n image with an f × f filter (no padding, stride 1) gives an (n − f + 1) × (n − f + 1) feature map. Padding with zeros keeps the size the same."))}
<p>For sequences (text, audio, time series) the classic choice was the <b>recurrent neural network (RNN)</b> and its LSTM variant, which read one step at a time while carrying a memory. Since 2017 <b>transformers</b> (unit 6) have largely replaced them.</p>
''', pill=("m", "5.4"))

SUM = topic("summary-ml5", "Unit summary", mini(
 ("Neuron", "a = f(w·x + b). ReLU = max(0, z) for hidden layers; sigmoid/softmax at the output. Nonlinearity is essential."),
 ("Network", "Layers of matrix multiply + bias + activation. Parameters per dense layer = in × out + out."),
 ("Training", "Forward pass → loss → backprop (chain rule) → optimizer step. Mini-batches, epochs, Adam. Beware vanishing gradients."),
 ("CNNs", "Small shared filters slide over images; pooling shrinks. Output size n − f + 1. Transformers now dominate sequences."),
))

CH = [chapter("ch-neuron", "Neurons", "Neurons", [NEURON]),
      chapter("ch-net", "Networks and Training", "Networks", [NET, BACK]),
      chapter("ch-cnn", "Convolutional Networks", "CNNs", [CNN, SUM])]

import math
s1 = 1 / (1 + math.exp(-1)); close(s1, .731); close(2 * (s1 - 1) * s1 * (1 - s1) * 2, -.212)
PQ = [
 q("A neuron has weights (2, −1), bias 1, ReLU, inputs (1, 4). Output?", ["0", "−1", "1", "3"], 0, "z = 2 − 4 + 1 = −1 → ReLU(−1) = 0.", "p"),
 q("Same neuron with inputs (3, 1)?", ["6", "5", "7", "0"], 0, "z = 6 − 1 + 1 = 6.", "p"),
 q("Which activation is the usual default for hidden layers?", ["ReLU", "Step", "Sigmoid", "Linear"], 0, "Cheap and trains well.", "c"),
 q("Why can't a network without nonlinear activations learn XOR?", ["Stacked linear layers collapse into a single linear function", "It needs more data", "XOR has no labels", "The learning rate is too small"], 0, "A linear boundary can't separate XOR.", "c"),
 q("A dense layer from 10 inputs to 5 neurons has how many parameters?", ["55", "50", "15", "60"], 0, "10 × 5 weights + 5 biases.", "p"),
 q("A network 4 → 8 → 3 (dense). Total parameters?", ["67", "56", "44", "35"], 0, "(4·8 + 8) + (8·3 + 3) = 40 + 27.", "p"),
 q("Backpropagation is based on…", ["the chain rule of calculus", "k-means", "the Pythagorean theorem", "random search"], 0, "Gradients flow backwards layer by layer.", "c"),
 q("σ(z) = 0.8. What is σ′(z)?", ["0.16", "0.8", "0.2", "0.64"], 0, "σ(1 − σ) = 0.8 × 0.2.", "p"),
 q("The vanishing gradient problem is worst with…", ["many sigmoid layers", "ReLU layers", "shallow networks", "large learning rates"], 0, "Each sigmoid derivative is at most 0.25.", "c"),
 q("Why are weights initialized randomly instead of all zeros?", ["So neurons in a layer learn different things", "To speed up the forward pass", "Because zero is not allowed", "To make the loss bigger"], 0, "Equal weights stay equal forever (symmetry).", "c"),
 q("Which step updates the weights in a training loop?", ["The optimizer step", "The forward pass", "Computing the loss", "Loading the batch"], 0, "Backward computes gradients; the optimizer applies them.", "c"),
 q("A 28 × 28 image is convolved with a 5 × 5 filter (no padding, stride 1). Output size?", ["24 × 24", "28 × 28", "23 × 23", "5 × 5"], 0, "28 − 5 + 1.", "p"),
 q("How many weights does one 3 × 3 filter have on an RGB image (3 channels), not counting bias?", ["27", "9", "3", "81"], 0, "3 × 3 × 3.", "p"),
 q("Max pooling with a 2 × 2 window on a 16 × 16 feature map gives…", ["8 × 8", "14 × 14", "16 × 16", "4 × 4"], 0, "Halves each side.", "p"),
 q("Why do CNNs use far fewer parameters than dense networks on images?", ["The same small filter is reused at every position", "They ignore color", "They use no biases", "They only look at the center"], 0, "Weight sharing.", "c"),
]
CHAL = [
 q("A neuron: ŷ = σ(wx), x = 1, w = 0, target y = 1, loss = −ln ŷ (cross-entropy). What is ∂L/∂w?", ["−0.5", "0.5", "−1", "0"], 0, "For sigmoid + cross-entropy, ∂L/∂z = ŷ − y = 0.5 − 1 = −0.5, and ∂z/∂w = x = 1.", "p"),
 q("A network has 784 inputs, a 128-neuron hidden layer and 10 outputs (dense). Roughly how many parameters?", ["≈ 101,770", "≈ 922", "≈ 7,840", "≈ 1,000,000"], 0, "784·128 + 128 + 128·10 + 10 = 100,352 + 128 + 1,280 + 10 = 101,770.", "p"),
 q("Which pair of weights and bias makes a single step-activation neuron compute AND of two 0/1 inputs?", ["w = (1, 1), b = −1.5", "w = (1, 1), b = −0.5", "w = (1, −1), b = 0", "w = (−1, −1), b = 1.5"], 0, "z ≥ 0 only when both inputs are 1: 1 + 1 − 1.5 = 0.5.", "m"),
 q("A 32 × 32 × 3 image goes through a conv layer with 16 filters of size 5 × 5 (no padding). Output shape and parameter count?", ["28 × 28 × 16, 1,216 parameters", "32 × 32 × 16, 400 parameters", "28 × 28 × 3, 75 parameters", "27 × 27 × 16, 1,200 parameters"], 0, "Each filter: 5·5·3 + 1 = 76 parameters; × 16 = 1,216. Output 32 − 5 + 1 = 28.", "p"),
 q("Training loss keeps falling but validation loss started rising at epoch 30. Best action?", ["Use the weights from about epoch 30 (early stopping) and add regularization", "Train for many more epochs", "Raise the learning rate", "Remove the validation set"], 0, "Classic overfitting.", "e"),
 q("Ten sigmoid layers each contribute a derivative of at most 0.25 to the chain. The gradient reaching layer 1 is at most what fraction of the gradient at the output?", ["≈ 1 × 10⁻⁶", "0.25", "2.5", "≈ 0.1"], 0, "0.25¹⁰ ≈ 9.5 × 10⁻⁷: vanishing gradients.", "p"),
]
EXQ = [
 q("An artificial neuron computes…", ["an activation of a weighted sum plus bias", "the average of its inputs only", "a decision tree split", "a distance"], 0, "f(w·x + b).", "c"),
 q("ReLU(−3) =", ["0", "−3", "3", "0.05"], 0, "max(0, z).", "p"),
 q("ReLU(2.5) =", ["2.5", "0", "1", "0.92"], 0, "Positive values pass through.", "p"),
 q("tanh outputs values between…", ["−1 and 1", "0 and 1", "0 and ∞", "−∞ and ∞"], 0, "Zero-centred.", "c"),
 q("A layer 6 → 4 has how many weights (not biases)?", ["24", "10", "28", "6"], 0, "6 × 4.", "p"),
 q("'Deep' learning refers to networks with…", ["many layers", "huge learning rates", "no hidden layers", "only convolution"], 0, "Depth = number of layers.", "c"),
 q("The universal approximation theorem says one hidden layer can…", ["approximate any continuous function given enough neurons", "solve any problem quickly", "never overfit", "replace all data"], 0, "It says nothing about how easy training is.", "c"),
 q("During backprop, gradients flow…", ["from the loss back toward the input layer", "from input to output", "randomly", "only through the bias"], 0, "Backward pass.", "c"),
 q("Adam is…", ["an optimizer that adapts the step size per weight", "an activation function", "a loss function", "a type of layer"], 0, "A popular gradient descent variant.", "c"),
 q("A conv layer's filters are…", ["learned during training", "fixed by hand", "random forever", "the input pixels"], 0, "Gradient descent learns them.", "c"),
 q("Pooling layers mainly…", ["shrink feature maps and add tolerance to small shifts", "add parameters", "classify the image", "normalize the labels"], 0, "Downsampling.", "c"),
 q("A 10 × 10 input and 3 × 3 filter, no padding, stride 1, gives…", ["8 × 8", "10 × 10", "7 × 7", "3 × 3"], 0, "10 − 3 + 1.", "p"),
]
FRQS = [
 {"q": "A network has inputs x = (2, 1), one hidden layer of two ReLU neurons, and one sigmoid output. Hidden weights: neuron A (1, 1) bias −1; neuron B (−1, 2) bias 0. Output weights (0.5, −1), bias 0.", "parts": [
  {"p": "(a) Compute the hidden activations.", "rubric": [["z_A = 2, h_A = 2", 1], ["z_B = 0, h_B = 0", 1]], "answer": "z_A = 2 + 1 − 1 = 2 → 2. z_B = −2 + 2 + 0 = 0 → 0."},
  {"p": "(b) Compute the output probability.", "rubric": [["z = 0.5·2 − 1·0 = 1", 1], ["σ(1) ≈ 0.731", 1]], "answer": "z = 1 → σ(1) ≈ 0.731."},
  {"p": "(c) How many parameters does this network have?", "rubric": [["Hidden 2·2 + 2 = 6", 1], ["Output 2 + 1 = 3; total 9", 1]], "answer": "6 + 3 = 9."}]},
 {"q": "Training dynamics.", "parts": [
  {"p": "(a) List the four steps of one training iteration.", "rubric": [["Forward pass and loss", 1], ["Backward pass (gradients) and optimizer update", 1]], "answer": "Forward pass → compute loss → backpropagate gradients → optimizer updates weights."},
  {"p": "(b) Explain why stacking linear layers without activations doesn't add power, using matrices.", "rubric": [["W₂(W₁x + b₁) + b₂ = (W₂W₁)x + (W₂b₁ + b₂)", 1], ["which is a single linear layer", 1]], "answer": "W₂(W₁x + b₁) + b₂ = (W₂W₁)x + (W₂b₁ + b₂): one matrix and one bias, i.e. a single linear layer."},
  {"p": "(c) Explain one cause of vanishing gradients and one fix.", "rubric": [["Cause: chains of small derivatives (sigmoid ≤ 0.25)", 1], ["Fix: ReLU, good initialization, residual connections or normalization", 1]], "answer": "Backprop multiplies many sigmoid slopes (≤ 0.25), so gradients shrink exponentially. Use ReLU activations, careful initialization, residual connections."}]},
]
build("ml", "ml-5", L, 5, "Neural Networks", 'Neural <span class="hl">networks</span>', "Neurons, activations, layers, backpropagation and convolutional networks, with a playground where you can watch a network learn.", "Machine learning unit 5: artificial neurons, activation functions, multilayer perceptrons, forward pass, backpropagation, optimizers, vanishing gradients and convolutional neural networks.", CH, PQ, CHAL, EXQ, FRQS, OUT, TAGS)
