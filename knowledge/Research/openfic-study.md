---
tags: [research, github, article-study, ai-writing, openfic]
created: 2026-07-31
status: absorbed
source: https://github.com/syrizelink/OpenFic
license: Apache-2.0
---

# OpenFic — 研究笔记

> 来源：小黑盒文章 · 2026-07-31 验证 + 吸收

## 项目验证

| 项 | 值 |
|----|-----|
| Stars | 1（刚开源，文章 07-28 发布时可能更低） |
| License | Apache-2.0 |
| 语言 | Python 3.12+ / React 19 / TypeScript |
| 版本 | v0.8.1（2026-07-31 刚发布，10 天迭代 5 版） |
| 安装 | Docker / pip (`openfic serve`) / 桌面版（163MB 实验性） |
| 定位 | AI 小说创作平台（SillyTavern 的写作向替代） |

## 项目分析

**作者动机**：玩了一年 SillyTavern（酒馆）→ 发现酒馆适合 RP 不适合人机协同写作 → 自己开发。Agent 功能从一键生成 → 固定工作流 → 父子节点 → Codex 式 Agent，踩了很多坑。

**核心卖点**：
1. 人机协同创作（非抽卡式一键生成）
2. Agentic RAG（百万字级语义检索）
3. 多层上下文管理（智能压缩/动态截断/稳定缓存，成本优先）
4. 本地持久化（零云存储）
5. 兼容 OpenAI API 任意模型

## 吸收价值评估

| 维度 | 评估 | 决策 |
|------|------|------|
| 产品本身 | 小说创作工具，非我们方向 | ❌ 不装（163MB 实验性） |
| **上下文压缩实现** | 生产级参数：0.8 触发/20K 尾部/2K 最小门槛 | ✅ 吸收为参考 |
| **Agentic RAG** | 百万字检索 = codebase-memory-mcp 同思路 | 🟡 已有类似工具 |
| **人机协同理念** | Agent 适应写作流程而非反之 | ✅ 与我们的体系哲学一致 |

## 落地行动

1. ✅ `knowledge/Dev/context-compaction-params-reference.md` — 上下文压缩参数参考
2. 📄 本笔记存档
3. 🟡 不装桌面版（产品定位不符 + 实验性）

## 结论

- 项目真实（Apache-2.0，10 天 5 版迭代，pip 已发布）
- **最大价值是生产级上下文压缩实现**（0.8 触发/20K 尾部预算），已吸收为参考
- 产品定位与我们无关（小说创作），但架构思想（成本优先/人机协同/本地持久化）与我们的 Second Brain 体系哲学一致

---
> 关联: [[openfic-absorbed]]（吸收补强） | [[HOME|🏠 首页]]

---
> 🗺️ 属于 [[MOC-Research|🔬 研究笔记]] · [[knowledge-map|🗺️ 知识地图]]
