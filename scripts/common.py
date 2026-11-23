"""各檢查關卡共用的工具。"""
import re
import sys
from datetime import datetime
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
TOPIC = ROOT / "topic-context-engineering"
REPORT = TOPIC / "report.md"

LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
CITE = re.compile(r"\[(S\d+)\]")
NUM = re.compile(r"\d[\d,]*(?:\.\d+)?")
CARD_ID = re.compile(r"\*\*([A-Z]+-\d+)\*\*")
CARD_REF = re.compile(r"[A-Z]+-\d+")


def numbers(text):
    """取出文字中的數字（去掉連結網址、來源代號、卡片編號、千分位逗號）。"""
    text = LINK.sub(lambda m: m.group(0).split("](")[0], text)
    text = CARD_ID.sub("", text)
    text = re.sub(r"\bS\d+\b", "", text)
    return {n.replace(",", "").rstrip(".") for n in NUM.findall(text)}


def load_cards():
    """讀取所有證據卡。回傳 {卡片編號: {text, cites, page, file}}。"""
    cards = {}
    for f in sorted((TOPIC / "cards").glob("*.md")):
        lines = f.read_text(encoding="utf-8").splitlines()
        page = ""
        for line in lines:
            if line.startswith("wiki:"):
                page = line.split(":", 1)[1].strip()
            m = CARD_ID.search(line)
            if line.startswith("- ") and m:
                cards[m.group(1)] = {
                    "text": CARD_ID.sub("", line[2:]).strip(),
                    "cites": CITE.findall(line),
                    "page": page,
                    "file": f.name,
                }
    return cards


def parse_draft(path):
    """讀取逐頁稿：--- 之間是欄位，後面是內文。"""
    text = path.read_text(encoding="utf-8")
    _, head, body = text.split("---", 2)
    meta = {}
    for line in head.strip().splitlines():
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip()
    meta["cards"] = CARD_REF.findall(meta.get("cards", ""))
    return meta, body.strip()


def parse_outline():
    """讀取 outline.md 的表格。回傳 [{n, stage, title, purpose, cards}]。"""
    rows = []
    for line in (TOPIC / "outline.md").read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 5 and cells[0].isdigit():
            rows.append({"n": int(cells[0]), "stage": cells[1], "title": cells[2],
                         "purpose": cells[3], "cards": CARD_REF.findall(cells[4])})
    return rows


def finish(gate, info, errors):
    """印出結果並寫入 report.md。回傳 exit code。"""
    status = "PASS" if not errors else "FAIL"
    lines = [f"[{status}] {gate}"] + [f"  {x}" for x in info] + [f"  - {e}" for e in errors]
    lines.append("  結果：" + ("通過" if not errors else f"{len(errors)} 個問題，退回"))
    print("\n".join(lines))
    TOPIC.mkdir(exist_ok=True)
    if not REPORT.exists():
        REPORT.write_text("# 執行與檢查紀錄\n\n由各關卡腳本自動寫入，人工確認與 AI 審查的結果另外註記。\n", encoding="utf-8")
    note = sys.argv[sys.argv.index("--note") + 1] if "--note" in sys.argv else ""
    with REPORT.open("a", encoding="utf-8") as f:
        f.write(f"\n### {datetime.now():%H:%M:%S} {gate} {status}" + (f"（{note}）" if note else "") + "\n\n```\n" + "\n".join(lines) + "\n```\n")
    return 1 if errors else 0
