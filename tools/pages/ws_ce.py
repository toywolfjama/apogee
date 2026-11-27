from ws_common import M, build_ws

T = lambda f, n=2: [f(*[(r >> (n - 1 - i)) & 1 for i in range(n)]) for r in range(1 << n)]
XOR = T(lambda a, b: a ^ b); AND = T(lambda a, b: a & b); NOR = T(lambda a, b: 1 - (a | b))
MAJ = T(lambda a, b, c: int(a + b + c >= 2), 3)
FS = T(lambda a, b, c: a ^ b ^ c, 3); FC = T(lambda a, b, c: int(a + b + c >= 2), 3)

G1 = [
 M("bits-1", "Flip the switches", "A register is a row of switches. Flip bits until the register holds each target number. The clock starts at your first click.",
   {"type": "bits", "n": 8, "par": 25, "rounds": [{"t": 5}, {"t": 12}, {"t": 100}, {"t": 255}, {"t": 128}]},
   win="Every unsigned number is a sum of place values: 100 = 64 + 32 + 4.",
   hints=["Start from the biggest place value that fits, subtract it, repeat.", "100 = 64 + 32 + 4."]),
 M("bits-2", "Hex, negatives and letters", "Same register, harder targets: hexadecimal, two's complement negatives and ASCII characters.",
   {"type": "bits", "n": 8, "par": 45, "rounds": [{"t": 0x3C, "as": "hex"}, {"t": 0xA5, "as": "hex"}, {"t": -1, "as": "signed"}, {"t": -100, "as": "signed"}, {"t": 65, "as": "ascii"}, {"t": 122, "as": "ascii"}]},
   win="Hex maps 4 bits per digit; negatives use invert-and-add-1; letters are just numbers ('A' = 65).",
   hints=["Each hex digit is 4 bits: 3 = 0011, C = 1100.", "−1 is all ones. For −100: write 100 = 0110 0100, invert to 1001 1011, add 1 → 1001 1100.", "'A' = 65 = 0100 0001; lowercase letters are 32 higher ('a' = 97), so 'z' = 122."]),
]
G2 = [
 M("gate-xor", "One gate, one job", "Pick the single gate whose output matches the target column.",
   {"type": "gates", "inputs": ["A", "B"], "slots": [{"id": "g", "in": ["A", "B"]}], "outputs": {"Y": "g"}, "target": {"Y": XOR}, "par": 6},
   win="XOR: 1 when the inputs differ. It's a 1-bit adder without the carry.", hints=["Look at rows 01 and 10 versus 11."]),
 M("gate-ha", "Build a half adder", "Two outputs this time: the sum bit S and the carry bit C of A + B.",
   {"type": "gates", "inputs": ["A", "B"], "slots": [{"id": "s", "in": ["A", "B"]}, {"id": "c", "in": ["A", "B"]}], "outputs": {"S": "s", "C": "c"}, "target": {"S": XOR, "C": AND}, "par": 6},
   win="S = A ⊕ B and C = A · B. Chain these and you can add numbers of any size.", hints=["1 + 1 = 10 in binary: sum 0, carry 1."]),
 M("gate-dm", "De Morgan's trick", "Make a NOR gate's truth table, but you can only use NOT on each input followed by one 2-input gate.",
   {"type": "gates", "inputs": ["A", "B"], "slots": [{"id": "na", "in": ["A"]}, {"id": "nb", "in": ["B"]}, {"id": "g", "in": ["na", "nb"]}], "outputs": {"Y": "g"}, "target": {"Y": NOR}, "palette": ["AND", "OR", "XOR", "NAND", "NOT", "BUF"], "par": 6},
   win="(A + B)′ = A′ · B′. That's De Morgan's law: push the NOT through and flip OR to AND.", hints=["NOR is 1 only when both inputs are 0.", "Invert both inputs, then which gate is 1 only when both inverted values are 1?"]),
 M("gate-maj", "The voting machine", "Three judges vote (A, B, C). The light turns on when at least two vote yes.",
   {"type": "gates", "inputs": ["A", "B", "C"], "slots": [{"id": "p", "in": ["A", "B"]}, {"id": "q", "in": ["A", "C"]}, {"id": "r", "in": ["B", "C"]}, {"id": "o", "in": ["p", "q", "r"]}], "outputs": {"M": "o"}, "target": {"M": MAJ}, "par": 8},
   win="M = AB + AC + BC: each pair of judges agreeing is enough.", hints=["Each of the first three gates should detect a pair voting yes together.", "The last gate fires if any pair agrees."]),
 M("gate-fa", "Boss level: the full adder", "Add three bits A + B + Cin. Five gates, two outputs. This is the circuit inside every adder in your computer.",
   {"type": "gates", "inputs": ["A", "B", "Cin"], "slots": [{"id": "x1", "in": ["A", "B"]}, {"id": "x2", "in": ["x1", "Cin"]}, {"id": "a1", "in": ["A", "B"]}, {"id": "a2", "in": ["x1", "Cin"]}, {"id": "o1", "in": ["a1", "a2"]}], "outputs": {"S": "x2", "Cout": "o1"}, "target": {"S": FS, "Cout": FC}, "par": 12},
   win="S = A ⊕ B ⊕ Cin, Cout = AB + Cin(A ⊕ B). Thirty-two of these in a row add 32-bit numbers.", hints=["S is 1 when an odd number of inputs are 1.", "Cout: either A and B are both 1, or exactly one of them is 1 and Cin is 1."]),
 M("kmap-ac", "Draw it on a K-map", "Click cells in the Karnaugh map until the simplest expression is exactly F = AC.",
   {"type": "lab", "task": "Which minterms have A = 1 and C = 1? Turn exactly those cells on.", "lab": {"type": "kmap", "vars": ["A", "B", "C", "D"], "ones": [], "title": "Your K-map", "sub": "Click a cell to make it 1."}, "goal": "expr === 'AC'", "need": "F = AC", "show": [["Current F =", "expr"]]},
   win="AC is a group of four: m10, m11, m14, m15. B and D change across the group, so they drop out.", hints=["A = 1 means the bottom two rows (11 and 10).", "C = 1 means the columns where CD is 11 or 10. Turn on the four cells where those rows and columns cross."]),
]
G3 = [
 M("cpu-1", "Your first program", "Write machine instructions that output M[13] + M[14] − M[15].",
   {"type": "cpuprog", "task": "Output the value of M[13] + M[14] − M[15], then stop.", "data": {"13": 9, "14": 6, "15": 4}, "target": [11], "lines": 8, "par": 5},
   win="LOAD, ADD, SUB, OUT, HALT: five instructions, each one fetched, decoded and executed.", hints=["Get M[13] into the accumulator with LOAD.", "LOAD 13 → ADD 14 → SUB 15 → OUT → HALT."]),
 M("cpu-2", "Make it loop", "Output 3, 2, 1 using a loop (no copy-pasting three OUTs).",
   {"type": "cpuprog", "task": "Output 3, 2, 1 and stop. M[14] = 3 and M[15] = 1.", "data": {"14": 3, "15": 1}, "target": [3, 2, 1], "lines": 10, "par": 6},
   win="A loop is just a conditional jump (JZ) plus an unconditional jump back (JMP).", hints=["LOAD 14, then OUT, then SUB 15.", "After subtracting, if ACC is 0 jump to a HALT; otherwise JMP back to the OUT."]),
 M("cache-1", "Fix the cache conflict", "Play the “conflict” sequence. In a direct-mapped cache addresses 0 and 4 fight over the same line. Change the layout to get a hit rate of at least 50%.",
   {"type": "lab", "task": "Choose a layout, then press “Play: conflict 0, 4, 0, 4”.", "lab": {"type": "cache", "addrBits": 6, "lines": 4, "block": 1, "ways": 1, "seqs": [{"name": "conflict 0, 4, 0, 4", "a": [0, 4, 0, 4, 0, 4, 1, 5]}]}, "goal": "total >= 8 && rate >= 0.5", "need": "hit rate ≥ 50% on 8 accesses", "show": [["Accesses", "total"], ["Hit rate", "rate", "pct"]]},
   win="With 2 ways, addresses 0 and 4 can live in the same set at the same time. Associativity removes conflict misses.", hints=["Direct-mapped gives every address exactly one possible line.", "Switch to 2-way set associative, then play again."]),
]
build_ws("comp-eng", "../../courses/comp-eng/workshop.html", "Computer Engineering", 'The <span class="hl">hardware</span> workshop',
 "Flip bits, wire gates, write machine code and tune a cache. Each mission has a goal, hints if you need them, and up to three stars.",
 [("Bits and Bytes", "Bits", G1), ("Logic Lab", "Gates", G2), ("The Machine", "CPU", G3)], ("wa.js", "math.js", "labs.js"), "Margin · Computer Engineering workshop · Progress saves in this browser")
