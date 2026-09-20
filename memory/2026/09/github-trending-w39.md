---
tags: [周报, GitHub Trending, W39]
date: 2026-09-20
---

# 🗞️ GitHub 周报 — W39（weekly 口径）

## 项目详情

| # | 项目 | ★ | 本周增长 | 核心价值 | 入库笔记 |
|:--|:--|--:|--:|:--|:--|
| 1 | Wei-Shaw/sub2api | 39.4k | 热榜 | 订阅配额→API Key 分发：token 计费+内置支付+多协议自适应 | [[knowledge/Dev/sub2api-api-gateway-2026-09-20]] |
| 2 | TheoLeeCJ/SemIf | 1.9k | 4天新库 | logits 直读决策概率：5x 提速零输出 token，Jev 开源复刻 | [[knowledge/AI/semif-logit-decisions-2026-09-20]] |
| 3 | Tencent/AI-Infra-Guard | 6.1k | +525 | AI 红队四层扫描：MCP/Skills/Agent/Infra + 越狱评估 | [[knowledge/Security/ai-infra-guard-2026-09-20]] |
| 4 | multica-ai/andrej-karpathy-skills | 205k | +21k | 单文件四原则治 LLM 编码通病（先想/极简/外科手术/目标驱动） | [[knowledge/Dev/karpathy-coding-guidelines-2026-09-20]] |
| 5 | alibaba/open-code-review | 21.3k | 增长 | 已在用：确定性+LLM 混合，~1/9 token，Delegation Mode | [[knowledge/Dev/open-code-review-2026-09-20]] |

## 可借鉴点归纳

**技术层面**
- 网关/计费：token 级计费 + 渠道倍率 + 分时定价，订阅配额分发是 2026 中转站商业模式（sub2api）
- 决策：小决策用 logits 概率直读代替让大模型写 JSON——零输出 token 5x 提速（SemIf）
- 安全：MCP/Skill 扫描分类法 MCP01-10 + 名称混淆/Rug Pull/工具阴影（A.I.G），装第三方技能前可扫
- 审查：确定性管线 + LLM 语义分离，行级定位 3 层策略 + 反思模块拦幻觉，~1/9 token（open-code-review）

**方法论层面**
- 行为约束单文件化：Karpathy 四原则可合并进任何 agent 的 CLAUDE.md/委派模板
- 「给成功标准而非指令」+ verify 检查点 = 编码 agent 独立循环的关键
- 宁缺毋滥的 Recall 取舍：垂直专用 agent（高 Precision）优于通用 agent（open-code-review）
- 可复现基准文化：timing/prompt hash/失败全入库，数字可重跑（SemIf）

**可实操行动**
1. Codex 委派模板并入 Karpathy 四原则（假设清单 + success criteria + verify 检查点 + 禁越界重构）
2. skill 安装门禁评估 A.I.G skill-scan（装前扫 SKILL.md vs 脚本一致性 + 高风险模式）
3. SemIf 范式参考：skill-pipeline 质检门/模型路由等高频小决策留作「logits 直读」候选（4060 贴边，可量化 GGUF 试跑）
4. sub2api 作中转商用功能清单对照（EasyCLIProxyAPI 升级路径）；计费倍率概念吸收进 ai-freelance-pricing
5. open-code-review Delegation Mode：委派 Codex 时用它自己的 LLM 审查，省 OCR API

## 文件操作清单

- 新建 5 篇项目笔记 + 1 篇周报详情（knowledge/Research/GitHub-Weekly-2026-09-20-weekly-5projects.md）
- 更新 MOC-GitHub（52→58 篇 + W39 区段）+ knowledge-map（W39 段）+ tracking CSV（5 行）
- 更新 ai-code-review skill（star 11K→21.3K + Delegation Mode）
- 更新 superpowers 吸收笔记 star（260k→276k）

---
*W39 · weekly 口径 · 2026-09-20 · 与脚本报告互补（脚本口径 Top5 连榜）*
