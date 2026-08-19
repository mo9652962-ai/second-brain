---
aliases:
  - 2026-08-19-card-bounded-agents-delegation-security
tags:
  - knowledge-card
  - ai-agent
  - security
  - multi-agent
  - authorization
  - MCP
created: 2026-08-19
source: "[[knowledge/Research/arxiv-2026-08-19-agent-llm]]"
status: fresh
---

# 🃏 知识卡片 · Agent 安全=授权架构：防注入靠「最小授权 + 模型外强制」

> **来源**：arXiv 2608.15888v1 *Bounded Agents: Delegation Security for Multi-Agent AI Systems*（Xabier Muruaga，08-16 提交池）· 2026-08-19 入库 · ✅ web_extract arXiv 原文摘要核实
> **一句话**：prompt 注入只有 agent **有权做**时才构成风险——把授权沿委派链「只收窄、不放宽」并放到模型外强制（APC），AgentDojo 四域泄密 75-100%→**0%**，授权延迟 P99 仅 **0.24ms**。

---

## 核心洞察

| 维度 | 内容 |
|------|------|
| 核心论点 | 注入攻击后果 = 授权架构问题，不是模型抗性问题——agent 无权做的事再怎么注入也做不了 |
| APC 机制 | Agentic Principal Chain：沿 principal→sub-agent 委派链追踪会话级授权状态，六个授权检查 + composition closure（跨会话约束非法动作组合），在模型外强制执行 |
| 效果数据 | AgentDojo 泄密 75-100%→0%（四域全降）；阻断 InjecAgent 盗数 544 例全中；intent binding：破坏 38.6%→4.0%、操纵 90.5%→12.1%；延迟 P99 0.24ms（3,154 实例实测） |
| 代价 | 949 对任务-注入组合下 utility 降 8.6/13.9 个百分点（安全性有少量可用性代价） |
| 开源 | 代码与数据公开：github.com/xmuruaga/bounded-agents |

## 对 sora 的影响

1. ✅ **现有实践已被学术背书**：Hermes 外部动作谨慎审批、dsh 禁 auto-mode、闲鱼交付前先问——「最小授权 + 模型外审批」正是 APC 的工程化雏形，方向正确
2. ⚠️ **MCP 工具面是最大暴露面**：本机挂了几十个 MCP 工具（filesystem/github/jlcmcp/…），每个工具就是一张「授权信封」——值得做一次最小授权盘点：禁用不常用的、按项目分组
3. 💡 **委派链只收窄不放宽**：给子 agent/外部编码工具派活时，任务描述就是授权边界——不把「可做范围」写太宽（呼应 ZCode 超范围改代码教训）
4. 💡 **硬数字可作内容素材**：「3,154 实例、泄密清零、延迟 0.24ms」——AI 博主选题（「为什么你的 AI 助手会被一句话骗走数据」）

## 行动项

- [x] arxiv 速览已入库（`knowledge/Research/arxiv-2026-08-19-agent-llm.md` 补录 14 篇强相关）
- [ ] 本周做一次 MCP 工具最小授权盘点：`hermes tools` 列出全部工具，禁用不常用/高风险的（预计 10 分钟）
- [ ] 后续派活/委派时把「授权边界」写进任务 prompt（一条原则：能做的最小集合）

## 为什么重要

- **三条独立佐证=领域共识**：同日池里 *Policy Algebra*（可靠能力=路径性质）与 *Embodied Agent 安全*（trust-boundary 视角）同主题交叉验证——「防注入靠最小授权 + 模型外强制」不是单篇论文的孤证
- **MCP/A2A 时代的委派安全基座**：工具即权限，sora 的工具链就是授权面，直接相关
- **可行动性强**：不只是一个认知，能当场落到 MCP 盘点这类具体动作

---

*卡片来源：当天知识库精选 · [[knowledge/Research/arxiv-2026-08-19-agent-llm]]（🥇 Bounded Agents——授权架构共识三线交叉 + 硬数据清零验证 + 直接落地 MCP 盘点；🥈 Zetta 三环自进化——harness 成进化对象，与 Hermes skill 沉淀同构）*
