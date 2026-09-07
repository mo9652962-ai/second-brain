---
aliases:
  - 2026-09-07-card-memory-portability
tags:
  - knowledge-card
  - ai-agent
  - memory
  - research
created: 2026-09-07
source: "[[knowledge/Research/arxiv-2026-09-07-agent-llm]]"
status: fresh
---

# 🃏 知识卡片 · 模型升级后，agent 的记忆还认不认？

> **来源**：arXiv 2609.05339《Does Your Agent's Memory Survive a Model Upgrade? A Controlled Study of Memory Portability》· 2026-09-07 新窗口入库 · ✅ 官方 arXiv abs 页核对（curl 直连）
> **一句话**：模型升级是常态、记忆迁移不是——agent 可以保留同一份记忆存储却仍然「忘记」：新模型可能按不同方式解读旧笔记、混合 embedding 版本可能弄坏检索、修复时还缺原始证据。

---

## 核心洞察 / 影响

| 维度 | 内容 |
|------|------|
| 问题 | 升级模型后，同一份记忆存储 ≠ 记忆还在——agent 可能「库还在、人失忆」 |
| 三种失败模式 | ①新模型解读旧笔记的方式变了 ②混合 embedding 版本弄坏检索 ③修复检索时缺原始证据 |
| 实验设计 | 相同历史在四种表示下对照：long-context 逐字保留 / 分块 RAG / 压缩成自然语言笔记 / 固定 schema 知识图谱 |
| 核心结论 | 记忆可移植性 = 表示形式 × 检索栈的联合问题，「模型升级 ≠ 记忆无缝」 |

## 对 sora 的影响

1. ⚠️ **k 自己的运行时**：Hermes 跨会话记忆 + Obsidian 知识库 + 模型 fallback 链（fangzhou-2 → jiyuanlvdong-2）——换模型/切 fallback 前，「同库记忆在新模型下还认不认」是真实风险，不是理论问题
2. ⚠️ **墨题 RAG**：DashScope text-embedding-v4——embedding 版本升级可能弄坏检索，且「修复时缺原始证据」= 向量库必须保原文，不能只存向量丢文档
3. 💡 **表示形式取舍**：long-context 逐字保留最稳但贵；压缩笔记依赖新模型的解读方式；知识图谱最结构化但迁移成本高——知识库设计要把「换模型后的可移植性」当一等需求

## 行动项

- [ ] 换模型/升级前：对关键记忆条目做一次「新模型可读性」抽查（旧笔记是否仍被正确解读、检索是否仍命中）
- [ ] 墨题 RAG 升级 embedding 前：备份原始文档 + 记录 embedding 版本，防止混合版本弄坏检索且无法修复
- [ ] 把「记忆可移植性检查」加入模型配置评估清单（fallback 链切换时必查）

## 为什么重要

- **时效性**：09-07 索引解冻全新窗口（list 页 480 篇、covered_ids 0 重叠），当天唯一实质新知识文件
- **强化自身**：直接验证 k 正在生产使用的三样东西——Hermes memory、Obsidian 知识库、墨题 RAG——「生产资产被外部受控实验独立验证」= 独立背书
- **可行动**：升级前抽查 / RAG 备份 / 评估清单，三个明确落点

---

*卡片来源：当天知识库精选 · [[knowledge/Research/arxiv-2026-09-07-agent-llm|arXiv Agent/LLM 09-07]]（🥇 唯一实质新知识 + 直击 k 自身运行时记忆可移植性，官方源 curl 核对通过）*

**亚军候选**：2609.04869《From Interaction Traces to Persistent Skills》——「轨迹→持久技能库」在线演化，直接背书 k 的 learn→research→apply 蒸馏路线。
