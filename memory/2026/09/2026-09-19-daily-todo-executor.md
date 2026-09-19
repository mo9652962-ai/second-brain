# 2026-09-19 每日待办执行报告

> 执行者：k (Hermes daily-todo-executor cron) ｜ 执行时间：2026-09-19 20:0x
> 今日 sibling cron 已先行：`2026-09-19-daily-review.md` + `2026-09-19-weekly-todo-cleanup.md`（weekly 已归档 Section 11 / 48 项，current.md 已更新）→ 本轮以**验证 + 新鲜项执行 + 汇总**为主。

## 📊 统计

| 指标 | 数值 |
|:---|:---|
| 扫描文件（含 `- [ ]`，全 vault） | 178 |
| 排除系统/归档/模板后待分类文件 | 49 |
| 待办行总数（排除后） | 248 |
| 今日新执行 ✅ | 1 |
| 需 sora 处理（报告列出） | ~12 组 |
| 模板/参考/开发 backlog（不改动） | 绝大多数 |

## ✅ 已执行

| 项 | 落点 | 说明 |
|:---|:---|:---|
| 墨题 SQLite 慢查询体检（09-17 卡片 P2） | `knowledge/cards/2026-09-17-ai-query-plan-optimization.md:35` | question_bank.db（10MB，vocabulary_entries 7958 行为最大表）12 条常见访问路径 EXPLAIN QUERY PLAN 全走索引（idx_vocab_user_term / idx_vocab_translation_queue / idx_questions_unit / idx_answers_session / idx_answer_events_question 等），**无缺失索引**；仅 3 条排序查询 USE TEMP B-TREE（8k 行量级可忽略）。app.db / vocabulary.db 为空库（0KB）未体检 |

## ⏳ 需你处理

### 🔴 P0 级
- **ZCode 卸载链（今日卡片 09-19，🔴 P0）**：`knowledge/cards/2026-09-19-zcode-silent-upload.md:42` —— 退出 ZCode 登录 → 卸载 ZCode（已不用，Codex 替代）→ 删除 `~/.zcode` 剩余快照（含墨题 126MB 加密快照 + 默认工作区已上传）→ 墨题 git 历史轮换敏感信息。证据链完整（本机 `~/.zcode` 存在、checkpoints 2 个 workspace），处置路径清晰。其中「git 历史轮换」可在你确认后由 k 代做。
- **万悟参赛确认**（9/25 12:00 截止，剩 6 天）：确认后 k 当天出《商业计划书/对策方案》初稿；9/21 前未确认 → wsl --shutdown 夜间窗口自动执行。

### 🟡 决策悬置
- **闲鱼试水决策**（第 42 天，周一 9/21 复盘，state.yaml 权威）：30 秒三选一（试水/放弃/再缓）；k 侧 100% 就绪，上架 30min 可逆。
- **卡片 cron 排程评估**（9/18 反思 🟢）：卡片 cron 12:33 跑时当日研究零产出 → 后移 22:00+ 或 prompt 加「候选池为空显式标记待补」；时序规则已 patch daily-knowledge-review，**改 jobs.json 需授权**。
- **ZCode 防御可选**（若暂不卸载才执行）：`icacls "C:\Users\31954\.zcode\v2\checkpoints" /deny 31954:(W)` 锁目录——若走 P0 卸载则此防御不需要。

### 🧩 内容/素材待拍板
- 抖音脚本《AI 会为了讨好你撒谎吗》（09-09 draft）：选标题三选一 + 口播语气改顺 + 数据配图生成（SiliconFlow Qwen-image 可用）。
- B 站初稿《Agent 操作系统之争》（08-23）：审校选标题 + 录屏素材 + 配图 4-5 张 + 发布平台决策。
- ai-blogger：B 站账号启用/注册、主页信息、OBS 配置（README/strategy 多项）。
- 闲鱼素材补全（L2 重做清单）：PPT 商品案例样张图 ×2、练习册商品主图、每商品描述 ≥200 字含 1 案例；搭网站写脚本商品决策（与 PPT 上架同批拍板）。

### 🔒 依赖/条件触发（旧卡片，已标注，无需行动）
- 零感 AI 付费实测（1 元/千字，需你付费+测试稿）→ 实测通过后写闲鱼 SOP。
- S4MP 跨网真机验证（需两台真机+公网）。
- 深读研究项 ×6（OverclaimBench 20812/19425/19759、harness 29 模式、pascal/editor 31 MCP、desert-ant CLI、GitHub 变现候选评估、AIRI 立项）→ ⏳ 需专项研究会话，保持 open 已标注。
- 换模型/升级条件触发项（记忆可移植性抽查、RAG embedding 版本备份）。

## 📋 未改动（模板/参考/开发 backlog）

- **模板**：content-template.md 发布前后检查项、tools-setup 检查清单、research/通用笔记模板、system/GitHub-Treasure-Hunt 格式示例。
- **QA 检查清单（文档内容非任务）**：docs/WPS 数学练习册标准化优化指南两处检查清单、eval-v2 EVAL_PLAN 质量判据。
- **开发 backlog（需编码会话/外部依赖，非 executor 职责）**：cloudbase-learning s1–s8 小程序实现清单、墨题 P0 错题 AI 诊断验收标准、P1 AI 服务层配置项、上云部署方案步骤（含服务器/域名购买决策）、self-study INDEX 委派项（@coder / sora 本周）。
- **条件触发研究主题**：memory/2026-09-19.md 行动项 6 条（P1/P2 全部「待触发」标注）。
- **重复/已迁移**：旧 daily logs 中的历史待办（已由 weekly cleanup 今日统一归档 Section 11，48 项）。

## 💡 建议

1. **ZCode 卸载**是今天最高优先级——静默上传已实锤（墨题 126MB 快照），建议今晚抽 10 分钟执行前三步（退出登录/卸载/删快照），git 历史轮换可交给 k。
2. 9/21（周一）是闲鱼决策复盘日，state.yaml 第 42 天，本周只需那 30 秒。
3. 万悟 9/25 硬截止：若有意参赛，建议 9/21 前确认，留给 k 一天出初稿。

---
_由 k (Hermes daily-todo-executor) 生成 ｜ vault 路径：memory/2026/09/2026-09-19-daily-todo-executor.md_
