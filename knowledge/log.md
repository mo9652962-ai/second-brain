---
title: 知识库操作日志
type: 日志
created: 2026-09-05
updated: 2026-09-05
tags: [meta, vault-maintenance]
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
- 产出：knowledge/Dev/网站公网部署全流程-Vercel-CDN-域名-2026-09-05.md
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

- **断链 15 条报告 → 全部核实假阳性（真断链 0）**：占位符（`[[wikilink]]`/`[[note-1]]`/`[[series-2026-08-14]]`/`[[skill-name]]`/`` [[` `]] ``）×8、维护笔记文档示例（`../knowledge/...`/`MOC-Development` 等）×3、dreaming 冻结快照指向 `.archive`（`[[2026-07-21-2347]]`，lint 排除 .archive 故报 not found）×2、模板 `[[所属MOC]]`×1
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
- **检测器修复②**：MOC 中 `knowledge/Research/eval-v2-.../README` 全路径写法未剥离 `knowledge/` 前缀 → 重名 README fallback 匹配错目标、误报孤立；已剥离前缀 → eval-v2 README 孤立消除
- **孤立挂载 3 个**：hackernews-2026-09-09 → MOC-Research AI 日报；每日股票分析 09-08/09-09 → MOC-Finance
- **标签统一**：`thousand-round`→`千轮研究`（9 处）、`安全`→`security`（独立标签 15 处，复合词 网络安全/接口安全/金额安全 不拆）
- **补 tags 10 个**：arxiv core-contributions ×3、graphify-weekly ×3、hackernews-deep-dive ×1、Security 笔记 ×3
- **格式修正 1 个**：某高校考研路线图 `tags:knowledge/education[ ]` 异常 → `tags: [knowledge/education]`
- **误伤恢复 6 个**：v1 正则误拆复合词（`网络security` 等），从备份恢复后改精确 token 匹配（lint-fix-tags-v2.py）
- **遗留**：duplicate 'readme'（Dev/system-prompts-reference vs Research/eval-v2-2026-08-31）全路径引用无歧义，低风险忽略
- **结果**：断链 0 / 缺 frontmatter 0 / 孤立 0 / 短页 0 / 标签同义冲突 0

## [2026-09-13] lint | 例行体检（断链0 + 补frontmatter 13 + 孤立挂载 3 + 标签归一）

- **断链 12 条报告（全仓库严格扫描）→ 真断链 0**：反引号内文档示例 ×9 已按规范剥 `[[` `]]`（log.md 3 + 09-08 维护笔记 6：`../knowledge/...`/`MOC-Development`/`knowledge/AI-Workflow`/`knowledge/arxiv-2026-07-31-...`/`projects`/`memory/2026/08/sug...`）；保留设计内项 3 处（09-04/09-08 剥离规则 prose 各 1、09-12 回顾指向 09-13 的前向导航链接 1）
- **补 frontmatter 13 个**：损坏闭合符 2（Dev/ecc-agent-harness `status: active---`、Education/某高校 `date: 2026-08---` 均缺换行闭合，lint 只查 startswith 漏报）+ 无 frontmatter 11（Content 竞品对标、Productivity system-cleanup-0912、Research self-study 9 份千轮报告）
- **孤立挂载 3 个**：竞品对标-AI商业广告接单教程 → MOC-Inbox；每日股票分析-09-11 → MOC-Finance；system-cleanup-report-0912 → MOC-Productivity（W37 区块）
- **标签归一**：某高校 tags 行归一化（lint-fix-tags-v2.py 幂等）；同义词（thousand-round/安全）已无目标
- **空文件**：全仓库 0 字节 = 0，无需清理
- **检测器盲区记录**：knowledge-lint.py 的 frontmatter 检测 `startswith("---")` 无法识别闭合符缺失（ecc/某高校类）；scan-vault-broken-links.py 旧版不剥离反引号（vault 版已修，lint 报 0）
- **结果**：lint 断链 0 / 缺 frontmatter 0 / 孤立 0 / 短页 0；全仓库严格扫描剩 3 处设计内保留
## [2026-09-13] lint | 每周例行体检

- 断链 0 / 孤立 1 / 缺 frontmatter 0
- 处理原则：只报告不自动修；新问题由 k 在下次会话处理

## [2026-09-14] lint | 例行体检 + 修复

- 断链 10→0：4 个 09-13 研究笔记「关联」区技能名伪链接（`context-management-bootstrapping` 等 9 个 Hermes 技能名）改反引号纯文本
- 缺 frontmatter 2→0：system-cleanup-report-20260913 / GitHub-Weekly-2026-09-13 补标准 frontmatter
- 孤立 2→0：system-cleanup-report + token-usage-report 挂载 MOC-Productivity（W38 区块）；hackernews-2026-09-14 挂载 MOC-Research
- 标签一致性：MCP/mcp、MOC/moc 大小写统一（8 文件）；周标签已统一大写（W31-W38）
- 空文件：0 字节 0 个；dreaming/light 近空文件（No notable updates）为系统占位，保留
- 遗留：Duplicate filenames（2 个 README.md 不同目录）低风险忽略
## [2026-09-15] lint | 每周例行体检

- 断链 0 / 孤立 0 / 缺 frontmatter 0
- 处理原则：只报告不自动修；新问题由 k 在下次会话处理

## [2026-09-17] lint | 全库体检 + 标签格式统一 + 检测器补盲

- **断链 2→0（全仓库 3548 链接）**：剩余 2 处为 09-04/09-08 维护笔记内反引号示例（`[[`。`]]` prose），按「先修检测器」原则加入 scan-vault-broken-links.py 白名单，不动正文
- **孤立 2→0**：hackernews-2026-09-16 → knowledge-map（Daily 区）；system-cleanup-report-20260915 → MOC-Productivity（W38 区块）
- **标签格式统一（重大）**：90 处 YAML 块式列表（`tags:\n  - xxx`）→ 流式 `tags: [a, b]`；lint-fix-tags-v2.py 升级 v3（BADFMT 幂等转换 + 同义映射扩展 27 项：闲鱼→xianyu、变现→monetization、方法论→methodology、自动化→automation、知识吸收→knowledge-absorption、多Agent→multi-agent、GitHub Trending→github-trending、降AI/反AI味→去AI味 等），42 文件同义归一，幂等复跑 0
- **检测器补盲（关键）**：knowledge-lint.py 新增「粘连闭合符」检测（`tags: [a]---` 缺独立 `---` 行）——旧检测只查 startswith 漏报 50 个文件（含 index.md/log.md/MOC 全部），本次修复 50/50；TOTAL ISSUES 计入 glued_fm
- **空文件**：全仓库 0 字节 = 0，空壳页 = 0，无需清理
- **frontmatter 修复 1**：Education/某高校 `date: 2026-08---` 粘连闭合（09-08 已修过但复现，已根治检测）
- **遗留**：Duplicate filenames（2 个 README.md 不同目录）低风险忽略
- **结果**：lint 断链 0 / 缺 frontmatter 0 / 粘连闭合 0 / 孤立 0 / 短页 0；全仓库断链 0
- **验证补盲**：ad-hoc 验证脚本（fixture mini-vault + 真实库双跑）抓到 lint-fix-tags-v2.py SPECIAL_FIX 重拼 frontmatter 缺换行 bug（`new_fm+"---"` → `new_fm+"\n---"`），修复后某高校不再被脚本写回粘连态；验证 11/11 PASS



## [2026-09-17] lint | Obsidian 优化强化
- **诊断**：lint 606 页（断链 0 / 缺 frontmatter 0 / 粘连闭合 0 / 孤立 1 / 短页 0 / 陈旧 0）；19 知识域 vs 9 MOC + Inbox
- **修复**：挂载 arxiv-2026-09-17-agent-llm → MOC-Research（计数 207→208）；index.md 头部更新（09-13/592 → 09-17/606）+ Research 计数 212 + 补 4 个小域行（Archive/Creative/Product/gaming）；knowledge-map 开 W39 速览区挂今日 arxiv
- **结果**：lint 全绿（孤立 0，仅剩 2 个 README.md 低风险重名忽略）


## [2026-09-19] lint | 例行体检 + 修复
- **诊断**：lint 617 页（断链 0 / 缺 frontmatter 4 / 粘连闭合 0 / 孤立 6 / 短页 0 / 陈旧 0）；全仓库断链扫描 3617 链接 0 断链；全仓库 0 字节空文件 = 0
- **修复**：
  - 补 frontmatter 4：system-cleanup-report-20260918、douyin-kiko-5-skills-ai-design-20260918、genoffice-ai-office-suite-20260918、wemux-ai-agent-platform-20260918（均 09-18 新增，tags/type/created/title 标准补齐）
  - 挂载孤儿 6：overclaimbench 知识卡 + hackernews-09-18 → MOC-Research；每日股票分析-09-18 → MOC-Finance；system-cleanup-09-18 → MOC-Productivity；genoffice / wemux 研究 → MOC-Research 头部
  - 标签格式 1：arxiv-2026-09-18-agent-llm 块式列表 → 流式（lint-fix-tags-v2.py 幂等）
  - 顺手挂载今日 hackernews-2026-09-19（cron 新生成孤儿）→ MOC-Research
- **结果**：lint 全绿（断链 0 / 缺 frontmatter 0 / 孤立 0，仅剩 2 个 README.md 低风险重名忽略）；全仓库 3628 链接 0 断链；skills/ 下 2 个 <100B 文件为技能模板占位（ERRORS.md / FEATURE_REQUESTS.md），设计内保留不动
## [2026-09-20] lint | 每周例行体检

- 断链 3 / 孤立 2 / 缺 frontmatter 2
- 处理原则：只报告不自动修；新问题由 k 在下次会话处理

## [2026-09-20] W39 周度整理 | 断链/孤立/frontmatter 清零 + 本周新增挂载

- 修复：断链 3（GEO `MOC-Content`→`MOC-Inbox`、PPT SOP ×2 技能名 `award-defense-presentation`→纯文本）
- 补 frontmatter 4：README-Template-01 / agent4science / GitHub-Weekly-2026-09-20 / system-cleanup-20260920
- 孤立页挂载 4：即梦Seedance / React-Bits / HN 09-20 / GitHub-Weekly-09-20（MOC-Inbox Content+AI 区、MOC-Dev、MOC-Research、MOC-GitHub W39）
- 本周新增挂载：AI 3 篇 + Content 3 篇 → MOC-Inbox；React-Bits → MOC-Dev；PPT SOP×2 + 模板库 + 清理报告 → MOC-Productivity W39 区；GitHub-Weekly 系列 → MOC-GitHub
- 索引更新：knowledge-map W39 速览区补全 30 行 + MOC 规模表同步；index.md 页面总数 606→642 + MOC/域表数字刷新
- 结果：lint 全绿（断链 0 / frontmatter 0 / 孤立 0，仅剩 2 个 README.md 低风险重名忽略）

## [2026-09-20] lint | 例行体检：8 问题 → 0

- 修复：README.md 真断链（memory/2026/2026-09-10.md → memory/2026/09/2026-09-10.md）；标签统一 2 处（semif 裸 tag AI→ai、竞品对标 #AI→#ai）；删除 temp_extracted_content.md 垃圾文件；清理 dreaming 空壳 2 只（deep/rem 09-20，无 footer 无入链）
- 并发进程已处理：award-defense-presentation 断链×2、MOC-Content→MOC-Inbox、孤立挂载×3、system-cleanup frontmatter
- 遗留：14 markdown 误报（verbatim+代码块）、历史 cron 孤儿（归档/非活跃）、README 重复文件名 1 组
- 验证：Broken wikilinks 0 / Missing frontmatter 0 / Orphan 0 / Tag case 0

## [2026-09-20] ingest | Devin / Cognition 评估

- 新增：`knowledge/Dev/Devin-Cognition-评估-2026-09-20.md`
- 挂载：`MOC-Dev` 与 `knowledge-map` 的 W39 新增区
- 内容：官方能力/集成/定价、公开 PR 质量研究、与 Codex/Hermes 的边界及低风险试用方案
- 证据边界：官方产品声明、2026-09-12 arXiv 观察性研究、厂商自报 Fusion 数据分开标注

## [2026-09-20] freshness | 时效审计

- 过期硬约束 0 / 待运行时验证 37 / 历史记录 352
- 处理原则：只报告不自动修；事实源见 knowledge/META/current-environment.md
