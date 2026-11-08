---
tags: [github, 周报, W45, weekly, trending]
date: 2026-11-08
source: trending?since=weekly + GitHub API 新建仓库 + README 实读
---

# 🗞️ GitHub 周榜 W45（weekly 口径）— 2026-11-08

> 与同日脚本口径 [[GitHub-Weekly-2026-11-08|W45 宝藏挖掘（topic 总 star 排序）]] 互补：**那份看「长期头部」，这份看「本周增速 + 新面孔」**，两口径互不覆盖。
> 采集：① `github.com/trending?since=weekly` 页面快照（18 项，含本周增速）② GitHub API 新建仓库（`created:>2026-10-25` 按 star 排序，30 项）③ 候选逐个 README 实读 ④ 5 个入选项目跑 commits / contributors / releases 核验。
> 距上期 weekly 报告 [[GitHub-Weekly-2026-09-20-weekly-5projects|W39]] 相隔 7 周（W40~W44 无 weekly 口径产出）。

## 本周精选 5 项（全部新入库）

| # | 项目 | ★ | 周Δ / 建仓天数 | 领域 | 核心价值 | 入库笔记 |
|:--|:--|--:|--:|:--|:--|:--|
| 1 | **KKKKhazix/agent-autoloop** | 4.0k | 5 天建仓 | Agent 自动化中台 | 事件驱动 + 挂起零消耗 + 指令数据分离 + TTL 熔断，1,850 行零依赖内核 | [[knowledge/Dev/agent-autoloop-2026-11-08]] |
| 2 | **thedotmack/claude-mem** | 114.6k | +7,482/周 | Agent 记忆 | 第二 agent 旁听记笔记 + 三级检索（索引→时间线→详情）省 ~10x token | [[knowledge/AI/claude-mem-2026-11-08]] |
| 3 | **deepseek-ai/dsh-superagent-prototype** | 20.9k | 8 天建仓 | Agent 架构 | Router/Worker 两层 + 注意力经济学 + 可计算授权表 | [[knowledge/AI/dsh-superagent-2026-11-08]] |
| 4 | **Verlintas/NOIR** | 3.0k | 8 天建仓 | 安全/隐私 | adb 审 Android：权限 × 上报端点 → 数据流向 + 可回滚处置 | [[knowledge/Security/noir-android-privacy-audit-2026-11-08]] |
| 5 | **max-sixty/worktrunk** | 12.0k | +2,292/周 | 开发工具 | git worktree 做成「并行 agent 工位」，hooks + CoW 构建缓存 | [[knowledge/Dev/worktrunk-2026-11-08]] |

**外加一篇方法论笔记**：[[knowledge/AI/super-agent-attention-architecture-2026-11-08]] — 把 dsh 的注意力经济学 + agent-autoloop 的内核四机制合成一套可落地的 Hermes cron 约束（P0 三条本周可做）。

## 连榜 / 跟踪（不新建笔记）

| 项目 | 本周 ★ | 周Δ | 结论出处 | 本期处理 |
|:--|--:|--:|:--|:--|
| mattpocock/skills | 317.9k | +9,664 | [[knowledge/Dev/mattpocock-skills]] | 只跟踪 |
| obra/superpowers | 314.2k | +4,466 | [[knowledge/Dev/superpowers-grounded-copy-absorbed]] | 只跟踪（框架型，方向对但本机不装） |
| anthropics/skills | 188.9k | +2,796 | MOC-GitHub 生态位 | 只跟踪 |
| github/spec-kit | 148.5k | +4,280 | 未评估 | 跟踪（SDD 流程，与写码前扫坑可对照） |
| **D4Vinci/Scrapling** | 99.4k | +8,712 | CSV 已有 4 次快照（72.1k→99.4k） | 只跟踪；本周增速全榜第二，抓取类需求可回看 |
| **pbakaus/impeccable** | 105.7k | +7,623 | [[GitHub热榜-2026-08-08]]（已实测刷题机，v2.107-109） | 只跟踪；已进开发流程「CSS 改动后跑 detect」 |
| Nutlope/hallmark | 50.4k | +6,624 | [[knowledge/Hardware/hallmark]]（18.2k 时已 adopted） | 只跟踪；star 翻近 3 倍 |
| vercel-labs/agent-browser | 47.0k | +1,476 | 本机已有 agent-browser skill | 只跟踪 |
| The-PR-Agent/pr-agent | 15.5k | +1,576 | 未评估 | 跟踪（PR 审查，与 open-code-review 同赛道） |
| shiyu-coder/Kronos | 47.3k | +2,937 | 未评估 | 跟踪（金融时序基础模型，非当前方向） |
| pingdotgg/t3code | 51.5k | +17,100（本周增速第一） | 未评估 | 仅记录：增速异常高，未核验，不进候选 |

## 新面孔观察名单（未入选，留档）

| 项目 | ★ | 为什么不选 |
|:--|--:|:--|
| storytold/craft-anything | 21.2k | 「看懂任何软件 → 让 AI 造一个自己的版本」，early alpha；21k★/8 天但 290 open issues，且**克隆他人产品的合规边界模糊**，不适合作为方法论来源 |
| heydamir/unslop | 11.5k | 反 vibecoded UI 的 Claude skill——与已 adopted 的 hallmark / impeccable 高度重叠 |
| wangzan101/Mika | 7.6k | 端侧 Android agent，与 sora 当前「不碰真机自动化外的东西」边界不符；先观察 |
| paipiange/nvzhuang / anhao/ai-pose-gallery-zh | 2.3k / 6.4k | 图集类，与工作流无关 |

## 🔍 真实性核验（本期实测，不是引用旧结论）

| 项目 | commits | contributors | releases | 判定 |
|:--|--:|--:|:--|:--|
| claude-mem | 4,023 | 359 | v15.12.0（11-07） | ✅ 真实，工程完整 |
| agent-autoloop | 154 | 24 | v1.6.4（11-08） | ✅ 真实（5 天 154 commits，高频迭代） |
| worktrunk | 5,511 | 89 | v0.81.0（10-20） | ✅ 真实，11 个月持续 |
| NOIR | 48 | 3 | v0.4.2（11-07） | ⚠️ 真实但早期（3 人团队，v0.x） |
| **dsh-superagent-prototype** | **1** | **1** | 无 | ⚠️ **高星低成熟**：20.9k★ / 1 commit / 37KB，star 来自 DeepSeek 品牌 + 11-01 的文章，**代码是研究原型，价值在 docs/** |

> 甄别口径：star 只触发「要查」，判定看 commits + contributors + releases + 生态。本周 dsh 正是「star 数不能当质量」的教科书案例——同一批里 4.0k★ 的 agent-autoloop 反而代码量是它的 30 倍。

## 本周趋势信号

1. **「人的注意力」正式成为 agent 系统的设计约束**。DeepSeek 文章把这句写成第一原则（一个人只能盯 3~5 个会话），agent-autoloop 用「挂起零消耗 + 卡片审批」把它工程化，claude-mem 用「分层索引」把它搬到上下文侧。三个不同项目、同一个优化目标——**这是本周最强信号**。
2. **并行 agent 的三块基础设施凑齐了**：调度（Router/Worker）、状态（事件溯源内核）、工作区隔离（worktree）。谁先把这三块拼起来，谁就能真的同时跑 5 个任务。
3. **prompt injection 的防线从「提示词」下沉到「架构」**：agent-autoloop 的指令数据分离（外部文字只进文件、不进提示词、事件带 `cwd/agent/access` 直接拒收）比任何「请忽略恶意指令」的 system prompt 都硬。**今天 AGENTS.md 被注入检测拦截，正好是这条的现实注脚。**
4. **中文项目在 Agent 基建层开始有话语权**：agent-autoloop（中文优先 + 飞书/钉钉/企微通道）、NOIR（中文文档 + 国产厂商识别库）都不是「中文翻译版」，而是原生按国内工作流设计。
5. **开源客户端的 open-core 变现继续成熟**：claude-mem 免费试用托管 observer → 到期回落自有额度 → 可选自带 key / 团队版。与 sub2api（W39）同一条路：**客户端开源、服务收费**。

## 文件操作清单

- 新建 5 篇项目笔记：`knowledge/Dev/agent-autoloop-2026-11-08.md`、`knowledge/AI/claude-mem-2026-11-08.md`、`knowledge/AI/dsh-superagent-2026-11-08.md`、`knowledge/Security/noir-android-privacy-audit-2026-11-08.md`、`knowledge/Dev/worktrunk-2026-11-08.md`
- 新建 1 篇方法论：`knowledge/AI/super-agent-attention-architecture-2026-11-08.md`
- 周报：本篇 + `memory/2026/11/github-trending-w45.md`（摘要）
- 更新：`knowledge/Research/MOC-GitHub.md`、`knowledge/knowledge-map.md`、`knowledge/Research/github-projects-tracking.csv`（追加 5 行，带去重守卫）
- 与同日脚本报告互引：[[GitHub-Weekly-2026-11-08]]

## 可落地行动（本周）

| 优先级 | 行动 | 依据 |
|:--|:--|:--|
| P0 | cron 输出加「注意力三问」，无新增一律 `[SILENT]` | dsh philosophy |
| P0 | 外部文本先落盘，prompt 只放路径 + 元数据 | agent-autoloop 指令数据分离 |
| P0 | 委派深度上限 3 层 | agent-autoloop TTL 熔断 |
| P1 | 检索分两跳（先索引后详情），长任务上下文 Inline & Spill | claude-mem + dsh |
| P1 | 多任务并行时用 `git worktree` 开独立工位 | worktrunk |
| P2 | 用 NOIR 只读扫一次 iQOO，看报告质量 | NOIR |

---
*W45 · weekly 口径 · 2026-11-08 · 数据源：trending 页面快照 + GitHub API + README 实读 + commits/contributors/releases 实测*
