---
tags: [research, AI-workflow, academic, methodology]
domain: AI
---
# Vibe-Research：AI 辅助科研全流程

来源：小黑盒 + GitHub modelscope/Awesome-Vibe-Research
更新：2026-07-25

## 核心思路

AI 深度融入科研全流程，按"科研怎么干"而不是"工具叫什么"组织。
9 个阶段：方向扫描 → 文献研究 → 方法设计 → 实验执行 → 可视化 → 写作 → 投稿 → 复现发布 → 传播

## 各阶段推荐工具

### 阶段一：Idea（灵感与选题）
| 工具 | Stars | 用途 |
|:----|:----:|:------|
| **STORM** | 29k | 多视角提问+检索，自动生成研究综述 |
| **paperseek** | 60 | 自然语言检索文献，自动迭代扩展 |
| **SciAgentsDiscovery** | 616 | 知识图谱+多智能体，跨学科生成假说 |
| **AutoDiscovery** | 186 | 从数据中发现可验证假说 |

### 阶段二：实验设计
| 工具 | Stars | 用途 |
|:----|:----:|:------|
| **Curie** | 363 | 自动化科学实验 agent，从假说澄清到实验方案 |

### 阶段三：实验执行
| 工具 | Stars | 用途 |
|:----|:----:|:------|
| **RD-Agent**（微软） | 13.6k | AI 驱动研发流程自动化 |
| **EurekAgent**（清华） | 55 | Docker 隔离实验环境，自动迭代 |
| **autoresearch**（Karpathy） | 87.8k | 单 GPU 自动跑 ML 实验 |
| **PaperBanana** | 6.6k | 多 agent 学术插图生成 |

### 阶段四：论文撰写
| 工具 | Stars | 用途 |
|:----|:----:|:------|
| **academic-research-skills** | 33.1k | Claude Code skill 套件，写作/润色/投稿 |
| **nature-skills** | 21.6k | Nature 级学术表达和绘图 skill |
| **RefChecker** | 407 | 检查引用真实性，防 AI 编造 |

### 阶段五：Review Loop
| 工具 | Stars | 用途 |
|:----|:----:|:------|
| **AI-Scientist**（Sakana AI） | 14k | 端到端自动科研+模拟审稿 |
| **AI-Scientist-v2** | 6.6k | 升级版，agentic tree search |
| **AutoResearchClaw** | 13.5k | 多阶段自进化研究流水线 |
| **EvoScientist** | 3.7k | 多 agent，持久记忆+技能演化 |
> 关联: [[researchpilot-skills]] · [[ai-research-collaboration]] · [[academic-service-research]] · academic-paper-writing（skill）
## 🔗 关键原则

1. **组合拳**：别指望一个工具从选题干到发表，分阶段配不同工具
2. **AI 主导 ≠ 你甩手**：关键判断（idea值不值、结果说明什么、rebuttal怎么回）还是你来
3. **从一个阶段切入**：先挑最头疼的那一步试一个工具
4. **注意学术规范**：很多会议要求披露 AI 使用情况

---

## 深度探索结论 (2026-07-26)

详见 [[vibe-research]] — 10 轮研究后的落地评估

### 已验证的方向
- **学术诚信闸门**：可以借鉴到 academic-paper-writing skill
- **RefChecker**：论文服务时可集成引用核验
- **EvoScientist 架构**：多 Agent + 记忆进化，与我们的自进化路线一致

---

## 深度探索总结（十轮）

> 基于 vibe-research.md 中的 15+ 个工具，10 轮搜索引擎深度调研
> 原则：优先评估能否应用/吸收强化自身

---

## 各工具评估

| 工具 | ⭐ | 定位 | 落地评估 |
|:-----|:-:|:-----|:---------|
| **STORM** (Stanford) | 29k | 多视角检索→生成维基级长文 | ⚠️ 需 OpenAI + You.com API，纯LLM成本高 |
| **AutoResearch** (Karpathy) | **87.8k** | 单GPU自动跑ML实验 | ❌ ML 研究专用，与你方向不符 |
| **AI-Scientist-v2** (Sakana) | 6.6k | 端到端自动科研+顶会论文 | ❌ 需要 Claude API + AWS，太重 |
| **academic-research-skills** | **33.1k** | Claude Code 科研全流程 Skill 套件 | ✅ **最值得关注** — 与 Hermes Skill 体系一致 |
| **RD-Agent** (微软) | 13.6k | AI 驱动研发自动化 | ❌ 面向量化金融/因子挖掘 |
| **RefChecker** (Amazon) | 1.2k | 检测 LLM 细粒度幻觉 | ✅ 轻量，可用来验引用真实性 |
| **EvoScientist** | 3.7k | 多 Agent + 持久记忆 → 自进化科研 | ✅ 架构思路值得参考（记忆+进化） |
| **SciAgentsDiscovery** | 616 | 知识图谱+多智能体→跨学科假说 | ⚠️ 学术前沿，不成熟 |
| **PaperBanana** | 6.6k | 多 Agent 学术插图生成 | ⚠️ 可关注，插图非刚需 |
| **EurekAgent** (清华) | 55 | Docker隔离实验环境 | ❌ Docker 已卸载 |

---

## 最值得落地的 3 个

### 1️⃣ academic-research-skills (33.1k⭐)

**为什么值：** 跟我们的 Skill 体系理念一致，是 Claude Code 的科研全流程套件（研究→写作→审阅→修订→定稿）

**核心功能：**
- 10 阶段调度器，含诚信验证闸门
- 三层引用定位锚（locator anchors）
- 声明级审计（`ARS_CLAIM_AUDIT=1`）
- Socratic 式论文结构规划
- 多视角同行评审

**可吸收到 Hermes 的点：**
- 诚信闸门（Stage 2.5 / 4.5）→ 我们的 academic-paper-writing 可以加入类似 check
- 引用审计机制 → RefChecker 可补充

### 2️⃣ EvoScientist 架构思路

不是直接装，而是**吸收其设计理念**：3 Agent（RA + EA + EMA）+ 持久记忆 + 跨任务进化
→ 跟我们已有的自我进化4步循环一致，确认方向正确。

### 3️⃣ RefChecker

轻量级引用核验，可集成到论文服务流程中：
- 输入 BibTeX/文本 → 核验标题/作者/年份/DOI/URL
- 可检测 AI 编造的虚假引用

---

## 结论

| 建议 | 说明 |
|:-----|:------|
| ✅ **吸收** academic-research-skills 的诚信闸门理念 | 改进我们的 academic-paper-writing skill |
| ✅ **集成** RefChecker | 论文服务时验引用真伪 |
| ⏳ **关注** EvoScientist 架构 | 方向已验证，我们的自进化路线正确 |
| ❌ **不装** STORM / AI-Scientist / RD-Agent | 太重，与闲鱼变现方向偏离 |

---
> 🗺️ 属于 [[MOC-Dev]] · [[Home|🏠 Home]]
