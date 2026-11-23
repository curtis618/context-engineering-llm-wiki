"""產生橫式流程圖 workflow/flowchart.png。用法：python scripts/make_flowchart.py"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

ROOT = Path(__file__).resolve().parent.parent
REG = FontProperties(fname=r"C:\Windows\Fonts\msjh.ttc")
BOLD = FontProperties(fname=r"C:\Windows\Fonts\msjhbd.ttc")
PAPER, INK, MUTED, ACCENT, WARM, CARD = "#f7f2e8", "#1c2b30", "#5a696e", "#0e6a62", "#bf5327", "#fffdf8"

NODES = ["Ingest\nraw → wiki", "檢索 wiki", "證據卡", "大綱", "逐頁稿", "渲染 HTML", "交件"]
# 每個箭頭下方的檢查：（程式或 AI 的關卡, 人工確認）
CHECKS = [
    ("關卡 0\nlint＋AI 審查", None),
    ("關卡 1\n覆蓋率", None),
    ("關卡 2\n卡片檢查", None),
    ("關卡 3\n大綱檢查", "人工確認大綱"),
    ("關卡 4 程式檢查\n關卡 5 AI 審查", None),
    ("關卡 6\n渲染檢查", "人工驗收"),
]
X0, STEP, W, H, Y = 1.15, 2.3, 1.6, 0.95, 3.05

fig, ax = plt.subplots(figsize=(16, 4.9), dpi=200)
fig.patch.set_facecolor(PAPER)
ax.set_xlim(0, 16.1)
ax.set_ylim(0, 4.9)
ax.axis("off")


def box(cx, cy, w, h, text, face, edge, color, font, size, lw=1.6):
    ax.add_patch(FancyBboxPatch((cx - w / 2, cy - h / 2), w, h, boxstyle="round,pad=0.02,rounding_size=0.14",
                                facecolor=face, edgecolor=edge, linewidth=lw, zorder=3))
    ax.text(cx, cy, text, ha="center", va="center", color=color, fontproperties=font, fontsize=size,
            linespacing=1.35, zorder=4)


xs = [X0 + i * STEP for i in range(len(NODES))]
for i, (x, label) in enumerate(zip(xs, NODES)):
    last = i == len(NODES) - 1
    box(x, Y, W, H, label, WARM if last else ACCENT, WARM if last else ACCENT, "white", BOLD, 13.5)

for i, (gate, human) in enumerate(CHECKS):
    a, b = xs[i] + W / 2, xs[i + 1] - W / 2
    mid = (a + b) / 2
    ax.add_patch(FancyArrowPatch((a + 0.04, Y), (b - 0.04, Y), arrowstyle="-|>", mutation_scale=16,
                                 color=INK, linewidth=1.8, zorder=2))
    ax.plot([mid, mid], [Y - 0.08, 2.18], color=WARM, linewidth=1.2, linestyle=(0, (2, 2)), zorder=1)
    box(mid, 1.78, 2.0, 0.78, gate, CARD, WARM, INK, REG, 10.5, lw=1.4)
    if human:
        ax.plot([mid, mid], [1.39, 1.2], color=INK, linewidth=1.2, zorder=1)
        box(mid, 0.93, 1.7, 0.5, human, INK, INK, "white", BOLD, 10.5)

# 退回路線
ax.add_patch(FancyArrowPatch((xs[5], Y + H / 2 + 0.06), (xs[0], Y + H / 2 + 0.06), connectionstyle="arc3,rad=0.16",
                             arrowstyle="-|>", mutation_scale=16, color=WARM, linewidth=1.8,
                             linestyle=(0, (5, 3)), zorder=1))
ax.text((xs[0] + xs[5]) / 2, 4.62, "檢查不通過 → 退回出錯的那一關，只重做被點名的部分（每圈最多 2 輪）",
        ha="center", va="center", color=WARM, fontproperties=BOLD, fontsize=11.5)

# 圖例
lx, ly = 0.4, 0.28
for face, edge, label, w in [(ACCENT, ACCENT, "節點（AI 或程式產出）", 3.0), (CARD, WARM, "檢查關卡", 1.9), (INK, INK, "人工確認", 1.9)]:
    ax.add_patch(FancyBboxPatch((lx, ly - 0.1), 0.34, 0.2, boxstyle="round,pad=0.01,rounding_size=0.05",
                                facecolor=face, edgecolor=edge, linewidth=1.2))
    ax.text(lx + 0.48, ly, label, ha="left", va="center", color=MUTED, fontproperties=REG, fontsize=10)
    lx += w

out = ROOT / "workflow" / "flowchart.png"
fig.savefig(out, facecolor=PAPER, bbox_inches="tight", pad_inches=0.15)
print(f"已產生 {out.relative_to(ROOT).as_posix()}")
