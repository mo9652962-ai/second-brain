---
type: reflection
tags: [reflection, self-improvement, infrastructure, execution-gap]
created: 2026-08-21
subject: 2026-08-20
---

# 🔍 反思日记 - 2026-08-20（周四）

> 回顾对象：8 月 20 日（运行日 8-21 − 1 = 8-20）
> 主题：研究补跑日（HarnessRisk 直评 Hermes + Gartner 推理成本 5x + arXiv 池解锁）+「反思≠执行」第 4 次复发

## 📊 昨日概览（SQLite 全天实测）

| 维度 | 数值 |
|:-----|:-----|
| 会议/会话 | ~12 个会话（研究补跑批 + 各 cron） |
| 非 cron 用户消息 | **242 条**（活跃日） |
| web_search | **73 次** |
| web_extract | 3 次（4.1%）⚠️ 低于 15%，但当日走 arXiv API 直调（curl 全文本），属等效深度手段 |
| terminal / patch / write_file / read_file | 1291 / 375 / 174 / 275（重工具日） |
| skill_view / skill_manage | 28 / 28 |
| knowledge/ 新增 | ~9 篇 08-20 命名（卡片 Hermes-harnessrisk + Creative 2 + Research arXiv + Security 4 + 墨题/开源实证）+ Gartner/HarnessRisk 研究 |
| memory/ 新增 | 5 份（daily-summary / daily-review / daily-todo-executor / vault-suggestion-executor / health） |
| skills/ 更新 | **21 个 SKILL.md**（src-bug-hunting、vmp-reversing、novel-pipeline/worldbuilding、gemini-second-opinion、epm-offline-adapter 等） |
| .learnings LRN | LRN-20260820-001（Gartner 推理成本 5x 背书低成本架构） |

> 今日为「补跑日」（晨窗错过 13:24 并发补跑），文件 mtime 成簇（22:33 补跑 commit），按**文件名日期**归因，非 mtime。

---

## 🔄 上次反思（8-19）行动项核查

| # | 行动项 | 状态 | 证据 |
|:-:|:-------|:----:|:-----|
| 1 | **P0 语义缓存最小版，硬截止 8/22** | ❌ 未落地 | projects/current.md「8/20 反思行动项」仍 `- [ ]`；Tavily 8-20 **第 7 次**复发（Firecrawl 重试接管） |
| 2 | **P1 health_provider_check.py 余额阈值告警** | ❌ 未落地 | projects/current.md 仍 `- [ ]`；keylink 余额 ¥0.05 风险未收口 |
| 3 | **P1 SRC 侦察收敛（补天 1 有效漏洞）** | 🟡 部分推进 | guat.edu.cn POC 已提交，**漏洞盒子实名审核中**（有实质进展，非悬空） |
| 4 | scripts/ 登记表 | ✅ 已落地 | scripts/README.md 已建，8-20 更正 cache_hit_monitor「已删」误记，实现单一事实源 |

> 结论：语义缓存（第 20 天，截止 8/22 已到）与余额告警（第 2 轮）**仍未落地**——「反思≠执行」第 4 次复发（8/4、8/16、8/18、8/19）。SRC 方向首次有真实推进（guat POC 审核中）。scripts 登记表首次坚持住了（8/20 用它抓到一个误记并更正）。

---

## 🔧 三个可改进的点

### 1. 语义缓存 P0（截止 8/22）在 8-20 仍是「已注册未落地」——执行面缺的不是清单而是调度（最高优先）

**问题**：语义缓存最小版（同 query 24h 去重中间件，估时 30min）从 8/17 起反复登记，**今天 8/21 = 硬截止 8/22 的前一天仍未动手**；Tavily 配额已连续 **7 个工作日**复发（8-20 第 7 次，431→Firecrawl 兜底）。这不是「没想清楚」，是纯执行缺失。

**根因**：`projects/current.md` 的 `- [ ]` 待办只被 daily-todo-executor 扫出来当「提醒」，但**没有一条执行线负责「这个 K-可做、估时 30min 的项今天就跑掉」**——它和「需 sora 操作」的闲鱼项并列在同一列表里，无人区分「agent 可立即执行」与「需人工」。语义缓存纯属 agent 可独立完成的 30min 任务，却被无限期躺在注册表里。

**行动**：
- 🔴 **立即升级**：语义缓存从「项目待办」升为「**今日 key task**」，在 projects/current.md 标 🔴 今日截止（8/22），并作为本 cron 后最重要动作
- 🛠️ **长效机制（本次登记）**：分类体系升级——projects 待办按「agent 可执行 / 需 sora」分列，agent 可执行的带预估时长，daily-todo-executor 扫 `- [ ]` 时对 agent 可执行项**直接跑**而非只提醒（这是 8/4 起「反思≠执行」第 4 次复发的根治点）

### 2. 主 provider(fangzhou-2) 月度配额耗尽（HTTP 429，8/28 才重置）——单点依赖暴露容灾盲区（8-20 新爆点）

**问题**：8-20 配置链主 provider `fangzhou-2` 月度配额耗尽返回 HTTP 429，需等到 **8/28 才重置**，全靠 fallback 链（jiyuanlvdong/dengzhen）被动接管。这是当天爆出的**新风险**，且 daily-log 明确给了出路：「default 可切 deepseek 官方（436ms 最快）或 jiyuanlvdong，k 可做 10min」。

**根因**：缺省 provider 只配一个「月度配额制」入口，配额随月份归零时没有「到期前自动切换/预警」机制；多个 provider 都是「即时探测接管」而非「按已知配额状态预择」。

**行动**：
- ⏳ **K 可做 10min**：default 切到 deepseek 官方或 jiyuanlvdong（436ms 最快，实测最快），并登记 projects/current.md「今日可执行」
- ⏰ 8/28 到点提醒重新评估 fangzhou-2 恢复，避免长期依赖单点

### 3. health_provider_check.py 余额阈值告警——连续两轮登记未落地，最小可用版不该是空白

**问题**：余额告警是 8/19 反思登记（keylink ¥0.05 险裸奔 + jiyuanlvdong 504×3），8-20 仍 `- [ ]`。8-20 又补新风险（fangzhou-2 429/8/28 才重置）——余额/配额类预警的系统性缺失仍在。

**根根因**：预估「实现需逐家接 provider 余额 API」成本>此刻收益，这一搁就是两轮；但**「能 fetch 的 provider 先做 + fetch 失败标红」的最小版其实低风险可落地**，只是没有被排进去执行（同改进点#1的调度问题）。

**行动**：
- ⏳ 最小化版：health_provider_check.py 对 deepseek/jiyuanlvdong/tests 能查余额的先用现有储备/查询做阈值判断，余额 `<¥1` 或 fetch 失败 → 标红；不完全整体实现也远优于空白
- 📌 与改进点#1的「agent 可执行项调度」合并执行

---

## 📊 今日知识吸收检查（全天审计，非 daily-review 时点值）

| # | 检查项 | 8-20 情况 | 证据 |
|---:|:---|:---|:---|
| 1 | `knowledge/` 新增 | ✅ ~9 篇 08-20 命名 | 卡片 `hermes-harnessrisk-security` + Creative `AI小说工厂流水线`/`sumeru-skill-distillation` + Research `arxiv-2026-08-20` + Security `android-so-vmp-reversing`/`cyber-skills-817`/`vmp-reversing`/`网安自学避坑` + Dev 墨题巡检/开源实证 |
| 2 | `skills/` 更新 | ✅ 21 个 SKILL.md | src-bug-hunting、vmp-reversing、novel-pipeline、novel-worldbuilding、resilient-file-download、gemini-second-opinion、media-transcription、epm-offline-adapter 等（08-20 mtime 实测） |
| 3 | `memory/` 条目 | ✅ 5 份 + LRN-20260820-001 | daily-summary / daily-review / daily-todo-executor / vault-suggestion-executor / health；LRN 记 Gartner 5x 背书 |
| 4 | web_search 与成果 | ✅ 73 次 | 产出 HarnessRisk 直评 Hermes（⭐⭐⭐⭐⭐）、Gartner 推理成本 5x 背书、arXiv 池解锁（652→20 强）、VMP 逆向链路；web_extract 低（3 次）因 **arXiv 走 API 直调**（等效深度），按技能规则不减达标 |

**🏁 评分：✅ 达标**（4/4 全中，远超「任意 1 项」门槛；无需从快速吸收选项库补救）

> 知识吸收点评：HarnessRisk 首次公开评测 Hermes 直接给 sora 的生产组合打分（DeepSeek-V4-Pro ASR 65.4%/检测 34.6%，且 Config 阶段最脆弱），是全栈级资产；Gartner 推理成本 5x 背书「低成本架构=生存项」，主动出 LRN-20260820-001。「收藏即止」无；短板仍在**执行侧**（3 项待办未落地），而非吸收侧。

---

## Next（已登记 projects/current.md「🧭 8/21 反思行动项」）

1. 🔴 **语义缓存最小版（同 query 24h 去重中间件）——今日执行，截止 8/22 前必须落地**（Tavily 第 7 次复发 + 成本 5x 预防）
2. ⏳ **主 provider default 切换**（fangzhou-2 429 耗尽，切 deepseek 官方/jiyuanlvdong，k 可做 10min）
3. ⏳ **health_provider_check.py 余额阈值告警最小版**（先做能 fetch 的 + 失败标红，连续第 2 轮补齐）
4. 🔧 **agent 可执行项分类**：projects 待办分「agent 可执行/需 sora」，executor 对 agent 可执行项直接执行——根治「反思≠执行」第 4 复发

---

_生成: daily-reflection cron · k (Hermes) · 2026-08-21_
> 🗺️ 属于 [[knowledge-map]] · [[Home|🏠 Home]]