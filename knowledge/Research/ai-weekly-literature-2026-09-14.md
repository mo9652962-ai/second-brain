---
title: "AI 文献周报 · 2026-09-07 ~ 2026-09-13"
type: note
domain: Research
status: active
tags: [knowledge/research]
source: null
date: 2026-09-14
---
# AI 文献周报 · 2026-09-07 ~ 2026-09-13

> 方向：AI Agent / 大模型(LLM) / 科研工具(AI for Science)
> 检索源：arXiv HTML 搜索端点 3 路查询(agent/llm/sci_tool，09-07→09-13 窗口) + arXiv 列表页 7 类目(recent)
> 覆盖度：✅ arXiv 搜索端点 HTTP 200 / ✅ arXiv 列表页 HTTP 200 实测；未覆盖：OpenAlex/Crossref(本周未跑)、CNKI/万方/维普(无免费 API)、DOAJ(403)
> 注：窗口 09-07~09-13 共 287 篇唯一命中，与既有速览 covered_ids 比对后 265 篇未覆盖；本报告精选 16 篇强相关（其中 10 篇与今日 09-14 daily 速览同池重选——本文献综述视角补核心发现/创新点/精读推荐，6 篇为速览漏网强相关）。所有标题/摘要来自 arXiv 真实响应并经 abs 页复核(搜索端点摘要偶有截断)；未臆造 DOI/被引/年份

---

## 一、本周值得关注论文（按方向）

### 🔧 AI Agent（训练进化 / 记忆 / 并行工具）

| 论文 | 核心发现 | 创新点 |
|---|---|---|
| **EvoRS** (2609.12459, 09-11) | 开放式 RL 中固定奖励系统随策略优化而退化(reward hacking/判别力下降)，奖励系统本身必须进化；EvoRS 在 writing/roleplay 上超固定奖励策略 2.107/4.767 分，消融证实全面固定奖励在开放式任务中不可靠 | 把奖励系统表示为可执行 Reward-DAG，由 agentic designer 从 on-policy rollouts 与奖励轨迹持续更新，动态适配评分机制与信号组合 |
| **GACA** (2609.12424, 09-11) | 长程 agent RL 的信用分配粒度应随状态而定：关键分支决策用 step 级信号、常规近确定性转移用 episode 级信号；ALFWorld/WebShop 上 1.5B/7B 均超 GRPO/GiGPO | critic-free 估计器按负对数似然(NLL)不确定性代理计算 per-step 权重混合两种 advantage，并给出风险分解与误差投影分析 |
| **BQ-LoRA** (2609.12896, 09-11) | 单一 LoRA 在固定 rank 预算下学多能力 agent，重复更新过度强调冗余行为变化、聚合更新超 rank 预算；在 AppWorld/BrowseComp-Plus 优于标准 LoRA | 通过行为商流形组织轨迹更新(行为商平衡 BQB + 决策保持压缩 DPC)，同时控制权重误差与决策分布失真 |
| **LifeMem** (2609.12655, 09-11) | 现有记忆 agent 跨环境迁移差且随经验累积灾难性遗忘；LifeMem 在 10 环境/13k+ 任务上实现经验复用，降低遗忘、提升跨任务迁移 | 按底层 workflow 聚类交互轨迹提取可复用技能，推理时召回技能+轨迹引导动作；任务流分析与结构相似轨迹合并消融 |
| **MAPLE** (2609.11636, 09-10) | 优化问题维护需要跨请求保留执行状态：NLDO 基准(15 轨迹/180 更新)上完成全部轨迹，在线质量 0.951、Pareto 超体积比 0.875 | LLM 语言构建+数学规划+进化搜索组合，记忆保留优化程序/已接受计划/历史更新/候选解，支撑自然语言连续修订 |
| **AIM** (2609.12320, 09-11) | 多用户 agent 系统需要私密/共享记忆分级：AIM 可见性分类 96.0%、状态感知操作准确率 70.5%；MUMBench 为首个多用户记忆 benchmark | index 级访问控制(私有仅属主可检索、公共跨用户共享)，动态分类信息；4 域多用户数据集评估检索/创建/更新/删除 |
| **ParaRecover** (2609.12345, 09-10) | 并行工具调用 agent 中间故障诊断恢复被现有基准忽视：10+ 主流 LLM 在多轮错误传播/隐式工具失败/精确重规划上仍挣扎 | 14 类错误 taxonomy(规划依赖/工具选择/参数匹配)×10,626 实例两级难度；SDE rubric 测结构完整性/诊断推理/进化策略，且可作为监督信号提升恢复能力 |

### 🧠 大模型（评测 / 推理 / 安全）

| 论文 | 核心发现 | 创新点 |
|---|---|---|
| **GAUGE** (2609.12191, 09-10) | 满意度≠任务成功：盲评小组判"满意"的对话 57.5% 实际任务失败；gate 在接近的强 agent 间失去分辨率(决策分歧从 <1% 跳到 31%) | 区分 ranking validity 与 construct validity；calibrate-then-trust 节奏 + judge-free 完成位作为截断回归零成本绊线 |
| **K-Bench** (2609.12808, 09-11) | TOFU/MUSE 的"拒答即遗忘"证书在 agent 部署下失效：秘密经工具观察通道 verbatim 泄漏；权重中的秘密 20 种已发表方法全部无法移除 | 检查 ReAct agent 的 6 个通道(CoT/工具调用/工具观察/摘要等)，K-Score 按秘密来源(权重/提示/检索库)分算且仅当 agent 保持可用才计遗忘 |
| **TAM** (2609.13005, 09-11) | 长程程序性推理是真实短板：GPT-5 等最强配置在 ICD-10-CM 编码 exact-match 仅 1%、联邦判刑 15.5%——短程 multi-hop 基准高估 LLM 推理 | 真实任务基准(数万条规则官方手册，人验证标签)，覆盖 RAG/ReAct/agent-harness 多基线；数据代码开源 |
| **SoK: Jailbreaking in Agentic AI** (2609.12413, 09-11) | 强原生对齐≠对抗鲁棒；最终响应被过滤时 planning/memory/tool 中间状态可能已被攻陷(低最终攻击成功率掩盖严重中间妥协) | 围绕 agentic 执行管线(交互/规划/记忆/工具/agent间通信)统一 attack/defense taxonomy + security-utility-efficiency 三轴评估框架 |

### 🧪 科研工具（AI4Science / 复现 / Deep Research）

| 论文 | 核心发现 | 创新点 |
|---|---|---|
| **AgentActionBench** (2609.11117, NLPCC 2026 Shared Task 11, 09-10) | 现有复现评测只看最终 repo 且限 ML；当前系统复现实验能力有限，执行是主要瓶颈；模型生成 rubric 与人工标注强相关 | 首个跨 ML+AI4Science(120+30 篇论文)的过程级复现基准，MCP-based Action Recorder 抓过程轨迹 + paper-specific rubric(1 万+ 条目) |
| **Wavering Oracles** (2609.11428, 09-10) | 多模型科研工作流可靠性可量化：选择性跨度 13.4~71.6pp(最强 Qwen3-4B 45.6、Gemma3-4B 被误导 -14.1、SmolLM3-3B 零选择性)；错误相关 0.285 把 7 模型等效独立数降到 2.58 | SycoBench-600 受控测量(17,055 轨迹)，selective updating(抗拒误导+接受正确建议)指标 + leave-one-stem-family-out 可靠性选择器(96.2%，恢复 67.7% 差距) |
| **RAG for Scientific Code** (2609.12190, 09-10) | 模型家族与检索质量 > 参数规模：9B 本地模型 0.795 分超过同管线更大模型、也超 Claude Code 架构下的同模型——科学代码理解可本地化 | 严格分离昂贵离线摄入(解析/结构图/LLM 生成实体解释/embedding)与轻量在线回答；11 类 100 题 IPPL(C++) 基准 + 独立 frontier judge 评分 |
| **X-ray 溅射 agent** (2609.12796, 09-11) | LLM agent 经 MCP 桥(17 工具三档)控制真实磁控溅射设备：反射率实测相对周期差 20%→2.26%→0.79%(阈值 3%)；识别 16 种接口失败模式 | schema 约束 + 校准只读(agent 只能写自己的工作区) + 实测验证闭环的 lab agent 实证——真实物理设备上可验证的 agent 控制 |
| **HybridDeepResearch** (2609.09410, 09-08) | 网页+SQL 混合深度研究极难：GLM-5.2/Claude-Sonnet-4.6/GPT-5 在 hard 子集 Pass@8 仅 50-54%；方向推理(跨系统保持约束)显著难于平行交叉 | 首个要求 web+SQL 完整可验证答案的 deep research 基准(380 任务，SQL2S/S2SQL/Parallel 三种推理模式，自动+人工双重验证) |

---

## 二、推荐精读（3 篇）

1. **Wavering Oracles** (2609.11428) — **本周对 sora 多源/多模型科研工作流最该读的一篇**。它把"多个模型一起用"的可靠性问题变成可测指标：选择性更新(抗拒误导+接受纠正)、错误相关性(0.285→等效独立数 2.58)、可靠性选择器(恢复 67.7% 差距)——直接映射 Hermes 的多源交叉验证/多 agent 联合研究(WorkBuddy+dsh+Gemini 盲评)，"什么时候该信哪个模型"有了量化依据。
2. **AgentActionBench / NLPCC 2026 Shared Task 11** (2609.11117) — **科研复现自动化首个过程级基准**。MCP-based Action Recorder + paper-specific rubrics 的评测设计可直接借鉴到 sora 的科研自动化 pipeline(论文服务/实验复现方向)；"执行是主要瓶颈"的结论提示：复现 agent 的短板在工具执行而非理解。
3. **ParaRecover** (2609.12345) — **并行工具调用 agent 的错误恢复教科书**。14 类错误 taxonomy + SDE rubric(结构/诊断/进化)既是被测对象也是训练信号，正对症 sora 的 Codex 委派/多 agent 排障(parallel tool-use 错误传播、级联失败)；建议与既有 SymTrace 失败归因思路对照读。
   - 备选：**GAUGE** (2609.12191) — sora 用 LLM-as-judge(Gemini 盲评)做跨源评估，GAUGE 的"满意度≠成功(57.5%)+接近 agent 间 31% 决策分歧"是对 judge 环节的直接预警。

---

## 三、本周趋势总结

1. **评测从"最终分数"下沉到"过程可信"**：ParaRecover(过程级错误恢复)、K-Bench(6 通道泄漏检测)、AgentActionBench(过程轨迹+rubric)、GAUGE(构造效度)四篇同向——"任务成功"不再是足够信号，中间过程(工具调用/推理链/行为轨迹)才是新评测对象。
2. **奖励系统从固定变自进化、信用分配变自适应**：EvoRS 让奖励系统本身成为进化对象(Reward-DAG)，GACA 让信用分配粒度随状态不确定性自适应——开放式 RL 训练的"最后一公里"开始被认真对待。
3. **记忆升级为 agent 核心基建，且进入多用户/隐私维度**：LifeMem(终身复用)、MAPLE(跨请求执行状态)、AIM(私密/共享分级+index 级访问控制)——从"记不记得住"到"跨环境迁移、跨用户安全共享"。
4. **科研 agent 从 demo 走向真实闭环与可靠性工程**：X-ray 溅射 agent(真实设备+反射率验证)、RAG-SciCode(本地化私有部署)、Wavering Oracles(选择性/错误多样性/校准裁决三目标)、HybridDeepResearch(混合证据保持约束)——"能跑通"已不是问题，"证据可信、错误可辨、可验证"才是。
5. **Agentic 安全独立成章**：SoK 把越狱防御重构到 agentic 全管线(规划/记忆/工具/agent间通信)，K-Bench 证明"模型级遗忘"证书在 agent 部署下失效(工具通道泄漏)——响应级防御不够，中间状态与工具通道都要防。
6. **长程程序性推理是当前 LLM 的真实短板**：TAM 的 1%(ICD-10-CM)/15.5%(判刑) exact-match 说明短程 multi-hop 基准显著高估推理能力；对科研/接单场景的启示：长手册、多步骤规则任务仍是 agent 化的价值洼地。

---

## 数据说明

- **检索源与 HTTP 码**：arXiv HTML 搜索端点 3 路查询(agentic AI OR LLM agent OR multi-agent / large language model / AI for science OR scientific discovery OR research automation，09-07→09-13 窗口)=200；arXiv 列表页 7 类目(cs.AI/CL/LG/MA/SE/RO/HC)=200
- **结果量**：3 路共 287 篇唯一命中(139+146+38)，与 covered_ids(607) 比对后 265 篇未覆盖；精选 16 篇入表(全部 09-10~09-11 提交，无重复收录)
- **覆盖度**：✅ arXiv(搜索端点+列表页)；未覆盖 OpenAlex/Crossref(本周未跑，arXiv 时间窗相关性检索为主)、CNKI/万方/维普(无免费 API)、DOAJ(403)；**HTML 搜索端点按相关度排序，非穷尽检索**
- **验证**：入表 16 篇全部经 abs 页复核完整摘要(搜索端点摘要偶截断)；未臆造 DOI/被引/年份；精读推荐映射 sora 现有工作流
- **原始数据**：`~\.openclaw\workspace\.temp\search_week_0914.json`、`abs_full_0914.json`(可复现证据)

---

*生成：Hermes cron · light-literature-search 方法论(多源回退) · 2026-09-14*

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
