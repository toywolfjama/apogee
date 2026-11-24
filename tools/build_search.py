"""Build assets/js/search-index.js from every built course page."""
import re, json, html, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
names = {}
js = (ROOT / "assets/js/courses.js").read_text()
for cid, nm in re.findall(r'id: "([^"]+)",\s*name: "([^"]+)",\s*blurb', js): names[cid] = nm
out = []
strip = lambda s: re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", s))).strip()
for p in sorted((ROOT / "courses").rglob("*.html")):
    s = p.read_text(); rel = p.relative_to(ROOT).as_posix()
    unit = strip(re.search(r"<title>(.*?)</title>", s).group(1).split("|")[0])
    course = names.get(re.search(r'data-course="([^"]*)"', s).group(1), "")
    for cid, t in re.findall(r'<div class="chapter" id="([^"]+)" data-title="([^"]+)"', s):
        if t in ("Practice Questions", "Challenge Questions", "Hard Questions", "Practice Exam", "Timed Set"): continue
        out.append({"t": strip(t), "u": unit, "c": course, "h": f"{rel}#{cid}", "k": "chapter"})
    for tid, h2 in re.findall(r'<section class="topic" id="([^"]+)">\s*<h2>(.*?)</h2>', s, re.S):
        t = strip(re.sub(r'<span class="pill[^"]*">.*?</span>', "", h2))
        if t: out.append({"t": t, "u": unit, "c": course, "h": f"{rel}#{tid}", "k": "topic"})
(ROOT / "assets/js/search-index.js").write_text("window.SEARCH_INDEX=" + json.dumps(out, ensure_ascii=False, separators=(",", ":")) + ";\n")
print(len(out), "entries")
