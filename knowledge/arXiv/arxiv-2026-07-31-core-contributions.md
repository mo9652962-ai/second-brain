---
aliases:
  - arxiv-2026-07-31-core
  - openforgerl-stateact-osreward
tags:
  - arxiv
  - research
  - ai-agent
  - llm
  - harness-training
  - computer-use
  - state-grounding
  - reward-model
created: 2026-07-31
updated: 2026-07-31
status: adopted
source: arxiv-weekly-2026-07-31
---

# arXiv 核心贡献精选 — 2026-07-31

**精选原则**：基于 arxiv 周报（Week 32，20 篇论文）+ 搜索引擎交叉验证 → 筛选与 **Hermes/Agent 体系** 强相关的 3 篇核心论文

本周主题：**Computer-Use Agent 基建 + Agent Harness 工程化**（2026-07-30 投稿爆发）

---

## 🥇 1. OpenForgeRL: Train Harness-native Agents in Any Environment

| 元数据 |  |
|:-------|:--|
| **ID** | [`2607.21557v2`](https://arxiv.org/abs/2607.21557v2) |
| **日期** | 2026-07-23 (v2) |
| **分类** | cs.AI, cs.CL |
| **作者** | Xiao Yu, Baolin Peng, Ruize Xu 等（Columbia / Dartmouth / MSR） |
| **状态** | ICLR 2027 投稿，✅ 已验证（社区有解读） |

### 核心贡献

> 一句话概括：用「轻量 proxy + K8s 编排」把现代 agent harness（Claude Code / Codex / **OpenClaw**）变成可端到端 RL 训练的环境，解决「训练-部署错配」。

现代 agent 依赖复杂的 inference harness 完成多轮推理、工具调用、外部系统访问；但开源 SFT/RL 栈无法原生表达 stateful、多进程的 harness 推理 —— 这就是 **train-deploy mismatch**：你在干净环境里训练的模型，和实际跑在 harness 里的模型是两套东西。

| 问题 | 传统做法的局限 | OpenForgeRL 的解法 |
|------|--------------|-------------------|
| **训练-部署错配** | 开源 RL 栈表达不了 harness 的状态化推理 | 在 harness 和 RL codebase 之间插一层 proxy，解耦训练与推理 |
| **训练数据难获取** | 需要人工构造干净环境 | proxy 直接把模型调用记录为训练数据 |
| **环境难扩展** | 单机跑 rollout 慢、状态易串 | K8s orchestrator 每个 rollout 独立远程容器，任意环境任意规模 |

### 关键技术机制

```
Agent Harness (OpenClaw/Codex/Claude Code)
        │  模型调用
        ▼
┌─────────────────────────┐
│   Lightweight Proxy     │ ← 伪装模型 API，同时记录轨迹为训练数据
└─────────────────────────┘
        │
        ├──→ 标准 RL codebase (veRL)  ← SFT/RL 训练
        │
        └──→ Kubernetes Orchestrator  ← 每个 rollout 独立容器
```

| 组件 | 职责 |
|:-----|:------|
| **轻量 proxy** | 拦截 harness 的模型调用、记录为训练数据，让任意 harness 接入标准 RL 栈 |
| **K8s orchestrator** | 每个 rollout 在独立远程容器运行，支持有状态、多进程环境规模化 |
| **RL codebase (veRL)** | 直接用成熟 RL 框架训练，无需为 harness 重写训练栈 |

### 关键结果

| 模型 | 基准 | 成绩 |
|:-----|:-----|:-----|
| OpenForgeClaw | ClawEval | 31.7 pass^3 / 55.9 pass@3 |
| OpenForgeClaw | QwenClawBench | 33.7 |
| OpenForgeGUI | OSWorld-Verified | 37.7 |
| OpenForgeGUI | Online-Mind2Web | 63.0 |
| OpenForgeGUI | WebVoyager | 72.3 |

- 只需 **几百到几千个任务** 就能训练出可用 agent（数据效率高）
- RL 提升可靠性：自验证、工具覆盖、多步规划；**错误恢复仍是短板**（诚实结论）

### 与 sora 的关联 🔗

这是本周对 Hermes 体系**最直接相关**的论文 —— 论文摘要里点名的 harness 就包括 OpenClaw，而 Hermes 正是 OpenClaw 系：

1. **轨迹记录层** — proxy 拦截模式可直接借鉴：为 Hermes 的模型调用链加一层「记录层」，累积真实使用轨迹，为未来训练自有模型备数据
2. **训练自有模型的路径** — 首次给出「用 OpenClaw 生态数据 + 标准 RL 栈」训练的开源方案，而非黑盒蒸馏
3. **错误恢复是短板** — 与我们自建系统的教训一致：agent 可靠性短板在 recovery，不在执行

**可借鉴到：** `hermes-automation-patterns` 的可靠性模式 + 未来自训模型的数据管线设计

---

## 🥈 2. StateAct: Program State, before Pixels, for Long-Horizon Computer-Use Agents

| 元数据 |  |
|:-------|:--|
| **ID** | [`2607.22798v1`](https://arxiv.org/abs/2607.22798v1) |
| **日期** | 2026-07-24 |
| **分类** | cs.SE, cs.CV |
| **作者** | Yan Yang, Xiangru Jian, Ziyang Luo 等（Salesforce AI Research） |
| **状态** | ✅ 已验证（HuggingFace Daily Papers 收录） |

### 核心贡献

> 一句话概括：**程序状态优先于像素** —— 主 agent 直接用代码操作底层状态（文件/DOM/后端），GUI 子 agent 只处理少数真正需要视觉的子目标。

主流 CUA 都在「加强感知」：更准的截图理解、更稳的点击定位。但截图只是程序状态的 **lossy 渲染**：不同状态可以产生相同像素，而代码可以直接读取和修改状态本身。StateAct 反其道而行 —— 让 agent 少看屏幕。

| 问题 | 截图驱动 agent 的缺陷 | StateAct 的改进 |
|------|---------------------|----------------|
| **信息丢失** | 像素是状态的压缩投影，关键信息在 DOM/文件/后端里 | 主 agent 行动空间 = 代码 + 结构化操作（bash、文件编辑、plan checklist） |
| **感知瓶颈** | 所有任务都走截图-点击，昂贵且易错 | GUI 子 agent 只在需要视觉时介入（28/108 任务、仅 1.1% 步骤） |
| **验证缺失** | 无法确认最终产物是否真的对了 | 独立 finish gate 双重检查保存结果的结构性失败 |

### 关键技术机制

```
主 Agent（code-first）
  ├── persistent bash        ← 直接操作状态
  ├── file editor            ← 直接读写文件
  ├── view_image             ← 只读查看图片
  ├── plan checklist         ← 计划跟踪
  ├── finish action          ← 收尾
  └── agent delegation       ← 委派给 GUI 子 agent（仅视觉子目标）
        │
        ▼
   GUI Subagent（截图+点击）    ← 28/108 任务，1.1% 步骤
        │
        ▼
   Finish Gate（独立验证）     ← 结构性失败检查
```

| 组件 | 职责 |
|:-----|:------|
| **主 agent（代码优先）** | 用代码直接读写程序状态，行动空间不暴露鼠标/键盘 |
| **GUI 子 agent** | 处理少数真正需要视觉交互的子目标 |
| **finish gate** | 独立于执行路径，验证最终产物是否有结构性失败 |

### 关键结果

| 指标 | 截图驱动 | StateAct | 变化 |
|:-----|:--------:|:--------:|:-----|
| OSWorld 2.0 二进制成功 | 20.6% | 26.9% | **+6.3pp** |
| OSWorld 2.0 部分成功 | 54.8% | 61.6% | **+6.8pp** |
| 每任务成本 | 基准 | — | **~9x 更低** |

- 消融：纯 code 无 GUI 子 agent 只有 45.9% partial → **视觉交互仍不可完全替代**，正确姿势是「状态为主、视觉兜底」
- 核心洞察：**瓶颈从感知转向推理** —— 失败更多取决于 agent 想什么，而不是看到什么

### 与 sora 的关联 🔗

直接映射到 Hermes 工具设计哲学：

1. **工具调用审计** — 检查高频任务（练习册生成、Obsidian 笔记管理）是否过度依赖「渲染层」（截图/文本快照）而非「状态层」（文件系统/API 直接读写）
2. **验证门思想** — finish gate 与我们的三环验证（State→Evidence→Recovery）同源：执行完独立检查产物，而不是相信 agent 自报
3. **分工原则** — 能直接操作状态的不用视觉；GUI 只做兜底。这适用于一切「有 API 却去截图」的场景

**可借鉴到：** `hermes-workflow-preferences` 的工具使用审计 + `light-consistency` 的产物验证

---

## 🥉 3. OSReward: Instituting Standardized Evaluation for Cross-Platform Computer-Use Reward Models

| 元数据 |  |
|:-------|:--|
| **ID** | [`2607.28609v1`](https://arxiv.org/abs/2607.28609v1) |
| **日期** | 2026-07-30 |
| **分类** | cs.AI, cs.CL, cs.CV |
| **作者** | Qiushi Sun, Kanzhi Cheng, Yian Wang 等 |
| **状态** | ✅ 已验证（承接 CUARewardBench 方向，CUA 奖励评估共识热点） |

### 核心贡献

> 一句话概括：首个系统评估 VLM judge 的 CUA 轨迹判断基准，发现前沿模型普遍有「宽松偏见」——把失败轨迹标成成功；并开源低成本可靠奖励模型 OS-Shepherd。

CUA 评估、数据清洗、RL 都需要验证轨迹是否完成任务，但人工标注无法规模化，于是 VLM 当 judge。**但从来没人系统检查过这些 judge 到底可不可靠。** OSReward 补上了这一环。

| 问题 | 现状 | OSReward 的贡献 |
|------|------|----------------|
| **judge 无基准** | VLM judge 被广泛使用，可靠性无人系统评估 | 首个高保真基准：多平台轨迹 + 多阶段人工标注 ground truth |
| **宽松偏见** | SOTA 模型普遍把失败标成成功 | 系统性识别并量化该偏见 |
| **可靠 judge 太贵** | 可信模型成本高，开源模型差距大 | 开源 OS-Shepherd-100K 语料 + 9B/35B 奖励模型 |

### 关键发现与机制

```
CUA Trajectory (actions + states + reasoning)
        │
        ▼
  VLM Judge 判定成功/失败
        │
        ▼
  ⚠️ 系统性宽松偏见：失败被标成成功
        │
        ▼
  OS-Shepherd-100K（开源推理标注语料）
        │
        ▼
  OS-Shepherd 9B / 35B —— 30-60× 更低成本匹配商用 judge（2026-08-03 修正：原文是倍率不是百分比）
```

| 组件 | 职责 |
|:-----|:------|
| **OSReward** | 基础基准：跨平台、人工标注 ground truth |
| **OSReward-Hard** | 挑战子集：聚焦真正困难的判断案例 |
| **OSReward-Multi** | 细粒度效率与对齐评分 |
| **OS-Shepherd-100K / OS-Shepherd** | 开源语料 + 奖励模型，低成本可靠奖励信号 |

### 关键结果

| 发现 | 数据 |
|:-----|:-----|
| SOTA VLM judge 可靠性 | 均未达理想 judge 水平 |
| 宽松偏见 | 系统性：**失败轨迹被标成成功** |
| 可信 judge 成本 | 太贵，无法规模化 |
| OS-Shepherd 性价比 | 以 **30-60× 更低成本** 匹配商用 judge（2026-08-03 修正）|

### 与 sora 的关联 🔗

1. **评估器可靠性自检** — 任何自动化评估（CUA 任务、论文总结、代码审查）都要先问：评估器自身的误判率是多少？宽松偏见是否存在？（与同周 Mis-Score 论文的 **15.3% FAIL 误判** 相互印证）
2. **奖励信号设计** — 若做 RL/微调，奖励模型要防 reward hacking；FaithEyes 的 helpful-tool ratio 是另一个思路
3. **开源替代商用** — 30-60× 成本差的模式（2026-08-03 修正），和我们的低成本模型路线（opencode-go 等）一致

**可借鉴到：** `hermes-automation-patterns` 增加「评估器可靠性自检清单」

---

## 📊 3 篇论文综合评估

| 论文 | 相关性 | 验证状态 | 落地紧迫性 | 核心价值 |
|------|:------:|:--------:|:----------:|:---------|
| **OpenForgeRL** | 🔥🔥🔥🔥🔥 | ✅ 已验证 | ⚠️⚠️⚠️ | 给「自己的 agent 训练」的开源路径 |
| **StateAct** | 🔥🔥🔥🔥🔥 | ✅ 已验证 | ⚠️⚠️⚠️ | 状态优先于渲染的工具设计哲学 |
| **OSReward** | 🔥🔥🔥🔥 | ✅ 已验证 | ⚠️⚠️ | 评估器可靠性 + 低成本奖励模型 |

```
立即行动
├── OpenForgeRL  [✅] 轨迹记录层 → 自训数据管线
└── StateAct     [✅] 工具使用 state vs render 审计
中期
    ├── OSReward [✅] 评估器可靠性自检清单
    └── AgentRadio [🔍] 异步被动感知多 Agent 原语
长期
    ├── AHD [🔍]  ⚠️ harness IP 可被黑盒蒸馏（点名 Hermes 类系统）
    ├── Frontis-MA1 [🔍] AI4AI 算子化自改进
    └── AskChem [🔍] claim 中心检索 → Second Brain 文献管线
```

## 🚀 落地行动清单（待办）

### 🔴 高优先级（本周内）

#### 1. 工具使用 state vs render 审计（参考 StateAct）✅ 已落地
- [x] 对高频任务统计「直接状态操作 vs 间接读取」比例 → 规则 #16 Step 3 每周自检
- [x] 优先改造「有 API 却走截图/文本快照」的路径 → 规则 #16 状态层优先
- 产出: `hermes-workflow-preferences` 规则 #16

#### 2. 轨迹记录层调研（参考 OpenForgeRL）✅ 已落地
- [x] 评估在 Hermes 模型调用链加 proxy 记录层的成本与收益 → **结论: 无需 proxy**，state.db 已原生记录
- [x] 输出：「自训数据管线」可行性备忘 → `knowledge/Research/openforgerl-trace-pipeline-feasibility.md`
- [x] P0 落地：`scripts/export_traces.py` 导出器（7 天 206 会话 / 77k 消息实测通过）

### 🟡 中优先级（2-3 周）

#### 3. 评估器可靠性自检清单（参考 OSReward + Mis-Score）✅ 已落地
- [x] 整理清单（误判率、宽松偏见、任务有效性）→ 规则 #17
- 产出: `hermes-workflow-preferences` 规则 #17

### 🟢 长期跟踪

| 方向 | 论文 | 关注点 |
|:-----|:-----|:-------|
| Harness 安全 | AHD (2607.28147) | ⚠️ 公开分享 agent 配置/技能的可蒸馏性风险 |
| 多 Agent 编排 | AgentRadio (2607.28430) | 异步消息 + 被动感知，单 agent 32.3%→62.1% |
| AI4AI | Frontis-MA1 (2607.28568) | Draft/Improve/Debug/Crossover 四算子 |

---

## 📝 延伸阅读材料

### 论文详情
- **OpenForgeRL**: [Abstract](https://arxiv.org/abs/2607.21557v2) | [PDF](https://arxiv.org/pdf/2607.21557v2)
- **StateAct**: [Abstract](https://arxiv.org/abs/2607.22798v1) | [PDF](https://arxiv.org/pdf/2607.22798v1) | [HTML](https://arxiv.org/html/2607.22798v1)
- **OSReward**: [Abstract](https://arxiv.org/abs/2607.28609v1) | [PDF](https://arxiv.org/pdf/2607.28609v1) | [Code](https://os-copilot.github.io/OSReward-Home/)

### 技术关键词
```
# harness-native-rl   # 训练-部署错配 / proxy 拦截 / K8s rollout
# state-grounding     # 程序状态优先 / GUI 兜底 / finish gate
# vlm-judge           # 宽松偏见 / 奖励模型 / reward hacking
```

---

*Generated via arxiv-summarize cron (arxiv-fetch 2026-07-31 输出) + 搜索引擎交叉验证 | Last updated: 2026-07-31*

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
