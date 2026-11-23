"""渲染節點：把已通過檢查的逐頁稿轉成 docs/index.html。

這個節點是純程式，只排版、不改字：內文一律來自 drafts/，
每頁底部的出處由該頁引用的證據卡自動產生。
"""
import html
import json
import re
import sys
from common import ROOT, TOPIC, WIKI, load_cards, parse_draft

OUT = ROOT / "docs" / "index.html"
config = json.loads((TOPIC / "config.json").read_text(encoding="utf-8"))
REPO = config.get("repo_url", "").rstrip("/")


def wiki_url(page):
    return f"{REPO}/blob/main/wiki/{page}" if REPO else f"../wiki/{page}"


def page_title(page):
    first = (WIKI / page).read_text(encoding="utf-8").splitlines()[0]
    return first.lstrip("# ").strip()


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    return re.sub(r"`(.+?)`", r"<code>\1</code>", s)


def render_body(body, layout):
    out, items, table = [], [], []

    def flush():
        nonlocal items, table
        if items:
            if layout == "grid":
                cols = 2 if len(items) in (2, 4) else 3
                cells = []
                for it in items:
                    m = re.match(r"\*\*(.+?)\*\*[：:]\s*(.*)", it)
                    cells.append(f"<div class=\"gcard\"><h3>{inline(m.group(1))}</h3><p>{inline(m.group(2))}</p></div>"
                                 if m else f"<div class=\"gcard\"><p>{inline(it)}</p></div>")
                out.append(f"<div class=\"grid\" style=\"--cols:{cols}\">{''.join(cells)}</div>")
            else:
                out.append("<ul>" + "".join(f"<li>{inline(it)}</li>" for it in items) + "</ul>")
            items = []
        if table:
            head, *rows = table
            out.append("<table><thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead><tbody>"
                       + "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows)
                       + "</tbody></table>")
            table = []

    for line in body.splitlines():
        line = line.rstrip()
        if line.startswith("- "):
            items.append(line[2:])
            continue
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip("|").split("|")]
            if not all(re.fullmatch(r":?-+:?", c) for c in cells):
                table.append(cells)
            continue
        flush()
        if not line:
            continue
        if line.startswith("## "):
            out.append(f"<p class=\"lead\">{inline(line[3:])}</p>")
        elif line.startswith("> "):
            out.append(f"<p class=\"callout\">{inline(line[2:])}</p>")
        else:
            out.append(f"<p>{inline(line)}</p>")
    flush()
    return "\n".join(out)


def main():
    cards = load_cards()
    drafts = sorted((TOPIC / "drafts").glob("*.md"))
    sections = []
    for f in drafts:
        meta, body = parse_draft(f)
        n, layout = int(meta["slide"]), meta.get("layout", "list")
        pages, sids = [], []
        for c in meta["cards"]:
            if cards[c]["page"] not in pages:
                pages.append(cards[c]["page"])
            sids += [s for s in cards[c]["cites"] if s not in sids]
        src_pages = {p.name.split("-")[0].upper(): "sources/" + p.name for p in (WIKI / "sources").glob("s*.md")}
        footer = ""
        if pages:
            links = " · ".join(f"<a href=\"{wiki_url(p)}\">{html.escape(page_title(p))}</a>" for p in pages)
            ids = " ".join(f"<a href=\"{wiki_url(src_pages[s])}\">{s}</a>" for s in sorted(sids, key=lambda x: int(x[1:])))
            footer = f"<footer><span class=\"src\">出處｜Wiki：{links}｜來源：{ids}</span><span class=\"pg\">{n} / {len(drafts)}</span></footer>"
        else:
            footer = f"<footer><span class=\"src\"></span><span class=\"pg\">{n} / {len(drafts)}</span></footer>"
        if layout == "cover":
            inner = f"<div class=\"body\"><h1>{inline(meta['title'])}</h1>\n{render_body(body, layout)}</div>"
        else:
            inner = (f"<header><span class=\"stage\">{html.escape(meta.get('stage', ''))}</span><h2>{inline(meta['title'])}</h2></header>\n"
                     f"<div class=\"body\">\n{render_body(body, layout)}\n</div>")
        sections.append(f"<section class=\"slide {layout}\" data-n=\"{n}\">\n{inner}\n{footer}\n</section>")
    page = (ROOT / "scripts" / "template.html").read_text(encoding="utf-8")
    page = page.replace("{{TITLE}}", html.escape(config["deck_title"])).replace("{{SLIDES}}", "\n".join(sections))
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(page, encoding="utf-8")
    print(f"已產生 {OUT.relative_to(ROOT).as_posix()}：{len(sections)} 頁")


if __name__ == "__main__":
    sys.exit(main())
