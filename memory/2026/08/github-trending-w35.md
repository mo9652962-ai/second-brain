---
tags: [周报, github trending, W35]
date: 2026-08-23
type: weekly-trending-report
---

# GitHub 周报 — 2026-08-23（W35）

> 本周周榜：2 个新面孔精选入库（ai-memory / llmfit）+ 连榜跟踪（OpenViking/diagram-design/semantica/Switchyard）。同日脚本产物见 [[../knowledge/Research/GitHub-Weekly-2026-08-23|GitHub-Weekly-2026-08-23]]（topic 口径 Top5，互引互补）。

## 项目详情表

| # | 项目 | ★ | 本周Δ | 核心价值 | 入库笔记 |
|:--|:--|--:|--:|:--|:--|
| 1 | **akitaonrails/ai-memory** | 4.1k | **+2,404** | 跨 agent 长期记忆 + 交接：11 agents × 75 hooks 统一记忆层，自改进循环（post-turn review/approval gates/curator，**明确借鉴 Hermes**），markdown-on-disk | [[ai-memory-cross-agent-2026-08-23]] |
| 2 | **AlexsJones/llmfit** | 33.5k | +1,991 | 硬件×模型匹配：一条命令找出机器能跑什么模型，MoE 感知估算 + 社区 PR 基准流 + Windows 签名 | [[llmfit-hardware-matching-2026-08-23]] |
| — | **volcengine/OpenViking** | 32.0k | +3,033 | 字节自进化上下文数据库（记忆/RAG/Skills 统一 viking:// VFS，L0/L1/L2 三层加载）。**08-20 已评估**（Hermes memory-provider 已覆盖）→ 仅跟踪 | *(见 开源项目速览实证-2026-08-20)* |
| — | **cathrynlavery/diagram-design** | 25.4k | +8,457 | 编辑级图表（无 Mermaid-slop）。**W34 已入库**，连续第二周暴涨（18.9k→25.4k）| [[diagram-design-2026-08-16]] |
| — | **semantica-agi/semantica** | 10.2k | +2,755 | 图原生上下文基础设施。**W33 已入库**，连榜第三周 | [[semantica-graph-native-2026-08-14]] |
| — | **NVIDIA-NeMo/Switchyard** | 2.2k | +642 | LLM 模型路由网关。**W33 已入库**，连榜 | [[switchyard-llm-routing-2026-08-14]] |
| — | **cordiverse/cordis** | 7.1k | +3,614 | dsh 底层框架（时空可组合性）。**08-17 已研究** → 仅跟踪 | *(见 spacetime-diagram-edge-2026-08-17)* |
| — | **harry0703/MoneyPrinterTurbo** | 114.6k | +10,470 | 本周周榜增长王（AI 短视频）。已覆盖 moneyprinterturbo-video 技能 → 仅跟踪 | *(见 moneyprinterturbo-video 技能)* |

## 脚本 Top5 delta（topic 口径，全部连榜）

| 项目 | 上周 | 本周 | Δ | 备注 |
|:--|--:|--:|--:|:--|
| langgenius/dify | 152,564 | 153,234 | +670 | 连续连榜 |
| ChromeDevTools/chrome-devtools-mcp | 49,233 | 49,587 | +354 | 已入库 |
| HKUDS/nanobot | 47,047 | 47,288 | +241 | 已入库 |
| DeusData/codebase-memory-mcp | 39,053 | 39,945 | +892 | 已入库 |
| tirth8205/code-review-graph | 30,287 | 30,708 | +421 | 已入库（本机已装 MCP）|

## 本周洞察

1. **跨厂商 Agent 记忆成为新主线** — ai-memory（+2,404）+ OpenViking（+3,033）+ TencentDB 记忆引擎：三个方向都在解决「Agent 上下文不互通」。ai-memory 的独特点是 hooks 事件矩阵 + 自改进循环，且 README 直接承认借鉴 Hermes Agent——说明 sora 用的 Hermes 体系正是这个方向的源头之一。
2. **「硬件×模型匹配」工具化** — llmfit 33.5k 星的背后是本地推理普及后的新痛点：模型太多、显存有限，选型成本高。MoE 感知估算 + 社区基准数据资产化是它的差异化。
3. **图表赛道持续升温** — diagram-design 连续第二周暴涨（本周 +8,457），「编辑级设计 + 无 Mermaid-slop」从 niche 变成主流诉求，与 sora 的 PPT/信息图技能方向一致。
4. **本周新面孔少** — 周榜 15 个项目中仅 ai-memory、llmfit 两个未入库的新面孔；其余多为连榜（diagram-design/semantica/OpenViking/cordis）或已覆盖（MoneyPrinterTurbo/public-apis/modular）。诚实报告：无爆款级新项目，方向验证为主。

## 💎 可借鉴点归纳

**技术层面**：
- ai-memory 的 auto-improve 双保险（schema enum 约束 + 归一化兜底）→ sora 的 skill-evolution 可抄
- llmfit 的 MoE 感知估算（只看 active subset）→ 本地模型选型决策表

**方法论层面**：
- 社区 PR 基准流（数据即资产）→ 交付成本库/选题池可借鉴
- 跨 agent 交接从「文档」（AGENTS.md）升级为「自动同步层」的思路

**可实操行动**：
- 🟢 试装 llmfit（Windows 签名版）跑 `llmfit list --fit` 看 4060 推荐
- 🟡 对照 ai-memory hooks 矩阵，评估 Mnemon 之外的第二条跨 agent 记忆路径
- 🟡 diagram-design 连续两周验证图表方法论，下次 PPT/信息图优先用其模板思路

## 文件操作清单

- ✅ 新建 2 篇笔记：`knowledge/Dev/ai-memory-cross-agent-2026-08-23.md`、`knowledge/Dev/llmfit-hardware-matching-2026-08-23.md`
- ✅ 更新 `knowledge/knowledge-map.md`（W35 区）
- ✅ 补链 `knowledge/Research/MOC-GitHub.md`
- ✅ 追加 `knowledge/Research/github-projects-tracking.csv`（2 个新项目行）

---
_生成: github-trending-digest 周报 cron · k (Hermes) · 2026-08-23_
