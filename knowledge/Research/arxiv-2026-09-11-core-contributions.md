---
title: arXiv 2026-09-11 核心贡献总结
date: 2026-09-13
source: arxiv-2026-09-11-agent-llm.md (20 主条目 + 12 简评精选)
selected: T1 Terminal Agent RL / BenchShield Reward Integrity / MCP Registry 普查
status: 已深挖 3 篇（web_search 双源交叉验证）
data-cutoff: 2026-09-13
tags: [arxiv, research, knowledge/research]
---

# arXiv 核心贡献总结 · 2026-09-11（09-13 补跑处理）

> 来源：arxiv-fetch cron 2026-09-13 06:41 输出（09-11 新窗口速览，441 篇池零重叠），web_search 双源交叉验证后深挖 3 篇
> 精选原则：fetch 明确推荐 3 篇待深读候选（T1 / BenchShield / MCP 普查）；跨周论文级去重确认与历史 55 个已深挖 ID 零重叠 ✅；3 篇候选分散 3 个方向——**终端 agent RL 规模化 / 验证基础设施形式化 / MCP 生态幸存者偏差实证**

## 🥇 T1: Terminal Agent Reinforcement Learning for Long-Horizon Tasks (2609.11042)

**标题**: T1: Terminal Agent Reinforcement Learning for Long-Horizon Tasks
**核心**: 122B 总参 MoE（Qwen3.5-122B-A10B，active 仅 10B）纯 RL 后训练出终端 agent——在云沙箱操作真实 shell、单任务最多 300+ 工具调用轮次、用任务自己的验证器给奖励。Terminal-Bench 2.1 从 43.8%→64.0%，以少一个数量级的 active 参数超越 GPT-5.4 / DeepSeek-V4-Flash。「RL 直接训 agent 行为」有了可复现的完整配方。

### 核心贡献表

| 发现 | 数据 | 对 sora 的意义 |
|:---|:---|:---|
| **任务自带验证器 = 奖励信号** | 每个任务执行自己的 verifier，dense process reward 按通过验证器绝对数计分 | 委派任务时显式写验证器（墨题门禁/Codex 测试）就是从「评答案」走向「评行为轨迹」 |
| **激进 warm-start 稳定 actor-critic** | SFT checkpoint 49.4% 起步，3 epoch PPO → 64.0%（+28.5% 相对增益） | 「先 SFT 到能跑再上 RL」的稳定性配方，4060 小模型自举可借鉴 |
| **TITO + R3 解决 MoE RL 不稳定** | 训练-推理 log-prob 差从 0.021 降到 0.013，loss 区零 token drift | TITO 训精确采样 token id + 回合边界 drift repair；R3 重放采样器每 token 专家选择——MoE 上 RL 不崩的关键工程 |
| **完全 OOD 训练语料** | 隔离种子 + 合成任务与 Terminal-Bench 2.1 不相交 | 增益反映真实能力迁移而非 benchmark 过拟合——评测可信度设计范本 |
| **Active 10B 打平/超越 frontier** | TB2.1：T1 64.0% vs GPT-5.4 54.8% / DS-V4-Flash 56.9% / Claude Opus 4.7 66.1%（逼近） | 小 active 参数 + 强 RL 配方 = 低成本高能力路线，k 的模型选型参考 |

### 方法/架构

```
Qwen3.5-122B-A10B（base，TB2.1 43.8%）
    ↓ SFT → RST checkpoint（49.4%）
    ↓ 3 epoch PPO（质量过滤 T1-15k）
    ├─ 激进 warm-start：稳定 actor-critic
    ├─ dense 过程奖励：按通过验证器绝对数计分
    ├─ TITO：训精确采样 token id + 回合边界 drift repair
    └─ R3：记录采样器每层 MoE 专家选择并在训练时重放
    ↓
T1（122B-A10B）
    ├─ Terminal-Bench 2.1: 64.0%（超 GPT-5.4/DS-V4-Flash，逼近 Opus 4.7）
    ├─ Long-Horizon Terminal Bench: 27.9%（匹配 Gemini-3.1-Pro，超 GPT-5.4/GLM-5.1）
    └─ Terminal-Bench Hard: 38.0%（超 DeepSeek-V4-Pro）
```

| 阶段 | Terminal-Bench 2.1 | LHTB |
|:---|:---|:---|
| Base (Qwen3.5-122B-A10B) | 43.8% | 18.9% |
| SFT (RST-38k) | 49.4% | 23.6% |
| SFT + RL (Tmax-15k) | 47.2% | 20.3% |
| SFT + RL (RST-38k) | 59.9% | 25.4% |
| **T1 (3 epoch PPO)** | **64.0%** | **27.9%** |

### 与 sora 的关联

✅ **编码委派配方直接启发**：T1 的「任务验证器做奖励 + 在线任务合成」= RL 版编码 agent 路线——Codex/dsh 委派时把「验证器是否可自动执行」作为任务定义的第一要素，可让委派闭环从「人工 review」走向「自动验证奖励」
✅ **小模型自举参照**：active 10B 打平/超越大模型，佐证「小模型 + 好配方」路线；TITO/R3 的稳定性工程是 MoE RL 训练必读
✅ **评测设计范本**：完全 OOD 训练语料证明「增益≠benchmark 过拟合」——k 自建评测（墨题 AI 评分/门禁）同样要防「刷训练集」

## 🥈 BenchShield: Formal Model-Backed Instrumentation for Reward Integrity (2609.11028)

**标题**: BenchShield: Formal Model-Backed Instrumentation for Reward Integrity in LLM-Agent Evaluation Infrastructure
**核心**: LM-agent 基准 = 交互式评估基础设施，reward hacking（利用奖励相关轨迹而非解决任务）是系统性漏洞。BenchShield 用 TLA+ 形式化 reward 生命周期（7 个完整性维度），静态 phase-aware taint 分析在运行前暴露 hacking 路径，运行时用基础设施侧证据归因 agent 行为——把「防刷分」从任务级补丁升级为可复用、可证的基础设施层。

### 核心贡献表

| 发现 | 数据 | 对 sora 的意义 |
|:---|:---|:---|
| **TLA+ 生命周期模型** | 7 完整性维度：I1-I6 结构不变量（TLC 检查）+ I7 语义义务（记录不强制） | 「评估边界」可形式化定义——k 的 LLM judge/门禁可借鉴「先定义完整性维度再实现检测」 |
| **静态 taint 分析前置暴露** | 全链 recall 23-94%→77-100%，同向量覆盖 16-56%→43-78% | 运行前就能暴露 hacking 路径，比事后检测便宜一个量级 |
| **运行时证据归因** | 96% 准确率区分「暴露」vs「实际利用」（LLM 轨迹检测器仅 36%） | 「基础设施侧证据」比「看轨迹猜」可靠得多——审计要拿事实链，不要 LLM 印象 |
| **公开裁决语料** | BenchShield Trajectories：456 条人工裁决（31,000+ 运行 / 3 基准），314 条（69%）含 reward hacking | 首个带 vector chain + lifecycle position 标注的 hacking 语料，防刷分研究的公共资产 |
| **结构隔离高性价比** | 独立 verifier 环境移除 82-95% I1-I4 暴露；但 I5（fail-open）/I7（语义充分）无法靠隔离 | 「验证器独立环境」是便宜高收益缓解——k 的 Codex 测试跑独立沙箱 = 默认动作 |
| **每任务成本降 65%** | 相对 agentic hackability scanner 基线 | 形式化检查不贵，「防刷分太贵」是伪借口 |

### 方法/架构

```
评估基准包 + backend 配置
    ↓ TLA+ 有限生命周期模型（authority domains / 保护资源 / 声明交接 / 奖励来源 / 证据释放）
    ├─ 静态 lane：phase-aware taint analysis → 运行前暴露 hacking 路径（7 完整性维度检查）
    └─ 运行时 lane：基础设施侧证据归因 → Checked / VecExp / AgtViol / Inconclusive
    ↓
BenchShield Trajectories（456 人工裁决：31,000+ 公开运行 × Terminal-Bench 3 / SkillsBench / ClawsBench）
```

| 指标 | 基线 (BenchJack agentic scanner) | BenchShield |
|:---|:---|:---|
| 全链 recall | 23-94% | 77-100% |
| 同向量覆盖 | 16-56% | 43-78% |
| 运行时检测准确率 | 36%（LLM transcript-only） | **96%**（基础设施证据） |
| 每任务成本 | — | 降 65% |

### 与 sora 的关联

✅ **自建评测防刷分直接参考**：墨题 AI 评分 / LLM judge / 交付门禁——「agent 能通过非任务方式提高分数吗」应是每次设计评测的自查问题；BenchShield 的「先定义完整性维度」方法可直接套用到 k 的评测设计
✅ **验证器可靠性主线**（09-10 已起）：与 10969「验证器继承同一上游故障」、10548「测试通过仍藏漏洞」合读——验证器自身成为独立工程问题；「跨证据源 > 跨模型」的实践（独立 verifier 环境）落地便宜
✅ **同主题活跃**：BenchJack hacker-fixer loops (2606.08960)、Hack-Verifiable Terminal Bench (2608.22103) 佐证「reward hacking 防御」是 2026 活跃方向

## 🥉 MCP Registry 普查: 随机抽样揭示的生态真相 (2609.10962)

**标题**: What a Random Draw from the MCP Registry Contains, and What Tool-Use Benchmarks Contain Instead
**核心**: MCP server 生态研究一直在「悄悄选择能工作的 server」（参考集/热门榜/手工策展/修复流水线）。作者对 24,135 个 server 普查、按发布种子随机抽 400 个 npm/stdio server 逐个线上探测——**仅 48.8% 完成握手，主导失败不是缺凭据（13.3%）而是根本不启动（37.5%）**；同时对照基准语料：BFCL v4 原始 68.8%、UltraTool 85.6% 是精确重复。「注册表一半是死的、基准一半是重复的」被量化实证。

### 核心贡献表

| 发现 | 数据 | 对 sora 的意义 |
|:---|:---|:---|
| **未修复随机样本真相** | 400 抽：握手 48.8%（策展框架 66.7%，差 17.9pt）；不启动 37.5% vs 缺凭据 13.3% | 评估 MCP server 前先实测启动，热门榜/策展列表是幸存者偏差 |
| **硬符合度极高** | 195 个运行 server、2,766 工具零致命 JSON Schema 违规 | 协议符合性不是问题；**可选安全标注**才是方差（随机缺失 58.8% vs 策展 41.5%） |
| **真实工具近重复极低** | 2.8%（cosine 0.70），全部在单 server 内（list_x/get_x/create_x 家族）；跨作者 0.0% | 真实生态里「工具混淆」几乎不存在——基准的难点设定失真 |
| **BFCL v4 冗余是语料特性** | 原始精确重复 68.8%（6,002/8,726）；去重后仍 16.7% 近重复，16.4pt 跨任务 | 用 BFCL 类基准评工具调用能力，不去重就是在测「重复率」；UltraTool 0.3% 证明不是合成语料通病 |
| **可复现审计** | seed + 探测流水线 + 逐 server 结果 Zenodo DOI 公开 | 「谁都能复核」的生态审计范式——k 做工具评估报告可借鉴 |
| **生态增长速率** | 16,548 (07-14) → 24,135 (08-22)，~195 新 server/天 | 官方 registry 24,135 是「活」的，评估结论时效性强（互补数据：fetchgate.dev 25,289 servers / 15,329 远程 URL / 53.7% 应答） |

### 方法/架构

```
24,135-server registry 普查（2026-08-22 快照）
    → npm/stdio 候选框架 7,258
    → 发布种子随机抽 400（seed 20260819，frame SHA-256 pinned）
    → 逐个线上探测（无修复、单次、无重试 → 48.8% 是下界）
    ├─ 握手成功 195 (48.8%) → 2,766 工具：硬符合 100%、安全标注缺失 58.8%
    ├─ 从不启动 150 (37.5%)
    ├─ 缺凭据 53 (13.3%)
    └─ 包不可用 2 (0.5%)
    ↓ 同一方法恒定对照基准语料（全局去重 + TF-IDF cosine）
    Real MCP 2.8% / BFCL v4 16.7% / UltraTool 0.3%（近重复率）
```

| 语料 | 原始记录 | 精确重复 | 近重复 (0.70) | 跨作者/跨任务 |
|:---|:---|:---|:---|:---|
| Real MCP (195 servers) | 2,766 | 0.4% | 2.8% | 0.0% |
| BFCL v4 | 8,726 | **68.8%** | **16.7%** | 16.4pt |
| UltraTool EN | 14,084 | **85.6%** | 0.3% | 0.3% |

### 与 sora 的关联

✅ **MCP 接入基线认知**：注册表「近一半是死的」是基线事实——装第三方 MCP server 前先实测启动（npm install + initialize 握手测试），热门榜/策展列表只是「能工作的子集」
✅ **基准可信度冲击**：BFCL v4 68.8% 原始重复——k 用工具调用基准评模型能力时必须先去重，否则分数是「重复率」不是「能力」
✅ **安全联动**：与 09-10「技能供应链安全」、09-11 No-Box 描述级注入预检 (10854) 同链——「可选安全标注缺失 58.8%」说明第三方 server 的安全信息普遍缺位，装前检查清单应含「描述级注入预检 + 实测启动」双步

## 综合评估矩阵

| 维度 | T1 (11042) | BenchShield (11028) | MCP 普查 (10962) |
|:---|:---|:---|:---|
| 相关性 (Hermes 体系) | ★★★★★ 委派配方/评测设计 | ★★★★★ 自建评测防刷分 | ★★★★★ MCP 接入/基准评估 |
| 可落地性 | 配方可复现（需算力） | 方法可直接套用（便宜） | 认知基线（立即可用） |
| 证据强度 | 双源验证（arXiv/HF/alphaXiv） | 双源验证（arXiv/Cool Papers） | 双源+第三方（Neural Feed/beri.net） |
| 数据截止 | 2026-09-13 | 2026-09-13 | 2026-09-13 |
| 吸收状态 | trial（等开源/配方落地验证） | adopted（方法入评测设计） | adopted（认知基线入 MCP 检查清单） |

## 落地行动清单

- 🔴 **待办 · 委派配方升级**：Codex/dsh 委派任务定义时把「验证器是否可自动执行」列为第一要素（T1 启发：任务验证器 = 奖励信号）；跟进 T1 是否开源 checkpoint/T1-15k 数据集
- 🔴 **待办 · 评测防刷分自查**：墨题 AI 评分 / LLM judge 设计时加「是否可通过非任务方式提高分数」自查问题（BenchShield 启发：先定义完整性维度再实现检测）；门禁验证从「换模型」升级到「换证据源」
- 🟡 **待办 · MCP 接入基线落地**：新 MCP server 接入前先实测启动（握手测试），不用热门榜代替；用 BFCL 类基准评工具调用能力前先全局去重；第三方 server 装前补「描述级注入预检」
- 🟢 **待办 · 延伸阅读**：BenchJack (2606.08960 hacker-fixer loops) / Hack-Verifiable Terminal Bench (2608.22103) / fetchgate.dev MCP registry audit（25,289 servers 全量审计互补）

## 延伸阅读

- [T1 arXiv](https://arxiv.org/abs/2609.11042) · [BenchShield arXiv](https://arxiv.org/abs/2609.11028) · [MCP 普查 arXiv](https://arxiv.org/abs/2609.10962)
- [BenchJack: Hardening Agent Benchmarks with Adversarial Hacker-Fixer Loops](https://arxiv.org/abs/2606.08960) — 验证器攻防循环
- [Hack-Verifiable Terminal Bench](https://arxiv.org/abs/2608.22103) — HVE 方法论适配 Terminal Bench
- [fetchgate.dev MCP registry audit](https://fetchgate.dev/blog/mcp-registry-audit-2026) — 全量远程 server 审计（互补视角）

---

## MANTA 试点记录（2026-09-13）

| 项 | 值 |
|:---|:---|
| 是否触发拓扑变更 | **否** |
| 触发的变更类型 | 无变更（保持固定流程） |
| 监控点1（候选池）判定 | fetch 明确推荐 3 篇候选分散 3 方向（执行推理 RL / 验证基础设施形式化 / MCP 生态实证）→ 判定**分散** → 保持常规 3 篇精选，未触发合并调研 |
| 监控点2（草稿）判定 | 3 篇选文均双源验证通过（arXiv abs/html 全文 + HuggingFace/alphaXiv/Cool Papers/The Neural Feed/beri.net 独立第三方）→ 证据**充分** → 保持固定验证路径，未触发独立验证者 |
| 子代理预算使用 | 0/3（全部主进程完成，无 delegate_task） |

**质量/成本观察**：
- 本次 fetch 输出自带「验证表 + 待深读清单」（fetch 阶段已完成粗选与双源验证），summarize 仅需 3 次 web_search 轻量复核关键数字（全命中、零修正）→ 选文决策成本 ≈ 0，验证成本 ~3 次搜索，固定拓扑下总成本与历史持平
- 09-06 观察点的「跨簇牺牲单簇深挖」信号继续成立：BenchShield 所在「验证基础设施」簇还有 10969/10548 强相关，本次用延伸阅读 + 落地行动清单兜底（未触发合并调研，符合「牺牲簇 ≤1 且用延伸阅读补偿」的判定线）
- 新观察：**fetch 推荐清单质量是 summarize 成本的决定变量**——fetch 输出含「🟢 待深读」标记时（本次 T1/BenchShield/MCP 三篇直接点名），summarize 无需重扫全池，直接消费清单即可；09-06 已记录该信号，本次再次验证。后续可考虑把「fetch 推荐清单」升级为 fetch→summarize 的正式接口字段

*本总结由 arxiv-summarize cron 自动生成（2026-09-13），选文/数字基于速览 + web_search 双源交叉验证。*
