---
tags: [ppt, design, 2026-trends]
domain: ppt-design
cross-domain: [ai-agent, academic, vibe-coding, workflow]
related: ["knowledge/AI-Agent", "knowledge/AI-Workflow", "knowledge/Academic", "knowledge/Vibe-Coding"]
created: 2026-07-21
updated: 2026-07-21
---

# PPT 设计知识库

> 已关联 Hermes Skill: `ppt-design-2026` (v1.0，12 章覆盖全流程)

```dataview
TABLE domain, tags, updated
FROM #ai-agent OR #workflow OR #ppt OR #academic OR #coding
WHERE file.name != this.file.name
SORT updated DESC
LIMIT 8
```

---

## 2026 最新趋势（2026-07-23 全网搜索更新）

来源：Microsoft PPT Blog、iSlide、ChatSlide、掘金、LumiChats、Storyflow

### 六大趋势（2026 升级版）

| # | 趋势 | 变化说明 |
|---|------|---------|
| 1 | **极致精准** | 不是"少即是多"，而是"精准即力量"。有意留白，每页一个核心观点 |
| 2 | **暖色极简 + 多元疯狂** | 暖色调+柔和形状 vs 高饱和色彩+夸张字体+拼贴混搭（两种并行流派） |
| 3 | **Async-First** | 大多数 deck 通过邮件/链接异步分享，无演讲者 → 每页必须独立可读 |
| 4 | **移动端优先** | 手机审阅普及 → 正文 ≥18pt，避免多列，高对比度配色 |
| 5 | **数据叙事化** | 图表从"展示数据"升级为"讲述故事"。一页一洞察，标注含义 |
| 6 | **AI 贯穿全流程** | 从大纲→设计建议→图片生成→多端适配，AI 深度嵌入 |

### 工具排行更新

依据 2026 年多家中英文评测综合排名：

```
🥇 Gamma      — prompt→deck <60s，最快出稿
🥇 Storyflow  — 故事先行，建框架再做 deck（2026 新星）
🥈 Copilot    — 原生 PPTX，格式完美
🥈 iSlide     — 中国市场首选，AI 排版升级
🥉 Canva      — 最强免费，设计资产库
🥉 Beautiful.ai — 自动布局一致性
```

### 关键发现

- **Gamma + python-pptx 互补**：Gamma 快速出稿 → python-pptx 精修格式 → 最佳工作流
- **数据叙事三大层次**：展示数据 → 说明含义 → 讲述故事
- **2026 中文学术 PPT 特有要求**：关键术语中英双语、GB/T 7714 引用、致谢不可忽视

---

## 🔗 知识关联

- **[[AI-Agent]]** — 由 k 的 6 个 PPT skills 全家桶驱动
- **[[Academic]]** — 学术 PPT 的学科规范与方法论
- **[[Vibe-Coding]]** — python-pptx 环境与图片下载策略
- **[[projects/current]]** — 变现落地进度
- **[[HOME]]** — 返回知识中枢
