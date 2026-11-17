"""P2FORCE: Unit 2 forces notes + guided solvers for the TI-84 Plus CE."""
from tilib import *
from customeq import custom

NOTES = [
 ("HOW TO START", [
  ["EVERY PROBLEM",
   "1 DRAW THE DOT",
   "2 DRAW FORCES",
   "  MG DOWN",
   "  FN OFF SURFACE",
   "  FRICTION,ROPE",
   "3 PICK + WAY"],
  ["EVERY PROBLEM 2",
   "4 SUM F=MA",
   "  ONE WAY AT A",
   "  TIME",
   "5 NOT MOVING",
   " THAT WAY? SUM=0",
   "6 SOLVE"],
  ["CONNECTED",
   "WHOLE SYSTEM",
   " A=OUTSIDE F/",
   "   TOTAL MASS",
   "THEN ONE OBJECT",
   " FOR TENSION OR",
   " CONTACT FORCE"],
 ]),
 ("CLUE WORDS", [
  ["HIDDEN VALUES",
   "CONST SPEED",
   "  A=0 SUM F=0",
   "AT REST A=0",
   "SMOOTH/ICE",
   "  NO FRICTION",
   "ROPE  SAME T"],
  ["MORE",
   "WEIGHT 50N",
   "  M=5KG",
   "ABOUT TO SLIP",
   "  FSF=MU*FN",
   "JUST LEAVES",
   "  TRACK FN=0"],
  ["MORE 2",
   "SCALE READS FN",
   "ORBIT=GRAVITY",
   "  IS CENTER F",
   "FLAT CURVE=",
   "  FRICTION",
   "STRING=TENSION"],
 ]),
 ("NEWTON LAWS", [
  ["1ST LAW",
   "NO NET FORCE=",
   " CONSTANT V",
   " (OR AT REST)",
   "MOVING DOESNT",
   " NEED A FORCE",
   ""],
  ["2ND LAW",
   "SUM F=MA",
   "A SAME WAY AS",
   "  NET FORCE",
   "MA IS NOT A",
   "  FORCE ARROW",
   ""],
  ["3RD LAW",
   "A PUSHES B,",
   "B PUSHES A BACK",
   "SAME SIZE",
   "OPPOSITE WAY",
   "DIFFERENT OBJECT",
   "NEVER CANCEL"],
 ]),
 ("FRICTION", [
  ["FRICTION",
   "SLIDING",
   " FKF=MU*FN",
   "NOT SLIDING",
   " FSF≤MU*FN",
   " (ONLY AS BIG",
   "  AS NEEDED)"],
  ["FN IS NOT MG IF",
   "RAMP MGCOSθ",
   "PULL UP AT θ",
   " MG-FSINθ",
   "PUSH DOWN AT θ",
   " MG+FSINθ",
   "ELEVATOR M(G+A)"],
 ]),
 ("RAMPS", [
  ["RAMPS",
   "TILT THE AXES",
   "DOWN RAMP",
   "  MG SIN θ",
   "INTO RAMP",
   "  MG COS θ",
   "FN=MG COS θ"],
  ["RAMP RESULTS",
   "NO FRICTION",
   " A=G SIN θ",
   "WITH FRICTION",
   " A=G(SINθ-",
   "    MU COSθ)",
   "SLIPS IF TANθ>MU"],
 ]),
 ("PULLEYS", [
  ["ATWOOD",
   "A=(M2-M1)G/",
   "   (M1+M2)",
   "T=M1(G+A)",
   "TABLE+HANGING",
   "A=(M2G-MU M1G)/",
   "   (M1+M2)"],
  ["TENSION",
   "ACCELERATING?",
   "T NOT = MG",
   "HANGING MASS",
   " GOING DOWN",
   " T=M(G-A)",
   "REST  T=MG"],
 ]),
 ("SPRINGS", [
  ["SPRINGS",
   "FS=KX",
   "X=STRETCH FROM",
   "  NATURAL LENGTH",
   "K=N/M STIFFNESS",
   "HANGING AT REST",
   " KX=MG"],
 ]),
 ("GRAVITY", [
  ["GRAVITY",
   "F=GM1M2/R²",
   "G=6.67E-11",
   "R=CENTER TO",
   "  CENTER",
   "2X DIST=1/4 F",
   "3X DIST=1/9 F"],
  ["LITTLE G",
   "G=GM/R²",
   "2X MASS=2X G",
   "2X RADIUS=1/4 G",
   "ORBIT",
   " V=SQRT(GM/R)",
   ""],
 ]),
 ("CIRCLES", [
  ["CIRCLES",
   "A=V²/R TO CENTER",
   "F=MV²/R",
   "V=2(PI)R/T",
   "NO OUTWARD",
   "  FORCE",
   "STRING CUT=",],
  ["CIRCLES 2",
   " GOES TANGENT",
   "FLAT CURVE",
   " V=SQRT(MU G R)",
   "LOOP TOP MIN",
   " V=SQRT(GR)",
   ""],
  ["HILL AND DIP",
   "TOP OF HILL",
   " FN=MG-MV²/R",
   "BOTTOM OF DIP",
   " FN=MG+MV²/R",
   "TOP OF LOOP",
   " FN=MV²/R-MG"],
 ]),
]

L = []
add = L.extend
add(["ClrHome", 'Disp "LOADING..."'])
code, ranges = slides(NOTES)
add(code)
add(["10→G", "Degree", "If Z<77200 or Z>77299", "Goto M", "Z-77200→E", "0→Z"])
ENTRY = {1: "FW", 2: "BX", 3: "RP", 4: "PL", 5: "CG", 6: "NM", 7: "B1", 8: "R1", 9: "A1", 10: "A2", 11: "E1", 12: "C1", 13: "C3", 14: "G1", 15: "S0", 16: "N1", 17: "C2", 18: "G3", 19: "F5", 20: "F1", 21: "F2", 22: "S0"}
for k, v in ENTRY.items():
    add([f"If E={k}", f"Goto {v}"])
add(["Lbl M",
     'Menu("P2FORCE UNIT 2","FIND WHAT?",FW,"BOXES+FRICTION",BX,"RAMPS",RP,"PULLEYS+ROPES",PL,"CIRCLES+GRAVITY",CG,"NOTES",NM,"MORE",MO',
     "Lbl MO",
     'Menu("MORE","SPRINGS",S0,"HIDDEN VALUES",H0,"CENTER OF MASS",CM,"CUSTOM EQUATION",X0,"SET G (10/9.8)",ZZ,"QUIT",Q,"BACK",M',
     "Lbl FW",
     'Menu("FIND WHAT?","ACCELERATION",F1,"A FORCE",F2,"NET FORCE",F3,"MASS",F4,"SPEED",F5,"MU, K OR G",F6,"BACK",M',
     "Lbl F1",
     'Menu("ACCELERATION","BOX PUSH/PULL",B1,"RAMP",RP,"ATWOOD 2 HANGING",A1,"TABLE+HANGING",A2,"BLOCKS PUSHED",A3,"CIRCLE V²/R",C1,"BACK",FW',
     "Lbl F2",
     'Menu("WHICH FORCE?","FRICTION",B2,"NORMAL/SCALE",F7,"TENSION",F8,"SPRING KX",S1,"GRAVITY GMM/R²",G1,"CENTER FORCE",C1,"BACK",FW',
     "Lbl F7",
     'Menu("NORMAL FORCE","FLAT/ANGLED PULL",B1,"RAMP",R1,"ELEVATOR/SCALE",E1,"HILL/DIP/LOOP",C3,"BACK",F2',
     "Lbl F8",
     'Menu("TENSION","ATWOOD 2 HANGING",A1,"TABLE+HANGING",A2,"LIFTED/LOWERED",E1,"STRING CIRCLE",C1,"CONTACT FORCE",A3,"BACK",F2',
     "Lbl F3",
     'Menu("NET FORCE","ADD FORCES",N1,"FROM M AND A",N2,"BACK",FW',
     "Lbl F4",
     'Menu("MASS","FROM WEIGHT",H1,"FROM F AND A",N3,"BACK",FW',
     "Lbl F5",
     'Menu("SPEED","MAX CURVE SPEED",C2,"LOOP TOP MIN",C4,"ORBIT SPEED",G3,"FROM PERIOD",C5,"BACK",FW',
     "Lbl F6",
     'Menu("FIND","MU",M1,"SPRING K",S2,"G ON A PLANET",G2,"BACK",FW'])

S = []
# ---- boxes ----
S += ["Lbl BX",
      'Menu("BOXES+FRICTION","PUSH/PULL A BOX",B1,"FRICTION FORCE",B2,"SLIDES TO STOP",B3,"ADD FORCES",N1,"ELEVATOR/SCALE",E1,"BACK",M']
S += ["Lbl B1", "ClrHome", 'Disp "PUSH/PULL A BOX","ANGLE 0 = FLAT","MU 0 = NO FRICTION"',
      'Input "MASS (KG) ",M', 'Input "FORCE (N) ",F', 'Input "ANGLE (DEG) ",θ', "1→Z", "If θ≠0", "Then",
      'Disp "1=PULL UP AT ANGLE","2=PUSH DOWN AT ANGLE"', 'Input "1 OR 2? ",Z', "End",
      'Input "MU STATIC ",P', 'Input "MU KINETIC ",Q',
      "If Z=2", "MG+Fsin(θ)→N", "If Z≠2", "MG-Fsin(θ)→N", "Fcos(θ)→X", "PN→S", "QN→K", "0→A",
      "If X>S or P=0", "(X-K)/M→A", "If X≤S and P≠0", "X→K"]
S += assign(["GIVEN", "M={M} KG", "F={F} N AT {θ} DEG", "MU S={P} MU K={Q}",
             "FN: UP-DOWN=0"])
S += cond("Z=2", ["FN=MG+F SIN θ", "FN={MG}+{Fsin(θ)}"], ["FN=MG-F SIN θ", "FN={MG}-{Fsin(θ)}"])
S += assign(["FN={N} N", "PUSH ALONG=F COS θ={X} N"], True)
S += cond("P≠0", ["MAX STATIC=MU*FN", "={P}*{N}={S} N"])
S += cond("X≤S and P≠0", ["PUSH < MAX STATIC", "SO IT DOES NOT MOVE", "FRICTION=PUSH={X} N", "A=0"],
          ["IT SLIDES: FKF=MU*FN", "FKF={Q}*{N}={K} N", "SUM F=MA", "FCOSθ-FKF=MA", "A=({X}-{K})/{M}", "A={A} M/S²"])
S += show("BX")
S += solver("B2", "FRICTION FORCE", ["PUSH 0 IF NOT GIVEN", "FLAT FLOOR, FN=MG"],
            [("M", "MASS", "KG"), ("P", "MU STATIC", ""), ("Q", "MU KINETIC", ""), ("F", "PUSH", "N")],
            ["MG→N", "PN→S", "QN→K"],
            ["FN=MG={M}*{G}={N} N", "MAX STATIC FSF=MU*FN", "={P}*{N}={S} N", "SLIDING FKF=MU*FN", "={Q}*{N}={K} N"], "BX",
            cond("F>0 and F≤S", ["PUSH {F} N < {S} N", "STAYS PUT: FRICTION={F} N"]) +
            cond("F>S", ["PUSH {F} N > {S} N", "SLIDES: FRICTION={K} N", "A=({F}-{K})/{M}={(F-K)/M} M/S²"]))
S += solver("B3", "SLIDES TO A STOP", ["ONLY FRICTION SLOWS IT"],
            [("Q", "MU KINETIC", ""), ("U", "START V", "M/S")], ["QG→A", "U²/(2A)→D", "U/A→T"],
            ["SUM F=MA", "MU*M*G=MA", "A=MU*G={Q}*{G}", "A={A} M/S² (SLOWING)", "V²=V0²-2AD", "D=V0²/(2A)",
             "D={U}²/(2*{A})={D} M", "T=V0/A={T} S"], "BX")
S += ["Lbl N1", "ClrHome", 'Disp "ADD FORCES","ANGLE FROM +X: RIGHT=0","UP=90 LEFT=180 DOWN=270"',
      'Input "HOW MANY? ",N', "0→X", "0→Y", '"GIVEN"→Str0',
      "For(J,1,N", 'Disp "FORCE "+toString(J)', 'Input "SIZE (N) ",F', 'Input "ANGLE (DEG) ",θ',
      "X+Fcos(θ)→X", "Y+Fsin(θ)→Y",
      'Str0+"!F"+toString(J)+"="+toString(F)+" N AT "+toString(θ)+"!  X="+toString(round(Fcos(θ),3))+" Y="+toString(round(Fsin(θ),3))→Str0',
      "End", 'Input "MASS (0=SKIP) ",M', "R►Pr(X,Y)→R", "R►Pθ(X,Y)→θ"]
S += assign(["ADD X PARTS={X} N", "ADD Y PARTS={Y} N", "NET=SQRT(X²+Y²)", "NET F={R} N", "AT {θ} DEG"], True)
S += cond("M>0", ["A=FNET/M={R}/{M}", "A={R/M} M/S²"])
S += show("BX")
S += solver("N2", "NET FORCE FROM M AND A", ["SUM F=MA"], [("M", "MASS", "KG"), ("A", "ACCEL", "M/S²")], ["MA→F"],
            ["SUM F=MA", "F={M}*{A}", "F={F} N"], "FW")
S += solver("N3", "MASS FROM F AND A", ["F MUST BE THE NET FORCE"], [("F", "NET F", "N"), ("A", "ACCEL", "M/S²")], ["F/A→M"],
            ["SUM F=MA", "M=F/A={F}/{A}", "M={M} KG"], "FW")
S += ["Lbl E1", "ClrHome", 'Disp "ELEVATOR, SCALE OR ROPE","ACCEL UP = +","ACCEL DOWN = -","CONST SPEED = 0"',
      'Input "MASS (KG) ",M', 'Input "ACCEL (M/S²) ",A', "M(G+A)→N"]
S += assign(["GIVEN", "M={M} KG", "A={A} M/S² (UP +)", "UP IS +", "FN-MG=MA", "FN=M(G+A)", "FN={M}*({G}+{A})",
             "FN={N} N", "(SCALE READING OR", "ROPE TENSION)", "WEIGHT MG={MG} N"])
S += cond("A>0", ["READS MORE THAN WEIGHT"]) + cond("A<0", ["READS LESS THAN WEIGHT"])
S += show("BX")

# ---- ramps ----
S += ["Lbl RP",
      'Menu("RAMPS","SLIDE DOWN?",R1,"COASTING UP",R2,"PUSH UP CONST V",R3,"FORCE TO HOLD",R4,"PUSH UP FIND A",R5,"BACK",M']
RAMPIN = [("M", "MASS", "KG"), ("θ", "ANGLE", "DEG")]
S += solver("R1", "RAMP: DOES IT SLIDE?", ["MU 0 = NO FRICTION"],
            RAMPIN + [("P", "MU STATIC", ""), ("Q", "MU KINETIC", "")],
            ["MGcos(θ)→N", "MGsin(θ)→X", "PN→S", "0→A", "If X>S or P=0", "G(sin(θ)-Qcos(θ))→A"],
            ["FN=MG COS θ", "FN={MG}*{cos(θ)}={N} N", "DOWN RAMP=MG SIN θ", "={MG}*{sin(θ)}={X} N"], "RP",
            cond("P≠0", ["MAX STATIC=MU*FN={S} N"]) +
            cond("X≤S and P≠0", ["{X} < {S} SO IT STAYS", "STATIC FRICTION={X} N UP", "A=0"],
                 ["IT SLIDES DOWN", "A=G(SIN θ-MU COS θ)", "A={G}*({sin(θ)}-{Q}*{cos(θ)})", "A={A} M/S²"]))
S += solver("R2", "COASTING UP A RAMP", ["GRAVITY+FRICTION SLOW IT"],
            RAMPIN[1:] + [("Q", "MU KINETIC", ""), ("U", "SPEED", "M/S")],
            ["G(sin(θ)+Qcos(θ))→A", "U²/(2A)→D"],
            ["BOTH POINT DOWN RAMP", "A=G(SIN θ+MU COS θ)", "A={G}*({sin(θ)}+{Q}*{cos(θ)})", "A={A} M/S² (SLOWING)",
             "DISTANCE UP=V²/(2A)", "D={U}²/(2*{A})", "D={D} M"], "RP")
S += solver("R3", "PUSH UP AT CONSTANT V", ["PUSH ALONG THE RAMP", "A=0 SO FORCES BALANCE"],
            RAMPIN + [("Q", "MU KINETIC", "")], ["MGsin(θ)+QMGcos(θ)→F"],
            ["FRICTION POINTS DOWN", "F=MG SIN θ+MU MG COS θ", "F={MGsin(θ)}+{QMGcos(θ)}", "F={F} N"], "RP")
S += solver("R4", "FORCE TO HOLD STILL", ["PUSH ALONG THE RAMP"],
            RAMPIN + [("P", "MU STATIC", "")], ["MGsin(θ)-PMGcos(θ)→F", "MGsin(θ)+PMGcos(θ)→W"],
            ["DOWN RAMP={MGsin(θ)} N", "MAX STATIC={PMGcos(θ)} N", "SMALLEST PUSH=", "MG SIN θ-MU MG COS θ", "={F} N",
             "(0 OR LESS=HOLDS ITSELF)", "LARGEST BEFORE IT SLIDES", "UP={W} N"], "RP")
S += solver("R5", "PUSH UP, FIND A", ["PUSH ALONG THE RAMP"],
            RAMPIN + [("Q", "MU KINETIC", ""), ("F", "PUSH", "N")], ["(F-MGsin(θ)-QMGcos(θ))/M→A"],
            ["SUM F=MA (UP +)", "F-MG SIN θ-MU MG COS θ", "  =MA", "A=({F}-{MGsin(θ)}-{QMGcos(θ)})/{M}", "A={A} M/S²"], "RP")

# ---- pulleys ----
S += ["Lbl PL",
      'Menu("PULLEYS+ROPES","ATWOOD 2 HANGING",A1,"TABLE+HANGING",A2,"BLOCKS PUSHED",A3,"LIFTED/LOWERED",E1,"BACK",M']
S += solver("A1", "ATWOOD (2 HANGING)", ["FRICTIONLESS PULLEY"],
            [("A", "M1", "KG"), ("B", "M2", "KG")], ["abs(B-A)G/(A+B)→C", "2ABG/(A+B)→T"],
            ["WHOLE SYSTEM", "A=(HEAVY-LIGHT)G/TOTAL", "A={abs(B-A)}*{G}/{A+B}", "A={C} M/S²",
             "LIGHT ONE GOES UP", "T-MLIGHT*G=MLIGHT*A", "T=M(G+A)", "T={T} N"], "PL")
S += ["Lbl A2", "ClrHome", 'Disp "TABLE + HANGING MASS","M1 ON TABLE, M2 HANGS","MU 0 = NO FRICTION"',
      'Input "M1 TABLE (KG) ",A', 'Input "M2 HANG (KG) ",B', 'Input "MU KINETIC ",Q',
      "BG→W", "QAG→K", "0→C", "If W>K", "(W-K)/(A+B)→C", "B(G-C)→T"]
S += assign(["GIVEN", "M1={A} KG ON TABLE", "M2={B} KG HANGING", "MU={Q}", "PULL=M2G={W} N", "FRICTION=MU M1 G={K} N"])
S += cond("W>K", ["SYSTEM: A=(M2G-MU M1G)", "  /(M1+M2)", "A=({W}-{K})/{A+B}", "A={C} M/S²", "HANGING: M2G-T=M2A",
                  "T=M2(G-A)={B}*({G}-{C})", "T={T} N"],
          ["PULL <= FRICTION", "NOTHING MOVES, A=0", "T=M2G={T} N"])
S += show("PL")
S += solver("A3", "BLOCKS PUSHED TOGETHER", ["PUSH ON BLOCK 1,", "IT PUSHES BLOCK 2", "MU 0 = NO FRICTION"],
            [("F", "PUSH", "N"), ("A", "M1 PUSHED", "KG"), ("B", "M2 FRONT", "KG"), ("Q", "MU KINETIC", "")],
            ["(F-Q(A+B)G)/(A+B)→C", "BC+QBG→P"],
            ["WHOLE SYSTEM", "A=(F-MU(M1+M2)G)/(M1+M2)", "A=({F}-{Q(A+B)G})/{A+B}", "A={C} M/S²",
             "FRONT BLOCK ONLY", "P-MU M2 G=M2 A", "P={B}*{C}+{QBG}", "CONTACT FORCE={P} N"], "PL")

# ---- circles + gravity ----
S += ["Lbl CG",
      'Menu("CIRCLES+GRAVITY","SPEED IN CIRCLE",C1,"FLAT CURVE",C2,"HILL/DIP/LOOP",C3,"GRAVITY FORCE",G1,"G ON A PLANET",G2,"ORBIT",G3,"MORE",CH',
      "Lbl CH",
      'Menu("MORE CIRCLES","LOOP TOP MIN V",C4,"FROM PERIOD",C5,"RATIOS",G4,"BACK",CG']
S += solver("C1", "MOVING IN A CIRCLE", ["MASS 0 IF NOT GIVEN"],
            [("V", "SPEED", "M/S"), ("R", "RADIUS", "M"), ("M", "MASS", "KG")],
            ["V²/R→A", "MA→F", "2πR/V→T"],
            ["A=V²/R TO THE CENTER", "A={V}²/{R}", "A={A} M/S²", "NET F=MV²/R", "F={M}*{A}", "F={F} N TO CENTER",
             "(TENSION, FRICTION OR", "GRAVITY PROVIDES IT)", "ONE LAP T=2(PI)R/V={T} S"], "CG")
S += solver("C2", "MAX SPEED ON FLAT CURVE", ["FRICTION HOLDS IT ON"],
            [("P", "MU STATIC", ""), ("R", "RADIUS", "M")], ["√(PGR)→V"],
            ["MU MG=MV²/R (M CANCELS)", "V=SQRT(MU G R)", "V=SQRT({P}*{G}*{R})", "V={V} M/S"], "CG")
S += ["Lbl C3", "ClrHome", 'Disp "HILL, DIP OR LOOP","1=TOP OF HILL","2=BOTTOM OF DIP/LOOP","3=TOP OF LOOP (INSIDE)"',
      'Input "1, 2 OR 3? ",Z', 'Input "MASS (KG) ",M', 'Input "SPEED (M/S) ",V', 'Input "RADIUS (M) ",R',
      "MV²/R→K", "If Z=1", "MG-K→N", "If Z=2", "MG+K→N", "If Z=3", "K-MG→N"]
S += assign(["GIVEN", "M={M} KG V={V} M/S", "R={R} M", "MV²/R={K} N", "MG={MG} N"])
S += cond("Z=1", ["TOP OF HILL", "MG-FN=MV²/R", "FN=MG-MV²/R={MG}-{K}"])
S += cond("Z=2", ["BOTTOM", "FN-MG=MV²/R", "FN=MG+MV²/R={MG}+{K}"])
S += cond("Z=3", ["TOP OF LOOP", "FN+MG=MV²/R", "FN=MV²/R-MG={K}-{MG}"])
S += assign(["FN={N} N"], True) + cond("N<0", ["FN<0: LEAVES THE TRACK"]) + show("CG")
S += solver("C4", "LOOP TOP MINIMUM SPEED", ["AT MINIMUM FN=0"], [("R", "RADIUS", "M")], ["√(GR)→V"],
            ["ONLY GRAVITY AT TOP", "MG=MV²/R", "V=SQRT(GR)", "V=SQRT({G}*{R})", "V={V} M/S"], "CH")
S += solver("C5", "SPEED FROM PERIOD", ["T = TIME FOR ONE LAP"], [("R", "RADIUS", "M"), ("T", "PERIOD", "S")],
            ["2πR/T→V", "V²/R→A"],
            ["V=2(PI)R/T", "V=2*3.1416*{R}/{T}", "V={V} M/S", "A=V²/R={A} M/S²"], "CH")
S += solver("G1", "GRAVITY BETWEEN MASSES", ["E NUMBERS: 2ND , KEY", "EX 6E24 FOR 6X10^24", "R CENTER TO CENTER"],
            [("A", "M1", "KG"), ("B", "M2", "KG"), ("R", "DISTANCE", "M")], ["6.67ᴇ⁻11AB/R²→F"],
            ["F=GM1M2/R²", "G=6.67E-11", "F=6.67E-11*{A}*{B}", "  /{R}²", "F={F} N"], "CG")
S += ["Lbl G2", "ClrHome", 'Disp "G ON A PLANET","1=COMPARE TO EARTH","2=REAL MASS + RADIUS"', 'Input "1 OR 2? ",Z',
      "If Z=2", "Goto G5", 'Input "X EARTH MASS ",A', 'Input "X EARTH RADIUS ",B', "10A/B²→C"]
S += assign(["GIVEN", "MASS={A} X EARTH", "RADIUS={B} X EARTH", "G=GM/R²", "G=10*{A}/{B}²", "G={C} M/S²"]) + show("CG")
S += ["Lbl G5", 'Input "MASS (KG) ",A', 'Input "RADIUS (M) ",R', "6.67ᴇ⁻11A/R²→C"]
S += assign(["GIVEN", "M={A} KG", "R={R} M", "G=GM/R²", "G=6.67E-11*{A}/{R}²", "G={C} M/S²"]) + show("CG")
S += solver("G3", "ORBIT", ["PLANET MASS, ORBIT RADIUS", "(FROM CENTER)", "E NUMBERS: 2ND , KEY"],
            [("A", "PLANET M", "KG"), ("R", "ORBIT R", "M")], ["√(6.67ᴇ⁻11A/R)→V", "2πR/V→T"],
            ["GRAVITY=CENTER FORCE", "GMM/R²=MV²/R", "V=SQRT(GM/R)", "V=SQRT(6.67E-11*{A}/{R})", "V={V} M/S",
             "PERIOD=2(PI)R/V", "T={T} S", "T={T/3600} HOURS"], "CG")
S += solver("G4", "GRAVITY RATIOS", ["TYPE THE MULTIPLIERS", "EX DOUBLED=2 HALVED=.5"],
            [("A", "M1 TIMES", ""), ("B", "M2 TIMES", ""), ("C", "DIST TIMES", "")], ["AB/C²→F"],
            ["F IS PROPORTIONAL TO", "M1*M2/R²", "F TIMES={A}*{B}/{C}²", "NEW F={F} X OLD F"], "CH")

# ---- springs, mu, center of mass, hidden ----
S += ["Lbl S0", 'Menu("SPRINGS","FORCE KX",S1,"FIND K",S2,"FIND STRETCH",S3,"BACK",M']
S += solver("S1", "SPRING FORCE", ["X FROM NATURAL LENGTH"], [("K", "K", "N/M"), ("X", "STRETCH", "M")], ["KX→F"],
            ["FS=KX", "FS={K}*{X}", "FS={F} N"], "S0")
S += solver("S2", "FIND SPRING K", ["HANGING MASS AT REST:", "KX=MG"], [("M", "MASS", "KG"), ("X", "STRETCH", "M")], ["MG/X→K"],
            ["AT REST KX=MG", "K=MG/X", "K={M}*{G}/{X}", "K={K} N/M"], "S0")
S += solver("S3", "FIND STRETCH", ["HANGING MASS AT REST"], [("M", "MASS", "KG"), ("K", "K", "N/M")], ["MG/K→X"],
            ["KX=MG", "X=MG/K", "X={M}*{G}/{K}", "X={X} M"], "S0")
S += ["Lbl M1", "ClrHome", 'Disp "FIND MU","1=FRICTION AND FN","2=RAMP ANGLE WHERE IT","  SLIPS OR SLIDES AT","  CONSTANT SPEED"',
      'Input "1 OR 2? ",Z', "If Z=2", "Goto M2", 'Input "FRICTION (N) ",F', 'Input "FN (N) ",N', "F/N→Q"]
S += assign(["GIVEN", "FRICTION={F} N", "FN={N} N", "F=MU*FN", "MU=F/FN={F}/{N}", "MU={Q}"]) + show("FW")
S += ["Lbl M2", 'Input "ANGLE (DEG) ",θ', "tan(θ)→Q"]
S += assign(["GIVEN", "ANGLE={θ} DEG", "MG SIN θ=MU MG COS θ", "MU=TAN θ", "MU={Q}"]) + show("FW")
S += ["Lbl CM", "ClrHome", 'Disp "CENTER OF MASS","TYPE EACH MASS AND", "ITS POSITION"', 'Input "HOW MANY? ",N',
      "0→A", "0→B", '"GIVEN"→Str0', "For(J,1,N", 'Disp "OBJECT "+toString(J)', 'Input "MASS (KG) ",M', 'Input "X (M) ",X',
      "A+M→A", "B+MX→B", 'Str0+"!M"+toString(J)+"="+toString(M)+" AT X="+toString(X)→Str0', "End", "B/A→C"]
S += assign(["XCM=SUM(MX)/SUM(M)", "XCM={B}/{A}", "XCM={C} M"], True) + show("MO")
S += ["Lbl H0", 'Menu("HIDDEN VALUES","CLUE WORDS",O2,"WEIGHT TO MASS",H1,"GRAMS TO KG",H2,"BACK",M']
S += solver("H1", "WEIGHT TO MASS", ["WEIGHT IS IN NEWTONS"], [("W", "WEIGHT", "N")], ["W/G→M"],
            ["W=MG", "M=W/G={W}/{G}", "M={M} KG"], "H0")
S += solver("H2", "GRAMS TO KG", ["DIVIDE BY 1000"], [("W", "MASS", "G")], ["W/1000→M"],
            ["M={W}/1000", "M={M} KG"], "H0")

labs = {}
def nl(t):
    labs.setdefault(t, "O" + "123456789ABCDEF"[len(labs)])
    return labs[t]
titles = [t for t, _ in NOTES]
for t in titles: nl(t)
S += ["Lbl NM", 'Menu("NOTES",' + ",".join(f'"{t}",{nl(t)}' for t in titles[:5]) + ',"MORE",NN,"BACK",M',
      "Lbl NN", 'Menu("NOTES 2",' + ",".join(f'"{t}",{nl(t)}' for t in titles[5:]) + ',"BACK",NM']
for t, (a, b) in ranges.items():
    S += [f"Lbl {nl(t)}", f"{a}→A", f"{b}→B", "Goto S"]
S += slide_viewer("NM")
S += custom([
  ("FNET=MA", "F-MA", "FMA", ["F=NET FORCE (N)", "M=MASS (KG)", "A=ACCEL (M/S²)"]),
  ("FKF=MU*FN", "F-QN", "FQN", ["F=FRICTION (N)", "Q=MU", "N=NORMAL F (N)"]),
  ("FS=KX", "F-KX", "FKX", ["F=SPRING F (N)", "K=N/M", "X=STRETCH (M)"]),
  ("F=MV²/R", "F-MV²/R", "FMVR", ["F=CENTER F (N)", "M=MASS", "V=SPEED", "R=RADIUS"]),
  ("FG=GM1M2/R²", "F-6.67ᴇ⁻11AB/R²", "FABR", ["F=FORCE (N)", "A=MASS 1", "B=MASS 2", "R=DISTANCE (M)"]),
  ("V=2(PI)R/T", "V-2πR/T", "VRT", ["V=SPEED", "R=RADIUS", "T=PERIOD (S)"]),
  ("FN=MG COS θ", "N-MGcos(θ)", "NMθ", ["N=NORMAL F", "M=MASS", "θ=ANGLE (DEG)"]),
], "MO", "X")
S += ["Lbl ZZ", "ClrHome", 'Disp "TYPE 10 OR 9.8"', 'Input "G=",G', "If G≤0", "10→G", "Goto M",
      "Lbl Q", "ClrHome", 'Disp "GOOD LUCK"']
add(S)
rets = [l[1:l.index('"', 1)] for l in L if l.endswith('→Str7') and l.startswith('"')]
q = L.index("Lbl ZZ")
L[q:q] = viewer(rets, "M")
if __name__ == "__main__":
    build("P2FORCE", L)
