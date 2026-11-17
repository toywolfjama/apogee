"""Shared pieces for the TI-84 Plus CE programs.
- work(): turn work lines with {expr} placeholders into TI code that builds Str0
- viewer(): the scrollable WORK + ANSWER screen and its exit menu
- solver(): one guided solver = prompts with units, math, work screen
- slides(): notes slides stored in Str9 (7 lines x 16 chars)
- build(): fix negatives, check labels/menus, save .8xp and a .txt listing"""
import re
from tivars import TIProgram

def _seg(ln):
    parts = re.split(r'\{([^{}]+)\}', ln)
    seg = []
    for i, p in enumerate(parts):
        if i % 2 == 0:
            p = p.replace(':', '').replace('"', "'")
            if p: seg.append('"' + p + '"')
        else:
            seg.append(f'toString(round({p},3))')
    return "+".join(seg) if seg else '" "'

def assign(lines, append=False):
    out, chunk = [], []
    # keep each line of code a reasonable length: 6 work lines per statement
    for i in range(0, len(lines), 6):
        part = '+"!"+'.join(_seg(l) for l in lines[i:i + 6])
        first = (i == 0 and not append)
        out.append(("" if first else 'Str0+"!"+') + part + "→Str0")
    return out

def cond(c, lines, else_lines=None):
    code = [f"If {c}", "Then"] + assign(lines, True)
    if else_lines:
        code += ["Else"] + assign(else_lines, True)
    return code + ["End"]

def show(ret):
    """End of a solver: open the work screen, come back to `ret` after."""
    return [f'"{ret}"→Str7', "Goto WK"]

def viewer(rets, fallback):
    v = ["Lbl WK",
         "{I,J,K,L,T}→L₆",
         'If sub(Str0,1,1)≠"!"', '"!"+Str0→Str0', '"WORK AND ANSWER"+Str0→Str0',
         '" "→Str6', "1→I", "length(Str0)→L",
         "While I≤L",
         'inStr(Str0,"!",I)→J', "If J=0", "L+1→J",
         "If J>I", "Then", "sub(Str0,I,J-I)→Str5", "Else", '" "→Str5', "End",
         "While length(Str5)>26", "Str6+sub(Str5,1,26)→Str6", "sub(Str5,27,length(Str5)-26)→Str5", "End",
         "If length(Str5)<26", 'Str5+sub("                          ",1,26-length(Str5))→Str5',
         "Str6+Str5→Str6", "J+1→I", "End",
         "sub(Str6,2,length(Str6)-1)→Str6", "length(Str6)/26→L",
         "Lbl WW", "0→T",
         "Lbl WP", "ClrHome", "For(I,1,9", "If 9T+I≤L", "Output(I,1,sub(Str6,26(9T+I-1)+1,26", "End",
         'Output(10,1,"UP/DOWN=MORE CLEAR=DONE"',
         "0→K", "Repeat max(K={25,34,45,105", "getKey→K", "End",
         "If K=45", "Goto WX",
         "If K=105 and 9T+9≥L", "Goto WX",
         "If K=25 and T>0", "T-1→T",
         "If (K=34 or K=105) and 9T+9<L", "T+1→T",
         "Goto WP",
         "Lbl WX",
         'Menu("DONE","SEE WORK AGAIN",WW,"CONTINUE",WR,"MAIN MENU",M',
         "Lbl WR",
         "L₆(1)→I", "L₆(2)→J", "L₆(3)→K", "L₆(4)→L", "L₆(5)→T"]
    for r in sorted(set(rets)):
        v += [f'If Str7="{r}"', f"Goto {r}"]
    return v + [f"Goto {fallback}"]

def solver(lab, title, hints, inputs, calc, work, ret, extra=None):
    """inputs: list of (var, name, unit). Prompt = 'NAME (UNIT) '.
    work: list of lines with {expr}; extra: TI code appended after work (e.g. cond())."""
    code = [f"Lbl {lab}", "ClrHome"]
    disp = [title] + list(hints)
    assert len(title) <= 26 and all(len(h) <= 26 for h in hints), (lab, title, hints)
    assert len(disp) + len(inputs) <= 10, (lab, "screen too full")
    code.append("Disp " + ",".join(f'"{d}"' for d in disp))
    for var, name, unit in inputs:
        p = f"{name} ({unit}) " if unit else f"{name} "
        assert len(p) <= 16, (lab, p)
        code.append(f'Input "{p}",{var}')
    code += calc
    given = ["GIVEN"] + [f"{name}={{{var}}}" + (f" {unit}" if unit else "") for var, name, unit in inputs]
    code += assign(given + list(work))
    if extra:
        code += extra
    code += show(ret)
    return code

ALLOWED = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 +-*/=().,'²θ<>?!≤")

def slides(sections):
    """sections: list of (title, [slide lines...]). Returns (code, ranges)."""
    flat, ranges = [], {}
    for title, ss in sections:
        start = len(flat) + 1
        for sl in ss:
            assert len(sl) <= 7, (title, sl)
            for ln in sl:
                bad = set(ln) - ALLOWED
                assert not bad, (ln, bad)
                assert len(ln) <= 16, (ln, len(ln))
            flat.append([ln.ljust(16) for ln in sl] + [" " * 16] * (7 - len(sl)))
        ranges[title] = (start, len(flat))
    code = []
    for i, lines in enumerate(flat):
        code.append(('"' if i == 0 else 'Str9+"') + "".join(lines) + '"→Str9')
    return code, ranges

def slide_viewer(back):
    return ["Lbl S", "A→N", "Lbl D", "ClrHome", "For(I,1,7",
            "Output(I,1,sub(Str9,112(N-1)+16(I-1)+1,16", "End",
            'Output(8,1,"< >MOVE CLR=MENU"', "0→K", "Repeat max(K={24,26,45", "getKey→K", "End",
            f"If K=45", f"Goto {back}", "If K=26 and N<B", "N+1→N", "If K=24 and N>A", "N-1→N", "Goto D"]

def fix_neg(line):
    out = []; inq = False; prev = ""
    for ch in line:
        if ch == '"': inq = not inq
        if ch == "-" and not inq and (prev == "" or prev in "(,=→+*/<>≤≥≠{"):
            ch = "⁻"
        out.append(ch)
        if not inq and ch != " ": prev = ch
        elif inq: prev = ch if ch == '"' else prev
    return "".join(out)

def split_args(s):
    out = []; depth = 0; inq = False; cur = ""
    for ch in s:
        if ch == '"': inq = not inq
        if not inq:
            if ch in "({": depth += 1
            elif ch in ")}": depth -= 1
            elif ch == "," and depth == 0: out.append(cur); cur = ""; continue
        cur += ch
    out.append(cur); return out

def check(lines):
    labels = [l[4:] for l in lines if l.startswith("Lbl ")]
    dup = {x for x in labels if labels.count(x) > 1}
    assert not dup, ("duplicate labels", dup)
    for x in labels:
        assert re.fullmatch(r"[A-Zθ0-9]{1,2}", x), ("bad label", x)
    targets = set()
    for l in lines:
        if l.startswith("Goto "): targets.add(l[5:])
        if l.startswith("Menu("):
            a = split_args(l[5:])
            assert len(a) % 2 == 1 and (len(a) - 1) // 2 <= 7, ("menu size", l)
            assert len(a[0].strip('"')) <= 16, ("menu title", l)
            for t, lab in zip(a[1::2], a[2::2]):
                assert len(t.strip('"')) <= 16, ("menu item", t)
                targets.add(lab.strip())
        if l.startswith("If ") and "Goto" in l: pass
        for m in re.finditer(r'"([^"]*)"', l):
            s = m.group(1)
            assert "->" not in s and "@" not in s and ("π" not in s or l.endswith("→Str1")), ("bad string", l)
    # Str7 targets
    for l in lines:
        m = re.match(r'^"(\w+)"→Str7$', l)
        if m: targets.add(m.group(1))
    missing = targets - set(labels)
    assert not missing, ("missing labels", missing)
    depth = 0
    for l in lines:
        if l == "Then" or l.startswith("While ") or l.startswith("For(") or l.startswith("Repeat "): depth += 1
        if l == "End": depth -= 1
        assert depth >= 0, ("End without block", l)
    assert depth == 0, ("unclosed blocks", depth)
    for l in lines:
        if l.startswith("Disp "):
            for a in split_args(l[5:]):
                a = a.strip()
                if a.startswith('"') and a.endswith('"') and a.count('"') == 2:
                    assert len(a) - 2 <= 26, ("disp too long", a)
    return labels

def build(name, lines, outdir="."):
    lines = [fix_neg(l) for l in lines]
    labels = check(lines)
    src = "\n".join(lines)
    from tivars.tokenizer.encoder import encode
    # equation strings (→Str1) must hold real tokens like cos( and π for String►Equ, so they use max munch
    parts = []
    def outside(l, f):
        seg = l.split('"')
        for k in range(0, len(seg), 2): seg[k] = f(seg[k])
        return '"'.join(seg)
    fixed = []
    for l in lines:
        mode = "max" if l.endswith("→Str1") else "smart"
        if l == "Pause": l = "Pause "                      # tivars' name for the Pause token
        l = outside(l, lambda t: t.replace("inStr(", "inString(").replace("R²", "R^2").replace("π", "pi"))
        if mode == "max": l = l.replace("R²", "R^2").replace("π", "pi")
        fixed.append(l)
        parts.append(encode(l, mode=mode)[0])
    lines = fixed
    prog = TIProgram(name=name)
    prog.data = b"\x3f".join(parts)
    prog.save(f"{outdir}/{name}.8xp")
    with open(f"{outdir}/{name}.txt", "w") as fh:
        fh.write(f"{name} (TI-84 Plus CE) - TI-BASIC source\n")
        fh.write("Every line below is one program line. → is the STO> key.\n\n")
        fh.write("\n".join(":" + l for l in lines) + "\n")
    # round-trip: make sure every line tokenized (no raw unknown text)
    back = TIProgram.open(f"{outdir}/{name}.8xp").string()
    assert back.count("\n") == src.count("\n"), "line count changed after tokenizing"
    # token audit: no lowercase-letter or statistics/window tokens outside strings
    from tivars.models import TI_84PCE
    T = TI_84PCE.tokens.bytes
    TWO = {0x5C, 0x5D, 0x5E, 0x60, 0x61, 0x62, 0x63, 0x7E, 0xAA, 0xBB, 0xEF}
    for n, part in enumerate(parts):
        i = 0; inq = False
        while i < len(part):
            b = part[i]; tok = part[i:i + 2] if b in TWO else bytes([b])
            if b == 0x2A: inq = not inq
            elif not inq:
                bad = b in (0x62, 0x63, 0x5C, 0x60, 0x61, 0x7E) or (b == 0xBB and 0xB0 <= part[i + 1] <= 0xCA and part[i + 1] != 0xBB)
                assert not bad, ("odd token", T[tok].langs["en"].display if tok in T else tok.hex(), lines[n])
            i += len(tok)
    print(name, "bytes", len(prog.data), "lines", len(lines), "labels", len(labels))
    return prog
