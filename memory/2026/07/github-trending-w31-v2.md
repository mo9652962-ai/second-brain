---
tags: [absorbed, weekly-trending, evaluation]
date: 2026-07-27
---

# W31 GitHub 热榜 · 研究与应用评估

> 来源：GitHub Trending Weekly · 2026-07-27

---

## 📊 评估矩阵

| 项目 | ⭐ | 本周 | 评估 | 结论 |
|:-----|:-:|:----:|:-----|:-----|
| **ai-agent-book** | 20k | +16.6k | ✅ 已下载，优先读 Ch2/Ch4/Ch5 | **adopted** |
| **code-review-graph** | 26k | +6.4k | 代码图谱MCP，理念与codebase-memory-mcp一致 | **backlog** |
| **jcode** ➡️ **abandoned** (12k★) | Rust agent harness | Smart App Control 封杀，放弃安装 |
| **pi-web** | 2.8k | +1.5k | pi coding agent 的 Web UI，已有 Hermes 桌面端 | **watch** |
| **OmniRoute** | 30k | +11k | 290+ providers + token压缩，已有8级fallback | **watch** |
| **kimi-code** | 5k | +1.5k | 月之暗面 coding agent CLI，竞品参考 | **watch** |

## 🔬 jcode 深入研究

**核心数据**（2026-07 实测对比）：
| 指标 | jcode | Claude Code | Codex CLI |
|:-----|:-----:|:-----------:|:---------:|
| RAM (1 session) | **27.8 MB** | 386.6 MB | 140 MB |
| RAM (10 sessions) | **117 MB** | 2,300 MB | 335 MB |
| 启动速度 | **14 ms** | 3,437 ms | 883 ms |
| 语言 | Rust | Python | TypeScript |

**关键特性**：
- 语义记忆图（类似知识图谱）
- 同仓库 Swarm 协调（多Agent协作）
- 40+ provider 支持
- Claude Code MCP 导入兼容
- Lazy skill loading

**对我们**：
- 可以在 Hermes 旁边跑轻量 Rust agent 做特定任务
- 但 Hermes + opencode-go 已经够用
- **标记为 trial**：资源不紧张时再试

## 下周关注

- **andrewyng/openworker** — Andrew Ng，README 还没写
- **open-seo** — SEO开源替代，如有自建站需求再用
