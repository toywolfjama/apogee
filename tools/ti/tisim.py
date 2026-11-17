"""Minimal TI-BASIC interpreter for the subset these programs use, to run solvers with scripted input.
Not a full emulator: enough to catch math errors, undefined vars, bad strings and broken control flow."""
import math, re
from tivars import TIProgram

class TIError(Exception): pass
class Done(Exception): pass

FUNCS = {
 "sin(": "_sin(", "cos(": "_cos(", "tan(": "_tan(", "sin⁻¹(": "_asin(", "cos⁻¹(": "_acos(", "tan⁻¹(": "_atan(",
 "√(": "_sqrt(", "round(": "_round(", "toString(": "_tostr(", "sub(": "_sub(", "inStr(": "_instr(",
 "length(": "_len(", "inString(": "_instr(", "max(": "_max(", "min(": "_min(", "abs(": "abs(", "R►Pr(": "_rpr(", "R►Pθ(": "_rpt(",
 "sum(": "_sum(", "int(": "_int(", "solve(": "_solve(", "dim(": "_len(",
}
VARNAMES = {"θ": "TH"}

def tok_expr(e):
    """Translate a TI expression to Python source."""
    out = []; i = 0; prev = None  # prev kind: 'val' or 'op'
    closers = []
    def push(s, kind):
        nonlocal prev
        if kind in ("val", "open") and prev == "val":
            out.append("*")
        out.append(s); prev = "val" if kind in ("val", "close") else ("op" if kind != "open" else "op")
    while i < len(e):
        c = e[i]
        if c == '"':
            j = e.find('"', i + 1)
            if j < 0: j = len(e)
            push(repr(e[i + 1:j]), "val"); i = j + 1; continue
        if c == " ": i += 1; continue
        m = None
        for f in sorted(FUNCS, key=len, reverse=True):
            if e.startswith(f, i): m = f; break
        if m: push(FUNCS[m], "open"); closers.append(")"); i += len(m); continue
        if e.startswith("Str", i) and i + 3 < len(e) and e[i + 3].isdigit():
            push(f"S['Str{e[i+3]}']", "val"); i += 4; continue
        if e.startswith("L₆", i) or e.startswith("L₁", i) or e.startswith("L₂", i) or e.startswith("L₃", i):
            if i + 2 < len(e) and e[i + 2] == "(":
                push(f"LST('{e[i:i+2]}')[_ix(", "val"); closers.append(")]"); prev = "op"; i += 3; continue
            push(f"LST('{e[i:i+2]}')", "val"); i += 2; continue
        if e.startswith("Y₁", i): push("'Y1'", "val"); i += 2; continue
        if e.startswith(" and ", i - 1) or e.startswith("and ", i):
            if e.startswith("and", i): push(" and ", "op"); i += 3; continue
        if e.startswith("or", i) and (i + 2 < len(e) and e[i + 2] in " ("):
            push(" or ", "op"); i += 2; continue
        if c in "0123456789.":
            m = re.match(r"\d*\.?\d+(ᴇ⁻?\d+)?|\d+\.", e[i:])
            t = m.group(0).replace("ᴇ⁻", "e-").replace("ᴇ", "e")
            push("(" + t + ")", "val"); i += len(m.group(0)); continue
        if c == "π": push("math.pi", "val"); i += 1; continue
        if c.isupper() or c == "θ":
            push(f"V['{VARNAMES.get(c, c)}']", "val"); i += 1; continue
        if c == "(": push("(", "open"); closers.append(")"); i += 1; continue
        if c == "{": push("TL([", "open"); closers.append("])"); i += 1; continue
        if c in ")}":
            if not closers: raise TIError("too many ) in " + e)
            out.append(closers.pop()); prev = "val"; i += 1; continue
        if c == "²": out.append("**2"); prev = "val"; i += 1; continue
        if c == "⁻": out.append("-"); prev = "op"; i += 1; continue
        ops = {"=": "==", "≠": "!=", "≤": "<=", "≥": ">=", "^": "**", "*": "*", "/": "/", "+": "+", "-": "-", "<": "<", ">": ">", ",": ","}
        if c in ops:
            if c == "-" and prev != "val":
                raise TIError("SYNTAX: subtraction minus used as negative in " + e)
            out.append(ops[c]); prev = "op"; i += 1; continue
        raise TIError(f"unknown token {c!r} in {e}")
    # close missing parens (TI allows)
    return "".join(out) + "".join(reversed(closers))

class TL(list):
    def _op(self, o, f):
        if isinstance(o, list): return TL(f(a, b) for a, b in zip(self, o))
        return TL(f(a, o) for a in self)
    def __eq__(self, o): return self._op(o, lambda a, b: float(a == b))
    def __ne__(self, o): return self._op(o, lambda a, b: float(a != b))
    def __mul__(self, o): return self._op(o, lambda a, b: a * b)
    __rmul__ = __mul__
    def __add__(self, o): return self._op(o, lambda a, b: a + b)
    __radd__ = __add__
    def __sub__(self, o): return self._op(o, lambda a, b: a - b)
    def __truediv__(self, o): return self._op(o, lambda a, b: a / b)
    def __pow__(self, o): return self._op(o, lambda a, b: a ** b)

def split_top(s, sep=","):
    out = []; d = 0; q = False; cur = ""
    for ch in s:
        if ch == '"': q = not q
        if not q:
            if ch in "({": d += 1
            elif ch in ")}": d -= 1
            elif ch == sep and d == 0: out.append(cur); cur = ""; continue
        cur += ch
    out.append(cur); return out

class Calc:
    def __init__(self, src, script, maxsteps=200000, verbose=False):
        self.lines = src.split("\n") if isinstance(src, str) else src
        self.labels = {l[4:]: i for i, l in enumerate(self.lines) if l.startswith("Lbl ")}
        self.V = {k: 0.0 for k in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}; self.V["TH"] = 0.0
        self.S = {}; self.L = {}; self.Y1 = None
        self.script = list(script); self.works = []; self.screens = []; self.maxsteps = maxsteps
        self.verbose = verbose; self.menus = []; self.leak = 0
    # ---- functions
    def env(self):
        d = math.radians
        def chk(x):
            if isinstance(x, complex): raise TIError("NONREAL ANS")
            return x
        def sqrt(x):
            if x < 0: raise TIError("NONREAL ANS sqrt(%s)" % x)
            return math.sqrt(x)
        def tostr(x):
            if isinstance(x, str): raise TIError("DATA TYPE toString(str)")
            if float(x).is_integer() and abs(x) < 1e10: return str(int(x)).replace("-", "⁻")
            return ("%.10g" % x).replace("-", "⁻").replace("e", "ᴇ")
        def rnd(x, n=9):
            return round(x, int(n))
        def sub(s, a, n):
            a, n = int(a), int(n)
            if not isinstance(s, str): raise TIError("DATA TYPE sub")
            if a < 1 or n < 1 or a + n - 1 > len(s): raise TIError(f"INVALID DIM sub(len {len(s)},{a},{n})")
            return s[a - 1:a - 1 + n]
        def instr(s, t, a=1):
            k = s.find(t, int(a) - 1); return k + 1
        def solve(expr, var, guess):
            raise TIError("SOLVE_STUB")
        def div0(x): return x
        def LST(name):
            if name not in self.L: raise TIError("UNDEFINED list " + name)
            return TL(self.L[name])
        return {"_ix": lambda x: int(x) - 1, "TL": TL, "math": math, "V": self.V, "S": self.Sget(), "LST": LST,
                "_sin": lambda x: math.sin(d(x)), "_cos": lambda x: math.cos(d(x)), "_tan": lambda x: math.tan(d(x)),
                "_asin": lambda x: math.degrees(math.asin(x)), "_acos": lambda x: math.degrees(math.acos(x)),
                "_atan": lambda x: math.degrees(math.atan(x)), "_sqrt": sqrt, "_round": rnd, "_tostr": tostr,
                "_sub": sub, "_instr": instr, "_len": len, "_max": lambda *a: max(a[0]) if len(a) == 1 else max(a),
                "_min": lambda *a: min(a[0]) if len(a) == 1 else min(a),
                "_rpr": lambda x, y: math.hypot(x, y), "_rpt": lambda x, y: math.degrees(math.atan2(y, x)),
                "_sum": sum, "_int": math.floor, "_solve": self.solve}
    def Sget(self):
        me = self
        class SD(dict):
            def __getitem__(s, k):
                if k not in me.S: raise TIError("UNDEFINED " + k)
                return me.S[k]
        return SD()
    def solve(self, y, var, guess):
        expr = tok_expr(self.Y1)
        name = None
        # var passed as its value; find which var by scanning Str4
        letter = self.S["Str4"]; key = VARNAMES.get(letter, letter)
        def f(x):
            old = self.V[key]; self.V[key] = x
            try: return eval(expr, self.env())
            finally: self.V[key] = old
        x = float(guess)
        for _ in range(200):
            h = 1e-6 * max(1, abs(x)); fx = f(x); dfx = (f(x + h) - fx) / h
            if dfx == 0: break
            nx = x - fx / dfx
            if abs(nx - x) < 1e-12: x = nx; break
            x = nx
        return x
    def ev(self, e):
        py = tok_expr(e)
        try:
            v = eval(py, self.env())
        except TIError: raise
        except ZeroDivisionError: raise TIError("DIVIDE BY 0 in " + e)
        except ValueError as x: raise TIError(f"DOMAIN {x} in {e}")
        except OverflowError: raise TIError("OVERFLOW in " + e)
        except Exception as x: raise TIError(f"{type(x).__name__} {x} in {e} -> {py}")
        if isinstance(v, bool): v = 1.0 if v else 0.0
        if isinstance(v, list) and not isinstance(v, TL): v = TL(v)
        return v
    def store(self, val, tgt):
        tgt = tgt.strip()
        if tgt.startswith("dim("):
            n = tgt[4:].rstrip(")"); k = int(val)
            cur = self.L.get(n, []); self.L[n] = (cur + [0.0] * k)[:k]; return
        m = re.match(r"^(L.)\((.+?)\)?$", tgt)
        if m and len(tgt) > 2:
            n = m.group(1); idx = int(self.ev(m.group(2)))
            if n not in self.L or not 1 <= idx <= len(self.L[n]): raise TIError("INVALID DIM " + tgt)
            self.L[n][idx - 1] = float(val); return
        if tgt.startswith("Str"):
            if not isinstance(val, str) and getattr(self, "auto", None): val = "M"
            if not isinstance(val, str): raise TIError("DATA TYPE store to " + tgt)
            self.S[tgt] = val
        elif tgt.startswith("L") and len(tgt) > 1:
            self.L[tgt] = list(val)
        else:
            if isinstance(val, (str, list)): raise TIError("DATA TYPE store to " + tgt)
            self.V[VARNAMES.get(tgt, tgt)] = float(val)
    def take(self, kind):
        if not self.script and getattr(self, "auto", None) and kind in self.auto:
            return self.auto[kind]()
        if not self.script: raise Done()
        k, v = self.script.pop(0)
        if k != kind: raise TIError(f"script expected {kind}, got {k}={v}")
        return v
    def find_end(self, i, stop_else=False):
        d = 0; j = i + 1
        while j < len(self.lines):
            l = self.lines[j]
            if l == "Then" or l.startswith(("While ", "For(", "Repeat ")): d += 1
            elif l == "End":
                if d == 0: return j
                d -= 1
            elif l == "Else" and d == 0 and stop_else: return j
            j += 1
        raise TIError("missing End")
    def run(self, start=0):
        pc = start; stack = []; steps = 0
        L = self.lines
        try:
            while pc < len(L):
                steps += 1
                if steps > self.maxsteps: raise TIError("too many steps (infinite loop?)")
                l = L[pc]
                if l.startswith("Lbl ") or l == "" or l == "Degree" or l.startswith("Pause") or l == "ClrHome":
                    pc += 1; continue
                if l.startswith("Goto "):
                    lab = l[5:]
                    if lab not in self.labels: raise TIError("LABEL " + lab)
                    if stack: self.leak += 1
                    stack = []
                    if lab == "WK": self.works.append(self.S.get("Str0", ""))
                    pc = self.labels[lab]; continue
                if l.startswith("Menu("):
                    a = split_top(l[5:])
                    items = [x.strip().strip('"') for x in a[1::2]]; tg = [x.strip() for x in a[2::2]]
                    self.menus.append(a[0].strip('"'))
                    want = self.take("menu")
                    if want not in items: raise TIError(f"menu {a[0]} has no {want}: {items}")
                    pc = self.labels[tg[items.index(want)]]; stack = []; continue
                if l.startswith("Input"):
                    m = re.match(r'Input(?: "([^"]*)",)?\s*(\S+)$', l)
                    var = m.group(2)
                    v = self.take("in")
                    self.store(v, var); pc += 1; continue
                if l.startswith("Disp "):
                    for a in split_top(l[5:]):
                        self.screens.append(self.ev(a))
                    pc += 1; continue
                if l.startswith("Output("):
                    a = split_top(l[7:].rstrip(")"))
                    self.ev(a[2]); pc += 1; continue
                if l.startswith("String►Equ("):
                    a = split_top(l[len("String►Equ("):])
                    self.Y1 = self.ev(a[0]); pc += 1; continue
                if l.startswith("If "):
                    c = self.ev(l[3:])
                    if pc + 1 < len(L) and L[pc + 1] == "Then":
                        if c:
                            stack.append(("if",)); pc += 2
                        else:
                            j = self.find_end(pc + 1, stop_else=True)
                            if L[j] == "Else": stack.append(("if",))
                            pc = j + 1
                        continue
                    pc += 1 if c else 2; continue
                if l == "Else":
                    j = self.find_end(pc); stack.pop(); pc = j + 1; continue
                if l.startswith("While "):
                    if self.ev(l[6:]): stack.append(("while", pc)); pc += 1
                    else: pc = self.find_end(pc) + 1
                    continue
                if l.startswith("Repeat "):
                    stack.append(("repeat", pc)); pc += 1; continue
                if l.startswith("For("):
                    a = split_top(l[4:].rstrip(")"))
                    var = a[0]; lo = self.ev(a[1]); hi = self.ev(a[2])
                    self.store(lo, var)
                    if lo <= hi: stack.append(("for", pc, var, hi)); pc += 1
                    else: pc = self.find_end(pc) + 1
                    continue
                if l == "End":
                    if not stack: raise TIError("End without block at %d" % pc)
                    top = stack[-1]
                    if top[0] == "if": stack.pop(); pc += 1; continue
                    if top[0] == "while":
                        stack.pop(); pc = top[1]; continue
                    if top[0] == "repeat":
                        if self.ev(L[top[1]][7:]): stack.pop(); pc += 1
                        else: pc = top[1] + 1
                        continue
                    if top[0] == "for":
                        _, fp, var, hi = top; v = self.V[VARNAMES.get(var, var)] + 1; self.store(v, var)
                        if v <= hi: pc = fp + 1
                        else: stack.pop(); pc += 1
                        continue
                if "→" in l:
                    e, t = l.rsplit("→", 1)
                    if t.strip() == "K" and e.strip() == "getKey":
                        self.V["K"] = float(self.take("key")); pc += 1; continue
                    self.store(self.ev(e), t); pc += 1; continue
                if l.startswith('"') or l.startswith("Str"):
                    pc += 1; continue
                raise TIError("unhandled line: " + l)
        except Done:
            return "done"
        return "end"

def load(path):
    return TIProgram.open(path).string().replace("\\'", "'").split("\n")

def works_text(s):
    return s.replace("!", "\n  ")
