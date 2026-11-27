from ws_common import M, build_ws
from cs_common import code, jcheck, verify

TRACES = [
 ("int x = 7;\nint y = x / 2;\nSystem.out.println(y + x % 2);", "4", "7 / 2 is integer division → 3; 7 % 2 = 1; 3 + 1 = 4."),
 ('String s = "margin";\nSystem.out.println(s.substring(1, 4) + s.length());', "arg6", "substring(1, 4) takes indexes 1, 2, 3 → \"arg\"; then string + int concatenates 6."),
 ("int sum = 0;\nfor (int i = 1; i <= 5; i += 2) {\n    sum += i;\n}\nSystem.out.println(sum);", "9", "i = 1, 3, 5 → 1 + 3 + 5 = 9."),
 ("int[] a = {4, 1, 3};\na[1] = a[0] + a[2];\nSystem.out.println(a[1] * 2);", "14", "a[1] becomes 4 + 3 = 7; 7 × 2 = 14."),
 ("double d = 7 / 2;\nSystem.out.println(d);", "3.0", "7 / 2 is computed with ints first (3), then widened to 3.0."),
 ("int n = 0;\nwhile (n * n < 30) {\n    n++;\n}\nSystem.out.println(n);", "6", "5 × 5 = 25 < 30 keeps going; 6 × 6 = 36 stops."),
 ('String t = "";\nfor (int i = 3; i > 0; i--) {\n    t += i;\n}\nSystem.out.println(t);', "321", "Appends 3, then 2, then 1."),
 ("boolean b = (5 > 3) && !(2 == 2);\nSystem.out.println(b);", "false", "true && !true = true && false = false."),
]
for src, out, _ in TRACES: jcheck(src, out, label="trace")
COUNTS = [
 ("for (int i = 0; i < 10; i += 3) {\n    count++;\n}", 4, "i = 0, 3, 6, 9."),
 ("for (int i = 10; i > 0; i /= 2) {\n    count++;\n}", 4, "i = 10, 5, 2, 1, then 0 stops."),
 ("for (int i = 0; i < 3; i++) {\n    for (int j = 0; j < i; j++) {\n        count++;\n    }\n}", 3, "Inner loop runs 0 + 1 + 2 = 3 times."),
 ("for (int i = 1; i <= 4; i++) {\n    for (int j = 1; j <= 4; j++) {\n        count++;\n    }\n}", 16, "4 × 4."),
 ("int k = 1;\nwhile (k < 100) {\n    k *= 3;\n    count++;\n}", 5, "k = 3, 9, 27, 81, 243: five multiplications."),
]
for src, n, _ in COUNTS: jcheck("int count = 0;\n" + src + "\nSystem.out.println(count);", str(n), label="count")
SUM = ["int[] nums = {3, 8, 2};", "int total = 0;", "for (int n : nums) {", "    total += n;", "}", "System.out.println(total);"]
jcheck("\n".join(SUM), "13", label="parsons")
MAXL = ["public static int max(int[] arr) {", "    int max = arr[0];", "    for (int i = 1; i < arr.length; i++) {", "        if (arr[i] > max) {", "            max = arr[i];", "        }", "    }", "    return max;", "}"]
jcheck("System.out.println(max(new int[]{4, 9, 2}));", "9", pre="\n".join(MAXL), label="parsons")
REV = ['String word = "java";', 'String rev = "";', "for (int i = word.length() - 1; i >= 0; i--) {", "    rev += word.charAt(i);", "}", "System.out.println(rev);"]
jcheck("\n".join(REV), "avaj", label="parsons")
CNT = ["public class Counter {", "    private int count;", "    public Counter() {", "        count = 0;", "    }", "    public void click() {", "        count++;", "    }", "}"]
jcheck("Counter c = new Counter(); c.click(); System.out.println(\"ok\");", "ok", cls="\n".join(CNT).replace("public class", "class"), label="parsons")
assert verify({})

G1 = [
 M("csa-trace", "Be the computer", "Read each snippet and type exactly what it prints. Every answer was checked by running real Java.",
   {"type": "calc", "pass": 0.6, "qs": [{"q": code(s), "a": o, "cs": True, "ph": "output", "x": x} for s, o, x in TRACES]},
   win="Integer division, string concatenation and loop bounds cause most AP CSA tracing mistakes.",
   hints=["int / int always gives an int: the decimal part is thrown away.", "substring(a, b) includes index a but stops before index b."]),
 M("csa-count", "Count the iterations", "How many times does count++ run? Type a number.",
   {"type": "calc", "pass": 0.6, "qs": [{"q": code("int count = 0;\n" + s), "a": n, "abs": 0, "x": x} for s, n, x in COUNTS]},
   win="For nested loops, count the inner loop for each value of the outer variable, then add.",
   hints=["Write down every value the loop variable takes, then count them."]),
]
G2 = [
 M("par-sum", "Assemble: add up an array", "The lines of a working program are scrambled. Put them back in order.",
   {"type": "parsons", "lines": SUM, "task": "Rebuild the program so it prints the sum of the array (13)."},
   win="Declare before you use, open the loop, update inside the braces, print after the loop.", hints=["The variables must be declared before the loop uses them.", "The print goes after the loop closes, or it would print three times."]),
 M("par-rev", "Assemble: reverse a string", "Put the lines in order so the program prints the word backwards.",
   {"type": "parsons", "lines": REV, "task": "Rebuild the program so it prints \"avaj\"."},
   win="Loop from the last index (length − 1) down to 0, adding one character at a time.", hints=["The last valid index is word.length() − 1."]),
 M("par-max", "Assemble: find the maximum", "Rebuild the classic find-the-max method.",
   {"type": "parsons", "lines": MAXL, "task": "Rebuild max(int[] arr), which returns the largest element."},
   win="Start with the first element as the best so far, then let each later element challenge it.", hints=["The return statement comes after the loop has checked every element.", "The if goes inside the for loop."]),
 M("par-class", "Assemble: write a class", "Put the class together in the standard order: field, constructor, method.",
   {"type": "parsons", "lines": CNT, "task": "Rebuild the Counter class."},
   win="Instance variables are private; the constructor has the class's name and no return type; methods change the object's state.", hints=["The constructor's name matches the class and has no return type."]),
]
G3 = [
 M("csa-sprint", "Exam-style sprint", "Eight AP CSA multiple-choice questions in five minutes.",
   {"type": "sprint", "time": 300, "pass": 0.75, "qs": [
    {"q": 'Which correctly compares the contents of two Strings a and b?', "o": ["a == b", "a.equals(b)", "a = b", "a.compareTo(b) == true"], "a": 1, "x": "== compares references; equals compares characters."},
    {"q": "What is 17 % 5?", "o": ["3", "2", "3.4", "12"], "a": 1, "x": "17 = 3 × 5 + 2."},
    {"q": "ArrayList list = [5, 7, 9]. After list.remove(0), what is list.get(0)?", "o": ["5", "7", "9", "an error"], "a": 1, "x": "Elements shift left after a removal."},
    {"q": "Which loop header visits every index of int[] arr?", "o": ["for (int i = 0; i <= arr.length; i++)", "for (int i = 1; i < arr.length; i++)", "for (int i = 0; i < arr.length; i++)", "for (int i = arr.length; i > 0; i--)"], "a": 2, "x": "Indexes run from 0 to length − 1."},
    {"q": "What does (int) 9.99 evaluate to?", "o": ["10", "9", "9.0", "a compile error"], "a": 1, "x": "Casting to int truncates toward zero."},
    {"q": "Which statement about constructors is true?", "o": ["They must return void", "They have the same name as the class", "A class can have only one", "They are called with the dot operator"], "a": 1, "x": "No return type, same name, overloading allowed."},
    {"q": "Math.random() returns a value in which range?", "o": ["[0, 1]", "[0, 1)", "(0, 1)", "[1, 10]"], "a": 1, "x": "0 inclusive, 1 exclusive."},
    {"q": "A method declared private in class A can be called from…", "o": ["any class", "subclasses only", "inside class A only", "classes in the same folder only"], "a": 2, "x": "private = visible only within its own class."}]},
   win="Fast, careful reading is the skill: most wrong answers come from == vs equals, off-by-one loops and integer division."),
]
build_ws("ap-csa", "../../courses/ap-csa/workshop.html", "AP Computer Science A", 'The <span class="hl">Java</span> workshop',
 "Trace code like a computer, count loop iterations, assemble scrambled programs and race through exam questions.",
 [("Trace", "Trace", G1), ("Assemble", "Assemble", G2), ("Exam Sprint", "Sprint", G3)], (), "Margin · AP CSA workshop · Answers checked against real Java")
