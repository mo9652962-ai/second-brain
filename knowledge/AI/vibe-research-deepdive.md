# Vibe-Research 十轮深度探索总结

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
