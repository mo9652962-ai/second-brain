---
tags: [workflow, orchestration, skills, pipeline, 2026-standards]
domain: ai-workflow
cross-domain: [ai-agent, ppt-design, academic, vibe-coding]
related: ["knowledge/AI-Agent", "knowledge/PPT-Design", "knowledge/Academic", "knowledge/Vibe-Coding"]
created: 2026-07-21
updated: 2026-07-21
---

# AI 工作流与 Skill 编排

```dataview
TABLE domain, tags, updated
FROM #ai-agent OR #workflow OR #ppt OR #academic OR #coding
WHERE file.name != this.file.name
SORT updated DESC
LIMIT 8
```

---

> 2026 年前沿：如何让多个 Skills 自然、准确地协同工作

---

## 核心洞察

> "没有明确的组合与协调机制，Skill 生态就无法发挥其关键价值：**编排多个 Skill 解决超越任何单一 Skill 能力的任务**。"
> — ArXiv 2603.02176 (2026-02)

这正是我们的问题：26 个 Skills 各自强大，但缺乏系统化的联动机制。

---

## 一、Multi-Agent 编排五大模式（2026 生产标准）

| 模式 | 结构 | 适用场景 |
|------|------|----------|
| **Orchestrator/Worker** | 1 规划者 → N 执行者 → 1 汇总 | 可分解为清晰子任务的工作 |
| **Pipeline/Sequential** | A → B → C → D | 顺序变换链（如 Unix 管道）|
| **Fan-Out/Fan-In** | 1 → N → 1 | Best-of-N、并行推理 |
| **Debate** | A ↔ B, N 轮 → Judge | 高风险正确性要求 |
| **Specialist Routing** | Router → 1 of N | 多样化查询类型 |

**→ 我们的 PPT/论文工作流对应模式：**

```
PPT 工作流 = Pipeline 模式
  大纲设计 → 结构生成 → 数据注入 → 图片方案 → 打破AI模式 → 背景注入

论文工作流 = Pipeline + Orchestrator 混合
  检索(Scholar) → 检索(知网) → 阅读(Parse) → 写作(CHN) → 写作(SCI) → 润色
```

---

## 二、Skill 内部设计五大模式（ADK 标准）

| 模式 | 作用 | 在我们的 Skills 中 |
|------|------|-------------------|
| **Tool Wrapper** | 将工具/库封装为按需加载的知识 | journal-sci-ssci-checker 检查期刊索引 |
| **Generator** | 从可复用模板生成结构化输出 | pptx-generator 从 JSON 生成 PPTX |
| **Reviewer** | 按检查清单评分 | ppt-optimizer 自检评分 |
| **Inversion** | 先访谈再行动，避免假设 | cn-ppt-outline-writer 收集需求 |
| **Pipeline** | 严格多步流程+检查点 | academic-presentation 全程控制 |

> 这些模式**可组合**：Pipeline 可以包含 Reviewer 步骤；Generator 可以先用 Inversion 收集变量。

---

## 三、Skill 组合编排最佳实践

### 3.1 渐进式加载（Progressive Disclosure）

```
Level 1: description 字段 → 触发条件匹配（不占 context）
Level 2: SKILL.md 本体 → 只在匹配时加载
Level 3: references/ 目录 → 只在特定步骤需要时加载
```

**→ 对我们的启示**：Skills 的 `description` 是最重要的单行文本——它是"开火条件"，不是摘要。

### 3.2 连贯单元设计（Coherent Units）

- **太窄**：多个 Skills 需要同时加载 → 上下文冗余 + 指令冲突
- **太宽**：难以精准激活，一个 Skill 试图做太多事
- **最佳**：一个 Skill = 一个可组合的连贯工作单元

### 3.3 验证循环（Validation Loops）

```
1. 执行工作
2. 运行验证器（脚本/检查清单/自查）
3. 如果失败 → 修复 → 重新验证
4. 只有通过验证才能继续
```

### 3.4 显式交付物（Explicit Deliverables）

❌ "写一篇论文"（范围模糊，容易跑偏）
✅ "生成：1) 摘要 200-300字 2) 引言含3个研究问题 3) 方法论含样本描述..."（可对照检查清单）

---

## 四、对我们 26 个 Skills 的实战改进

### 4.1 技能家族分类（Skill Families）

```
📝 论文家族 (9 skills)
├── 🔍 检索层: cnki-scholar, cnki-advanced-search, journal-sci-ssci-checker
├── 📖 阅读层: paper-parse, paper-summarize-academic
└── ✍️ 写作层: chinese-academic-writing, sci-paper-three-pass, paper-writing-workflow

🎨 PPT家族 (6 skills)
├── 📐 设计层: cn-ppt-outline-writer, academic-presentation
├── 🔧 生成层: pptx-generator, openclaw-slides, PowerPoint/PPTX
└── ✅ 检查层: ppt-optimizer

🖼️ 图片家族 (7 skills)
├── 🎨 创作层: ai-image-generation, nano-banana-pro-image-gen, image-prompt-generator
└── 🔧 工具层: (其余)

🤖 自改进家族 (3 skills)
├── proactive-agent, self-improving-agent, skill-vetter
```

### 4.2 Pipeline 触发词映射

| 用户说 | 自动触发的 Skill 链 |
|--------|-------------------|
| "做PPT" / "制作演示" | cn-ppt-outline-writer → pptx-generator → ppt-optimizer |
| "写论文" / "润色论文" | cnki-scholar → paper-parse → chinese-academic-writing → sci-paper-three-pass |
| "学术汇报" | cn-ppt-outline-writer + academic-presentation → pptx-generator → ppt-optimizer |
| "检索文献" | cnki-advanced-search + cnki-scholar + journal-sci-ssci-checker |
| "生成图片" | image-prompt-generator → ai-image-generation / nano-banana-pro-image-gen |
| "自我改进" | proactive-agent + self-improving-agent |

### 4.3 关键改进点

1. **Pipeline Gate 机制**：在 PPT 6 轮方法论中插入显式检查点
   - "v1 完成后，运行 ppt-optimizer 评分，≥80 分才能进 v2"
   - 避免 Agent 跳过关键步骤直接生成最终结果

2. **Skill 间数据契约**：定义明确的输入/输出格式
   - `cn-ppt-outline-writer` 输出 `outline.json` → `pptx-generator` 读入 `outline.json`
   - `cnki-scholar` 输出 `papers.json` → `paper-parse` 读入逐篇解析

3. **渐进式加载优化**：只在需要时加载 references/
   - 不让全部 6 个 PPT Skills 同时占满 context
   - 用 `description` 精准匹配任务，按需激活

4. **子 Agent 并行化**：
   - PPT 图片搜索可以 Fan-Out: 同时搜 Wikimedia + 本地生成
   - 论文检索可以 Fan-Out: 同时搜知网(中文) + OpenAlex(英文)

---

## 五、2026 前沿趋势

### Stacked Skill Invocation（2026-06 Claude Code）
> 单条消息链式调用最多 5 个 Skills

这意味着我们可以设计「复合 Skill」——一个描述触发多个协同 Skills。

### 基于文件系统的消息传递
> Pipeline 步骤间通过文件系统传递数据，而非都塞进 context

步骤 A 写 `output.json` → 步骤 B 读 `output.json`，节省 context token。

### Orchestration > Automation
> 2026 关键词从"自动化"变成"编排"——路径在执行中决定，而非预先固定

---

## 六、立即行动计划

- [ ] 为每个 Skill Family 建立 Pipeline 定义文件（`pipelines/ppt-pipeline.md` 等）
- [ ] 在 `cn-ppt-outline-writer` 和 `pptx-generator` 之间建立 JSON 数据契约
- [ ] 给 `ppt-optimizer` 添加 gate 检查功能（评分+阻断）
- [ ] 优化各 Skill 的 `description` 字段（触发条件精准化）
- [ ] 测试 Fan-Out 并行搜索（知网 + OpenAlex 并行）

---

## 🔗 知识关联

- **[[AI-Agent]]** — k 的 Skills 架构与编排能力
- **[[PPT-Design]]** — PPT 6 轮方法论如何改造成 Pipeline
- **[[Academic]]** — 论文全流程的 Pipeline 化
- **[[Vibe-Coding]]** — 脚本和数据契约的实现环境
- **[[projects/current]]** — 改进任务追踪
- **[[HOME]]** — 返回知识中枢

---

## 参考来源

- explainx.ai — Multi-Agent Orchestration Patterns Guide 2026
- developersdigest.tech — 7 AI Agent Orchestration Patterns
- YouMind/Google ADK — 5 Agent Skill Design Patterns
- agentskills.io — Best Practices for Skill Creators
- Anthropic — Building Effective AI Agents (PDF)
- ArXiv 2603.02176 — Organizing Agent Skills at Ecosystem Scale
- MindStudio — Chaining Skills Into Autonomous Pipelines
- anthonytd.com — Building Skills for AI Agents
