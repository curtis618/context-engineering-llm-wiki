"""關卡 3：大綱。通過後才交給人確認。

通過條件：8–15 頁、頁碼連續；每個內容頁至少對應一張卡且卡片存在；
教學階段依「開場→為什麼→是什麼→怎麼做→實務→總結」的順序且四個必要階段都有；
用到的來源 >= 5 篇。
"""
import sys
from common import finish, load_cards, parse_outline

STAGES = ["開場", "為什麼", "是什麼", "怎麼做", "實務", "總結"]
REQUIRED = ["為什麼", "是什麼", "怎麼做", "總結"]

rows, cards, errors = parse_outline(), load_cards(), []
if not 8 <= len(rows) <= 15:
    errors.append(f"共 {len(rows)} 頁，不在 8–15 頁內")
if [r["n"] for r in rows] != list(range(1, len(rows) + 1)):
    errors.append("頁碼不連續")
used, sources, last = set(), set(), 0
for r in rows:
    if r["stage"] not in STAGES:
        errors.append(f"第 {r['n']} 頁：階段「{r['stage']}」不在 {STAGES}")
        continue
    idx = STAGES.index(r["stage"])
    if idx < last:
        errors.append(f"第 {r['n']} 頁：階段「{r['stage']}」順序倒退")
    last = max(last, idx)
    if r["stage"] != "開場" and not r["cards"]:
        errors.append(f"第 {r['n']} 頁：沒有對應任何證據卡")
    for c in r["cards"]:
        if c not in cards:
            errors.append(f"第 {r['n']} 頁：卡片 {c} 不存在")
        else:
            used.add(c)
            sources |= set(cards[c]["cites"])
for s in REQUIRED:
    if s not in [r["stage"] for r in rows]:
        errors.append(f"缺少必要的教學階段「{s}」")
if len(sources) < 5:
    errors.append(f"只用到 {len(sources)} 篇來源，少於 5 篇")
unused = sorted(set(cards) - used)
info = [f"共 {len(rows)} 頁，用到卡片 {len(used)} / {len(cards)} 張",
        f"用到來源 {len(sources)} 篇：{' '.join(sorted(sources))}",
        f"未用到的卡片（僅供參考）：{' '.join(unused) or '無'}"]
sys.exit(finish("關卡 3 大綱", info, errors))
