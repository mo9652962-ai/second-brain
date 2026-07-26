---
tags: [workflow, orchestration, skills, pipeline, hermes, 2026-standards]
domain: ai-workflow
cross-domain: [hermes-agent, skill-authoring, multi-agent, automation]
related: ["skills/hermes-agent", "skills/hermes-model-fallback", "skills/hermes-search-config", "skills/test-driven-development", "skills/systematic-debugging"]
created: 2026-07-23
updated: 2026-07-23
---

# AI 工作流与 Skill 编排（Hermes Edition）

```dataview
TABLE domain, tags, updated
FROM #hermes OR #workflow OR #skill OR #automation OR #multi-agent
WHERE file.name != this.file.name
SORT updated DESC
LIMIT 8
```

---

> Hermes Agent 生态下的编排：如何用 delegate_task、cronjob、skill_manage 让多个 Skills 自然、准确地协同工作

---

## 核心洞察

> "没有明确的组合与协调机制，Skill 生态就无法发挥其关键价值：**编排多个 Skill 解决超越任何单一 Skill 能力的任务**。"
> — ArXiv 2603.02176 (2026-02)

这正是 Hermes 的设计哲学：**70+ Skills 各自强大，通过 `delegate_task`、`cronjob`、`skill_manage` 等原生工具实现系统化的联动机制。**

---

## 一、Hermes 原生编排能力 vs. 五大模式对照

Hermes 内置的编排工具覆盖了所有经典多 Agent 编排模式：

| 经典模式 | Hermes 实现 | 适用场景 |
|----------|-------------|----------|
| **Orchestrator/Worker** | `delegate_task()` — 父Agent派生子Agent | 可分解为清晰子任务的工作 |
| **Pipeline/Sequential** | Skill 链 + `context_from` 数据传递 | 顺序变换链（如写作→翻译→润色） |
| **Fan-Out/Fan-In** | `delegate_task(tasks=[...])` — 并行子任务 | Best-of-N、并行推理 |
| **Debate** | `delegate_task()` + Cron 审核节点 | 高风险正确性要求 |
| **Specialist Routing** | `skill_manage` + 条件加载 | 多样化查询类型 |

### 1.1 Orchestrator/Worker 模式

```python
# Hermes: 父Agent 派生子Agent 并行工作
from hermes_tools import delegate_task

# 并行执行 3 个子任务
results = delegate_task(tasks=[
    {"goal": "搜索 2026 年 DeepSeek 最新论文", "context": "关注技术突破"},
    {"goal": "检索 arXiv 上关于 Agent 编排的论文", "context": "2025-2026"},
    {"goal": "总结当前 AI Agent 最佳实践", "context": "面向开发者"},
])
# 父Agent 自动汇总所有结果
```

**要点**：
- `delegate_task(tasks=[...])` 并行派生子 Agent，默认最多 3 个并发
- `background=True` 让子任务在后台运行，不阻塞主会话
- Leaf 角色不能继续派生子任务；`role="orchestrator"` 可以嵌套
- 子 Agent 的结果自动回到父 Agent 的上下文

### 1.2 Pipeline/Sequential 模式

```text
Hermes Cron Pipeline:   cronjob A → cronjob B → cronjob C
                             │             │
                        context_from   context_from
```

通过 Cron 的 `context_from` 实现步骤间数据传递：

```bash
# 步骤 A：每天早上 9 点检索论文
hermes cron create "0 9 * * *" \
  --prompt "检索 arXiv 上最新 AI 论文" \
  --name paper-fetch

# 步骤 B：论文检索完成后自动执行总结
hermes cron create "0 10 * * *" \
  --prompt "总结昨天获取的论文" \
  --context-from paper-fetch \
  --name paper-summarize
```

### 1.3 Fan-Out/Fan-In 模式

```python
# 并行 Fan-Out：同时搜索多个来源
from hermes_tools import delegate_task

tasks = [
    {"goal": "用 web_search 搜索 'DeepSeek R1 2026'", "context": ""},
    {"goal": "用 arxiv skill 搜索 2026 DeepSeek 论文", "context": ""},
    {"goal": "搜索中文社区关于 DeepSeek 的讨论", "context": ""},
]
results = delegate_task(tasks=tasks)
# 汇总 = 自动的 Fan-In
```

### 1.4 Debate 模式

借助 Cron 的审核节点实现多轮验证：

```bash
# 主任务：生成报告
hermes cron create --schedule "0 14 * * *" \
  --prompt "撰写本周 AI 行业周报" \
  --name weekly-report

# 审核节点：生成 2 小时后运行质量检查
hermes cron create --schedule "0 16 * * *" \
  --prompt "审核 weekly-report 的输出，检查事实准确性" \
  --context-from weekly-report \
  --name report-review
```

### 1.5 Specialist Routing 模式

```python
# 根据任务类型加载对应 Skill
skill_manage(action='view', name='test-driven-development')  # 开发任务
skill_manage(action='view', name='systematic-debugging')     # 调试任务
skill_manage(action='view', name='academic-paper-writing')   # 论文任务
# 按需加载，不浪费 context
```

---

## 二、Skill 内部设计五大模式（Hermes 兼容）

| 模式 | 作用 | Hermes Skills 实例 |
|------|------|-------------------|
| **Tool Wrapper** | 将工具/库封装为按需加载的知识 | `huggingface-hub` 封装 HF CLI；`llama-cpp` 封装 GGUF 推理 |
| **Generator** | 从可复用模板生成结构化输出 | `powerpoint` 从 JSON 生成 PPTX；`xlsx` 生成 Excel |
| **Reviewer** | 按检查清单评分 | `requesting-code-review` 安全检查清单 |
| **Inversion** | 先访谈再行动，避免假设 | `plan` 模式：先写计划再执行 |
| **Pipeline** | 严格多步流程+检查点 | `test-driven-development` 红绿重构循环；`systematic-debugging` 4 阶段流程 |

> 这些模式**可组合**：Pipeline 可以包含 Reviewer 步骤；Generator 可以先用 Inversion 收集变量。

### 2.1 Hermes Skill 结构规范

```yaml
---
name: my-skill
description: "精确的触发条件描述——这是最重要的单行文本"
tags: [hermes, workflow, ...]
version: 1.0.0
author: k
---

# SKILL.md
## 触发条件
- 当用户说 X 时
- 当遇到 Y 场景时

## 步骤
1. Step one
2. Step two

## Pitfalls
- ⚠️ 常见陷阱
```

### 2.2 渐进式加载（Hermes 三级）

```
Level 1: skill_list / description 字段 → 触发条件匹配（不占 context）
Level 2: skill_view(name) → SKILL.md 本体 → 只在匹配时加载
Level 3: linked_files (references/, templates/, scripts/) → 只在特定步骤需要时加载
```

**→ 最重要的原则**：Skills 的 `description` 是"开火条件"，不是摘要。

---

## 三、Hermes 原生编排最佳实践

### 3.1 delegate_task 并行化

```python
# 并行 Fan-Out：从多个来源获取信息
from hermes_tools import delegate_task

results = delegate_task(tasks=[
    {"goal": "搜索 Tavily: 2026 LLM trends"},
    {"goal": "搜索 Exa: latest AI research papers"},
    {"goal": "搜索 DDGS: AI agent frameworks comparison"},
])

# 自动汇总结果
summary = "\n\n".join([r["summary"] for r in results])
```

### 3.2 Cron 定时任务链

```bash
# 早 8:00 —— 获取晨间信息
hermes cron create "0 8 * * *" \
  --prompt "搜索今日 AI 头条并总结" \
  --name morning-digest

# 晚 7:00 —— 回顾与记录到 Obsidian
hermes cron create "0 19 * * *" \
  --prompt "回顾 today's digest 并写入 Obsidian" \
  --context-from morning-digest \
  --name evening-review
```

### 3.3 Skill 链式管道

```text
文档处理 Pipeline:
  web_extract(URL) → [content] → delegate_task(write_summary)
  → [summary] → skill_view('powerpoint') → create_ppt(summary)
```

### 3.4 验证循环（Testing Loops）

```
┌─────────────────────────────────────┐
│ 1. 执行工作                           │
│ 2. 运行验证器（TDD skill / 自检清单）  │
│ 3. 如果失败 → 修复 → 重新验证          │
│ 4. 只有通过验证才能提交/继续            │
└─────────────────────────────────────┘
```

Hermes 内置 TDD skill (`test-driven-development`) 和代码审查 skill (`requesting-code-review`) 直接支持此模式。

### 3.5 显式交付物

❌ "写一篇论文"（范围模糊，容易跑偏）
✅ "生成：1) 摘要 200-300字 2) 引言含3个研究问题 3) 方法论含样本描述..."（可对照检查清单）

---

## 四、Hermes Skills 生态分类（70+ Skills）

### 按家族分类

```text
📝 学术家族 (6 skills)
├── academic-paper-writing, arxiv, youtube-content, llm-wiki
├── ocr-and-documents, pdf

🛠️ 开发家族 (10+ skills)
├── TDD: test-driven-development, systematic-debugging
├── 代码质量: requesting-code-review, simplify-code, spike
├── 工程: engineering-workflow, web-dev-2026
├── 模型: llama-cpp, huggingface-hub, weights-and-biases

🎨 创意家族 (12+ skills)
├── ascii-art, ascii-video, architecture-diagram, excalidraw
├── p5js, sketch, claude-design, popular-web-designs
├── manim-video, comfyui, baoyu-infographic, songwriting-and-ai-music

📊 生产力家族 (10+ skills)
├── office: docx, xlsx, powerpoint, pdf, nano-pdf
├── 笔记: obsidian, obsidian-vault-management, notion
├── 邮件: himalaya
├── 日历: google-workspace
├── 数据: airtable, maps

🤖 自主 Agent 家族 (4 skills)
├── claude-code, codex, opencode
├── hermes-agent（元技能：配置 Hermes 自身）

🔍 搜索家族 (5+ skills)
├── hermes-search-config, hermes-model-fallback
├── hermes-web-search-config, github-*
├── blogwatcher, polymarket

🏠 智能家居 (1 skill)
├── openhue

🎵 媒体家族 (5+ skills)
├── youtube-content, gif-search, heartmula, songsee
├── text-to-speech
```

### Pipeline 触发词映射

| 用户说 | 自动触发的 Skill 链 |
|--------|-------------------|
| "开发新功能" | `plan` → `test-driven-development` → `requesting-code-review` |
| "修复这个 bug" | `systematic-debugging` → `engineering-workflow` |
| "写论文" | `arxiv` → `academic-paper-writing` → `humanizer` |
| "做 PPT" | `powerpoint` / `sketch` → `architecture-diagram` |
| "生成图片" | `comfyui` / `ascii-art` |
| "日常汇报" | `hermes-model-fallback` + `hermes-search-config` + cron |
| "自我改进" | 自动：`session_search` 回顾 + `skill_manage` 优化 |

### 关键改进点

1. **delegate_task 作为 Pipeline Gate**
   - 在 Pipeline 中插入显式检查点：
     ```python
     result = delegate_task(goal="生成初稿")
     verify = delegate_task(goal=f"审核以下内容，评分>=80才能通过：{result}")
     if not verify_passed:  # 重新生成
     ```

2. **Skill 间数据契约**
   - `delegate_task` 的 `context` 参数传递结构化数据
   - `cronjob` 的 `context_from` 链式传递输出
   - 文件系统传递：A 写 `output.json` → B 读 `output.json`（节省 context token）

3. **渐进式加载优化**
   - 用 `skill_manage(action='view', name='...')` 按需加载
   - 不用一次性加载全部 Skills
   - 用 `description` 精准匹配任务

4. **并行化**
   - `delegate_task(tasks=[...])` 支持 Fan-Out 模式
   - 同时搜索多个来源（Tavily + Exa + DDGS 并行）
   - 跨模型并行推理

---

## 五、2026 前沿趋势

### Stacked Skill Invocation

单次会话可链式调用多个 Skills，通过 `skill_manage()` 逐级激活。

### 基于文件系统的消息传递

Pipeline 步骤间通过文件系统传递数据，而非都塞进 context：
```python
# 步骤 A
open("output.json", "w").write(json.dumps(result_a))
# 步骤 B — 读取步骤 A 的输出
result_a = json.load(open("output.json"))
```

### Orchestration > Automation

> 2026 关键词从"自动化"变成"编排"——路径在执行中决定，而非预先固定

Hermes 的 `delegate_task` 天生支持运行时路径决策：父 Agent 根据子任务结果决定下一步调用哪个 Skill。

### Hermes Curator 自动 Skill 维护

Hermes 的 Curator 系统自动管理 Agent 创建的 Skill：
- 追踪使用频率
- 标记长期未使用的 Skill 为"陈旧"
- 可选合并重叠 Skill（`curator.consolidate: true`）
- **永远不会删除**——最大破坏动作是归档

---

## 六、立即行动计划（执行完成 ✅）

- [x] ✅ 为常用工作流建立 Hermes Cron Pipeline 定义
  ```bash
  hermes cron create "0 7 * * *" "检索 arXiv 最新论文" --name arxiv-fetch --skill arxiv
  hermes cron create "0 8 * * *" "总结 arxiv-fetch 论文到 Obsidian" --name arxiv-summarize
  ```
- [x] ✅ 测试 Fan-Out 并行搜索（Tavily + Exa + DDGS 并行）
- [x] ✅ 配置 Curator 自动维护 Skill 生态（93 全活跃）
- [x] ✅ JSON 数据契约：delegate_task context 结构化传递
- [x] ✅ Skill description 触发条件精准化（随使用自然优化）

---

## 🔗 知识关联

- **[[hermes-agent]]**（skills/） — Hermes Agent 完整 CLI 与配置参考
- **[[hermes-model-fallback]]**（skills/） — 模型容灾链配置
- **[[hermes-search-config]]**（skills/） — 5 搜索引擎多后端配置
- **[[test-driven-development]]**（skills/） — TDD 红绿重构循环
- **[[systematic-debugging]]**（skills/） — 4 阶段 Bug 诊断
- **[[../LLM-Providers]]** — 当前模型与提供商配置

---

## 参考来源

- Hermes Agent Docs — https://hermes-agent.nousresearch.com/docs/
- Anthropic — Building Effective AI Agents
- ArXiv 2603.02176 — Organizing Agent Skills at Ecosystem Scale
- explainx.ai — Multi-Agent Orchestration Patterns Guide 2026
- Hermes Agent Skills — 70+ skills catalog
---
> 关联: [[AI-Agent]] · [[k-self-improvement]] · [[Cross-Domain|🔀 知识地图]] | [[HOME|🏠 首页]]
