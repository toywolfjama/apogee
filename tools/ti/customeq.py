"""Custom one-equation solver: pick an equation, pick the unknown letter, type the rest."""
from tilib import assign, show

def custom(eqs, back, pre="C"):
    """eqs: list of (title, expr_equal_to_zero, letters, legend_lines). Labels: {pre}0 menu, {pre}1.. eqs, {pre}Z solve."""
    code = []
    labs = [f"{pre}{'123456789ABCDEFGH'[i]}" for i in range(len(eqs))]
    first = eqs[:6]
    if len(eqs) <= 6:
        code += [f"Lbl {pre}0", f'Menu("CUSTOM EQUATION",' + ",".join(f'"{t}",{l}' for (t, *_), l in zip(eqs, labs)) + f',"BACK",{back}']
    else:
        code += [f"Lbl {pre}0", f'Menu("CUSTOM EQUATION",' + ",".join(f'"{t}",{l}' for (t, *_), l in zip(first, labs)) + f',"MORE",{pre}Y',
                 f"Lbl {pre}Y", f'Menu("MORE EQUATIONS",' + ",".join(f'"{t}",{l}' for (t, *_), l in zip(eqs[6:], labs[6:])) + f',"BACK",{pre}0']
    letters = []
    for (t, ex, lets, leg), l in zip(eqs, labs):
        assert len(t) <= 16 and len(leg) <= 6
        for ch in lets:
            if ch not in letters: letters.append(ch)
        code += [f"Lbl {l}", f'"{ex}"→Str1', f'"{lets}"→Str3', f'"{t}"→Str2', "ClrHome",
                 "Disp " + ",".join(f'"{x}"' for x in [t] + leg), f"Goto {pre}Z"]
    code += [f"Lbl {pre}Z", 'Disp "FIND WHICH LETTER?"', 'Input "LETTER? ",Str4',
             "If inStr(Str3,Str4)=0", "Then", 'Disp "NOT IN THIS EQUATION"', "Pause", "End",
             "If inStr(Str3,Str4)=0", f"Goto {pre}0",
             "String►Equ(Str1,Y₁", "ClrHome", 'Disp "TYPE EACH VALUE"',
             '"EQUATION!"+Str2+"!KNOWN VALUES"→Str0',
             "For(I,1,length(Str3", "sub(Str3,I,1)→Str5", "If Str5≠Str4", "Then",
             'Disp Str5+" ="', "Input Z"]
    for ch in letters:
        code += [f'If Str5="{ch}"', f"Z→{ch}"]
    code += ['Str0+"!"+Str5+"="+toString(Z)→Str0', "End", "End"]
    for ch in letters:
        guess = "45" if ch == "θ" else "1"
        code += [f'If Str4="{ch}"', f"solve(Y₁,{ch},{guess})→Z"]
    code += ['Str0+"!SOLVE FOR "+Str4+"!"+Str4+"="+toString(round(Z,4))→Str0'] + show(f"{pre}0")
    return code
