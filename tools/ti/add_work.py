"""Adds a SHOW WORK option to every solver in solver.txt -> solver_work.txt.
Work lines use {expr} placeholders that become toString(round(expr,3))."""
import re

def S(*lines):
    """Build TI code assigning lines (joined by '!') to Str0."""
    out = []
    for ln in lines:
        parts = re.split(r'\{([^{}]+)\}', ln)
        seg = []
        for i, p in enumerate(parts):
            if i % 2 == 0:
                p = p.replace(':', '')
                if p: seg.append('"' + p + '"')
            else:
                seg.append(f'toString(round({p},3))')
        out.append("+".join(seg) if seg else '" "')
    return out

def assign(lines, append=False):
    segs = S(*lines)
    expr = '+"!"+'.join(segs)
    return [("Str0+\"!\"+" if append else "") + expr + "→Str0"]

def cond(c, lines, else_lines=None):
    code = [f"If {c}", "Then"] + assign(lines, True)
    if else_lines:
        code += ["Else"] + assign(else_lines, True)
    return code + ["End"]

def menu(ret):
    return [f'"{ret}"→Str7', "Goto WK"]

W = {}
W["Y1"] = ("YH", assign(["E=E' (MASS CANCELS)", "1/2V2²=1/2V1²+G(H1-H2)", "V2²=V1²+2G(H1-H2)",
                         "V2²={U}²+2*{G}*({H}-{J})", "V2²={R}"]) +
           cond("R≥0", ["V2=SQRT({R})", "V2={√(R)} M/S"], ["NEGATIVE, CANT REACH"]))
W["Y2"] = ("YH", assign(["E=E'", "1/2V²+GH1=GH2", "H2=H1+V²/(2G)", "H2={H}+{U}²/(2*{G})",
                         "H2={H}+{U²/(2G)}", "H2={R} M"]))
W["Y7"] = ("YH", assign(["HEAT=E BEFORE-E AFTER", "E BEFORE=MGH+1/2MV²", "={MGH}+{.5MU²}", "={MGH+.5MU²} J",
                         "E AFTER=MGH+1/2MV²", "={MGJ}+{.5MV²}", "={MGJ+.5MV²} J", "HEAT={MGH+.5MU²}-{MGJ+.5MV²}",
                         "HEAT={R} J"]))
W["X1"] = ("Y3", assign(["W=CHANGE IN KE", "D GOES WITH V²", "D2=D1*(SPEED TIMES)²", "D2={D}*({S})²",
                         "D2={D}*{S²}", "D2={DS²} M"]))
W["X2"] = ("Y3", assign(["F*D=1/2MV²", "D=MV²/(2F)", "D={M}*{V}²/(2*{F})", "D={MV²}/{2F}", "D={MV²/(2F)} M"]))
W["X3"] = ("Y3", assign(["F*D=1/2MV²", "F=MV²/(2D)", "F={M}*{V}²/(2*{D})", "F={MV²}/{2D}", "F={MV²/(2D)} N"]))
W["X4"] = ("Y3", assign(["FKF*D=1/2MV²", "MU*MG*D=1/2MV²", "D=V²/(2*MU*G)", "D={V}²/(2*{Q}*{G})",
                         "D={V²}/{2QG}", "D={V²/(2QG)} M", "T=V/(MU*G)={V}/{QG}", "T={V/(QG)} S"]))
W["Y4"] = ("Z1", assign(["W=F*D*COS θ", "W={F}*{D}*COS({θ})", "W={F}*{D}*{cos(θ)}", "W={W} J"]) +
           cond("T>0", ["P=W/T={W}/{T}", "P={W/T} W"]))
W["Y6"] = ("YS", assign(["US=1/2KX²", "US=.5*{K}*{X}²", "US={R} J"]) +
           cond("M>0", ["1/2KX²=1/2MV²", "V=X*SQRT(K/M)", "V={X}*SQRT({K}/{M})", "V={X√(K/M)} M/S",
                        "1/2KX²=MGH", "H={R}/({M}*{G})", "H={R/(MG)} M"]))
W["S1"] = ("YS", assign(["1/2MV²=1/2KX²", "X=V*SQRT(M/K)", "X={V}*SQRT({M}/{K})", "X={V√(M/K)} M"]))
W["S2"] = ("YS", assign(["1/2KX²=MU*MG*D", "1/2KX²=.5*{K}*{X}²={R}", "MU*MG={Q}*{M}*{G}={QMG}",
                         "D={R}/{QMG}", "D={R/(QMG)} M"]))
W["YP"] = ("Z1", assign(["H=L(1-COS θ)", "H={L}(1-COS {θ})", "H={L}(1-{cos(θ)})", "H={H} M", "V=SQRT(2GH)",
                         "V=SQRT(2*{G}*{H})", "V={V} M/S"]) +
           cond("M>0", ["T=MG+MV²/L", "T={MG}+{M}*{V}²/{L}", "T={MG}+{MV²/L}", "T={MG+MV²/L} N"]))
W["C5"] = ("C1", assign(["TOP: MG=MV²/R", "V²=GR={G}*{R}={GR}", "MGH=MG(2R)+1/2M(GR)", "H=2R+.5R=2.5R",
                         "H=2.5*{R}={2.5R} M", "MIN V TOP=SQRT({GR})={√(GR)}"]))
W["C6"] = ("C1", assign(["LOOP TOP=2R={2R} M", "V²=V0²+2G(H-2R)", "V²={U}²+2*{G}*({H}-{2R})", "V²={S}"]) +
           cond("S≥0", ["V={√(S)} M/S", "TOP: N+MG=MV²/R", "N=MV²/R-MG", "N={M}*{S}/{R}-{MG}",
                        "N={MS/R}-{MG}", "N={MS/R-MG} N"], ["NEGATIVE, NEVER GETS THERE"]))
W["C7"] = ("C1", assign(["BOTTOM: N-MG=MV²/R", "N=MG+MV²/R", "N={MG}+{M}*{V}²/{R}", "N={MG}+{MV²/R}",
                         "N={MG+MV²/R} N"]))
W["C2"] = ("Z3", assign(["SPEED THERE V={V}"]) +
           cond("Z=2", ["VALLEY: N-MG=MV²/R", "N=MG+MV²/R", "N={MG}+{M}*{V}²/{R}", "N={MG}+{MV²/R}", "N={N} N"],
                ["HILL: MG-N=MV²/R", "N=MG-MV²/R", "N={MG}-{M}*{V}²/{R}", "N={MG}-{MV²/R}", "N={N} N"]))
W["C3"] = ("Z3", assign(["W=MGH", "W={M}*{G}*{H}", "W={MGH} J", "P=W/T={MGH}/{T}", "P={MGH/T} W"]))
W["C4"] = ("Z3", assign(["H=L*SIN θ={L}*{sin(θ)}", "H={H} M", "FN=MG*COS θ={MG}*{cos(θ)}", "FN={N} N",
                         "FKF=MU*FN={Q}*{N}={F} N", "HEAT=FKF*L={F}*{L}={FL} J",
                         "A=G SIN θ-MU G COS θ={A}", "V²=V0²+2AL", "V²={U}²+2*{A}*{L}={S}"]) +
           cond("S≥0", ["V=SQRT({S})={√(S)} M/S"], ["NEGATIVE, STOPS ON RAMP"]))
W["B2"] = ("Z4", assign(["F=MG={M}*{G}={MG} N", "W=MGH={MG}*{H}", "W={MGH} J"]) +
           cond("T>0", ["P=W/T={MGH}/{T}={MGH/T} W"]))
W["B3"] = ("Z4", assign(["FN=MG={M}*{G}={MG} N", "FKF=MU*FN={Q}*{MG}", "FKF={QMG} N"]) +
           cond("D>0", ["W=-FKF*D=-{QMG}*{D}", "W={-QMGD} J"]))
W["Y8"] = ("Z2", assign(["P=P'", "M1V1+M2V2=(M1+M2)V'", "{A}*{B}+{C}*{D}=({A}+{C})V'", "{AB}+{CD}={A+C}V'",
                         "{AB+CD}={A+C}V'", "V'={AB+CD}/{A+C}", "V'={V} M/S", "KE BEFORE={.5AB²+.5CD²}",
                         "KE AFTER={.5(A+C)V²}", "KE LOST={R} J"]))
W["Y9"] = ("Z2", assign(["P=P'", "M1V1+M2V2=M1V1'+M2V2'", "{A}*{B}+{C}*{D}={A}*{E}+{C}V2'",
                         "{AB}+{CD}={AE}+{C}V2'", "V2'=({AB+CD}-{AE})/{C}", "V2'={V} M/S"]))
W["E1"] = ("Z2", assign(["ELASTIC: P AND KE KEPT", "V1'=((M1-M2)V1+2M2V2)", "   /(M1+M2)",
                         "V1'=({A-C}*{B}+2*{C}*{D})", "   /{A+C}", "V1'={E} M/S", "V2'=((M2-M1)V2+2M1V1)",
                         "   /(M1+M2)", "V2'=({C-A}*{D}+2*{A}*{B})", "   /{A+C}", "V2'={V} M/S"]))
W["W1"] = ("Z2", assign(["P=P'", "(M1+M2)V0=M1V1'+M2V2'", "{A+C}*{U}={A}*{E}+{C}V2'",
                         "V2'=({(A+C)U}-{AE})/{C}", "V2'={V} M/S"]))
W["W2"] = ("ZI", assign(["FT=MDV", "IMPULSE=FT={F}*{T}={FT}", "DV=FT/M={FT}/{M}", "DV={FT/M}",
                         "V'=V+DV={U}+{FT/M}", "V'={U+FT/M} M/S"]))
W["W3"] = ("ZI", assign(["FT=MDV", "F=M(V'-V)/T", "F={M}*({V}-{U})/{T}", "F={M(V-U)}/{T}", "F={M(V-U)/T} N"]))
W["E2"] = ("ZI", cond("Z=2", ["AREA=1/2*F*T", "=.5*{F}*{T}"], ["AREA=F*T", "={F}*{T}"]) +
           assign(["IMPULSE={J} N*S", "DV=IMPULSE/M={J}/{M}", "DV={J/M}", "V'={U}+{J/M}", "V'={U+J/M} M/S"], True))
W["Q1"] = ("Z5", assign(["STEP 1 E=E'", "MGH=1/2MV²", "V1=SQRT(2GH)", "V1=SQRT(2*{G}*{H})", "V1={B} M/S"]) +
           cond("Z=1", ["STEP 2 P=P' (STICK)", "{A}*{B}=({A}+{C})V'", "V'={AB}/{A+C}", "V'={V} M/S",
                        "RISE AFTER=V²/(2G)={V²/(2G)}"],
                ["STEP 2 ELASTIC", "V1'=(M1-M2)V1/(M1+M2)", "V1'={(A-C)B/(A+C)}", "V2'=2M1V1/(M1+M2)",
                 "V2'={2AB/(A+C)}"]))
W["Q2"] = ("Z5", cond("O=1", ["STEP 1 E=E' (SWING)", "V=SQRT(2GH)", "V=SQRT(2*{G}*{H})={V}", "STEP 2 P=P'",
                              "MB*VB=(MB+M)V", "VB={A+C}*{V}/{A}", "VB={B} M/S"],
                      ["STEP 1 P=P'", "MB*VB=(MB+M)V", "V={A}*{B}/{A+C}", "V={V} M/S", "STEP 2 E=E' (SWING)",
                       "1/2V²=GH", "H=V²/(2G)={V}²/(2*{G})", "H={V²/(2G)} M"]))
W["Q3"] = ("Z5", assign(["STEP 1 P=P'", "M1V1+M2V2=(M1+M2)V'", "V'=({AB}+{CD})/{A+C}", "V'={V} M/S",
                         "STEP 2 FKF*D=1/2MV²", "MU*MG*D=1/2MV²", "D=V²/(2*MU*G)", "D={V}²/(2*{Q}*{G})",
                         "D={V²/(2QG)} M"]))

def work_code(label):
    ret, body = W[label]
    return ['""→Str0'] + body, ret

src = open("solver.txt").read().split("\n")
out = []
i = 0
blocks = {}
# split into blocks by label
cur = None
for ln in src:
    m = re.match(r"^Lbl (\w+)$", ln)
    if m:
        cur = m.group(1)
    blocks.setdefault(cur, []).append(ln)
order = []
for ln in src:
    m = re.match(r"^Lbl (\w+)$", ln)
    if m: order.append(m.group(1))

def patch_tail(lines, label):
    code, ret = work_code(label)
    # find the last "Goto ret" line
    for k in range(len(lines) - 1, -1, -1):
        if lines[k] == f"Goto {ret}":
            break
    else:
        raise SystemExit(f"no Goto {ret} in {label}")
    j = k
    if lines[k - 1] == "Pause":
        j = k - 1
    return lines[:j] + code + menu(ret) + lines[k + 1:]

for lab in W:
    blocks[lab] = patch_tail(blocks[lab], lab)

# Q2 needs a branch flag
q2 = blocks["Q2"]
ti = q2.index("If B=0"); assert q2[ti + 1] == "Then"; q2.insert(ti + 2, "1→O")
ei = q2.index("Else"); q2.insert(ei + 1, "0→O")

# coaster points: show work per point, then continue at CN
c9 = blocks["C9"]
k = c9.index('Disp "SPEED (M/S)=",round(V,3)')
p = c9.index("Pause", k)
pts = ['""→Str0'] + assign(["POINT "  + "{P+1}", "E=E' (MASS CANCELS)", "V²=VA²+2G(HA-H)",
                            "V²={U}²+2*{G}*({H}-{J})", "V²={R}", "V=SQRT({R})", "V={V} M/S"], True)
pts = [x.replace('"POINT "+toString(round(P+1,3))', '"POINT "+sub(Str8,P,1)') for x in pts]
c9[p:p + 1] = pts + ['"CN"→Str7', "Goto WK", "Lbl CN"]
# curved track at a point: work screen too, then on to the next point
cn = blocks["C9"]
a = cn.index("Lbl CN")
k = cn.index("MV²/Q→K", a)
e = cn.index("P+1→P", k)
curve = ["MV²/Q→K",
         "If Z=1", "MG-K→N", "If Z=2", "MG+K→N", "If Z=3", "K-MG→N",
         '"POINT "+sub(Str8,P,1)+"!V="+toString(round(V,3))+" M/S  R="+toString(Q)+" M"→Str0'] + \
        cond("Z=1", ["HILL TOP MG-N=MV²/R", "N=MG-MV²/R", "N={MG}-{M}*{V}²/{Q}", "N={MG}-{K}"]) + \
        cond("Z=2", ["VALLEY N-MG=MV²/R", "N=MG+MV²/R", "N={MG}+{M}*{V}²/{Q}", "N={MG}+{K}"]) + \
        cond("Z=3", ["LOOP TOP N+MG=MV²/R", "N=MV²/R-MG", "N={M}*{V}²/{Q}-{MG}", "N={K}-{MG}"]) + \
        assign(["TRACK FORCE N={N} N"], True) + \
        cond("N<0", ["N<0 SO IT LEAVES THE TRACK"]) + \
        ['"CP"→Str7', "Goto WK", "Lbl CP"]
cn[k:e] = curve
# skip without entering a Then block (a Goto out of Then leaks memory)
z = cn.index('Input "TYPE ",Z', a)
assert cn[z + 1:z + 3] == ["If Z>0", "Then"]
cn[z + 1:z + 3] = ["If Z=0", "Goto CP"]

# one-equation custom: record knowns and the solved value
vz = blocks["VZ"]
k = vz.index("String►Equ(Str1,Y₁")
vz.insert(k, '"EQUATION!"+Str1+"=0!KNOWN VALUES"→Str0')
k = vz.index("Input Z")
vz.insert(k + 1, 'Str0+"!"+Str5+"="+toString(Z)→Str0')
k = vz.index('Disp "ANSWER",Str4+" =",round(Z,4)')
vz[k + 1:k + 3] = ['Str0+"!SOLVE FOR "+Str4+"!"+Str4+"="+toString(round(Z,4))→Str0'] + menu("U1")

# energy balance: list each energy with numbers
r0 = blocks["R0"]
k = len(r0) - 1 - r0[::-1].index("Goto U2")
eb = ['"E BEFORE = E AFTER!BEFORE"→Str0',
      'Str0+"!MGH="+toString(round(MGH,3))→Str0',
      'If O≠5', 'Str0+"!1/2MV²="+toString(round(.5MU²,3))→Str0',
      'Str0+"!1/2KX²="+toString(round(.5KX²,3))→Str0',
      'If O≠4', 'Str0+"!W ADDED="+toString(round(W,3))→Str0',
      'Str0+"!AFTER"→Str0',
      'If O≠2', 'Str0+"!MGH="+toString(round(MGJ,3))→Str0',
      'If O≠1', 'Str0+"!1/2MV²="+toString(round(.5MV²,3))→Str0',
      'Str0+"!1/2KX²="+toString(round(.5KY²,3))→Str0',
      'If O≠3', 'Str0+"!HEAT="+toString(round(Q,3))→Str0',
      'Str0+"!SET BEFORE=AFTER,!SOLVE FOR UNKNOWN"→Str0']
r0[k - 1:k + 1] = eb + menu("U2")

# momentum balance: list each object's momentum
u3 = blocks["U3"]
k = len(u3) - 1 - u3[::-1].index("Goto U0")
mb = ['"P=P'+"'"+'!TOTAL P BEFORE"→Str0',
      'For(I,1,N',
      'Str0+"!M"+sub("123456789",I,1)+"V="+toString(L₁(I))+"*"+toString(L₂(I))+"="+toString(round(L₁(I)L₂(I),3))→Str0',
      'End',
      'Str0+"!TOTAL="+toString(round(P,3))→Str0',
      'If S=1',
      'Str0+"!STUCK V'+"'"+'=P/TOTAL M!"+"="+toString(round(P,3))+"/"+toString(sum(L₁))+"!V'+"'"+'="+toString(round(V,3))→Str0',
      'If S≠1',
      'Str0+"!V'+"'"+'=(P-OTHERS)/M!"+"=("+toString(round(P,3))+"-"+toString(round(sum(L₁*L₃)-L₁(J)V,3))+")/"+toString(L₁(J))+"!V'+"'"+'="+toString(round(V,3))→Str0']
u3[k - 1:k + 1] = mb + menu("U0")

# B1 ends "Pause / End / Goto Z4" inside an If D>0 block: patch manually
b1 = blocks["B1"]
k = len(b1) - 1 - b1[::-1].index("Goto Z4")
b1code = ['""→Str0'] + cond("Z=2", ["FN=MG+F SIN θ", "FN={MG}+{Fsin(θ)}"], ["FN=MG-F SIN θ", "FN={MG}-{Fsin(θ)}"]) + \
    assign(["FN={N} N", "FKF=MU*FN={Q}*{N}", "FKF={K} N", "FNET=F COS θ-FKF", "FNET={Fcos(θ)}-{K}", "FNET={C} N",
            "A=FNET/M={C}/{M}", "A={A} M/S²"], True) + \
    cond("D>0", ["WNET=FNET*D={C}*{D}", "WNET={CD} J", "V²=V0²+2WNET/M", "V²={U}²+2*{CD}/{M}", "V²={U²+2CD/M}"]) + \
    cond("D>0 and U²+2CD/M≥0", ["V={√(U²+2CD/M)} M/S"])
b1[k:k + 1] = b1code + menu("Z4")
W["B1"] = ("Z4", [])

# viewer + return dispatcher (shared with the unit programs)
from tilib import viewer
rets = sorted({r for r, _ in W.values()} | {"CN", "CP", "U0", "U1", "U2", "H0"})
final = []
for lab in order:
    final += blocks[lab]
# a Goto as the last line of an If-Then block: close the block first, then jump
i = 0
while i < len(final) - 1:
    if final[i].startswith("Goto ") and final[i + 1] == "End":
        j = i
        while final[j] != "Then": j -= 1
        c = final[j - 1]
        assert c.startswith("If "), c
        g = final[i]
        final[i:i + 2] = ["End", c, g]
    i += 1
final += viewer(rets, "Z0")
open("solver_work.txt", "w").write("\n".join(final) + "\n")
print("work added; returns:", rets)
