"""關卡 1：覆蓋率。檢索結果 sources.md 是否足夠做一份簡報。

通過條件：列出的頁面都存在、概念頁 >= 3、這些頁面引用到的來源 >= 5。
不足就停下，回去補 ingest，不用模型自己的知識硬湊。
"""
import sys
from common import CITE, LINK, TOPIC, WIKI, finish

text = (TOPIC / "sources.md").read_text(encoding="utf-8")
errors, concepts, cited = [], [], set()
for target in LINK.findall(text):
    page = (TOPIC / target).resolve()
    if not page.exists():
        errors.append(f"sources.md 列出的頁面不存在：{target}")
        continue
    if page.parent.name == "concepts":
        concepts.append(page.name)
        cited |= set(CITE.findall(page.read_text(encoding="utf-8")))
all_concepts = {p.name for p in (WIKI / "concepts").glob("*.md")}
if len(concepts) < 3:
    errors.append(f"相關概念頁只有 {len(concepts)} 頁，少於 3 頁")
if len(cited) < 5:
    errors.append(f"引用到的來源只有 {len(cited)} 篇，少於 5 篇")
info = [f"相關概念頁 {len(concepts)} / wiki 共 {len(all_concepts)} 頁",
        f"涵蓋來源 {len(cited)} 篇：{' '.join(sorted(cited))}",
        f"未選用的概念頁：{'、'.join(sorted(all_concepts - set(concepts))) or '無'}"]
sys.exit(finish("關卡 1 覆蓋率", info, errors))
