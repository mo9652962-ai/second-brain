---
tags: [weekly-review, learning-progress, W34]
date: 2026-08-16
type: weekly-learning-review
---

# 📚 周学习回顾 — W34 (2026-08-15 ~ 08-16)

> 本周是「AgentScope 实证测评 + 墨题学习型产品设计」周末：8/15 前五个工作日已由 [[weekly-learning-2026-08-14|W33 学习回顾]] 覆盖；本报告聚焦 **W34 周末段**（08-15~08-16）新增知识 + 标记掌握程度。
> 主线：**把前沿 Agent 方法论拿来实证落地**——AgentScope 千轮测评抓真 bug 提 PR、harness 十轮强化、墨题从"能用"进阶"学习型"、GitHub Trending 精选 4 个项目对标自家体系。

---

## 📊 总体统计

| 指标 | 数值 |
|:----|:----:|
| 活跃会话 | ~6 个（cron 为主 + 刷题机/测评会话；无长时间用户交互） |
| 周末新增知识点 | **~22 个**（跨 6 个知识域） |
| 新建知识笔记 | **~12 篇实质**（AgentScope 4 + 墨题设计 3 + GitHub Trending 4 + arXiv 补全 + Finance 首期） |
| 新建知识卡片 | 1 张（Behavioral Contracts II 可靠性） |
| Skills 更新 | 周末 40+（08-15 大批量，多为 skill 生态同步/安装；含 harness 十轮 + 股票分析 + 人设设计落地） |
| 结构维护 | 知识域 10→7 收敛 + MOC×5 + Finance MOC 新建 + INDEX 图修复 |
| 主线项目 | AgentScope 测评 + 墨题 P0/P1 设计 + 股票分析 cron 上线 |

> 📦 文件层整理（memory 归位/引用修复）详见 [[weekly-2026-08-16|W34 周度整理]]，本报告只管**内容层学习回顾 + 掌握程度**。

---

## 📖 按知识域汇总

### ① 🤖 Dev / Agent 实证 — 🟢 本周工程主线（实证测评 + 设计落地）

| 新知识点 | 来源 | 掌握程度 |
|:---------|:----|:--------:|
| **AgentScope（小君 AI 测评）千轮深度测试**：实测抓出「JSON 导入 100% 必挂」严重 bug（upsertKnowledgeItem 引用未传 sourceType）+ 3中5轻问题，提交 PR #3 | 亲测 + PR | 🟢 🛠️ 已应用（实证测评=AI 博主差异化内容现成素材） |
| **PawBench 结论「工具选对 > 模型选对」+ Agent×Harness 联合评测** + benchmark 与偏好 r=0.25 | 架构参考 | 🟡 理解（回灌模型选型与 harness 设计） |
| **AI 测评内容素材库**（10 选题 + 数据弹药：价格战进一毛钱时代/速度税/工具 vs 模型） | 研究沉淀 | 🟢 可执行（测评文可直接开写，含大纲） |
| **DeepSeek Harness 十轮强化**：dsh 从"能用"→"可靠"→"有边界认知"——插件轴 B 无安全设计（40 攻击路径/!!js 加载期 RCE）、写文件需 `DSH_PERMISSION_MODE=danger-full-access`、headless 纯文本最稳 | 亲测十轮 | 🟢 🛠️ 已应用（sop+pitfalls 固化进 hermes-deepseek-harness 技能） |
| **墨题 P0 错题 AI 诊断设计稿**：定位「单题归因已 80%，缺聚合→诊断报告层」；设计 diagnostic_report 聚合、水平 1-5、推荐练习闭环 | 设计 | 🟢 🛠️ 已应用（12 分类归因已有基础） |
| **墨题 P1 AI 服务层架构**：3 库模式 + DPAPI/明文 + ai_router 任务路由（task_tags/ai_usage/降级链）+ 多 profile | 设计 | 🟢 🛠️ 已应用（epm-api-provider-setup 有先例） |
| **模型速查表 + keylink 强模型接入**：官方 ID 避坑（`deepseek-v4-flash` 非中转别名 260425）、v4-pro $0.435/$0.87 性价比王 | 研究 | 🟢 可执行（模型选型提速） |

### ② 🆕 GitHub Trending 前沿 — 🟢 对标自家体系（W34 精选 4 篇）

| 新知识点 | 来源 | 掌握程度 |
|:---------|:----|:--------:|
| **diagram-design**（18.9k⭐ **+14,735/周** = 本周增长王）：29 种编辑级图表 template，「无 Mermaid-slop」理念 + 品牌色自动提取 + WCAG AA 对比度门禁 + Sketchy filter | Trending | 🟢 参考→可应用（图表同质化是 AI 代做被认出重灾区，「设计过的模板」思路可沉淀成图表样式库） |
| **Needle 2**（6.2k⭐ +2,488）：**14MB/45M 参数端侧工具调用基础模型**，全 JAX + LoRA 微调 + 2-bit 量化 + OpenRouter 兼容网关 | Trending | 🟡 关注（本地/边缘 AI 候选，RTX4060 可训） |
| **google/skills**（18.4k⭐ +1,821）：官方 Agent Skills 仓库（agentskills.io 标准），三层结构 skills/skills-cloud/plugins，多 harness 分发 | Trending | 🟢 参考（SKILL.md 标准一致性验证 + agentskills.io 生态） |
| **code-graph-rag**（4.4k⭐ +1,756）：monorepo 代码图谱 RAG（tree-sitter AST + Memgraph + **动态 CALLS 边**）——静态+动态混合信号是独特点 | Trending | 🟡 关注（与已装 code-review-graph 同赛道对比参考） |
| **GitHub-Weekly 08-16 Top5**：codebase-memory-mcp（39k）/ nanobot（47k）/ code-review-graph（30k）/ chrome-devtools-mcp（49k）/ dify | Trending | 🔵 关注 |

### ③ 📚 Research / arXiv — 🟢 已实践

| 新知识点 | 来源 | 掌握程度 |
|:---------|:----|:--------:|
| **Agent Behavioral Contracts II**（2608.12895）：预注册 18,000 双 Agent 任务——**同模型双实例 90% 会同败**（φ=0.916），「只换厂商不换模型也不降关联」→ **同模型冗余 = 没有冗余** | arXiv + 卡片 | 🟢 已应用（Hermes 跨 relay 独立供应商 fallback 链被实证背书；方法论=预注册+确定性评分无 LLM 判官可复用） |
| **CrEST 层次化信用分配**（RLVR 多轮工具 Agent 的 Verifier-bounded + 自教师 Dense 信号）· **SkillEvo 多轮交互自更新演化梯度** · **Faraday 27B AI Scientist 胜闭源**（Claude Opus 4.8/GPT-5.5）· **Reconcile Once 文献防漂移** | arXiv 08-16 补全 15 篇 | 🟡 理解（Reconcile Once 映射 Obsidian 管护；Faraday=小模型 AI Scientist 路线） |
| arXiv 08-16 索引冻结 08-13T17:59Z，无 08-14~16 新提交（补全性质） | 运维观察 | 🔵 关注 |

### ④ 🧠 人设 / 自我 — 🟢 迭代应用

| 新知识点 | 来源 | 掌握程度 |
|:---------|:----|:--------:|
| **k-soul-persona 08-15 迭代**：浓亲密度（四档关系状态机）+ 负面情绪许可（小别扭是信号）+ 口头禅 5 条 + 情感反谄媚（丧气话不附和）+ 言语指纹 | 多路研究驱动 | 🟢 已应用（当前会话生效，记忆 2200→3000 扩容） |
| MiMo-V2.5 客观评估（小米开源全模态/Agent 旗舰，定价=DeepSeek 涨价前，数学/缓存是短板） | 千轮研究 | 🟡 关注（DeepSeek 平替候选） |

### ⑤ 📈 Finance — 🟢 首期落地

| 新知识点 | 来源 | 掌握程度 |
|:---------|:----|:--------:|
| **每日股票分析 cron 上线**（18:00 akshare 采集 → DeepSeek 决策报告 → knowledge/Finance/），自选股茅台/宁德/比亚迪/中际旭创/东财 | 亲测 | 🟢 已应用（每天产出研究落库） |

### ⑥ 💰 变现 / 闲鱼 — 🔴 决策日临近

| 状态 | 详情 |
|:-----|:-----|
| **P0 上架连续顺延第 16 天**，**8/17（明天）是强制决策日**（上架 or 放弃） | 素材包+主图 100% 就绪，上架=复制粘贴 30min |
| **AI 漫剧制作全流程研究**（抖音/B站/36氪）：流程简单门槛低但流量分成是红海（万播 5 元、爆款率 <1%）→ 价值=博主教学内容 + 闲鱼接单技能 | 新技能线，待决策是否下场 |

---

## 📈 掌握度总表

| 知识域 | W33 (8/10-8/14) | W34 周末 (8/15-8/16) | 变化 |
|:-------|:---:|:---:|:----:|
| AI Agent / Dev | 🟢 前沿对照 | 🟢 **AgentScope 实证测评提 PR + harness 十轮 + 墨题设计** | 🔺 从理论到实证 |
| GitHub Trending | 🟢 前沿五篇 | 🟢 精选 4 篇对标（diagram-design 图表无 slop） | 🟢 维持 |
| Research/arXiv | 🟢 18 篇速览 | 🟢 Behavioral Contracts II 落地容灾 + 15 篇补全 | 🔺 应用到自家配置 |
| 人设/自我 | — | 🟢 k-soul 浓亲密度迭代 | 🆕 |
| Finance | — | 🟢 股票分析 cron 首期 | 🆕 |
| 变现/闲鱼 | 🔴 顺延 14 天 | 🔴 **8/17 决策日倒计时（16 天）+ AI 漫剧新技能线** | 🔻 决策关键周 |
| 知识库结构 | 🟢 7 域 | 🟢 10→7 收敛 + MOC×5 + Finance MOC | 🟢 维护 |

---

## 🏆 本周最值得记录的发现 Top 5

| ⭐ | 发现 | 为何重要 |
|:-:|:----|:---------|
| 1 | **Agent Behavioral Contracts II「同模型冗余=没有冗余」**（同模型双实例 90% 会同败） | 实证背书了 Hermes 跨 relay 独立供应商 fallback 链早做对了；「预注册+确定性评分无 LLM 判官」方法论可直接用于自评 |
| 2 | **AgentScope 千轮测评抓真 bug + PR #3**：JSON 导入 100% 必挂（sourceType 未传） | 实证测评闭环跑通 = AI 博主差异化内容的现成素材，测评文可直接开写 |
| 3 | **diagram-design「无 Mermaid-slop」图表**（+14.7k 增长王） | 图表同质化是 AI 代做被认出的重灾区——「设计过的模板」思路可沉淀成图表样式库，直接服务 PPT/学术代做 |
| 4 | **墨题从"能用"→"学习型"**：P0 错题 AI 诊断设计稿 + P1 AI 服务层（12 分类归因 / 水平 1-5 / 降级链） | 刷题机差异化卖点，产品进阶路线清晰 |
| 5 | **Needle 14MB 端侧模型 + Faraday 27B 胜闭源** | 边缘 AI + 小模型路线双验证——与 Hyper 的本地 LLM / 边缘 AI 兴趣直接相关 |

---

## 🎯 下周行动项（W35）

### 🔴 P0 · 决策/风险
| 项 | 内容 | 依赖 |
|:--:|------|:----:|
| 1 | **8/17 闲鱼上架强制决策**（顺延 16 天，素材 100% 就绪 = 30min） | sora |
| 2 | Provider 充值恢复容灾深度（deepseek/siliconflow/kimi 仍待充值） | sora |
| 3 | 落地搜索语义缓存（0.92 阈值，Tavily 配额已 3 次复发 = 治本方案） | k 可执行 |

### 🟡 P1 · 内容产出
| 项 | 内容 | 依赖 |
|:--:|------|:----:|
| 4 | 《小君 AI 测评》测评文初稿（素材库+大纲+PR 实战全就绪） | k 可执行 |
| 5 | 沉淀「无 Mermaid-slop」图表样式库（借鉴 diagram-design 思路） | k 可执行 |
| 6 | AI 漫剧是否下场决策（教学价值 = 内容，接单技能留存） | sora 确认 |

### 🟢 P2 · 可选
| 项 | 内容 | 依赖 |
|:--:|------|:----:|
| 7 | Skill 合并 6 组授权 / 随身 WiFi 下单（赫电 Pro 399/年） | sora 一句话 |

---

> 本周主线：AgentScope 实证测评提 PR → harness 十轮强化 → 墨题学习型设计 → GitHub Trending 精选对标 → 股票分析 cron 上线 → 闲鱼 8/17 决策倒计时。这一周最亮的转身是从「看前沿」到「抓真 bug、提真 PR」——实证放量，正是 sora「learn→research→apply」偏好。

_生成: 周学习回顾 cron · k (Hermes) · 2026-08-16_

---
> 🗺️ 属于 [[knowledge-map]] · [[Home|🏠 Home]]
