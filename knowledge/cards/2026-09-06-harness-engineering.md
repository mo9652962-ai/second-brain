---
aliases:
  - 2026-09-06-card-harness-engineering
tags:
  - knowledge-card
  - ai-agent
  - harness
  - research
created: 2026-09-06
source: "[[knowledge/Research/arxiv-2026-09-06-core-contributions]]"
status: fresh
---

# 🃏 知识卡片 · 400 万行源码解剖 11 个编码 Agent：SKILL.md 已成主流、零框架零向量检索是实证方向

> **来源**：arXiv 2609.00006《Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents》（2026-07-15 提交，2026-09-06 入库深挖）· ✅ 官方 arXiv 原文核对
> **一句话**：对 11 个生产编码 harness（含 Hermes/OpenClaw/OpenCode）做源码级解剖——**没有任何一个导入通用 agentic 框架，也没有一个用向量检索代码**，全靠手写 async loop + 确定性检索；扩展标准上 **SKILL.md 采用率 9/11 领先 MCP 8/11**。

---

## 核心洞察 / 影响

| 维度 | 内容 |
|------|------|
| 平台转折 | 2026 上半年「agent = model + harness」从口号变平台事实：ACP 进 6 系统 + 新增 harness hosting 角色（OpenHands 把各家 CLI 当可互换后端） |
| 实证规模 | 11 生产 harness（Claude Code/Codex CLI/Gemini CLI/Mistral Vibe/OpenHands/Aider/Mini-SWE-Agent/**Hermes/Pi/OpenCode/OpenClaw**）+ Omnigent meta-harness 对照，约 400 万行 Python/TS/Rust |
| 解剖框架 | 7 个规范子系统（loop/工具/上下文/安全/编排/扩展面…）× 每系统最小+最大实现；审计出 13 条横切观察 + 29 个重复设计模式 |
| 两大空白 | 三倍语料扩张后仍成立：①无 agent runtime 导入 LangChain/AutoGen 等通用框架 ②无 embedding 检索代码——**确定性检索（ripgrep/tree-sitter/glob/自动发现的 md 上下文文件）是行业主流** |
| 扩展标准 | **SKILL.md 技能文件 9/11 > MCP 8/11**（首个被点名正例的机制：Markdown 技能注入 system prompt） |
| 90 天纵向 | 4→7 月快照同系统源码 diff：收敛变成模仿（hook 词汇逐字复制）、行为策略从 prompt 散文迁移到配置 |
| 产出 | 18 条设计建议 + 90 行 minimum-viable-harness 脚手架（实现其中 10 条） |

## 对 sora 的影响

1. ✅ **k 的技能体系路线被 400 万行级实证背书**：SKILL.md 9/11 领先 MCP 8/11——portable markdown 技能注入 system prompt 是行业主流方向，不是个人偏好
2. ✅ **确定性检索路线被证实**：行业没有一家用向量检索代码——k 的 AGENTS.md / 技能文件 / 确定性检索优于向量检索的取向与实证一致
3. ⚠️ **Hermes 被独立点名**：论文列 Hermes 为增长最快的开源 harness + self-improving skill loop——生产资产的独立外部背书，可直接进产品/内容文案
4. 💡 **「策略进配置不进 prompt」**：行为策略从 prompt 散文迁移到配置是 90 天纵向实证趋势，对应 hermes-harness-profile 的配置化治理思路
5. 💡 **29 个设计模式 = 自查清单**：可对照「k 的运行时用了哪些、缺哪些」（verify-on-stop 守卫、log-as-queue、语法感知命令权限等）

## 行动项

- [ ] 通读论文 HTML 版（arxiv.org/html/2609.00006v1）29 个设计模式 → 对照自身 harness 配置做「用了/缺了」自查，缺口记入 projects/current.md
- [ ] 把「SKILL.md 领先 MCP + 零框架零向量检索」写成 1 条抖音脚本/图文素材（sora 做实事「实战派 AI 自动化」定位高度契合）
- [ ] 跟进 ACP + harness hosting 角色 → 与 EasyCLIProxyAPI 多 agent 接入路线对照，评估 OpenHands 式「CLI 当可互换后端」能否简化现有委派链

## 为什么重要

- **时效性**：2026-09-06 当天 arXiv 核心贡献深挖入库（2609.xxxxx 全新池，与历史 2607/2608 零重叠；web_search 双源交叉 + 官方 arXiv 页核对 9/11 vs 8/11、400 万行等数字）
- **强化自身**：这是「k 运行所在平台」的源码解剖——Hermes 是被研究对象之一；方法论可迁移为 harness 设计/审查框架
- **可行动**：29 模式自查 + 抖音内容素材 + 委派链对照，三个明确落点

---

*卡片来源：当天知识库精选 · [[knowledge/Research/arxiv-2026-09-06-core-contributions|arXiv 核心贡献 09-06]]（🥇 直接解剖 k 的运行时本体 + SKILL.md>MCP 实证背书技能体系 + 零向量检索验证确定性路线，外部硬证据 + 三个可执行落点）*

**亚军候选**：graphify-weekly 09-06（1925 节点/3487 边/140 社区，3 周 773 新文件图谱更新）——运维型基础设施报告，价值高但非当日新知识、可行动性低于本篇。
