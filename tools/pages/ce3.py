from lab_common import *
L = "Computer Engineering"
TAGS = {"c": "Concept", "p": "Calculation", "d": "Design", "r": "Reading circuits"}
OUT = "../../courses/comp-eng/ce-3.html"

GATES = topic("gates", "Logic gates", f'''
<p>A <b>logic gate</b> takes one or more bits in and produces one bit out. Gates are built from a handful of transistors (unit 1), and every digital circuit, including a whole CPU, is gates wired together.</p>
{xlab("gate")}
{table(["Gate", "Boolean expression", "Output is 1 when…", "Spoken"], [
 ["NOT", "Y = A′ (or Ā, ¬A)", "A is 0", "not A"],
 ["AND", "Y = A · B (or AB)", "both inputs are 1", "A and B"],
 ["OR", "Y = A + B", "at least one input is 1", "A or B"],
 ["NAND", "Y = (AB)′", "not both are 1", ""],
 ["NOR", "Y = (A + B)′", "both are 0", ""],
 ["XOR", "Y = A ⊕ B = A′B + AB′", "the inputs differ", "exclusive or"],
 ["XNOR", "Y = (A ⊕ B)′", "the inputs are equal", "equivalence"],
])}
{box("trap", "+ is not addition", "In Boolean algebra, + means OR, so 1 + 1 = 1. And · means AND. Read A + B as \"A or B\".")}
<p>A <b>truth table</b> lists the output for every combination of inputs. With n inputs there are 2ⁿ rows. Write the rows in binary counting order (000, 001, 010, …) so you never miss one.</p>
''', pill=("c", "3.1"))

ALG = topic("algebra", "Boolean algebra", f'''
<p>Boolean algebra lets you simplify a circuit on paper before you build it. Fewer gates means a cheaper, faster, cooler chip.</p>
{table(["Law", "AND form", "OR form"], [
 ["Identity", "A · 1 = A", "A + 0 = A"],
 ["Null (domination)", "A · 0 = 0", "A + 1 = 1"],
 ["Idempotent", "A · A = A", "A + A = A"],
 ["Complement", "A · A′ = 0", "A + A′ = 1"],
 ["Double negation", "(A′)′ = A", ""],
 ["Commutative", "AB = BA", "A + B = B + A"],
 ["Associative", "(AB)C = A(BC)", "(A + B) + C = A + (B + C)"],
 ["Distributive", "A(B + C) = AB + AC", "A + BC = (A + B)(A + C)"],
 ["Absorption", "A(A + B) = A", "A + AB = A"],
 ["De Morgan", "(AB)′ = A′ + B′", "(A + B)′ = A′B′"],
])}
<p><b>De Morgan's laws</b> are the most important: to push a NOT through a group, <b>flip AND ↔ OR and complement each variable</b>. "Not (raining and cold)" is the same as "not raining or not cold".</p>
{steps("Simplify Y = AB + AB′ + A′B", [
 ("a|AB + AB′|e  b|+ A′B|n", "Group the first two terms."),
 ("c|A(B + B′)|e  b|+ A′B|n", "Factor out A (distributive law)."),
 ("d|A · 1|e  b|+ A′B|n", "B + B′ = 1 (complement law)."),
 ("e|A + A′B|e", "A · 1 = A."),
 ("f|A + B|g", "A + A′B = A + B. (If A is 1 the result is 1; if A is 0 it's just B.) Three gates → one OR gate."),
])}
{steps("Use De Morgan on Y = (A′ + BC)′", [
 ("a|(A′ + BC)′|e", "A NOT over an OR."),
 ("b|(A′)′ · (BC)′|e", "De Morgan: OR becomes AND, complement each piece."),
 ("c|A · (B′ + C′)|e", "Double negation, and De Morgan again on (BC)′."),
 ("d|AB′ + AC′|g", "Distribute if you want sum-of-products form."),
])}
{box("tip", "Check with a truth table", "Any two Boolean expressions are equal if and only if their truth tables match on every row. When in doubt, build both tables.")}
''', pill=("p", "3.2"), det=("Proving A + A′B = A + B", "<p>A + A′B = (A + A′)(A + B) by the OR-distributive law = 1 · (A + B) = A + B. Or check all four rows: (0,0) → 0 and 0; (0,1) → 1 and 1; (1,0) → 1 and 1; (1,1) → 1 and 1. ✓</p>"))

SOP = topic("sop", "From truth table to circuit", f'''
<p>Any truth table can be turned into a circuit with this recipe, called <b>sum of products (SOP)</b>:</p>
<ol class="steps"><li>Find every row where the output is 1. Each one is a <b>minterm</b>.</li>
<li>Write an AND term for that row: use the variable if it's 1 in that row, its complement if it's 0.</li>
<li>OR all the terms together.</li></ol>
{worked("Build the majority function M(A, B, C): output 1 when at least two inputs are 1.", "Rows with output 1: 011, 101, 110, 111 (minterms 3, 5, 6, 7). SOP: M = A′BC + AB′C + ABC′ + ABC. Simplified (see K-maps below): M = AB + AC + BC.")}
{xlab("circuit", title="Majority vote circuit", inputs=["A", "B", "C"], gates=[{"id": "g1", "t": "AND", "in": ["A", "B"]}, {"id": "g2", "t": "AND", "in": ["A", "C"]}, {"id": "g3", "t": "AND", "in": ["B", "C"]}, {"id": "g4", "t": "OR", "in": ["g1", "g2", "g3"]}], outputs={"M": "g4"}, note="M = AB + AC + BC. This is used in fault-tolerant systems: three computers vote, and a single faulty one is outvoted.")}
<p>The dual recipe, <b>product of sums (POS)</b>, uses the rows where the output is 0 (<b>maxterms</b>): write an OR term that is 0 on that row (the variable if it's 0, its complement if it's 1), then AND them. POS is shorter when the output has fewer 0s than 1s.</p>
<p>Shorthand: F(A, B, C) = Σm(3, 5, 6, 7) lists the minterms, and F = ΠM(0, 1, 2, 4) lists the maxterms. They describe the same function.</p>
''', pill=("d", "3.3"))

KMAP = topic("kmaps", "Karnaugh maps", f'''
<p>A <b>K-map</b> is a truth table folded into a grid so that neighbouring cells differ in exactly one variable. The columns are in <b>Gray code order</b> (00, 01, 11, 10), not counting order. That way, any two adjacent 1s can be merged and one variable disappears.</p>
{xlab("kmap", vars=["A", "B", "C", "D"], ones=[0, 2, 5, 7, 8, 10, 13, 15], title="4-variable K-map", sub="Click cells to change the function: 0 → 1 → X (don't care) → 0. The four corners and the middle form two groups of four.")}
<ol class="steps"><li>Circle groups of 1s. Each group must be a rectangle with <b>1, 2, 4, 8 or 16</b> cells.</li>
<li>Make groups <b>as large as possible</b>; bigger groups mean fewer variables.</li>
<li>Groups may <b>overlap</b>, and they <b>wrap around</b> the edges (the left and right columns are neighbours, so are the top and bottom rows, and so are the four corners).</li>
<li>Use as <b>few groups</b> as possible while covering every 1.</li>
<li>For each group, keep only the variables that stay the same across the whole group.</li></ol>
<p>A group of 2ᵏ cells eliminates k variables. In a 4-variable map: a pair gives a 3-literal term, a quad gives 2 literals, an octet gives 1.</p>
{xlab("kmap", vars=["A", "B", "C"], ones=[3, 5, 6, 7], title="Majority function on a 3-variable map", sub="Three overlapping pairs give AB + AC + BC.")}
{box("tip", "Don't-care conditions", "Sometimes an input combination can never happen, like the codes 10–15 in a circuit that only receives decimal digits 0–9. Mark those cells X and treat each one as a 1 if it helps you make a bigger group, or a 0 if it doesn't.")}
''', pill=("d", "3.4"))

UNIV = topic("universal", "Universal gates", f'''
<p>NAND by itself can build <b>any</b> logic function, and so can NOR. That's why they're called universal. Chips are often built almost entirely from NAND gates because a NAND is the cheapest CMOS gate.</p>
{table(["Build", "From NAND only"], [["NOT A", "A NAND A"], ["A AND B", "(A NAND B) NAND (A NAND B)"], ["A OR B", "(A NAND A) NAND (B NAND B)  — De Morgan: (A′B′)′ = A + B"]])}
{xlab("circuit", title="XOR from four NAND gates", inputs=["A", "B"], gates=[{"id": "n1", "t": "NAND", "in": ["A", "B"]}, {"id": "n2", "t": "NAND", "in": ["A", "n1"]}, {"id": "n3", "t": "NAND", "in": ["B", "n1"]}, {"id": "n4", "t": "NAND", "in": ["n2", "n3"]}], outputs={"A⊕B": "n4"}, note="The classic 4-NAND XOR. Click the truth table rows to set the inputs.")}
<p><b>Bubble pushing:</b> by De Morgan, a NAND gate is the same as an OR gate with inverted inputs, and a NOR is an AND with inverted inputs. A two-level AND-OR circuit can therefore be redrawn as NAND-NAND with no change in behaviour.</p>
''', pill=("d", "3.5"))

SUM = topic("summary-ce3", "Unit summary", mini(
 ("Gates", "AND · OR + NOT ′, plus NAND, NOR, XOR (inputs differ), XNOR (inputs equal). n inputs → 2ⁿ truth-table rows."),
 ("Algebra", "A + A′ = 1, A·A′ = 0, A + AB = A, A + A′B = A + B. De Morgan: (AB)′ = A′ + B′, (A + B)′ = A′B′."),
 ("SOP / POS", "SOP: OR together an AND term for every 1 row. POS: AND together an OR term for every 0 row. Σm(…) and ΠM(…) shorthand."),
 ("K-maps", "Gray-code order. Groups of 1, 2, 4, 8; as big as possible; may wrap and overlap. Keep the variables that don't change. NAND and NOR are universal."),
))

CH = [chapter("ch-gates", "Gates and Truth Tables", "Gates", [GATES]),
      chapter("ch-alg", "Boolean Algebra", "Algebra", [ALG, SOP]),
      chapter("ch-kmap", "Karnaugh Maps", "K-maps", [KMAP, UNIV, SUM])]

# verify a few identities by brute force
import itertools
for A, B, C in itertools.product([0, 1], repeat=3):
    assert (A and B or A and not B or (not A) and B) == (A or B)
    assert (not ((not A) or (B and C))) == (A and not B or A and not C)
    assert ((A and B) or (A and C) or (B and C)) == (A + B + C >= 2)
PQ = [
 q("What is the output of an XOR gate with inputs 1 and 1?", ["0", "1", "2", "undefined"], 0, "XOR is 1 only when the inputs differ.", "c"),
 q("Which gate outputs 0 only when all its inputs are 1?", ["NAND", "NOR", "AND", "XNOR"], 0, "NAND = NOT(AND).", "c"),
 q("A truth table for a 4-input function has how many rows?", ["16", "8", "4", "32"], 0, "2⁴ = 16.", "c"),
 q("In Boolean algebra, 1 + 1 equals…", ["1", "2", "0", "10"], 0, "+ is OR.", "c"),
 q("Simplify A + AB.", ["A", "B", "AB", "A + B"], 0, "Absorption law: if A is 1 the result is 1; if A is 0 both terms are 0.", "p"),
 q("Simplify A · A′.", ["0", "1", "A", "A′"], 0, "Complement law.", "p"),
 q("By De Morgan, (A + B)′ equals…", ["A′B′", "A′ + B′", "AB", "(AB)′"], 0, "Flip OR to AND and complement each variable.", "p"),
 q("By De Morgan, (ABC)′ equals…", ["A′ + B′ + C′", "A′B′C′", "A + B + C", "(A + B + C)′"], 0, "Flip AND to OR and complement each variable.", "p"),
 q("Simplify A′B + AB.", ["B", "A", "A + B", "1"], 0, "B(A′ + A) = B · 1 = B.", "p"),
 q("F has 1s only in rows 001 and 110 (inputs A B C). Its SOP form is…", ["A′B′C + ABC′", "A′B′C′ + ABC", "(A + B + C′)(A′ + B′ + C)", "A ⊕ B ⊕ C"], 0, "001 → A′B′C; 110 → ABC′.", "d"),
 q("Why are K-map columns ordered 00, 01, 11, 10?", ["So adjacent cells differ in exactly one variable", "It is binary counting order", "To put the 1s on the right", "It is alphabetical"], 0, "Gray code: neighbours differ by one bit, so they can be merged.", "c"),
 q("In a 4-variable K-map, a group of 4 cells produces a term with how many literals?", ["2", "1", "3", "4"], 0, "A group of 2ᵏ removes k variables: 4 − 2 = 2.", "c"),
 q("Which of these is a valid K-map group size?", ["8", "6", "3", "5"], 0, "Only powers of 2.", "c"),
 q("Which single gate type can build any logic function on its own?", ["NAND", "AND", "OR", "XOR"], 0, "NAND (and NOR) are universal.", "c"),
 q("How do you make a NOT gate from one NAND gate?", ["Connect both inputs to A", "Connect one input to 0", "Use the output twice", "It's impossible"], 0, "A NAND A = (AA)′ = A′.", "d"),
 q("Expression for: \"the alarm sounds (Y) if the door is open (D) and the system is armed (S), or if the panic button (P) is pressed.\"", ["Y = DS + P", "Y = D + S + P", "Y = D(S + P)", "Y = (D + S)P"], 0, "AND for 'and', OR for 'or'.", "d"),
]
CHAL = [
 q("Simplify (A + B)(A + B′).", ["A", "B", "A + B", "1"], 0, "Distributive (OR form): A + BB′ = A + 0 = A.", "p"),
 q("A 4-variable K-map has 1s in the four corner cells only (m0, m2, m8, m10). The simplified expression is…", ["B′D′", "A′C′", "BD", "A′B′C′D′"], 0, "The corners form one group of 4 that wraps both ways. A and C change across it; B = 0 and D = 0 stay fixed.", "d"),
 q("Simplify F(A, B, C) = Σm(0, 1, 2, 3, 7).", ["A′ + BC", "A′B′ + BC", "A′ + B", "AB + C"], 0, "Rows 0–3 are the whole A = 0 half: A′. m7 pairs with m3 to give BC.", "d"),
 q("F = Σm(1, 3, 5) + d(7) for inputs A B C. Simplest SOP?", ["C", "A′C + B′C", "A′B′C + A′BC + AB′C", "B′C"], 0, "Treat m7 as 1: m1, m3, m5, m7 is the whole C = 1 half → F = C.", "d"),
 q("How many 2-input NAND gates do you need to build A OR B?", ["3", "2", "1", "4"], 0, "Invert A (1 NAND), invert B (1 NAND), then NAND the results: (A′B′)′ = A + B.", "d"),
 q("Which expression equals A ⊕ B ⊕ C?", ["1 when an odd number of inputs are 1", "1 when all three inputs are 1", "1 when exactly two inputs are 1", "(A + B + C)′"], 0, "XOR chains compute parity, used in error-detecting codes.", "c"),
]
EXQ = [
 q("An AND gate has inputs 1 and 0. Output?", ["0", "1", "10", "undefined"], 0, "Both must be 1.", "c"),
 q("A NOR gate outputs 1 when…", ["all inputs are 0", "any input is 1", "inputs differ", "all inputs are 1"], 0, "NOR = NOT(OR).", "c"),
 q("A′ + A equals…", ["1", "0", "A", "A′"], 0, "Complement law.", "p"),
 q("(A′)′ equals…", ["A", "A′", "0", "1"], 0, "Double negation.", "p"),
 q("A(A + B) simplifies to…", ["A", "AB", "A + B", "B"], 0, "Absorption.", "p"),
 q("(A′B)′ equals…", ["A + B′", "A′ + B", "AB′", "A′B′"], 0, "De Morgan: (A′)′ + B′ = A + B′.", "p"),
 q("A 3-input function has how many possible minterms?", ["8", "3", "6", "9"], 0, "2³.", "c"),
 q("The minterm for row A=1, B=0, C=1 is…", ["AB′C", "A′BC′", "A + B′ + C", "ABC"], 0, "Use the variable for 1, its complement for 0.", "d"),
 q("XNOR outputs 1 when…", ["the inputs are equal", "the inputs differ", "both are 1 only", "both are 0 only"], 0, "XNOR is an equality detector.", "c"),
 q("In a K-map, groups may…", ["overlap and wrap around the edges", "be any shape", "contain 0s", "have 3 cells"], 0, "Rectangles of 1, 2, 4, 8 … that may overlap and wrap.", "c"),
 q("Simplify AB + AB′.", ["A", "B", "1", "AB"], 0, "A(B + B′) = A.", "p"),
 q("Which pair are both universal gates?", ["NAND and NOR", "AND and OR", "XOR and XNOR", "AND and NOT"], 0, "Either one alone can build anything.", "c"),
]
FRQS = [
 {"q": "A security light L turns on when it's dark (D = 1) and motion is sensed (M = 1), or when the manual switch S is on — but never when the maintenance lock K is on.", "parts": [
  {"p": "(a) Write a Boolean expression for L.", "rubric": [["(DM + S)", 1], ["ANDed with K′", 1]], "answer": "L = (DM + S)K′ = DMK′ + SK′."},
  {"p": "(b) How many rows are in the truth table, and how many rows have L = 1?", "rubric": [["16 rows", 1], ["5 rows: K = 0 and (S = 1 or D = M = 1): S=1 gives 4 rows, plus D=M=1,S=0 gives 1", 1]], "answer": "2⁴ = 16 rows. With K = 0: S = 1 gives 4 rows (any D, M), S = 0 needs D = M = 1 (1 row). Total 5."},
  {"p": "(c) Draw or describe a circuit using AND, OR and NOT gates.", "rubric": [["AND(D, M)", 1], ["OR with S, then AND with NOT K", 1]], "answer": "AND gate on D and M → OR gate with S → AND gate with the output of a NOT gate on K."}]},
 {"q": "Simplify F(A, B, C, D) = Σm(0, 1, 2, 3, 8, 9, 10, 11, 14, 15).", "parts": [
  {"p": "(a) Fill in a K-map and identify the groups.", "rubric": [["Octet: m0–3 and m8–11 (B = 0)", 1], ["Quad m10, m11, m14, m15 (A = 1, C = 1)", 1]], "answer": "B = 0 is 8 cells (rows 00 and 10). m10, m11, m14, m15 form a quad with A = 1, C = 1."},
  {"p": "(b) Write the simplified SOP.", "rubric": [["F = B′ + AC", 2]], "answer": "F = B′ + AC."},
  {"p": "(c) Rewrite your answer using only NAND gates (describe the gates).", "rubric": [["B′ = B NAND B", 1], ["F = (B · (AC)′)′ = B NAND (A NAND C)", 1]], "answer": "By De Morgan, B′ + AC = (B · (AC)′)′. So F = B NAND (A NAND C): two NAND gates."}]},
]
build("comp-eng", "ce-3", L, 3, "Boolean Logic and Gates", 'Boolean <span class="hl">logic</span>', "Gates, truth tables, Boolean algebra, De Morgan's laws and Karnaugh maps: how to design the smallest circuit for any rule.", "Intro to computer engineering unit 3: logic gates, truth tables, Boolean algebra, De Morgan's laws, sum of products and Karnaugh maps with interactive labs.", CH, PQ, CHAL, EXQ, FRQS, OUT, TAGS)
