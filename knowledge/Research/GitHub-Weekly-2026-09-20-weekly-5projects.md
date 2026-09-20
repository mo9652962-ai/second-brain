---
tags: [GitHub, 周报, W39, weekly]
date: 2026-09-20
source: trending+web_search 综合
---

# 🗞️ GitHub 周榜 W39（weekly 口径）— 2026-09-20

> 与脚本口径 Top5（topic 总 star 排序）互补；本周 GitHub API 断连（HTTP:000），数据来自 trending 页面快照 + web_search 多源交叉验证。

## 本周精选 5 项（全部新入库）

| # | 项目 | ★ | 周Δ | 领域 | 核心价值 | 入库笔记 |
|:--|:--|--:|--:|:--|:--|:--|
| 1 | **Wei-Shaw/sub2api** | 39.4k | 热榜中 | API 网关/变现 | 订阅配额→API Key 分发：token 计费+内置支付+多协议自适应，中转站商用范本 | [[knowledge/Dev/sub2api-api-gateway-2026-09-20]] |
| 2 | **TheoLeeCJ/SemIf** | 1.9k | 4 天新库 | AI 决策范式 | 从 logits 直读决策概率不走文本生成：21 标准 1.02s vs 5.33s，5 倍提速零输出 token | [[knowledge/AI/semif-logit-decisions-2026-09-20]] |
| 3 | **Tencent/AI-Infra-Guard** | 6.1k | +525 | AI 安全 | 腾讯朱雀 AI 红队：MCP/Skills/Agent/Infra 四层扫描 + 越狱评估 + Crescendo/TAP 红队 | [[knowledge/Security/ai-infra-guard-2026-09-20]] |
| 4 | **multica-ai/andrej-karpathy-skills** | 205k | +21k | 编码规范 | 单文件 CLAUDE.md 四原则（先想/极简/外科手术/目标驱动）治 LLM 编码通病 | [[knowledge/Dev/karpathy-coding-guidelines-2026-09-20]] |
| 5 | **alibaba/open-code-review** | 21.3k | 增长中 | 代码审查 | 已在用工具的深度补全：确定性+LLM 混合架构，~1/9 token，Delegation Mode | [[knowledge/Dev/open-code-review-2026-09-20]] |

## 连榜/跟踪（不新建笔记）

- **ECC** 250.2k→242.3k（+36.7k/周，W37 已评估，AgentShield 安全方向与 A.I.G 呼应）
- **obra/superpowers** 276.3k（+24.7k/周；07-27 已吸收「grounded-copy」，结论不装——框架型项目，star 增长验证的是方向非本项目）
- **mattpocock/skills** 232.5k（+19.8k/周；已有 mattpocock-methodology/skills 吸收）
- **openai/codex** 114.0k（+17.4k/周；日常在用工具，本期仅跟踪）
- **anthropics/claude-code** 142.6k（+22.8k/周；日常在用，跟踪）
- **n8n-io/n8n** 201.9k（+60.3k/周；工作流自动化老牌，无方法论新启发，跟踪）

## 本周趋势信号

1. **订阅配额经济升温**：sub2api 全年霸榜（2026-02-28 首次 #1，至今 39.4k★），「把订阅拆成 API 卖」成 2026 真实商业模式——与 sora 的反代/中转基建（EasyCLIProxyAPI/WorkBuddy 反代）直接同赛道。
2. **「决策不走文本生成」新范式**：Jev（闭源 TypeSafe）→ SemIf（开源复刻）→ jev-ultrafast（browser-use 应用）：小决策用 logits 概率而非让大模型写 JSON。本周多项目同信号，值得跟踪。
3. **AI 安全体检工具化**：Tencent A.I.G（MCP/Skills 扫描）+ ECC AgentShield + cloudflare/security-audit-skill（trendshift 周榜）——AI 供应链（MCP/技能）安全成为厂商押注点，与 sora 外部 skills 安装场景强相关。
4. **编码 agent 行为约束成为刚需**：karpathy-skills 205k★ 单文件四原则——「给成功标准而非指令」成共识，验证文化（OverclaimBench/完成声明核验）与此同源。
5. **专用 agent 跑赢通用 agent**：open-code-review 确定性+LLM 混合（~1/9 token、更高 Precision）——垂直工具化是 agent 应用效率方向。

## 文件操作清单

- 新建 5 篇项目笔记（Dev×3 / AI×1 / Security×1）
- 周报：[[GitHub-Weekly-2026-09-20-weekly-5projects]] + memory/2026/09/github-trending-w39.md
- 更新：MOC-GitHub + knowledge-map（W39 段）+ tracking CSV + ai-code-review skill（star 11K→21.3K）
- 可借鉴点落地：① Codex 委派模板并入 Karpathy 四原则 ② skill 安装门禁评估 skill-scan ③ SemIf 作为「决策不走生成」范式参考（4060 贴边）④ sub2api 作为中转商用的功能清单对照

---
*W39 · weekly 口径 · 2026-09-20 · GitHub API 断连日，数据经多源交叉验证*
