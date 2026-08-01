# Hermes Agent 健康检查报告

**生成时间：** 2026-08-01 14:40 (GMT+8)
**执行方式：** cron 自动巡检 (daily-health-check)

---

## 📊 整体状态：🔴 需要关注（fallback 链部分失效，存在可用通道）

**核心问题：** 当前默认 provider `custom:fangzhou-1`（deepseek-v4-pro）**火山方舟周配额已耗尽**（HTTP 429 AccountQuotaExceeded，8/3 00:00 自动重置）；fallback 链中的 opencode-go（401 余额不足）与 SiliconFlow（402 余额不足）也不可用。**但 DeepSeek 官方 API 与 fangzhou-2 备用账户实测可用**，系统未完全中断。

---

## 🔑 1. API Key 连通性实测（2026-08-01 14:35 实测）

| Provider | Key | 状态 | 详情 |
|----------|-----|------|------|
| DeepSeek 官方 (deepseek-v4-flash) | DEEPSEEK_API_KEY | ✅ 200 | 正常，响应 0.7s |
| fangzhou-2 火山方舟 (deepseek-v4-pro) | ark-0984… | ✅ 200 | 正常，1.0s |
| fangzhou-2 (doubao-seed-2-0-mini) | ark-0984… | ✅ 200 | 正常，4.4s |
| Kimi (kimi-k2.7-code) | moonshot | ✅ 200 | 正常 |
| Tavily / Exa / Firecrawl | 搜索三后端 | ✅ 200 | 全部正常 |
| **fangzhou-1 火山方舟（当前默认）** | ark-c1fd… | ❌ **429** | **AccountQuotaExceeded 周配额耗尽**，8/3 00:00 重置 |
| **opencode-go** | OPENCODE_GO_API_KEY | ❌ **401** | **余额不足**，需充值 (opencode.ai/workspace/…/billing) |
| **SiliconFlow** | SILICONFLOW_API_KEY | ❌ **402** | **余额不足**（已知问题） |

---

## ⏰ 2. Cron 任务状态（14 个任务）

| 任务 | 调度 | 上次运行 | 状态 |
|------|------|----------|------|
| obsidian-github-sync | 每2小时 | 08-01 14:00 | ✅ ok |
| weekly-knowledge-consolidation | 周日 12:15 | 07-26 13:45 | ✅ ok |
| arxiv-summarize | 周日 13:00 | 07-31 13:24 | ✅ ok |
| 项目追踪 | 每日 21:00 | 07-31 21:07 | ✅ ok |
| 闲鱼提醒 | 工作日 07:30 | 07-31 13:37 | ✅ ok |
| obsidian-maintenance | 每日 06:00 | — | ⏳ 待运行 |
| 组会报告 | 周日 20:00 | — | ⏳ 待运行 |
| 文献周报 | 周一 07:00 | — | ⏳ 待运行 |
| GitHub 宝藏挖掘 | 周日 12:30 | — | ⏳ 待运行 |
| 提醒安装 Lyricify | 一次性 08-02 09:00 | — | ⏳ 待运行 |
| **arxiv-fetch** | 每日 07:00 | 08-01 07:00 | ❌ **429 配额超限** |
| **daily-health-check** | 每日 08:15 | 08-01 08:15 | ❌ **429 配额超限** |
| **daily-self-improvement** | 每日 08:30 | 08-01 08:30 | ❌ **429 配额超限** |
| **hackernews-daily** | 每日 07:00 | 08-01 07:00 | ❌ **429 配额超限** |
| **biweekly-skill-audit** | 每月1/15日 | 08-01 12:30 | ❌ **配置漂移保护跳过**（provider deepseek→custom，model deepseek-v4-flash→deepseek-v4-pro，未 pin） |

**429 失败根因：** 这些任务运行在默认模型链上（fangzhou-1 / deepseek-v4-pro），方舟周配额耗尽后直接失败；fallback 到 opencode-go（401）与 SiliconFlow（402）同样失败。

---

## 🔗 3. Gateway 状态

| 项目 | 状态 |
|------|------|
| Gateway 进程 | ✅ 运行中 (PID 29316) |
| 微信平台 | ✅ connected |
| QQBot 平台 | ✅ connected |
| Hermes 桌面进程 | ✅ 运行中（主进程 778MB + 若干 node/python 子进程） |
| 会话存储 | ✅ 正常读写 |

---

## 📀 4. 磁盘空间

| 项目 | 值 | 状态 |
|------|-----|------|
| C: 总容量 | 448 GB | — |
| 已使用 | 173 GB (39%) | ✅ 健康 |
| 可用 | **275 GB** | ✅ 充足 |

---

## 💾 5. 内存 & CPU

| 项目 | 值 | 状态 |
|------|-----|------|
| 总内存 | 15.6 GB | — |
| 已使用 | 12.2 GB (78.2%) | ⚠️ 偏高（Windows 常规水平） |
| 可用 | 3.4 GB | ⚠️ 偏紧 |
| CPU 负载 | 0% | ✅ 空闲 |
| 系统运行时间 | 1.1 天 | ✅ |

---

## 🚨 问题汇总（按优先级）

1. **🔴 P0：fangzhou-1 火山方舟周配额耗尽（429）** — 当前默认模型不可用，导致每日 4 个 cron 失败。8/3 00:00 自动恢复，或立即切换到 fangzhou-2 备用账户。
2. **🔴 P0：opencode-go 余额不足（401）** — fallback 链第 1-5 项全部失效。需在 opencode.ai 充值。
3. **🟡 P1：SiliconFlow 余额不足（402）** — fallback 链第 6-7 项失效。需充值或忽略（已有 DeepSeek 官方兜底）。
4. **🟡 P1：biweekly-skill-audit 配置漂移** — 全局配置从 deepseek 漂移到 custom:fangzhou-1 后任务被保护机制跳过。需 pin 任务配置。
5. **🟢 P2：内存可用仅 3.4GB** — 15.6GB 机器已用 78%，长期偏高建议清理后台进程。

---

## ✅ 建议操作

```bash
# 方案 A（推荐）：立即将默认模型切到 fangzhou-2 备用账户（实测 200 可用）
hermes config set model.default deepseek-v4-pro
hermes config set model.provider custom:fangzhou-2

# 方案 B：切到 DeepSeek 官方（实测 200 可用）
hermes config set model.default deepseek-v4-flash
hermes config set model.provider deepseek

# 方案 C：8/3 00:00 配额自动重置后无需操作，期间 cron 会继续报 429

# 修复 biweekly-skill-audit 配置漂移（pin 到当前配置）
hermes cron update 1b7f96681587 provider=custom:fangzhou-1 model=deepseek-v4-pro
# 或 pin 回原值：provider=deepseek model=deepseek-v4-flash
```

**备用：** 充值 opencode-go (https://opencode.ai/workspace/wrk_01KVTQMGT5Z2DQ2S1CWQJJ65QA/billing) 恢复主 fallback 链。

---

## 📝 附注

- 本报告由 cron 自动生成，已存档：`health/HEALTH_REPORT-2026-08-01.md`
- 实测脚本留存：`scripts/api_health_test.sh`（可复用做 API 连通性巡检）、`scripts/health_check.ps1`
- 当前 cron 会话本身运行于 deepseek 官方 provider，说明 DeepSeek 兜底通道工作正常

*报告由 Hermes Agent 自动生成*
