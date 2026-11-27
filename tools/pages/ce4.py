from lab_common import *
L = "Computer Engineering"
TAGS = {"c": "Concept", "p": "Calculation", "d": "Design", "r": "Reading circuits"}
OUT = "../../courses/comp-eng/ce-4.html"

FA = [{"id": "x1", "t": "XOR", "in": ["A", "B"]}, {"id": "x2", "t": "XOR", "in": ["x1", "Cin"]}, {"id": "a1", "t": "AND", "in": ["A", "B"]}, {"id": "a2", "t": "AND", "in": ["x1", "Cin"]}, {"id": "o1", "t": "OR", "in": ["a1", "a2"]}]
ADD = topic("adders", "Adders: how a computer does arithmetic", f'''
<p>A <b>combinational circuit</b> has outputs that depend only on its current inputs; it has no memory. The most important one in any computer is the adder.</p>
<h3>Half adder: add two bits</h3>
<p>Adding two bits gives a 2-bit answer: 0+0 = 00, 0+1 = 01, 1+1 = 10. The low bit is the <b>sum</b> S, the high bit is the <b>carry</b> C.</p>
{eq("S = A ⊕ B &nbsp;&nbsp;&nbsp;&nbsp; C = A · B")}
{xlab("circuit", title="Half adder", inputs=["A", "B"], gates=[{"id": "x", "t": "XOR", "in": ["A", "B"]}, {"id": "a", "t": "AND", "in": ["A", "B"]}], outputs={"S": "x", "C": "a"})}
<h3>Full adder: add two bits plus a carry in</h3>
<p>To add multi-bit numbers each column also needs the carry from the column to its right. A <b>full adder</b> has three inputs (A, B, C<sub>in</sub>):</p>
{eq("S = A ⊕ B ⊕ C<sub>in</sub> &nbsp;&nbsp;&nbsp;&nbsp; C<sub>out</sub> = AB + C<sub>in</sub>(A ⊕ B)")}
{xlab("circuit", title="Full adder", inputs=["A", "B", "Cin"], gates=FA, outputs={"S": "x2", "Cout": "o1"}, note="S is 1 when an odd number of inputs are 1. Cout is 1 when at least two are 1 (it's the majority function from unit 3).")}
<h3>Ripple-carry adder</h3>
<p>Chain n full adders, feeding each carry out into the next carry in, and you can add n-bit numbers. Here's a 2-bit version: inputs A₁A₀ + B₁B₀.</p>
{xlab("circuit", title="2-bit ripple-carry adder", inputs=["A1", "A0", "B1", "B0"], init=[0, 1, 1, 1], gates=[{"id": "s0", "t": "XOR", "in": ["A0", "B0"], "label": "XOR (S0)"}, {"id": "c0", "t": "AND", "in": ["A0", "B0"], "label": "AND (carry)"}, {"id": "x1", "t": "XOR", "in": ["A1", "B1"]}, {"id": "s1", "t": "XOR", "in": ["x1", "c0"]}, {"id": "g1", "t": "AND", "in": ["A1", "B1"]}, {"id": "p1", "t": "AND", "in": ["x1", "c0"]}, {"id": "co", "t": "OR", "in": ["g1", "p1"]}], outputs={"Cout": "co", "S1": "s1", "S0": "s0"}, note="Try 01 + 11: the carry from bit 0 ripples into bit 1. The answer Cout S1 S0 = 100 = 4.")}
{box("trap", "Ripple is slow", "Each full adder must wait for the carry from the one before it. In a 64-bit ripple adder the last sum bit can't settle until the carry has crawled through all 64 stages. Real CPUs use faster designs (below).")}
''', pill=("d", "4.1"))

SUBALU = topic("alu", "Subtraction, the ALU and fast carries", f'''
<p><b>Subtraction for free:</b> A − B = A + B′ + 1 (two's complement). Put an XOR gate on each B input controlled by a signal SUB, and feed SUB into the first carry in. When SUB = 0 the XORs pass B through and C<sub>in</sub> = 0 (add). When SUB = 1 the XORs invert B and C<sub>in</sub> = 1 (subtract). One circuit does both.</p>
<p>The <b>arithmetic logic unit (ALU)</b> is the calculator at the heart of a CPU. It computes several results at once (sum, AND, OR, XOR, a comparison…) and a multiplexer picks the one the instruction asked for. It also produces <b>flags</b>:</p>
{table(["Flag", "Set when", "Used for"], [["Z (zero)", "the result is 0", "if a == b (compute a − b, check Z)"], ["N (negative)", "the top bit of the result is 1", "if a < b for signed numbers"], ["C (carry)", "there was a carry out of the top bit", "unsigned overflow, multi-word arithmetic"], ["V (overflow)", "signed overflow happened", "detecting wrong signed results"]])}
<h3>Propagation delay and carry lookahead</h3>
<p>Every gate takes a tiny time to respond, its <b>propagation delay</b> (a few picoseconds in a modern chip). The longest path from any input to any output is the <b>critical path</b>; it sets how fast the clock can tick.</p>
<p>For each bit position define <b>generate</b> G = AB (this column makes a carry by itself) and <b>propagate</b> P = A ⊕ B (this column passes an incoming carry along). Then</p>
{eq("C<sub>i+1</sub> = G<sub>i</sub> + P<sub>i</sub>C<sub>i</sub>")}
<p>Expanding this, C₂ = G₁ + P₁G₀ + P₁P₀C₀, and so on: every carry can be computed directly from the inputs in two gate levels. A <b>carry-lookahead adder</b> does exactly that, trading extra gates for speed. Its delay grows like log n instead of n.</p>
{worked("A ripple-carry adder's full adder has a carry delay of 2 gate delays. How long until the final carry of a 32-bit adder is ready?", "The carry passes through 32 stages: 32 × 2 = 64 gate delays. At 10 ps per gate that's 640 ps, which alone would limit the clock to about 1.5 GHz.")}
''', pill=("c", "4.2"))

MUX = topic("mux", "Multiplexers: choosing between inputs", f'''
<p>A <b>multiplexer (MUX)</b> is a digital switch. Its <b>select</b> inputs choose which data input is copied to the output. A 2:1 MUX has one select bit; a 4:1 MUX has two; an 2ⁿ:1 MUX has n.</p>
{eq("2:1 MUX: Y = S′·D₀ + S·D₁")}
{xlab("circuit", title="2:1 multiplexer", inputs=["S", "D0", "D1"], gates=[{"id": "n", "t": "NOT", "in": ["S"]}, {"id": "a0", "t": "AND", "in": ["D0", "n"]}, {"id": "a1", "t": "AND", "in": ["D1", "S"]}, {"id": "o", "t": "OR", "in": ["a0", "a1"]}], outputs={"Y": "o"}, note="S = 0 lets D0 through; S = 1 lets D1 through.")}
<p>MUXes are everywhere in a CPU: picking which register feeds the ALU, choosing between PC + 4 and a branch target, selecting which ALU result to keep. A MUX can also implement any function directly: put the truth table's output column on the data inputs and the variables on the select lines.</p>
{worked("Implement F(A, B) = A ⊕ B with a 4:1 MUX.", "Select lines = A, B. Data inputs D₀…D₃ = the truth table outputs 0, 1, 1, 0. Done, no other gates needed.")}
''', pill=("d", "4.3"))

DEC = topic("decoders", "Decoders, encoders and comparators", f'''
<p>A <b>decoder</b> turns an n-bit code into 2ⁿ separate lines, exactly one of which is 1. Memory uses decoders to activate the one row that matches an address.</p>
{xlab("circuit", title="2-to-4 decoder", inputs=["A1", "A0"], gates=[{"id": "n1", "t": "NOT", "in": ["A1"]}, {"id": "n0", "t": "NOT", "in": ["A0"]}, {"id": "y0", "t": "AND", "in": ["n1", "n0"]}, {"id": "y1", "t": "AND", "in": ["n1", "A0"]}, {"id": "y2", "t": "AND", "in": ["A1", "n0"]}, {"id": "y3", "t": "AND", "in": ["A1", "A0"]}], outputs={"Y0": "y0", "Y1": "y1", "Y2": "y2", "Y3": "y3"}, note="Each output is one minterm. Output Yk is 1 exactly when the input is k in binary.")}
{mini(("Encoder", "The reverse: 2ⁿ input lines → n-bit code. A priority encoder outputs the code of the highest-numbered active input, used to decide which interrupt or request goes first."),
      ("Comparator", "A = B for one bit is XNOR. For n bits, AND together all n XNORs. A > B and A < B come from subtracting and checking flags, or from a dedicated magnitude comparator."),
      ("7-segment decoder", "Turns a 4-bit digit 0–9 into the 7 signals that light the segments of a display. Each segment is its own K-map problem, and codes 10–15 are don't-cares."),
      ("Demultiplexer", "One input, many outputs: the select bits choose which output receives the data. It's a decoder with an enable input."))}
''', pill=("d", "4.4"))

SUM = topic("summary-ce4", "Unit summary", mini(
 ("Adders", "Half: S = A⊕B, C = AB. Full: S = A⊕B⊕Cin, Cout = AB + Cin(A⊕B). Ripple-carry = chain of full adders; delay grows with n."),
 ("ALU", "A − B = A + B′ + 1 via XORs on B. Flags Z, N, C, V. Carry lookahead: G = AB, P = A⊕B, Cᵢ₊₁ = Gᵢ + PᵢCᵢ."),
 ("MUX", "Select bits choose a data input. 2ⁿ:1 MUX has n selects. Can implement any truth table."),
 ("Decoders", "n inputs → 2ⁿ one-hot outputs (each a minterm). Encoders go the other way. Equality = AND of XNORs."),
))

CH = [chapter("ch-add", "Adders", "Adders", [ADD, SUBALU]),
      chapter("ch-mux", "Multiplexers and Decoders", "MUX & decoders", [MUX, DEC, SUM])]

PQ = [
 q("A half adder's carry output is which gate of A and B?", ["AND", "XOR", "OR", "NAND"], 0, "Carry is 1 only for 1 + 1.", "c"),
 q("A half adder's sum output is which gate of A and B?", ["XOR", "AND", "OR", "XNOR"], 0, "Sum is 1 when exactly one input is 1.", "c"),
 q("A full adder has inputs A = 1, B = 1, Cin = 1. Outputs (Cout, S)?", ["(1, 1)", "(1, 0)", "(0, 1)", "(1, 1, 1)"], 0, "1 + 1 + 1 = 3 = 11₂.", "p"),
 q("A full adder has A = 1, B = 0, Cin = 1. Outputs (Cout, S)?", ["(1, 0)", "(0, 1)", "(1, 1)", "(0, 0)"], 0, "1 + 0 + 1 = 2 = 10₂.", "p"),
 q("How many full adders does an 8-bit ripple-carry adder need?", ["8", "16", "4", "7 plus a half adder only"], 0, "One per bit (the lowest could be a half adder, but 8 full adders is the standard design).", "c"),
 q("How does an adder/subtractor compute A − B?", ["A + B′ + 1", "A + B − 1", "A′ + B", "(A + B)′"], 0, "Two's complement: invert B with XORs and set the carry in to 1.", "c"),
 q("Why is a ripple-carry adder slow for wide numbers?", ["Each stage waits for the carry from the previous stage", "XOR gates are slow", "It uses too much memory", "It needs a clock for each bit"], 0, "The delay grows linearly with the number of bits.", "c"),
 q("In carry lookahead, a bit position 'generates' a carry when…", ["A and B are both 1", "A or B is 1", "A and B differ", "the carry in is 1"], 0, "G = AB: this column produces a carry no matter what comes in.", "c"),
 q("How many select lines does an 8:1 multiplexer need?", ["3", "8", "2", "4"], 0, "2³ = 8.", "c"),
 q("A 2:1 MUX has S = 1, D0 = 0, D1 = 1. Output?", ["1", "0", "S", "undefined"], 0, "S = 1 selects D1.", "r"),
 q("A 3-to-8 decoder receives input 101. Which output is 1?", ["Y5", "Y3", "Y1", "Y8"], 0, "101₂ = 5. Exactly one output is active.", "r"),
 q("How many outputs does a 4-to-16 decoder have, and how many are 1 at once?", ["16 outputs, exactly 1 active", "4 outputs, 1 active", "16 outputs, 4 active", "16 outputs, any number active"], 0, "One-hot output.", "c"),
 q("Which gate checks if two single bits are equal?", ["XNOR", "XOR", "NAND", "OR"], 0, "XNOR is 1 when its inputs match.", "c"),
 q("After the ALU computes a − b, the Z flag is 1. What do we know?", ["a equals b", "a is less than b", "an overflow happened", "b is zero"], 0, "Z = the result was zero.", "c"),
 q("A circuit's output depends only on its present inputs, not on any history. It is…", ["combinational", "sequential", "a flip-flop", "clocked"], 0, "No memory = combinational.", "c"),
]
CHAL = [
 q("In a 4-bit carry-lookahead adder, which is C₂ written with generate/propagate terms?", ["G₁ + P₁G₀ + P₁P₀C₀", "G₁ + G₀ + C₀", "P₁P₀C₀", "G₁P₁ + G₀P₀"], 0, "C₁ = G₀ + P₀C₀; substitute into C₂ = G₁ + P₁C₁.", "p"),
 q("To implement F(A, B, C) = Σm(1, 2, 6, 7) with a 4:1 MUX using A and B as selects, the data inputs D₀…D₃ should be…", ["C, C′, 0, 1", "0, 1, 1, 0", "C′, C, 1, 0", "1, 0, C, C′"], 0, "AB = 00: m0 = 0, m1 = 1 → C. AB = 01: m2 = 1, m3 = 0 → C′. AB = 10: m4, m5 = 0 → 0. AB = 11: m6, m7 = 1 → 1.", "d"),
 q("A 4-bit adder/subtractor computes 0101 − 0111 (5 − 7). What 4 bits come out, and what is the carry out?", ["1110, carry 0", "1110, carry 1", "0010, carry 1", "1010, carry 0"], 0, "0101 + 1000 + 1 = 1110 (= −2), with no carry out. In subtraction, carry 0 means a borrow occurred (5 < 7 unsigned).", "p"),
 q("Each gate has 15 ps of delay. A full adder's carry path is 2 gates. What is the worst-case delay of a 16-bit ripple adder's carry chain?", ["480 ps", "240 ps", "30 ps", "960 ps"], 0, "16 × 2 × 15 = 480 ps.", "p"),
 q("How many 2-input AND gates (no other gates except inverters) does a 3-to-8 decoder need if built from 2-input ANDs only?", ["16", "8", "24", "12"], 0, "Each output is a 3-input AND = two 2-input ANDs, so 8 × 2 = 16.", "d"),
 q("A signed overflow flag V for addition can be computed from the carries into and out of the top bit as…", ["V = C_in(top) ⊕ C_out(top)", "V = C_out(top)", "V = C_in(top) · C_out(top)", "V = N ⊕ Z"], 0, "Overflow happens exactly when the carry into the sign bit differs from the carry out of it.", "c"),
]
EXQ = [
 q("1 + 1 in a half adder gives S and C =", ["S = 0, C = 1", "S = 1, C = 1", "S = 1, C = 0", "S = 0, C = 0"], 0, "10₂.", "p"),
 q("A full adder's Cout is 1 when…", ["at least two inputs are 1", "exactly one input is 1", "all inputs are 0", "Cin is 1"], 0, "It's the majority function.", "c"),
 q("A full adder's sum is 1 when…", ["an odd number of inputs are 1", "all inputs are 1 only", "at least two inputs are 1", "Cin is 0"], 0, "S = A ⊕ B ⊕ Cin is parity.", "c"),
 q("A ripple-carry adder connects each stage's ___ to the next stage's ___.", ["carry out, carry in", "sum, carry in", "carry in, sum", "sum, sum"], 0, "Carries ripple from low bit to high bit.", "c"),
 q("The critical path of a circuit is…", ["its longest input-to-output delay path", "the path with the most wires", "the clock line", "the power supply"], 0, "It limits the clock speed.", "c"),
 q("A 16:1 MUX needs how many select bits?", ["4", "16", "8", "2"], 0, "2⁴ = 16.", "c"),
 q("For a 2:1 MUX, Y =", ["S′D₀ + SD₁", "SD₀ + S′D₁", "D₀ ⊕ D₁", "S(D₀ + D₁)"], 0, "S = 0 picks D₀.", "d"),
 q("A 2-to-4 decoder with input 10 activates…", ["Y2", "Y1", "Y0 and Y1", "Y4"], 0, "10₂ = 2.", "r"),
 q("Which device selects one of many inputs?", ["Multiplexer", "Decoder", "Demultiplexer", "Encoder"], 0, "MUX = many in, one out.", "c"),
 q("The ALU's N flag after a subtraction a − b is 1. For signed numbers with no overflow, this means…", ["a < b", "a > b", "a = b", "b = 0"], 0, "The result is negative.", "c"),
 q("Why add XOR gates on the B inputs of an adder?", ["To invert B when subtracting", "To double B", "To compare A and B", "To store B"], 0, "B ⊕ 1 = B′, B ⊕ 0 = B.", "d"),
 q("Carry-lookahead adders are faster than ripple adders because…", ["carries are computed in parallel from G and P signals", "they skip the sum bits", "they use fewer gates", "they run at a higher voltage"], 0, "More gates, shorter critical path.", "c"),
]
FRQS = [
 {"q": "Adders.", "parts": [
  {"p": "(a) Write the truth table for a full adder (inputs A, B, Cin; outputs Cout, S).", "rubric": [["All 8 rows", 1], ["Correct S column (0 1 1 0 1 0 0 1)", 1], ["Correct Cout column (0 0 0 1 0 1 1 1)", 1]], "answer": "ABC → (Cout,S): 000→00, 001→01, 010→01, 011→10, 100→01, 101→10, 110→10, 111→11."},
  {"p": "(b) Show the carries and result when a 4-bit ripple adder computes 1011 + 0110.", "rubric": [["Carries: 0 into bit 1, then 1 into bits 2 and 3 and 1 out of bit 3", 1], ["Sum 0001 with carry out 1 (11 + 6 = 17)", 1]], "answer": "Bit0: 1+0 = 1, c 0. Bit1: 1+1 = 0, c 1. Bit2: 0+1+1 = 0, c 1. Bit3: 1+0+1 = 0, c 1. Result 1 0001 = 17 ✓ (4-bit register keeps 0001, carry flag set)."},
  {"p": "(c) Explain how the same adder can subtract.", "rubric": [["XOR each B bit with SUB to invert it", 1], ["Set Cin = SUB = 1 so A + B′ + 1 = A − B", 1]], "answer": "Pass each B bit through an XOR with the SUB control and set the carry in to SUB. With SUB = 1 the adder computes A + B′ + 1 = A − B."}]},
 {"q": "Design a circuit with a 2-bit input N = N₁N₀ that outputs F = 1 when N is 1 or 2.", "parts": [
  {"p": "(a) Give F as a Boolean expression and name the gate it is.", "rubric": [["F = N₁′N₀ + N₁N₀′", 1], ["= N₁ ⊕ N₀ (XOR)", 1]], "answer": "Rows 01 and 10 → F = N₁′N₀ + N₁N₀′ = N₁ ⊕ N₀."},
  {"p": "(b) Implement F with a 2-to-4 decoder and one more gate.", "rubric": [["Uses decoder outputs Y1 and Y2", 1], ["ORs them", 1]], "answer": "Feed N into the decoder and OR its outputs Y1 and Y2."},
  {"p": "(c) Implement F with a 4:1 MUX.", "rubric": [["Selects N₁N₀", 1], ["Data inputs 0, 1, 1, 0", 1]], "answer": "Select lines N₁N₀; D₀ = 0, D₁ = 1, D₂ = 1, D₃ = 0."}]},
]
build("comp-eng", "ce-4", L, 4, "Combinational Circuits", 'Circuits that <span class="hl">compute</span>', "Half and full adders, the ALU, multiplexers and decoders: the building blocks inside every processor.", "Intro to computer engineering unit 4: half adders, full adders, ripple-carry and carry-lookahead adders, ALUs, multiplexers, decoders and comparators.", CH, PQ, CHAL, EXQ, FRQS, OUT, TAGS)
