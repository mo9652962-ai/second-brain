---
domain: 编程
cross-domain: ["AI-Agent", "AI-Workflow", "CAD-Design"]
related: [[AI-Agent]], [[AI-Workflow]], [[CAD-Design]], [[Vibe-Coding]]
description: "编程技术栈、Python 3.14 新特性、AI Agent 架构模式、ReAct 范式、Hermes Agent 技能开发"
---

# 编程技术栈

> 2026-07-21 全网学习汇总。来源: Tavily、Exa、Firecrawl、DDGS、SearXNG

## Python 3.14 (2026 年 10 月发布) — 核心新特性

### 1. Template String Literals (t-strings) — PEP 750

`t"..."` 不像 f-string 立即渲染，而是生成一个 **Template 对象**，包含静态部分和插值——可以在渲染前处理/转义。

```python
from string.templatelib import Template

# 安全的 SQL/DSL 构建
t = t"SELECT * FROM users WHERE id = {user_id}"
# Template 对象，可在最终渲染前做参数化/转义处理

# 对比 f-string (立即渲染，容易 SQL 注入)
# f"SELECT * FROM users WHERE id = {user_id}"  ← 危险！
```

**适用场景**: SQL 参数化、HTML 模板、LLM prompt 结构化拼接

### 2. Deferred Annotation Evaluation — PEP 649 & 749

类型注解延迟求值，**不再需要前向引用引号**。

```python
# Python 3.13
class Node:
    def __init__(self, next: "Node | None" = None): ...

# Python 3.14
class Node:
    def __init__(self, next: Node | None = None): ...  # 直接写！
```

**对 FastAPI/Pydantic 项目是大提升**——注解不再在定义时立即求值。

### 3. Multiple Interpreters — PEP 734

```python
from concurrent.futures import InterpreterPoolExecutor

with InterpreterPoolExecutor() as executor:
    future = executor.submit(cpu_intensive_task)
    result = future.result()
```

每个 interpreter 有独立的 GIL → **真正的多核并行**，启动比 process 快，内存占用更少。

### 4. Free-threaded Mode (正式支持)

Python 3.14 的 free-threaded build (`python3.14t`) 正式受支持。Snowflake 等库已开始适配。

### 5. Asyncio Introspection

```bash
# 查看某个 PID 里的 async 任务树
python -m asyncio pstree 12345
```

调试 async 代码的利器，无需第三方 profiler。

### 6. 其他实用更新

| 特性 | 说明 |
|------|------|
| `uuid7()` | 按创建时间可排序的 UUID |
| `date.strptime()` | 直接解析日期字符串，无需先转 datetime |
| `Zstandard` 压缩 | `tarfile`/`zipfile`/`shutil` 原生支持 `.zst` |
| `locals()` 返回真 mapping | 可观察更新，调试器更稳定 |
| 增强 REPL | 语法高亮 + 智能补全 |
| `asyncio.get_event_loop()` | 不再隐式创建 loop，必须用 `asyncio.run()` |

---

## AI Agent 架构模式 (2026 生产标准)

### ReAct Pattern (Reason + Act)

```
Thought: 我需要搜索 Wikipedia 确认马达加斯加的位置
Action: search_wikipedia
Action Input: Madagascar
Observation: 马达加斯加是非洲东南海岸的岛国...

Thought: 根据搜索结果，我知道答案了
Final Answer: 马达加斯加位于...
```

**核心代码结构**:

```python
@dataclass
class Action:
    thought: str
    action_name: Optional[str] = None
    action_input: Optional[str] = None

class ReActAgent:
    def __init__(self, llm, tools, max_steps=5):
        self.llm = llm
        self.tools = tools
        self.max_steps = max_steps
    
    def run(self, query):
        for step in range(self.max_steps):
            action = self.llm.decide(self.context, self.tools)
            if action.action_name == "final_answer":
                return action.action_input
            tool = self.tools[action.action_name]
            observation = tool(action.action_input)
            self.context.add(observation)
```

### CodeAct Pattern (2026 新兴)

**ReAct 的进化版**: Agent 直接生成 Python 代码来推理和调用工具，而非 JSON/text 格式。

```python
# ReAct: {"action": "calculator", "input": "2+2"}
# CodeAct: 
"""
result = calculator("2+2")
print(f"2+2 = {result}")
"""
```

**Manus AI 使用的核心模式** — 更适合代码密集型任务。

### 生产级 Agent 的 6 个必须组件

```
┌─────────────────────────────────────┐
│  1. Reasoning Engine (LLM planner)  │
├─────────────────────────────────────┤
│  2. Tool System (严格契约 + 重试)    │
├─────────────────────────────────────┤
│  3. Memory (core / archival / recall)│
├─────────────────────────────────────┤
│  4. Observability (trace + 评估)     │
├─────────────────────────────────────┤
│  5. Guardrails (安全边界)            │
├─────────────────────────────────────┤
│  6. Human-in-the-Loop (审批机制)     │
└─────────────────────────────────────┘
```

**关键原则**: "If you want an AI agent that actually works in production, treat it like a **distributed system** where the LLM happens to be the planner."

### 6 大 Agent 编排模式

| 模式 | 结构 | 适用场景 |
|------|------|----------|
| **Orchestrator-Worker** | 1 规划 → N 执行 → 1 汇总 | PPT/论文多步骤任务 |
| **Pipeline/Sequential** | A → B → C 顺序变换 | 数据处理流水线 |
| **Fan-Out/Fan-In** | 并行执行后合并 | 知网+OpenAlex 并行检索 |
| **Debate** | 多 Agent 辩论 → Judge 裁决 | 高风险决策 |
| **Specialist Routing** | Router → 1 of N 专家 | 按查询类型路由 |
| **CodeAct Loop** | Agent 写代码 → 执行 → 观察 | 代码密集型任务 |

---

## Hermes Agent 框架下的 Agent 架构

### Hermes 核心编排工具

| 工具 | 用途 | 对应模式 |
|------|------|----------|
| `delegate_task` | 向子 Agent 委派独立任务，获得结果后继续 | Orchestrator-Worker |
| `cronjob` | 定时执行技能工作流（周期性自动化） | Pipeline / Scheduled |
| `skill_manage` | 创建/更新/删除技能（程序记忆） | Generator / Reviewer |
| `terminal` | 执行 shell 命令（前台/后台/PTY） | CodeAct Loop |
| `process` | 管理后台进程生命周期 | Daemon / Watcher |

### 典型工作流示例

```python
# Hermes Agent 中 Orchestrator-Worker 模式
# 主 Agent 委派并行任务给子 Agent
subtask_a = delegate_task("搜索 2026 AI Agent 趋势", tools=["web_search"])
subtask_b = delegate_task("总结 ReAct 论文核心观点", tools=["web_extract"])
results = await asyncio.gather(subtask_a, subtask_b)

# 合并结果
final = synthesize(results)
```

### Cronjob 自动化

```bash
# 每周一早 8 点执行学术文献检索
hermes cron create --schedule "0 8 * * 1" \
  --skill academic-paper-writing \
  --input '{"query": "latest AI agent papers last week"}'
```

---

## Hermes Skill 开发最佳实践

### Skill 设计五模式

| 模式 | 说明 | 例子 |
|------|------|------|
| **Tool Wrapper** | 封装工具为按需加载知识 | Tavily 搜索 skill |
| **Generator** | 从模板生成结构化输出 | PPT 大纲 → 幻灯片 |
| **Reviewer** | 按检查清单评分 | ppt-optimizer |
| **Inversion** | 先访谈再行动 | 需求澄清 skill |
| **Pipeline** | 严格多步流程 + 检查点 | 论文写作 6 轮流程 |

### SKILL.md 格式要点

```markdown
# Skill Name
> 描述 ≤160 字符（精准匹配触发词）

## 触发条件
- 用户说「做 PPT」→ 自动激活 PPT skill 家族

## 工作流
1. 步骤 A
2. 步骤 B

## 输出格式
\```json
{ "key": "value" }
\```

## 安全
- 不执行 rm -rf /
- 敏感操作前询问
```

### Skill 安全

- **Skill Specter**: NVIDIA 合作，自动扫描隐藏指令
- **Skill Card**: 每个 skill 需说明来源和功能
- **Gating**: 通过 allowlist 控制 skill 可访问的工具
- **Pinned Skills**: 保护关键技能不被意外删除；锁定后仍可 patch（改进），仅禁止 delete

---

## build123d + AI Agent 结合 (2026 前沿)

### Text-to-CAD Harness

```
用户 prompt → Agent 生成 build123d 代码 → 运行生成 STEP/STL/GLB
                                    ↓
                          Viewer 预览 (@cad 引用)
                                    ↓
                          修改参数 → 重新生成
```

**示例工作流**:

```python
# Agent 生成的代码
from build123d import *

# 参数化 L 型支架
WALL_HEIGHT = 50
THICKNESS = 5
HOLE_DIA = 4

with BuildPart() as bracket:
    with BuildSketch() as sk:
        Rectangle(40, WALL_HEIGHT)
        Rectangle(THICKNESS, WALL_HEIGHT, align=Align.MIN)
    extrude(amount=30)
    
    # 4 个安装孔
    with Locations(bracket.faces().sort_by(Axis.Z)[-1]):
        with GridLocations(30, WALL_HEIGHT-10, 2, 2):
            CounterSinkHole(HOLE_DIA/2, HOLE_DIA)

export_step(bracket.part, "bracket.step")
export_stl(bracket.part, "bracket.stl")
```

**@cad 引用语法**: `修改墙高 → @cad[bracket.step#face:wall]`

---

## 学习资源

| 资源 | 链接 | 说明 |
|------|------|------|
| Python 3.14 官方文档 | docs.python.org/3/whatsnew/3.14.html | 权威 |
| build123d 文档 | build123d.readthedocs.io | 参数化 CAD |
| ReAct 从零实现 | til.simonwillison.net/llms/python-react-pattern | Simon Willison |
| AI Agent 架构 | redis.io/blog/ai-agent-architecture | Redis 出品 |
| LangChain 2026 框架 | langchain.com/resources/ai-agent-frameworks | 框架对比 |
| Hermes Agent Docs | hermes-agent.nousresearch.com/docs | 官方文档 |

---

_最后更新: 2026-07-23_
