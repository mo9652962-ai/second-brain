---
date: 2026-08-23
tags: [周报, API成本, Token用量, 存储, 运维监控]
aliases: [API成本周报W34, weekly-cost-report-2026W34]
status: adopted
---

# API 成本周报 W34（2026.08.17 - 08.23）

## 结论速览

| 指标 | 本周 W34 | 上周 W33 | 变动 |
|:---|:---:|:---:|:---:|
| 会话数 | 92 | 106 | −13% |
| API 调用 | 3,487 | 8,084 | −57% |
| Input tokens | 18.1M | 75.3M | −76% |
| Output tokens | 2.0M | 4.1M | −51% |
| Cache read tokens | 655M | 1.83B | −64% |
| **核算成本 estUSD** | **$92.98** | **$273.12** | **−66%** |
| 其中 CNY 虚高 ~¥21.90 | $21.90 实为 ¥21.90 ≈ $3.1 | — | — |
| 修正后实际成本 | ~$73.08 | ~$100.3 | −27% |

> **结论：本周成本大幅下降（-66% raw / -27% 修正），主要原因是上周的高成本会话「日常问候与闲聊」($202.92) 已结束，且 glm-5.2 高价兜底模型未再触发。但 $71.07 的 desktop 桌面会话（ox-alpha）值得关注——单日烧掉 76% 的周成本。**

---

## 本周要点

1. **成本结构从「chat 对话」转向「desktop 桌面使用」**：上周成本大头是日常聊天会话（$202.92，deepseek 长会话劣化导致上下文膨胀），本周成本大头是「dsh桌面端检查与更新」桌面会话（$71.07，stealth/ox-alpha 11.5M input + 916K output）。桌面会话单次 2068 调用就烧了 $71。
2. **Ox-alpha 存在 rate-limit 瓶颈**：8/23 出现 84 次 429 速率限制，上下文压缩被阻塞，每次等待 120s+，导致 cron 延迟和重试堆积。
3. **Tokenrhythm 中转站 8/22-23 不稳定**：errors.log 出现大量 503/504（1051+1578 行），导致多个 cron 重试失败（周失败 167/993 次=17%）。
4. **CNY 计价虚高问题仍存在**：jiyuanlvdong/dengzhen 的 $21.90 实为 CNY，修正后实际成本少 ~$18.80。

---

## 按日分布

| 日期 | 会话 | 调用 | Input | Output | 成本 |
|:---|:---:|:---:|:---:|:---:|:---:|
| 08-17 Mon | 16 | 134 | 1.5M | 105K | $1.72 |
| 08-18 Tue | 13 | 252 | 848K | 171K | $0.94 |
| 08-19 Wed | 13 | 178 | 988K | 135K | $2.24 |
| 08-20 Thu | 13 | 225 | 857K | 143K | $3.70 |
| 08-21 Fri | 12 | 239 | 943K | 182K | $5.12 |
| 08-22 Sat | **6** | **2,177** | **11.9M** | **1.0M** | **$73.10** 🔥 |
| 08-23 Sun | 19 | 285 | 1.2M | 239K | $6.20 |

> 8/22 单日 $73.10（占周 79%），几乎全部来自桌面 dsh 会话。

---

## 按模型

| 模型 | 会话 | 调用 | Input | Output | Cache Read | 成本 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **stealth/ox-alpha** | 1 | 2,066 | 11.5M | 916K | 551M | **$71.07** 🔥 |
| deepseek-v4-flash-0731 | 47 | 801 | 2.8M | 674K | 61M | $13.03 ⚠️CNY |
| deepseek-v4-flash | 44 | 620 | 3.9M | 382K | 43M | $8.87 ⚠️CNY |

> ⚠️ 后两者经 tokenrhythm 中转，成本实为 CNY 标记为 USD，CNY 修正后分别约 ¥13.03 ≈ $1.86 和 ¥8.87 ≈ $1.27。

---

## 按来源

| 来源 | 会话 | 调用 | 成本 |
|:---|:---:|:---:|:---:|
| **cron** | 91 | 1,422 | **$21.96** |
| **desktop** | 1 | 2,068 | **$71.07** 🔥 |

> desktop 只有 1 个会话但占 76% 成本。cron 91 个会话合计 $21.96。

---

## 按供应商

| Provider | 会话 | 调用 | Input | Output | 成本 |
|:---|:---:|:---:|:---:|:---:|:---:|
| **custom:openrouter** | 1 | 2,068 | 11.5M | 917K | **$71.07** ✅ real USD |
| custom: （tokenrhythm） | 38 | 801 | 2.8M | 674K | $13.03 ⚠️ CNY |
| custom:jiyuanlvdong | 39 | 522 | 3.5M | 322K | $8.87 ⚠️ CNY |
| deepseek | 1 | 69 | 129K | 45K | $0.05 ✅ real USD |
| custom:keylink | 2 | 20 | 207K | 14K | $0.00 |
| custom:sensenova | 2 | 10 | 82K | 2K | $0.00 |

---

## Top 成本会话

| 成本 | 模型 | 调用 | Input | Output | 会话标题 |
|:---:|:---|:---:|:---:|:---:|:---|
| **$71.07** | stealth/ox-alpha | 2,068 | 11.5M | 917K | dsh桌面端检查与更新 |
| $2.30 | deepseek-v4-flash | 83 | 181K | 45K | daily-todo-executor · 08/21 |
| $1.72 | deepseek-v4-flash-0731 | 60 | 229K | 74K | arxiv-fetch · 08/21 |
| $1.71 | deepseek-v4-flash-0731 | 62 | 125K | 55K | weekly-knowledge-consolidation |
| $0.89 | deepseek-v4-flash-0731 | 40 | 43K | 48K | daily-todo-executor · 08/23 |
| $0.85 | deepseek-v4-flash | 23 | 326K | 12K | weekly-learning-progress · 08/23 |
| $0.83 | deepseek-v4-flash-0731 | 24 | 136K | 20K | arxiv-summarize · 08/23 |
| $0.80 | deepseek-v4-flash-0731 | 52 | 176K | 38K | obsidian-maintenance · 08/19 |

> 第一名的 $71.07 是板上钉钉的 real USD（OpenRouter）。其余为 CNY 中转载体。

---

## 跨周长会话

| 标题 | 模型 | 成本 | 时间范围 |
|:---|:---|:---:|:---|
| 日常问候与闲聊 | deepseek-v4-flash-0731 | $202.92（全生命周期） | 08/15 01:10 ~ 08/21 23:58 |

> 该会话上周启动，本周至 08/21 仍在活跃（本周约 40% 的消息量）。其全生命周期成本 $202.92 上周已计入大部分，本周残余贡献已被 started_at 聚合排除。按 messages 估算本周消息占比 ~40%，但无额外计费数据。

---

## 异常与根因

| 问题 | 影响 | 根因 | 时间 |
|:---|:---|:---|:---|
| **429 Rate-limit**（84 次） | ox-alpha 上下文压缩阻塞，cron 延迟 | OpenRouter upstream stealth/ox-alpha 共享池限流 | 8/23 ≥20:55 |
| **503 风暴**（1,051+1,578 行） | 多个 cron 重试 3 次失败 | tokenrhythm.studio 中转站不稳定 | 8/22-8/23 |
| **504 Gateway Time-out**（30 次） | 同 503，cron 重试失败 | tokenrhythm 中转站不稳定 | 8/23 21:00+ |
| Cromwell 168 次失败 | 17% 执行失败率 | 主要由上述 503/504 导致 | 全周 |

> 429 当前仍在持续（8/23 20:55 起）。建议：在 OpenRouter 绑定自己的 provider key 以绕过共享池限流，或增加 fallback 模型。

---

## 成本口径问题

| 问题 | 涉及 | 本周金额 | 说明 |
|:---|:---|:---:|:---|
| **CNY 记成 USD** | tokenrhythm/jiyuanlvdong | $21.90 | 实为 ¥21.90 ≈ $3.1，虚高 ~7× |
| 修正后实际成本 | — | **~$73.08** | $71.07(OpenRouter)+$0.05(deepseek)+$3.1(CNY修正)+$0.86(其他) |

---

## 存储容量

| 位置 | 大小 | 备注 |
|:---|:---:|:---|
| **C: 盘**（448GB） | 已用 242G / 54% | |
| **D: 盘**（932GB） | 已用 570G / 62% | |
| **Hermes 总目录** | **10.47 GB** | |
| ├ hermes-agent | 9.67 GB | 含 models ~4.7G, 工具链, 运行时 |
| ├ state.db | 515 MB | 会话数据库 |
| ├ backups | 90 MB | 可清理 |
| ├ logs | 18 MB | |
| ├ cron | 4.3 MB | |
| └ audio_cache | 0 | |
| **Obsidian 仓库** | **703 MB** | |
| ├ .git | 48 MB | |
| ├ projects | 8.7 MB | |
| ├ knowledge | 3.6 MB | |
| └ memory | 2.6 MB | |

---

## 洞察与建议

### P0 — 立即

- **OpenRouter ox-alpha 429 降级**：当前 8/23 20:55 起持续限流，context_compressor 被阻塞。建议绑定自己的 provider key（OpenRouter 设置 → 添加 provider key），或配置 fallback 模型链。

### P1 — 本周

- **Desktop 会话成本预警**：$71.07 的单桌面会话说明大模型桌面交互有成本失控风险（ox-alpha 1M ctx + 2068 次调用 = $71）。建议对 desktop 会话设置 token 预算上限，或考虑将复杂任务拆分。
- **Tokenrhythm 中转站不稳定**：8/22-23 的 503/504 风暴导致 167 次 cron 失败。建议将 jiyuanlvdong 降级为备用，或增加更多中转站冗余。

### P2 — 持续优化

- **Backups 清理**：90MB 可定期清理（`backups/` 目录保留最近 3 份即可）。
- **CNY 口径修正**：tokenrhythm/jy 的 $21.90 成本虚高问题持续存在，不影响实际支出但干扰成本分析。修正后实际成本 ~$73/周，月均 ~$300。
- **models 目录**：9.67GB 的 hermes-agent 中 models 约 4.7G，如空间紧张可清理不常用的模型。

---

## 余额

> 本周未执行余额探测（需要 API key）。建议下周补充各供应商余额状态。

---
> 🗺️ 属于 [[MOC-Productivity]] · [[Home|🏠 Home]]
