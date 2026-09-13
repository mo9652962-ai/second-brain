---
date: 2026-09-13
tags: [周报, API成本, Token用量, 存储, 运维监控]
aliases: [API成本周报W37, weekly-cost-report-2026W37]
status: adopted
---

# 本周 API 成本报告（W37）

> 统计周期：2026-09-07（周一）～ 2026-09-13（周日）
> 生成时间：2026-09-13 21:09
> ⚠️ 账面 estimated_cost_usd 本周严重失真（$14.0M），本报告成本一律采用**官方 CNY 价重算的真实口径**，记账问题详见「成本口径问题」节。

## 📊 核心指标

| 指标 | 本周 W37 | 上周 W36 | 变化 |
|:---|---:|---:|:---|
| 会话数 | 120 | 167 | -28.1% |
| API 调用 | 2,345 | 6,287 | -62.7% ⬇️ |
| 输入 Tokens | 28.55M | 62.92M | -54.6% |
| 输出 Tokens | 2.32M | 4.90M | -52.6% |
| 缓存读取 | 247.26M | 1,003.64M | -75.4% |
| 推理 Tokens | 1.33M | 2.29M | -41.9% |
| 缓存命中率 | 89.6% | 94.1% | -4.5pp |
| 消息数（本周） | 12,742 | - | - |
| **真实边际成本** | **¥6.51（≈$0.90）** | **¥116.55（≈$16.19）** | **-94.4% ⬇️** |
| 账面 estUSD（失真） | $14,021,151 | $4,286,609 | 不可比 ❌ |

## 🔑 三~四要点

1. **真实成本极低且大幅下降（-94%）**：本周边际成本 ¥6.51，几乎全部来自 jiyuanlvdong-2 relay（deepseek-v4-flash-0731）。主力流量走火山 coding plan（订阅制，不按量计费），边际≈0。
2. **用量整体回落**：调用量 -62.7%、输入 -54.6%、缓存 -75.4%——上周「查找之前连接的 MCP」桌面大会话（3,096 次调用 / 749M 缓存）本周停烧，是主因。
3. **火山 coding plan 晚高峰 5 小时额度打满**：09-11~09-13 每晚 20:00-21:00 档多个 cron 报 429（reset 窗口 09-11 20:46 / 09-13 22:02），fallback 到 jiyuanlvdong-2 兜底，个别环节仍 Connection error。
4. **成本记账 bug 恶化**：tokenrhythm relay 价格格式（input/output 为空）导致 jiyuanlvdong-2 账面成本被放大 ~10⁶ 倍（单会话账面 $2.97M，真实 ¥1.87）；fangzhou-1 的 pro 会话 cost_source='none' 仍记 $3.2M。账面数字不可信。

## 📅 每日明细（真实口径）

| 日期 | 会话 | 调用 | 输入(M) | 输出(M) | 缓存(M) | 账面estUSD(失真) |
|:---|---:|---:|---:|---:|---:|---:|
| 09-07 (一) | 17 | 343 | 2.99 | 0.27 | 23.32 | $1 |
| 09-08 (二) | 23 | 403 | 4.52 | 0.34 | 27.24 | $2 |
| 09-09 (三) | 13 | 227 | 3.16 | 0.20 | 13.40 | $0 |
| 09-10 (四) | 14 | 691 | 8.99 | 0.61 | 125.95 | $3,224,999 |
| 09-11 (五) | 13 | 88 | 1.07 | 0.11 | 6.27 | $2,091,028 |
| 09-12 (六) | 17 | 180 | 3.05 | 0.30 | 13.32 | $3,196,389 |
| 09-13 (日) | 23 | 413 | 4.77 | 0.48 | 37.76 | $5,508,731 |
| **总计** | **120** | **2,345** | **28.55** | **2.32** | **247.26** | $14.0M ❌ |

> 09-10 账面尖峰 = 「当前整体现状梳理」deepseek-v4-pro-260425 单会话（fangzhou-1）；09-12/09-13 尖峰 = jiyuanlvdong-2 价格格式 bug 放大（非真实费用）。

## 💰 成本分析（真实口径，CNY 官方价重算）

### 按 Provider

| Provider | 会话 | 调用 | 输入(M) | 输出(M) | 缓存(M) | 真实边际成本 |
|:---|---:|---:|---:|---:|---:|---:|
| custom（fangzhou-2 火山 coding plan） | 86 | 1,572 | 19.85 | 1.50 | 106.08 | ≈¥0（订阅） |
| custom:fangzhou-1（火山 coding plan） | 1 | 461 | 5.81 | 0.40 | 111.48 | ≈¥0（订阅） |
| custom:jiyuanlvdong-2（tokenrhythm relay） | 24 | 312 | 2.70 | 0.42 | 29.70 | **¥6.51** |
| NULL（no-agent/ping） | 9 | 0 | - | - | - | ¥0 |
| **总计** | **120** | **2,345** | **28.55** | **2.32** | **247.26** | **¥6.51 ≈ $0.90** |

jiyuanlvdong-2 来源拆分：cron ¥3.65（9 会话，fallback 兜底）/ desktop ¥2.91（15 会话）。

### 按模型

| 模型 | 会话 | 调用 | 输入(M) | 输出(M) | 缓存(M) | 真实成本 |
|:---|---:|---:|---:|---:|---:|---:|
| deepseek-v4-flash | 93 | 1,558 | 19.85 | 1.50 | 104.84 | ≈¥0（方舟订阅） |
| deepseek-v4-flash-0731 | 25 | ~316 | 2.89 | 0.42 | 30.94 | ¥6.51 |
| deepseek-v4-pro-260425 | 1 | 461 | 5.81 | 0.40 | 111.48 | ≈¥0（方舟订阅） |
| gemini-3.8-flash-high | 1 | 0 | - | - | - | 全部失败（8317 代理不可达）|

### Top 真实成本会话（本周，¥）

| 成本 | 调用 | 会话 | 时间 |
|---:|---:|:---|:---|
| ¥1.87 | 93 | daily-todo-executor · Sep 13 20:23（方舟 429 → fallback） | 09-13 20:00 |
| ¥0.61 | 32 | daily-todo-executor · Sep 11 20:17 | 09-11 20:01 |
| ¥0.33 | 17 | daily-monetization-review · Sep 13 18:04 | 09-13 18:00 |
| ¥0.32 | 18 | weekly-learning-progress · Sep 13 20:04 | 09-13 20:00 |
| ¥0.28 | 13 | Group: rmtvu0vl5-38vu5 | 09-11 02:00 |

## 🔁 跨周长会话

- 「查找之前连接的 MCP」（deepseek-v4-flash-0731 @ jiyuanlvdong-2）：08-31 起跑、09-10 13:46 最后活跃；生命周期 13,560 条消息中本周产生 6,918 条（51%）。**按 started_at 口径其成本记入上周（¥115.95 大头）**，本周真实成本估算未含其本周后段用量，实际边际可能略高于 ¥6.51。

## 🚨 异常与根因

### cron 执行（本周）

- 成功 794 / 失败 193 / running 1 / unknown 9 → 成功率 ~80%

| 失败根因 | 次数 | 说明 |
|:---|---:|:---|
| provider 连接错误 | 66 | jiyuanlvdong-2 (tokenrhythm) 间歇不可达（09-12 00:xx、09-13 20:20 等）；EasyCLIProxyAPI 127.0.0.1:8317 连不上（gemini-3.8-flash-high ×14，09-11~09-12）|
| HTTP 429 限流/配额 | 50 | 火山 coding plan 5 小时额度打满（reset 09-11 20:46 / 09-13 22:02），晚间 20:00/21:00 档多个 cron 受影响 → fallback jiyuanlvdong-2 |
| deterministic-verify 哨兵 | 35 | 每晚 21:30 报「无产物」（arxiv-fetch / obsidian-maintenance / daily-health-check），多为按需任务无产出 + Obsidian MCP 未开的已知模式 |
| config.yaml 损坏 | 7 | 09-11 21:00 ~ 09-12 12:21 窗口拒绝启动（C4 事件），**当前已恢复，yaml 校验 OK** |
| HTTP 402 余额不足 | 7 | 任务 pin 到余额枯竭的 jiyuanlvdong（非 -2）|
| drift 跳过（unpinned） | 7 | 全局模型漂移导致 unpinned 任务 fail-closed |
| Script not found | 5 | 脚本路径/改名问题 |
| HTTP 503 | 2 | 方舟鉴权/模型配置读取暂不可用（09-10 18:00）|
| 600s 超时 | 4 | 每日仓库+知识库优化 / graphify / health-check / arxiv |
| 504 / 400 模型已关闭 | 2 | 零星 |

### agent.log API 失败（本周 31 条 WARNING）

- 火山 5h 配额 429 ×13（傍晚档）、cpa-gui/gemini Connection error ×14、jiyuanlvdong-2 Connection/429 ×6。

## ⚠️ 成本口径问题（本周重点，账面不可信）

- state.db 本周账面 estimated_cost_usd = **$14.0M**（上周 $4.3M），全部失真，**严禁直接引用**。
- 根因：tokenrhythm relay 的 `/v1/models` 返回 `pricing` 中 **input/output 为空、只有 cache 价格（CNY）**；Hermes 的 `provider_models_api` 估算把单位/币种理解错 → jiyuanlvdong-2 会话成本放大 ~10⁶ 倍（例：daily-todo-executor 09-13 账面 $2.97M，真实 ¥1.87）。
- fangzhou-1 的 deepseek-v4-pro-260425 会话 cost_source='none'/status='unknown' 仍产出 $3.2M 账面值（火山 coding plan 订阅制无按量价，不应计费）。
- 另外 relay 对 deepseek-v4-flash-0731 的缓存价已从 ¥0.02/M（8 月）涨到 **¥0.1/M**（现价），成本估算已按 0.1 采用。
- 处理建议：将 jiyuanlvdong-2 / fangzhou 系加入「成本不可审计」白名单；修 cost estimator 解析标准 pricing 格式（P1）。

## 📦 存储使用

| 位置 | 大小 | 说明 |
|:---|---:|:---|
| C 盘 | 294G / 448G（66%，可用 154G）| 安全 |
| D 盘 | 593G / 932G（64%，可用 339G）| 安全 |
| Obsidian Vault | 678M | knowledge 5.3M / memory 2.5M / site 17M / .git 54M |
| Hermes 总目录 | 14.69G | 见下 |
| ├ hermes-agent | 9.08G | git 安装 + 依赖（大头） |
| ├ node | 2.1G | 内置 Node 运行时 |
| ├ state.db (+WAL) | 0.8G + 0.02G | 上周 710MB，+~15%；周内峰值曾 1.6G（VACUUM 回落） |
| ├ state-snapshots | 0.77G | 状态快照（可清旧） |
| ├ profiles / scripts / sessions | 0.42G / 0.36G / 0.29G | - |
| ├ bin / lsp / chrome-profile / skills | 0.21G / 0.2G / 0.15G / 0.14G | - |
| ├ backups / logs / cache | 0.09G / 0.03G / 0.02G | backups 可清 |

> 注：上周报告「Hermes ~900MB」为不完整口径（未含 hermes-agent 等），本周已补全实测；08-14 参考口径 11G → 现 14.7G（node 2.1G、state-snapshots 0.77G 为主要增量）。

## 💳 余额 / 配额

| 项 | 状态 |
|:---|:---|
| 火山方舟 coding plan（fangzhou-2 默认 / fangzhou-1）| 订阅制；晚高峰 5h 用量额度打满（09-11 20:46 / 09-13 22:02 reset），非余额问题 |
| jiyuanlvdong-2（tokenrhythm）| 可用，无公开余额端点；偶发 Connection error；cache 价 ¥0.1/M |
| jiyuanlvdong（非 -2）| 余额不足（本周 7 次 402）|
| sensenova | 未使用（上周 ¥0.60）|
| config.yaml | ✅ 当前解析正常（C4 已恢复）|

## 📌 洞察与建议

- **P0 错峰调度**：火山 coding plan 的 5h 用量额度在傍晚档打满，导致 20:00/21:00 档 cron（todo-executor / learning-progress / 组会报告 / 项目追踪等）成片 429 并 fallback 到高价 relay。建议把 20:00-21:30 的任务错峰到 22:30 后或早晨（参考 hermes-automation-patterns 错峰调度）。
- **P1 修成本记账**：tokenrhythm 价格格式导致 jiyuanlvdong-2 账面成本放大 ~10⁶ 倍 + fangzhou-1 无定价却记账——把这两家加入「成本不可审计」白名单，或修 cost estimator。
- **P1 排查 8317 本地代理**：gemini-3.8-flash-high 任务 09-11~09-12 连续 14 次 Connection error（EasyCLIProxyAPI 未起/不稳），若该任务仍需运行需拉起代理并验证。
- **P2 缓存命中率 89.6%**：健康（≥85%）但低于上周 94.1%——本周大量新会话/并行集群（09-12 夜间）带来冷缓存；无需处理。
- **P2 存储**：C 盘 154G 可用暂安全；Hermes 目录 14.7G 里 hermes-agent 9.1G + node 2.1G 为核心，backups(0.09G) 和 state-snapshots 旧快照可择机清理。
- **P2 哨兵误报**：deterministic-verify 本周 35 次失败多为「无产物」误报（按需任务 + Obsidian MCP 未开），保持 Known 模式处理，不升级。

---

*数据来源：Hermes state.db sessions/messages 表 + cron/executions.db + logs/agent.log；真实成本按官方/relay CNY 价重算（汇率 7.2），火山 coding plan 视为订阅制。*

---
> 🗺️ 属于 [[MOC-Productivity]] · [[Home|🏠 Home]]