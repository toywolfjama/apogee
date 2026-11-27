from lab_common import *
L = "Computer Engineering"
TAGS = {"c": "Concept", "p": "Calculation", "d": "Design", "r": "Reading circuits"}
OUT = "../../courses/comp-eng/ce-5.html"

MEM = topic("latches", "Memory from feedback: latches", f'''
<p>Combinational circuits forget everything the moment their inputs change. To build memory, you feed a circuit's output back into its own input. The simplest memory cell is the <b>SR latch</b>: two NOR gates, each feeding the other.</p>
{table(["S (set)", "R (reset)", "Q next", "Meaning"], [["0", "0", "Q", "hold: remember the last value"], ["1", "0", "1", "set"], ["0", "1", "0", "reset"], ["1", "1", "invalid", "both outputs forced to 0; avoid"]])}
<p>Once you set it, you can let go of S and the loop keeps Q = 1 forever (as long as there's power). That single loop is the origin of every bit of SRAM and every register in your computer.</p>
{box("tip", "Latch vs flip-flop", "A <b>latch</b> is level-sensitive: while its enable is 1, the output follows the input. A <b>flip-flop</b> is edge-triggered: it only looks at its input at the instant the clock rises (0 → 1), then holds that value for the whole cycle. Almost all processor state lives in flip-flops.")}
''', pill=("c", "5.1"))

FF = topic("flipflops", "Flip-flops and the clock", f'''
<p>A <b>clock</b> is a signal that switches 0, 1, 0, 1 at a steady rate. Every flip-flop in a synchronous circuit updates at the same instant, the <b>rising edge</b>, so the whole system marches in lockstep. A 3 GHz clock has a period of 1/(3 × 10⁹) ≈ 0.33 ns.</p>
{xlab("flipflop")}
{table(["Flip-flop", "Inputs", "Behaviour at the clock edge", "Typical use"], [
 ["D (data)", "D", "Q ← D", "registers: just store a value"],
 ["T (toggle)", "T", "T = 1: Q ← Q′. T = 0: hold", "counters"],
 ["JK", "J, K", "00 hold, 01 reset, 10 set, 11 toggle", "general purpose (fixes SR's invalid case)"],
 ["SR (clocked)", "S, R", "00 hold, 01 reset, 10 set, 11 not allowed", "mostly historical"],
])}
<h3>Timing rules</h3>
<p>The input of a flip-flop must be stable for a short <b>setup time</b> before the edge and a <b>hold time</b> after it. Between two flip-flops, the signal has to get through the combinational logic in time:</p>
{eq("T<sub>clock</sub> ≥ t<sub>clk→Q</sub> + t<sub>logic</sub> + t<sub>setup</sub>")}
{worked("A flip-flop has clock-to-Q delay 40 ps and setup time 30 ps. The slowest logic path between flip-flops is 430 ps. Maximum clock frequency?", "T ≥ 40 + 430 + 30 = 500 ps, so f ≤ 1/(500 × 10⁻¹² s) = 2 GHz. To go faster you must shorten the critical path, for example by pipelining (unit 6).")}
''', pill=("c", "5.2"))

REG = topic("registers", "Registers and counters", f'''
{mini(("Register", "n D flip-flops sharing one clock store an n-bit word. A 64-bit CPU register is 64 flip-flops. Add a MUX in front of each D input to choose between loading a new value and keeping the old one (a load-enable)."),
      ("Shift register", "Flip-flops in a chain, each D fed by its neighbour's Q. Every clock edge shifts the bits one place. Used to turn serial data (one bit at a time, like USB) into parallel words, and back."),
      ("Binary counter", "Each bit toggles when every lower bit is 1. With T flip-flops: T₀ = 1, T₁ = Q₀, T₂ = Q₀Q₁, … An n-bit counter counts 0 to 2ⁿ − 1 and wraps."),
      ("Register file", "A small array of registers (say 32 × 64 bits) with a decoder to choose which one to write and MUXes to choose which ones to read. It's the fastest storage in the CPU."))}
{xlab("fsm", title="2-bit counter", sub="Each clock tick moves to the next count and wraps from 3 back to 0.", states=[{"id": "0", "label": "00", "out": "0"}, {"id": "1", "label": "01", "out": "1"}, {"id": "2", "label": "10", "out": "2"}, {"id": "3", "label": "11", "out": "3"}], trans=[["0", "tick", "1"], ["1", "tick", "2"], ["2", "tick", "3"], ["3", "tick", "0"]], inputs=["tick"], h=260, startAng=180)}
{worked("A 4-bit counter driven by a 1 kHz clock starts at 0. What does it read after 37 ms?", "37 ticks. A 4-bit counter wraps every 16, so 37 mod 16 = 5 → 0101.")}
''', pill=("d", "5.3"))

FSM = topic("fsm", "Finite state machines", f'''
<p>A <b>finite state machine (FSM)</b> is a circuit that remembers which of a fixed set of <b>states</b> it's in and moves between them based on its inputs. Traffic lights, vending machines, elevator controllers, network protocols and the control unit of a CPU are all FSMs.</p>
<ol class="steps"><li>List the states (what does the machine need to remember?).</li><li>Draw the <b>state diagram</b>: a circle per state, an arrow per transition labelled with the input that causes it.</li>
<li>Write the <b>state table</b>: current state + input → next state (+ output).</li><li>Give each state a binary code. k state bits can encode up to 2ᵏ states.</li><li>Derive the next-state and output logic (K-maps!) and store the state in flip-flops.</li></ol>
<h3>Moore machine: outputs depend only on the state</h3>
{xlab("fsm", title="Sequence detector for 101", sub="Output 1 whenever the last three inputs were 1, 0, 1 (overlaps allowed). Try 1 0 1 0 1.", states=[{"id": "S0", "label": "S0", "out": "0", "xy": [.13, .45], "loop": 90}, {"id": "S1", "label": "S1", "out": "0", "xy": [.42, .3]}, {"id": "S2", "label": "S2", "out": "0", "xy": [.56, .78]}, {"id": "S3", "label": "S3", "out": "1", "accept": True, "xy": [.86, .42]}], trans=[["S0", "0", "S0"], ["S0", "1", "S1"], ["S1", "1", "S1"], ["S1", "0", "S2"], ["S2", "0", "S0"], ["S2", "1", "S3"], ["S3", "1", "S1"], ["S3", "0", "S2"]], inputs=["0", "1"], h=320)}
<p>S0 = haven't seen anything useful, S1 = just saw a 1, S2 = just saw 1 0, S3 = just saw 1 0 1 (output 1). From S3, a 0 means we've seen …1 0, which is S2, so the overlapping pattern isn't missed.</p>
<h3>Mealy machine: outputs depend on the state and the input</h3>
{xlab("fsm", title="Vending machine (15¢)", sub="Inputs: N = nickel (5¢), D = dime (10¢). Labels are input/output; output 1 = dispense.", states=[{"id": "0", "label": "0¢", "xy": [.5, .2]}, {"id": "5", "label": "5¢", "xy": [.82, .76]}, {"id": "10", "label": "10¢", "xy": [.18, .76]}], startAng=180, trans=[["0", "N", "5", "0"], ["0", "D", "10", "0"], ["5", "N", "10", "0"], ["5", "D", "0", "1"], ["10", "N", "0", "1"], ["10", "D", "0", "1"]], inputs=["N", "D"], h=300)}
{box("tip", "Moore or Mealy?", "Mealy machines often need fewer states and react in the same cycle as the input. Moore machines are safer: their outputs only change on clock edges, so glitches on the inputs can't leak through.")}
''', pill=("d", "5.4"), det=("From state table to circuit: the 101 detector", "<p>Encode S0 = 00, S1 = 01, S2 = 10, S3 = 11 in flip-flops Q₁Q₀, with input X. Next-state table: S0: X = 0 → 00, X = 1 → 01. S1: 0 → 10, 1 → 01. S2: 0 → 00, 1 → 11. S3: 0 → 10, 1 → 01. Read off D₀ (next Q₀) = X. D₁ (next Q₁) is 1 for (S1, 0), (S2, 1), (S3, 0): D₁ = Q₁′Q₀X′ + Q₁Q₀′X + Q₁Q₀X′ = Q₀X′ + Q₁Q₀′X. Output Z = Q₁Q₀. Two D flip-flops and a few gates.</p>"))

SUM = topic("summary-ce5", "Unit summary", mini(
 ("Latches", "Feedback = memory. SR latch: set, reset, hold; S = R = 1 invalid. Latch = level-sensitive, flip-flop = edge-triggered."),
 ("Flip-flops", "D: Q ← D. T: toggle when 1. JK: hold / reset / set / toggle. Clock period ≥ clk→Q + logic + setup."),
 ("Registers", "n flip-flops = n-bit register. Shift registers move bits. Counters: bit k toggles when all lower bits are 1."),
 ("FSMs", "States + transitions. Moore: output from state. Mealy: output from state + input. k flip-flops hold up to 2ᵏ states."),
))

CH = [chapter("ch-latch", "Latches and Flip-flops", "Flip-flops", [MEM, FF]),
      chapter("ch-reg", "Registers and Counters", "Registers", [REG]),
      chapter("ch-fsm", "State Machines", "FSMs", [FSM, SUM])]

close(1 / 500e-12, 2e9)
PQ = [
 q("What turns a combinational circuit into a memory element?", ["Feeding an output back into an input", "Adding more inputs", "Using XOR gates", "Raising the voltage"], 0, "Feedback lets the circuit hold a state.", "c"),
 q("An SR latch has S = 0, R = 0. What happens?", ["Q keeps its previous value", "Q becomes 0", "Q becomes 1", "Q is invalid"], 0, "00 is the hold condition.", "c"),
 q("Which SR latch input combination should be avoided?", ["S = 1, R = 1", "S = 0, R = 0", "S = 1, R = 0", "S = 0, R = 1"], 0, "It forces both outputs to the same value and the final state is unpredictable.", "c"),
 q("A D flip-flop has D = 1 at a rising clock edge. Afterwards Q is…", ["1", "0", "the old Q", "Q′"], 0, "D flip-flops copy D on the edge.", "r"),
 q("A T flip-flop with Q = 1 and T = 1 receives a clock edge. New Q?", ["0", "1", "undefined", "T"], 0, "T = 1 toggles.", "r"),
 q("A JK flip-flop with J = 1, K = 1 does what at the clock edge?", ["Toggles", "Sets", "Resets", "Holds"], 0, "11 = toggle.", "c"),
 q("What is the clock period of a 4 GHz processor?", ["0.25 ns", "4 ns", "0.4 ns", "250 ns"], 0, "1 / (4 × 10⁹) = 2.5 × 10⁻¹⁰ s.", "p"),
 q("A latch differs from a flip-flop because a latch…", ["passes its input through whenever it's enabled", "only changes at the clock edge", "can't store data", "has no outputs"], 0, "Latches are level-sensitive.", "c"),
 q("How many flip-flops are in a 32-bit register?", ["32", "16", "64", "5"], 0, "One per bit.", "c"),
 q("An 8-bit counter can count from 0 up to…", ["255", "256", "127", "8"], 0, "2⁸ − 1, then it wraps.", "p"),
 q("A 3-bit counter starts at 000. What does it read after 11 clock edges?", ["011", "111", "101", "000"], 0, "11 mod 8 = 3.", "p"),
 q("What does a shift register do each clock edge?", ["Moves every bit one position", "Adds 1", "Clears all bits", "Swaps the high and low halves"], 0, "Each flip-flop takes its neighbour's value.", "c"),
 q("An FSM has 6 states. How many flip-flops does it need (binary encoding)?", ["3", "6", "2", "4"], 0, "2² = 4 < 6 ≤ 8 = 2³.", "p"),
 q("In a Moore machine, the outputs depend on…", ["the current state only", "the inputs only", "the state and the inputs", "the clock frequency"], 0, "Mealy machines also use the inputs.", "c"),
 q("Clock-to-Q = 50 ps, logic = 700 ps, setup = 50 ps. Maximum clock frequency?", ["1.25 GHz", "2 GHz", "1.43 GHz", "800 MHz"], 0, "T = 800 ps → 1/800 ps = 1.25 GHz.", "p"),
 q("A setup-time violation means…", ["the input changed too close to the clock edge", "the clock stopped", "the flip-flop was reset", "two flip-flops share a clock"], 0, "The flip-flop may capture the wrong value or go metastable.", "c"),
]
CHAL = [
 q("For the 101 detector (S0 = 00, S1 = 01, S2 = 10, S3 = 11, input X), what is the next-state equation for Q₀?", ["D₀ = X", "D₀ = X′", "D₀ = Q₁X", "D₀ = Q₀ ⊕ X"], 0, "Every transition on X = 1 goes to S1 or S3 (Q₀ = 1); every transition on X = 0 goes to S0 or S2 (Q₀ = 0).", "d"),
 q("A 4-bit counter built from T flip-flops needs T₃ = ?", ["Q₀Q₁Q₂", "Q₂", "Q₀ + Q₁ + Q₂", "1"], 0, "A bit toggles when all lower bits are 1 (like 0111 → 1000).", "d"),
 q("A mod-10 counter (0–9) needs at least how many flip-flops, and how many unused states does it have?", ["4 flip-flops, 6 unused", "10 flip-flops, 0 unused", "3 flip-flops, 0 unused", "4 flip-flops, 0 unused"], 0, "2³ = 8 is too few; 2⁴ = 16 gives 6 spare codes (which can be don't-cares).", "d"),
 q("An FSM recognizes inputs that end in 110. Using a Moore design, what is the minimum number of states?", ["4", "3", "2", "8"], 0, "You need to remember: nothing, 1, 11, 110 (output state). That's 4.", "d"),
 q("Two flip-flops are separated by logic with delays between 120 ps and 900 ps. With clk→Q 60 ps and setup 40 ps, what is the shortest safe clock period?", ["1000 ps", "1060 ps", "220 ps", "960 ps"], 0, "The longest path decides: 60 + 900 + 40 = 1000 ps.", "p"),
 q("In the 15¢ vending machine (Mealy), what output sequence results from inputs N, N, N, D, D?", ["0, 0, 1, 0, 1", "0, 0, 1, 1, 0", "0, 1, 0, 1, 1", "0, 0, 0, 1, 1"], 0, "0→5 (0), 5→10 (0), 10→0 (1), 0→10 (0), 10→0 (1).", "r"),
]
EXQ = [
 q("A circuit whose output depends on its past inputs is called…", ["sequential", "combinational", "asynchronous only", "a decoder"], 0, "It has memory.", "c"),
 q("A D flip-flop samples its input…", ["at the rising clock edge", "continuously", "only at power-on", "when D changes"], 0, "Edge-triggered.", "c"),
 q("SR latch with S = 1, R = 0 makes Q =", ["1", "0", "Q", "invalid"], 0, "Set.", "r"),
 q("T flip-flop with T = 0 at the clock edge:", ["holds", "toggles", "resets", "sets"], 0, "T = 0 means no change.", "r"),
 q("The period of a 500 MHz clock is…", ["2 ns", "0.5 ns", "500 ns", "20 ns"], 0, "1/(5 × 10⁸) = 2 × 10⁻⁹ s.", "p"),
 q("Which device converts serial data into parallel words?", ["Shift register", "Decoder", "Full adder", "MUX"], 0, "Shift the bits in one at a time, then read them all at once.", "c"),
 q("A 5-bit counter has how many distinct states?", ["32", "5", "31", "10"], 0, "2⁵.", "p"),
 q("An FSM with 9 states needs at least how many state bits?", ["4", "3", "9", "5"], 0, "2³ = 8 < 9 ≤ 16.", "p"),
 q("In a Mealy machine, outputs are usually drawn on the…", ["transition arrows", "state circles", "clock line", "reset line"], 0, "Because they depend on the input that causes the transition.", "c"),
 q("The minimum clock period is set by…", ["the slowest path between flip-flops plus flip-flop overheads", "the fastest path", "the number of flip-flops", "the supply voltage only"], 0, "clk→Q + longest logic + setup.", "c"),
 q("What does a JK flip-flop do with J = 0, K = 1?", ["Resets Q to 0", "Sets Q to 1", "Toggles", "Holds"], 0, "K resets.", "r"),
 q("Why do synchronous circuits use one shared clock?", ["So every flip-flop updates at the same moment and the system stays in step", "To save power", "Because gates need clocks to work", "To make the circuit combinational"], 0, "A common time reference keeps state changes orderly.", "c"),
]
FRQS = [
 {"q": "Design a Moore FSM for a garage door. Input B is a button. The door cycles Closed → Opening → Open → Closing → Closed, advancing one state each time B = 1 at a clock edge (it stays put when B = 0). Output M (motor on) is 1 in Opening and Closing.", "parts": [
  {"p": "(a) Draw the state diagram (describe states and transitions).", "rubric": [["4 states in the right cycle", 1], ["B = 1 advances, B = 0 self-loops", 1], ["M = 1 only in the two moving states", 1]], "answer": "Closed (M=0) →B=1→ Opening (M=1) →B=1→ Open (M=0) →B=1→ Closing (M=1) →B=1→ Closed. Every state loops to itself on B = 0."},
  {"p": "(b) How many flip-flops are needed? Give one state encoding.", "rubric": [["2 flip-flops", 1], ["Valid encoding, e.g. Closed 00, Opening 01, Open 10, Closing 11", 1]], "answer": "4 states → 2 flip-flops. Closed = 00, Opening = 01, Open = 10, Closing = 11."},
  {"p": "(c) With that encoding, write the output equation for M.", "rubric": [["M = Q₀ (for the encoding above)", 2]], "answer": "M is 1 in 01 and 11, so M = Q₀."}]},
 {"q": "Timing.", "parts": [
  {"p": "(a) Flip-flops have clk→Q = 35 ps and setup = 25 ps. The critical path through the logic is 540 ps. Find the maximum clock frequency.", "rubric": [["T = 600 ps", 1], ["f ≈ 1.67 GHz", 1]], "answer": "T = 35 + 540 + 25 = 600 ps; f = 1/600 ps ≈ 1.67 GHz."},
  {"p": "(b) The engineers split the logic into two halves of 270 ps each with a new register in between. What is the new maximum frequency, and what is the trade-off?", "rubric": [["T = 35 + 270 + 25 = 330 ps → ≈ 3.03 GHz", 1], ["Trade-off: each result now takes 2 cycles (latency) and extra registers cost area/power", 1]], "answer": "T = 330 ps, f ≈ 3.03 GHz. Throughput nearly doubles, but each result takes two cycles to come out and you pay for the extra flip-flops. This is pipelining."}]},
]
build("comp-eng", "ce-5", L, 5, "Sequential Logic and State Machines", 'Circuits that <span class="hl">remember</span>', "Latches, flip-flops, clocks, registers, counters and finite state machines: how circuits store information and step through time.", "Intro to computer engineering unit 5: SR latches, D/T/JK flip-flops, clocks and timing, registers, counters and Moore and Mealy finite state machines.", CH, PQ, CHAL, EXQ, FRQS, OUT, TAGS)
