"""關卡 6：渲染（程式檢查）。確認渲染節點只排版、沒改字。

通過條件：HTML 頁數與逐頁稿相同；每頁的標題與每一行內文都原樣出現在 HTML；
每個內容頁的頁尾有 wiki 連結與來源代號，且代號與證據卡一致。
版面是否溢出另外用瀏覽器實測（window.checkOverflow()）。
"""
import html
import re
import sys
from common import ROOT, TOPIC, finish, load_cards, parse_draft

page = (ROOT / "docs" / "index.html").read_text(encoding="utf-8")
sections = dict(re.findall(r'<section class="slide[^"]*" data-n="(\d+)">(.*?)</section>', page, re.S))
drafts = sorted((TOPIC / "drafts").glob("*.md"))
cards, errors = load_cards(), []


def squash(s):
    return re.sub(r"\s+", "", s)


if len(sections) != len(drafts):
    errors.append(f"HTML {len(sections)} 頁，逐頁稿 {len(drafts)} 頁，數量不符")
lines_checked = 0
for f in drafts:
    meta, body = parse_draft(f)
    n = meta["slide"]
    sec = sections.get(str(int(n)))
    if sec is None:
        errors.append(f"第 {n} 頁：HTML 裡沒有這一頁")
        continue
    text = squash(html.unescape(re.sub(r"<[^>]+>", "", sec)))
    pieces = [meta["title"]]
    for line in body.splitlines():
        if line.startswith("|"):
            pieces += [c for c in line.strip("|").split("|") if not re.fullmatch(r"\s*:?-+:?\s*", c)]
        elif line.strip():
            pieces.append(re.sub(r"^(- |> |## )", "", line))
    for p in pieces:
        p = squash(re.sub(r"\*\*|`", "", p))
        lines_checked += 1
        if p and p not in text:
            errors.append(f"第 {n} 頁：這段文字沒有原樣出現在 HTML：{p[:20]}…")
    want = {s for c in meta["cards"] for s in cards[c]["cites"]}
    foot = re.search(r"<footer>(.*?)</footer>", sec, re.S).group(1)
    got = set(re.findall(r">(S\d+)</a>", foot))
    if want != got:
        errors.append(f"第 {n} 頁：頁尾來源 {sorted(got)} 與卡片 {sorted(want)} 不一致")
    if want and "Wiki：<a " not in foot:
        errors.append(f"第 {n} 頁：頁尾沒有 wiki 連結")
info = [f"HTML {len(sections)} 頁，比對 {lines_checked} 段文字"]
sys.exit(finish("關卡 6 渲染（文字與出處）", info, errors))
