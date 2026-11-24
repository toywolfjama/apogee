"""Apply the clean design + brand to every built HTML page (idempotent)."""
import re, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
pages = [p for p in ROOT.rglob("*.html") if ".git" not in p.parts and "node_modules" not in p.parts]
for p in pages:
    s = p.read_text()
    m = re.search(r'<body class="([^"]*)"([^>]*)>', s)
    if m:
        course = re.search(r'data-course="([^"]*)"', m.group(2))
        cls = "th-clean " + (f"c-{course.group(1)}" if course and course.group(1) else ("home" if p.name == "index.html" and p.parent == ROOT else "c-" + p.stem))
        s = s[:m.start()] + f'<body class="{cls}"{m.group(2)}>' + s[m.end():]
    if "clean.css" not in s:
        s = re.sub(r'(<link rel="stylesheet" href="([./]*)assets/css/site.css">)', r'\1\n<link rel="stylesheet" href="\2assets/css/clean.css">', s, count=1)
    s = s.replace("Apogee", "Crux")
    s = re.sub(r'https://fonts\.googleapis\.com/css2\?[^"]+', "https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&family=Bricolage+Grotesque:opsz,wght@12..96,500..800&family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=JetBrains+Mono:wght@400;500;700&display=swap", s)
    p.write_text(s)
print(len(pages), "pages cleaned")
