# Agent 操作系统层：Harness 趋势研究（面试视角）

> 来源：抖音 @划水的青蛙《Agent的操作系统层的出现愈发清晰》（2026-08-21）
> 研究日期：2026-08-22 | 触发：sora 抖音学习任务 → 千轮研究 → 存库
> 状态：✅ 已完成（含面试答题框架）

## TL;DR（结论置顶）

**Agent = Model + Harness**。2026-08 两周内，DeepSeek 开源 DeepSeek Harness（14.9 万星、5100+ 插件）与 OpenAI 全面开源 Codex Harness（CLI/SDK/app-server 三大组件）几乎同一天落地——两大巨头同时在把「Agent 运行框架」从产品能力下沉为**平台级基础设施**。这不是巧合，而是行业共识的显性化：**模型能力的边际收益递减，下一个竞争杠杆在运行时层**。Harness 正在成为 Agent 的「操作系统」：管上下文、工具、状态、权限、调度、审计。

## 一、核心事件时间线

| 时间 | 事件 | 意义 |
|:---|:---|:---|
| 2026-01-23 | OpenAI《Unrolling the Codex agent loop》 | 官方拆解 agent loop，harness 概念出圈 |
| 2026-02-04 | OpenAI《Unlocking the Codex harness: App Server》 | JSON-RPC 协议开放，harness 平台化起点 |
| 2026-04-15 | OpenAI Agents SDK 大升级 | model-native harness + 原生沙箱，接入 7 家沙箱供应商 |
| 2026-08-13 | **DeepSeek Harness 开源** | 12h 破 5 万星，一切皆插件（Cordis 架构） |
| 2026-08-21 | **OpenAI 全面开源 Codex Harness** | CLI/SDK/app-server 三大件，Apache-2.0 |

## 二、什么是 Harness / Agent OS

### 一句话定义
模型是大脑，Harness 是让大脑拥有手和脚、记忆和门禁的**运行环境**。裸模型不是 Agent，模型 + Harness 才是。

### Harness 管的资源（类比 OS 资源管理）

| 传统 OS 管 | Agent Harness 管 |
|:---|:---|
| CPU / 内存 | Context Budget（上下文预算） |
| 进程 / 线程 | Agent Loop / Subagent 调度 |
| 文件系统 | Workspace / AGENTS.md / 项目记忆 |
| 权限系统 | 沙箱、审批流、信息流隔离 |
| 设备驱动 | 工具注册表（Tools/Skills/MCP） |
| 日志 / 审计 | Append-only Session Log / Trajectory |
| 进程隔离 | Sandbox（Landlock/bwrap/worker_threads） |

### 学术定义（AI Harness Engineering, arXiv 2605.13357）
Harness = 包在 foundation model 外部的 runtime substrate，11 项职责：上下文管理、工具调用、项目记忆、任务状态、可观测性、失败归因、验证、权限、维护状态。H0-H3 ladder 实证：**同样模型，Harness 层级越高，可审计行为越强**。

## 三、为什么「操作系统层」这个概念现在清晰了

1. **模型边际收益递减**：OpenAI 官方数据——仅调整 Harness（保留推理+上下文压缩），ARC-AGI-3 得分 13.3% → 38.3%（3 倍），**输出 Token 减少 6 倍**。模型没换，工作方式换了，能力就变了。
2. **长任务需求**：企业要 agent 连续干几小时、跨上下文窗口，需要状态持久化、验证循环、失败恢复——这些全是 Harness 的事。
3. **安全可控**：agent 有文件/Shell/网络/凭据权限，必须有沙箱 + 审批 + 审计。AOHP（Android 开源 Harness）实证：OS 级 agent 支持使任务完成率 +21.12%、token 成本 -51.55%。
4. **两巨头同时押注**：DeepSeek 走「一切皆插件」（Cordis，可热插拔、可回滚、可自进化 RHI）；OpenAI 走「平台开放」（把 Codex 底座开源，让业务系统直接嵌入）。路线不同，方向一致：**Harness 是新的竞争层**。

## 四、DeepSeek Harness 为什么被称为「赛博乐高」

- **Everything is a Plugin**：模型、工具、Skills、会话、沙箱、存储、调度、UI，连 **Agent Loop 本身**都是插件
- **Cordis 内核**：只管插件加载/卸载/依赖，不承载能力；插件卸载时注册效果按反序回滚（服务不中断）
- **Append-only Session Log**：模型看到的一切（系统提示、思维链、工具调用、子 Agent 调度、上下文注入）写入同一事件流 → 可搜索、分叉、回放
- **Preset**：一键分发完整 Agent 能力（整合插件+技能+网页浏览+上下文策略）
- **RHI 方向**：把 Harness 切成有稳定语义、可归因的离散单元 → 为「Harness 自进化」打基础（腾讯云长文分析）

## 五、面试答题框架（怎么理解这个趋势）

### 第一层：定义（30 秒）
> 「Agent = Model + Harness。模型负责推理，Harness 负责让模型在真实环境持续工作——管上下文怎么装、工具怎么调、失败怎么恢复、权限怎么控、轨迹怎么审计。最近 DeepSeek 开源 DeepSeek Harness、OpenAI 开源 Codex Harness，本质是把这个运行时层从各家产品里抽出来，变成可复用、可组合的平台。」

### 第二层：为什么现在（1 分钟）
> 「三个驱动力：一、模型能力增长边际递减，OpenAI 实测优化 Harness 让 ARC-AGI-3 从 13.3% 涨到 38.3%、Token 省 6 倍，说明同样的模型换一套运行时能力差异巨大；二、企业级长任务需要状态、验证、恢复，这些是模型本身给不了的；三、安全可控，Agent 有真实权限，必须沙箱+审批+审计。所以竞争从『谁的模型强』转向『谁能把模型组织成可靠的工作系统』。」

### 第三层：架构理解（加分项）
> 「传统 OS 管 CPU/内存/文件/进程，Harness 管 Context Budget/工具注册表/Workspace/Agent 调度/沙箱/审计——是一套面向 Agent 的资源管理抽象。DeepSeek 更进一步把 Agent Loop 本身做成插件（可热替换、可回滚、可自进化），OpenAI 则把 Codex 底座开放成 CLI/SDK/app-server 让业务系统直接嵌入。两条路线，一个方向。」

### 第四层：风险与深度（拉开差距）
> 「要泼冷水：插件生态的供应链安全（恶意插件可碰上下文/文件/Shell/凭据）、长会话稳定性和预算失控、评测体系（Model/Prompt/Tools/Harness/Budget 五要素要分开写）。以及 Harness 本身会被模型能力吸收一部分——今天 harness 补模型的短板，未来部分能力会内化进模型。」

### 第五层：落地经验（杀手锏）
> 「我自己实际用过 dsh（DeepSeek Harness）做编码委派：headless 一次性任务、Web UI 插件生态、沙箱权限配置、跨 agent 记忆（mnemon）——亲身体会到 Harness 层的插件化让『换一个 provider 就能换整个产品形态』。」

## 六、对 sora 的启示

1. **dsh 实战价值确认**：你已经在用行业最前沿的 harness 架构（插件树 22 个、Cordis 配置、Preset），这段经验是面试/内容/接单的差异化素材
2. **AI 博主内容方向**：这个主题适合做一期「DeepSeek Harness vs OpenAI Codex Harness：Agent 操作系统层之争」——有冲突、有数据、有概念
3. **接单角度**：Harness 生态的基础设施缺口（插件权限审计、成本仪表盘、跨会话记忆、领域 Preset）是独立开发者机会——王若风博客明确提了这点
4. **评估视角**：评估任何 Agent 产品时，不再只看模型，要看 Model + Prompt + Tools + Harness + Budget 五要素

## 参考资料

- DeepSeek Harness 官网/架构文档：https://www.deepseek.com/harness/ · https://deepseek-harness.github.io/deepseek-harness/reference/
- OpenAI Codex Harness 开源解读（新智元/新浪科技 2026-08-21）
- OpenAI Agents SDK 演进：https://openai.com/index/the-next-evolution-of-the-agents-sdk/
- 新浪科技《黑鲸鱼 DeepSeek Harness，从「赛博乐高」变成 Agent Store》
- 王若风《DeepSeek Harness 爆火之后，我翻完 X 上的讨论》
- 腾讯云《DeepSeek的Harness，有一套新世界观》（RHI 视角）
- arXiv 2605.13357《AI Harness Engineering》
- arXiv 2606.01508《Agent Operating Systems (AOS)》
- LangChain《The Anatomy of an Agent Harness》
