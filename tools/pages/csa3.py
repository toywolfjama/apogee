from gen_unit import topic, chapter, worked, box, detailed, quiz_section, page
from cs_common import *

T3 = {"e": "Writing Classes", "m": "References & static"}
CH = []
def O(*xs): return [esc(x) for x in xs]
def Oc(*xs): return [ic(x) for x in xs]
NL = chr(10)

ACCOUNT = '''public class BankAccount
{
    private String owner;
    private double balance;

    public BankAccount(String name, double start)
    {
        owner = name;
        balance = start;
    }

    public double getBalance()
    {
        return balance;
    }

    public void deposit(double amount)
    {
        if (amount > 0)
            balance += amount;
    }

    public boolean withdraw(double amount)
    {
        if (amount > balance)
            return false;
        balance -= amount;
        return true;
    }

    public String toString()
    {
        return owner + ": $" + balance;
    }
}'''
ACC_NOPUB = ACCOUNT.replace("public class BankAccount", "class BankAccount")
jcheck('BankAccount a = new BankAccount("Ana", 50.0);\na.deposit(25.0);\nboolean ok = a.withdraw(100.0);\nSystem.out.println(ok + " " + a);', "false Ana: $75.0", cls=ACC_NOPUB)

HOW = '''<ol class="steps">
<li>Start with <b>Anatomy of a Class</b>: every later topic builds on it.</li>
<li>Memory animations show what happens inside the computer when objects are created and passed to methods. Use <b>Step ▶</b>.</li>
<li>Free-response question 2 asks you to write a whole class. The <b>Class FRQ</b> chapter walks through one.</li>
<li>Then <b>Practice</b>, <b>Challenge</b> and the timed <b>Practice Exam</b>.</li></ol>'''
mem0 = {"type": "memory", "frames": [
  {"note": 'BankAccount a = new BankAccount("Ana", 50.0);  the constructor fills in the new object\'s instance variables.', "vars": [["a", "BankAccount", "@x"]], "objs": [["x", "BankAccount", [["owner", '"Ana"'], ["balance", 50.0]]]]},
  {"note": "a.deposit(25.0);  the method changes this object's balance.", "vars": [["a", "BankAccount", "@x"]], "objs": [["x", "BankAccount", [["owner", '"Ana"'], ["balance", 75.0]]]]},
  {"note": "a.withdraw(100.0) returns false: 100 > 75, so balance doesn't change.", "vars": [["a", "BankAccount", "@x"], ["ok", "boolean", "false"]], "objs": [["x", "BankAccount", [["owner", '"Ana"'], ["balance", 75.0]]]]}]}
CORE = f'''<p>In Units 1 and 2 you used classes other people wrote. In Unit 3 you write your own: you decide what data each object stores (<b>instance variables</b>), how objects are set up (<b>constructors</b>), and what they can do (<b>methods</b>).</p>
{anim(mem0, "One BankAccount object: its data lives inside the object")}
<div class="grid2"><div class="mini"><h4>Exam weight</h4><p>Unit 3 is 10–18% of the multiple choice, and free-response question 2 (Class Design) asks you to write a complete class every year.</p></div>
<div class="mini"><h4>The main skill</h4><p>Turning a description ("each account has an owner and a balance; you can deposit…") into instance variables, a constructor and methods.</p></div></div>'''
CH.append(chapter("overview-c3", "Overview", "Overview", [topic("core-c3", "Core ideas", CORE)]))

# ------------- design
DESIGN = topic("abstraction", "Abstraction and program design", f'''
<p><b>Abstraction</b> means hiding details so you can think about the big picture. A class is an abstraction: someone using <code>BankAccount</code> calls <code>deposit</code> without knowing how the balance is stored. Methods are abstractions too: write a task once, give it a name, and call it wherever it's needed.</p>
<h3>Designing a class from a description</h3>
<ol class="steps"><li><b>Nouns</b> describing what each object knows become instance variables ("an owner", "a balance").</li>
<li><b>Verbs</b> describing what it does become methods ("deposit", "withdraw").</li>
<li>What must be known when an object is made becomes constructor parameters.</li></ol>
<p>Designers often sketch this as a <b>class diagram</b>: class name, then attributes, then methods.</p>
<div class="tblwrap"><table><tr><th>BankAccount</th></tr><tr><td><code>- owner : String</code><br><code>- balance : double</code></td></tr><tr><td><code>+ BankAccount(name : String, start : double)</code><br><code>+ getBalance() : double</code><br><code>+ deposit(amount : double) : void</code><br><code>+ withdraw(amount : double) : boolean</code></td></tr></table></div>
<p>(− means private, + means public.)</p>
''', pill=("e", "3.1"), sub="Deciding what a class should know and do.")
IMPACT = topic("impact", "Impact of program design", '''
<p>Programs affect people. The AP framework expects you to consider:</p>
<div class="grid2"><div class="mini"><h4>System reliability</h4><p>Testing with many inputs, including edge cases, reduces bugs that could harm users.</p></div>
<div class="mini"><h4>Privacy</h4><p>Collecting personal data creates responsibility to protect it and use it only as users expect.</p></div>
<div class="mini"><h4>Intellectual property</h4><p>Code, libraries and media are owned by their creators. Licenses say how they can be used; using someone's work without permission can be illegal.</p></div>
<div class="mini"><h4>Legal and ethical effects</h4><p>Software can have unintended consequences, such as bias in automated decisions or excluding users with disabilities.</p></div></div>''', pill=("e", "3.2"), sub="Reliability, privacy, ownership and ethics.")
CH.append(chapter("design-c3", "Abstraction & Design", "Design", [DESIGN, IMPACT]))

# ------------- anatomy
ANAT = topic("anatomy", "Anatomy of a class", f'''
{code(ACCOUNT)}
<div class="tblwrap"><table><tr><th>Part</th><th>In the example</th><th>Purpose</th></tr>
<tr><td>Instance variables</td><td><code>private String owner;</code> <code>private double balance;</code></td><td>Each object's own data</td></tr>
<tr><td>Constructor</td><td><code>public BankAccount(String name, double start)</code></td><td>Sets the starting values; same name as the class, no return type</td></tr>
<tr><td>Accessor (getter)</td><td><code>getBalance()</code></td><td>Returns information without changing the object</td></tr>
<tr><td>Mutator (setter)</td><td><code>deposit</code>, <code>withdraw</code></td><td>Changes the object's state</td></tr>
<tr><td><code>toString</code></td><td>returns <code>"Ana: $75.0"</code></td><td>Called automatically when the object is printed or joined to a String</td></tr></table></div>
{lab(type="object", cls="BankAccount", var="a", ctor='new BankAccount("Ana", 50.0)', dbl=True, fields={"owner": '"Ana"', "balance": 50.0},
  methods=[{"sig": "deposit(double amount)", "ret": "void", "params": ["amount"], "defaults": {"amount": 25}, "body": "if (amount > 0) f.balance += amount;"},
           {"sig": "withdraw(double amount)", "ret": "boolean", "params": ["amount"], "defaults": {"amount": 100}, "body": "if (amount > f.balance) return false; f.balance -= amount; return true;"},
           {"sig": "getBalance()", "ret": "double", "params": [], "body": "return f.balance;"},
           {"sig": "toString()", "ret": "String", "params": [], "body": "return f.owner.replace(/\"/g, '') + ': $' + f.balance.toFixed(1);"}])}
<h3>Encapsulation: private data, public methods</h3>
<p>Instance variables are <code>private</code>: code outside the class can't touch them directly (<code>a.balance = 1000000;</code> is a compile error). Outside code must go through public methods, which can check that changes make sense (deposit ignores negative amounts). This is <b>encapsulation</b>, and on the exam, instance variables should always be private.</p>
{box("trap", "Common mistake", "Re-declaring an instance variable inside the constructor: <code>double balance = start;</code> creates a new local variable and leaves the instance variable at 0.0. Write <code>balance = start;</code>.")}
''', pill=("e", "3.3"), sub="Instance variables, constructors, methods.",
 det=("Access modifiers and what each part may do", '''<h4>private vs public</h4><p><code>private</code> members are visible only inside the class's own code, including in other objects of the same class. <code>public</code> members are visible everywhere. Classes and constructors are normally public; helper methods used only inside the class can be private.</p>
<h4>Why encapsulate?</h4><p>If every class could change a balance directly, you'd have no single place to enforce rules like "no negative deposits". Encapsulation also lets you change how data is stored later without breaking the code that uses the class.</p>
<h4>Default values</h4><p>An instance variable that the constructor doesn't set keeps its default: 0, 0.0, false or null. A local variable has no default and must be assigned before use.</p>'''))

POINT2 = '''class Counter
{
    private int count;
    private int step;

    public Counter()
    {
        count = 0;
        step = 1;
    }

    public Counter(int start, int step)
    {
        count = start;
        this.step = step;
    }

    public void click() { count += step; }
    public int getCount() { return count; }
}'''
jcheck('Counter a = new Counter();\nCounter b = new Counter(10, 5);\na.click(); b.click(); b.click();\nSystem.out.println(a.getCount() + " " + b.getCount());', "1 20", cls=POINT2)
CT = Tr("""public Counter(int start, int step)
{
    count = start;
    this.step = step;
}
public void click() { count += step; }

Counter b = new Counter(10, 5);
b.click();
b.click();
System.out.println(b.getCount());""", title="Counter class + calling code")
CT.s(8).s(1, start=10, step=5).s(3, **{"this.count": 10}).s(4, **{"this.step": 5}).s(5)
CT.drop("start", "step", "this.count", "this.step"); CT.s(8, b="@→ new Counter")
CT.s(9, **{"b.count": 10, "b.step": 5}).s(6, **{"b.count": 15}).s(10).s(6, **{"b.count": 20}).s(11, out="20")
jcheck("Counter b = new Counter(10, 5);\nb.click();\nb.click();\nSystem.out.println(b.getCount());", "20", cls=POINT2)
CTOR = topic("constructors", "Constructors", f'''
<p>A constructor runs once, when <code>new</code> creates an object. Its job is to give every instance variable a sensible starting value.</p>
{code(POINT2)}
{code("Counter a = new Counter();          // uses the no-parameter constructor\nCounter b = new Counter(10, 5);     // uses the two-parameter constructor\na.click(); b.click(); b.click();\nSystem.out.println(a.getCount() + \" \" + b.getCount());")}
{outbox("1 20")}
{anim(CT.spec(), "Step into the constructor: new runs it, then the reference is stored in b")}
<ul><li>A constructor has the <b>same name as the class</b> and <b>no return type</b> (not even void).</li>
<li>A class can have several constructors with different parameter lists (overloading).</li>
<li>If you write no constructor, Java provides a default one with no parameters that leaves every instance variable at its default value. Once you write any constructor, that default one is no longer provided.</li></ul>
{box("trap", "Mutable objects as parameters", "If a constructor receives an object that can be changed (like another class's object) and just stores the reference, the outside code still has an alias to it. To be safe, store a copy.")}
''', pill=("e", "3.4"), sub="Setting up a new object.")
CH.append(chapter("anatomy-c3", "Anatomy & Constructors", "Classes", [ANAT, CTOR]))

# ------------- methods
RECT = '''class Rectangle
{
    private int width;
    private int height;

    public Rectangle(int w, int h)
    {
        width = w;
        height = h;
    }

    public int area()
    {
        return width * height;
    }

    public boolean isSquare()
    {
        return width == height;
    }

    public void scale(int factor)
    {
        width *= factor;
        height *= factor;
    }

    public String toString()
    {
        return width + "x" + height;
    }
}'''
jcheck('Rectangle r = new Rectangle(2, 3);\nSystem.out.println(r.area() + " " + r.isSquare());\nr.scale(2);\nSystem.out.println(r);', "6 false 4x6", cls=RECT)
METH = topic("writing-methods", "Writing methods", f'''
{code(RECT)}
<div class="grid3"><div class="mini"><h4>Return a value</h4><p><code>area()</code> computes and returns an int. A non-void method must return a value of its declared type on every path.</p></div>
<div class="mini"><h4>Return a boolean</h4><p><code>return width == height;</code> returns the comparison directly; no if needed.</p></div>
<div class="mini"><h4>void mutator</h4><p><code>scale</code> changes the instance variables and returns nothing.</p></div></div>
{code('Rectangle r = new Rectangle(2, 3);\nSystem.out.println(r.area() + " " + r.isSquare());\nr.scale(2);\nSystem.out.println(r);    // calls toString automatically')}
{outbox("6 false" + NL + "4x6")}
{lab(type="object", cls="Rectangle", var="r", ctor="new Rectangle(2, 3)", fields={"width": 2, "height": 3},
  methods=[{"sig": "area()", "ret": "int", "params": [], "body": "return f.width * f.height;"},
           {"sig": "isSquare()", "ret": "boolean", "params": [], "body": "return f.width === f.height;"},
           {"sig": "scale(int factor)", "ret": "void", "params": ["factor"], "defaults": {"factor": 2}, "body": "f.width *= Math.trunc(factor); f.height *= Math.trunc(factor);"},
           {"sig": "toString()", "ret": "String", "params": [], "body": "return f.width + 'x' + f.height;"}])}
<p>A <code>return</code> statement ends the method immediately. Code after a return on the same path never runs (the compiler reports it as unreachable).</p>
{box("trap", "Print vs return", "If the method says it returns a value, return it. Printing inside the method instead of returning loses free-response points.")}
''', pill=("e", "3.5"), sub="Accessors, mutators, toString and return values.",
 det=("Parameters, local variables and return paths", '''<h4>Parameters are local variables</h4><p>A method's parameters exist only while the method runs. They're initialized with copies of the arguments.</p>
<h4>Every path must return</h4><p><code>if (x &gt; 0) return 1;</code> alone doesn't compile in a method that returns int, because when x ≤ 0 nothing is returned. Add an else or a final return.</p>
<h4>Calling other methods of the same class</h4><p>Inside a class, a method can call another instance method by name alone: <code>if (isSquare()) …</code> calls it on the same object.</p>'''))

SWAP = '''public static void change(int n, Rectangle r)
{
    n = 99;
    r.scale(10);
    r = new Rectangle(1, 1);
}'''
jcheck('int x = 5;\nRectangle box = new Rectangle(2, 3);\nchange(x, box);\nSystem.out.println(x + " " + box);', "5 20x30", cls=RECT, pre=SWAP)
mem1 = {"type": "memory", "frames": [
  {"note": "Before the call: x = 5 and box refers to a 2x3 Rectangle.", "vars": [["x", "int", 5], ["box", "Rectangle", "@a"]], "objs": [["a", "Rectangle", [["width", 2], ["height", 3]]]]},
  {"note": "change(x, box): n gets a copy of 5; r gets a copy of the reference, so r and box point to the same object.", "vars": [["x", "int", 5], ["box", "Rectangle", "@a"], ["n", "int", 5], ["r", "Rectangle", "@a"]], "objs": [["a", "Rectangle", [["width", 2], ["height", 3]]]]},
  {"note": "n = 99 changes only the copy. x is still 5.", "vars": [["x", "int", 5], ["box", "Rectangle", "@a"], ["n", "int", 99], ["r", "Rectangle", "@a"]], "objs": [["a", "Rectangle", [["width", 2], ["height", 3]]]]},
  {"note": "r.scale(10) changes the shared object, which box also sees.", "vars": [["x", "int", 5], ["box", "Rectangle", "@a"], ["n", "int", 99], ["r", "Rectangle", "@a"]], "objs": [["a", "Rectangle", [["width", 20], ["height", 30]]]]},
  {"note": "r = new Rectangle(1, 1) points r somewhere else. box is not affected.", "vars": [["x", "int", 5], ["box", "Rectangle", "@a"], ["n", "int", 99], ["r", "Rectangle", "@b"]], "objs": [["a", "Rectangle", [["width", 20], ["height", 30]]], ["b", "Rectangle", [["width", 1], ["height", 1]]]]},
  {"note": "After the method returns, n and r disappear. Printed: 5 20x30", "vars": [["x", "int", 5], ["box", "Rectangle", "@a"]], "objs": [["a", "Rectangle", [["width", 20], ["height", 30]]]]}]}
REFS = topic("passing-refs", "Passing and returning object references", f'''
<p>Java always passes <b>copies</b>. For a primitive, it copies the value. For an object, it copies the <b>reference</b>, so the method gets a second arrow to the same object.</p>
{code(SWAP)}
{code('int x = 5;\nRectangle box = new Rectangle(2, 3);\nchange(x, box);\nSystem.out.println(x + " " + box);')}
{anim(mem1, "What changes and what doesn't when a method receives a primitive and a reference")}
{outbox("5 20x30")}
<div class="grid3"><div class="mini"><h4>Changing a primitive parameter</h4><p>No effect on the caller.</p></div>
<div class="mini"><h4>Calling a mutator on an object parameter</h4><p>The caller sees the change: same object.</p></div>
<div class="mini"><h4>Reassigning an object parameter</h4><p>No effect on the caller's variable.</p></div></div>
<h3>Returning references</h3><p>A method that returns an instance variable that refers to a changeable object lets outside code change the object's insides. Accessors should return primitives, Strings (which can't change) or copies.</p>
''', pill=("m", "3.6"), sub="Copies of values and copies of references.",
 det=("Objects of the same class", '''<h4>Private access across objects</h4><p>Inside a class's methods, you can access the private variables of <b>any</b> object of that class, not just <code>this</code>. That's how methods like <code>equals</code> or <code>isBiggerThan(Rectangle other)</code> compare: <code>return area() &gt; other.width * other.height;</code></p>
<h4>Methods that build new objects</h4><p>A method can create and return a new object: <code>public Rectangle doubled() { return new Rectangle(width * 2, height * 2); }</code>. The original is unchanged.</p>'''))
CH.append(chapter("methods-c3", "Methods & References", "Methods", [METH, REFS]))

# ------------- static, scope, this
STAT = '''class Student
{
    private static int nextId = 1;
    private String name;
    private int id;

    public Student(String name)
    {
        this.name = name;
        id = nextId;
        nextId++;
    }

    public int getId() { return id; }
    public static int getNextId() { return nextId; }
}'''
jcheck('Student a = new Student("Ana");\nStudent b = new Student("Ben");\nSystem.out.println(a.getId() + " " + b.getId() + " " + Student.getNextId());', "1 2 3", cls=STAT)
mem2 = {"type": "memory", "frames": [
  {"note": "static int nextId belongs to the class itself: there's only one, shared by every Student.", "vars": [["Student.nextId", "static int", 1]], "objs": []},
  {"note": 'new Student("Ana") gets id 1, then nextId becomes 2.', "vars": [["Student.nextId", "static int", 2], ["a", "Student", "@p"]], "objs": [["p", "Student", [["name", '"Ana"'], ["id", 1]]]]},
  {"note": 'new Student("Ben") gets id 2, then nextId becomes 3. Each object has its own name and id.', "vars": [["Student.nextId", "static int", 3], ["a", "Student", "@p"], ["b", "Student", "@q"]], "objs": [["p", "Student", [["name", '"Ana"'], ["id", 1]]], ["q", "Student", [["name", '"Ben"'], ["id", 2]]]]}]}
STATIC = topic("static", "Class variables and class methods", f'''
<p>A <code>static</code> variable belongs to the class, not to any one object. There is exactly one copy, shared by all objects. A <code>static</code> method belongs to the class too and is called with the class name.</p>
{code(STAT)}
{anim(mem2, "One shared static variable, separate instance variables per object")}
{lab(type="object", cls="Student (static nextId shown too)", var="Student", ctor="(reset class)", priv=False, fields={"static nextId": 1, "students made": 0},
  methods=[{"sig": "new Student(String name)", "label": 'new Student("Sam")', "note": "made a student with id", "ret": "creates an object", "params": [], "body": "f['students made']++; const id = f['static nextId']; f['static nextId']++; return id;"},
           {"sig": "getNextId()", "label": "Student.getNextId()", "ret": "static int", "params": [], "body": "return f['static nextId'];"}])}
{code('Student a = new Student("Ana");\nStudent b = new Student("Ben");\nSystem.out.println(a.getId() + " " + b.getId() + " " + Student.getNextId());')}
{outbox("1 2 3")}
<ul><li>Static methods can use static variables and other static methods.</li>
<li>Static methods <b>can't</b> use instance variables or <code>this</code> directly: there's no particular object.</li>
<li>Instance methods can use both instance and static variables.</li></ul>
''', pill=("m", "3.7"), sub="static: one shared copy for the whole class.")
SHADOW = '''class Temp
{
    private int value = 10;

    public void show()
    {
        int value = 3;
        System.out.println(value + " " + this.value);
    }
}'''
jcheck('new Temp().show();', "3 10", cls=SHADOW)
SH = Tr("""private int value = 10;

public void show()
{
    int value = 3;
    System.out.println(value + " " + this.value);
}""", title="Inside class Temp")
SH.s(1, **{"this.value": 10}).s(3).s(5, value=3).s(6, out="3 10").s(7)
SCOPE = topic("scope-this", "Scope, access and the this keyword", f'''
<p>A variable's <b>scope</b> is the part of the program where it can be used.</p>
<div class="tblwrap"><table><tr><th>Kind</th><th>Declared</th><th>Can be used</th></tr>
<tr><td>Instance variable</td><td>in the class, outside methods</td><td>in every instance method of the class</td></tr>
<tr><td>Parameter</td><td>in a method header</td><td>only inside that method</td></tr>
<tr><td>Local variable</td><td>inside a method or block</td><td>from its declaration to the end of its block (<code>{{ }}</code>)</td></tr></table></div>
<p>If a local variable or parameter has the same name as an instance variable, the local one <b>shadows</b> it: the plain name means the local variable.</p>
{code(SHADOW)}
{anim(SH.spec(), "Two variables named value: the local one wins unless you write this.value")}
{outbox("3 10")}
<h3>this</h3>
<p>Inside an instance method or constructor, <code>this</code> refers to the object the method was called on. Uses:</p>
<ul><li>Telling a shadowed instance variable apart: <code>this.name = name;</code></li>
<li>Passing the current object to another method: <code>other.compareWith(this);</code></li></ul>
{box("trap", "Common mistake", "Writing <code>name = name;</code> in a constructor whose parameter is also called name. That assigns the parameter to itself, and the instance variable stays null. Use <code>this.name = name;</code>.")}
''', pill=("m", "3.8–3.9"), sub="Where variables exist, and the current object.")
CH.append(chapter("static-c3", "static, Scope & this", "static & this", [STATIC, SCOPE]))

# ------------- FRQ2
TICKET = '''public class TicketBooth
{
    private int capacity;
    private int sold;
    private double price;

    public TicketBooth(int capacity, double price)
    {
        this.capacity = capacity;
        this.price = price;
        sold = 0;
    }

    /** Sells n tickets if enough are left; returns the cost, or 0.0 if not enough */
    public double buy(int n)
    {
        if (sold + n > capacity)
            return 0.0;
        sold += n;
        return n * price;
    }

    public int ticketsLeft()
    {
        return capacity - sold;
    }
}'''
jcheck('TicketBooth t = new TicketBooth(100, 12.5);\nSystem.out.println(t.buy(4) + " " + t.buy(97) + " " + t.ticketsLeft());', "50.0 0.0 96", cls=TICKET.replace("public class", "class"))
FRQ = topic("frq-c3", "Free response 2: class design", f'''
<p>You get a description and example calls, and you write the entire class. Use the example calls to find the constructor parameters and every method header.</p>
<div class="box plain"><b class="lbl">Prompt</b>A <code>TicketBooth</code> is created with a capacity and a ticket price. <code>buy(n)</code> sells n tickets if that many are left and returns the total cost; otherwise it sells nothing and returns 0.0. <code>ticketsLeft()</code> returns how many can still be sold.
{code('TicketBooth t = new TicketBooth(100, 12.5);' + NL + 't.buy(4);          // returns 50.0' + NL + 't.buy(97);         // returns 0.0 (only 96 left)' + NL + 't.ticketsLeft();   // returns 96')}</div>
{worked("Write the TicketBooth class.", code(TICKET))}
<h3>Checklist graders use</h3>
<ol class="steps"><li>Class header and private instance variables for everything the object must remember (including things not passed in, like <code>sold</code>).</li>
<li>Constructor with the right parameters that initializes every instance variable.</li>
<li>Each method header matches the example calls (name, parameter types, return type).</li>
<li>Each method's logic: checks, updates to the state, and correct return values.</li></ol>
{box("tip", "Think about state", "Ask: what must each object remember between method calls? Every such value needs an instance variable. Values that are only needed during one call should be local variables.")}
''', sub="Writing a complete class from a description.")
CH.append(chapter("frq-ch-c3", "Class FRQ", "Class FRQ", [FRQ]))
REV = topic("review-c3", "Class checklist", '''<div class="tblwrap"><table><tr><th>Rule</th><th>Example</th></tr>
<tr><td>Instance variables are private</td><td><code>private int count;</code></td></tr>
<tr><td>Constructor: class name, no return type</td><td><code>public Counter(int start)</code></td></tr>
<tr><td>Set instance variables, don't redeclare them</td><td><code>count = start;</code> not <code>int count = start;</code></td></tr>
<tr><td>Shadowed names need this</td><td><code>this.count = count;</code></td></tr>
<tr><td>Accessor returns, doesn't change state</td><td><code>public int getCount() { return count; }</code></td></tr>
<tr><td>Mutator is usually void</td><td><code>public void reset() { count = 0; }</code></td></tr>
<tr><td>toString returns a String</td><td><code>public String toString() { return "Count: " + count; }</code></td></tr>
<tr><td>static = shared by the class</td><td><code>private static int total;</code>, called as <code>ClassName.method()</code></td></tr></table></div>''', sub="Quick review.")
MIS = topic("mistakes-c3", "Common mistakes", '''<ol class="steps">
<li>Giving a constructor a return type (<code>public void Counter()</code> is a method, not a constructor).</li>
<li>Redeclaring instance variables as locals in the constructor.</li>
<li><code>name = name;</code> instead of <code>this.name = name;</code></li>
<li>Making instance variables public.</li>
<li>Using an instance variable inside a static method.</li>
<li>Thinking a method can change a caller's primitive variable or make the caller's reference point elsewhere.</li>
<li>Forgetting an instance variable for something the object must remember between calls.</li></ol>''', sub="Points students lose most often.")
CH.append(chapter("review-ch-c3", "Review", "Review", [REV, MIS]))

# ------------- questions
P = []
def addq(intro, snippet, opts, a, x, run, t="e", cls="", pre="", exp=None, err=None, sim=None, k=None, extra=""):
    P.append(q(f"{intro}{extra}{code(snippet) if snippet else ''}", opts, a, x, t=t, run=run, cls=cls, pre=pre, exp=exp, err=err, sim=sim, k=k))
RECT_NP = RECT
addq("Given the <code>Rectangle</code> class from this page, what is printed?", 'Rectangle r = new Rectangle(3, 4);' + NL + 'r.scale(2);' + NL + 'System.out.println(r.area());', O("48", "24", "12", "96"), 0, "After scale(2), it's 6x8 = 48.", 'Rectangle r = new Rectangle(3, 4);\nr.scale(2);\nSystem.out.println(r.area());', cls=RECT_NP)
addq("Given the <code>Rectangle</code> class, what is printed?", 'Rectangle r = new Rectangle(5, 5);' + NL + 'System.out.println(r + " " + r.isSquare());', O("5x5 true", "Rectangle@1b6d3586 true", "25 true", "5x5 false"), 0, "Joining an object to a String calls its toString.", 'Rectangle r = new Rectangle(5, 5);\nSystem.out.println(r + " " + r.isSquare());', cls=RECT_NP)
P.append(q("Which is a correct constructor header for a class named <code>Song</code>?", Oc("public Song(String title, int seconds)", "public void Song(String title, int seconds)", "public song(String title, int seconds)", "public Song Song(String title)"), 0, "Same name as the class (case matters) and no return type."))
P.append(q("Why are instance variables declared <code>private</code>?", O("So only the class's own methods can access them directly, which protects the object's data", "So they use less memory", "So they can be used in static methods", "So other classes can change them faster"), 0, "That's encapsulation: outside code must use the public methods."))
BAD = '''class Box
{
    private int size;
    public Box(int s)
    {
        int size = s;
    }
    public int getSize() { return size; }
}'''
addq("What is printed?", 'Box b = new Box(7);' + NL + 'System.out.println(b.getSize());', O("0", "7", "Compile error", "null"), 0, "The constructor declares a new local variable size, so the instance variable keeps its default 0.", 'Box b = new Box(7);\nSystem.out.println(b.getSize());', cls=BAD, extra=code(BAD))
BAD2 = '''class Pet
{
    private String name;
    public Pet(String name)
    {
        name = name;
    }
    public String getName() { return name; }
}'''
addq("What is printed?", 'Pet p = new Pet("Rex");' + NL + 'System.out.println(p.getName());', O("null", "Rex", "Compile error", "name"), 0, "Inside the constructor, name means the parameter, so the line assigns the parameter to itself. The instance variable stays null.", 'Pet p = new Pet("Rex");\nSystem.out.println(p.getName());', cls=BAD2, extra=code(BAD2), t="m")
addq("Given the <code>Counter</code> class from this page, what is printed?", 'Counter c = new Counter(3, 4);' + NL + 'c.click();' + NL + 'c.click();' + NL + 'System.out.println(c.getCount());', O("11", "5", "8", "3"), 0, "3 + 4 + 4 = 11.", 'Counter c = new Counter(3, 4);\nc.click();\nc.click();\nSystem.out.println(c.getCount());', cls=POINT2)
addq("Given the <code>BankAccount</code> class, what is printed?", 'BankAccount a = new BankAccount("Lee", 20.0);' + NL + 'a.deposit(-5.0);' + NL + 'a.withdraw(8.0);' + NL + 'System.out.println(a.getBalance());', O("12.0", "7.0", "20.0", "17.0"), 0, "deposit ignores negative amounts; withdraw(8.0) succeeds: 20 − 8 = 12.0.", 'BankAccount a = new BankAccount("Lee", 20.0);\na.deposit(-5.0);\na.withdraw(8.0);\nSystem.out.println(a.getBalance());', cls=ACC_NOPUB)
P.append(q("Which statement, written in a class other than <code>BankAccount</code>, causes a compile error?", Oc("a.balance = 100.0;", "a.deposit(100.0);", "double d = a.getBalance();", "System.out.println(a);"), 0, "balance is private.", run="BankAccount a = new BankAccount(\"X\", 1.0);\na.balance = 100.0;", cls=ACC_NOPUB.replace("class BankAccount", "class BankAccount") + "\nclass Other { static void f(BankAccount a) { a.balance = 100.0; } }", err="compile"))
INC = '''public static void bump(int n, Counter c)
{
    n++;
    c.click();
}'''
addq("Given the <code>Counter</code> class, what is printed?", 'int n = 5;' + NL + 'Counter c = new Counter();' + NL + 'bump(n, c);' + NL + 'System.out.println(n + " " + c.getCount());', O("5 1", "6 1", "5 0", "6 0"), 0, "n is a copy, so the caller's n stays 5. c refers to the same Counter, so the click is visible.", 'int n = 5;\nCounter c = new Counter();\nbump(n, c);\nSystem.out.println(n + " " + c.getCount());', cls=POINT2, pre=INC, extra=code(INC), t="m")
RESET = '''public static void reset(Counter c)
{
    c = new Counter();
}'''
addq("Given the <code>Counter</code> class, what is printed?", 'Counter c = new Counter(10, 1);' + NL + 'reset(c);' + NL + 'System.out.println(c.getCount());', O("10", "0", "1", "Compile error"), 0, "reset points its own copy of the reference at a new object. The caller's c still refers to the original.", 'Counter c = new Counter(10, 1);\nreset(c);\nSystem.out.println(c.getCount());', cls=POINT2, pre=RESET, extra=code(RESET), t="m")
addq("Given the <code>Student</code> class with its static <code>nextId</code>, what is printed?", 'Student x = new Student("A");' + NL + 'Student y = new Student("B");' + NL + 'Student z = new Student("C");' + NL + 'System.out.println(y.getId() + Student.getNextId());', O("6", "24", "2", "5"), 0, "y's id is 2; after three students nextId is 4. 2 + 4 = 6 (int addition).", 'Student x = new Student("A");\nStudent y = new Student("B");\nStudent z = new Student("C");\nSystem.out.println(y.getId() + Student.getNextId());', cls=STAT, t="m")
P.append(q("Which line causes a compile error inside this class?" + code('''class Item
{
    private double price;
    private static int count;
    public static void report()
    {
        System.out.println(price);    // line A
        System.out.println(count);    // line B
    }
}'''), O("Line A", "Line B", "Both", "Neither"), 0, "A static method has no object, so it can't use the instance variable price. Static variables are fine.", t="m",
  run="", cls='class Item { private double price; private static int count; public static void report() { System.out.println(price); } }', err="compile"))
P.append(q("A class keeps a running total of how many objects have been created. The variable should be…", O("a private static int", "a private int instance variable", "a local variable in the constructor", "a parameter of the constructor"), 0, "One shared count for the whole class means static.", t="m"))
addq("What is printed?", 'new Temp().show();', O("3 10", "10 10", "3 3", "10 3"), 0, "The local value 3 shadows the instance variable; this.value is the instance variable, 10.", 'new Temp().show();', cls=SHADOW, extra=code(SHADOW), t="m")
P.append(q("What does the keyword <code>this</code> refer to inside an instance method?", O("The object the method was called on", "The class itself", "The most recently created object", "The method's return value"), 0, "this is a reference to the current object.", t="m"))
P.append(q("A method has header <code>public int max(int a, int b)</code> and body <code>if (a &gt; b) return a;</code>. What happens?", O("Compile error: missing return on some path", "It returns b when a ≤ b", "It returns 0 when a ≤ b", "Run-time error"), 0, "A non-void method must return a value on every path.", run="", cls="", pre="public int max(int a, int b) { if (a > b) return a; }", err="compile"))
P.append(q("Which describes an accessor method?", O("It returns information about the object without changing it", "It changes the object's instance variables", "It has the same name as the class", "It must be static"), 0, "Getters are accessors; setters/mutators change state."))
LOOP3 = '''class Thermostat
{
    private int temp;
    public Thermostat(int t) { temp = t; }
    public void adjust(int target)
    {
        while (temp < target) temp += 2;
        while (temp > target) temp--;
    }
    public int getTemp() { return temp; }
}'''
addq("What is printed?", 'Thermostat t = new Thermostat(65);' + NL + 't.adjust(70);' + NL + 'System.out.println(t.getTemp());', O("70", "71", "69", "72"), 0, "65 → 67 → 69 → 71 (up by 2), then down by 1 to 70.", 'Thermostat t = new Thermostat(65);\nt.adjust(70);\nSystem.out.println(t.getTemp());', cls=LOOP3, extra=code(LOOP3))
P.append(q("If a class defines the constructor <code>public Dog(String name)</code> and no others, which statement compiles?", Oc('Dog d = new Dog("Rex");', "Dog d = new Dog();", 'Dog d = Dog("Rex");', 'Dog d = new Dog("Rex", 3);'), 0, "Once any constructor is written, Java no longer provides the no-argument one.",
  run='Dog d = new Dog();', cls='class Dog { private String name; public Dog(String name) { this.name = name; } }', err="compile"))
CMP = '''class Box2
{
    private int size;
    public Box2(int s) { size = s; }
    public boolean biggerThan(Box2 other)
    {
        return size > other.size;
    }
}'''
addq("This method accesses <code>other.size</code>, which is private. What happens?", 'Box2 a = new Box2(5);' + NL + 'Box2 b = new Box2(3);' + NL + 'System.out.println(a.biggerThan(b));', O("It prints true", "Compile error: size is private", "It prints false", "Run-time error"), 0, "Private means private to the class, so any Box2 method can read another Box2's size.", 'Box2 a = new Box2(5);\nBox2 b = new Box2(3);\nSystem.out.println(a.biggerThan(b));', cls=CMP, extra=code(CMP), t="m", exp="true")
addq("Given the <code>BankAccount</code> class, what is printed?", 'BankAccount a = new BankAccount("Kim", 10.0);' + NL + 'BankAccount b = a;' + NL + 'b.deposit(5.0);' + NL + 'a.withdraw(3.0);' + NL + 'System.out.println(b.getBalance());', O("12.0", "15.0", "7.0", "10.0"), 0, "a and b are aliases for one account: 10 + 5 − 3 = 12.0.", 'BankAccount a = new BankAccount("Kim", 10.0);\nBankAccount b = a;\nb.deposit(5.0);\na.withdraw(3.0);\nSystem.out.println(b.getBalance());', cls=ACC_NOPUB, t="m")
P.append(q("Which is the best reason to write a method instead of repeating the same code in several places?", O("Procedural abstraction: write it once, name it, and reuse it, so changes happen in one place", "Methods make programs run faster", "Java requires all code to be in separate methods", "Methods use less memory than loops"), 0, "Methods reduce repetition and hide details behind a name."))
P.append(q("A programmer uses an image library found online in an app they sell. What should they check first?", O("The library's license, to see whether commercial use is allowed", "Whether the library is written in Java", "How many lines of code it has", "Nothing; anything online is free to use"), 0, "Intellectual property: licenses state how code can be used."))
GT = '''class Score
{
    private int pts;
    public Score(int p) { pts = p; }
    public void add(int p) { pts += p; }
    public String toString() { return "pts=" + pts; }
}'''
addq("What is printed?", 'Score s = new Score(4);' + NL + 's.add(s.toString().length());' + NL + 'System.out.println(s);', O("pts=9", "pts=8", "pts=4", "pts=5"), 0, "toString() is \"pts=4\" with length 5. 4 + 5 = 9.", 'Score s = new Score(4);\ns.add(s.toString().length());\nSystem.out.println(s);', cls=GT, extra=code(GT), t="m")
PQ = P

C = []
CH1 = '''class Node
{
    private int val;
    private static int created = 0;
    public Node(int v) { val = v; created++; }
    public Node copyPlus(int d) { return new Node(val + d); }
    public int getVal() { return val; }
    public static int getCreated() { return created; }
}'''
C.append(q(f"What is printed?{code(CH1)}{code('Node a = new Node(1);' + NL + 'Node b = a.copyPlus(2).copyPlus(3);' + NL + 'System.out.println(b.getVal() + \" \" + Node.getCreated());')}", O("6 3", "6 2", "3 3", "6 1"), 0, "copyPlus returns a new Node each time: values 1, 3, 6. Three Nodes were created.", t="m", run='Node a = new Node(1);\nNode b = a.copyPlus(2).copyPlus(3);\nSystem.out.println(b.getVal() + " " + Node.getCreated());', cls=CH1))
SW = '''public static void swap(Counter a, Counter b)
{
    Counter temp = a;
    a = b;
    b = temp;
}'''
C.append(q(f"Given the <code>Counter</code> class, what is printed?{code(SW)}{code('Counter x = new Counter(1, 1);' + NL + 'Counter y = new Counter(2, 1);' + NL + 'swap(x, y);' + NL + 'System.out.println(x.getCount() + \" \" + y.getCount());')}", O("1 2", "2 1", "1 1", "2 2"), 0, "swap only rearranges its own copies of the references. The caller's x and y are unchanged.", t="m", run='Counter x = new Counter(1, 1);\nCounter y = new Counter(2, 1);\nswap(x, y);\nSystem.out.println(x.getCount() + " " + y.getCount());', cls=POINT2, pre=SW))
SW2 = '''public static void swapCounts(Counter a, Counter b)
{
    int ca = a.getCount();
    while (a.getCount() < b.getCount()) a.click();
    while (b.getCount() > ca) b.click();
}'''
C.append(q(f"Given the <code>Counter</code> class, what happens?{code(SW2)}{code('Counter x = new Counter(1, 1);' + NL + 'Counter y = new Counter(3, 1);' + NL + 'swapCounts(x, y);')}", O("The second loop never ends (click only increases)", "x is 3 and y is 1", "x is 1 and y is 3", "Compile error"), 0, "After the first loop x is 3. y is 3 > 1, and click() only adds, so the condition never becomes false.", t="m"))
WR = '''class Wallet
{
    private int cents;
    public Wallet(int c) { cents = c; }
    public Wallet combine(Wallet other)
    {
        cents += other.cents;
        other.cents = 0;
        return this;
    }
    public int get() { return cents; }
}'''
C.append(q(f"What is printed?{code(WR)}{code('Wallet a = new Wallet(5);' + NL + 'Wallet b = new Wallet(7);' + NL + 'Wallet c = a.combine(b);' + NL + 'c.combine(new Wallet(1));' + NL + 'System.out.println(a.get() + \" \" + b.get() + \" \" + (c == a));')}", O("13 0 true", "12 0 true", "13 7 false", "12 7 false"), 0, "combine returns this, so c is a. a: 5 + 7 = 12, then + 1 = 13. b was emptied to 0.", t="m", run='Wallet a = new Wallet(5);\nWallet b = new Wallet(7);\nWallet c = a.combine(b);\nc.combine(new Wallet(1));\nSystem.out.println(a.get() + " " + b.get() + " " + (c == a));', cls=WR))
SH2 = '''class Acc
{
    private int total;
    public void add(int total)
    {
        total += total;
    }
    public int get() { return total; }
}'''
C.append(q(f"What is printed?{code(SH2)}{code('Acc a = new Acc();' + NL + 'a.add(4);' + NL + 'a.add(6);' + NL + 'System.out.println(a.get());')}", O("0", "10", "20", "Compile error"), 0, "The parameter total shadows the instance variable, so the method only doubles its parameter. The instance variable stays 0.", t="m", run='Acc a = new Acc();\na.add(4);\na.add(6);\nSystem.out.println(a.get());', cls=SH2))
C.append(q("A <code>Course</code> class stores a teacher object passed to its constructor and has <code>getTeacher()</code> that returns it. Why might this be a problem?", O("Outside code receives a reference to the stored object and can change it, bypassing Course's methods", "Objects can't be returned from methods", "The teacher would be copied each time, wasting memory", "It causes a compile error"), 0, "Returning a reference to a mutable instance variable breaks encapsulation; return a copy or only the needed information.", t="m"))
CS = '''class Temp2
{
    private static int count = 0;
    private int id;
    public Temp2() { count += 2; id = count; }
    public int getId() { return id; }
    public static int getCount() { return count; }
}'''
C.append(q(f"What is printed?{code(CS)}{code('Temp2 a = new Temp2();' + NL + 'Temp2 b = new Temp2();' + NL + 'Temp2 c = b;' + NL + 'System.out.println(a.getId() + c.getId() + Temp2.getCount());')}", O("10", "8", "246", "12"), 0, "a.id = 2, b.id = 4, count = 4. c is b. 2 + 4 + 4 = 10 (all ints).", t="m", run='Temp2 a = new Temp2();\nTemp2 b = new Temp2();\nTemp2 c = b;\nSystem.out.println(a.getId() + c.getId() + Temp2.getCount());', cls=CS))
CHAL = C

E = []
E.append(q("Which is true of a constructor?", O("It has the same name as the class and no return type", "It must be declared void", "It must be static", "A class can have only one"), 0, "Constructors can be overloaded and have no return type.", k="concept"))
E.append(q(f"Given the <code>Rectangle</code> class, what is printed?{code('Rectangle r = new Rectangle(2, 5);' + NL + 'Rectangle s = r;' + NL + 's.scale(3);' + NL + 'System.out.println(r.area());')}", O("90", "10", "30", "270"), 0, "r and s are one object: 6x15 = 90.", t="m", run='Rectangle r = new Rectangle(2, 5);\nRectangle s = r;\ns.scale(3);\nSystem.out.println(r.area());', cls=RECT, k="calc"))
E.append(q("Which instance variable declaration follows good encapsulation?", Oc("private int score;", "public int score;", "static int score;", "int score = 0;"), 0, "Instance variables should be private.", k="concept"))
E.append(q(f"What is printed?{code('class Lamp' + NL + '{' + NL + '    private boolean on;' + NL + '    public void toggle() { on = !on; }' + NL + '    public boolean isOn() { return on; }' + NL + '}')}{code('Lamp l = new Lamp();' + NL + 'l.toggle();' + NL + 'l.toggle();' + NL + 'l.toggle();' + NL + 'System.out.println(l.isOn());')}", O("true", "false", "null", "Compile error"), 0, "on starts false (default); three toggles: true, false, true.", run='Lamp l = new Lamp();\nl.toggle();\nl.toggle();\nl.toggle();\nSystem.out.println(l.isOn());', cls='class Lamp { private boolean on; public void toggle() { on = !on; } public boolean isOn() { return on; } }', k="calc"))
E.append(q("A static method tries to use an instance variable directly. What happens?", O("Compile error", "It uses the most recent object's value", "It uses 0", "Run-time error"), 0, "Static methods don't belong to an object.", t="m", k="concept"))
DBL = '''public static void triple(int x, Rectangle r)
{
    x *= 3;
    r.scale(3);
}'''
E.append(q(f"Given the <code>Rectangle</code> class, what is printed?{code(DBL)}{code('int n = 2;' + NL + 'Rectangle r = new Rectangle(1, 2);' + NL + 'triple(n, r);' + NL + 'System.out.println(n + \" \" + r);')}", O("2 3x6", "6 3x6", "2 1x2", "6 1x2"), 0, "The int is a copy; the object is shared.", t="m", run='int n = 2;\nRectangle r = new Rectangle(1, 2);\ntriple(n, r);\nSystem.out.println(n + " " + r);', cls=RECT, pre=DBL, k="calc"))
E.append(q("Inside a constructor with parameter <code>speed</code>, how do you set the instance variable also named speed?", Oc("this.speed = speed;", "speed = speed;", "speed = this.speed;", "int speed = speed;"), 0, "this.speed is the instance variable; plain speed is the parameter.", t="m", k="concept"))
E.append(q(f"Given the <code>Student</code> class, what is printed?{code('for (int i = 0; i < 4; i++)' + NL + '    new Student(\"S\" + i);' + NL + 'System.out.println(Student.getNextId());')}", O("5", "4", "1", "0"), 0, "nextId starts at 1 and increases once per student: 5.", t="m", run='for (int i = 0; i < 4; i++)\n    new Student("S" + i);\nSystem.out.println(Student.getNextId());', cls=STAT, k="calc"))
E.append(q(f"Given the <code>TicketBooth</code> class, what is printed?{code('TicketBooth t = new TicketBooth(10, 2.0);' + NL + 'double a = t.buy(6);' + NL + 'double b = t.buy(5);' + NL + 'double c = t.buy(4);' + NL + 'System.out.println(a + b + c + \" \" + t.ticketsLeft());')}", O("20.0 0", "22.0 0", "12.0 4", "20.0 1"), 0, "6 sold (12.0), 5 rejected (0.0, only 4 left), 4 sold (8.0). Total 20.0, 0 left.", run='TicketBooth t = new TicketBooth(10, 2.0);\ndouble a = t.buy(6);\ndouble b = t.buy(5);\ndouble c = t.buy(4);\nSystem.out.println(a + b + c + " " + t.ticketsLeft());', cls=TICKET.replace("public class", "class"), k="calc"))
E.append(q("What does a class's <code>toString</code> method do when the object is printed?", O("Its return value is what gets printed", "It prints the object's memory address", "It must print the object itself", "Nothing; it's only called explicitly"), 0, "println and String concatenation call toString automatically.", k="concept"))
E.append(q("Which describes a local variable declared inside a method?", O("It exists only while that method's block runs", "It keeps its value between calls", "Every object has its own copy", "Other classes can access it with the dot operator"), 0, "Local variables disappear when their block ends.", t="m", k="concept"))
E.append(q(f"What is printed?{code(SHADOW.replace('int value = 3;', 'int value = 3;' + NL + '        this.value += value;'))}{code('Temp t = new Temp();' + NL + 't.show();' + NL + 't.show();')}", O("3 13 3 16", "3 10 3 10", "13 13 16 16", "3 13 3 13"), 0, "Each call adds the local 3 to the instance variable: 13, then 16.", t="m", run='Temp t = new Temp();\nt.show();\nt.show();', cls=SHADOW.replace('int value = 3;', 'int value = 3;\n        this.value += value;'), k="calc"))
E.append(q("A class has a method <code>public boolean equals(Point other)</code> that compares x and y. Which statement is true?", O("It can read other.x and other.y even though they're private", "It can't compile because the fields are private", "It must be static", "It must return an int"), 0, "Private access is per class, not per object.", t="m", k="concept"))
E.append(q("Which change makes a method an accessor rather than a mutator?", O("It returns information and doesn't change instance variables", "It's declared void", "It takes no parameters", "It's declared private"), 0, "Accessors report state; mutators change it.", k="concept"))
E.append(q("Software that decides loan approvals is found to reject one group of people more often for reasons unrelated to risk. This is an example of…", O("an unintended ethical impact of program design", "a syntax error", "an intellectual property violation", "a run-time exception"), 0, "Topic 3.2: programs can have harmful effects their designers didn't intend.", k="concept"))
FRQS = [
 {"q": f"Write the complete class <code>Plant</code>. A plant is created with a name and a starting height in centimeters. <code>water()</code> makes it grow 2 cm, but only if it was not watered the previous time a method was called that day; <code>newDay()</code> resets that, and <code>getHeight()</code> returns the height.{code('Plant p = new Plant(\"Fern\", 10);' + NL + 'p.water();       // height 12' + NL + 'p.water();       // already watered today: still 12' + NL + 'p.newDay();' + NL + 'p.water();       // height 14' + NL + 'p.getHeight();   // returns 14')}",
  "parts": [{"p": "(a) Write the class.", "rubric": [["Private instance variables for name, height and whether it was watered today", 1], ["Constructor with (String, int) that initializes all three", 1], ["water() grows by 2 only when not yet watered, then records that it was", 1], ["newDay() resets the watered flag", 1], ["getHeight() returns the height", 1]],
   "answer": code('public class Plant\n{\n    private String name;\n    private int height;\n    private boolean wateredToday;\n\n    public Plant(String name, int height)\n    {\n        this.name = name;\n        this.height = height;\n        wateredToday = false;\n    }\n\n    public void water()\n    {\n        if (!wateredToday)\n        {\n            height += 2;\n            wateredToday = true;\n        }\n    }\n\n    public void newDay()\n    {\n        wateredToday = false;\n    }\n\n    public int getHeight()\n    {\n        return height;\n    }\n}')}]},
 {"q": f"Write the class <code>Scoreboard</code> for a two-team game. It's created with two team names. <code>recordPoint(String team)</code> adds a point to that team. <code>leader()</code> returns the name of the team with more points, or \"tie\".{code('Scoreboard s = new Scoreboard(\"Red\", \"Blue\");' + NL + 's.recordPoint(\"Blue\");' + NL + 's.leader();   // returns \"Blue\"' + NL + 's.recordPoint(\"Red\");' + NL + 's.leader();   // returns \"tie\"')}",
  "parts": [{"p": "(a) Write the class.", "rubric": [["Private variables for both names and both scores", 1], ["Constructor stores names and sets scores to 0", 1], ["recordPoint compares with equals and adds to the right score", 1], ["leader returns the correct name or \"tie\"", 1]],
   "answer": code('public class Scoreboard\n{\n    private String team1, team2;\n    private int score1, score2;\n\n    public Scoreboard(String a, String b)\n    {\n        team1 = a;\n        team2 = b;\n        score1 = 0;\n        score2 = 0;\n    }\n\n    public void recordPoint(String team)\n    {\n        if (team.equals(team1))\n            score1++;\n        else if (team.equals(team2))\n            score2++;\n    }\n\n    public String leader()\n    {\n        if (score1 > score2) return team1;\n        if (score2 > score1) return team2;\n        return "tie";\n    }\n}')}]}]
jcheck('Plant p = new Plant("Fern", 10);\np.water(); p.water(); p.newDay(); p.water();\nSystem.out.println(p.getHeight());\nScoreboard s = new Scoreboard("Red", "Blue");\ns.recordPoint("Blue");\nSystem.out.println(s.leader());\ns.recordPoint("Red");\nSystem.out.println(s.leader());', "14 Blue tie",
       cls='class Plant { private String name; private int height; private boolean wateredToday; public Plant(String name, int height){this.name=name;this.height=height;wateredToday=false;} public void water(){ if(!wateredToday){height+=2;wateredToday=true;} } public void newDay(){wateredToday=false;} public int getHeight(){return height;} }\nclass Scoreboard { private String team1, team2; private int score1, score2; public Scoreboard(String a, String b){team1=a;team2=b;} public void recordPoint(String team){ if(team.equals(team1)) score1++; else if(team.equals(team2)) score2++; } public String leader(){ if(score1>score2) return team1; if(score2>score1) return team2; return "tie"; } }')
EX = {"title": "Unit 3 Practice Exam: Class Creation", "mcqMinutes": 30, "frqMinutes": 25, "tags": T3,
      "kinds": {"concept": "Concept", "calc": "Code tracing"}, "mcq": E, "frq": FRQS}

if __name__ == "__main__":
    assert verify({"practice": PQ, "challenge": CHAL, "exam": E}), "fix questions"
    balance(PQ, 31); balance(CHAL, 32); balance(E, 33)
    EX["mcq"] = strip_private(E)
    CH.append(chapter("practice-c3", "Practice Questions", "Practice", [quiz_section("practice-quiz-c3", "Practice questions", f"{len(PQ)} questions. Every code answer was checked by running it in Java.", "quiz-c3", T3)]))
    CH.append(chapter("challenge-c3", "Challenge Questions", "Challenge", [quiz_section("challenge-quiz-c3", "Challenge questions", "References, static and shadowing traps. Turn off animated models in ⚙ Settings for a real exam feel.", "quiz-challenge-c3", T3)], hard=True))
    CH.append(chapter("exam-ch-c3", "Practice Exam", "Practice Exam", ['<section class="topic" id="exam-box-c3"><h2>Practice exam</h2><p class="sub">15 multiple-choice questions (30 minutes) and 2 class-design free-response questions (25 minutes). No feedback until you submit.</p><div class="exam" data-src="exam-c3"></div></section>']))
    HTML = page("unit-3", "AP CSA Unit 3: Class Creation", "AP Computer Science A · Unit 3",
                'Class<br><span class="hl">Creation</span>',
                f"Abstraction and design, instance variables, constructors, writing methods, passing references, static members, scope and this: explanations, memory animations you can step through, {len(PQ) + len(CHAL)} practice questions checked in Java, and a timed practice exam with class-design free response.",
                "AP Computer Science A Unit 3 review with memory animations, practice questions and a practice exam.",
                CH, {"quiz-c3": strip_private(PQ), "quiz-challenge-c3": strip_private(CHAL), "exam-c3": EX},
                course="ap-csa", footer="Apogee · AP Computer Science A · Java", extra_js=("cs-sims.js",))
    open("/home/claude/ap-physics-study/courses/ap-csa/unit-3.html", "w").write(HTML)
    print("CSA unit 3 written:", len(PQ), len(CHAL), len(E))
