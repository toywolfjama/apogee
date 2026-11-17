"""P1MOTION: Unit 1 kinematics notes + guided solvers for the TI-84 Plus CE."""
from tilib import *

NOTES = [
 ("HOW TO PICK", [
  ["5 THINGS",
   "V0 START SPEED",
   "V  END SPEED",
   "A  ACCELERATION",
   "T  TIME",
   "DX DISTANCE",
   "KNOW 3, FIND 1"],
  ["WHICH EQUATION",
   "NO DX?",
   " V=V0+AT",
   "NO A?",
   " DX=1/2(V+V0)T",
   "NO V?",
   " DX=V0T+1/2AT²"],
  ["WHICH EQUATION 2",
   "NO T?",
   " V²=V0²+2ADX",
   "",
   "PICK THE ONE",
   "MISSING THE ONE",
   "YOU DONT NEED"],
  ["EVERY PROBLEM",
   "1 PICK + SIDE",
   "2 LIST V0 V A T",
   "  AND DX",
   "3 ADD HIDDEN 0S",
   "4 PICK EQUATION",
   "5 SOLVE+UNITS"],
 ]),
 ("CLUE WORDS", [
  ["HIDDEN VALUES",
   "AT REST V=0",
   "FROM REST V0=0",
   "DROPPED V0=0",
   "STOPS V=0",
   "TOP OF THROW",
   "  V=0"],
  ["MORE",
   "FREE FALL",
   "  A=-10 (UP +)",
   "CONST SPEED A=0",
   "HORIZONTAL",
   " LAUNCH VY0=0",
   "LEVEL GROUND"],
  ["MORE 2",
   " SAME H START",
   " AND END",
   "KM/H /3.6=M/S",
   "BACK/LEFT/DOWN",
   "  NEGATIVE",
   "BRAKES A<0"],
 ]),
 ("FREE FALL", [
  ["FREE FALL",
   "A=-G ALWAYS",
   "EVEN AT TOP",
   "TOP V=0 A=-10",
   "MASS DOESNT",
   "  MATTER",
   "G=10 M/S²"],
  ["DROPPED",
   "T=SQRT(2H/G)",
   "V=SQRT(2GH)",
   "EX H=45",
   "T=SQRT(9)=3S",
   "V=30 M/S",
   ""],
  ["THROWN UP",
   "T TOP=V0/G",
   "H MAX=V0²/(2G)",
   "BACK DOWN SAME",
   "  SPEED",
   "TOTAL T=2V0/G",
   "(SAME HEIGHT)"],
 ]),
 ("GRAPHS", [
  ["X-T GRAPH",
   "SLOPE=VELOCITY",
   "FLAT=AT REST",
   "STRAIGHT=CONST V",
   "CURVE UP=",
   "  SPEEDING UP +",
   ""],
  ["V-T GRAPH",
   "SLOPE=ACCEL",
   "AREA=DX",
   "FLAT=CONST V",
   "CROSS 0=TURNS",
   "  AROUND",
   "BELOW AXIS=-DX"],
  ["A-T GRAPH",
   "AREA=CHANGE IN V",
   "",
   "SPEEDING UP?",
   "V,A SAME SIGN",
   "SLOWING DOWN?",
   "V,A OPPOSITE"],
 ]),
 ("PROJECTILES", [
  ["PROJECTILES",
   "X AND Y SEPARATE",
   "ONLY T IS SHARED",
   "X  VX CONSTANT",
   "  DX=VX*T",
   "Y  FREE FALL",
   "  A=-10"],
  ["AT AN ANGLE",
   "VX=V0 COS θ",
   "VY=V0 SIN θ",
   "T UP=VY/G",
   "T TOTAL=2VY/G",
   "RANGE=VX*T",
   "H=VY²/(2G)"],
  ["OFF A CLIFF",
   "VY0=0",
   "T=SQRT(2H/G)",
   "RANGE=V0*T",
   "TOP OF PATH",
   " VY=0, VX SAME",
   "45 DEG=MAX RANGE"],
 ]),
 ("VECTORS", [
  ["COMPONENTS",
   "AX=A COS θ",
   "AY=A SIN θ",
   "θ FROM X AXIS",
   "BACK TO ONE",
   "A=SQRT(AX²+AY²)",
   "θ=TAN-1(AY/AX)"],
  ["ADDING",
   "ADD ALL X",
   "ADD ALL Y",
   "THEN REBUILD",
   "3-4-5 TRIANGLE",
   "SIN 30=.5",
   "COS 60=.5"],
 ]),
 ("RELATIVE", [
  ["RELATIVE MOTION",
   "V GROUND=",
   " V REL TRAIN",
   " +V TRAIN",
   "TOWARD EACH",
   " OTHER  ADD",
   "SAME WAY  SUB"],
  ["RIVER",
   "AIM ACROSS",
   "T=WIDTH/VBOAT",
   "DRIFT=VRIVER*T",
   "V=SQRT(VB²+VR²)",
   "LAND STRAIGHT",
   "V=SQRT(VB²-VR²)"],
 ]),
]

L = []
add = L.extend
add(["ClrHome", 'Disp "LOADING..."'])
code, ranges = slides(NOTES)
add(code)
add(["10→G", "Degree",
     # entry point when started from the Units 1-3 launcher
     "If Z<77100 or Z>77199", "Goto M", "Z-77100→E", "0→Z"])
ENTRY = {1: "FW", 2: "PJ", 3: "VC", 4: "GR", 5: "NM", 6: "K1", 7: "K2", 8: "K4", 9: "K5", 10: "K9", 11: "KE", 12: "KF", 13: "P1", 14: "P2", 15: "P3", 16: "V4", 17: "F1", 18: "F2", 19: "F3", 20: "F4", 21: "F5"}
for k, v in ENTRY.items():
    add([f"If E={k}", f"Goto {v}"])
add(["Lbl M",
     'Menu("P1MOTION UNIT 1","FIND WHAT?",FW,"PROJECTILES",PJ,"VECTORS+RIVER",VC,"GRAPHS",GR,"HIDDEN VALUES",H0,"NOTES",NM,"MORE",MO',
     "Lbl MO",
     'Menu("MORE","CUSTOM EQUATION",C0,"SET G (10/9.8)",ZZ,"QUIT",Q,"BACK",M',
     "Lbl FW",
     'Menu("FIND WHAT?","FINAL SPEED V",F1,"DISTANCE DX",F2,"ACCELERATION A",F3,"TIME T",F4,"START SPEED V0",F5,"PROJECTILE",PJ,"BACK",M',
     "Lbl F1",
     'Menu("FIND V. YOU HAVE","V0, A, T",K1,"V0, A, DX",K2,"V0, DX, T",K3,"DROPPED FROM H",K4,"THROWN UP,LANDS",KF,"BACK",FW',
     "Lbl F2",
     'Menu("FIND DX. HAVE","V0, A, T",K5,"V0, V, T",K6,"V0, V, A",K7,"MAX HEIGHT UP",K8,"GRAPH AREA",GR,"BACK",FW',
     "Lbl F3",
     'Menu("FIND A. YOU HAVE","V0, V, T",K9,"V0, V, DX",KA,"V0, DX, T",KB,"GRAPH SLOPE",R1,"BACK",FW',
     "Lbl F4",
     'Menu("FIND T. YOU HAVE","V0, V, A",KC,"V0, V, DX",KD,"V0, A, DX",KE,"DROPPED FROM H",K4,"THROWN UP,LANDS",KF,"TIME TO TOP",K8,"BACK",FW',
     "Lbl F5",
     'Menu("FIND V0. HAVE","V, A, T",KG,"V, A, DX",KH,"DX, A, T",KI,"HOW HIGH IT WENT",KJ,"BACK",FW'])

S = []
S += solver("K1", "FIND V", ["V=V0+AT", "BACKWARD/DOWN = NEGATIVE"],
            [("U", "V0", "M/S"), ("A", "A", "M/S²"), ("T", "T", "S")], ["U+AT→V"],
            ["V=V0+AT", "V={U}+{A}*{T}", "V={U}+{AT}", "V={V} M/S"], "F1")
S += solver("K2", "FIND V (NO TIME)", ["V²=V0²+2ADX"],
            [("U", "V0", "M/S"), ("A", "A", "M/S²"), ("D", "DX", "M")], ["U²+2AD→S"],
            ["V²=V0²+2ADX", "V²={U}²+2*{A}*{D}", "V²={U²}+{2AD}", "V²={S}"], "F1",
            cond("S≥0", ["V=SQRT({S})", "V=+/-{√(S)} M/S", "(SIGN = DIRECTION)"], ["V² IS NEGATIVE", "IT NEVER GETS THAT FAR"]))
S += solver("K3", "FIND V (NO ACCEL)", ["DX=1/2(V+V0)T"],
            [("U", "V0", "M/S"), ("D", "DX", "M"), ("T", "T", "S")], ["2D/T-U→V"],
            ["DX=1/2(V+V0)T", "V=2DX/T-V0", "V=2*{D}/{T}-{U}", "V={2D/T}-{U}", "V={V} M/S"], "F1")
S += solver("K4", "DROPPED FROM HEIGHT", ["V0=0, FALLS DOWN"],
            [("H", "HEIGHT", "M")], ["√(2H/G)→T", "√(2GH)→V"],
            ["DROPPED SO V0=0", "DX=1/2GT²", "T=SQRT(2H/G)", "T=SQRT(2*{H}/{G})", "T={T} S",
             "V²=2GH", "V=SQRT(2*{G}*{H})", "V={V} M/S (DOWN)"], "F1")
S += solver("K5", "FIND DX (NO FINAL V)", ["DX=V0T+1/2AT²"],
            [("U", "V0", "M/S"), ("A", "A", "M/S²"), ("T", "T", "S")], ["UT+.5AT²→D"],
            ["DX=V0T+1/2AT²", "DX={U}*{T}+.5*{A}*{T}²", "DX={UT}+{.5AT²}", "DX={D} M"], "F2")
S += solver("K6", "FIND DX (NO ACCEL)", ["DX=1/2(V+V0)T"],
            [("U", "V0", "M/S"), ("V", "V", "M/S"), ("T", "T", "S")], [".5(V+U)T→D"],
            ["DX=1/2(V+V0)T", "DX=.5*({V}+{U})*{T}", "DX=.5*{V+U}*{T}", "DX={D} M"], "F2")
S += solver("K7", "FIND DX (NO TIME)", ["V²=V0²+2ADX", "STOPPING? V=0, A NEGATIVE"],
            [("U", "V0", "M/S"), ("V", "V", "M/S"), ("A", "A", "M/S²")], ["(V²-U²)/(2A)→D"],
            ["V²=V0²+2ADX", "DX=(V²-V0²)/(2A)", "DX=({V}²-{U}²)/(2*{A})", "DX={V²-U²}/{2A}", "DX={D} M"], "F2")
S += solver("K8", "THROWN STRAIGHT UP", ["AT THE TOP V=0"],
            [("U", "SPEED UP", "M/S")], ["U²/(2G)→H", "U/G→T"],
            ["TOP: V=0, A=-G", "0=V0²-2GH", "H=V0²/(2G)", "H={U}²/(2*{G})", "H={H} M",
             "0=V0-GT", "T TOP=V0/G={U}/{G}", "T TOP={T} S", "UP AND BACK={2T} S"], "F2")
S += solver("K9", "FIND A (NO DISTANCE)", ["A=(V-V0)/T"],
            [("U", "V0", "M/S"), ("V", "V", "M/S"), ("T", "T", "S")], ["(V-U)/T→A"],
            ["V=V0+AT", "A=(V-V0)/T", "A=({V}-{U})/{T}", "A={V-U}/{T}", "A={A} M/S²"], "F3",
            cond("A*V<0", ["V AND A OPPOSITE SIGNS", "SO IT IS SLOWING DOWN"]))
S += solver("KA", "FIND A (NO TIME)", ["V²=V0²+2ADX"],
            [("U", "V0", "M/S"), ("V", "V", "M/S"), ("D", "DX", "M")], ["(V²-U²)/(2D)→A"],
            ["V²=V0²+2ADX", "A=(V²-V0²)/(2DX)", "A=({V}²-{U}²)/(2*{D})", "A={V²-U²}/{2D}", "A={A} M/S²"], "F3")
S += solver("KB", "FIND A (NO FINAL V)", ["DX=V0T+1/2AT²"],
            [("U", "V0", "M/S"), ("D", "DX", "M"), ("T", "T", "S")], ["2(D-UT)/T²→A"],
            ["DX=V0T+1/2AT²", "A=2(DX-V0T)/T²", "A=2*({D}-{U}*{T})/{T}²", "A=2*{D-UT}/{T²}", "A={A} M/S²"], "F3")
S += solver("KC", "FIND T (NO DISTANCE)", ["T=(V-V0)/A"],
            [("U", "V0", "M/S"), ("V", "V", "M/S"), ("A", "A", "M/S²")], ["(V-U)/A→T"],
            ["V=V0+AT", "T=(V-V0)/A", "T=({V}-{U})/{A}", "T={V-U}/{A}", "T={T} S"], "F4",
            cond("T<0", ["T<0: CHECK YOUR SIGNS"]))
S += solver("KD", "FIND T (NO ACCEL)", ["DX=1/2(V+V0)T"],
            [("U", "V0", "M/S"), ("V", "V", "M/S"), ("D", "DX", "M")], ["2D/(V+U)→T"],
            ["DX=1/2(V+V0)T", "T=2DX/(V+V0)", "T=2*{D}/({V}+{U})", "T={2D}/{V+U}", "T={T} S"], "F4")
# quadratic for time
S += ["Lbl KE", "ClrHome", 'Disp "FIND T (NO FINAL V)","DX=V0T+1/2AT²","USES QUADRATIC FORMULA"',
      'Input "V0 (M/S) ",U', 'Input "A (M/S²) ",A', 'Input "DX (M) ",D',
      "U²+2AD→S", "If A=0", "D/U→T",
      "If A≠0 and S≥0", "(-U+√(S))/A→P", "If A≠0 and S≥0", "(-U-√(S))/A→Q",
      "If A≠0 and S≥0", "max(P,Q)→T", "If A≠0 and S≥0 and min(P,Q)>0", "min(P,Q)→T"]
S += assign(["GIVEN", "V0={U} M/S", "A={A} M/S²", "DX={D} M", "DX=V0T+1/2AT²"])
S += cond("A=0", ["A=0 SO DX=V0T", "T=DX/V0={D}/{U}", "T={T} S"])
S += cond("A≠0", ["1/2AT²+V0T-DX=0", "a={.5A} b={U} c={-D}", "T=(-b+/-SQRT(b²-4ac))/2a",
                  "b²-4ac=V0²+2A*DX={S}"])
S += cond("A≠0 and S<0", ["NEGATIVE: NEVER REACHES DX"])
S += cond("A≠0 and S≥0", ["T1={P} S", "T2={Q} S", "USE THE POSITIVE ONE", "T={T} S"])
S += show("F4")
S += solver("KF", "THROWN UP, LANDS LOWER", ["TYPE 0 IF IT LANDS AT", "THE SAME HEIGHT"],
            [("U", "SPEED UP", "M/S"), ("H", "START H", "M")],
            ["(U+√(U²+2GH))/G→T", "U-GT→V", "U²/(2G)→R"],
            ["UP IS +, A=-G, DY=-H", "-H=V0T-1/2GT²", "1/2GT²-V0T-H=0", "T=(V0+SQRT(V0²+2GH))/G",
             "T=({U}+SQRT({U}²+2*{G}*{H}))/{G}", "T={T} S", "V=V0-GT={U}-{G}*{T}", "V={V} M/S (-=DOWN)",
             "RISES {R} M ABOVE START"], "F4")
S += solver("KG", "FIND V0 (NO DISTANCE)", ["V0=V-AT"],
            [("V", "V", "M/S"), ("A", "A", "M/S²"), ("T", "T", "S")], ["V-AT→U"],
            ["V=V0+AT", "V0=V-AT", "V0={V}-{A}*{T}", "V0={U} M/S"], "F5")
S += solver("KH", "FIND V0 (NO TIME)", ["V0²=V²-2ADX"],
            [("V", "V", "M/S"), ("A", "A", "M/S²"), ("D", "DX", "M")], ["V²-2AD→S"],
            ["V²=V0²+2ADX", "V0²=V²-2ADX", "V0²={V}²-2*{A}*{D}", "V0²={S}"], "F5",
            cond("S≥0", ["V0={√(S)} M/S"], ["NEGATIVE: CHECK SIGNS"]))
S += solver("KI", "FIND V0 (NO FINAL V)", ["DX=V0T+1/2AT²"],
            [("D", "DX", "M"), ("A", "A", "M/S²"), ("T", "T", "S")], ["(D-.5AT²)/T→U"],
            ["DX=V0T+1/2AT²", "V0=(DX-1/2AT²)/T", "V0=({D}-{.5AT²})/{T}", "V0={U} M/S"], "F5")
S += solver("KJ", "LAUNCH SPEED FROM HEIGHT", ["THROWN UP, MAX HEIGHT H"],
            [("H", "MAX H", "M")], ["√(2GH)→U"],
            ["TOP: V=0", "0=V0²-2GH", "V0=SQRT(2GH)", "V0=SQRT(2*{G}*{H})", "V0={U} M/S"], "F5")

# ---- projectiles ----
S += ["Lbl PJ",
      'Menu("PROJECTILE","LEVEL GROUND",P1,"FLAT OFF A CLIFF",P2,"ANGLE + HEIGHT",P3,"LAUNCH SPEED",P4,"V AT A TIME",P5,"BACK",M']
S += solver("P1", "LEVEL GROUND", ["LANDS AT LAUNCH HEIGHT"],
            [("U", "V0", "M/S"), ("θ", "ANGLE", "DEG")],
            ["Ucos(θ)→X", "Usin(θ)→Y", "2Y/G→T", "XT→R", "Y²/(2G)→H"],
            ["VX=V0 COS θ={U}*{cos(θ)}", "VX={X} M/S", "VY=V0 SIN θ={U}*{sin(θ)}", "VY={Y} M/S",
             "T UP=VY/G={Y/G} S", "T TOTAL=2VY/G", "T={T} S", "RANGE=VX*T={X}*{T}", "RANGE={R} M",
             "MAX H=VY²/(2G)", "H={Y}²/(2*{G})", "H={H} M", "SPEED AT TOP=VX={X}"], "PJ")
S += solver("P2", "LAUNCHED FLAT (HORIZ)", ["VY0=0"],
            [("U", "V0", "M/S"), ("H", "HEIGHT", "M")],
            ["√(2H/G)→T", "UT→R", "GT→Y", "√(U²+Y²)→V", "tan⁻¹(Y/U)→θ"],
            ["Y: H=1/2GT²", "T=SQRT(2H/G)", "T=SQRT(2*{H}/{G})", "T={T} S", "X: RANGE=V0*T",
             "RANGE={U}*{T}", "RANGE={R} M", "LANDING VY=GT={Y} M/S", "V=SQRT(VX²+VY²)",
             "V=SQRT({U}²+{Y}²)", "V={V} M/S", "ANGLE {θ} DEG BELOW FLAT"], "PJ")
S += solver("P3", "ANGLE FROM A HEIGHT", ["H=HOW HIGH ABOVE LANDING"],
            [("U", "V0", "M/S"), ("θ", "ANGLE", "DEG"), ("H", "HEIGHT", "M")],
            ["Ucos(θ)→X", "Usin(θ)→Y", "(Y+√(Y²+2GH))/G→T", "XT→R", "H+Y²/(2G)→P", "Y-GT→W", "√(X²+W²)→V"],
            ["VX={X} M/S", "VY={Y} M/S", "UP +: -H=VYT-1/2GT²", "T=(VY+SQRT(VY²+2GH))/G",
             "T=({Y}+SQRT({Y}²+2*{G}*{H}))/{G}", "T={T} S", "RANGE=VX*T={X}*{T}", "RANGE={R} M",
             "MAX HEIGHT={P} M", "LAND VY=VY-GT={W}", "LAND SPEED={V} M/S"], "PJ")
S += solver("P4", "FIND LAUNCH SPEED", ["LAUNCHED FLAT FROM", "HEIGHT H, LANDS AT RANGE"],
            [("H", "HEIGHT", "M"), ("R", "RANGE", "M")], ["√(2H/G)→T", "R/T→U"],
            ["FALL TIME FIRST", "T=SQRT(2H/G)", "T=SQRT(2*{H}/{G})", "T={T} S", "V0=RANGE/T",
             "V0={R}/{T}", "V0={U} M/S"], "PJ")
S += solver("P5", "POSITION AND V AT TIME", ["START AT HEIGHT 0"],
            [("U", "V0", "M/S"), ("θ", "ANGLE", "DEG"), ("T", "TIME", "S")],
            ["Ucos(θ)→X", "Usin(θ)→Y", "Y-GT→W", "XT→R", "YT-.5GT²→H", "√(X²+W²)→V"],
            ["VX={X} M/S (SAME ALL T)", "VY=V0 SIN θ-GT", "VY={Y}-{G}*{T}={W}", "X=VX*T={R} M",
             "Y=VYT-1/2GT²", "Y={Y}*{T}-.5*{G}*{T}²", "Y={H} M", "SPEED={V} M/S"], "PJ")

# ---- vectors and relative motion ----
S += ["Lbl VC",
      'Menu("VECTORS+RIVER","COMPONENTS",V1,"FROM X AND Y",V2,"ADD 2 VECTORS",V3,"RIVER BOAT",V4,"RELATIVE V",V5,"BACK",M']
S += solver("V1", "COMPONENTS", ["ANGLE FROM THE +X AXIS"],
            [("A", "SIZE", ""), ("θ", "ANGLE", "DEG")], ["Acos(θ)→X", "Asin(θ)→Y"],
            ["AX=A COS θ", "AX={A}*{cos(θ)}", "AX={X}", "AY=A SIN θ", "AY={A}*{sin(θ)}", "AY={Y}"], "VC")
S += solver("V2", "BUILD FROM X AND Y", ["LEFT/DOWN = NEGATIVE"],
            [("X", "X PART", ""), ("Y", "Y PART", "")], ["R►Pr(X,Y)→A", "R►Pθ(X,Y)→θ"],
            ["A=SQRT(AX²+AY²)", "A=SQRT({X}²+{Y}²)", "A={A}", "θ=TAN-1(AY/AX)", "θ={θ} DEG FROM +X"], "VC")
S += solver("V3", "ADD TWO VECTORS", ["ANGLES FROM +X AXIS"],
            [("A", "A SIZE", ""), ("P", "A ANGLE", "DEG"), ("B", "B SIZE", ""), ("Q", "B ANGLE", "DEG")],
            ["Acos(P)+Bcos(Q)→X", "Asin(P)+Bsin(Q)→Y", "R►Pr(X,Y)→R", "R►Pθ(X,Y)→θ"],
            ["ADD X PARTS", "X={Acos(P)}+{Bcos(Q)}", "X={X}", "ADD Y PARTS", "Y={Asin(P)}+{Bsin(Q)}", "Y={Y}",
             "SIZE=SQRT(X²+Y²)", "SIZE={R}", "ANGLE={θ} DEG FROM +X"], "VC")
S += ["Lbl V4", "ClrHome", 'Disp "RIVER BOAT","1=AIMS STRAIGHT ACROSS","2=LANDS STRAIGHT ACROSS"',
      'Input "1 OR 2? ",Z', 'Input "BOAT V (M/S) ",B', 'Input "RIVER V (M/S) ",C', 'Input "WIDTH (M) ",W',
      "If Z=2", "Goto V6", "W/B→T", "CT→D", "√(B²+C²)→V", "tan⁻¹(C/B)→θ"]
S += assign(["GIVEN", "BOAT={B} M/S", "RIVER={C} M/S", "WIDTH={W} M", "AIMS STRAIGHT ACROSS",
             "T=WIDTH/VBOAT={W}/{B}", "T={T} S", "DRIFT=VRIVER*T={C}*{T}", "DRIFT={D} M DOWNSTREAM",
             "V=SQRT(VB²+VR²)", "V=SQRT({B}²+{C}²)={V} M/S", "{θ} DEG OFF STRAIGHT"]) + show("VC")
S += ["Lbl V6", "If C≥B", "Then", '"GIVEN!BOAT="+toString(B)+"!RIVER="+toString(C)+"!BOAT MUST BE FASTER!THAN THE RIVER"→Str0', "Else",
      "√(B²-C²)→V", "W/V→T", "sin⁻¹(C/B)→θ"]
S += assign(["GIVEN", "BOAT={B} M/S", "RIVER={C} M/S", "WIDTH={W} M", "AIM UPSTREAM",
             "SIN(AIM)=VR/VB={C}/{B}", "AIM={θ} DEG UPSTREAM", "V ACROSS=SQRT(VB²-VR²)",
             "V=SQRT({B}²-{C}²)={V} M/S", "T=WIDTH/V={W}/{V}", "T={T} S"]) + ["End"] + show("VC")
S += solver("V5", "RELATIVE VELOCITY", ["BOTH MEASURED FROM GROUND", "SAME DIRECTION = SAME SIGN"],
            [("A", "V OF A", "M/S"), ("B", "V OF B", "M/S")], ["A-B→C"],
            ["A AS SEEN BY B", "V=VA-VB", "V={A}-{B}", "V={C} M/S", "B AS SEEN BY A={-C} M/S",
             "WALKING ON A TRAIN?", "V GROUND=V WALK+V TRAIN", "SO V WALK=VA-VB TOO"], "VC")

# ---- graphs ----
S += ["Lbl GR",
      'Menu("GRAPHS","SLOPE 2 POINTS",R1,"AREA TRIANGLE",R2,"AREA TRAPEZOID",R3,"AREA RECTANGLE",R4,"AVG SPEED+VEL",R5,"BACK",M']
S += solver("R1", "SLOPE FROM 2 POINTS", ["X-T SLOPE=VELOCITY", "V-T SLOPE=ACCELERATION"],
            [("P", "TIME 1", "S"), ("A", "VALUE 1", ""), ("Q", "TIME 2", "S"), ("B", "VALUE 2", "")],
            ["(B-A)/(Q-P)→S"],
            ["SLOPE=RISE/RUN", "=({B}-{A})/({Q}-{P})", "={B-A}/{Q-P}", "SLOPE={S}"], "GR")
S += solver("R2", "TRIANGLE AREA", ["V-T AREA=DISPLACEMENT"],
            [("T", "BASE TIME", "S"), ("V", "HEIGHT V", "M/S")], [".5TV→D"],
            ["AREA=1/2*BASE*HEIGHT", "=.5*{T}*{V}", "DX={D} M"], "GR")
S += solver("R3", "TRAPEZOID AREA", ["V-T AREA=DISPLACEMENT"],
            [("T", "TIME", "S"), ("U", "V START", "M/S"), ("V", "V END", "M/S")], [".5(U+V)T→D"],
            ["AREA=1/2(V1+V2)T", "=.5*({U}+{V})*{T}", "DX={D} M"], "GR")
S += solver("R4", "RECTANGLE AREA", ["V-T AREA=DISPLACEMENT"],
            [("T", "TIME", "S"), ("V", "V", "M/S")], ["TV→D"],
            ["AREA=V*T", "={V}*{T}", "DX={D} M"], "GR")
S += solver("R5", "AVERAGE SPEED + VELOCITY", ["DISTANCE=TOTAL PATH", "DISPLACEMENT=START TO END"],
            [("D", "DISTANCE", "M"), ("X", "DISPLACE", "M"), ("T", "TIME", "S")], ["D/T→S", "X/T→V"],
            ["AVG SPEED=DIST/T", "={D}/{T}={S} M/S", "AVG VEL=DISPL/T", "={X}/{T}={V} M/S"], "GR")

# ---- hidden values + notes ----
S += ["Lbl H0",
      'Menu("HIDDEN VALUES","CLUE WORDS",' + "N2" + ',"KM/H TO M/S",H1,"MPH TO M/S",H2,"BACK",M']
S += solver("H1", "KM/H TO M/S", ["DIVIDE BY 3.6"], [("K", "SPEED", "KM/H")], ["K/3.6→V"],
            ["1 KM/H=1000M/3600S", "V={K}/3.6", "V={V} M/S"], "H0")
S += solver("H2", "MPH TO M/S", ["MULTIPLY BY .447"], [("K", "SPEED", "MPH")], ["K*.44704→V"],
            ["1 MPH=.447 M/S", "V={K}*.447", "V={V} M/S"], "H0")
labs = {}
def nl(t):
    labs.setdefault(t, "N" + "123456789ABCDEF"[len(labs)])
    return labs[t]
titles = [t for t, _ in NOTES]
for t in titles: nl(t)
S += ["Lbl NM", 'Menu("NOTES",' + ",".join(f'"{t}",{nl(t)}' for t in titles[:5]) + ',"MORE",NN,"BACK",M',
      "Lbl NN", 'Menu("NOTES 2",' + ",".join(f'"{t}",{nl(t)}' for t in titles[5:]) + ',"BACK",NM']
for t, (a, b) in ranges.items():
    S += [f"Lbl {nl(t)}", f"{a}→A", f"{b}→B", "Goto S"]
S += slide_viewer("NM")

# ---- custom ----
from customeq import custom
S += custom([
  ("V=V0+AT", "V-U-AT", "VUAT", ["V=FINAL V (M/S)", "U=V0 START (M/S)", "A=ACCEL (M/S²)", "T=TIME (S)"]),
  ("DX=V0T+1/2AT²", "D-UT-.5AT²", "DUAT", ["D=DX (M)", "U=V0 (M/S)", "A=ACCEL (M/S²)", "T=TIME (S)"]),
  ("V²=V0²+2ADX", "V²-U²-2AD", "VUAD", ["V=FINAL V (M/S)", "U=V0 (M/S)", "A=ACCEL", "D=DX (M)"]),
  ("DX=1/2(V+V0)T", "D-.5(V+U)T", "DVUT", ["D=DX (M)", "V=FINAL V", "U=V0", "T=TIME (S)"]),
  ("AX=A COS θ", "X-Acos(θ)", "XAθ", ["X=X PART", "A=SIZE", "θ=ANGLE (DEG)"]),
  ("V=DX/T", "V-D/T", "VDT", ["V=VELOCITY (M/S)", "D=DX (M)", "T=TIME (S)"]),
], "MO", "C")

S += ["Lbl ZZ", "ClrHome", 'Disp "TYPE 10 OR 9.8"', 'Input "G=",G', "If G≤0", "10→G", "Goto M",
      "Lbl Q", "ClrHome", 'Disp "GOOD LUCK"']
add(S)
rets = [l[1:l.index('"', 1)] for l in L if l.endswith('→Str7') and l.startswith('"')]
# viewer must come before the final Lbl Q block ends the program: put it before Lbl ZZ
q = L.index("Lbl ZZ")
L[q:q] = viewer(rets, "M")
if __name__ == "__main__":
    build("P1MOTION", L)
