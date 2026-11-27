"""Builds workshop pages: a list of hands-on missions run by assets/js/workshop.js."""
import json
from gen_unit import page, chapter

def M(mid, title, brief, spec, win=None, hints=None):
    spec = dict(spec); spec["id"] = mid
    if win: spec["win"] = win
    if hints: spec["hints"] = hints
    return (mid, title, brief, spec)

def build_ws(course, out, name, h1, intro, groups, extra_js, footer, keep_sims=False):
    n = 0; chs = []
    for ci, (t, short, ms) in enumerate(groups):
        secs = []
        for (mid, title, brief, spec) in ms:
            n += 1
            data = json.dumps(spec, ensure_ascii=False).replace("&", "&amp;").replace("'", "&#39;")
            secs.append(f'<section class="topic mission" id="m-{mid}" data-m=\'{data}\'>\n  <h2><span class="pill">Mission {n}</span>{title}</h2>\n  <p class="sub">{brief}</p>\n  <div class="m-play"></div>\n</section>')
        chs.append(chapter(f"ws-ch{ci + 1}", t, short, secs))
    html = page("workshop", f"{name} Workshop", f"{name} · Workshop", h1, intro, f"Interactive {name} workshop: hands-on missions with goals, hints and stars.", chs, {}, course=course, footer=footer, extra_js=tuple(extra_js) + ("workshop.js",))
    html = html.replace('</div>\n\n<main class="page">', '</div>\n<div class="ws-meter"></div>\n\n<main class="page">', 1)
    if not keep_sims:
        html = html.replace('<script src="../../assets/js/sims.js"></script>\n', "")
    html = html.replace('<script src="../../assets/js/exam.js"></script>\n', "")
    open(out, "w").write(html)
    print(out, n, "missions")
    return n
