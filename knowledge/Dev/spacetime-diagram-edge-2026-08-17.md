---
tags: [github, agent, 编程范式, 图表, 边缘AI, 研究笔记, 2026-08]
domain: AI
---

# 时空编程/图表/边缘AI 周榜研究（2026-08-17）

> 来源：小红书「时空编程新范式 + 图表 + Cursor插件 + 14MB模型 + unsloth」
> 方法：GitHub API 实证 + 论文/README 深读
> 相关: [[agent-infra-weekly-2026-08-17]] | [[game-engine-ai-research-2026-08-17]]

## 5 项目实证数据（GitHub API 实时）

| 项目 | 实际⭐ | 语言 | 定位 | 对我们的价值 |
|:---|:---|:---|:---|:---|
| cordiverse/cordis | 4,408 | TS | 时空可组合性元框架（**dsh 底层**）| ⭐ 理解 dsh 理论底座 |
| cathrynlavery/diagram-design | ~19K | Skill(HTML+SVG) | 27 种编辑级图表 | ⭐ 图表方法论 |
| cursor/plugins | 3,019 | TS | Cursor 插件规范 | ⏸️ 象征意义>实用 |
| cactus-compute/needle | 6,264 | Python | 14MB 边缘模型(45M参数) | ⏸️ 边缘AI方向 |
| unslothai/unsloth | 72,250 | Python | 本地训练显存优化 | ⭐ 4060 8GB 可微调 |

## 一、Cordis — dsh 的底层框架（最重要发现）

### 真相：不是新项目
- 就是 **dsh（DeepSeek Harness）的插件系统底座**——之前研究 dsh 源码时见过「Cordis 插件树/Reversible Plugin Spine」
- 论文《A Programming Paradigm for Spatiotemporal Composability》北大+DeepSeek，2026-08-13 预印本

### 核心概念（理解 dsh 为什么这样设计）
| 维度 | 含义 | 工程对应 |
|:---|:---|:---|
| **时间可组合性** | 移除组件时副作用完全回滚（卸载即复原）| dsh 插件卸载干净不留孤儿监听器 |
| **空间可组合性** | 依赖可声明、发现、响应式管理 | dsh 插件间 Service 提供/注入 |
| **可逆效应** | 每个上下文变换带运行时跟踪的逆 | ctx.effect → dispose 闭包 LIFO 恢复 |
| **响应式余效应** | 上下文变化通知组件 | ctx.set/get/isolation/intercept |

### 核心定理（Theorem 73）
**动态组合系统的静止状态 = 静态装配等价**——无论组件加载多少次、什么顺序，最终行为只与最终启用的组件有关。这就是「路径无关」。

### 对我们的意义
- dsh 的插件热重载/卸载即回滚/依赖注入，全部建立在这个理论上
- 我们写 dsh 插件时理解此模型 = 知道为什么插件要有 dispose、为什么依赖要声明
- 我们自己的 Sims4 mod 插件/协议管理同理——可逆效应模式通用

## 二、diagram-design — 27 种编辑级图表

- 自包含 HTML+SVG，无构建、无外部依赖、无 Mermaid 粗糙感
- 27 类型：架构/流程图/时序/状态机/ER/时间线/泳道/象限/雷达/Loop飞轮/Gantt/散点/过程/Medallion/数据流/DP安全矩阵...
- **复杂度预算**：每类型限节点数（如序列图最多 5 lifeline、架构图 12 节点）——防图表堆砌
- 品牌匹配 60 秒（读网站配色）
- 导出 SVG（Figma）/PNG（Playwright 2x）

### 与我们已有技能的对照
| 我们已有 | diagram-design 增量 |
|:---|:---|
| architecture-diagram（暗色 SVG HTML）| 27 类型全集 + 亮/暗/编辑级三变体 + 品牌皮肤 |
| excalidraw（手绘 JSON）| 编辑级质感（非手绘）+ 复杂度预算 |
| baoyu-infographic（21 布局）| 技术图表向（非营销向）|

**结论**：方法论值得吸收（复杂度预算 + 类型选择表），不装整个 skill（我们有 architecture-diagram 够用）。

## 三、cursor/plugins — 平台级动作

- 官方插件规范：plugin.json + skills/ + rules/ + mcp.json + marketplace.json
- 首批官方插件：continual-learning、create-plugin、ralph-loop、cursor-sdk 等 + 第三方 MCP（HubSpot/Intercom/X...）
- 对 sora：用 Hermes 不用 Cursor——**象征意义大于实用**；插件规范结构（skill+rule+mcp 分离）与 Hermes 插件体系同构，看一眼即可

## 四、needle — 14MB 边缘模型

- 45M 参数工具调用模型，JAX 实现，14MB
- 支持 LoRA 微调 + .cact 量化导出（2bit 起）
- 手机/手表/智能家居/机器人场景
- 对 sora：有单片机/边缘AI兴趣（microcontroller-edge-ai 技能）——方向对但暂缺硬件场景，**留档观察**

## 五、unsloth — 本地训练显存优化（真实增量）

- 72.3K⭐，本地微调 LLM 瑞士军刀
- **RTX 3090 24GB 可微调大模型**；我们 **RTX 4060 8GB**——unsloth 的显存优化（梯度检查点/量化/内存复用）可能让 8GB 微调 7B 级模型可行
- 支持 Qwen3.8/Kimi K3/DeepSeek-V4/FLUX
- 对我们：本地 Qwen3-8B（C:\Users\31954\models）微调成专用模型（如墨题词库标注模型）的潜在工具

## 落地决策

| 项目 | 决策 |
|:---|:---|
| cordis | ✅ 理解即可（dsh 已内置）——已沉淀本文档 |
| diagram-design | ⚠️ 方法论吸收（复杂度预算/类型表），不装 |
| cursor/plugins | ⏸️ 观察 |
| needle | ⏸️ 观察（边缘AI方向）|
| unsloth | ⭐ 值得试——4060 8GB 微调本地 Qwen3-8B 潜力 |

## 后续可做
- 想试 unsloth：`pip install unsloth` → 用本地 Qwen3-8B 微调一个墨题专用模型（词库标注/错题分析）→ 需要先确认 8GB 可行性（unsloth 官方称 7B 可 5GB 内训练）
