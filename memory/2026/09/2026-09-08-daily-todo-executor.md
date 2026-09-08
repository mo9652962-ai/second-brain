---
tags: [daily-todo-executor, todo, cron]
created: 2026-09-08
type: daily-todo-executor
---

# ✅ 每日待办落实 · 2026-09-08（周二）

> 全库 `- [ ]` 扫描（排除 .git/.obsidian/skills/templates/system/.hermes/.learnings/.qoder/.github/.archive/dreaming）+ 分类 + 自动执行项落地。
> Freshness guard：今日 sibling crons 已跑（daily-review 13:22 / vault-suggestion-executor 10:18 / vault-maintenance 13:10 / health 13:18），中枢追踪器已更新；本执行器增量 = 探活 cron 落地 + 计数漂移修复 + 汇总报告。

---

## 📊 统计

| 指标 | 数值 |
|:-----|:-----|
| 含 `- [ ]` 文件数 | 87 |
| 待办行数（原始） | 337 |
| 真实可分类待办（排除模板/backlog） | ~15 |
| ✅ 本次自动执行 | **2**（探活 cron 落地 + 计数漂移修复） |
| ⏳ 需 sora 处理 | ~12 |
| 📋 模板/参考/backlog（不动） | ~320 行 |

---

## ✅ 已执行（2 项）

### 1. 🔴 外部生图/关键 API 周探活 cron 落地（reflection 09-07 行动项，已拖第 2 天）

reflection 09-07 明确要求「外部生图/关键 API 每周探活 cron → k **当场建**，不再等明日 P1」。今日实测确认其必要性：

| 服务 | 实测状态 | 判定 |
|:-----|:---------|:-----|
| XAI (grok-imagine) | HTTP 400 `Incorrect API key` | ❌ **key 失效，需重生成** |
| FAL (flux) | HTTP 403 `User is locked. Reason: TOP_UP` | ❌ **账户锁定，需充值** |
| SiliconFlow (vision/img/tts) | HTTP 200 | ✅ 正常 |
| DeepSeek 官方 | HTTP 200 | ✅ 正常 |
| EXA 搜索 | HTTP 200 | ✅ 正常 |

**落地物**：
- 脚本 `scripts/api_image_probe.sh`（副本在 `~/.hermes/scripts/`）——5 路最小调用，不打印 key，输出 markdown 报告到 `memory/YYYY/MM/YYYY-MM-DD-api-probe.md`
- cron `api-media-weekly-probe`（job `f3e0c5d8d2d0`，`15 10 * * 1` 每周一 10:15，`--no-agent` 纯脚本模式，`--deliver local`）——全健康时静默，有异常时输出报告全文提醒
- jobs.json 回读验证：`enabled=True`，`next_run_at=2026-09-14T10:15:00+08:00` ✅
- 首次探活报告：`memory/2026/09/2026-09-08-api-probe.md`

> 💡 这正好收口 memory 里的旧记录：**SiliconFlow key 已恢复**（实测 200，之前 401 疑已重生成）；XAI 失效 + FAL 锁定仍待 sora 处理。

### 2. 🔧 MEMORY.md 闲鱼计数漂移修复（第 38 天 → 第 39 天）

sibling cron 更新不对称复发：current.md 已 6 处一致「第 39 天」，MEMORY.md 待提升区仍残留「第 38 天」。已用 byte-level replace 对齐（`决策悬置第 38 天` → `决策悬置第 39 天`），验证命中。

---

## ⏳ 需 sora 处理（置顶）

### 🔴 P0
| 项 | 说明 | 阻塞点 |
|:---|:-----|:-------|
| **闲鱼试水决策** | 悬置第 39 天，k 侧 100% 就绪（素材 16 次核验 PASS + 操作清单两段式）；9/6 fallback 已过、9/7 触达升级已触发 | sora 一句话二选一（试水/放弃/再缓），30min 可逆 |
| **XAI key 重生成** | 探活实测 `Incorrect API key`（HTTP 400）——grok-imagine 生图主后端失效 | 控制台重生成 key 即可，无需改代码 |
| **FAL 充值解锁** | 探活实测 `TOP_UP`（HTTP 403）——flux 备用生图锁定 | 充值后自动恢复 |

### 🟡 P1/P2
| 项 | 说明 |
|:---|:-----|
| SiliconFlow key | ⚠️ 实测 200 正常，无需处理（若 401 记录陈旧可忽略） |
| 微信推送通道 | 需 serverchan/pushplus token 才可建「闲鱼决策微信提醒」，不建则维持现状 |
| 随身WiFi下单确认 | 赫电 Pro 399 元/年，选型已确认，阻塞 30+ 天 |
| 桌面美化部署 | TranslucentTB + Rainmeter 安装包已就绪，待 sora 执行 |
| 小红书「AI PPT 教程」 | 依赖 PPT 样例素材（portfolio/ 导出 + 水印） |
| 测评文发布 | 《小君AI测评》初稿已写，需选标题 + 配截图（8/17 遗留） |
| skill 合并授权 | skill-audit-09-01 三项（fangzhou-ark / android-automation / search-config 各 2 合 1）+ 09-08 审计 5 组近义合并（水墨 UI 4 合 1 等）——均为破坏性合并，需 sora 确认后执行 |

### ⏳ 依赖决策/待推进
- 墨题上云部署：服务器选型（腾讯 38/99 vs 阿里 99）+ 域名决策 → 之后 k 可全自动按方案部署
- AI 博主：B 站账号启用/注册、OBS 录屏配置、第 1 个视频选题
- 复现方案书 SummerCheckin：是否立项（agent 表/知识库/聊天室 3 模块）

---

## 📋 未改动（模板/参考/backlog，~320 行）

- `docs/WPS数学练习册标准化优化指南.md` — 质检清单（模板）
- `knowledge/Research/EVAL_PLAN.md` — 评估标准检查表（模板）
- `knowledge/Dev/cloudbase-learning-s1~s8.md` — 学习笔记实践清单（backlog，按单接单时用）
- `knowledge/Dev/墨题-P0/P1 设计稿` + `墨题上云部署方案` — 项目验收/部署 backlog
- `knowledge/Research/刷题机*千轮研究` + `多Agent协作增强v2.7` — 开发 backlog
- `knowledge/Research/接单工作流-SOP.md` / `论文Pipeline-数据契约.md` — SOP 流程清单
- `projects/ai-blogger/*` — 内容发布检查表 + 平台 setup 清单
- `outputs/xianyu-master/*` — 依赖闲鱼决策，不动
- `knowledge/cards/*` 行动项 — 多为条件触发/需 sora 决策（09-08 知识卡三项 = 明日 P0/P1，不重复执行）
- `knowledge/Research/skill-audit-2026-09-01.md` — 合并项待 sora 授权（见上）

---

## 💡 建议

1. **优先处理 P0 三件**：闲鱼拍板（30 秒）+ XAI key 重生成（2 分钟）+ FAL 充值（可选，备用）——都可在下周一探活 cron 首跑前搞定，届时报告全绿
2. SiliconFlow 视觉链实测健康，AI 图片技能可正常用（避开 XAI/FAL 即可）
3. skill 合并若要推进，说「确认合并」即执行（方案已备）；否则 09-15 月度审计时一并处理

---

_生成: daily-todo-executor cron · k (Hermes) · 2026-09-08_

---
> 🗺️ 属于 [[knowledge-map]] · [[Home|🏠 Home]]
