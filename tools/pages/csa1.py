from gen_unit import topic, chapter, worked, box, detailed, quiz_section, page, shuffle
from cs_common import *

T1 = {"e": "Programs & Types", "m": "Objects & Strings"}
CH = []

# ------------------------------------------------------------------ overview
HOW = '''<ol class="steps">
<li>Read the chapters in order. Each topic has an explanation, code, a worked example and a <b>Detailed explanation</b> for the full reasoning.</li>
<li>Use the <b>labs</b> (dashed boxes): type your own values and watch Java's answer change.</li>
<li>Code animations step through a program line by line. Press <b>Step ▶</b> to go one line at a time and predict the next value before you see it.</li>
<li>Then do <b>Practice</b>, <b>Challenge</b> and the timed <b>Practice Exam</b>.</li></ol>'''
t = Tr('''int score = 7;
int bonus = 2;
score = score + bonus;
System.out.println(score);''')
t.s(1, score=7).s(2, bonus=2).s(3, score=9).s(4, out="9")
jcheck("int score = 7;\nint bonus = 2;\nscore = score + bonus;\nSystem.out.println(score);", "9")
CORE = f'''<p>A Java program is a list of instructions that run from top to bottom. Each instruction stores a value, computes something, or calls a method. Unit 1 is about the building blocks: <b>variables and types</b>, <b>expressions</b>, <b>calling methods</b>, <b>creating objects</b>, and working with <b>Strings</b>.</p>
{anim(t.spec(), "Step through: each line runs in order and changes the variables")}
<div class="grid2"><div class="mini"><h4>Exam weight</h4><p>Unit 1 is 15–25% of the AP exam. Almost every multiple-choice question in the other units also needs these skills, especially tracing code by hand.</p></div>
<div class="mini"><h4>The main skill</h4><p>Tracing: keeping track of every variable's value as each line runs. Write a small table on scratch paper and update it line by line.</p></div></div>'''
CH.append(chapter("overview-c1", "Overview", "Overview", [topic("start-c1", "How to use this page", HOW, sub="Suggested order."), topic("core-c1", "Core ideas", CORE)]))

# ------------------------------------------------------------------ programs and variables
jcheck('System.out.print("A");\nSystem.out.println("B");\nSystem.out.println("C");', "AB C")
ALG = topic("algorithms", "Algorithms, programs and compilers", f'''
<p>An <b>algorithm</b> is a step-by-step process to solve a problem. A <b>program</b> is an algorithm written in a programming language. Java code is turned into something the computer can run by a <b>compiler</b>, which also checks the code's grammar.</p>
<div class="tblwrap"><table><tr><th>Kind of error</th><th>When it appears</th><th>Example</th></tr>
<tr><td><b>Syntax (compile-time) error</b></td><td>The compiler refuses to build the program.</td><td>Missing semicolon, misspelled keyword, storing a String in an int</td></tr>
<tr><td><b>Run-time error (exception)</b></td><td>The program compiles, then crashes while running.</td><td>Dividing an int by 0, calling a method on <code>null</code>, a bad String index</td></tr>
<tr><td><b>Logic error</b></td><td>It runs, but gives the wrong answer.</td><td>Using <code>&lt;</code> instead of <code>&lt;=</code>, adding when you meant to multiply</td></tr></table></div>
<h3>Output</h3>
<p><code>System.out.println(x)</code> prints x and then moves to a new line. <code>System.out.print(x)</code> prints x and stays on the same line.</p>
{code('System.out.print("A");\nSystem.out.println("B");\nSystem.out.println("C");')}
<p>Output:</p>{outbox("AB\nC")}
''', pill=("e", "1.1"), sub="How code becomes a running program, and the three kinds of errors.",
 det=("Compiling, running and finding errors", '''<h4>What the compiler does</h4><p>The compiler reads your whole source file and translates it into bytecode. It refuses if any line breaks Java's rules, and it reports the first problems it finds. Nothing runs until every compile error is fixed.</p>
<h4>Exceptions</h4><p>An exception is Java's way of stopping a program that tried something impossible while running: <code>ArithmeticException</code> (integer division by zero), <code>NullPointerException</code> (using a reference that points to nothing), <code>StringIndexOutOfBoundsException</code> (a bad index). The program stops at that line unless the exception is handled.</p>
<h4>Logic errors are the hardest</h4><p>The computer can't detect them. You find them by testing with inputs whose answers you already know, especially edge cases like 0, 1, negative numbers and empty Strings.</p>
<h4>On the exam</h4><p>Questions often ask what happens when code runs. Check in this order: does it compile? does it crash? if not, trace the output.</p>'''))

jcheck('int a = 5;\ndouble b = 2.5;\nboolean done = false;\nString name = "Ada";\nSystem.out.println(a + " " + b + " " + done + " " + name);', "5 2.5 false Ada")
VARS = topic("variables", "Variables and data types", f'''
<p>A <b>variable</b> is a named storage location. Every variable has a <b>type</b> that decides what it can hold. Declaring a variable gives it a type and name; assigning gives it a value.</p>
<div class="tblwrap"><table><tr><th>Type</th><th>Holds</th><th>Examples</th></tr>
<tr><td><code>int</code></td><td>whole numbers</td><td><code>0</code>, <code>-12</code>, <code>2147483647</code></td></tr>
<tr><td><code>double</code></td><td>numbers with decimals</td><td><code>2.5</code>, <code>-0.1</code>, <code>3.0</code></td></tr>
<tr><td><code>boolean</code></td><td>true or false</td><td><code>true</code>, <code>false</code></td></tr>
<tr><td><code>String</code> (a reference type)</td><td>text</td><td><code>"Ada"</code>, <code>""</code></td></tr></table></div>
<p><code>int</code>, <code>double</code> and <code>boolean</code> are <b>primitive types</b>: the variable holds the value itself. <code>String</code> and every class are <b>reference types</b>: the variable holds a reference (an arrow) to an object.</p>
{code('int a = 5;\ndouble b = 2.5;\nboolean done = false;\nString name = "Ada";\nSystem.out.println(a + " " + b + " " + done + " " + name);')}
{outbox("5 2.5 false Ada")}
<p>A <b>final</b> variable is a constant: once assigned, it can't change. By convention its name is in capitals: <code>final int MAX_TRIES = 3;</code></p>
{box("trap", "Common mistake", "An int can be stored in a double (<code>double d = 5;</code> stores 5.0), but a double can't be stored in an int without a cast: <code>int x = 2.5;</code> is a compile error.")}
''', pill=("e", "1.2"), sub="Choosing a type, declaring and assigning.",
 det=("Primitive vs reference, and naming rules", '''<h4>Why two kinds of types?</h4><p>Primitives are small, fixed-size values (an int is 32 bits). Objects can be large and complicated, so the variable stores only the object's address. This difference explains aliasing and <code>==</code> vs <code>equals</code>, which come up later in this unit.</p>
<h4>Naming</h4><p>Names can contain letters, digits, _ and $, can't start with a digit, and can't be keywords like <code>int</code> or <code>class</code>. Java style uses camelCase: <code>totalScore</code>, <code>numStudents</code>. Names are case-sensitive: <code>score</code> and <code>Score</code> are different variables.</p>
<h4>Declaring twice</h4><p>A variable can be declared only once in the same block. <code>int x = 3; int x = 4;</code> is a compile error; the second line should be <code>x = 4;</code>.</p>
<h4>Using a variable before giving it a value</h4><p>A local variable that has been declared but not assigned can't be used: the compiler reports "variable might not have been initialized".</p>'''))

jcheck('System.out.println(7 / 2);\nSystem.out.println(7.0 / 2);\nSystem.out.println(7 % 2);\nSystem.out.println(1 + 2 + "3" + 4 + 5);', "3 3.5 1 3345")
EXPR = topic("expressions", "Expressions and output", f'''
<p>Arithmetic operators: <code>+ - * / %</code>. Java follows the usual order of operations: <code>* / %</code> before <code>+ -</code>, left to right, with parentheses first.</p>
<h3>Integer division and remainder</h3>
<p>When <b>both</b> operands are ints, <code>/</code> gives an int: the decimal part is cut off (not rounded). <code>%</code> (modulus) gives the remainder.</p>
<div class="tblwrap"><table><tr><th>Expression</th><th>Value</th><th>Why</th></tr>
<tr><td><code>7 / 2</code></td><td>3</td><td>int / int: 3.5 truncated</td></tr>
<tr><td><code>7.0 / 2</code></td><td>3.5</td><td>a double is involved</td></tr>
<tr><td><code>7 % 2</code></td><td>1</td><td>7 = 2·3 + <b>1</b></td></tr>
<tr><td><code>2 % 7</code></td><td>2</td><td>7 goes in 0 times, remainder 2</td></tr>
<tr><td><code>-7 / 2</code></td><td>-3</td><td>truncates toward zero</td></tr></table></div>
{lab(type="arith")}
<h3>String concatenation</h3>
<p><code>+</code> with a String joins text. It's evaluated left to right, so the order matters:</p>
{code('System.out.println(1 + 2 + "3" + 4 + 5);')}
{outbox("3345")}
<p>1 + 2 is 3 (both ints), then "3" + "3" is "33", then "334", then "3345".</p>
<h3>Escape sequences</h3><p>Inside a String: <code>\\"</code> is a quote, <code>\\\\</code> is a backslash, <code>\\n</code> is a new line.</p>
{worked("What does <code>System.out.println(17 % 5 + 17 / 5 * 2);</code> print?", "17 % 5 = 2. 17 / 5 = 3 (int division), times 2 = 6. 2 + 6 = <b>8</b>.")}
{box("trap", "Common mistake", "<code>int / int</code> by zero throws ArithmeticException, but <code>double / 0</code> gives Infinity. AP questions use the int case.")}
''', pill=("e", "1.3"), sub="Operators, integer division, % and joining Strings.",
 det=("Using % in real code", '''<h4>Even or odd</h4><p><code>n % 2 == 0</code> is true for even n. Odd numbers give a remainder of 1 (or −1 for negative n), so test <code>n % 2 != 0</code> for odd.</p>
<h4>Digits</h4><p><code>n % 10</code> is the last digit; <code>n / 10</code> removes the last digit. Repeating both in a loop (Unit 2) takes a number apart digit by digit.</p>
<h4>Wrapping around</h4><p><code>(i + 1) % size</code> cycles 0, 1, 2, …, size−1, 0, … which is handy for clocks and turns.</p>
<h4>Divisibility</h4><p><code>a % b == 0</code> means b divides a evenly.</p>'''))
jcheck('System.out.println(17 % 5 + 17 / 5 * 2);', "8")

t = Tr('''int x = 10;
int y = 3;
x = x + y;
y = x - y;
x = x - y;
System.out.println(x + " " + y);''')
t.s(1, x=10).s(2, y=3).s(3, x=13).s(4, y=10).s(5, x=3).s(6, out="3 10")
jcheck('int x = 10;\nint y = 3;\nx = x + y;\ny = x - y;\nx = x - y;\nSystem.out.println(x + " " + y);', "3 10")
ASSIGN = topic("assignment", "Assignment statements and input", f'''
<p>The assignment operator <code>=</code> means "store": evaluate the right side, then put the value in the variable on the left. It is <b>not</b> a statement that two things are equal.</p>
{code('x = x + 1;   // take x, add 1, store the result back in x')}
<p>The value on the right is computed using the <b>current</b> values of the variables, before anything changes.</p>
{anim(t.spec(ask=None), "Swapping two values without a third variable. Use Step ▶ to predict each line")}
<h3>Input</h3><p>Programs can read keyboard input with the <code>Scanner</code> class. The AP exam does not test keyboard input; values usually come in as method parameters.</p>
{box("tip", "Tracing tip", "Write each variable at the top of a column. Each time a line assigns, cross out the old value and write the new one below it. Never update in your head.")}
''', pill=("e", "1.4"), sub="= means store, and the right side is evaluated first.")
CH.append(chapter("basics-c1", "Programs & Variables", "Variables", [ALG, VARS, EXPR, ASSIGN]))

# ------------------------------------------------------------------ casting
jcheck('double d = 3.99;\nint n = (int) d;\nSystem.out.println(n);\nSystem.out.println((double) 7 / 2);\nSystem.out.println((double) (7 / 2));\nSystem.out.println((int) (2.6 + 0.5));', "3 3.5 3.0 3")
jcheck('int big = Integer.MAX_VALUE;\nbig = big + 1;\nSystem.out.println(big == Integer.MIN_VALUE);', "true")
CAST = topic("casting", "Casting and range of variables", f'''
<p>A <b>cast</b> converts a value to another type: <code>(int)</code> or <code>(double)</code> in front of a value.</p>
<div class="grid2"><div class="mini"><h4><code>(int)</code> on a double</h4><p>Cuts off the decimal part (truncates toward zero). <code>(int) 3.99</code> is 3; <code>(int) -3.99</code> is -3.</p></div>
<div class="mini"><h4><code>(double)</code> on an int</h4><p>Gives the same number as a double: <code>(double) 7</code> is 7.0. Use it to force real division.</p></div></div>
{code('System.out.println((double) 7 / 2);    // cast happens first: 7.0 / 2 = 3.5\nSystem.out.println((double) (7 / 2));  // 7 / 2 = 3 first, then 3.0')}
{outbox("3.5\n3.0")}
<h3>Rounding</h3><p>To round a positive double to the nearest int: <code>(int) (x + 0.5)</code>. For a negative double: <code>(int) (x - 0.5)</code>.</p>
{lab(type="casting", d=2.6)}
<h3>Range and overflow</h3><p>An int is stored in 32 bits, so it can only hold values from <code>Integer.MIN_VALUE</code> (−2,147,483,648) to <code>Integer.MAX_VALUE</code> (2,147,483,647). Going past the end <b>overflows</b> and wraps around to the other end without any error.</p>
{code('int big = Integer.MAX_VALUE;\nbig = big + 1;   // now equals Integer.MIN_VALUE')}
<p>Doubles are stored approximately, so some decimals can't be represented exactly: <code>0.1 + 0.2</code> prints 0.30000000000000004.</p>
''', pill=("e", "1.5"), sub="Converting between int and double.",
 det=("When Java converts automatically", '''<h4>Widening is automatic</h4><p>An int fits inside a double without losing anything, so Java converts automatically when you store an int in a double or mix them in arithmetic: <code>5 + 2.0</code> is 7.0.</p>
<h4>Narrowing needs a cast</h4><p>A double can lose its decimal part when it becomes an int, so Java makes you write the cast to show you mean it.</p>
<h4>Where the cast applies</h4><p>A cast applies only to the value right after it. <code>(int) 2.5 * 2</code> is <code>2 * 2</code> = 4, but <code>(int) (2.5 * 2)</code> is 5. Use parentheses to cast a whole expression.</p>
<h4>Averages</h4><p>The classic bug: <code>int sum = 7, count = 2; double avg = sum / count;</code> gives 3.0, because the int division happens before the value is stored. Fix: <code>(double) sum / count</code>.</p>'''))

jcheck('int n = 5;\nn += 3;\nn *= 2;\nn -= 4;\nn /= 3;\nn %= 3;\nn++;\nSystem.out.println(n);', "2")
t = Tr('''int n = 5;
n += 3;
n *= 2;
n -= 4;
n /= 3;
n %= 3;
n++;
System.out.println(n);''')
t.s(1, n=5).s(2, n=8).s(3, n=16).s(4, n=12).s(5, n=4).s(6, n=1).s(7, n=2).s(8, out="2")
COMP = topic("compound", "Compound assignment operators", f'''
<div class="tblwrap"><table><tr><th>Short form</th><th>Means</th></tr>
<tr><td><code>x += 3;</code></td><td><code>x = x + 3;</code></td></tr><tr><td><code>x -= 3;</code></td><td><code>x = x - 3;</code></td></tr>
<tr><td><code>x *= 3;</code></td><td><code>x = x * 3;</code></td></tr><tr><td><code>x /= 3;</code></td><td><code>x = x / 3;</code> (int division if x is an int)</td></tr>
<tr><td><code>x %= 3;</code></td><td><code>x = x % 3;</code></td></tr><tr><td><code>x++;</code> / <code>x--;</code></td><td>add 1 / subtract 1</td></tr></table></div>
{anim(t.spec(ask="vars"), "Trace n through each operator; values appear as you step", reveal=False)}
{worked("What is n after the code above runs?", "5 → 8 → 16 → 12 → 4 (12 / 3) → 1 (4 % 3) → <b>2</b>.")}
{box("tip", "Exam note", "On the AP exam, <code>++</code> and <code>--</code> appear only as their own statements (<code>count++;</code>), never inside a larger expression.")}
''', pill=("e", "1.6"), sub="Shortcuts for updating a variable.")
CH.append(chapter("casting-c1", "Casting & Operators", "Casting", [CAST, COMP]))

# ------------------------------------------------------------------ methods and API
jcheck('System.out.println(Math.abs(-4));\nSystem.out.println(Math.pow(2, 3));\nSystem.out.println(Math.sqrt(49));', "4 8.0 7.0")
API = topic("api", "APIs, libraries and documentation", f'''
<p>A <b>library</b> is a collection of classes someone else wrote. An <b>API</b> (application program interface) is the documentation that tells you what those classes do and how to call their methods, without showing their code. You use <code>String</code> and <code>Math</code> this way: you know what <code>Math.sqrt</code> does without seeing how.</p>
<p>A <b>class</b> defines a type: the <b>attributes</b> (data) each object has and the <b>behaviors</b> (methods) it can perform.</p>
<h3>Comments</h3>
{code("""// a single-line comment
/* a comment that can
   span several lines */
/** A Javadoc comment, used to document a method
 *  @param n the number of items (precondition: n > 0)
 *  @return the average
 */""")}
<p>A <b>precondition</b> is something that must be true before a method is called; the method doesn't have to check it. A <b>postcondition</b> is something that will be true after the method finishes (often describing the return value).</p>
{box("tip", "FRQ note", "If a free-response question states a precondition (for example, \"n is positive\"), you can assume it. You don't need extra code to check it.")}
''', pill=("e", "1.7–1.8"), sub="Using code other people wrote.")

SIG = topic("signatures", "Method signatures and calling methods", f'''
<p>A method is a named block of code. Its <b>signature</b> is its name and its parameter list. The header also shows its return type.</p>
{code('public static double average(int a, int b)')}
<div class="grid3"><div class="mini"><h4>Return type</h4><p><code>double</code>: the call produces a double value. <code>void</code> means it returns nothing.</p></div>
<div class="mini"><h4>Parameters</h4><p><code>int a, int b</code>: the method needs two ints, in that order.</p></div>
<div class="mini"><h4>Arguments</h4><p>The actual values you pass: <code>average(3, 8)</code>. They are copied into the parameters.</p></div></div>
<h3>Calling methods</h3>
<ul><li>A <b>void</b> method is called as its own statement: <code>printReport();</code></li>
<li>A <b>non-void</b> method returns a value you should use: <code>double avg = average(3, 8);</code> or <code>System.out.println(average(3, 8));</code></li>
<li><b>Class (static) methods</b> are called with the class name: <code>Math.sqrt(16)</code>. Inside the same class, the name alone works.</li></ul>
<h3>Overloading</h3><p>Several methods can share a name if their parameter lists differ (in number, type or order of types). Java picks the one that matches the arguments: <code>Math.abs(-3)</code> returns int 3 and <code>Math.abs(-3.0)</code> returns double 3.0.</p>
{box("trap", "Common mistake", "Calling a non-void method and ignoring the result: <code>Math.sqrt(x);</code> compiles but does nothing useful. The value must be stored or used.")}
''', pill=("e", "1.9–1.10"), sub="Reading a method header and calling it correctly.",
 det=("Parameters are copies", '''<h4>Pass by value</h4><p>When you call a method, each argument's value is copied into the matching parameter. If the method changes its parameter, the caller's variable doesn't change. For objects, the copy is a copy of the reference, so the method can change the object both variables point to (Unit 3 goes deeper).</p>
<h4>Matching arguments</h4><p>The number of arguments must match, and each must be compatible with its parameter's type. An int argument works for a double parameter (widening), but a double argument doesn't work for an int parameter.</p>
<h4>Return values flow back</h4><p>A call like <code>average(3, 8)</code> is replaced by its return value when the expression is evaluated, so <code>average(3, 8) * 2</code> works like any number.</p>'''))

jcheck('int roll = (int) (Math.random() * 6) + 1;\nSystem.out.println(roll >= 1 && roll <= 6);', "true")
MATH = topic("math-class", "The Math class", f'''
<div class="tblwrap"><table><tr><th>Method</th><th>Returns</th><th>Example</th></tr>
<tr><td><code>Math.abs(x)</code></td><td>absolute value (int for int, double for double)</td><td><code>Math.abs(-4)</code> → 4</td></tr>
<tr><td><code>Math.pow(base, exp)</code></td><td>double: base<sup>exp</sup></td><td><code>Math.pow(2, 3)</code> → 8.0</td></tr>
<tr><td><code>Math.sqrt(x)</code></td><td>double: square root</td><td><code>Math.sqrt(49)</code> → 7.0</td></tr>
<tr><td><code>Math.random()</code></td><td>double from 0.0 up to (not including) 1.0</td><td>0.7316…</td></tr></table></div>
<h3>Random integers in a range</h3>
<p>To get a random int from <b>low</b> to <b>high</b> inclusive:</p>
{code('int r = (int) (Math.random() * (high - low + 1)) + low;')}
{worked("Write an expression for a random die roll from 1 to 6.", "Range size = 6 − 1 + 1 = 6. <code>(int) (Math.random() * 6) + 1</code>. Math.random() * 6 is in [0, 6); casting gives 0–5; adding 1 gives 1–6.")}
{box("trap", "Common mistake", "<code>(int) Math.random() * 6</code> is always 0: the cast applies to Math.random() first (giving 0), then 0 * 6.")}
''', pill=("e", "1.11"), sub="The Java Quick Reference Math methods.",
 det=("Why the random formula works", '''<h4>Stretch, shift, cut</h4><p>Math.random() gives a double in [0, 1). Multiplying by the number of possible values (high − low + 1) stretches it to [0, count). Casting to int gives one of 0, 1, …, count − 1, each equally likely. Adding low shifts the range to low … high.</p>
<h4>Checking a formula</h4><p>Plug in the extremes: the smallest Math.random() can be is 0, the largest is just under 1. For <code>(int) (Math.random() * 10) + 5</code>: smallest 0 + 5 = 5, largest (int) 9.99… + 5 = 14. Range 5–14.</p>
<h4>pow and sqrt always return doubles</h4><p><code>Math.pow(2, 3)</code> prints 8.0, not 8. To store it in an int, cast: <code>(int) Math.pow(2, 3)</code>.</p>'''))
CH.append(chapter("methods-c1", "Methods & the Math Class", "Methods", [API, SIG, MATH]))

# ------------------------------------------------------------------ objects
POINT = '''class Point {
    private int x;
    private int y;
    public Point(int x, int y) { this.x = x; this.y = y; }
    public int getX() { return x; }
    public void moveRight(int d) { x += d; }
}'''
jcheck('Point p = new Point(2, 5);\nPoint q = p;\nq.moveRight(3);\nSystem.out.println(p.getX());', "5", cls=POINT)
mem = {"type": "memory", "frames": [
  {"note": "Point p = new Point(2, 5);  creates an object; p stores a reference to it.", "vars": [["p", "Point", "@a"]], "objs": [["a", "Point", [["x", 2], ["y", 5]]]]},
  {"note": "Point q = p;  copies the reference, not the object. Both arrows point to the same Point (aliases).", "vars": [["p", "Point", "@a"], ["q", "Point", "@a"]], "objs": [["a", "Point", [["x", 2], ["y", 5]]]]},
  {"note": "q.moveRight(3);  changes the one shared object, so p.getX() is now 5 too.", "vars": [["p", "Point", "@a"], ["q", "Point", "@a"]], "objs": [["a", "Point", [["x", 5], ["y", 5]]]]},
  {"note": "q = new Point(0, 0);  q now points to a new object. p is unchanged.", "vars": [["p", "Point", "@a"], ["q", "Point", "@b"]], "objs": [["a", "Point", [["x", 5], ["y", 5]]], ["b", "Point", [["x", 0], ["y", 0]]]]},
  {"note": "q = null;  q points to nothing. Calling q.getX() now would throw a NullPointerException.", "vars": [["p", "Point", "@a"], ["q", "Point", "null"]], "objs": [["a", "Point", [["x", 5], ["y", 5]]]]}]}
OBJ = topic("objects", "Objects: instances of classes", f'''
<p>A <b>class</b> is a blueprint. An <b>object</b> is one thing built from that blueprint, with its own values for each attribute. <code>Point</code> is a class; a point at (2, 5) is an object of that class (an <b>instance</b>).</p>
<p>Objects are created with <code>new</code> and a <b>constructor</b>, which sets up the new object's starting values:</p>
{code("Point p = new Point(2, 5);")}
<p>The variable <code>p</code> doesn't contain the object; it holds a <b>reference</b> to where the object lives in memory.</p>
{anim(mem, "References, aliases and null. Use Step ▶ to go one line at a time")}
<h3>Constructors and overloading</h3>
<p>A class can have several constructors with different parameter lists. <code>new Point()</code> might make (0, 0), while <code>new Point(2, 5)</code> uses the given values. Arguments must match one constructor's parameters in number, order and type.</p>
<h3>null</h3><p>A reference variable that doesn't point to any object holds <code>null</code>. Calling a method through a null reference throws a <b>NullPointerException</b>.</p>
''', pill=("m", "1.12–1.13"), sub="Classes, objects, constructors and references.",
 det=("What new actually does", '''<h4>Three steps</h4><p><code>new Point(2, 5)</code> (1) sets aside memory for a new Point object, (2) runs the constructor to fill in its attributes, (3) produces a reference to it. The assignment then stores that reference in the variable.</p>
<h4>Aliasing</h4><p>After <code>Point q = p;</code> there's still only one object. Changing it through q is visible through p. That's the main difference from primitives: <code>int b = a;</code> copies the number itself.</p>
<h4>Garbage collection</h4><p>When no variable refers to an object anymore, Java eventually reclaims its memory automatically.</p>
<h4>Default values</h4><p>An object's attributes that aren't set by the constructor get defaults: 0 for int, 0.0 for double, false for boolean, null for references.</p>'''))

jcheck('Point p = new Point(1, 1);\np.moveRight(4);\nint a = p.getX();\nSystem.out.println(a * 2);', "10", cls=POINT)
INST = topic("instance-methods", "Calling instance methods", f'''
<p>An <b>instance method</b> belongs to an object and is called with the dot operator on a reference: <code>p.moveRight(4)</code>. It can read and change that object's own attributes.</p>
{code(POINT)}
{code("Point p = new Point(1, 1);\np.moveRight(4);        // void: changes p's x to 5\nint a = p.getX();      // non-void: returns 5\nSystem.out.println(a * 2);")}
{outbox("10")}
<div class="grid2"><div class="mini"><h4>Class method</h4><p>Called on the class: <code>Math.sqrt(9)</code>. Doesn't need an object.</p></div>
<div class="mini"><h4>Instance method</h4><p>Called on an object: <code>p.getX()</code>, <code>name.length()</code>. Uses that object's data.</p></div></div>
{box("trap", "Common mistake", "Calling an instance method with the class name: <code>Point.getX()</code> is a compile error, because Java doesn't know which point you mean.")}
''', pill=("m", "1.14"), sub="The dot operator on an object.")
CH.append(chapter("objects-c1", "Objects", "Objects", [OBJ, INST]))

# ------------------------------------------------------------------ Strings
jcheck('String s = "computer";\nSystem.out.println(s.length());\nSystem.out.println(s.substring(1, 4));\nSystem.out.println(s.substring(3));\nSystem.out.println(s.indexOf("put"));\nSystem.out.println(s.indexOf("z"));', "8 omp puter 3 -1")
jcheck('String a = "apple";\nSystem.out.println(a.compareTo("banana") < 0);\nSystem.out.println("cat".compareTo("cat"));\nSystem.out.println(a.equals("Apple"));', "true 0 false")
jcheck('String s = "hi";\ns.toUpperCase();\nSystem.out.println(s);\ns = s + "!";\nSystem.out.println(s);', "hi hi!")
strspec = {"type": "strbox", "s": "computer", "ops": [{"f": "length"}, {"f": "substring", "a": 1, "b": 4}, {"f": "substring", "a": 3}, {"f": "indexOf", "x": "put"}, {"f": "indexOf", "x": "z"}]}
smem = {"type": "memory", "frames": [
  {"note": 'String s = "hi";', "vars": [["s", "String", "@a"]], "objs": [["a", "String", '"hi"']]},
  {"note": 's.toUpperCase(); returns a NEW String "HI" that nothing stores. s still points to "hi". Strings never change.', "vars": [["s", "String", "@a"]], "objs": [["a", "String", '"hi"'], ["b", "String", '"HI" (lost)']]},
  {"note": 's = s + "!"; builds a new String "hi!" and moves the arrow to it.', "vars": [["s", "String", "@c"]], "objs": [["a", "String", '"hi"'], ["c", "String", '"hi!"']]}]}
STR = topic("strings", "String manipulation", f'''
<p>A String is an object holding a sequence of characters. Each character has an <b>index</b>, starting at <b>0</b>. The last index is <code>length() - 1</code>.</p>
{anim(strspec, "Indexes start at 0. substring stops BEFORE its second index")}
<div class="tblwrap"><table><tr><th>Method (Java Quick Reference)</th><th>Returns</th></tr>
<tr><td><code>int length()</code></td><td>number of characters</td></tr>
<tr><td><code>String substring(int from, int to)</code></td><td>characters from index <code>from</code> up to but <b>not including</b> <code>to</code></td></tr>
<tr><td><code>String substring(int from)</code></td><td>from index <code>from</code> to the end</td></tr>
<tr><td><code>int indexOf(String str)</code></td><td>index of the first occurrence of str, or <b>−1</b> if not found</td></tr>
<tr><td><code>boolean equals(String other)</code></td><td>true if the characters are exactly the same</td></tr>
<tr><td><code>int compareTo(String other)</code></td><td>negative if this comes first alphabetically, 0 if equal, positive if after</td></tr></table></div>
{lab(type="string", s="computer", a=1, b=4, c=3, x="put", t="cat")}
<h3>One character</h3><p>To get the character at index i as a String: <code>s.substring(i, i + 1)</code>.</p>
<h3>Strings are immutable</h3><p>No String method changes a String. Methods like <code>substring</code> return a <b>new</b> String. To "change" s, assign the result back: <code>s = s.substring(1);</code></p>
{anim(smem, "String methods return new Strings; the original never changes")}
<h3>== vs equals</h3><p>For objects, <code>==</code> checks whether two references point to the <b>same object</b>. To compare text, always use <code>equals</code>.</p>
{worked('Given <code>String w = "banana";</code>, what is <code>w.substring(w.indexOf("n"), w.length() - 1)</code>?', 'indexOf("n") = 2. length() − 1 = 5. substring(2, 5) = characters at 2, 3, 4 = <b>"nan"</b>.')}
{box("trap", "Common mistakes", "substring(a, b) has length b − a. An index equal to length() is allowed as the <i>end</i> of substring, but not as a start for a one-character substring. Going past it throws StringIndexOutOfBoundsException.")}
''', pill=("m", "1.15"), sub="Indexes, substring, indexOf, equals and compareTo.",
 det=("compareTo and String details", '''<h4>How compareTo decides</h4><p>It compares character by character from the left. At the first difference, it returns the difference of the two characters' codes. If one String runs out first, the shorter one comes first. Uppercase letters come before lowercase ("Zebra" comes before "apple"). Only the sign of the result matters on the exam.</p>
<h4>Concatenation with other types</h4><p><code>"Score: " + 90</code> is "Score: 90". Any value joined with a String becomes text, and objects use their <code>toString</code> method.</p>
<h4>Finding every occurrence</h4><p>Combining indexOf and substring in a loop (Unit 2) lets you count or remove every copy of a word: find it, record it, then search again in the part after it.</p>
<h4>Empty String</h4><p><code>""</code> has length 0. <code>s.substring(s.length())</code> is legal and gives "".</p>'''))
jcheck('String w = "banana";\nSystem.out.println(w.substring(w.indexOf("n"), w.length() - 1));', "nan")
CH.append(chapter("strings-c1", "Strings", "Strings", [STR]))

# ------------------------------------------------------------------ tracing & FRQ
FRQ = topic("frq-c1", "Tracing questions and free response", f'''
<p>The AP exam has 42 multiple-choice questions and 4 free-response questions, all on the computer. Unit 1 skills appear in nearly every question. Three habits earn points:</p>
<ol class="steps"><li><b>Trace on paper.</b> Make a table with a column per variable and update it line by line.</li>
<li><b>Check types at every step.</b> Is this division int / int? Is this + joining Strings?</li>
<li><b>Check compile and run-time problems first</b>: wrong type stored, method called on the class instead of an object, bad substring index, null reference.</li></ol>
<h3>Free-response question 1: Methods and Control Structures</h3>
<p>You write method bodies that call other methods described in the problem. Read each method's header carefully: its return type tells you whether to store the result, and its parameters tell you what to pass.</p>
{code("""// Given: public static int getScore(String name)   returns a player's score
// Write: average of two players' scores, as a double
public static double averageScore(String a, String b)
{
    int total = getScore(a) + getScore(b);
    return total / 2.0;
}""")}
{box("tip", "Free-response scoring", "You lose points for calling methods incorrectly (wrong number or type of arguments), for losing precision with int division, and for printing instead of returning. Small syntax slips like a missing semicolon usually aren't penalized.")}
''', sub="How Unit 1 shows up on the exam.")
CH.append(chapter("frq-ch-c1", "Tracing & FRQs", "Tracing & FRQs", [FRQ]))

REV = topic("review-c1", "Java Quick Reference: Unit 1 lines", '''
<div class="tblwrap"><table><tr><th>Class</th><th>Method</th><th>What it does</th></tr>
<tr><td>String</td><td><code>int length()</code></td><td>number of characters</td></tr>
<tr><td>String</td><td><code>String substring(int from, int to)</code></td><td>from index from up to to − 1</td></tr>
<tr><td>String</td><td><code>String substring(int from)</code></td><td>from index from to the end</td></tr>
<tr><td>String</td><td><code>int indexOf(String str)</code></td><td>first index of str, or −1</td></tr>
<tr><td>String</td><td><code>boolean equals(Object other)</code></td><td>same characters?</td></tr>
<tr><td>String</td><td><code>int compareTo(String other)</code></td><td>&lt; 0, 0 or &gt; 0 alphabetically</td></tr>
<tr><td>Math</td><td><code>int abs(int x)</code>, <code>double abs(double x)</code></td><td>absolute value</td></tr>
<tr><td>Math</td><td><code>double pow(double base, double exp)</code></td><td>power</td></tr>
<tr><td>Math</td><td><code>double sqrt(double x)</code></td><td>square root</td></tr>
<tr><td>Math</td><td><code>double random()</code></td><td>0.0 ≤ value &lt; 1.0</td></tr>
<tr><td>Integer</td><td><code>Integer.MIN_VALUE</code>, <code>Integer.MAX_VALUE</code></td><td>smallest and largest int</td></tr></table></div>''', sub="These are on the reference sheet you get during the exam.")
MIS = topic("mistakes-c1", "Common mistakes", '''<ol class="steps">
<li>Forgetting int division: <code>5 / 2</code> is 2, and <code>(double) (5 / 2)</code> is 2.0.</li>
<li>Thinking (int) rounds. It truncates: <code>(int) 2.9</code> is 2.</li>
<li>substring's second index is excluded; indexes start at 0.</li>
<li>Comparing Strings with == instead of equals.</li>
<li>Expecting a String method to change the String. Strings are immutable; store the result.</li>
<li>Ignoring the return value of a non-void method.</li>
<li>Calling a method on null (NullPointerException).</li>
<li>Reading "1" + 2 + 3 as "6". It's "123"; but 1 + 2 + "3" is "33".</li></ol>''', sub="Points students lose most often.")
CH.append(chapter("review-ch-c1", "Review", "Review", [REV, MIS]))

# ------------------------------------------------------------------ practice
def O(*xs): return [esc(x) for x in xs]
def Oc(*xs): return [ic(x) for x in xs]
PQ = [
 q(f"What is printed?{code('System.out.println(14 / 4);')}", O("3", "3.5", "4", "2"), 0, "Both operands are ints, so the result is truncated: 3.", run="System.out.println(14 / 4);"),
 q(f"What is printed?{code('System.out.println(14 % 4);')}", O("2", "3", "3.5", "0"), 0, "14 = 4·3 + 2, so the remainder is 2.", run="System.out.println(14 % 4);"),
 q(f"What is printed?{code('System.out.println(14 / 4.0);')}", O("3.5", "3", "3.0", "4"), 0, "4.0 is a double, so this is real division: 3.5.", run="System.out.println(14 / 4.0);"),
 q(f"What is printed?{code('System.out.println(2 + 3 * 4 % 5);')}", O("4", "0", "5", "2"), 0, "* and % go left to right before +: 3 * 4 = 12, 12 % 5 = 2, 2 + 2 = 4.", run="System.out.println(2 + 3 * 4 % 5);"),
 q(f"What is printed?{code('System.out.println(\"A\" + 1 + 2);')}", O("A12", "A3", "3A", "Error"), 0, "Left to right: \"A\" + 1 is \"A1\", then \"A1\" + 2 is \"A12\".", run='System.out.println("A" + 1 + 2);'),
 q(f"What is printed?{code('System.out.println(1 + 2 + \"A\");')}", O("3A", "12A", "A3", "Error"), 0, "1 + 2 is evaluated first as int addition: 3, then 3 + \"A\" is \"3A\".", run='System.out.println(1 + 2 + "A");'),
 q(f"What is printed?{code('double d = 7 / 2;' + chr(10) + 'System.out.println(d);')}", O("3.0", "3.5", "3", "4.0"), 0, "7 / 2 is int division (3) before it is stored, then widened to 3.0.", run="double d = 7 / 2;\nSystem.out.println(d);"),
 q(f"What is printed?{code('System.out.println((int) 9.99);')}", O("9", "10", "9.99", "9.0"), 0, "(int) truncates; it doesn't round.", run="System.out.println((int) 9.99);"),
 q(f"What is printed?{code('System.out.println((double) 9 / 2);')}", O("4.5", "4.0", "4", "5.0"), 0, "The cast applies to 9 first, giving 9.0 / 2 = 4.5.", run="System.out.println((double) 9 / 2);"),
 q(f"What is printed?{code('System.out.println((double) (9 / 2));')}", O("4.0", "4.5", "4", "5.0"), 0, "9 / 2 = 4 (int) first, then cast to 4.0.", run="System.out.println((double) (9 / 2));"),
 q("Which line causes a compile error?", Oc("int x = 3.0;", "double y = 3;", "int z = (int) 3.7;", "double w = 3 / 2;"), 0, "A double can't be stored in an int without a cast. The others are legal (widening or an explicit cast).", run="int x = 3.0;", err="compile"),
 q(f"What is the value of n after this code?{code('int n = 10;' + chr(10) + 'n -= 4;' + chr(10) + 'n *= 3;' + chr(10) + 'n %= 5;')}", O("3", "18", "0", "2"), 0, "10 → 6 → 18 → 18 % 5 = 3.", run="int n = 10;\nn -= 4;\nn *= 3;\nn %= 5;\nSystem.out.println(n);"),
 q("Which expression gives a random int from 5 to 10 inclusive?", Oc("(int) (Math.random() * 6) + 5", "(int) (Math.random() * 5) + 5", "(int) Math.random() * 6 + 5", "(int) (Math.random() * 10) + 5"), 0, "There are 10 − 5 + 1 = 6 values, so multiply by 6, then add the low end 5.", t="e"),
 q(f"What is printed?{code('System.out.println(Math.pow(3, 2) + Math.abs(-4));')}", O("13.0", "13", "5.0", "9.04"), 0, "Math.pow returns double 9.0; 9.0 + 4 = 13.0.", run="System.out.println(Math.pow(3, 2) + Math.abs(-4));"),
 q(f"What is printed?{code('System.out.println(Math.sqrt(36) / 4);')}", O("1.5", "1", "1.0", "6.0"), 0, "Math.sqrt returns 6.0; 6.0 / 4 = 1.5.", run="System.out.println(Math.sqrt(36) / 4);"),
 q("A method has the header <code>public static int area(int w, int h)</code>. Which call is correct?", Oc("int a = area(3, 4);", "area(3);", "double a = area(3.5, 4);", "String a = area(3, 4);"), 0, "Two int arguments, and the int result is stored in a compatible variable. area(3.5, 4) passes a double to an int parameter.", t="e"),
 q("Which describes a precondition?", O("A condition that must be true before the method is called", "A condition the method guarantees after it finishes", "A comment that describes the return type", "An exception the method throws"), 0, "Preconditions are the caller's responsibility; postconditions describe what's true afterward."),
 q(f"What is printed?{code('String s = \"hello world\";' + chr(10) + 'System.out.println(s.substring(2, 5));')}", O("llo", "ello", "llo w", "el"), 0, "Indexes 2, 3, 4: l, l, o.", t="m", run='String s = "hello world";\nSystem.out.println(s.substring(2, 5));', sim={"type": "strbox", "s": "hello world", "ops": [{"f": "substring", "a": 2, "b": 5}], "ask": True}),
 q(f"What is printed?{code('String s = \"hello world\";' + chr(10) + 'System.out.println(s.indexOf(\"o\"));')}", O("4", "5", "7", "-1"), 0, "The first \"o\" is at index 4 (h0 e1 l2 l3 o4).", t="m", run='String s = "hello world";\nSystem.out.println(s.indexOf("o"));', sim={"type": "strbox", "s": "hello world", "ops": [{"f": "indexOf", "x": "o"}], "ask": True}),
 q(f"What is printed?{code('String s = \"hello\";' + chr(10) + 'System.out.println(s.substring(s.length() - 2));')}", O("lo", "o", "llo", "l"), 0, "length() is 5, so substring(3) is \"lo\".", t="m", run='String s = "hello";\nSystem.out.println(s.substring(s.length() - 2));'),
 q(f"What happens?{code('String s = \"cat\";' + chr(10) + 'System.out.println(s.substring(2, 4));')}", O("A StringIndexOutOfBoundsException is thrown", "t", "t followed by a space", "Compile error"), 0, "The end index 4 is past length() = 3, so it fails while running.", t="m", run='String s = "cat";\nSystem.out.println(s.substring(2, 4));', err="runtime"),
 q(f"What is printed?{code('String s = \"Java\";' + chr(10) + 's.substring(1);' + chr(10) + 'System.out.println(s);')}", O("Java", "ava", "J", "Error"), 0, "Strings are immutable. The new String from substring is never stored, so s is still \"Java\".", t="m", run='String s = "Java";\ns.substring(1);\nSystem.out.println(s);'),
 q("Which correctly checks whether two String variables <code>a</code> and <code>b</code> have the same text?", Oc("a.equals(b)", "a == b", "a.compareTo(b) == 1", "a = b"), 0, "== compares references; equals compares characters.", t="m"),
 q(f"What is printed?{code('System.out.println(\"apple\".compareTo(\"banana\") < 0);')}", O("true", "false", "-1", "Error"), 0, "\"apple\" comes before \"banana\", so compareTo is negative.", t="m", run='System.out.println("apple".compareTo("banana") < 0);'),
 q(f"Given the <code>Point</code> class shown, what is printed?{code(POINT)}{code('Point a = new Point(3, 4);' + chr(10) + 'Point b = a;' + chr(10) + 'b.moveRight(2);' + chr(10) + 'System.out.println(a.getX());')}", O("5", "3", "2", "Error"), 0, "a and b refer to the same object, so moving it through b changes what a sees.", t="m", run="Point a = new Point(3, 4);\nPoint b = a;\nb.moveRight(2);\nSystem.out.println(a.getX());", cls=POINT,
   sim={"type": "memory", "hide": [], "frames": [{"note": "a = new Point(3, 4)", "vars": [["a", "Point", "@p"]], "objs": [["p", "Point", [["x", 3], ["y", 4]]]]}, {"note": "b = a copies the reference", "vars": [["a", "Point", "@p"], ["b", "Point", "@p"]], "objs": [["p", "Point", [["x", 3], ["y", 4]]]]}, {"note": "b.moveRight(2) changes the shared object", "vars": [["a", "Point", "@p"], ["b", "Point", "@p"]], "objs": [["p", "Point", [["x", "?"], ["y", 4]]]]}]}),
 q(f"What happens?{code('Point p = null;' + chr(10) + 'System.out.println(p.getX());')}", O("A NullPointerException is thrown", "0 is printed", "null is printed", "Compile error"), 0, "p refers to no object, so calling a method through it fails at run time.", t="m", run="Point p = null;\nSystem.out.println(p.getX());", cls=POINT, err="runtime"),
 q("Which is a compile error, assuming the <code>Point</code> class above?", Oc("int x = Point.getX();", "Point p = new Point(1, 2);", "new Point(0, 0).moveRight(1);", "int x = new Point(1, 2).getX();"), 0, "getX is an instance method; it must be called on an object, not the class.", t="m", run="int x = Point.getX();", cls=POINT, err="compile"),
 q("Which statement about <code>int</code> and <code>String</code> variables is true?", O("An int variable stores its value; a String variable stores a reference to an object", "Both store references", "Both store their values directly", "A String variable can't be null"), 0, "int is primitive; String is a reference type and can be null.", t="m"),
 q(f"What is printed?{code('int big = Integer.MAX_VALUE;' + chr(10) + 'big++;' + chr(10) + 'System.out.println(big < 0);')}", O("true", "false", "An error occurs", "Nothing"), 0, "Adding 1 to the largest int overflows and wraps to Integer.MIN_VALUE, which is negative. No error is reported.", run="int big = Integer.MAX_VALUE;\nbig++;\nSystem.out.println(big < 0);"),
 q(f"What is printed?{code('int a = 5, b = 2;' + chr(10) + 'double avg = (double) (a + b) / 2;' + chr(10) + 'System.out.println(avg);')}", O("3.5", "3.0", "3", "4.0"), 0, "(double) 7 = 7.0, divided by 2 = 3.5.", run="int a = 5, b = 2;\ndouble avg = (double) (a + b) / 2;\nSystem.out.println(avg);"),
]
CHAL = [
 q(f"What is printed?{code('String s = \"mississippi\";' + chr(10) + 'int i = s.indexOf(\"ss\");' + chr(10) + 's = s.substring(i + 2);' + chr(10) + 'System.out.println(s.indexOf(\"ss\") + i);')}", O("4", "2", "3", "5"), 0, "First \"ss\" at 2. s becomes \"issippi\" (from index 4), where \"ss\" is at index 1. 1 + 2 = 3? Careful: printed is s.indexOf(\"ss\") + i = 1 + 2 = 3.", t="m", run='String s = "mississippi";\nint i = s.indexOf("ss");\ns = s.substring(i + 2);\nSystem.out.println(s.indexOf("ss") + i);', exp="3"),
 q(f"What is printed?{code('int x = 7;' + chr(10) + 'double y = x / 2 + x % 2 * 1.5;' + chr(10) + 'System.out.println(y);')}", O("4.5", "5.0", "3.5", "4.0"), 0, "x / 2 = 3 (int). x % 2 * 1.5 = 1 * 1.5 = 1.5. 3 + 1.5 = 4.5.", run="int x = 7;\ndouble y = x / 2 + x % 2 * 1.5;\nSystem.out.println(y);"),
 q(f"What is printed?{code('System.out.println(\"\" + 1 + 2 * 3 + 4);')}", O("164", "1234", "11", "74"), 0, "* first: 2 * 3 = 6. Then left to right from the String: \"1\", \"16\", \"164\".", run='System.out.println("" + 1 + 2 * 3 + 4);'),
 q(f"Which expression rounds a <b>negative</b> double d to the nearest int?", Oc("(int) (d - 0.5)", "(int) (d + 0.5)", "(int) d + 0.5", "(int) d"), 0, "For negatives, subtract 0.5 before truncating toward zero: −2.6 − 0.5 = −3.1 → −3.", run="double d = -2.6;\nSystem.out.println((int) (d - 0.5));", exp="-3"),
 q(f"What is printed?{code('String a = \"code\";' + chr(10) + 'String b = a;' + chr(10) + 'a = a + \"r\";' + chr(10) + 'System.out.println(b + \" \" + a);')}", O("code coder", "coder coder", "code code", "coder code"), 0, "a + \"r\" builds a new String and moves a to it; b still refers to the original \"code\".", t="m", run='String a = "code";\nString b = a;\na = a + "r";\nSystem.out.println(b + " " + a);'),
 q(f"Assume <code>s</code> is a String with at least 2 characters. Which expression is always the same as <code>s</code>?", Oc("s.substring(0, 1) + s.substring(1)", "s.substring(0, 1) + s.substring(2)", "s.substring(1) + s.substring(0, 1)", "s.substring(0, s.length() - 1)"), 0, "The first character plus everything from index 1 rebuilds the whole String.", t="m", run='String s = "tree";\nSystem.out.println(s.substring(0, 1) + s.substring(1));', exp="tree"),
 q(f"Which values can <code>(int) (Math.random() * 4) * 2 + 1</code> produce?", O("1, 3, 5, 7", "1 to 8", "1, 3, 5, 7, 9", "2, 4, 6, 8"), 0, "(int) (Math.random() * 4) is 0–3; times 2 is 0, 2, 4, 6; plus 1 is 1, 3, 5, 7."),
 q(f"What is printed?{code('int m = 123;' + chr(10) + 'int d = m % 10 * 100 + m / 10 % 10 * 10 + m / 100;' + chr(10) + 'System.out.println(d);')}", O("321", "123", "6", "312"), 0, "m % 10 = 3, m / 10 % 10 = 2, m / 100 = 1. 300 + 20 + 1 = 321: the digits reversed.", run="int m = 123;\nint d = m % 10 * 100 + m / 10 % 10 * 10 + m / 100;\nSystem.out.println(d);"),
]
# fix challenge #1 options to match the real answer
CHAL[0]["o"] = O("3", "2", "4", "5"); CHAL[0]["x"] = "The first \"ss\" is at index 2, so i = 2. s becomes s.substring(4) = \"issippi\", where \"ss\" is at index 1. 1 + 2 = 3."
EXQ = [
 q(f"What is printed?{code('System.out.println(5 + 3 / 2 * 2);')}", O("7", "8", "9", "6"), 0, "3 / 2 = 1, times 2 = 2, plus 5 = 7.", run="System.out.println(5 + 3 / 2 * 2);", k="calc"),
 q("Which is a run-time error (not a compile error)?", Oc("int x = 5 / 0;", "int x = 5.0;", "String s = 5;", "int x = \"5\";"), 0, "5 / 0 compiles but throws ArithmeticException when run.", k="concept", run="int x = 5 / 0;", err="runtime"),
 q(f"What is printed?{code('double d = 2.7;' + chr(10) + 'int n = (int) d * 2;' + chr(10) + 'System.out.println(n);')}", O("4", "5", "5.4", "6"), 0, "The cast applies to d first: (int) 2.7 = 2, then 2 * 2 = 4.", run="double d = 2.7;\nint n = (int) d * 2;\nSystem.out.println(n);", k="calc"),
 q(f"What is printed?{code('int x = 4;' + chr(10) + 'x += x * 2;' + chr(10) + 'x /= 5;' + chr(10) + 'System.out.println(x);')}", O("2", "2.4", "3", "12"), 0, "x = 4 + 8 = 12; 12 / 5 = 2 (int).", run="int x = 4;\nx += x * 2;\nx /= 5;\nSystem.out.println(x);", k="calc"),
 q("Which gives a random int from 0 to 9 inclusive?", Oc("(int) (Math.random() * 10)", "(int) (Math.random() * 9)", "(int) Math.random() * 10", "(int) (Math.random() * 10) + 1"), 0, "Math.random() * 10 is in [0, 10); casting gives 0–9.", k="concept"),
 q("The header is <code>public static void greet(String name)</code>. Which statement is legal?", Oc('greet("Ana");', 'String s = greet("Ana");', 'greet();', 'System.out.println(greet("Ana"));'), 0, "A void method returns nothing, so its call can't be stored or printed.", k="concept"),
 q(f"What is printed?{code('String w = \"keyboard\";' + chr(10) + 'System.out.println(w.substring(3, 6) + w.indexOf(\"b\"));')}", O("boa3", "boa4", "ybo3", "boar3"), 0, "substring(3, 6) is \"boa\"; indexOf(\"b\") is 3. Joined: \"boa3\".", t="m", run='String w = "keyboard";\nSystem.out.println(w.substring(3, 6) + w.indexOf("b"));', k="calc"),
 q(f"What is printed?{code('String s = \"abc\";' + chr(10) + 'System.out.println(s.indexOf(\"d\") + s.length());')}", O("2", "3", "-1", "4"), 0, "indexOf returns −1 for not found; −1 + 3 = 2.", t="m", run='String s = "abc";\nSystem.out.println(s.indexOf("d") + s.length());', k="calc"),
 q("Which statement is true about Strings in Java?", O("String methods return new Strings and never change the original", "substring changes the original String", "== is the correct way to compare String contents", "Indexes start at 1"), 0, "Strings are immutable.", t="m", k="concept"),
 q(f"What is printed?{code(POINT)}{code('Point p = new Point(0, 0);' + chr(10) + 'Point q = new Point(0, 0);' + chr(10) + 'q.moveRight(1);' + chr(10) + 'System.out.println(p.getX() + q.getX());')}", O("1", "2", "0", "Error"), 0, "p and q are two different objects; only q moved.", t="m", run="Point p = new Point(0, 0);\nPoint q = new Point(0, 0);\nq.moveRight(1);\nSystem.out.println(p.getX() + q.getX());", cls=POINT, k="calc"),
 q("What does <code>new</code> do?", O("Creates an object, runs a constructor and produces a reference to the object", "Declares a primitive variable", "Copies an existing object", "Calls a static method"), 0, "new allocates the object, runs the matching constructor and returns a reference.", t="m", k="concept"),
 q(f"What is printed?{code('System.out.println(\"B\".compareTo(\"a\") < 0);')}", O("true", "false", "0", "Error"), 0, "Uppercase letters come before lowercase ones, so \"B\" comes first: negative.", t="m", run='System.out.println("B".compareTo("a") < 0);', k="calc"),
 q("Which method call returns a <code>double</code>?", Oc("Math.sqrt(16)", "Math.abs(-16)", "\"16\".length()", "\"16\".indexOf(\"6\")"), 0, "sqrt always returns double. abs(int) returns int.", k="concept"),
 q(f"What is printed?{code('int a = 9, b = 4;' + chr(10) + 'System.out.println(a / b + \" \" + a % b + \" \" + (double) a / b);')}", O("2 1 2.25", "2.25 1 2.25", "2 1 2.0", "2 0 2.25"), 0, "9 / 4 = 2, 9 % 4 = 1, 9.0 / 4 = 2.25.", run='int a = 9, b = 4;\nSystem.out.println(a / b + " " + a % b + " " + (double) a / b);', k="calc"),
 q(f"What is printed?{code('String s = \"tic\";' + chr(10) + 's = s + s.substring(1, 2);' + chr(10) + 's = s.substring(1) + s.length();' + chr(10) + 'System.out.println(s);')}", O("ici4", "tici4", "ici3", "ic4"), 0, "s = \"tic\" + \"i\" = \"tici\". substring(1) = \"ici\", length is 4 → \"ici4\".", t="m", run='String s = "tic";\ns = s + s.substring(1, 2);\ns = s.substring(1) + s.length();\nSystem.out.println(s);', k="calc"),
]
FRQS = [
 {"q": f"A class has the method <code>public static int getPoints(String level)</code>, which returns the points earned for a level. Write <code>bonusRound</code>.{code('/** Returns the average points for levels a and b, plus 10% of that average. */' + chr(10) + 'public static double bonusRound(String a, String b)')}",
  "parts": [
   {"p": "(a) Write the method body.", "rubric": [["Calls getPoints correctly for both levels", 1], ["Computes the average without int division (uses 2.0 or a cast)", 1], ["Adds 10% of the average (× 1.1 or + 0.1 × average)", 1], ["Returns the result (does not print it)", 1]],
    "answer": code("public static double bonusRound(String a, String b)\n{\n    double avg = (getPoints(a) + getPoints(b)) / 2.0;\n    return avg * 1.1;\n}")}]},
 {"q": f"Write a static method <code>initials</code> that takes a first name and a last name (each at least one character) and returns the initials followed by the length of the full name without spaces. For example, <code>initials(\"Grace\", \"Hopper\")</code> returns <code>\"GH11\"</code>.",
  "parts": [
   {"p": "(a) Write the method.", "rubric": [["Correct header returning String with two String parameters", 1], ["Gets the first character of each name with substring(0, 1)", 1], ["Adds the two lengths", 1], ["Concatenates in the right order and returns", 1]],
    "answer": code('public static String initials(String first, String last)\n{\n    return first.substring(0, 1) + last.substring(0, 1) + (first.length() + last.length());\n}')}]},
]
jcheck('System.out.println(initials("Grace", "Hopper"));', "GH11", pre='public static String initials(String first, String last) { return first.substring(0, 1) + last.substring(0, 1) + (first.length() + last.length()); }')

EX = {"title": "Unit 1 Practice Exam: Using Objects and Methods", "mcqMinutes": 30, "frqMinutes": 20, "tags": T1,
      "kinds": {"concept": "Concept", "calc": "Code tracing"}, "mcq": EXQ, "frq": FRQS}

if __name__ == "__main__":
    ok = verify({"practice": PQ, "challenge": CHAL, "exam": EXQ})
    assert ok, "fix the questions above"
    balance(PQ, 11); balance(CHAL, 12); balance(EXQ, 13)
    EX["mcq"] = strip_private(EXQ)
    CH.append(chapter("practice-c1", "Practice Questions", "Practice", [quiz_section("practice-quiz-c1", "Practice questions", f"{len(PQ)} questions. Every code answer was checked by running it in Java. Use scratch paper to trace.", "quiz-c1", T1)]))
    CH.append(chapter("challenge-c1", "Challenge Questions", "Challenge", [quiz_section("challenge-quiz-c1", "Challenge questions", "Traps that combine several rules. Turn off animated models in ⚙ Settings for a real exam feel.", "quiz-challenge-c1", T1)], hard=True))
    CH.append(chapter("exam-ch-c1", "Practice Exam", "Practice Exam", ['<section class="topic" id="exam-box-c1"><h2>Practice exam</h2><p class="sub">15 multiple-choice questions (30 minutes) and 2 free-response questions (20 minutes). No feedback until you submit.</p><div class="exam" data-src="exam-c1"></div></section>']))
    HTML = page("unit-1", "AP CSA Unit 1: Using Objects and Methods", "AP Computer Science A · Unit 1",
                'Using Objects<br><span class="hl">and Methods</span>',
                f"Variables and types, expressions, casting, calling methods, the Math class, objects and references, and Strings: explanations, code you can step through, interactive labs, {len(PQ) + len(CHAL)} practice questions checked in Java, and a timed practice exam.",
                "AP Computer Science A Unit 1 review with code animations, interactive labs, practice questions and a practice exam.",
                CH, {"quiz-c1": strip_private(PQ), "quiz-challenge-c1": strip_private(CHAL), "exam-c1": EX},
                course="ap-csa", footer="Apogee · AP Computer Science A · Java", extra_js=("cs-sims.js",))
    import os; os.makedirs("/home/claude/ap-physics-study/courses/ap-csa", exist_ok=True)
    open("/home/claude/ap-physics-study/courses/ap-csa/unit-1.html", "w").write(HTML)
    print("CSA unit 1 written:", len(PQ), len(CHAL), len(EXQ))
