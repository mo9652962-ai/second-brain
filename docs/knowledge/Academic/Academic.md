---
tags: [academic, paper, research]
domain: academic
cross-domain: [ai-agent, ppt-design, vibe-coding, workflow]
related: ["knowledge/AI-Agent", "knowledge/AI-Workflow", "knowledge/PPT-Design", "knowledge/Vibe-Coding"]
created: 2026-07-21
updated: 2026-07-23
status: adopted
---

# 学术知识库

```dataview
TABLE domain, tags, updated
FROM #ai-agent OR #workflow OR #ppt OR #academic OR #coding
WHERE file.name != this.file.name
SORT updated DESC
LIMIT 8
```

---

> 本知识库同时兼容 **OpenClaw** 与 **Hermes Agent** 环境。以下 9 个论文 skills 通过 ClawHub 安装，在两个平台中均可正常使用。

## 论文 Skills 全家桶

| 阶段 | Skill | 用途 |
|------|-------|------|
| 检索 | cnki-scholar | 知网/万方/维普 |
| 检索 | cnki-advanced-search | 知网高级检索自动化 |
| 检索 | journal-sci-ssci-checker | SCI/SSCI 索引检查 |
| 阅读 | paper-parse | 双模式深度研读 |
| 阅读 | paper-summarize-academic | 结构化摘要 |
| 写作 | chinese-academic-writing | 中文学术写作（去AI化） |
| 写作 | sci-paper-three-pass | SCI 三轮精修 |
| 写作 | paper-writing-workflow | 标准论文写作流程 |

## 中文学术去 AI 化要点

- AI 痕迹特征识别
- 学术习语库
- 句式多样性注入
- 论证非线性重构
- 策略性不完美

## 变现方向

- 论文翻译润色（200-800 元/篇）
- 文献检索报告（100-200 元/次）
- SCI/SSCI 期刊推荐（50-100 元/次）
- 论文答辩 PPT（200-400 元/套）→ 详见 [[PPT-Design#学术 PPT 规范]]

---

## 🔗 知识关联

- **[[AI-Agent]]** — 由 9 个论文 skills 全家桶驱动（ClawHub 安装，Hermes / OpenClaw 双平台兼容）
- **[[PPT-Design]]** — 论文答辩 PPT 制作与学术汇报设计
- **[[Vibe-Coding]]** — 文献管理工具与写作环境
- **[[projects/current]]** — 学术服务变现进度
- **[[HOME]]** — 返回知识中枢
---
> 关联: [[PPT-Design]] · [[AI-Workflow]] · [[Cross-Domain|🔀 知识地图]] | [[HOME|🏠 首页]]
