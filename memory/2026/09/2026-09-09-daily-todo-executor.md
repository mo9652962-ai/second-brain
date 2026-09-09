---
tags: [daily-todo-executor, todo, cron]
created: 2026-09-09
type: daily-todo-executor
---

# ✅ 每日待办落实 · 2026-09-09（周三）

> 全库 `- [ ]` 扫描（排除 .git/.obsidian/.venv/图片/二进制）+ 分类 + 自动执行项落地。
> 背景：本 cron 昨晚 network error，今晚重跑（daily-review 09-09 已注明）。sibling crons 已处理：vault-suggestion-executor（闲鱼第 40 天推进 + HOME 补链）、daily-review（arXiv/知识卡）、health、obsidian-maintenance——本执行器增量 = 评测意图泄露审计落地 + 知识卡闭环 + 内容草稿 + 汇总报告。

---

## 📊 统计

| 指标 | 数值 |
|:-----|:-----|
| 含 `- [ ]` 文件数 | **129** |
| 待办行数（原始匹配） | **465** |
| 真实可分类待办（排除模板/SOP/backlog/历史报告） | ~20 |
| ✅ 本次自动执行 | **3 项**（评测规范落地 + 2 卡闭环 + 内容草稿） |
| ⏳ 需 sora 处理（沿用 + 新增） | ~14 项 |
| 📋 模板/参考/backlog/条件触发（不动） | ~440 行 |

---

## ✅ 已执行（3 项）

### 1. 🧪 评测意图泄露审计 + 设计规范落地（09-09 eval-reactivity 卡两项行动项闭环）

arXiv 2609.05009 实证「评测框架本身污染评测结果」——对 k 自建评测资产做了全库审计：

| 评测/质检资产 | 盲评设计 | 意图泄露风险 | 处置 |
|:---|:---|:---|:---|
| shuorenhua 改写实跑（被测模型） | ✅ 匿名 B-xx / 乱序 / 无预期 / 禁自评 | ⚠️ **残留**：prompt 首句明示「benchmark 盲测改写实跑」「作为被测模型」——被测模型知道自己被测（partial exposure） | 登记专项修复（去框架化 + 重跑 benchmark），不仓促改 |
| shuorenhua 交叉判分（judge） | ✅ 盲测映射 + 硬指标脚本化 | 🟡 低（judge 身份明示属必要） | 保持 |
| ai-cmo evals / service-quality 质检门 | 输出断言/自查清单（非 LLM judge 被测） | ✅ 无泄露 | 保持 |
| knowledge-lint / vault 检查脚本 | 程序化检测 | ✅ 无 LLM judge | 保持 |

**落地物**：`knowledge/META/评测设计规范-意图隐藏-2026-09-09.md` —— ①被测侧意图隐藏硬规范 ②judge 侧注意 ③元数据规范（exposed/hidden/partial 三态 + 分层回测）④与 service-quality「评估器审计」互补关系。09-09 卡两项行动项已标记 `[x]`。

### 2. 🔁 09-08 heihe 卡复核闭环（2/3 项）

- ✅ **AI 营销技能库「质量断言」原语** → 实测 09-08 已落地（ai-cmo SKILL.md「核心原语 2：evals 质量断言」+「核心原语 1：product-marketing 上下文前置」），本次复核确认，卡标记 `[x]`
- ✅ **选型规则固化** → 已是 k 常驻基线（memory「评项目须实证」+ 09-08 研究方法论），无需再落地，卡标记 `[x]`
- ⏳ **深读 pascal/editor 31 个 MCP 工具** → 需专项研究会话，卡保持 `[ ]` 并注明

### 3. 🎬 评测反应性抖音脚本草稿（daily-review P2「k 可做 15min」）

`projects/ai-blogger/drafts/2026-09-09-AI会为了讨好你撒谎吗-抖音脚本.md` —— 标题三选一 + 前 3 秒钩子 + 60 秒分镜 + 封面/标签 + 发布前检查。数据源已核对（arXiv 2609.05009，N=12,800）。**未发布**，等 sora 审校。

---

## ⏳ 需 sora 处理（置顶，未改动原文件）

### 🔴 P0
| 项 | 说明 | 阻塞点 |
|:---|:-----|:-------|
| **闲鱼试水决策** | 悬置第 **40 天**；k 侧 100% 就绪（今日第 17 次素材核验 PASS）；「闲鱼提醒」cron 工作日 7:30 仍在触达 | 一句话二选一（试水/放弃/再缓），30min 可逆 |
| **XAI key 重生成** | 探活实测 `Incorrect API key`——grok-imagine 生图主后端失效 | 控制台重生成，2min |
| **FAL 充值解锁** | 探活实测 `TOP_UP` 403——flux 备用生图锁定 | 可选，充值自动恢复 |

### 🟡 P1/P2
| 项 | 说明 |
|:---|:-----|
| skill 合并授权 | 09-08 审计 5 组近义合并（水墨 UI 4 合 1 等）——破坏性，需确认后执行 |
| 微信推送通道 | 需 serverchan/pushplus token；不建则维持现有 cron 触达 |
| MCP 解除 | 打开 Obsidian → Local REST API → /mcp reconnect（1min） |
| 消息网关影响面定性 | FlClash 已重启核验 200 正常，仅剩降级定性一句话 |
| 随身WiFi下单 | 赫电 Pro 399 元/年，选型已确认，阻塞 30+ 天 |
| 桌面美化部署 | TranslucentTB + Rainmeter 安装包就绪 |
| 小红书「AI PPT 教程」 | 依赖 PPT 样例素材（portfolio 导出 + 水印） |
| 测评文发布 | 《小君AI测评》初稿已写，需选标题 + 配截图 |
| 零感 AI 付费实测 | 降 AI 率主推工具定标（1 元/千字） |
| DeepSeek/备用 provider 充值 | deepseek 官方/siliconflow 402，容灾深度减薄 |
| 抖音脚本草稿审校 | 新增：`projects/ai-blogger/drafts/` 三选一标题 + 口播语气 |

### ⏳ 依赖决策/专项会话
- 墨题上云部署（服务器选型 腾讯 38/99 vs 阿里 99 + 域名）→ 之后 k 可全自动
- AI 博主：B 站账号启用、OBS 录屏、第 1 个视频选题
- SummerCheckin 复现方案书：是否立项
- CAD MCP 深读（pascal/editor 31 工具）+ harness 论文 29 模式通读：需专项研究会话

---

## 📋 评估后放弃/暂缓（保持 `[ ]` 作条件触发器）

| 项 | 判定 |
|:---|:-----|
| knowledge-lint 加固（issue caps + severity） | 暂缓：已使用 3 次达触发器，但周检 13/13 PASS、库健康；卡片自述「优先级低，避免过度工程」→ 等周检报 NEEDS ATTENTION 再加固 |
| knowledge-lint 新检测项（stale_claim / uncited-claim） | 进 backlog，低优先，库健康不引入 |
| 记忆可移植性 3 项（09-07 卡） | 条件触发：换模型/升级 embedding 前执行 |
| harness 卡 2 项（论文通读 / ACP 跟进） | 需专项会话 + 对照 EasyCLIProxyAPI 路线评估 |
| shuorenhua 被测 prompt 去框架化 | 专项修复：需重跑 benchmark + 更新 results-v*（已登记在设计规范 §3） |

---

## 💡 建议

1. **P0 三件仍是主线**：闲鱼拍板（30s）+ XAI key（2min）+ FAL（可选）——下周一探活 cron 首跑前搞定即全绿
2. 评测反应性是「正在使用的东西被实证揭示缺陷」：规范已立，shuorenhua 修复等专项会话做（会改口径，值得但别在 cron 里仓促改）
3. 抖音草稿是现成的低摩擦内容弹药——sora 选个标题、顺一遍口播就能进发布流程

---

_生成: daily-todo-executor cron · k (Hermes) · 2026-09-09_

---
> 🗺️ 属于 [[knowledge-map]] · [[Home|🏠 Home]]
