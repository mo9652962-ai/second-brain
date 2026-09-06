---
tags: [周报, GitHub Trending, W37]
date: 2026-09-06
type: weekly-trending-report
---

# GitHub 周报 — 2026-09-06（W37）

> 本周周榜：**5 个全新面孔全部入库**（archify / ECC / scientific-agent-skills / OpenMAIC / VoiceStudio）+ 连榜跟踪。同日脚本产物见 [[../knowledge/Research/GitHub-Weekly-2026-09-06|GitHub-Weekly-2026-09-06]]（topic 口径 Top5，互引互补）。

## 项目详情表

| # | 项目 | ★ | 本周Δ | 核心价值 | 入库笔记 |
|:--|:--|--:|--:|:--|:--|
| 1 | **tt-a1i/archify** | 49.9k | **+19,480** | 可验证系统图 Agent Skill：typed JSON IR → 确定性编译 + 校验收据（Proof Lab）+ Before/Delta/After 快照评审。**本周增长王** | [[../knowledge/Dev/archify-verifiable-diagrams-2026-09-06|archify-verifiable-diagrams-2026-09-06]] |
| 2 | **affaan-m/ECC** | 250.2k | +5,445 | 多 Agent harness 优化系统：68 agents + 286 skills + hooks/memory + AgentShield 安全扫描，覆盖 Claude Code/Codex/Cursor/Antigravity/Qwen。**周榜总星第一**，已甄别非刷星（2,631 commits/354 contributors/16 releases） | [[../knowledge/Dev/ecc-agent-harness-2026-09-06|ecc-agent-harness-2026-09-06]] |
| 3 | **K-Dense-AI/scientific-agent-skills** | 43.0k | +5,491 | 科研 Agent 技能库 #1：165 validated skills + 100+ 数据库 + 技能库 CI 治理样板（scan/tests/security/license per skill） | [[../knowledge/AI/scientific-agent-skills-library-2026-09-06|scientific-agent-skills-library-2026-09-06]] |
| 4 | **THU-MAIC/OpenMAIC** | 32.1k | +10,109 | 清华多 Agent 交互课堂：DSL 场景引擎 + choreography 编排规范（单一事实源）+ 确定性时间轴 + 课堂视频导出器 | [[../knowledge/AI/openmaic-multiagent-classroom-2026-09-06|openmaic-multiagent-classroom-2026-09-06]] |
| 5 | **debpalash/VoiceStudio** | 19.1k | +6,761 | 全本地 ElevenLabs 替代：语音克隆/视频配音/转写/有声书，646 语言；AGPL-3.0 | [[../knowledge/AI/voicestudio-local-voice-2026-09-06|voicestudio-local-voice-2026-09-06]] |

## 脚本 Top5 delta（topic 口径，全部连榜）

| 项目 | 上周 | 本周 | Δ | 备注 |
|:--|--:|--:|--:|:--|
| HKUDS/nanobot | 47,527 | 47,740 | +213 | 已入库 |
| DeusData/codebase-memory-mcp | 41,133 | 42,390 | +1,257 | 已入库 |
| ChromeDevTools/chrome-devtools-mcp | 50,167 | 51,099 | +932 | 已入库 |
| tirth8205/code-review-graph | 30,708 | 31,203 | +495 | 已入库（本机已装 MCP）|
| sansan0/TrendRadar | 61,920 | 62,055 | +135 | 已入库 |

## 连榜/观察区（未新建笔记）

- **screenshot-to-code** 77.9k（+2,034）— 经典截图转代码，长期连榜，业务关联低 → 仅跟踪
- **awesome-mcp-servers** 94.4k（+1,287）— MCP 服务器清单，已覆盖 → 仅跟踪
- **gods-eye-view** 18.1k（+5,926）— 真实数据卫星模拟器，炫但非核心 → 观察
- **minimind** 58.9k（+3,649）— 2h 从零训 64M LLM，学习价值高但已覆盖本地 LLM 技能 → 观察
- **patent-disclosure-skill** 7.5k（+1,996）— 中文专利 Agent 技能（交底书/解读/Obsidian 入库），小而新（39 commits）→ 观察，**软著/专利需求可回头细看**
- **magnitude** 3.3k（+1,396）— 本地推理服务器，明说支持 Hermes，太小 → 观察
- **open-seo** 17.3k（+2,755）— Semrush/Ahrefs 开源替代，与网站部署业务相关 → 观察（W31 提过）
- **timesfm** 31.4k（+2,968）— Google 时序基础模型，与股票分析相关 → 观察
- **tailcat** 6.4k（+3,187）— Tailscale 版 netcat → 观察

## 本周洞察

1. **可验证/可审计 = Agent 产物新标准**。archify 的校验证据链、ECC 的 AgentShield、scientific-agent-skills 的 validated skills——三个独立项目指向同一信号：生成物必须带证明。与 sora 的 service-quality / G5 门禁思路同频，方向被验证。
2. **Agent Skills 标准生态成熟**。archify / scientific-agent-skills / patent-disclosure-skill 全是 SKILL.md 单文件 + npx skills add 一键装——sora 的技能体系就在这个标准上，生态成熟 = 可批量吸收外部技能。
3. **多 Agent 编排从 prompt 走向 spec**。OpenMAIC 的 choreography 单一事实源 + 纯解释器 + eslint 边界，是「防多 agent 行为漂移」的工程化答案，对 sora 的联合研究流水线有直接借鉴。
4. **本地优先继续爆发，但硬件是瓶颈**。VoiceStudio（全本地语音）、ECC（本地 harness）、magnitude（本地推理）——趋势明确；RTX4060 8GB/16GB 内存决定只能选轻量路径。
5. **甄别方法论的正面案例**：ECC 250k★ 初看可疑（知名度与星数不符），但 commit/contributors/releases/赞助页全真实——高星甄别流程正确拦截了误判，也证明「先查再判」比「看星数下结论」可靠。

## 💎 可借鉴点归纳

**技术层面**：
- archify「确定性编译 + validation receipt」→ sora 交付物（PPT/论文图/PCB 文件）附带校验证据，升级质量门禁为产物的一部分
- OpenMAIC「choreography 单一事实源 + 纯解释器」→ 多 agent 协作任务契约化，防各 agent 各自实现导致漂移
- scientific-agent-skills「技能库 CI 门禁（scan/tests/security/license）」→ sora 130+ 技能的入库自动化模板
- VoiceStudio「后端源码指纹握手」→ 墨题部署验证用指纹而非版本号判断新旧代码

**方法论层面**：
- ECC「Optimize the context window. Persist everything else.」→ 记忆分层原则再确认
- ECC「工程化心智预装（plan→test→implement→review→verify→remember→improve）」→ skill 体系本质是流程资产化
- Agent Skills 标准生态 → 技能即分发单元，跨 agent 复用

**可实操行动**：
- 🟢 试装 archify（`npx skills add tt-a1i/archify -g`），拿 1 个真实系统（如墨题架构）出图验证
- 🟢 抄 scientific-agent-skills 的 CI 门禁模式到 sora 技能库治理（skill-tests + scan）
- 🟡 评估 ECC 安装（先读安装文档，注意别叠加安装坑）
- 🟡 OpenMAIC 的 demo 看效果，编排 spec 思路记入 multi-agent-research
- 🟡 VoiceStudio 等硬件升级或非商用场景再试（AGPL + 显存）

## 文件操作清单

- ✅ 新建 5 篇笔记：`knowledge/Dev/archify-verifiable-diagrams-2026-09-06.md`、`knowledge/Dev/ecc-agent-harness-2026-09-06.md`、`knowledge/AI/scientific-agent-skills-library-2026-09-06.md`、`knowledge/AI/openmaic-multiagent-classroom-2026-09-06.md`、`knowledge/AI/voicestudio-local-voice-2026-09-06.md`
- ✅ 更新 `knowledge/knowledge-map.md`（W37 GitHub Trending 区块 + 头部日期）
- ✅ 补链 `knowledge/Research/MOC-GitHub.md`（W37 周报 + 周精选 5 项）
- ✅ 追加 `knowledge/Research/github-projects-tracking.csv`（5 个新项目行，带去重守卫；同日脚本快照 23 行共存不冲突）
- ✅ 自动脚本产物 `knowledge/Research/GitHub-Weekly-2026-09-06.md`（topic 口径 Top5，全部连榜）

---
_生成: github-trending-digest 周报 cron · k (Hermes) · 2026-09-06_
