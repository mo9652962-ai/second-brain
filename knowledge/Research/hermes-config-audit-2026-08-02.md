---
tags: [hermes, audit, config, knowledge-accuracy]
created: 2026-08-02
status: report
---

# Hermes 配置知识准确性审计 (2026-08-02)

> 审计方法：读取实际 `AppData/Local/hermes/config.yaml`（8月1日 21:27 版）+ cron/jobs.json + .env，与知识库文档/技能文档逐项对比。
> 结论：**知识库核心配置文档（LLM-Providers.md）严重过时，技能文档存在 4 处明确错误，需人工更新 6 个文件。**

---

## 📊 实际配置快照（对比基准）

| 项目 | 实际值 |
|------|--------|
| model.default | `deepseek-v4-pro` / `custom:fangzhou-2` |
| default_model | `doubao-seed-2-0-pro` / `custom:fangzhou-1` |
| fallback 链 | 8 级：①opencode-go/deepseek-v4-pro → ②kimi-k3 → ③kimi-k2.7-code → ④qwen3.7-plus → ⑤glm-5.2 → ⑥siliconflow/Qwen3.5-4B → ⑦siliconflow/DeepSeek-V4-Pro → ⑧deepseek直连/deepseek-v4-flash |
| custom_providers | [0]opencode-go [1]siliconflow [2]kimi [3]fangzhou-2(ark-0984备) [4]fangzhou-1(ark-c1fd主) |
| auxiliary | vision/browser_screenshot=opencode-go/minimax-m3；其余 8 项全=fangzhou-2（doubao seed 系列） |
| model_aliases | pro/flash=fangzhou-2；glm/code/kimi/db/lite/mini/mini2=fangzhou-1 |
| smart_model_routing | enabled，cheap_model=fangzhou-2/deepseek-v4-flash |
| vision | doubao-vision-pro-32k-241028 / custom:fangzhou-1 |
| MCP | 6 个（code-review-graph/filesystem/github/jlcmcp/memvid/obsidian） |
| Cron | **28 个任务**（26 个 pin deepseek-v4-flash/deepseek 直连，2 个未指定） |
| 搜索 | .env 中 TAVILY/EXA/FIRECRAWL/SEARXNG 全有效 ✅ |
| Skills | skills_list 193 / filesystem 219 个 SKILL.md |

---

## ❌ 不一致清单（需人工更新）

### A. 知识库文档（knowledge/）

#### 1. `knowledge/AI/LLM-Providers.md` — 严重过时（updated 仍为 07-23）
| 文档写的 | 实际 | 影响 |
|---------|------|------|
| 主力模型 `deepseek-v4-flash` / opencode-go | `deepseek-v4-pro` / custom:fangzhou-2（default_model=doubao-seed-2-0-pro/fangzhou-1） | 主模型已切换为方舟，文档还停在 opencode-go 时代 |
| fallback 末级 `deepseek-chat` | `deepseek-v4-flash`（旧别名已退役） | 引用了已退役模型名 |
| Cron "18 个定时任务" | 28 个 | 数量翻倍未同步 |
| "93 Skills" | 193+ | 翻倍未同步 |
| 供应商仅 opencode-go/siliconflow/deepseek | 实际还有方舟双账户（fangzhou-1/fangzhou-2，已是主默认）+ Kimi 独立 provider | 缺失当前主力架构 |
| 环境变量列出 OPENROUTER_API_KEY | OpenRouter 07-26 已从 fallback 移除 | key 残留在 .env 未清理 |
| 未覆盖 | auxiliary 10 项、model_aliases 9 项、smart_model_routing、vision 块 | 文档缺整块新配置 |

#### 2. `knowledge/Tools/hermes-agent-ecosystem.md` — 轻微偏差
- "opencode-go | 主 provider（deepseek-v4-flash/pro）🟢 通过火山方舟" → **混淆**：opencode-go 是独立网关 `https://opencode.ai/zen/go/v1`，并非"通过火山方舟"；当前主默认已是方舟（fangzhou-1/2）
- "Cron 任务: 28 个" ✅ 正确，无需改

#### 3. `knowledge/AI/deepseek-v4-flash-0731-upgrade.md` — 基本准确
- "26 个 cron 任务已全部 pin 到 v4-flash" → 实际 28 个任务中 26 个 pin（2 个未指定模型）。建议改为"26/28"避免误读总任务数。

### B. 技能文档（skills/）

#### 4. `hermes/fangzhou-ark-setup/SKILL.md` — 明确错误
- model_aliases 示例：`pro`/`flash` 写 `custom:fangzhou-1` → 实际 config 是 **`custom:fangzhou-2`**（第 565-570 行）
- 其余 alias（glm/code/kimi/db/lite/mini/mini2）写 fangzhou-1 ✅ 一致

#### 5. `hermes-smart-model-router/SKILL.md` — 明确错误
- "主模型 `ark-code-latest`" → config 无此模型；且 `fangzhou-ark-config` 技能自己确认 ark-code-latest API 层 500 未部署
- "视觉模型 `doubao-vision-pro-128k`" → 实际 `doubao-vision-pro-32k-241028`
- auxiliary 建议全 `custom:fangzhou-1` → 实际全 `custom:fangzhou-2`（vision/browser_screenshot 为 opencode-go）
- "方舟 40+ 模型矩阵" → 实际模型列表 120+

#### 6. `hermes-model-strengths/SKILL.md` — 轻微偏差
- fallback 链第 ⑧ 级写 "kimi-k2.6 (OpenRouter)" → OpenRouter 已移除，实际末级 = deepseek-v4-flash 直连（8 级链，无 OpenRouter）
- "deepseek-v4-flash ← 主力（日常对话）" → config 默认是 deepseek-v4-pro/fangzhou-2（但 cron 26 任务用 flash，需注明双轨）

#### 7. `low-cost-model-guide/SKILL.md` — 轻微偏差
- "当前主力供应商 opencode-go + DeepSeek 直连 + OpenRouter 三路" → OpenRouter 已移除，应为"方舟 + opencode-go + siliconflow + DeepSeek 直连"

#### 8. `model-supplier-strategy/SKILL.md` — 轻微偏差（fallback 链✅）
- "主模型: 方舟 Coding Plan（第一账户）/ ark-code-latest（Auto模式）" → ark-code-latest 未部署；实际主默认 deepseek-v4-pro/fangzhou-2 + doubao-seed-2-0-pro/fangzhou-1
- fallback 链 ①-⑧ ✅ 与实际完全一致

### C. 一致项（无需处理）
- ✅ `hermes-model-configuration` — fallback 链末级 deepseek-v4-flash，正文正确
- ✅ `knowledge/Research/hermes-context-audit-2026-07-31.md` — MCP 6 个与 config 一致
- ✅ 记忆（memory）：双火山位置 custom_providers[3,4]、v4-flash 退役别名、Kimi 位置全部与 config 一致

---

## 📋 需要人工更新的文件清单（按优先级）

| 优先级 | 文件 | 改动内容 |
|:---:|------|---------|
| P0 | `knowledge/AI/LLM-Providers.md` | 全面重写：主力模型=方舟双账户、fallback 末级=v4-flash、cron=28、skills=193、补 auxiliary/aliases 章节 |
| P0 | `hermes/fangzhou-ark-setup/SKILL.md` | 第 87-88 行 alias pro/flash 改 `custom:fangzhou-2` |
| P1 | `hermes-smart-model-router/SKILL.md` | 主模型去掉 ark-code-latest、视觉模型改 doubao-vision-pro-32k-241028、auxiliary provider 改 fangzhou-2 |
| P1 | `knowledge/Tools/hermes-agent-ecosystem.md` | 修正 opencode-go"通过火山方舟"表述，标注当前主 provider=方舟 |
| P2 | `hermes-model-strengths/SKILL.md` | fallback ⑧ 级去掉 OpenRouter，改为 deepseek-v4-flash 直连 |
| P2 | `low-cost-model-guide/SKILL.md` | 去掉 OpenRouter 三路表述 |
| P2 | `model-supplier-strategy/SKILL.md` | 主模型行去掉 ark-code-latest，注明实际两个 default |
| P2 | `knowledge/AI/deepseek-v4-flash-0731-upgrade.md` | "26 个"改为"26/28 个 cron 任务" |

---

## 🔍 观察项（暂不处理）

1. `.env` 残留 `OPENROUTER_API_KEY` —— fallback 链已移除，key 可清理
2. `LEARNINGS.md` 提到"心跳模型 mimo-v2.5"，当前 config 无此模型（可能已废弃，历史记录保留即可）
3. model_aliases `mini`=minimax-m3 指向 fangzhou-1，但 fangzhou-1 models 列表无 minimax-m3（fangzhou-ark-setup 称 minimax 系可在方舟 chat_completions 用，待实测确认）
4. config.yaml 存在双 default 字段（`model.default` 与 `default_model`）指向不同 provider，属设计冗余（备用/心跳用），文档应注明

---

*2026-08-02 · 定时审计 · 对比基准 config.yaml 8/1 21:27 版*

---
> 🗺️ 属于 [[MOC-Research|🔬 研究笔记]] · [[knowledge-map|🗺️ 知识地图]]
