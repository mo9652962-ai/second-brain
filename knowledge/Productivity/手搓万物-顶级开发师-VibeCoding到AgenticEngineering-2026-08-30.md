# 抖音学习研究：手搓万物成为顶级开发师（Vibe Coding → Agentic Engineering）

> 来源：抖音 @瑟兰迪尔《教你手搓万物，成为顶级开发师》https://v.douyin.com/4ZmN8YxBceY/ （22s，2847赞）
> 研究日期：2026-08-30 · 方法：元数据抓取 + 千轮搜索
> 关联：已有 vibe-coding 知识库（vibe-coding-要不要学代码-2026-08-30.md / 小程序前端技术拆解）

## 视频核心

"手搓万物，成为顶级开发师"——Vibe Coding 从入门到精通，核心是把自己从"打字员"升级为"系统设计师/导演"。

## 2026 年 Vibe Coding 全景（搜索结果整合）

### 四代编程谱系（Karpathy 演进）

```
第一代：手写代码（关键基础设施）
第二代：代码补全（Cursor Tab，日常编码）
第三代：Vibe Coding（原型验证，2025.2 Karpathy 提出）
第四代：Agentic Engineering（编排 Agent，2026.2 Karpathy 亲自跨越）
```

**关键信号**：Karpathy 已不再用"vibe coding"这个词，改叫 **agentic engineering**——"99% 时间不亲自写代码，而是编排写代码的 Agent，自己作为监督角色"。

### 三层 AI 编程结构（Karpathy）

| 层 | 工具 | 场景 | 占比 |
|:---|:---|:---|:---|
| 顺境 | Cursor | 高频交互、局部微调（Tab 补全）| ~75% |
| 逆境 | Claude Code / Codex | 大块生成、跨域探索、新领域 | 大功能 |
| 绝境 | GPT-5 Pro | 深度推理、复杂重构、棘手 Bug | 极少数 |

### 工具横评（2026 数据）

| 工具 | 定位 | SWE-bench |
|:---|:---|:---|
| Claude Code | 终端 Agent | 80.8%（最高）|
| Cursor | AI IDE | 71 |
| GitHub Copilot | IDE 插件 | — |
| Windsurf | AI IDE | 68 |

### 从 Vibe Coding 到 Agentic Engineering 的四阶段路径

```
第一阶段：用 vibe coding 理解 AI 编程（1-2 周）
第二阶段：学会写 CLAUDE.md 控制 Agent（2-4 周）→ 契约关键
第三阶段：掌握 Skill 和 Hooks 扩展能力（1-2 月）→ 封装复利
第四阶段：构建 Agent 工作流体系（持续）→ Farm 调度中台并行驱动
```

### 顶级开发师的核心能力（非代码技能）

1. **写规范不写代码**：Spec-Driven，先出 PRD/用户故事当契约
2. **Context 管理**：CLAUDE.md / AGENTS.md 沉淀项目上下文（有规范 vs 无规范输出质量差 3 倍）
3. **Skill 封装复利**：今天 30 分钟封装，以后每次省 10 分钟
4. **工程纪律**：小步迭代、接口冻结、单一事实源（memory-bank/）
5. **多 AI 交叉 Review**：不同模型互相 review 发现盲区

### 反模式速查（Vibe Coding Guide 16 章）

- 需求含糊就直接开写 → 把澄清成本后置
- 一次让 AI 改太多地方 → 失去问题定位能力
- 只有生成没有门禁 → 把模型输出误当完成
- 上下文全量堆给模型 → 注意力失焦
- 用 Git 及时回滚，不在坏代码上反复修补

## 与我们团队现状的映射

| 阶段 | 我们的实现 | 状态 |
|:---|:---|:---|
| 第二阶段（契约）| AGENTS.md 注入 Codex/Antigravity + 8 槽密任务包 | ✅ 已超越 |
| 第三阶段（Skill）| 452 技能库 + .agents/skills 19 个三方共享 | ✅ 已超越 |
| 第四阶段（Agent 编排）| multi-agent-research v1.3（k 指挥 7 执行体）| ✅ 已超越 |
| **四代全用** | 关键手写（k 核验）+ 补全 + Vibe（Antigravity 前端）+ Agent 编排 | ✅ 已是 |

**结论：我们的联合工作体系已经处于第四代（Agentic Engineering）**，视频讲的"手搓万物"路径我们已走完。

## 可执行下一步

1. **对标 Vibe Coding Guide 反模式**：审查我们的密任务包是否犯"需求含糊/一次改太多"
2. **memory-bank 模式**：墨题项目考虑加 memory-bank/（设计文档/API 契约单一事实源）
3. **多 AI 交叉 Review 制度化**：已有盲评矩阵（OpenAI/Google/腾讯系），强化为默认流程
4. **Skill 复利盘点**：把今天 3 个视频的研究沉淀为可复用技能

## 结论

"手搓万物"的顶级开发师 = 意图架构师：精通需求拆解、系统品味、AI 上下文驾驭。我们团队已经是第四代形态，差距在**沉淀密度**（Skill 库持续积累）而非范式。

---
> 🗺️ 属于 [[MOC-Productivity]] · [[Home|🏠 Home]]
