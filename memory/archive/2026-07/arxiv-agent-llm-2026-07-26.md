---
date: 2026-07-26
tags: [arxiv, AI-Agent, LLM, weekly-digest]
source: arXiv API (cs.AI, cs.CL, cs.LG)
---

# arXiv AI Agent / LLM 论文周报 — 2026-07-26

检索日期: 2026-07-26 | 覆盖: 2026-07-20 ~ 2026-07-23

---

## 精选 Highlight

### 1. NVIDIA-labs OO Agents (NOOA)
[2607.20709](https://arxiv.org/abs/2607.20709) | cs.AI, cs.CL
Paul Furgale et al. — Agent = Python 对象，方法 = tool。用原生 OOP 替代传统 prompt + tool schema + callback 分离式开发。

### 2. PATS: Policy-Aware Training Scaffolding for Agentic RL
[2607.21419](https://arxiv.org/abs/2607.21419) | cs.AI
Yipeng Shi et al. — 针对长程 LLM agent RL 中弱策略重复失败问题，通过 scaffolding 引导探索。

### 3. GRADRAG: Cross-Component Prompt Adaptation for Multi-Agent RAG
[2607.21324](https://arxiv.org/abs/2607.21324) | cs.CL, cs.AI
Paolo Pedinotti, Enrico Santus — 多 agent RAG 的跨组件 prompt 协同优化。

### 4. Euclid-MCP: MCP Server for Prolog Reasoning
[2607.21412](https://arxiv.org/abs/2607.21412) | cs.AI, cs.CL, cs.SE
Bartolomeo Bogliolo — 基于 MCP 的 Prolog 逻辑推理服务器。

### 5. PRO-LONG: Programmatic Memory for Long-Horizon Reasoning
[2607.20064](https://arxiv.org/abs/2607.20064) | cs.AI
Alexis Fox et al. — 程序化记忆机制，ARC-AGI-3 持续学习基准显著提升。

### 6. AttriMem: Attribution-Guided Memory Learning
[2607.21106](https://arxiv.org/abs/2607.21106) | cs.AI
Qinfeng Li et al. — 归因分析驱动的 agent 记忆构建策略学习。

### 7. Dark Room in the Reward Channel — GRPO Trained LLM Agents
[2607.21273](https://arxiv.org/abs/2607.21273) | cs.LG
Yu Wang — **重要发现**：GRPO 框架下密集每步奖励不仅无效而且破坏策略。

### 8. AgentDebugX: Open-Source Agent Failure Debugging
[2607.18754](https://arxiv.org/abs/2607.18754) | cs.AI, cs.CL
Kunlun Zhu et al. — 解决错误根源定位问题，支持根因诊断到恢复全链路。

### 9. Is Deep Research Reliable?
[2607.20891](https://arxiv.org/abs/2607.20891) | cs.AI
Pengyu Zhu et al. — Deep Research agent 的误导性知识可靠性问题。

### 10. Agents in the Wild: Research Meets Deployment
[2607.19336](https://arxiv.org/abs/2607.19336) | cs.AI, cs.CL
Grace Hui Yang et al. — LLM agentic system 从研究到生产部署综述。

---

## Agent 框架与方法

| ID | 标题 | 关键词 | 日期 |
|----|------|--------|------|
| [2607.20709](https://arxiv.org/abs/2607.20709) | NVIDIA-labs OO Agents | Python OOP agent | 07-22 |
| [2607.21419](https://arxiv.org/abs/2607.21419) | PATS | Agentic RL scaffolding | 07-23 |
| [2607.21412](https://arxiv.org/abs/2607.21412) | Euclid-MCP | MCP + Prolog | 07-23 |
| [2607.21324](https://arxiv.org/abs/2607.21324) | GRADRAG | Multi-agent RAG | 07-23 |
| [2607.20064](https://arxiv.org/abs/2607.20064) | PRO-LONG | Programmatic memory | 07-22 |
| [2607.21106](https://arxiv.org/abs/2607.21106) | AttriMem | Memory learning | 07-23 |
| [2607.20734](https://arxiv.org/abs/2607.20734) | LLMs Get Lost in Evolving Intent | Intent tracking | 07-22 |
| [2607.20268](https://arxiv.org/abs/2607.20268) | PoTRE | Test-time reasoning | 07-22 |
| [2607.19592](https://arxiv.org/abs/2607.19592) | Knowledge-Centric Self-Improvement | Knowledge vs agent-centric | 07-21 |
| [2607.18806](https://arxiv.org/abs/2607.18806) | AI Tour Meeting | Multi-agent planning | 07-21 |

## Agent 评估与安全

| ID | 标题 | 关键词 | 日期 |
|----|------|--------|------|
| [2607.20926](https://arxiv.org/abs/2607.20926) | SciExplore | Scientific agent eval | 07-23 |
| [2607.20891](https://arxiv.org/abs/2607.20891) | Is Deep Research Reliable? | Reliability | 07-23 |
| [2607.20827](https://arxiv.org/abs/2607.20827) | Auditing Provenance Sensitivity | Provenance audit | 07-23 |
| [2607.20759](https://arxiv.org/abs/2607.20759) | IssueTrojanBench | Trojan coding agents | 07-22 |
| [2607.20255](https://arxiv.org/abs/2607.20255) | Ethics of Offensive Security Agents | Agent ethics | 07-22 |
| [2607.20216](https://arxiv.org/abs/2607.20216) | SLM Orchestration for Malware | Small model ensemble | 07-22 |
| [2607.20121](https://arxiv.org/abs/2607.20121) | OpenSkillRisk | Third-party skills safety | 07-22 |
| [2607.19595](https://arxiv.org/abs/2607.19595) | Twin Agent | Context compression security | 07-21 |
| [2607.18366](https://arxiv.org/abs/2607.18366) | Operational Hallucination and Safety Drift | Safety degradation | 07-20 |
| [2607.19865](https://arxiv.org/abs/2607.19865) | DocOps | Document ops benchmark | 07-22 |

## Agent 应用

| ID                                             | 标题                               | 领域                 | 日期    |
| ---------------------------------------------- | -------------------------------- | ------------------ | ----- |
| [2607.21482](https://arxiv.org/abs/2607.21482) | Agentic Coding Without the Cloud | Local coding agent | 07-23 |
| [2607.21019](https://arxiv.org/abs/2607.21019) | HiMe: Health Agent Platform      | Healthcare         | 07-23 |
| [2607.21268](https://arxiv.org/abs/2607.21268) | pAI-Econ-claude                  | Economics          | 07-23 |
| [2607.20630](https://arxiv.org/abs/2607.20630) | GenDB: LLM for Query Processing  | Database           | 07-22 |
| [2607.18772](https://arxiv.org/abs/2607.18772) | RF-Agent                         | Circuit design     | 07-21 |
| [2607.19794](https://arxiv.org/abs/2607.19794) | TriAgent                         | Finance            | 07-22 |
| [2607.20582](https://arxiv.org/abs/2607.20582) | Bayesian Medical AI Agents       | Medical            | 07-22 |
| [2607.18566](https://arxiv.org/abs/2607.18566) | The Story Shapes the Agent       | Narrative priors   | 07-20 |
|                                                |                                  |                    |       |

## LLM 训练与推理

| ID                                             | 标题                              | 关键词                 | 日期    |
| ---------------------------------------------- | ------------------------------- | ------------------- | ----- |
| [2607.21273](https://arxiv.org/abs/2607.21273) | Dark Room in Reward Channel     | GRPO pitfalls       | 07-23 |
| [2607.20908](https://arxiv.org/abs/2607.20908) | Multi-turn RL for CUDA Kernel   | RLVR code gen       | 07-23 |
| [2607.21518](https://arxiv.org/abs/2607.21518) | Same Objective, Opposite Advice | Safety alignment    | 07-23 |
| [2607.20773](https://arxiv.org/abs/2607.20773) | HARP: Human-AI Research         | Research platform   | 07-22 |
| [2607.20690](https://arxiv.org/abs/2607.20690) | UI Principle via RL             | Code quality        | 07-22 |
| [2607.18213](https://arxiv.org/abs/2607.18213) | SWE-Pruner Pro                  | Context pruning     | 07-20 |
| [2607.18754](https://arxiv.org/abs/2607.18754) | AgentDebugX                     | Debug toolkit       | 07-21 |
| [2607.19899](https://arxiv.org/abs/2607.19899) | Harnessing Disagreement         | Agreement blindness | 07-22 |
|                                                |                                 |                     |       |

---

## 趋势观察

1. **MCP 生态扩展** — Euclid-MCP 将 MCP 扩展到符号推理领域
2. **Agent 记忆机制成热点** — 三篇同时出现：AttriMem, PRO-LONG, Twin Agent
3. **Agent RL 奖励设计** — "Dark Room" 揭示 GRPO 关键陷阱，PATS 提出 scaffolding
4. **Agent 安全从理论走向审计** — OpenSkillRisk, IssueTrojanBench, Auditing Provenance 等 benchmark 集中涌现
5. **NOOA 框架** — OOP 范式替代传统 prompt 工程
6. **轻量级 Agent** — 多篇探索小模型编排替代单一大型 LLM

---

*自动采集于 arXiv API · 分类: cs.AI, cs.CL, cs.LG · 共 ~39 篇相关论文*

## 精选论文深度解读

📝 [[memory/2026/07/arxiv-paper-deepdive-2026-07-26|论文深度解读 2026-07-26]] — NOOA / Dark Room in GRPO / AgentDebugX
|
## k 的学习笔记 (2026-07-26)

### 🧠 可直接应用的洞察

**1. NOOA — OOP Agent 范式**
Agent = Python 对象。跟我现在用 Skill 的方式异曲同工——把能力封装成可复用模块。
→ 后续 Skill 开发可参考 OOP 思维：每个 Skill 是一个对象，tools 是它的方法。

**2. Euclid-MCP — MCP + 符号推理**
MCP 协议不止连 API，还能连 Prolog 逻辑引擎。
→ 我们已经有 4 个 MCP 服务器了，证明 MCP 生态是对的路线。

**3. Dark Room in GRPO — 奖励陷阱**
密集每步奖励破坏策略。跟之前讨论的"提示词越精细越好"相反——过度约束反而有害。
→ 写 prompt 时留空间，别把每一步都框死。

**4. RF-Agent — 电路设计 AI [2607.18772]**
AI 辅助电路设计的 agent。跟 jlcmcp 方向一致！
→ 我们这条路有人在做，不是孤例。

**5. OpenSkillRisk [2607.20121] — 第三方 Skill 安全**
Skill 安全审计的 benchmark。
→ 正好我们有 93 个 skill，安全是个值得关注的维度。

### 趋势总结
- MCP 生态在扩展（Euclid-MCP 是证明）
- 记忆机制是当前热点（AttriMem, PRO-LONG）
- Agent 安全和可靠性从理论走向实战审计
- 轻量/本地 Agent 是明确方向（Agentic Coding Without the Cloud）

### 实操行动建议
- [ ] 考虑把 NOOA 的 OOP 思维融入未来 Skill 设计
- [ ] 关注 MCP 新工具（Euclid 如果开源可以一试）
- [ ] 给 RF-Agent 论文标星，后续学习 AI for circuit design

---
*学习人: k | 方法: arXiv 周报精读*
