---
tags: [Dev, Agent, harness, Codex, Claude-Code, 安全, GitHub-Trending, W37]
aliases: [ECC, agent-harness, 多Agent工具箱]
date: 2026-09-06
source: https://github.com/affaan-m/ECC
domain: Dev
status: active
---

# ECC — 多 Agent Harness 性能优化系统

**250.2k★（本周 +5,445，周榜总星第一）** · "The agent harness performance optimization system"——给 Agent 预装一整套「协调的工程系统与工具箱」：先计划再构建、用测试验证改动、换新上下文自审、记住重要的事、把重复胜利固化成可复用技能与工作流。

MIT · 2,631 commits · 354 contributors · 16 releases · 2026-01-18→02-07 首 4 万星（爆发式增长）。

## 核心特征

- **核心循环**：`plan → test → implement → review → verify → remember → improve`
- **"Optimize the context window. Persist everything else."**——上下文窗口省着用，其余全部持久化。
- **内容规模**：68 agents（计划/评审/构建修复/安全/架构/领域）+ 286 skills（TDD/研究/安全/docs/前端/数据/ML/运维）+ 94 命令 shim + hooks/rules/memory/continuous learning。
- **AgentShield 安全扫描**：扫 prompts、hooks、MCP 配置、权限、secrets、agent 文件——安全内建。
- **多 harness 支持**：Claude Code 最佳、Codex 有官方同步路径、Cursor/OpenCode/Gemini/Zed/GitHub Copilot/Antigravity/Qwen 为能力受限适配器；还带 CodeBuddy(Tencent) 安装适配。
- **一键安装**：`npx ecc-universal install --guided`，一次审阅流程配好 Claude Code + Codex + Kimi Code。
- **坑位明确**："Do not stack install methods"——同一 harness 装两次会重复 skills/commands/hooks/配置；多个 harness 各装一次没问题。有 Reset/Uninstall 流程。

## 技术架构（文字图）

```
npx ecc-universal install --guided
        │  (Claude Code / Codex / Kimi Code 一次审阅装好)
        ▼
┌─────────────────────────────────────────────┐
│  ECC 工具箱（per harness）                     │
│  ├─ 68 agents   (plan/review/repair/sec/arch)│
│  ├─ 286 skills  (TDD/research/security/...)  │
│  ├─ 94 commands (skills-first 过渡期)         │
│  ├─ hooks + memory + continuous learning      │
│  ├─ rules      (按语言/项目选择性常驻)         │
│  └─ AgentShield (prompts/hooks/MCP/密钥扫描)  │
└─────────────────────────────────────────────┘
```

## 💎 可借鉴点（⭐ 核心价值）

1. **「工程化心智预装」思路**。ECC 把 `plan→test→implement→review→verify→remember→improve` 循环装进每个 agent，而不是每次 prompt 重写一遍——正是 sora 把 skill 体系预装进 Hermes 的规模化版本。验证了「把流程固化为资产」是 agent 生产力的正解。
2. **"Optimize context window, persist everything else"** = sora 记忆分层（memory-crystal / 四级记忆）的同款原则，可对照 ECC 的 memory 实现补强。
3. **AgentShield 安全扫描对照**。sora 有 hermes-codex-security-gate（凭据 BLOCKED / 验证 L0-4 / MAX_STEPS），ECC 的扫描面（prompts/hooks/MCP 配置/权限/密钥/agent 文件）是现成的检查清单，可补全自家门禁。
4. **多 harness 并存 vs 不叠加安装**。sora 用 Codex + Claude + Antigravity + DeepSeek Harness 多 agent——「每 harness 各装一次、别叠加」的坑直接适用，避免重复 skill/hook 污染。
5. **254k★ 生态信号**：agent 工具链（harness 增强层）是 2026 最热赛道，与 sora 的 multi-agent-infra / EasyCLIProxyAPI 方向一致。

## 安装/验证

```bash
npx ecc-universal setup        # Claude Code 配置
npx ecc-universal install --guided   # 一次配多个 harness
# 已有 Claude/Codex 环境的注意：先确认无旧安装再装，避免叠加
```

## 总结评价

| 维度 | 评分 | 说明 |
|:--|:--|:--|
| 技术含金量 | ★★★★★ | 68 agents/286 skills/安全扫描，工程与生态兼备 |
| 关联度 | ★★★★★ | 直接覆盖 sora 的多 agent 工具链（Codex/Claude/Antigravity） |
| 可迁移性 | ★★★★ | 循环范式/记忆原则/安全清单可搬；整体安装需评估侵入性 |
| 热度 | ★★★★★ | 250k★ 周榜第一 |
| 值得安装 | 🟡 谨慎评估 | 功能强但侵入 agent 配置，先读安装文档再决定；低风险（MIT） |

> 🗺️ 属于 [[MOC-Dev]] · [[MOC-GitHub]] · [[HOME|🏠 Home]]
> 📅 周报见 [[../../memory/2026/09/github-trending-w37|W37 周报]]
