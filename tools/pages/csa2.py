from gen_unit import topic, chapter, worked, box, detailed, quiz_section, page
from cs_common import *

T2 = {"e": "Selection", "m": "Iteration"}
CH = []
def O(*xs): return [esc(x) for x in xs]
def Oc(*xs): return [ic(x) for x in xs]
NL = chr(10)

HOW = '''<ol class="steps">
<li>Selection (if statements and boolean logic) comes first, then loops, then the standard algorithms that combine them.</li>
<li>Use the <b>Step ▶</b> button on code animations to run one line at a time. Predict the next value before you press it.</li>
<li>The <b>labs</b> let you flip booleans and change loop headers to see the effect immediately.</li>
<li>Then <b>Practice</b>, <b>Challenge</b> and the timed <b>Practice Exam</b>.</li></ol>'''
# trace: count down loop
code0 = '''int n = 3;
while (n > 0)
{
    System.out.print(n + " ");
    n--;
}
System.out.println("go");'''
t = Tr(code0); out = ""
t.s(1, n=3)
n = 3
while True:
    t.s(2)
    if not n > 0: break
    out += f"{n} "; t.s(4, out=f"{n} "); n -= 1; t.s(5, n=n)
t.s(7, out="go")
jcheck(code0, "3 2 1 go")
CORE = f'''<p>So far, every line of a program ran exactly once, top to bottom. Unit 2 changes that. <b>Selection</b> (if statements) lets a program choose which lines run. <b>Iteration</b> (loops) lets it repeat lines.</p>
{anim(t.spec(), "A loop repeats while its condition is true. Step through to watch the condition being checked")}
<div class="grid2"><div class="mini"><h4>Exam weight</h4><p>Unit 2 is 25–35% of the exam, the second largest unit. Loop tracing appears in many multiple-choice questions, and free-response question 1 always uses loops and if statements.</p></div>
<div class="mini"><h4>The main skill</h4><p>Tracing loops: keep a table with one row per pass through the loop. Count passes carefully, especially the first and last.</p></div></div>'''
CH.append(chapter("overview-c2", "Overview", "Overview", [topic("core-c2", "Core ideas", CORE)]))

# ---------------- boolean + if
code_g = '''int score = 85;
String grade;
if (score >= 90)
    grade = "A";
else if (score >= 80)
    grade = "B";
else if (score >= 70)
    grade = "C";
else
    grade = "F";
System.out.println(grade);'''
t = Tr(code_g); t.s(1, score=85).s(2).s(3).s(5).s(6, grade="B").s(11, out="B")
jcheck(code_g, "B")
REL = topic("booleans", "Boolean expressions", f'''
<p>A <b>boolean expression</b> evaluates to <code>true</code> or <code>false</code>. Relational operators compare two values:</p>
<div class="tblwrap"><table><tr><th>Operator</th><th>Meaning</th><th>Example (x = 5)</th></tr>
<tr><td><code>==</code></td><td>equal to</td><td><code>x == 5</code> → true</td></tr><tr><td><code>!=</code></td><td>not equal to</td><td><code>x != 5</code> → false</td></tr>
<tr><td><code>&lt;</code>, <code>&lt;=</code></td><td>less than, at most</td><td><code>x &lt; 5</code> → false, <code>x &lt;= 5</code> → true</td></tr>
<tr><td><code>&gt;</code>, <code>&gt;=</code></td><td>greater than, at least</td><td><code>x &gt; 3</code> → true</td></tr></table></div>
{lab(type="bool", vars=[], exprs=["x > 3", "x == 5", "x != y", "x % 2 == 0", "x <= y"], nums={"x": 5, "y": 8}, note="Change x and y. Each expression is evaluated the way Java would.")}
{box("trap", "Common mistakes", "<code>=</code> stores; <code>==</code> compares. For objects (including Strings), <code>==</code> checks whether two references point to the same object; use <code>equals</code> to compare contents.")}
''', pill=("e", "2.1–2.2"), sub="Comparisons that produce true or false.")
IF = topic("if-statements", "if, else and else if", f'''
{code("""if (condition)
{
    // runs only when condition is true
}
else
{
    // runs only when condition is false
}""")}
<p>An <b>if-else-if chain</b> checks conditions from the top and runs <b>only the first</b> branch whose condition is true; the rest are skipped.</p>
{anim(t.spec(), "score = 85: the chain stops at the first true condition")}
<h3>Separate ifs vs else if</h3>
{code("""int x = 95;
if (x > 90) System.out.print("A");
if (x > 80) System.out.print("B");   // separate if: also checked""")}
<p>Prints <code>AB</code>. With <code>else if</code> on the second line, it would print only <code>A</code>.</p>
{worked("What is printed when <code>score</code> is 70? When it's 69?", "70: 70 ≥ 90 false, 70 ≥ 80 false, 70 ≥ 70 true → <b>C</b>. 69: all three false → the else runs → <b>F</b>.")}
{box("trap", "Braces", "Without braces, an if controls only the next single statement. Indentation doesn't matter to Java.")}
''', pill=("e", "2.3–2.4"), sub="Choosing which code runs.",
 det=("Nested ifs and dangling else", '''<h4>Nested if statements</h4><p>An if inside another if runs only when both conditions hold. <code>if (a) { if (b) {...} }</code> behaves like <code>if (a &amp;&amp; b) {...}</code>, but nesting lets you add an else that applies only when a is true and b is false.</p>
<h4>Which if does an else belong to?</h4><p>Without braces, an else belongs to the nearest unmatched if above it, regardless of indentation. Exam questions sometimes indent code misleadingly to test this.</p>
<h4>Order matters in a chain</h4><p>In an else-if chain, put the most specific (narrowest) conditions first. If <code>score &gt;= 70</code> came first, a score of 95 would get a C.</p>'''))
jcheck('int x = 95;\nif (x > 90) System.out.print("A");\nif (x > 80) System.out.print("B");', "AB")
CH.append(chapter("selection-c2", "Selection", "if Statements", [REL, IF]))

# ---------------- compound booleans
jcheck('int x = 0;\nif (x != 0 && 10 / x > 1) System.out.println("big");\nelse System.out.println("safe");', "safe")
COMP = topic("compound-bool", "Compound boolean expressions", f'''
<div class="tblwrap"><table><tr><th>Operator</th><th>Name</th><th>True when</th></tr>
<tr><td><code>&amp;&amp;</code></td><td>and</td><td>both sides are true</td></tr>
<tr><td><code>||</code></td><td>or</td><td>at least one side is true</td></tr>
<tr><td><code>!</code></td><td>not</td><td>the expression is false</td></tr></table></div>
<p>Order: <code>!</code> first, then <code>&amp;&amp;</code>, then <code>||</code>. So <code>a || b &amp;&amp; c</code> means <code>a || (b &amp;&amp; c)</code>.</p>
{lab(type="bool", vars=["a", "b", "c"], exprs=["a && b", "a || b", "!a", "a || b && c", "(a || b) && c", "!(a && b)"])}
<h3>Short-circuit evaluation</h3>
<p>Java stops as soon as the answer is known. With <code>&amp;&amp;</code>, if the left side is false, the right side is never evaluated. With <code>||</code>, if the left side is true, the right side is skipped.</p>
{code('if (x != 0 && 10 / x > 1)   // safe: if x is 0, the division never happens')}
<p>This is how you guard against errors: check that something is safe <b>before</b> using it, on the left side of <code>&amp;&amp;</code>.</p>
''', pill=("e", "2.5"), sub="and, or, not, and short-circuiting.")
DEM = topic("demorgan", "Equivalent boolean expressions and De Morgan's laws", f'''
<div class="big-eq">!(a &amp;&amp; b) ≡ !a || !b &nbsp;&nbsp;&nbsp;&nbsp; !(a || b) ≡ !a &amp;&amp; !b</div>
<p>To push a <code>!</code> inside parentheses: negate each part and <b>flip</b> && and ||. Negating a comparison flips it: <code>!(x &lt; 5)</code> is <code>x &gt;= 5</code>, and <code>!(x == y)</code> is <code>x != y</code>.</p>
{lab(type="bool", vars=["a", "b"], exprs=["!(a && b)", "!a || !b", "!a && !b", "!(a || b)"], note="Flip a and b in every combination: the first two always match, and so do the last two.")}
{worked("Simplify <code>!(x &gt; 3 &amp;&amp; y &lt;= 10)</code>.", "Negate each part and flip &&: <code>!(x &gt; 3)</code> is <code>x &lt;= 3</code>, <code>!(y &lt;= 10)</code> is <code>y &gt; 10</code>. Result: <b><code>x &lt;= 3 || y &gt; 10</code></b>.")}
<p>To check whether two expressions are equivalent, use a truth table: try every combination of true and false and compare the results.</p>
{box("trap", "Common mistake", "Negating <code>x &lt; 5</code> as <code>x &gt; 5</code>. It's <code>x &gt;= 5</code>: the opposite of \"less than\" includes equal.")}
''', pill=("e", "2.6"), sub="Rewriting conditions without changing their meaning.",
 det=("Why De Morgan's laws work", '''<h4>In words</h4><p>"Not (raining and cold)" means at least one of them is false: not raining, or not cold. "Not (raining or cold)" means neither: not raining and not cold.</p>
<h4>Truth tables</h4><p>With two variables there are only 4 combinations (TT, TF, FT, FF). With three, 8. Writing them out is the most reliable way to check equivalence on the exam.</p>
<h4>Comparing objects</h4><p>Two references are equal with <code>==</code> only if they point to the same object. Two different String objects with the same characters are <code>equals</code> but not <code>==</code>. Use <code>equals</code> for content; use <code>== null</code> to check whether a reference points nowhere.</p>'''))
CH.append(chapter("logic-c2", "Boolean Logic", "Boolean Logic", [COMP, DEM]))

# ---------------- while loops
code_w = '''int num = 472;
int sum = 0;
while (num > 0)
{
    sum += num % 10;
    num /= 10;
}
System.out.println(sum);'''
t = Tr(code_w); num = 472; sm = 0; t.s(1, num=num).s(2, sum=sm)
while True:
    t.s(3)
    if not num > 0: break
    sm += num % 10; t.s(5, sum=sm); num //= 10; t.s(6, num=num)
t.s(8, out=str(sm))
jcheck(code_w, "13")
WHILE = topic("while-loops", "while loops", f'''
{code("""while (condition)
{
    // body: repeats as long as condition is true
}""")}
<p>Java checks the condition; if it's true, the body runs, then Java goes back and checks again. When the condition is false, the loop ends and the program continues after it. If the condition is false the first time, the body never runs.</p>
{anim(t.spec(ask="out"), "Adding the digits of 472. Step through and predict the printed sum", reveal=False)}
{worked("What does the code above print?", "Passes: sum 2 (num 47), sum 9 (num 4), sum 13 (num 0). num &gt; 0 is now false, so it prints <b>13</b>.")}
<h3>Infinite loops</h3><p>If nothing in the body moves the condition toward false, the loop never ends:</p>
{code("""int i = 0;
while (i < 10)
{
    System.out.println(i);   // forgot i++: prints 0 forever
}""")}
<h3>Sentinel and flag loops</h3><p>A loop can run until a special value appears (a sentinel) or until a boolean flag changes. That's useful when you don't know the number of passes in advance.</p>
''', pill=("m", "2.7"), sub="Repeat while a condition is true.",
 det=("Designing a while loop", '''<h4>Three parts</h4><p>Every loop needs (1) initialization before it, (2) a condition, and (3) an update inside the body that eventually makes the condition false. Missing the update is the usual cause of infinite loops.</p>
<h4>Off by one</h4><p>The most common loop bug is running one time too many or too few. Check the first pass and the last pass by hand: what is the variable's value when the body runs for the last time?</p>
<h4>Return inside a loop</h4><p>A <code>return</code> statement inside a loop ends the whole method immediately, which ends the loop too. This is common in search methods: return as soon as you find the answer, and return a "not found" value after the loop.</p>'''))

code_f = '''int total = 0;
for (int i = 1; i <= 4; i++)
{
    total += i * i;
}
System.out.println(total);'''
t = Tr(code_f); tot = 0; t.s(1, total=0)
i = 1; t.s(2, i=1)
while i <= 4:
    tot += i * i; t.s(4, total=tot); i += 1; t.s(2, i=i)
t.drop("i"); t.s(6, out=str(tot))
jcheck(code_f, "30")
FOR = topic("for-loops", "for loops", f'''
{code("""for (initialize; condition; update)
{
    body
}""")}
<p>A for loop puts the three parts of a counting loop on one line. The order is: initialize once, then check the condition, run the body, update, check again, and so on.</p>
{anim(t.spec(), "for (int i = 1; i <= 4; i++) adds 1 + 4 + 9 + 16")}
<p>The same loop as a while loop:</p>
{code("""int i = 1;
while (i <= 4)
{
    total += i * i;
    i++;
}""")}
{lab(type="loop", a=0, b=5, s=1)}
<h3>Counting passes</h3>
<ul><li><code>for (int i = 0; i &lt; n; i++)</code> runs <b>n</b> times (i = 0 … n−1).</li>
<li><code>for (int i = 1; i &lt;= n; i++)</code> runs <b>n</b> times (i = 1 … n).</li>
<li><code>for (int i = a; i &lt; b; i++)</code> runs <b>b − a</b> times; with <code>&lt;=</code>, <b>b − a + 1</b> times.</li></ul>
{box("trap", "Scope", "A variable declared in the for header (like <code>int i</code>) exists only inside the loop. Using i after the loop is a compile error.")}
''', pill=("m", "2.8"), sub="Counting loops in one line.")
CH.append(chapter("loops-c2", "while & for Loops", "Loops", [WHILE, FOR]))

# ---------------- algorithms
ALGS = '''public static int countMultiples(int n, int k)
{
    int count = 0;
    for (int i = 1; i <= n; i++)
    {
        if (i % k == 0)
            count++;
    }
    return count;
}'''
jcheck("System.out.println(countMultiples(20, 3));", "6", pre=ALGS)
code_m = '''int a = 4, b = 9, c = 2;
int max = a;
if (b > max)
    max = b;
if (c > max)
    max = c;
System.out.println(max);'''
t = Tr(code_m); t.s(1, a=4, b=9, c=2).s(2, max=4).s(3).s(4, max=9).s(5).s(7, out="9")
jcheck(code_m, "9")
ALG = topic("std-algorithms", "Standard algorithms with loops", f'''
<p>A handful of patterns cover most loop questions. Learn their shape and you can write them quickly in a free-response answer.</p>
<div class="grid2">
<div class="mini"><h4>Sum and average</h4><p>Start a total at 0, add each value, divide by the count at the end (as a double).</p></div>
<div class="mini"><h4>Count</h4><p>Start a counter at 0; inside the loop, <code>if (condition) count++;</code></p></div>
<div class="mini"><h4>Minimum / maximum</h4><p>Start with the first value (not 0), and replace it whenever you find a bigger (or smaller) one.</p></div>
<div class="mini"><h4>Divisibility and digits</h4><p><code>n % k == 0</code> tests divisibility; <code>n % 10</code> and <code>n / 10</code> take apart digits.</p></div></div>
{code(ALGS)}
{worked("What does <code>countMultiples(20, 3)</code> return?", "Multiples of 3 from 1 to 20: 3, 6, 9, 12, 15, 18. Returns <b>6</b>.")}
{anim(t.spec(), "Finding the largest of three values: start with the first and replace when bigger")}
{box("trap", "Common mistake", "Starting a maximum at 0. If all the values are negative, the answer would wrongly be 0. Start with the first value, or with Integer.MIN_VALUE.")}
''', pill=("m", "2.9"), sub="Sum, count, min/max, divisibility.",
 det=("Writing algorithms from a description", '''<h4>Start with the result variable</h4><p>Decide what the method returns, declare a variable for it, and give it a starting value that is correct if the loop never runs (0 for a count, true for "all", false for "any").</p>
<h4>"Any" vs "all"</h4><p>To check whether <b>any</b> value meets a condition, return true as soon as one does, and false after the loop. To check whether <b>all</b> do, return false as soon as one fails, and true after the loop.</p>
<h4>Averages</h4><p>Divide only after the loop, and avoid int division: <code>(double) sum / count</code>. If the count could be 0, check first.</p>'''))

STRALG = '''public static String reverse(String s)
{
    String result = "";
    for (int i = s.length() - 1; i >= 0; i--)
    {
        result += s.substring(i, i + 1);
    }
    return result;
}'''
COUNT = '''public static int countLetter(String s, String letter)
{
    int count = 0;
    for (int i = 0; i < s.length(); i++)
    {
        if (s.substring(i, i + 1).equals(letter))
            count++;
    }
    return count;
}'''
jcheck('System.out.println(reverse("stop"));\nSystem.out.println(countLetter("banana", "a"));', "pots 3", pre=STRALG + COUNT)
code_r = '''String s = "cat";
String result = "";
for (int i = s.length() - 1; i >= 0; i--)
{
    result += s.substring(i, i + 1);
}
System.out.println(result);'''
t = Tr(code_r); t.s(1, s="cat").s(2, result="")
res = ""; i = 2; t.s(3, i=2)
while i >= 0:
    res += "cat"[i]; t.s(5, result=res); i -= 1; t.s(3, i=i)
t.drop("i"); t.s(7, out="tac")
jcheck(code_r, "tac")
SALG = topic("string-algorithms", "String algorithms", f'''
<p>Loops over Strings visit each index from 0 to <code>length() - 1</code> and look at one character at a time with <code>substring(i, i + 1)</code>.</p>
{anim(t.spec(), "Reversing a String by walking backward through its indexes")}
{code(STRALG)}
{code(COUNT)}
{worked('What does <code>countLetter("banana", "a")</code> return?', "Indexes 1, 3 and 5 hold \"a\": returns <b>3</b>.")}
<h3>Finding a substring</h3><p>To check every position for a word of length k, the loop must stop at <code>s.length() - k</code>, so <code>substring(i, i + k)</code> never goes past the end:</p>
{code("""for (int i = 0; i <= s.length() - k; i++)
{
    if (s.substring(i, i + k).equals(word))
        ...
}""")}
{box("trap", "Common mistake", "<code>i &lt;= s.length()</code> with <code>substring(i, i + 1)</code> goes one past the end and throws StringIndexOutOfBoundsException on the last pass.")}
''', pill=("m", "2.10"), sub="Reverse, count, find and build Strings.")
CH.append(chapter("algorithms-c2", "Loop Algorithms", "Algorithms", [ALG, SALG]))

# ---------------- nested loops & run time
code_n = '''for (int r = 1; r <= 3; r++)
{
    for (int c = 1; c <= r; c++)
    {
        System.out.print("*");
    }
    System.out.println();
}'''
t = Tr(code_n); out = ""
r = 1; t.s(1, r=1)
while r <= 3:
    c = 1; t.s(3, c=1)
    while c <= r:
        t.s(5, out="*"); c += 1; t.s(3, c=c)
    t.drop("c"); t.s(7, out="\n"); r += 1; t.s(1, r=r)
jcheck(code_n, "* ** ***")
NEST = topic("nested-loops", "Nested iteration", f'''
<p>A loop inside a loop: for <b>each</b> pass of the outer loop, the inner loop runs <b>all</b> of its passes. The inner loop restarts from the beginning every time.</p>
{anim(t.spec(), "The inner loop's limit depends on r, so each row is one star longer")}
{outbox("*" + NL + "**" + NL + "***")}
<h3>Counting how many times the inner body runs</h3>
{anim({"type": "grid", "n": 4, "m": 5, "mode": "rect", "outer": "i", "inner": "j", "note": "4 outer passes × 5 inner = 20"}, "for (i = 0; i < 4; i++) for (j = 0; j < 5; j++): every cell is one inner pass")}
{anim({"type": "grid", "n": 5, "m": 5, "mode": "tri", "outer": "i", "inner": "j", "note": "0 + 1 + 2 + 3 + 4 = 10"}, "for (j = 0; j < i; j++): the inner loop grows with i, making a triangle")}
<div class="tblwrap"><table><tr><th>Inner loop</th><th>Inner body runs (outer i = 0 … n−1)</th></tr>
<tr><td><code>j &lt; m</code></td><td>n × m</td></tr>
<tr><td><code>j &lt; i</code></td><td>0 + 1 + … + (n−1) = n(n−1)/2</td></tr>
<tr><td><code>j &lt;= i</code></td><td>1 + 2 + … + n = n(n+1)/2</td></tr></table></div>
''', pill=("m", "2.11"), sub="Loops inside loops.")
jcheck('int count = 0;\nfor (int i = 0; i < 5; i++)\n  for (int j = 0; j < i; j++)\n    count++;\nSystem.out.println(count);', "10")
RUN = topic("run-time", "Informal run-time analysis", f'''
<p>A <b>statement execution count</b> is how many times a line runs. Comparing counts tells you which algorithm does less work, especially as the input size n grows.</p>
{worked("How many times does <code>count++</code> run?" + code('int count = 0;' + NL + 'for (int i = 0; i < 5; i++)' + NL + '    for (int j = 0; j < i; j++)' + NL + '        count++;'), "i = 0: 0 times; i = 1: 1; i = 2: 2; i = 3: 3; i = 4: 4. Total <b>10</b>.")}
<ul><li>One loop over n items: about <b>n</b> executions.</li>
<li>Two loops one after the other: about <b>2n</b>, still grows like n.</li>
<li>A loop nested inside another, each over n: about <b>n²</b>. Doubling n quadruples the work.</li></ul>
{box("tip", "Exam style", "Questions ask for an exact count for specific numbers, or which code segment runs a statement more times. Count the passes of each loop separately, then multiply (nested) or add (one after the other).")}
''', pill=("m", "2.12"), sub="Counting how many times code runs.")
CH.append(chapter("nested-c2", "Nested Loops & Run Time", "Nested Loops", [NEST, RUN]))

# ---------------- FRQ
FRQ1 = '''public static int longestRun(String s, String ch)
{
    int best = 0;
    int current = 0;
    for (int i = 0; i < s.length(); i++)
    {
        if (s.substring(i, i + 1).equals(ch))
        {
            current++;
            if (current > best)
                best = current;
        }
        else
        {
            current = 0;
        }
    }
    return best;
}'''
jcheck('System.out.println(longestRun("aabaaab", "a"));', "3", pre=FRQ1)
FRQ = topic("frq-c2", "Free response: methods and control structures", f'''
<p>Free-response question 1 gives you a scenario and asks you to write one or two methods using loops and if statements, often calling other methods that are described for you. A reliable process:</p>
<ol class="steps"><li>Read the header: what does it return, what are the parameters?</li>
<li>Work one example from the prompt by hand and notice what you're keeping track of.</li>
<li>Declare those variables, then write the loop, then the if statements, then the return.</li>
<li>Check the first and last loop passes for off-by-one errors.</li></ol>
{worked('Write <code>longestRun(s, ch)</code>: the length of the longest stretch of consecutive copies of the one-letter String ch in s. <code>longestRun("aabaaab", "a")</code> returns 3.', code(FRQ1) + "Keep the current run length, reset it when a different letter appears, and remember the best seen so far.")}
{box("tip", "Scoring", "Graders award points for each part of the algorithm: the loop visiting every element, the correct comparison, updating the right variables, and returning (not printing) the result. A working but slightly different approach still earns full credit.")}
''', sub="How Unit 2 shows up in free response.")
CH.append(chapter("frq-ch-c2", "Tracing & FRQs", "Tracing & FRQs", [FRQ]))
REV = topic("review-c2", "Patterns to know", '''<div class="tblwrap"><table><tr><th>Pattern</th><th>Shape</th></tr>
<tr><td>Visit every character</td><td><code>for (int i = 0; i &lt; s.length(); i++) … s.substring(i, i + 1)</code></td></tr>
<tr><td>Count matches</td><td><code>if (…) count++;</code> inside a loop</td></tr>
<tr><td>Running maximum</td><td><code>if (x &gt; max) max = x;</code></td></tr>
<tr><td>Digits of n</td><td><code>while (n &gt; 0) { digit = n % 10; n /= 10; }</code></td></tr>
<tr><td>Any match</td><td><code>if (…) return true;</code> in the loop, <code>return false;</code> after it</td></tr>
<tr><td>Passes of <code>for (i = a; i &lt; b; i++)</code></td><td>b − a</td></tr>
<tr><td>De Morgan</td><td><code>!(a &amp;&amp; b)</code> = <code>!a || !b</code>; <code>!(a || b)</code> = <code>!a &amp;&amp; !b</code></td></tr></table></div>''', sub="Quick review.")
MIS = topic("mistakes-c2", "Common mistakes", '''<ol class="steps">
<li>Off-by-one: <code>&lt;</code> vs <code>&lt;=</code>, starting at 0 vs 1.</li>
<li>Forgetting the update and writing an infinite loop.</li>
<li>Using separate ifs when only one branch should run (else if).</li>
<li>Negating <code>&lt;</code> as <code>&gt;</code> instead of <code>&gt;=</code>.</li>
<li>Putting the risky check before the guard: <code>10 / x &gt; 1 &amp;&amp; x != 0</code> crashes when x is 0.</li>
<li>Returning inside a loop too early ("return false" in the else of a search loop).</li>
<li>Comparing Strings with ==.</li></ol>''', sub="Points students lose most often.")
CH.append(chapter("review-ch-c2", "Review", "Review", [REV, MIS]))

# ---------------- questions
P = []
def add(text_code, opts, a, x, run, t="e", exp=None, err=None, pre="", sim=None, intro="What is printed?", k=None):
    P.append(q(f"{intro}{code(text_code)}", opts, a, x, t=t, run=run, exp=exp, err=err, pre=pre, sim=sim, k=k))
c1 = 'int x = 7;' + NL + 'if (x > 5)' + NL + '    System.out.print("A");' + NL + 'else if (x > 3)' + NL + '    System.out.print("B");' + NL + 'if (x > 6)' + NL + '    System.out.print("C");'
add(c1, O("AC", "A", "ABC", "AB"), 0, "x > 5 prints A and skips the else if. The last if is separate: 7 > 6 prints C.", c1)
c2 = 'int a = 3, b = 8;' + NL + 'if (a > b || b % a == 2)' + NL + '    System.out.println("yes");' + NL + 'else' + NL + '    System.out.println("no");'
add(c2, O("yes", "no", "yesno", "Nothing"), 0, "a > b is false, but 8 % 3 == 2 is true, so || is true.", c2)
P.append(q("Which is equivalent to <code>!(x &gt;= 10 || y == 0)</code>?", Oc("x < 10 && y != 0", "x < 10 || y != 0", "x <= 10 && y != 0", "x > 10 && y == 0"), 0, "De Morgan: negate each part and flip || to &&. !(x >= 10) is x < 10; !(y == 0) is y != 0."))
P.append(q("Which is equivalent to <code>!(a &amp;&amp; !b)</code>?", Oc("!a || b", "!a && b", "a || !b", "!a || !b"), 0, "Negate each: !a and !!b = b. Flip && to ||."))
c3 = 'int x = 0;' + NL + 'if (x == 0 || 10 / x > 2)' + NL + '    System.out.println("ok");'
add(c3, O("ok", "An ArithmeticException is thrown", "Nothing", "Compile error"), 0, "x == 0 is true, so || short-circuits and 10 / x never runs.", c3)
c4 = 'int x = 0;' + NL + 'if (10 / x > 2 || x == 0)' + NL + '    System.out.println("ok");'
add(c4, O("An ArithmeticException is thrown", "ok", "Nothing", "Compile error"), 0, "The left side runs first and divides by zero.", c4, err="runtime")
c5 = 'int n = 1;' + NL + 'while (n < 50)' + NL + '{' + NL + '    n *= 3;' + NL + '}' + NL + 'System.out.println(n);'
add(c5, O("81", "27", "54", "243"), 0, "1 → 3 → 9 → 27 → 81. 81 < 50 is false, so the loop stops.", c5, t="m")
c6 = 'int count = 0;' + NL + 'for (int i = 3; i < 15; i += 3)' + NL + '{' + NL + '    count++;' + NL + '}' + NL + 'System.out.println(count);'
add(c6, O("4", "5", "3", "12"), 0, "i = 3, 6, 9, 12; 15 fails the test. 4 passes.", c6, t="m")
c7 = 'for (int i = 10; i > 0; i -= 4)' + NL + '{' + NL + '    System.out.print(i + " ");' + NL + '}'
add(c7, O("10 6 2", "10 6 2 -2", "10 6", "6 2"), 0, "10, 6, 2; then −2 > 0 is false.", c7, t="m")
c8 = 'int sum = 0;' + NL + 'for (int k = 1; k <= 10; k++)' + NL + '{' + NL + '    if (k % 3 == 0)' + NL + '        sum += k;' + NL + '}' + NL + 'System.out.println(sum);'
add(c8, O("18", "15", "30", "9"), 0, "3 + 6 + 9 = 18.", c8, t="m")
P.append(q("How many times does the body of <code>for (int i = 5; i &lt;= 20; i++)</code> run?", O("16", "15", "20", "14"), 0, "With <=, the count is 20 − 5 + 1 = 16.", t="m", run='int c = 0;\nfor (int i = 5; i <= 20; i++) c++;\nSystem.out.println(c);', exp="16", sim=None))
c9 = 'int i = 0;' + NL + 'while (i < 5)' + NL + '{' + NL + '    i += 2;' + NL + '}' + NL + 'System.out.println(i);'
add(c9, O("6", "4", "5", "8"), 0, "0 → 2 → 4 → 6. 6 < 5 is false. The value after the loop is 6.", c9, t="m")
c10 = 'String s = "loops";' + NL + 'String r = "";' + NL + 'for (int i = 0; i < s.length(); i += 2)' + NL + '{' + NL + '    r += s.substring(i, i + 1);' + NL + '}' + NL + 'System.out.println(r);'
add(c10, O("lop", "los", "oo", "lp"), 0, "Indexes 0, 2, 4: l, o, s? Check: s = l0 o1 o2 p3 s4, so indexes 0, 2, 4 give l, o, s.", c10, t="m")
P[-1]["o"] = O("los", "lop", "oo", "lps"); P[-1]["x"] = "s is l(0) o(1) o(2) p(3) s(4). Indexes 0, 2, 4 give \"los\"."
c11 = 'String s = "abcabc";' + NL + 'int count = 0;' + NL + 'for (int i = 0; i < s.length() - 1; i++)' + NL + '{' + NL + '    if (s.substring(i, i + 2).equals("bc"))' + NL + '        count++;' + NL + '}' + NL + 'System.out.println(count);'
add(c11, O("2", "1", "3", "0"), 0, "\"bc\" starts at indexes 1 and 4.", c11, t="m")
c12 = 'String s = "hello";' + NL + 'for (int i = 0; i <= s.length(); i++)' + NL + '{' + NL + '    System.out.print(s.substring(i, i + 1));' + NL + '}'
add(c12, O("hello, then a StringIndexOutOfBoundsException", "hello", "hell", "Compile error"), 0, "When i = 5, substring(5, 6) is past the end. The five letters print first, then it crashes.", c12, t="m", err="runtime")
c13 = 'int count = 0;' + NL + 'for (int i = 0; i < 4; i++)' + NL + '    for (int j = 0; j < 3; j++)' + NL + '        count++;' + NL + 'System.out.println(count);'
add(c13, O("12", "7", "16", "9"), 0, "4 outer passes × 3 inner = 12.", c13, t="m", sim={"type": "grid", "n": 4, "m": 3, "mode": "rect", "ask": True})
c14 = 'int count = 0;' + NL + 'for (int i = 1; i <= 4; i++)' + NL + '    for (int j = 1; j <= i; j++)' + NL + '        count++;' + NL + 'System.out.println(count);'
add(c14, O("10", "16", "6", "4"), 0, "1 + 2 + 3 + 4 = 10.", c14, t="m", sim={"type": "grid", "n": 4, "m": 4, "mode": "tri2", "ask": True, "outer": "row", "inner": "col"})
c15 = 'for (int i = 1; i <= 3; i++)' + NL + '{' + NL + '    for (int j = i; j <= 3; j++)' + NL + '        System.out.print(j);' + NL + '    System.out.print(" ");' + NL + '}'
add(c15, O("123 23 3", "123 123 123", "1 12 123", "321 32 3"), 0, "Each row starts j at i: 123, then 23, then 3.", c15, t="m")
c16 = 'int n = 1234;' + NL + 'int count = 0;' + NL + 'while (n > 0)' + NL + '{' + NL + '    if (n % 2 == 0)' + NL + '        count++;' + NL + '    n /= 10;' + NL + '}' + NL + 'System.out.println(count);'
add(c16, O("2", "1", "4", "3"), 0, "Digits 4, 3, 2, 1. Even digits: 4 and 2.", c16, t="m")
c17 = 'int x = 10;' + NL + 'while (x != 0)' + NL + '{' + NL + '    x -= 3;' + NL + '}'
P.append(q(f"What happens when this runs?{code(c17)}", O("It never stops (infinite loop)", "It stops with x = 1", "It stops with x = 0", "It stops with x = -2"), 0, "x goes 10, 7, 4, 1, −2, −5, … and never equals 0 exactly.", t="m"))
P.append(q("Which loop header makes the body run exactly 10 times?", Oc("for (int i = 0; i < 10; i++)", "for (int i = 0; i <= 10; i++)", "for (int i = 1; i < 10; i++)", "for (int i = 10; i > 1; i--)"), 0, "i = 0 … 9 is 10 values. The others run 11, 9 and 9 times.", t="m"))
c18 = 'boolean found = false;' + NL + 'int i = 0;' + NL + 'String s = "carrot";' + NL + 'while (i < s.length() && !found)' + NL + '{' + NL + '    if (s.substring(i, i + 1).equals("r"))' + NL + '        found = true;' + NL + '    else' + NL + '        i++;' + NL + '}' + NL + 'System.out.println(i);'
add(c18, O("2", "3", "6", "4"), 0, "The loop stops when found becomes true at index 2 (c0 a1 r2). i isn't incremented on that pass.", c18, t="m")
c19 = 'int max = 0;' + NL + 'int[] unused = {};' + NL + 'int a = -5, b = -2, c = -9;' + NL + 'if (a > max) max = a;' + NL + 'if (b > max) max = b;' + NL + 'if (c > max) max = c;' + NL + 'System.out.println(max);'
c19 = 'int max = 0;' + NL + 'int a = -5, b = -2, c = -9;' + NL + 'if (a > max) max = a;' + NL + 'if (b > max) max = b;' + NL + 'if (c > max) max = c;' + NL + 'System.out.println(max);'
add(c19, O("0", "-2", "-5", "-9"), 0, "max starts at 0 and no value is bigger, so it prints 0, which isn't one of the values. That's why a maximum should start at the first value.", c19, t="m")
c20 = 'int a = 5;' + NL + 'boolean p = a > 3 && a < 10;' + NL + 'boolean r = !p || a == 5;' + NL + 'System.out.println(p + " " + r);'
add(c20, O("true true", "true false", "false true", "false false"), 0, "p: 5 > 3 && 5 < 10 is true. r: !p is false, but a == 5 is true, so r is true.", c20)
c21 = 'int x = 4, y = 7;' + NL + 'if (x > 2)' + NL + '    if (y > 10)' + NL + '        System.out.print("P");' + NL + '    else' + NL + '        System.out.print("Q");' + NL + 'System.out.print("R");'
add(c21, O("QR", "R", "PR", "PQR"), 0, "x > 2 is true; the inner if is false, so its else (the nearest unmatched if) prints Q. R always prints.", c21)
P.append(q("A loop runs <code>for (int i = 0; i &lt; n; i++)</code> and contains another loop <code>for (int j = 0; j &lt; n; j++)</code>. If n doubles, the number of times the inner body runs…", O("quadruples", "doubles", "stays the same", "increases by n"), 0, "The inner body runs n × n = n² times; (2n)² = 4n².", t="m"))
c22 = 'String word = "level";' + NL + 'boolean same = true;' + NL + 'int n = word.length();' + NL + 'for (int i = 0; i < n / 2; i++)' + NL + '{' + NL + '    if (!word.substring(i, i + 1).equals(word.substring(n - 1 - i, n - i)))' + NL + '        same = false;' + NL + '}' + NL + 'System.out.println(same);'
add(c22, O("true", "false", "An exception is thrown", "Compile error"), 0, "It compares mirrored letters (l/l, e/e). \"level\" is a palindrome.", c22, t="m")
c23 = 'int total = 0;' + NL + 'for (int i = 1; i < 6; i++)' + NL + '{' + NL + '    if (i % 2 == 0)' + NL + '        continue;' + NL + '    total += i;' + NL + '}' + NL + 'System.out.println(total);'
c23 = 'int total = 0;' + NL + 'for (int i = 1; i < 6; i++)' + NL + '{' + NL + '    if (i % 2 == 1)' + NL + '        total += i;' + NL + '}' + NL + 'System.out.println(total);'
add(c23, O("9", "15", "6", "5"), 0, "Odd i: 1 + 3 + 5 = 9.", c23, t="m")
c24 = 'int x = 15;' + NL + 'String r;' + NL + 'if (x % 3 == 0 && x % 5 == 0)' + NL + '    r = "FizzBuzz";' + NL + 'else if (x % 3 == 0)' + NL + '    r = "Fizz";' + NL + 'else' + NL + '    r = "" + x;' + NL + 'System.out.println(r);'
add(c24, O("FizzBuzz", "Fizz", "15", "FizzFizzBuzz"), 0, "15 is divisible by both 3 and 5, and that branch is checked first.", c24)
PQ = P

C = []
def addc(text_code, opts, a, x, run, t="m", exp=None, err=None, pre=""):
    C.append(q(f"What is printed?{code(text_code)}", opts, a, x, t=t, run=run, exp=exp, err=err, pre=pre))
d1 = 'int count = 0;' + NL + 'for (int i = 0; i < 5; i++)' + NL + '    for (int j = i; j < 5; j++)' + NL + '        count++;' + NL + 'System.out.println(count);'
addc(d1, O("15", "25", "10", "20"), 0, "j runs 5, 4, 3, 2, 1 times: 15.", d1)
d2 = 'int a = 1, b = 1;' + NL + 'while (b < 30)' + NL + '{' + NL + '    int temp = a + b;' + NL + '    a = b;' + NL + '    b = temp;' + NL + '}' + NL + 'System.out.println(a + " " + b);'
addc(d2, O("21 34", "13 21", "34 55", "21 30"), 0, "Fibonacci pairs: (1,2), (2,3), (3,5), (5,8), (8,13), (13,21), (21,34). 34 ≥ 30 ends it.", d2)
d3 = 'String s = "aXbXcX";' + NL + 'int i = s.indexOf("X");' + NL + 'while (i >= 0)' + NL + '{' + NL + '    s = s.substring(0, i) + s.substring(i + 1);' + NL + '    i = s.indexOf("X");' + NL + '}' + NL + 'System.out.println(s);'
addc(d3, O("abc", "aXbXc", "abcX", "Nothing; infinite loop"), 0, "Each pass removes the first X and searches again until none are left.", d3)
d4 = 'int x = 6;' + NL + 'int steps = 0;' + NL + 'while (x != 1)' + NL + '{' + NL + '    if (x % 2 == 0)' + NL + '        x /= 2;' + NL + '    else' + NL + '        x = 3 * x + 1;' + NL + '    steps++;' + NL + '}' + NL + 'System.out.println(steps);'
addc(d4, O("8", "7", "9", "6"), 0, "6, 3, 10, 5, 16, 8, 4, 2, 1: 8 steps.", d4)
C.append(q("For which values of x and y is <code>!(x &gt; 0 &amp;&amp; y &gt; 0) &amp;&amp; (x &gt; 0 || y &gt; 0)</code> true?", O("Exactly one of x, y is positive", "Both are positive", "Neither is positive", "At least one is positive"), 0, "The first part says not both; the second says at least one. Together: exactly one.", t="e"))
d5 = 'int count = 0;' + NL + 'for (int i = 1; i <= 16; i *= 2)' + NL + '    for (int j = 0; j < i; j++)' + NL + '        count++;' + NL + 'System.out.println(count);'
addc(d5, O("31", "16", "32", "80"), 0, "i = 1, 2, 4, 8, 16: total 1 + 2 + 4 + 8 + 16 = 31.", d5)
d6 = 'String s = "racecar";' + NL + 'String r = "";' + NL + 'for (int i = 0; i < s.length(); i++)' + NL + '{' + NL + '    String c = s.substring(i, i + 1);' + NL + '    if (r.indexOf(c) == -1)' + NL + '        r += c;' + NL + '}' + NL + 'System.out.println(r);'
addc(d6, O("race", "racecar", "rce", "ecar"), 0, "Each letter is added only the first time it appears: r, a, c, e.", d6)
d7 = 'int n = 0;' + NL + 'for (int i = 0; i < 3; i++)' + NL + '{' + NL + '    for (int j = 0; j < 3; j++)' + NL + '    {' + NL + '        if (i == j) continue;' + NL + '        n += i * j;' + NL + '    }' + NL + '}' + NL + 'System.out.println(n);'
d7 = 'int n = 0;' + NL + 'for (int i = 0; i < 3; i++)' + NL + '{' + NL + '    for (int j = 0; j < 3; j++)' + NL + '    {' + NL + '        if (i != j)' + NL + '            n += i * j;' + NL + '    }' + NL + '}' + NL + 'System.out.println(n);'
addc(d7, O("4", "5", "9", "2"), 0, "Pairs with i ≠ j: (0,1),(0,2),(1,0),(1,2),(2,0),(2,1). Products 0,0,0,2,0,2 = 4.", d7)
CHAL = C

E = []
def adde(text_code, opts, a, x, run, t="m", k="calc", exp=None, err=None):
    E.append(q(f"What is printed?{code(text_code)}", opts, a, x, t=t, run=run, k=k, exp=exp, err=err))
e1 = 'int x = 12;' + NL + 'if (x % 4 == 0)' + NL + '    x /= 4;' + NL + 'else if (x % 3 == 0)' + NL + '    x /= 3;' + NL + 'System.out.println(x);'
adde(e1, O("3", "4", "1", "12"), 0, "12 % 4 == 0, so x becomes 3 and the else if is skipped.", e1, t="e")
E.append(q("Which expression is true exactly when n is between 1 and 10 inclusive?", Oc("n >= 1 && n <= 10", "n >= 1 || n <= 10", "1 <= n <= 10", "!(n < 1 && n > 10)"), 0, "Both bounds must hold, so &&. 1 <= n <= 10 doesn't compile in Java; the last is always true.", t="e", k="concept"))
E.append(q("Which is equivalent to <code>!(a || b)</code>?", Oc("!a && !b", "!a || !b", "a && b", "!a || b"), 0, "De Morgan's law.", t="e", k="concept"))
e2 = 'int k = 2;' + NL + 'while (k < 40)' + NL + '{' + NL + '    k = k * k;' + NL + '}' + NL + 'System.out.println(k);'
adde(e2, O("256", "16", "40", "64"), 0, "2 → 4 → 16 → 256.", e2)
e3 = 'int s = 0;' + NL + 'for (int i = 2; i <= 8; i += 2)' + NL + '    s += i;' + NL + 'System.out.println(s);'
adde(e3, O("20", "12", "30", "14"), 0, "2 + 4 + 6 + 8 = 20.", e3)
e4 = 'String w = "Mississippi";' + NL + 'int n = 0;' + NL + 'for (int i = 0; i < w.length(); i++)' + NL + '    if (w.substring(i, i + 1).equals("s"))' + NL + '        n++;' + NL + 'System.out.println(n);'
adde(e4, O("4", "3", "2", "11"), 0, "Four lowercase s characters.", e4)
e5 = 'int c = 0;' + NL + 'for (int i = 0; i < 6; i++)' + NL + '    for (int j = 0; j < 2; j++)' + NL + '        c++;' + NL + 'System.out.println(c);'
adde(e5, O("12", "8", "6", "36"), 0, "6 × 2 = 12.", e5)
E.append(q(f"How many times is <code>System.out.print</code> called?{code('for (int i = 0; i < 4; i++)' + NL + '    for (int j = i; j < 4; j++)' + NL + '        System.out.print(\"*\");')}", O("10", "16", "4", "6"), 0, "j runs 4, 3, 2, 1 times: 10.", run='for (int i = 0; i < 4; i++)\n    for (int j = i; j < 4; j++)\n        System.out.print("*");', exp="**********", t="m", k="calc"))
e6 = 'int x = 3, y = 5;' + NL + 'if (x > y || y - x == 2 && x != 3)' + NL + '    System.out.println("T");' + NL + 'else' + NL + '    System.out.println("F");'
adde(e6, O("F", "T", "TF", "Compile error"), 0, "&& first: (2 == 2 && x != 3) is false. x > y is false. false || false is false.", e6, t="e")
e7 = 'String s = "abc";' + NL + 'String out = "";' + NL + 'for (int i = 0; i < s.length(); i++)' + NL + '    out = s.substring(i, i + 1) + out;' + NL + 'System.out.println(out);'
adde(e7, O("cba", "abc", "aabbcc", "cab"), 0, "Each letter is placed in front of the previous result, reversing the String.", e7)
e8 = 'int n = 0;' + NL + 'int i = 10;' + NL + 'while (i > 1)' + NL + '{' + NL + '    i /= 2;' + NL + '    n++;' + NL + '}' + NL + 'System.out.println(n);'
adde(e8, O("3", "4", "5", "2"), 0, "10 → 5 → 2 → 1: 3 passes.", e8)
E.append(q("What happens if a while loop's condition is false the first time it's checked?", O("The body never runs", "The body runs once", "An exception is thrown", "The loop runs forever"), 0, "The condition is checked before every pass, including the first.", t="m", k="concept"))
e9 = 'int a = 10;' + NL + 'boolean b = a % 3 == 1 && a / 3 == 3;' + NL + 'System.out.println(!b);'
adde(e9, O("false", "true", "1", "Compile error"), 0, "10 % 3 == 1 is true; 10 / 3 == 3 is true; b is true, so !b is false.", e9, t="e")
e10 = 'for (int i = 1; i <= 3; i++)' + NL + '{' + NL + '    for (int j = 1; j <= 3; j++)' + NL + '        if (j == i) System.out.print(i * j);' + NL + '}'
adde(e10, O("149", "123", "111", "369"), 0, "Only when j equals i: 1·1, 2·2, 3·3 → 1, 4, 9.", e10)
E.append(q("A method should return true if any character in s is a digit. The loop checks each character and does <code>return true;</code> when it finds one. Where should <code>return false;</code> go?", O("After the loop", "In an else inside the loop", "Before the loop", "It isn't needed"), 0, "Returning false inside the loop would stop after checking only the first character.", t="m", k="concept"))
FRQS = [
 {"q": f"Write a static method <code>countVowels</code> that returns how many characters of the String <code>s</code> are one of the lowercase vowels a, e, i, o, u. You may use the String <code>\"aeiou\"</code> and <code>indexOf</code>.{code('public static int countVowels(String s)')}",
  "parts": [{"p": "(a) Write the method.", "rubric": [["Loops over every index of s without going out of bounds", 1], ["Gets one character with substring(i, i + 1)", 1], ["Correctly tests whether it's a vowel (indexOf != -1 or five equals checks)", 1], ["Counts and returns the total", 1]],
   "answer": code('public static int countVowels(String s)\n{\n    int count = 0;\n    for (int i = 0; i < s.length(); i++)\n    {\n        if ("aeiou".indexOf(s.substring(i, i + 1)) != -1)\n            count++;\n    }\n    return count;\n}')}]},
 {"q": f"A number is \"balanced\" if the sum of its even digits equals the sum of its odd digits. Write <code>isBalanced</code> for a positive int n. For example, <code>isBalanced(1236)</code> is true (1 + 3 = 4, 2... no: 2 + 6 = 8) is false, while <code>isBalanced(132)</code> is true (1 + 3 = 4? no). Use: <code>isBalanced(325)</code> is false and <code>isBalanced(1342)</code> is true (1 + 3 = 4 = 4? even digits 4 + 2 = 6). See the model answer for exact examples.",
  "parts": []},
]
# replace the confusing second FRQ with a clean one
FRQS[1] = {"q": f"A number's <b>digit gap</b> is its largest digit minus its smallest digit. Write <code>digitGap</code> for a positive int n. For example, <code>digitGap(5291)</code> returns 8 (9 − 1) and <code>digitGap(7)</code> returns 0.{code('public static int digitGap(int n)')}",
  "parts": [{"p": "(a) Write the method.", "rubric": [["Loops over the digits using % 10 and / 10 until n is 0", 1], ["Initializes max and min correctly (first digit, or 0 and 9)", 1], ["Updates max and min correctly", 1], ["Returns max − min", 1]],
   "answer": code('public static int digitGap(int n)\n{\n    int max = n % 10;\n    int min = n % 10;\n    while (n > 0)\n    {\n        int d = n % 10;\n        if (d > max) max = d;\n        if (d < min) min = d;\n        n /= 10;\n    }\n    return max - min;\n}')}]}
jcheck('System.out.println(countVowels("education"));\nSystem.out.println(digitGap(5291) + " " + digitGap(7));', "5 8 0",
       pre='public static int countVowels(String s){int count=0;for(int i=0;i<s.length();i++){if("aeiou".indexOf(s.substring(i,i+1))!=-1)count++;}return count;}\npublic static int digitGap(int n){int max=n%10;int min=n%10;while(n>0){int d=n%10;if(d>max)max=d;if(d<min)min=d;n/=10;}return max-min;}')
EX = {"title": "Unit 2 Practice Exam: Selection and Iteration", "mcqMinutes": 30, "frqMinutes": 20, "tags": T2,
      "kinds": {"concept": "Concept", "calc": "Code tracing"}, "mcq": E, "frq": FRQS}

if __name__ == "__main__":
    assert verify({"practice": PQ, "challenge": CHAL, "exam": E}), "fix questions"
    balance(PQ, 21); balance(CHAL, 22); balance(E, 23)
    EX["mcq"] = strip_private(E)
    CH.append(chapter("practice-c2", "Practice Questions", "Practice", [quiz_section("practice-quiz-c2", "Practice questions", f"{len(PQ)} questions. Every code answer was checked by running it in Java.", "quiz-c2", T2)]))
    CH.append(chapter("challenge-c2", "Challenge Questions", "Challenge", [quiz_section("challenge-quiz-c2", "Challenge questions", "Long traces and logic traps. Turn off animated models in ⚙ Settings for a real exam feel.", "quiz-challenge-c2", T2)], hard=True))
    CH.append(chapter("exam-ch-c2", "Practice Exam", "Practice Exam", ['<section class="topic" id="exam-box-c2"><h2>Practice exam</h2><p class="sub">15 multiple-choice questions (30 minutes) and 2 free-response questions (20 minutes). No feedback until you submit.</p><div class="exam" data-src="exam-c2"></div></section>']))
    HTML = page("unit-2", "AP CSA Unit 2: Selection and Iteration", "AP Computer Science A · Unit 2",
                'Selection<br><span class="hl">and Iteration</span>',
                f"Boolean expressions, if statements, De Morgan's laws, while and for loops, standard algorithms, String algorithms, nested loops and run-time analysis: explanations, code you can step through, interactive labs, {len(PQ) + len(CHAL)} practice questions checked in Java, and a timed practice exam.",
                "AP Computer Science A Unit 2 review with code animations, interactive labs, practice questions and a practice exam.",
                CH, {"quiz-c2": strip_private(PQ), "quiz-challenge-c2": strip_private(CHAL), "exam-c2": EX},
                course="ap-csa", footer="Crux · AP Computer Science A · Java", extra_js=("cs-sims.js",))
    open("/home/claude/ap-physics-study/courses/ap-csa/unit-2.html", "w").write(HTML)
    print("CSA unit 2 written:", len(PQ), len(CHAL), len(E))
