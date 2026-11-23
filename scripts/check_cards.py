"""關卡 2：證據卡。每張卡只能來自一個 wiki 頁面。

通過條件：卡片檔指向的 wiki 頁存在；每張卡有編號與出處；
出處在該 wiki 頁出現過；卡片裡的數字在該 wiki 頁找得到；編號不重複。
"""
import sys
from common import CARD_ID, CITE, TOPIC, WIKI, finish, numbers

errors, seen, total = [], set(), 0
files = sorted((TOPIC / "cards").glob("*.md"))
for f in files:
    lines = f.read_text(encoding="utf-8").splitlines()
    page_rel = next((l.split(":", 1)[1].strip() for l in lines if l.startswith("wiki:")), "")
    page = WIKI / page_rel
    if not page_rel or not page.exists():
        errors.append(f"{f.name}：wiki 頁面 {page_rel or '（未填）'} 不存在")
        continue
    wiki_text = page.read_text(encoding="utf-8")
    wiki_cites, wiki_nums = set(CITE.findall(wiki_text)), numbers(wiki_text)
    for i, line in enumerate(lines, 1):
        if not line.startswith("- "):
            continue
        total += 1
        m = CARD_ID.search(line)
        if not m:
            errors.append(f"{f.name}:{i} 卡片沒有編號")
            continue
        cid = m.group(1)
        if cid in seen:
            errors.append(f"{f.name}:{i} 編號 {cid} 重複")
        seen.add(cid)
        cites = CITE.findall(line)
        if not cites:
            errors.append(f"{f.name}:{i} {cid} 沒有出處")
        for s in cites:
            if s not in wiki_cites:
                errors.append(f"{f.name}:{i} {cid} 的出處 {s} 不在 {page_rel}")
        for n in sorted(numbers(line) - wiki_nums):
            errors.append(f"{f.name}:{i} {cid} 的數字 {n} 在 {page_rel} 找不到")
info = [f"卡片檔 {len(files)} 個，卡片 {total} 張"]
sys.exit(finish("關卡 2 證據卡", info, errors))
