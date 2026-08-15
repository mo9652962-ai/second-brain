---
tags: [周报, github trending, W33]
date: 2026-08-14
---

# GitHub 周报 — 2026-08-14（W33）

> 本周 GitHub Trending 全新面孔为主，Top5 与上周（nanobot/codebase-memory-mcp/chrome-devtools-mcp/TrendRadar/ruflo）**完全不同**。5 个精选项目已写独立笔记。

## 项目详情表
| # | 项目 | ★ | 本周Δ | 核心价值 | 入库笔记 |
|:--|:--|--:|--:|:--|:--|
| 1 | **PrimeIntellect-ai/prime-agent** | 15.7k | **+12,476** | 自改进 RLM agent：RLM + Continual Harness，与 Hermes memory/skills/cron/subagent 一一对应 | [[prime-agent-rlm-2026-08-14]] |
| 2 | **TencentCloud/TencentDB-Agent-Memory** | 21.5k | +5,388 | 记忆中枢四资产（Chat/Skill/Wiki/CodeGraph）——**已评估过**(08-05/08-08)，✅ 验证 sora 体系，只跟踪 delta | *(已入库，不新建，见 github-trending-2026-08-05)* |
| 3 | **addyosmani/agent-skills** | 87.1k | +4,562 | 生产级工程技能：四原则 + CI references/链接门禁 + 多 agent 单源 | [[agent-skills-addyosmani-2026-08-14]] |
| 4 | **semantica-agi/semantica** | 7.3k | +4,073 | 图原生 AI 基础设施：Context Graph + PROV-O provenance + 可审计决策 | [[semantica-graph-native-2026-08-14]] |
| 5 | **cloudflare/computer** | 8.1k | +3,599 | 给 agent 一台沙箱电脑（VFS + capnweb RPC，与 celld 联动）| [[cloudflare-computer-2026-08-14]] |
| — | **NVIDIA-NeMo/Switchyard** | 1.4k | +900 | LLM 模型路由网关（星少但命中 sora 多供应商配置痛点）| [[switchyard-llm-routing-2026-08-14]] |

## 本周洞察
1. **「长寿/自改进 agent」是主战场**：prime-agent（+12k）领跑本周，RLM + Continual Harness（可回滚的自改进）成为标准配方——与 sora 现有 skills 自举、cron、todo 高度同构，方向被大厂验证。
2. **Agent Skills 工程化爆发**：addyosmani(87k) + TencentDB 的 Skill 资产 + google/skills —— 「技能」从文档走向「可校验、可版本化、多 agent 单源」的生产级装配。
3. **可审计 AI / Context Engineering 升温**：semantica（图原生 + provenance）与上周 codebase-memory-mcp 呼应——存「意义」而非「嵌入」。
4. **多模型路由成标配**：Switchyard 的「统一协议 + 翻译层 + 路由算法」——可反哺 sora 的 9 provider fallback 链设计。
5. **Agent 云基础设施竞速**：Cloudflare(computer) × Deno(celld, +1.8k) 都押注「给 agent 可信电脑 + 分布式持久化」。

## 文件操作清单
- ✅ 新建 5 篇笔记：`knowledge/Dev/prime-agent-rlm-2026-08-14.md`、`knowledge/Dev/semantica-graph-native-2026-08-14.md`、`knowledge/Dev/agent-skills-addyosmani-2026-08-14.md`、`knowledge/Dev/switchyard-llm-routing-2026-08-14.md`、`knowledge/Dev/cloudflare-computer-2026-08-14.md`
- ✅ 更新 `knowledge/knowledge-map.md`（新增 W33 条目）
- ✅ 追加 `knowledge/Research/github-projects-tracking.csv`
- ⚠️ TencentDB-Agent-Memory **不新建笔记**（08-05/08-08 已深度评估，结论「验证体系/不迁移/只读参考」），仅跟踪 star delta：**12k → 21.5k（+9.5k，增速猛）**

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]