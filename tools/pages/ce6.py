from lab_common import *
L = "Computer Engineering"
TAGS = {"c": "Concept", "p": "Calculation", "d": "Design", "r": "Reading code"}
OUT = "../../courses/comp-eng/ce-6.html"

PROGS = [
 {"name": "Add two numbers", "desc": "Adds memory[13] and memory[14], stores the sum in memory[15] and outputs it.", "code": [["LOAD", 13], ["ADD", 14], ["STORE", 15], ["OUT"], ["HALT"]], "data": {"13": 5, "14": 7}},
 {"name": "Countdown loop", "desc": "Outputs 3, 2, 1, 0 using SUB, a conditional jump (JZ) and an unconditional jump (JMP).", "code": [["LOAD", 14], ["OUT"], ["SUB", 15], ["JZ", 5], ["JMP", 1], ["OUT"], ["HALT"]], "data": {"14": 3, "15": 1}},
 {"name": "Multiply 4 × 3", "desc": "There's no multiply instruction, so it adds 4 three times. Watch memory[14] count down and memory[12] build up.", "code": [["LOAD", 14], ["JZ", 9], ["SUB", 15], ["STORE", 14], ["LOAD", 12], ["ADD", 13], ["STORE", 12], ["JMP", 0], ["HALT"], ["LOAD", 12], ["OUT"], ["HALT"]], "data": {"12": 0, "13": 4, "14": 3, "15": 1}},
]

ARCH = topic("architecture", "Inside a computer", f'''
<p>Nearly every computer follows the <b>von Neumann architecture</b> (1945): the program and its data live together in the same memory, and a processor fetches instructions from it one at a time. That's the <b>stored-program</b> idea: to run different software you just load different bits into memory.</p>
{mini(("CPU", "The processor. The <b>control unit</b> decodes instructions and sends control signals; the <b>ALU</b> does arithmetic and logic; <b>registers</b> hold the values being worked on."),
      ("Memory (RAM)", "A big array of numbered bytes. Each location has an <b>address</b>. It holds both instructions and data."),
      ("Buses", "Wires connecting the parts: the address bus says where, the data bus carries the value, the control bus says read or write."),
      ("I/O", "Keyboard, screen, network, storage. Devices signal the CPU with <b>interrupts</b> so it doesn't have to keep checking them."))}
{table(["Special register", "Holds"], [["PC (program counter)", "the address of the next instruction"], ["IR (instruction register)", "the instruction being executed"], ["MAR (memory address register)", "the address being read or written"], ["MDR (memory data register)", "the value going to or coming from memory"], ["ACC / general registers", "data being worked on"]])}
''', pill=("c", "6.1"))

CYCLE = topic("cycle", "The fetch–decode–execute cycle", f'''
<p>A CPU does the same thing billions of times per second:</p>
<ol class="steps"><li><b>Fetch:</b> copy the PC into the MAR, read that memory location into the IR, and add 1 to the PC.</li>
<li><b>Decode:</b> the control unit splits the instruction into its <b>opcode</b> (what to do) and <b>operand</b> (what to do it to).</li>
<li><b>Execute:</b> the ALU computes, memory is read or written, or the PC is changed by a jump.</li></ol>
<p>Our toy CPU has 8-bit instructions: the top 4 bits are the opcode, the bottom 4 bits are a memory address (0–15).</p>
{table(["Opcode", "Bits", "Meaning"], [["HALT", "0000", "stop"], ["LOAD a", "0001", "ACC ← memory[a]"], ["STORE a", "0010", "memory[a] ← ACC"], ["ADD a", "0011", "ACC ← ACC + memory[a]"], ["SUB a", "0100", "ACC ← ACC − memory[a]"], ["JMP a", "0101", "PC ← a"], ["JZ a", "0110", "if ACC = 0 then PC ← a"], ["OUT", "0111", "output ACC"]])}
{xlab("cpu", progs=PROGS)}
{box("tip", "Loops and ifs are just jumps", "There's no 'while' in hardware. A loop is a conditional jump backwards; an if statement is a conditional jump over the code you want to skip. Compilers turn every high-level control structure into jumps.")}
''', pill=("r", "6.2"))

ISA = topic("isa", "Instruction sets and assembly", f'''
<p>The <b>instruction set architecture (ISA)</b> is the contract between software and hardware: the list of instructions, registers and addressing modes a processor understands. x86-64 (Intel, AMD), ARM (phones, Apple Silicon) and RISC-V (open source) are the big ones today.</p>
{table(["", "RISC (reduced)", "CISC (complex)"], [["Examples", "ARM, RISC-V, MIPS", "x86"], ["Instructions", "few, simple, fixed length (32 bits)", "many, some very powerful, variable length (1–15 bytes)"], ["Memory access", "only load and store touch memory", "many instructions can use memory operands"], ["Design goal", "one instruction per cycle, easy to pipeline", "fewer instructions per program"]])}
<p><b>Assembly language</b> is the human-readable form of machine code: one line per instruction. Here is a C statement and the RISC-V assembly a compiler might produce, with a, b, c in registers x10, x11, x12:</p>
{code('''
# C:  a = b + c - 5;
add  x10, x11, x12    # x10 = b + c
addi x10, x10, -5     # x10 = x10 - 5

# C:  if (a == 0) b = 1;
bne  x10, x0, skip    # x0 is always 0: branch if a != 0
addi x11, x0, 1       # b = 1
skip:
''', "asm")}
<p>An <b>assembler</b> translates assembly into binary machine code. A <b>compiler</b> translates a high-level language (C, Rust) into assembly. An <b>interpreter</b> (Python) runs a program by executing it statement by statement inside another program.</p>
''', pill=("r", "6.3"))

PERF = topic("performance", "Measuring performance", f'''
<p>How long a program takes depends on three things:</p>
{eq("CPU time = instruction count × CPI × clock period = (IC × CPI) / f")}
<p><b>CPI</b> is the average number of clock cycles per instruction. A compiler lowers IC, the microarchitecture lowers CPI, and the circuit and process technology raise f. Speeding up any one of them helps.</p>
{worked("A program runs 2 × 10⁹ instructions with an average CPI of 1.5 on a 3 GHz CPU. How long does it take?", "Time = (2 × 10⁹ × 1.5) / (3 × 10⁹) = 1.0 s.")}
<h3>Amdahl's law</h3>
<p>Speeding up part of a program only helps that part. If a fraction p of the time is improved by a factor s:</p>
{eq("Overall speedup = 1 / ((1 − p) + p / s)")}
{worked("80% of a program can run on many cores. With 8 cores, what is the speedup? With infinitely many?", "8 cores: 1 / (0.2 + 0.8/8) = 1 / 0.3 ≈ 3.33×. Infinite cores: 1 / 0.2 = 5×. The 20% that stays serial caps the gain.")}
''', pill=("p", "6.4"))

PIPE = topic("pipelining", "Pipelining", f'''
<p>A laundry analogy: wash, dry, fold. You don't wait for load 1 to be folded before washing load 2. A <b>pipelined</b> CPU splits each instruction into stages and works on several instructions at once, one per stage. The classic RISC pipeline has five:</p>
{table(["Stage", "What happens"], [["IF", "Instruction fetch"], ["ID", "Instruction decode and register read"], ["EX", "Execute in the ALU"], ["MEM", "Memory access (loads and stores)"], ["WB", "Write back the result to a register"]])}
{xlab("pipeline", ins=[{"t": "add x1, x2, x3"}, {"t": "sub x4, x1, x5", "dep": True}, {"t": "lw  x6, 0(x7)", "load": True}, {"t": "add x8, x6, x9", "dep": True}, {"t": "or  x10, x2, x3"}], title="5-stage pipeline", sub="Instruction 2 needs x1 from instruction 1, and instruction 4 needs x6 loaded by instruction 3.")}
<p>Ideally a pipeline finishes one instruction per cycle (CPI ≈ 1), even though each one takes 5 cycles from start to finish. <b>Hazards</b> break the ideal:</p>
{mini(("Data hazard", "An instruction needs a result that isn't written yet. Fixes: stall (insert bubbles) or forward the result straight from the ALU output."),
      ("Control hazard", "After a branch, the CPU doesn't know which instruction comes next. Modern CPUs predict the branch direction (often >95% correctly) and throw away the work if they guessed wrong."),
      ("Structural hazard", "Two instructions need the same hardware in the same cycle, such as one memory port. Fixed by duplicating hardware (separate instruction and data caches)."))}
{worked("A 5-stage pipeline runs 100 instructions with no stalls. How many cycles? What's the speedup over a non-pipelined CPU that takes 5 cycles per instruction?", "Pipelined: 5 + (100 − 1) = 104 cycles. Non-pipelined: 500. Speedup ≈ 4.8×, approaching 5× for long programs.")}
''', pill=("c", "6.5"))

MEMH = topic("memory", "The memory hierarchy and caches", f'''
<p>Fast memory is small and expensive; big memory is slow. Computers stack them:</p>
{table(["Level", "Typical size", "Typical access time"], [["Registers", "~1 KB", "< 1 ns"], ["L1 cache", "32–64 KB per core", "~1 ns"], ["L2 cache", "0.5–2 MB", "~4 ns"], ["L3 cache", "8–64 MB shared", "~10–20 ns"], ["Main memory (DRAM)", "8–64 GB", "~60–100 ns"], ["SSD", "0.5–4 TB", "~50–100 µs"], ["Hard disk", "1–20 TB", "~5–10 ms"]])}
<p>This works because programs have <b>locality</b>. <b>Temporal locality</b>: data used now will probably be used again soon (a loop counter). <b>Spatial locality</b>: data near what's used now will probably be used soon (the next element of an array). A cache keeps recently used data and loads it in <b>blocks</b> (lines) to exploit both.</p>
{xlab("cache", addrBits=6, lines=4, block=1, ways=1, seqs=[{"name": "array walk", "a": [0, 1, 2, 3, 0, 1, 2, 3]}, {"name": "conflict 0, 4, 0, 4", "a": [0, 4, 0, 4, 0, 4, 1, 5]}, {"name": "loop with reuse", "a": [8, 9, 10, 11, 8, 9, 10, 11, 12, 13]}])}
<p>An address is split into <b>tag | index | offset</b>. The offset picks a byte inside the block, the index picks which set to look in, and the tag is compared to check that it's the right block. In a <b>direct-mapped</b> cache each block has exactly one possible place, so two hot blocks with the same index keep kicking each other out (try the conflict sequence, then switch to 2-way). Bigger blocks help spatial locality (try 2- and 4-byte blocks on the array walk).</p>
{eq("Average memory access time = hit time + miss rate × miss penalty")}
{worked("L1 hits take 1 ns, the miss rate is 5%, and a miss costs 80 ns. AMAT?", "1 + 0.05 × 80 = 5 ns. Cutting the miss rate to 2% gives 1 + 1.6 = 2.6 ns, nearly twice as fast.")}
{box("tip", "Virtual memory", "Each program sees its own private address space. The operating system and a hardware unit (the MMU) translate these virtual addresses into physical RAM addresses in 4 KB pages, using a page table. A small cache of recent translations, the TLB, keeps this fast. Pages that don't fit in RAM can be swapped to disk.")}
''', pill=("p", "6.6"))

SUM = topic("summary-ce6", "Unit summary", mini(
 ("Architecture", "Von Neumann: program and data share memory. CPU = control unit + ALU + registers. PC points at the next instruction."),
 ("Cycle", "Fetch (MAR ← PC, IR ← M[MAR], PC++), decode (opcode + operand), execute. Loops and ifs are jumps."),
 ("Performance", "Time = IC × CPI / f. Amdahl: 1/((1 − p) + p/s). Pipelining → CPI ≈ 1; hazards cause stalls; forwarding and prediction help."),
 ("Memory", "Registers → caches → DRAM → SSD. Locality makes caches work. Address = tag | index | offset. AMAT = hit + miss rate × penalty."),
))

CH = [chapter("ch-cpu", "The Processor", "CPU", [ARCH, CYCLE]),
      chapter("ch-isa", "Instructions and Performance", "ISA & speed", [ISA, PERF, PIPE]),
      chapter("ch-mem", "Memory", "Memory", [MEMH, SUM])]

close(2e9 * 1.5 / 3e9, 1); close(1 / (0.2 + 0.8 / 8), 3.333); close(1 + .05 * 80, 5)
PQ = [
 q("What does the program counter (PC) hold?", ["The address of the next instruction", "The current instruction", "The result of the last calculation", "The number of instructions run"], 0, "The PC points into memory at what to fetch next.", "c"),
 q("In the von Neumann architecture, instructions and data are stored…", ["in the same memory", "in separate memories", "only in registers", "on the hard drive only"], 0, "The stored-program concept.", "c"),
 q("During fetch, after the instruction is read, the PC is…", ["incremented to point at the next instruction", "cleared", "copied into the ACC", "left alone"], 0, "So the next fetch gets the following instruction (unless a jump changes it).", "c"),
 q("The toy instruction 0011 1110 means…", ["ADD 14", "LOAD 14", "SUB 14", "STORE 3"], 0, "Opcode 0011 = ADD, address 1110 = 14.", "r"),
 q("ACC = 9 and memory[6] = 4. After SUB 6, ACC =", ["5", "13", "−5", "4"], 0, "9 − 4.", "r"),
 q("Which instruction makes a loop possible?", ["A jump back to an earlier address", "STORE", "OUT", "LOAD"], 0, "Jumps change the PC.", "c"),
 q("In RISC ISAs, which instructions access memory?", ["Only loads and stores", "Every instruction", "Only branches", "None"], 0, "Load/store architecture.", "c"),
 q("A program has 5 × 10⁸ instructions, CPI 2, clock 2 GHz. Run time?", ["0.5 s", "2 s", "0.25 s", "5 s"], 0, "5e8 × 2 / 2e9 = 0.5 s.", "p"),
 q("50% of a program is sped up 4×. Overall speedup?", ["1.6×", "2×", "4×", "2.5×"], 0, "1 / (0.5 + 0.5/4) = 1 / 0.625 = 1.6.", "p"),
 q("Ideal CPI of a pipelined processor is about…", ["1", "5", "0.2", "the number of stages"], 0, "One instruction completes per cycle once the pipeline is full.", "c"),
 q("A data hazard happens when…", ["an instruction needs a result that hasn't been written yet", "two programs share memory", "the cache is full", "the clock is too slow"], 0, "Read-after-write dependence.", "c"),
 q("What is forwarding (bypassing)?", ["Sending an ALU result directly to a later instruction without waiting for write-back", "Skipping an instruction", "Predicting a branch", "Sending data to the hard drive"], 0, "It removes most data-hazard stalls.", "c"),
 q("Looping over an array element by element mainly benefits from…", ["spatial locality", "temporal locality only", "virtual memory", "branch prediction"], 0, "Neighbouring addresses come in the same cache block.", "c"),
 q("Hit time 2 ns, miss rate 10%, miss penalty 50 ns. AMAT?", ["7 ns", "5 ns", "52 ns", "12 ns"], 0, "2 + 0.1 × 50 = 7 ns.", "p"),
 q("Which is fastest?", ["Registers", "L2 cache", "DRAM", "SSD"], 0, "Closest to the ALU, and tiny.", "c"),
 q("A 64-byte cache block with byte addresses needs how many offset bits?", ["6", "64", "8", "4"], 0, "2⁶ = 64.", "p"),
]
CHAL = [
 q("Trace the countdown program (LOAD 14; OUT; SUB 15; JZ 5; JMP 1; OUT; HALT with M[14] = 3, M[15] = 1). How many times is OUT executed?", ["4", "3", "5", "2"], 0, "Outputs 3, 2, 1 inside the loop, then 0 at address 5.", "r"),
 None,
 q("A cache has 8 lines, direct-mapped, 4-byte blocks, 10-bit addresses. How many tag bits?", ["5", "3", "2", "7"], 0, "Offset 2 bits, index 3 bits, tag 10 − 5 = 5.", "p"),
 q("With 90% of work parallelizable, what's the maximum speedup on any number of cores?", ["10×", "90×", "9×", "Infinite"], 0, "1 / 0.1.", "p"),
 q("A 5-stage pipeline (no forwarding, register file writes in the first half of a cycle and reads in the second) runs add x1,… then sub …,x1. How many stall cycles?", ["2", "1", "0", "3"], 0, "sub's ID must line up with add's WB (cycle 5); it would normally be in ID at cycle 3, so it waits 2 cycles.", "c"),
 q("Direct-mapped cache with 4 one-byte lines. Access sequence 0, 4, 8, 0, 4, 8. Hit rate?", ["0%", "50%", "33%", "100%"], 0, "All three map to index 0, so each access evicts the previous one. Every access misses.", "p"),
]
# fix the A vs B question with correct numbers
CHAL[1] = q("Machine A: 3 GHz, CPI 2.0. Machine B: 2 GHz, CPI 1.2. Same instructions. Which is faster, and by how much?", ["B, about 1.11× faster", "A, 1.5× faster", "A, about 1.11× faster", "They are equal"], 0, "Time per instruction: A = 2.0/3 GHz = 0.667 ns, B = 1.2/2 GHz = 0.6 ns. B is faster by 0.667/0.6 ≈ 1.11×. Higher clock speed alone doesn't decide it.", "p")
close((2 / 3) / (1.2 / 2), 1.111)
EXQ = [
 q("Which unit decodes instructions and controls the other parts?", ["Control unit", "ALU", "Cache", "Bus"], 0, "The ALU computes; the control unit directs.", "c"),
 q("MAR stands for…", ["Memory address register", "Main arithmetic register", "Machine accumulator register", "Memory array row"], 0, "It holds the address being accessed.", "c"),
 q("ACC = 3. Instructions: ADD 9 (M[9] = 4), STORE 10. Now M[10] =", ["7", "4", "3", "10"], 0, "3 + 4 = 7, then store.", "r"),
 q("JZ 8 with ACC = 5 does what?", ["Nothing; execution continues with the next instruction", "Jumps to 8", "Sets ACC to 0", "Halts"], 0, "Only jumps if ACC is zero.", "r"),
 q("A compiler translates…", ["a high-level language into assembly or machine code", "machine code into English", "assembly into a high-level language", "data into instructions at run time only"], 0, "Then an assembler makes the binary.", "c"),
 q("CPU time equals…", ["instruction count × CPI × clock period", "clock rate × CPI", "instruction count / CPI", "CPI × clock rate / instruction count"], 0, "IC × CPI × T.", "c"),
 q("Amdahl's law shows that…", ["the part you can't speed up limits the total speedup", "more cores always give linear speedup", "clock speed doubles every two years", "caches remove all memory delay"], 0, "Serial fraction caps the gain.", "c"),
 q("How many cycles does a 5-stage pipeline need for 20 instructions with no stalls?", ["24", "100", "20", "25"], 0, "5 + 19.", "p"),
 q("Branch prediction addresses which hazard?", ["Control hazards", "Data hazards", "Structural hazards", "Cache misses"], 0, "It guesses which way a branch goes.", "c"),
 q("A loop counter that's used every iteration shows…", ["temporal locality", "spatial locality", "no locality", "a structural hazard"], 0, "Same data reused soon.", "c"),
 q("In a cache address, the index bits choose…", ["which set to look in", "which byte in the block", "whether it's valid", "the tag"], 0, "Tag | index | offset.", "c"),
 q("Virtual memory translates…", ["virtual addresses into physical addresses", "assembly into machine code", "floats into integers", "cache tags into indexes"], 0, "Via page tables and the TLB.", "c"),
]
FRQS = [
 {"q": "Use the toy CPU (LOAD, STORE, ADD, SUB, JMP, JZ, OUT, HALT; 16 addresses).", "parts": [
  {"p": "(a) Write a program that outputs M[12] + M[13] − M[14].", "rubric": [["LOAD 12, ADD 13, SUB 14", 1], ["OUT then HALT", 1]], "answer": "0: LOAD 12; 1: ADD 13; 2: SUB 14; 3: OUT; 4: HALT."},
  {"p": "(b) Give the 8-bit machine code for your first two instructions.", "rubric": [["LOAD 12 = 0001 1100", 1], ["ADD 13 = 0011 1101", 1]], "answer": "LOAD 12 = 0001 1100; ADD 13 = 0011 1101."},
  {"p": "(c) Describe the register changes during the fetch of the instruction at address 1.", "rubric": [["MAR ← PC (1)", 1], ["IR ← M[1], PC ← 2", 1]], "answer": "MAR ← 1; MDR/IR ← memory[1] (ADD 13); PC ← 2. Then decode: opcode ADD, operand 13."}]},
 {"q": "Performance and memory.", "parts": [
  {"p": "(a) A program executes 4 × 10⁹ instructions: 50% ALU (CPI 1), 30% loads/stores (CPI 3), 20% branches (CPI 2). Find the average CPI and the time on a 2.5 GHz CPU.", "rubric": [["CPI = 0.5 + 0.9 + 0.4 = 1.8", 1], ["Time = 4e9 × 1.8 / 2.5e9 = 2.88 s", 1]], "answer": "CPI = 0.5(1) + 0.3(3) + 0.2(2) = 1.8. Time = 4 × 10⁹ × 1.8 / 2.5 × 10⁹ = 2.88 s."},
  {"p": "(b) A better cache cuts the load/store CPI from 3 to 2. What is the new time and the speedup?", "rubric": [["New CPI 1.5, time 2.4 s", 1], ["Speedup 1.2×", 1]], "answer": "CPI = 0.5 + 0.6 + 0.4 = 1.5 → 2.4 s. Speedup = 2.88/2.4 = 1.2×."},
  {"p": "(c) A direct-mapped cache has 16 lines and 16-byte blocks with 32-bit addresses. Give the number of offset, index and tag bits.", "rubric": [["Offset 4, index 4", 1], ["Tag 24", 1]], "answer": "Offset = log₂16 = 4, index = log₂16 = 4, tag = 32 − 8 = 24."}]},
]
build("comp-eng", "ce-6", L, 6, "Processors and Memory", 'Inside the <span class="hl">processor</span>', "Fetch–decode–execute, instruction sets and assembly, performance, pipelining and the memory hierarchy, with a CPU you can step through by hand.", "Intro to computer engineering unit 6: von Neumann architecture, fetch-decode-execute, assembly language, RISC vs CISC, CPU performance, Amdahl's law, pipelining, caches and virtual memory.", CH, PQ, CHAL, EXQ, FRQS, OUT, TAGS)
