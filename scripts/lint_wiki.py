"""Wiki 健康檢查（lint）。

檢查四項（見 AGENTS.md）：
  1. 連結沒有斷
  2. 概念頁每條說法都有出處，且出處存在
  3. index.md 列出所有頁面，且沒有孤兒頁
  4. 數字能在所引用來源的 raw/ 檔案找到

用法：python scripts/lint_wiki.py [--record "說明"]
有任何錯誤時 exit code 為 1。
"""
import re
import sys
from datetime import datetime
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
RAW = ROOT / "raw"
HISTORY = ROOT / "logs" / "lint-history.md"

LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
CITE = re.compile(r"\[(S\d+)\]")
NUM = re.compile(r"\d[\d,]*(?:\.\d+)?")


def numbers(text):
    """取出文字中的數字（去掉千分位逗號）。"""
    text = LINK.sub(lambda m: m.group(0).split("](")[0], text)  # 去掉連結網址
    text = re.sub(r"\bS\d+\b", "", text)  # 去掉來源代號
    return {n.replace(",", "").rstrip(".") for n in NUM.findall(text)}


def rel(p):
    return p.relative_to(ROOT).as_posix()


def main():
    pages = sorted(WIKI.rglob("*.md"))
    content_pages = [p for p in pages if p.name not in ("index.md", "log.md")]
    raw_files = {p.name.split("-")[0].upper(): p for p in RAW.glob("S*.md")} if RAW.exists() else {}
    source_pages = {p.name.split("-")[0].upper(): p for p in (WIKI / "sources").glob("s*.md")}
    raw_numbers = {sid: numbers(p.read_text(encoding="utf-8")) for sid, p in raw_files.items()}

    errors = {1: [], 2: [], 3: [], 4: []}
    inbound = {p: set() for p in pages}

    for page in pages:
        text = page.read_text(encoding="utf-8")
        # 1. 連結
        for target in LINK.findall(text):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            dest = (page.parent / target.split("#")[0]).resolve()
            if not dest.exists():
                errors[1].append(f"{rel(page)}：連結 {target} 不存在")
            elif dest in inbound and dest != page:
                inbound[dest].add(page)

        is_concept = page.parent.name == "concepts"
        is_source = page.parent.name == "sources"
        section = ""
        for i, line in enumerate(text.splitlines(), 1):
            if line.startswith("#"):
                section = line.lstrip("# ").strip()
                continue
            # 2. 出處
            if is_concept and line.lstrip().startswith("- ") and section != "相關頁面":
                cites = CITE.findall(line)
                if not cites:
                    errors[2].append(f"{rel(page)}:{i} 這條說法沒有出處")
                for sid in cites:
                    if sid not in source_pages or sid not in raw_files:
                        errors[2].append(f"{rel(page)}:{i} 出處 {sid} 沒有對應的來源頁或 raw 檔")
                # 4. 數字
                allowed = set().union(*[raw_numbers.get(s, set()) for s in cites]) if cites else set()
                for n in sorted(numbers(line) - allowed):
                    errors[4].append(f"{rel(page)}:{i} 數字 {n} 在 {''.join(cites) or '（無出處）'} 的 raw 檔找不到")
            if is_source:
                sid = page.name.split("-")[0].upper()
                for n in sorted(numbers(line) - raw_numbers.get(sid, set())):
                    errors[4].append(f"{rel(page)}:{i} 數字 {n} 在 {sid} 的 raw 檔找不到")

    # 2b. 來源頁必須有對應 raw 檔
    for sid, p in source_pages.items():
        if sid not in raw_files:
            errors[2].append(f"{rel(p)}：找不到 raw/{sid}-*.md")

    # 3. 目錄與孤兒頁
    index = WIKI / "index.md"
    for p in content_pages:
        if index not in inbound[p]:
            errors[3].append(f"{rel(p)}：index.md 沒有列出這一頁")
        if not (inbound[p] - {index, WIKI / 'log.md'}):
            errors[3].append(f"{rel(p)}：孤兒頁，沒有被其他內容頁連結")

    names = {1: "連結沒有斷", 2: "每條說法有出處", 3: "目錄完整、無孤兒頁", 4: "數字能在 raw/ 找到"}
    total = sum(len(v) for v in errors.values())
    lines = [f"檢查 {len(content_pages)} 個內容頁（概念頁 {sum(p.parent.name == 'concepts' for p in pages)}、來源頁 {len(source_pages)}），raw 檔 {len(raw_files)} 個"]
    for k in (1, 2, 3, 4):
        lines.append(f"[{'PASS' if not errors[k] else 'FAIL'}] {k}. {names[k]}（{len(errors[k])} 個問題）")
        lines.extend(f"    - {e}" for e in errors[k])
    lines.append("結果：" + ("全部通過" if total == 0 else f"共 {total} 個問題"))
    print("\n".join(lines))

    if "--record" in sys.argv:
        note = sys.argv[sys.argv.index("--record") + 1]
        HISTORY.parent.mkdir(exist_ok=True)
        if not HISTORY.exists():
            HISTORY.write_text("# Lint 執行紀錄\n\n由 `scripts/lint_wiki.py --record` 自動寫入。\n", encoding="utf-8")
        with HISTORY.open("a", encoding="utf-8") as f:
            f.write(f"\n## {datetime.now():%Y-%m-%d %H:%M:%S} {note}\n\n```\n" + "\n".join(lines) + "\n```\n")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
