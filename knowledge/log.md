---
title: 知识库操作日志
type: 日志
created: 2026-09-05
updated: 2026-09-05
tags: [meta, 知识库治理]
---

# 🕐 知识库操作日志 — Knowledge Log

> 时间导向（append-only）。格式：`## [YYYY-MM-DD] 动作 | 主题`
> 动作：ingest / update / query / lint / create / archive / delete
> 超过 500 条时轮转：改名为 log-YYYY.md 重新开始。

## [2026-09-05] create | Knowledge Index + Log 建立

- 依据 Karpathy LLM-Wiki 规范创建 `index.md`（内容目录）+ `log.md`（时间线）
- 触发：抖音学习研究「AI 为什么不翻知识库」（一只桌子）→ 千轮研究 → 落地三增量
- 产出：index.md、log.md、knowledge-lint.py（只读体检脚本）

## [2026-09-05] lint | 知识库首轮体检（修复后）

- 扫描 525 页（含新增 index/log/规则页）
- 修复 lint 脚本路径解析 bug（相对/绝对路径 key 不一致、cand2 分支、双 CRLF）
- 结果：0 缺 frontmatter（已补 12 个）、「知识库-AI不翻知识库根因」已通过 index 挂载解除孤立
- 剩余：43 断链（多为 Archive 历史残留 + 模板占位）、22 孤立页（Daily/Research 历史存量）、1 组重复文件名（readme）
- 处理原则：只报告不自动修；P0 结构性修复待用户确认后执行
- 体检脚本正式落位：`META/scripts/knowledge-lint.py`

## [2026-09-05] create | Knowledge Query Rules

- 创建 `META/KNOWLEDGE-QUERY-RULES.md`：回答前读 index、回答中标来源、回答后写回、证据不足拒答
- 依据：OpenAI 引用格式化指南 + RAG claim-attribution + Karpathy 查询规范

## [2026-09-05] ingest | 知识库-AI不翻知识库根因

- 抖音学习研究（@一只桌子）：「差的不是资料，是最上面那层规则」
- 2 轮搜索引擎增强（10+ 来源）：AGENTS.md 三层级、RAG 检索 5 错误、Karpathy LLM-Wiki
- 落地：墨题 AGENTS.md 补「知识库优先规则」段；本知识库 index/log/lint 三增量
## [2026-09-05] lint | 每周例行体检

- 断链 0 / 孤立 0 / 缺 frontmatter 0
- 处理原则：只报告不自动修；新问题由 k 在下次会话处理


## [2026-09-05] ingest | 工具精度方法论学习研究

- 触发：知识库清理实战（lint 43 误报 vs 14 实际）→ 6 源搜索引擎研究
- 核心：假阳性税（FP→忽略→mute→召回归零）、Precision/Recall 4 问、wiki-lint 现代实践 5 参考
- 产出：knowledge/AI/工具精度方法论-假阳性税与知识库Lint-2026-09-05.md
- 反哺：knowledge-lint skill 新增精度方法论章节 + backlog（issue caps/severity/stale_claim）

## [2026-09-05] lint | 断链0·空文件0·标签冲突0·孤立1挂载MOC-Research(arxiv-09-05-agent-llm)·META→meta归一(3文件)

## [2026-09-05] ingest | 运动曲线学习研究

- 触发：抖音「设计师PPM：动效丝滑的关键就是要懂运动曲线」
- 5+ 源研究（M3 官方 / iOS / IBM / Ant Design / 社区实践）
- 产出：knowledge/Productivity/运动曲线-easing-动效丝滑关键-2026-09-05.md
- 反哺：apple-design-web skill 新增「4b 运动曲线」章节

## [2026-09-05] ingest | 网站公网部署学习研究

- 触发：抖音「写代码的码农：网站做完怎么让别人访问」（完整章节要点）
- 研究：Vercel 官方 DNS 细节 + 5 坑 + Cloudflare 中国加速方案 + 域名注册商对比
- 产出：knowledge/Development/网站公网部署全流程-Vercel-CDN-域名-2026-09-05.md
- 反哺：fastapi-cloud-deploy skill 补前端托管面
- 关键发现：Vercel Hobby 免费仅限非商业用途——墨题商业化前需定前端平台
## [2026-09-06] lint | 每周例行体检

- 断链 0 / 孤立 0 / 缺 frontmatter 0
- 处理原则：只报告不自动修；新问题由 k 在下次会话处理

## [2026-09-06] 整理 | W37 周度整理

- 本周新增 ~45 篇实质笔记（arXiv×6 + HN×6 + 多Agent Eval×8 + 部署/闲鱼/方法论）
- 补挂：MOC-Productivity W37 区 +5 · MOC-Dev AI 域 +1（知识库根因）
- 修正：MOC-Research 3 链接从「入口治理」误区移入「评测」区
- 索引：knowledge-map W37 区 + index（Research 186 / 总 532）+ MOC-Inbox 状态（孤立 0）
- 报告：memory/2026/09/weekly-2026-09-06.md

## [2026-09-06] lint | 例行体检修复（cron）

- 体检：断链 0 / 缺 frontmatter 0 / 空页 0 / 孤立 0（修复后）/ duplicate 1（低风险保留）
- 挂载：MOC-Research 补挂 [[arxiv-2026-09-06-agent-llm]]（速览页孤立 → 0）
- 标签一致性：`ai agent`→`ai-agent`（Dev/airi.md）· `github trending`→`github-trending`（Research/GitHub-Weekly-2026-08-14.md）
- 清理：git rm `Research/MOC-Research.md.bak`（8-10 旧残渣）+ 根目录 4 个 `.temp-*.py`（标注 safe to delete）
- 保留说明：duplicate 'readme'（Dev/system-prompts-reference 与 Research/eval-v2-2026-08-31 各一 README，均以完整路径引用，Obsidian 解析不冲突，低风险不处理）


## [2026-09-07] lint | 例行体检 + 修复（cron 手动触发）

- 扫描 546 页；备份至 `.backup/knowledge-lint-20260907/`
- 断链 0 / 空文件 0 / 极小页(<100字符) 0 / stale 0
- 修复缺 frontmatter 3 个（与同系列格式对齐）：
  - `Productivity/system-cleanup-report-20260906`（仿 08-23）
  - `Productivity/token-usage-report-20260906`（仿 08-23，tags: 周报/API成本/Token用量）
  - `Research/GitHub-Weekly-2026-09-06`（仿 08-30，tags: knowledge/research）
- 挂载孤立页 4 个（幂等，未删页）：
  - `Daily/hackernews-2026-09-06` → MOC-Inbox（续 09-05 序列）
  - `Productivity/token-usage-report-20260906` + `system-cleanup-report-20260906` → MOC-Productivity（W37 区）
  - `Research/arxiv-2026-09-07-agent-llm` → MOC-Research（续 09-06 序列）
- 标签一致性：新增 frontmatter 全部采用域标签体系（knowledge/<domain>），与同系列一致
- 剩余：1 组重复文件名（`Dev/system-prompts-reference/README` vs `Research/eval-v2-2026-08-31/README`）——均为全路径引用、无短链歧义，低风险忽略
- 结果：断链 0 / 缺 frontmatter 0 / 孤立 0（TOTAL ISSUES: 1，低风险）

## [2026-09-08] lint | 断链修复 + 孤立挂载 + 标签统一

- **断链修复 33+7 处**（全仓库 3114 链接严格扫描）：
  - 缺 `knowledge/` 前缀 26 处（index.md 5、MOC-Inbox 9、MOC-Productivity 3、MOC-Security 2、MOC-Research 2、工具精度方法论 2、网站公网部署 1、运动曲线 1、portfolio 3→改 `portfolio/` 前缀）
  - 相对路径层数错误 8 处：`github-trending-w35/w37` 的 `../knowledge/...` → `../../../knowledge/...`（memory/YYYY/MM/ 出发需 3 层）
  - 真断链转纯文本 4 处：knowledge-map 的 3 个 archive 周报（archive 目录已清理）+ AI-Agent 的 arxiv-agent-llm-2026-07-26（文件已归档移除）
  - 周报内部路径修正 1 处：weekly-2026-08-16 `memory/2026-08-14` → `[[memory/2026/08/2026-08-14]]`
- **孤立页挂载 2 个**（幂等，未删页）：`Research/arxiv-2026-09-08-agent-llm`、`Research/黑盒热榜5项目实证研究-2026-09-08` → MOC-Research（续 09-08 序列）
- **补 frontmatter 1 个**：`Research/黑盒热榜5项目实证研究-2026-09-08`（tags: [research, github, 实证研究, github-trending, W37]）
- **标签一致性**：`codex` → `Codex`（codex-2week-game-absorbed.md，与主流大写统一）
- **空文件**：全仓库 0 字节 md = 0，无需清理（dreaming/light/2026-09-08.md 曾被并发写入瞬间报 0 字节，实际 37 字节非空）
- **说明**：`Research/eval-v2-2026-08-31/README` 仍报孤立系 lint 的 README 重名检测盲区——MOC-Research 已有全路径入链，Obsidian 实际有效
- **结果**：断链 0 / 缺 frontmatter 0 / 孤立 1（lint 盲区）/ 重复文件名 1 组（低风险忽略）

## [2026-09-08] lint | 例行体检（断链16处修复 + 空壳清理 + 标签统一 + 孤立挂载）

- **断链修复 16 处**：dreaming 快照剥括号 6（light-08-06/07 的 health-2026-07-24 等）+ 维护笔记文档示例剥括号 8（log.md 3、08-13-maintenance 3、09-04-maintenance 2）+ `MEMORY.md`→`MEMORY` 5（含 1 带别名）
- **空壳清理 3 个**：dreaming light/deep/rem 09-08（无 footer + 计数 0）；09-05~07 带 footer 保留
- **标签统一 6 处**：`github trending`→`github-trending`（W31~35）×5、`GitHub Trending`→`github-trending`（W37）×1
- **孤立挂载 4 个**：GitHub-Weekly-09-08→MOC-GitHub、skill-audit-09-08→MOC-Research、CAD自动化MCP参考→MOC-Dev、hackernews-09-08→knowledge-map；均挂 HOME.md
- **补 frontmatter 2 个**：CAD自动化MCP参考-pascal-09-08、GitHub-Weekly-09-08
- **遗留**：eval-v2 README 报孤立 = lint README 重名盲区（MOC-Research 全路径入链有效）；09-04-maintenance「剥离方括号」为规则 prose 保留
- 详见 [[memory/2026/09/2026-09-08-vault-maintenance|2026-09-08 维护笔记]]

## [2026-09-09] lint | 例行体检（断链0/空文件0/标签0冲突 + 检测器同步）

- **断链 15 条报告 → 全部核实假阳性（真断链 0）**：占位符（`[[wikilink]]`/`[[note-1]]`/`[[series-2026-08-14]]`/`[[skill-name]]`/`` [[` `]] ``）×8、维护笔记文档示例（`[[../knowledge/...]]`/`[[MOC-Development]]` 等）×3、dreaming 冻结快照指向 `.archive`（`[[2026-07-21-2347]]`，lint 排除 .archive 故报 not found）×2、模板 `[[所属MOC]]`×1
- **检测器同步（先修检测器）**：skills 目录 `knowledge-lint.py` 为旧版（`Path(target).stem` 截断版本号 `MiMo-V2.5`→`MiMo-V2` → 误报 28 条断链）；已同步 vault 修复版（`strip_md()` 保留版本号点 + EXTERNAL_ROOTS 精确大小写）→ 正确 15 条全为占位符假阳性
- **空文件**：全仓库 0 字节 + <3 字符 md = 0，无需清理
- **标签一致性**：877 distinct tags，大小写 + 分隔符归一（`re.sub(r'[-_\s]+','-')`）冲突 = 0
- **缺 frontmatter 284 个全为系统文件**（skills/.venv/README/AGENTS 等仓库元数据，非笔记，不补）；真实笔记 0 缺
- **孤立页**：活跃 170（多为 memory/ 历史每日日志 + knowledge 新页待挂载，属 daily/周度 cron 职责，本次未动）
- **遗留**：`memory/dreaming/light-2026-08-06/07` 的 `[[2026-07-21-2347]]` 为冻结历史引用，保留
- **结果**：真断链 0 / 空文件 0 / 标签冲突 0

## [2026-09-10] lint | 例行体检（断链9→0 + 孤立5→0 + 标签统一 + 检测器双修复）

- **断链 9 条报告 → 全部为反引号代码示例假阳性**（log.md 维护笔记中 `[[wikilink]]`/`[[note-1]]`/`[[所属MOC]]` 等占位符示例被全文正则误抓）
- **检测器修复①（先修检测器）**：`extract_links` 先剥离行内反引号 + ``` 代码块 → 假阳性归零
- **检测器修复②**：MOC 中 `[[knowledge/Research/eval-v2-.../README]]` 全路径写法未剥离 `knowledge/` 前缀 → 重名 README fallback 匹配错目标、误报孤立；已剥离前缀 → eval-v2 README 孤立消除
- **孤立挂载 3 个**：hackernews-2026-09-09 → MOC-Research AI 日报；每日股票分析 09-08/09-09 → MOC-Finance
- **标签统一**：`thousand-round`→`千轮研究`（9 处）、`安全`→`security`（独立标签 15 处，复合词 网络安全/接口安全/金额安全 不拆）
- **补 tags 10 个**：arxiv core-contributions ×3、graphify-weekly ×3、hackernews-deep-dive ×1、Security 笔记 ×3
- **格式修正 1 个**：桂航考研路线图 `tags:knowledge/education[ ]` 异常 → `tags: [knowledge/education]`
- **误伤恢复 6 个**：v1 正则误拆复合词（`网络security` 等），从备份恢复后改精确 token 匹配（lint-fix-tags-v2.py）
- **遗留**：duplicate 'readme'（Dev/system-prompts-reference vs Research/eval-v2-2026-08-31）全路径引用无歧义，低风险忽略
- **结果**：断链 0 / 缺 frontmatter 0 / 孤立 0 / 短页 0 / 标签同义冲突 0
