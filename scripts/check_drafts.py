"""關卡 4：逐頁稿（程式檢查）。

通過條件：頁數與大綱相同；每頁引用的卡片與大綱一致；
內文的數字都能在該頁引用的卡片裡找到；標題與內文沒有超過字數上限。
用法：python scripts/check_drafts.py [頁碼 ...]（不給頁碼就檢查全部）
"""
import re
import sys
from common import TOPIC, finish, load_cards, numbers, parse_draft, parse_outline

MAX_TITLE, MAX_BODY, MAX_ITEMS, MAX_ITEM = 20, 260, 6, 70


def visible(text):
    """去掉 markdown 符號與空白後的可見字數。"""
    return len(re.sub(r"[\s*|>#`\-]", "", text))


rows, cards, errors = parse_outline(), load_cards(), []
only = {int(a) for a in sys.argv[1:] if a.isdigit()}
files = sorted((TOPIC / "drafts").glob("*.md"))
if len(files) != len(rows):
    errors.append(f"逐頁稿 {len(files)} 頁，大綱 {len(rows)} 頁，數量不符")
checked = 0
for f in files:
    meta, body = parse_draft(f)
    n = int(meta["slide"])
    if only and n not in only:
        continue
    checked += 1
    row = next((r for r in rows if r["n"] == n), None)
    if row is None:
        errors.append(f"第 {n} 頁：大綱裡沒有這一頁")
        continue
    if meta["cards"] != row["cards"]:
        errors.append(f"第 {n} 頁：卡片 {meta['cards']} 與大綱 {row['cards']} 不一致")
    allowed = set()
    for c in meta["cards"]:
        if c in cards:
            allowed |= numbers(cards[c]["text"])
        else:
            errors.append(f"第 {n} 頁：卡片 {c} 不存在")
    for num in sorted(numbers(meta["title"] + "\n" + body) - allowed):
        errors.append(f"第 {n} 頁：數字 {num} 在引用的卡片裡找不到")
    if visible(meta["title"]) > MAX_TITLE:
        errors.append(f"第 {n} 頁：標題 {visible(meta['title'])} 字，超過 {MAX_TITLE}")
    if visible(body) > MAX_BODY:
        errors.append(f"第 {n} 頁：內文 {visible(body)} 字，超過 {MAX_BODY}")
    items = [l for l in body.splitlines() if l.startswith("- ")]
    if len(items) > MAX_ITEMS:
        errors.append(f"第 {n} 頁：條列 {len(items)} 點，超過 {MAX_ITEMS}")
    for l in items:
        if visible(l) > MAX_ITEM:
            errors.append(f"第 {n} 頁：有一點 {visible(l)} 字，超過 {MAX_ITEM}：{l[:18]}…")
info = [f"檢查 {checked} 頁（上限：標題 {MAX_TITLE} 字、內文 {MAX_BODY} 字、{MAX_ITEMS} 點、每點 {MAX_ITEM} 字）"]
sys.exit(finish("關卡 4 逐頁稿", info, errors))
