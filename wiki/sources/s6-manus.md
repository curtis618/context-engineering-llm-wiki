# S6　Manus〈Context Engineering for AI Agents: Lessons from Building Manus〉

- 作者：Yichao 'Peak' Ji（Manus）
- 日期：2025-07-18
- 原文網址：https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus
- raw 檔案：[S6-manus.md](../../raw/S6-manus.md)
- 讀到的範圍：全文。

## 這篇在講什麼

Manus 團隊實際打造 agent 產品後整理出的六條經驗，重點在成本、速度與讓 agent 不偏離目標。作者自己也說這些不是放諸四海皆準的真理。

## 重點

- 選擇 context engineering 而不是自己訓練模型，因為改進可以在幾小時內上線，而不是幾週。
- 比喻：如果模型進步是上漲的潮水，產品要當船，不要當釘在海床上的柱子。
- 圍繞 KV-cache 設計：輸入與輸出的 token 比例約 100:1；以 Claude Sonnet 為例，有快取的輸入價格是沒快取的十分之一。
- 用遮罩代替移除：不要在任務中途增減工具。
- 把檔案系統當成上下文：容量無限、可以持久保存。
- 靠複誦控制注意力：反覆改寫 todo.md，把目標留在上下文的最後面。
- 把錯誤留在上下文裡：模型看到失敗才會修正。
- 小心被 few-shot 帶偏：模型會模仿上下文裡「動作與結果」的模式，解法是加入少量變化。

## 相關概念頁

- [實戰經驗：Manus 的六條心得](../concepts/production-lessons.md)
- [寫入](../concepts/write-context.md)
- [壓縮](../concepts/compress-context.md)
- [好的上下文長什麼樣子](../concepts/designing-good-context.md)
