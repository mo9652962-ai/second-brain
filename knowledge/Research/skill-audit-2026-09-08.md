---
tags: [skill-audit]
---

# 月度技能使用统计与审计 (2026-09-08)

> 口径：技能使用数据来自 `~/AppData/Local/hermes/skills/.usage.json`（use_count 为累计值）。「本月使用」= last_used_at / last_viewed_at 落在 2026-09-01 ~ 09-08。TOP 排名 = 本月使用过的技能按累计 use_count 降序。

## 📊 概览
- 技能总量（.usage.json 登记）: 392
- 本月（9/1-9/8）实际使用过: 97 个
- state=stale 技能: 79 个（含 bundled 遗产技能，多数正常）
- 从未使用（use+view=0）: 98 个（含大量 bundled/导入遗产技能）

## 🏆 本月最常用 TOP 10
| # | 技能 | 累计 use_count | 本月最后使用 |
|---|------|------|------|
| 1 | hermes-automation-patterns | 290 | 09-08 |
| 2 | daily-knowledge-review | 219 | 09-08 |
| 3 | obsidian-vault-management | 201 | 09-08 |
| 4 | knowledge-graph-chunk-extraction | 145 | 09-06 |
| 5 | english-practice-machine-dev | 129 | 09-07 |
| 6 | knowledge-absorption | 101 | 09-06 |
| 7 | obsidian | 99 | 09-08 |
| 8 | arxiv-weekly-digest | 77 | 09-08 |
| 9 | daily-knowledge-absorption-gate | 72 | 09-08 |
| 10 | english-practice-machine | 71 | 09-07 |

> 特征：前 3 名 + 6/7/9 名全是 cron 日常链路（知识吸收→回顾→obsidian 落地），墨题（english-practice-machine 两枚）与 arxiv 周报也在高频区。结论：日常 cron 自举闭环运转良好，主战场 = 知识管理 + 墨题产品。

## 🔍 需要更新的技能（内容过时，命中已知陷阱）

### P0 — 同时命中 3+ 类过时标记（模型别名/搜索降级/退役路由，改配置时会带偏）
| 技能 | 命中 |
|------|------|
| hermes-configuration-patterns | openrouter + tavily + ark-code-latest + deepseek-chat |
| hermes-model-configuration | openrouter + tavily + deepseek-chat |
| hermes/ai-api-provider-evaluation | siliconflow + tavily + deepseek-chat + openrouter |
| software-development/hermes-model-fallback | openrouter + siliconflow |

### P1 — 命中 2 类
| 技能 | 命中 |
|------|------|
| hermes-provider-matrix | openrouter + ark-code-latest |
| hermes-smart-model-router | ark-code-latest + siliconflow |
| hermes-search-config | tavily + siliconflow |
| model-supplier-strategy | openrouter + ark-code-latest |
| model-capability-reference | openrouter + doubao-seed-2.0-pro |
| software-development/ai-code-review | deepseek-chat + siliconflow |
| security/ai-agent-security-audit | openrouter + siliconflow + tavily |
| ai-image-generation | openrouter + siliconflow |
| hermes/hermes-health-check | openrouter + siliconflow |

### P2 — 命中 1 类（高频/常驻技能优先处理）
- **hermes/daily-knowledge-review**（use=219）— tavily
- **knowledge-graph-chunk-extraction**（use=145）— tavily
- **ppt-design-2026** — tavily
- **productivity/vault-todo-cleanup** — tavily
- **hermes/deepseek-api-clients** — deepseek-chat/reasoner
- **hermes/fangzhou-ark-setup** — doubao-seed-2.0-pro
- **productivity/primary-math-daily-practice** — ark-code-latest
- **hermes-model-routing-implementation** — openrouter
- **development/multi-end-ai-provider-config** — openrouter
- **low-cost-model-guide** — openrouter
- **cad/freecad-automation** — openrouter
- **ai-automated-photoshop / edtech/epm-ai-feature-rollout / gaming/godot-ai-game-dev** — siliconflow
- **productivity/hermes-web-search-config** — tavily（与 hermes-search-config 重复）
- **autonomous-ai-agents/hermes-agent** — openrouter（需甄别：可能是文档引用非推荐）

### 甄别后「正常，不需改」
- research/web-search-fallbacks — 故意含 Tavily 作备选阶梯，符合 9/2 搜索链决策
- hermes/skill-library-audit — 记录陷阱清单本身
- research/ai-api-relay-evaluation — 以 OpenRouter 为研究对象
- @axdlee/siliconflow-media（hub，不可自动改）— 主推 SiliconFlow，但 **key 已失效 401** → 需用户控制台重生成或标记废弃

## 🗂️ 建议归档（项目已结束 / 长期未用，by=agent）
| 技能 | use | 最后使用 | 理由 |
|------|-----|---------|------|
| sims4-mod-development | 98 | 08-05 | Sims4 联机启动器项目已交付，整族停用 |
| sims-4-modding-multiplayer | 39 | 08-05 | 同上 |
| sims4-mp-launcher-dev | 4 | 08-05 | 同上 |
| comfyui-troubleshooting | 23 | 08-03 | 生图已转云端，本地部署已标 [已退役] |
| comfyui | 6 | 08-01 | 同上（本体） |
| android-automation | 3 | 07-31 | 与 uiautomator2-android-automation 近义重复 |
| 5plus-app-packaging | 0 | 从未 | 与 uniapp-multiplatform-publish / hbuilderx 重复 |
| miniapp-reversing-audit | 0 | 从未 | 与 wechat-miniapp-reversing / wxapkg 重复 |
| spa-frontend-cache-updates | 0 | 从未 | 与 development/frontend-deploy-cache 重复 |
| web-text-annotation | 0 | 从未 | 与 web-text-annotation-feature 重复 |
| video-editing-jianying | 0 | 从未 | 剪映教程，8/14 建后未用 |

## 🔀 建议合并（近义重复，待 sora 确认）
- **水墨 UI 家族**（4 个）：chinese-aesthetic-web-ui / chinese-ink-wash-ui / ink-wash-ui-theming / ink-wash-web-ui-theming → 并成 1 个
- **移动端布局调试**（2 个）：mobile-web-layout-debugging / mobile-webview-layout-debugging → 并成 1 个
- **搜索配置**（2 个）：hermes-search-config / productivity/hermes-web-search-config → 并成 1 个
- **教育课题申报**（2 个，9/7 新建）：education-research-proposal / education-research-proposal-writing → 并成 1 个
- **数学练习家族**（4 个）：math-worksheet-generation / educational-worksheet-generator / primary-math-daily-practice / xiaoshengchu-math-practice → 建议统一入口（家教需求持续，勿删，仅整合）

## 📋 建议操作
1. **patch P0/P1/P2**：agent-created 可自动改；`created_by=None` 的技能（如 hermes-model-configuration 若为 None）需先 `hermes curator adopt <name>` 才能后台自动维护
2. **归档**：sims4 三件套 + comfyui 两件 + 4 个零使用重复技能 → 移入 .archive（参考 references/skill-merge-workflow.md）
3. **合并**：上述 5 组近义重复 → 需 sora 确认后执行（skill 规则：不自主合并/删除）
4. **SiliconFlow key**：siliconflow-media 等 23 个技能引用 SiliconFlow，主 key 已失效 → sora 控制台重生成后自动恢复，无需改技能

## 执行记录
- 仅统计与识别，未自动 patch / 归档 / 合并（cron 后台阶段 + 待 sora 确认）

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
