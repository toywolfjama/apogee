from lab_common import *
L = "Computer Engineering"
TAGS = {"c": "Concept", "p": "Calculation", "d": "Design", "r": "Reading circuits"}
OUT = "../../courses/comp-eng/ce-2.html"

BASES = topic("bases", "Binary, decimal and hexadecimal", f'''
<p>A computer stores everything as <b>bits</b>: 0 or 1, off or on, low voltage or high voltage. Group bits together and you can count. Every number system works the same way: each digit is worth the <b>base</b> times the digit to its right.</p>
{table(["System", "Base", "Digits", "Place values (right to left)", "Written"], [
 ["Decimal", "10", "0–9", "1, 10, 100, 1000", "45"],
 ["Binary", "2", "0, 1", "1, 2, 4, 8, 16, 32, 64, 128", "101101₂ or 0b101101"],
 ["Hexadecimal", "16", "0–9, A–F (A = 10 … F = 15)", "1, 16, 256, 4096", "2D₁₆ or 0x2D"],
 ["Octal", "8", "0–7", "1, 8, 64, 512", "55₈ or 0o55"],
])}
{xlab("bits", n=8, value=45, signed=False, title="8-bit binary number", sub="Click bits to flip them. Each bit is worth twice the one to its right.")}
<h3>Binary → decimal: add the place values of the 1s</h3>
{worked("Convert 1011 0110₂ to decimal.", "Place values of the 1 bits: 128 + 32 + 16 + 4 + 2 = 182.")}
<h3>Decimal → binary: divide by 2, read the remainders upward</h3>
{steps("Convert 45 to binary", [
 ("a|45 ÷ 2 = 22 r|e  b|1|g", "Remainder is the lowest bit (the 1s place)."),
 ("c|22 ÷ 2 = 11 r|e  d|0|g", "Keep dividing the quotient."),
 ("e|11 ÷ 2 = 5 r|e  f|1|g", ""),
 ("g|5 ÷ 2 = 2 r|e  h|1|g", ""),
 ("i|2 ÷ 2 = 1 r|e  j|0|g", ""),
 ("k|1 ÷ 2 = 0 r|e  l|1|g", "Quotient hit 0, so stop."),
 ("m|101101₂|v", "Read the remainders from the bottom up: 101101. Check: 32 + 8 + 4 + 1 = 45 ✓"),
])}
<p>Or subtract the biggest power of 2 that fits: 45 − 32 = 13, 13 − 8 = 5, 5 − 4 = 1, 1 − 1 = 0. The powers used (32, 8, 4, 1) are the 1 bits.</p>
<h3>Hex is shorthand for binary</h3>
<p>One hex digit is exactly 4 bits (a <b>nibble</b>), so you convert by grouping bits in fours from the right. No arithmetic needed.</p>
{table(["Hex", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"], [["Binary", "0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"]])}
{worked("Convert 1101 0111 1010₂ to hex, and 0x3F to binary and decimal.", "Groups 1101 | 0111 | 1010 → D 7 A, so 0xD7A. 0x3F = 0011 1111₂ = 3 × 16 + 15 = 63.")}
{box("tip", "Where you'll see hex", "Memory addresses (0x7FFE…), colors (#FF8800 is red FF, green 88, blue 00), MAC addresses, and error codes. Programmers use it because it's compact but still maps directly onto bits.")}
''', pill=("p", "2.1"))

SIZES = topic("sizes", "How many bits do you need?", f'''
<p><b>n bits can represent 2ⁿ different values</b>. To give N different things their own code you need ⌈log₂ N⌉ bits (round up).</p>
{table(["Bits", "Values", "Unsigned range", "Example"], [["1", "2", "0–1", "a flag"], ["4", "16", "0–15", "a hex digit"], ["8", "256", "0–255", "a byte, one color channel"], ["16", "65,536", "0–65,535", "a port number"], ["32", "≈ 4.3 billion", "0 – 4,294,967,295", "an IPv4 address"], ["64", "≈ 1.8 × 10¹⁹", "", "a memory address on a 64-bit CPU"]])}
{worked("How many bits to give each of 200 students a unique ID?", "2⁷ = 128 is too few, 2⁸ = 256 is enough, so 8 bits.")}
{mini(("Units", "8 bits = 1 byte. Storage makers use powers of 10 (1 KB = 1000 bytes, 1 GB = 10⁹ bytes). Operating systems often use powers of 2: 1 KiB = 1024 bytes, 1 MiB = 1024² bytes, 1 GiB = 1024³ bytes. That's why a \"500 GB\" drive shows up as about 465 GiB."),
      ("Bits vs bytes", "Network speeds are in bits per second (Mb/s, lowercase b). File sizes are in bytes (MB, capital B). A 100 Mb/s connection moves at most 12.5 MB/s."))}
''', pill=("p", "2.2"))

ARITH = topic("arith", "Binary addition and overflow", f'''
<p>Binary addition works exactly like the column addition you learned in school, except you carry at 2 instead of 10: 0+0 = 0, 0+1 = 1, 1+1 = 10 (write 0 carry 1), 1+1+1 = 11 (write 1 carry 1).</p>
{steps("Add 0110 1011 + 0011 0110 (107 + 54)", [
 ("a|  01101011|e  b|+ 00110110|e", "Line up the bits and start from the right."),
 ("c|carries 11111100|v  a|  01101011|e  b|+ 00110110|e", "1+0 = 1. 1+1 = 0 carry 1. 0+1+1 = 0 carry 1. … Each column adds two bits plus the carry in."),
 ("d|= 10100001|g", "Result 1010 0001₂ = 161. Check: 107 + 54 = 161 ✓"),
])}
<p>An 8-bit register can only hold 0–255. If an unsigned sum needs a 9th bit, that bit (the <b>carry out</b>) is lost and the answer wraps around. This is <b>overflow</b>.</p>
{worked("Add 200 + 100 in an 8-bit unsigned register.", "300 = 1 0010 1100₂ needs 9 bits. The register keeps the low 8 bits: 0010 1100₂ = 44. The carry flag is set to warn that the true answer was 300 = 256 + 44.")}
{box("trap", "Real overflow bugs", "In 2014 the Gangnam Style video passed 2,147,483,647 views, the largest signed 32-bit number, and YouTube had to switch its counter to 64 bits. In 1996 the Ariane 5 rocket exploded after a 64-bit value was squeezed into a 16-bit integer.")}
''', pill=("p", "2.3"))

SIGNED = topic("signed", "Negative numbers: two's complement", f'''
<p>Almost every computer stores negative integers in <b>two's complement</b>. The idea: the leftmost bit is worth a <i>negative</i> amount. In 8 bits, the place values are −128, 64, 32, 16, 8, 4, 2, 1.</p>
{xlab("bits", n=8, value=251, title="Two's complement lab", sub="The top bit is worth −128. Try Negate, and try +1 on 0111 1111.")}
{table(["Bits", "Unsigned", "Two's complement"], [["0000 0000", "0", "0"], ["0000 0001", "1", "1"], ["0111 1111", "127", "127 (largest)"], ["1000 0000", "128", "−128 (smallest)"], ["1111 1111", "255", "−1"], ["1111 1011", "251", "−5"]])}
<p>The range of n-bit two's complement is <b>−2ⁿ⁻¹ to 2ⁿ⁻¹ − 1</b>. For 8 bits: −128 to 127.</p>
<h3>To negate a number: invert every bit, then add 1</h3>
{steps("Find −20 in 8-bit two's complement", [
 ("a|+20 = 0001 0100|e", "Start with the positive version."),
 ("b|invert → 1110 1011|v", "Flip every bit (this is the one's complement)."),
 ("c|+1 → 1110 1100|g", "Add 1. Check with place values: −128 + 64 + 32 + 8 + 4 = −20 ✓"),
])}
{mini(("Why it's brilliant", "The same adder circuit works for signed and unsigned numbers. Subtraction is just adding the negation: A − B = A + (inverted B) + 1. There's only one zero (sign-magnitude has +0 and −0)."),
      ("Signed overflow", "Overflow happens when two numbers with the same sign add to a result with the other sign: 100 + 50 in 8 bits gives 1001 0110 = −106. Adding a positive and a negative can never overflow."),
      ("Sign extension", "To widen a two's complement number, copy the sign bit into the new bits: −5 = 1111 1011 (8-bit) = 1111 1111 1111 1011 (16-bit)."),
      ("Other schemes", "Sign-magnitude: top bit is just a minus sign (two zeros, awkward adders). One's complement: negate by inverting only (also two zeros). Both are mostly history."))}
''', pill=("c", "2.4"))

BITOPS = topic("bitops", "Bitwise operations and masks", f'''
<p>Processors can apply logic to every bit of a word at once. These operations show up constantly in low-level code, networking and graphics.</p>
{table(["Operation", "Example (8-bit)", "Use"], [
 ["AND &", "1011 0110 & 0000 1111 = 0000 0110", "Keep some bits, clear the rest (a mask)"],
 ["OR |", "1011 0110 | 0000 0001 = 1011 0111", "Force some bits to 1"],
 ["XOR ^", "1011 0110 ^ 1111 1111 = 0100 1001", "Flip chosen bits; x ^ x = 0"],
 ["NOT ~", "~1011 0110 = 0100 1001", "Flip every bit"],
 ["Shift left ≪ k", "0000 0101 ≪ 2 = 0001 0100", "Multiply by 2ᵏ"],
 ["Shift right ≫ k", "0001 0100 ≫ 2 = 0000 0101", "Divide by 2ᵏ (rounding down)"],
])}
{worked("A status byte is 1010 0110. Is bit 2 (counting from 0 at the right) set? Then turn bit 0 on.", "Test: 1010 0110 & 0000 0100 = 0000 0100 ≠ 0, so bit 2 is set. Set bit 0: 1010 0110 | 0000 0001 = 1010 0111.")}
{code('''
x = 0b10110110
low_nibble = x & 0x0F      # 0b0110  = 6
high_nibble = (x >> 4) & 0x0F  # 0b1011 = 11
x = x | (1 << 0)           # set bit 0
is_odd = (x & 1) == 1      # check the lowest bit
''')}
''', pill=("p", "2.5"))

TEXT = topic("text", "Text: ASCII and Unicode", f'''
<p>Characters are just numbers that everyone agrees on. <b>ASCII</b> (1963) uses 7 bits for 128 characters: 'A' = 65 (0x41), 'a' = 97 (0x61), '0' = 48 (0x30), space = 32.</p>
{box("tip", "Handy ASCII patterns", "Upper and lower case differ by 32, which is one bit (0x20): 'A' = 0100 0001, 'a' = 0110 0001. The digit characters '0'–'9' are 48–57, so the character c has value c − 48.")}
<p><b>Unicode</b> gives every character in every writing system (and emoji) a number called a <b>code point</b>, written U+XXXX: 'é' = U+00E9, '€' = U+20AC, '😀' = U+1F600. There are over 1.1 million possible code points.</p>
<p><b>UTF-8</b> stores code points in 1 to 4 bytes. Plain ASCII characters keep their 1-byte codes, so old ASCII files are already valid UTF-8, which is a big reason UTF-8 now runs almost the entire web.</p>
{table(["Code point range", "Bytes in UTF-8", "Bit pattern"], [["U+0000 – U+007F", "1", "0xxxxxxx"], ["U+0080 – U+07FF", "2", "110xxxxx 10xxxxxx"], ["U+0800 – U+FFFF", "3", "1110xxxx 10xxxxxx 10xxxxxx"], ["U+10000 – U+10FFFF", "4", "11110xxx 10xxxxxx 10xxxxxx 10xxxxxx"]])}
''', pill=("c", "2.6"))

FLOAT = topic("float", "Floating point: real numbers in 32 bits", f'''
<p>To store numbers like 6.5, 0.001 or 3 × 10⁸, computers use scientific notation in binary: <b>(−1)<sup>sign</sup> × 1.fraction × 2<sup>exponent</sup></b>. The IEEE 754 single-precision format packs this into 32 bits:</p>
{xlab("float32", value=6.5)}
{steps("Encode 6.5 as a float", [
 ("a|6.5 = 110.1₂|e", "6 = 110, and .5 = .1 in binary (one half)."),
 ("b|= 1.101₂ × 2²|e", "Normalize: move the point so there's one 1 before it."),
 ("c|sign 0|s  d|exp 2 + 127 = 129 = 10000001|v  f|fraction 101000…|g", "Store the exponent with a bias of 127 so it's never negative. The leading 1 isn't stored (it's free)."),
 ("g|0 10000001 10100000000000000000000|n", "That's 0x40D00000."),
])}
{mini(("Limited precision", "A float has 24 significant bits, about 7 decimal digits. A double (64 bits: 1 + 11 + 52) has about 16."),
      ("0.1 isn't exact", "0.1 in binary is 0.000110011001100… forever, like 1/3 in decimal. So 0.1 + 0.2 == 0.3 is false in most languages. Never compare floats with ==; check if they're within a small tolerance."),
      ("Special values", "Exponent all 0s: zero and tiny 'subnormal' numbers. Exponent all 1s: ±infinity (fraction 0) or NaN, 'not a number' (fraction ≠ 0), from things like 0/0."),
      ("Range", "Largest float ≈ 3.4 × 10³⁸. Smallest normal ≈ 1.18 × 10⁻³⁸. Money should never be stored in floats; use integers counting cents."))}
''', pill=("c", "2.7"), det=("Decoding a float by hand", "<p>Take 0xC1480000 = 1100 0001 0100 1000 0000 … Sign = 1 (negative). Exponent = 1000 0010₂ = 130, so the power is 130 − 127 = 3. Fraction bits 1001 000… → significand 1.1001₂ = 1 + 1/2 + 1/16 = 1.5625. Value = −1.5625 × 2³ = −12.5.</p>"))

SUM = topic("summary-ce2", "Unit summary", mini(
 ("Bases", "Binary place values 1, 2, 4, 8, … Hex digit = 4 bits. Decimal → binary: divide by 2, read remainders upward."),
 ("Capacity", "n bits → 2ⁿ values. Need ⌈log₂ N⌉ bits for N things. 1 KiB = 1024 bytes."),
 ("Signed", "Two's complement: top bit worth −2ⁿ⁻¹. Negate = invert + 1. Range −2ⁿ⁻¹ … 2ⁿ⁻¹ − 1. Overflow when same-sign inputs give an opposite-sign result."),
 ("Data", "Masks with AND/OR/XOR; shifts multiply/divide by 2. ASCII 'A' = 65. UTF-8 uses 1–4 bytes. Float = sign, biased exponent, fraction; 0.1 isn't exact."),
))

CH = [chapter("ch-bases", "Number Systems", "Bases", [BASES, SIZES]),
      chapter("ch-arith", "Binary Arithmetic", "Arithmetic", [ARITH, SIGNED, BITOPS]),
      chapter("ch-data", "Text and Real Numbers", "Text & floats", [TEXT, FLOAT, SUM])]

assert int("10110110", 2) == 182 and bin(45) == "0b101101" and 0x3F == 63 and 107 + 54 == 161 and int("10100001", 2) == 161
assert (300 & 255) == 44 and ((-20) & 255) == 0b11101100 and ((100 + 50) & 255) - 256 == -106
import struct
assert struct.pack(">f", 6.5).hex() == "40d00000" and struct.unpack(">f", bytes.fromhex("c1480000"))[0] == -12.5
PQ = [
 q("Convert 1100 1010₂ to decimal.", ["202", "212", "198", "170"], 0, "128 + 64 + 8 + 2 = 202.", "p"),
 q("Convert 77 to binary.", ["100 1101", "100 1011", "101 1001", "111 0111"], 0, "64 + 8 + 4 + 1 = 77 → 1001101.", "p"),
 q("Convert 0xB4 to decimal.", ["180", "164", "184", "1104"], 0, "B = 11: 11 × 16 + 4 = 180.", "p"),
 q("Convert 1110 0101 1011₂ to hex.", ["0xE5B", "0xE5C", "0xD5B", "0xEB5"], 0, "1110 = E, 0101 = 5, 1011 = B.", "p"),
 q("How many different values can 10 bits represent?", ["1024", "100", "1000", "512"], 0, "2¹⁰ = 1024.", "p"),
 q("How many bits are needed to give each of 1000 sensors a unique address?", ["10", "9", "8", "1000"], 0, "2⁹ = 512 < 1000 ≤ 1024 = 2¹⁰.", "p"),
 q("What is the range of an 8-bit two's complement number?", ["−128 to 127", "−127 to 127", "0 to 255", "−256 to 255"], 0, "−2⁷ to 2⁷ − 1.", "c"),
 q("What decimal value is 1111 1110 in 8-bit two's complement?", ["−2", "254", "−126", "−1"], 0, "−128 + 64 + 32 + 16 + 8 + 4 + 2 = −2. Or: invert → 0000 0001, +1 → 0000 0010 = 2, so it's −2.", "p"),
 q("Write −7 in 8-bit two's complement.", ["1111 1001", "1000 0111", "1111 1000", "0000 0111"], 0, "7 = 0000 0111 → invert 1111 1000 → +1 → 1111 1001.", "p"),
 q("In 8-bit two's complement, 0111 1111 + 0000 0001 gives…", ["1000 0000 = −128 (signed overflow)", "1000 0000 = 128", "0000 0000", "an error that stops the CPU"], 0, "127 + 1 wraps to −128. Two positives gave a negative: overflow.", "c"),
 q("x = 0110 1101. What is x & 0000 1111?", ["0000 1101", "0110 1111", "0110 0000", "0000 0010"], 0, "AND with a mask keeps only the low 4 bits.", "p"),
 q("Shifting an unsigned binary number left by 3 places…", ["multiplies it by 8", "divides it by 8", "adds 3", "multiplies by 3"], 0, "Each shift doubles: 2³ = 8.", "c"),
 q("The ASCII code for 'C' is 67. What is the code for 'c'?", ["99", "68", "35", "97"], 0, "Lowercase is uppercase + 32.", "p"),
 q("Why does 0.1 + 0.2 == 0.3 evaluate to false in most languages?", ["0.1 and 0.2 can't be represented exactly in binary floating point", "the computer adds in decimal", "== doesn't work on numbers", "floats only hold integers"], 0, "Like 1/3 in decimal, 0.1 is an infinitely repeating binary fraction, so it's rounded.", "c"),
 q("In IEEE 754 single precision, the exponent is stored with a bias of…", ["127", "128", "255", "0"], 0, "Stored exponent = actual exponent + 127.", "c"),
 q("A 1 Gb/s (gigabit) link transfers a 500 MB file in at least about…", ["4 seconds", "0.5 seconds", "500 seconds", "40 seconds"], 0, "500 MB = 4000 Mb; 4000 Mb ÷ 1000 Mb/s = 4 s.", "p"),
]
CHAL = [
 q("Using 8-bit two's complement, compute −100 + (−50). What bit pattern is stored and what does it mean?", ["0110 1010 = 106: signed overflow", "1001 0110 = −150", "1111 0110 = −10", "1000 0000 = −128"], 0, "True sum −150 is out of range. −100 = 1001 1100, −50 = 1100 1110; sum = 1 0110 1010 → keep 0110 1010 = 106. Two negatives gave a positive: overflow.", "p"),
 q("What float is stored in the bits 0 10000011 01000000000000000000000?", ["20.0", "10.0", "5.0", "−20.0"], 0, "Exponent 131 − 127 = 4. Significand 1.01₂ = 1.25. 1.25 × 16 = 20.", "p"),
 q("The UTF-8 encoding of '€' (U+20AC) uses how many bytes?", ["3", "2", "1", "4"], 0, "0x20AC is in U+0800–U+FFFF, which takes 3 bytes.", "c"),
 q("x ^ y ^ y equals…", ["x", "y", "0", "x ^ y"], 0, "y ^ y = 0 and x ^ 0 = x. This is how XOR swaps and simple ciphers work.", "c"),
 q("A 12-bit two's complement value 1111 1111 1010 is sign-extended to 16 bits. Result in hex?", ["0xFFFA", "0x0FFA", "0xFFA0", "0x8FFA"], 0, "Copy the sign bit (1) into the 4 new bits: 1111 1111 1111 1010 = 0xFFFA (= −6).", "p"),
 q("A 32-bit signed integer counter adds 1 per millisecond starting at 0. Roughly when does it overflow?", ["After about 24.9 days", "After about 49.7 days", "After about 1 year", "After about 68 years"], 0, "2³¹ − 1 ≈ 2.147 × 10⁹ ms ≈ 2.147 × 10⁶ s ≈ 24.9 days. (Unsigned would last 49.7 days, a famous Windows 95 bug.)", "p"),
]
EXQ = [
 q("1001 0001₂ in decimal is…", ["145", "137", "129", "153"], 0, "128 + 16 + 1.", "p"),
 q("200 in hex is…", ["0xC8", "0xC0", "0xD8", "0x128"], 0, "200 = 12 × 16 + 8.", "p"),
 q("0x7F in binary is…", ["0111 1111", "1111 0111", "0111 0000", "1000 0000"], 0, "7 = 0111, F = 1111.", "p"),
 q("How many bits does one hex digit stand for?", ["4", "8", "2", "16"], 0, "16 = 2⁴.", "c"),
 q("The largest unsigned 16-bit number is…", ["65,535", "65,536", "32,767", "32,768"], 0, "2¹⁶ − 1.", "p"),
 q("−1 in 8-bit two's complement is…", ["1111 1111", "1000 0001", "1000 0000", "0000 0001"], 0, "Invert 0000 0001 → 1111 1110, +1 → 1111 1111.", "p"),
 q("Which addition overflows in 8-bit two's complement?", ["90 + 50", "−90 + 50", "90 + (−50)", "−50 + (−50)"], 0, "140 > 127. Mixed signs can't overflow; −100 fits.", "c"),
 q("How do you subtract B from A with an adder circuit?", ["Add A to the two's complement of B", "Add A to B and invert", "Shift B right", "AND A with B"], 0, "A − B = A + (~B + 1).", "c"),
 q("To clear (set to 0) the low 4 bits of an 8-bit value x, use…", ["x & 0xF0", "x | 0x0F", "x ^ 0xFF", "x & 0x0F"], 0, "AND with 1111 0000 keeps the high nibble and zeroes the rest.", "p"),
 q("0001 1000 ≫ 3 equals…", ["0000 0011", "1100 0000", "0000 0110", "0001 1011"], 0, "24 ÷ 8 = 3.", "p"),
 q("A double-precision float has about how many significant decimal digits?", ["16", "7", "32", "64"], 0, "52 fraction bits + the hidden 1 = 53 bits ≈ 16 digits.", "c"),
 q("Why is UTF-8 backward compatible with ASCII?", ["Code points 0–127 are stored as the same single bytes", "It only stores English", "It uses 7-bit bytes", "It stores characters as floats"], 0, "Every ASCII file is already valid UTF-8.", "c"),
]
FRQS = [
 {"q": "Number conversions and arithmetic. Show your work.", "parts": [
  {"p": "(a) Convert 157 to 8-bit binary and to hex.", "rubric": [["1001 1101", 1], ["0x9D", 1]], "answer": "157 = 128 + 16 + 8 + 4 + 1 = 1001 1101₂ = 0x9D."},
  {"p": "(b) Write −45 in 8-bit two's complement.", "rubric": [["45 = 0010 1101", 1], ["Invert + 1 → 1101 0011", 1]], "answer": "0010 1101 → 1101 0010 → 1101 0011."},
  {"p": "(c) Add 0101 1010 + 0011 0111 as 8-bit signed numbers. Give the result and state whether overflow occurred.", "rubric": [["Sum bits 1001 0001", 1], ["Identifies signed overflow (90 + 55 = 145 > 127, result reads −111)", 1]], "answer": "90 + 55 = 145 → 1001 0001, which reads as −111. Two positives gave a negative: overflow."}]},
 {"q": "Floating point.", "parts": [
  {"p": "(a) Encode −0.75 in IEEE 754 single precision (give sign, exponent bits, fraction bits).", "rubric": [["−0.75 = −1.1₂ × 2⁻¹", 1], ["Sign 1, exponent 126 = 0111 1110", 1], ["Fraction 1000…0 (0xBF400000)", 1]], "answer": "0.75 = 0.11₂ = 1.1₂ × 2⁻¹. Sign 1, exponent −1 + 127 = 126 = 01111110, fraction 100…0. Bits 1 01111110 10000000000000000000000 = 0xBF400000."},
  {"p": "(b) Explain why a bank should not store account balances as floats, and suggest an alternative.", "rubric": [["Most decimal fractions (0.10) are not exact in binary, so rounding errors accumulate", 1], ["Store whole cents as integers (or use a decimal type)", 1]], "answer": "Values like $0.10 can't be stored exactly, so repeated sums drift. Store integer cents or use a decimal number type."}]},
]
build("comp-eng", "ce-2", L, 2, "Number Systems and Data", 'Numbers in <span class="hl">binary</span>', "Binary and hex, two's complement, overflow, bit masks, text encoding and floating point: how a computer turns everything into 0s and 1s.", "Intro to computer engineering unit 2: binary, hexadecimal, two's complement, overflow, bitwise operations, ASCII, UTF-8 and IEEE 754 floating point.", CH, PQ, CHAL, EXQ, FRQS, OUT, TAGS)
