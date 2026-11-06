---
tags: [research, vault, knowledge-governance, obsidian]
type: research
domain: Research
created: 2026-11-06
updated: 2026-11-06
---

# 知识库治理日审计：MOC 去重 / 标签归一 / 行尾固化（2026-11-06）

> 研究主题 · 2026-11-06 · 结论置顶

## 🎯 结论（TL;DR）

1. **知识域本体是健康的**：`knowledge/` 720 页，lint 实测 0 断链 / 0 入链孤儿 / 0 缺 frontmatter。日常报出的「孤立 36%」是口径假象——扫描范围含根目录 meta 文件（SOUL/AGENTS/PRIVACY）、`skills/` 第三方技能文档、`.hermes`/`.learnings`，这些本不该挂 MOC。
2. **真正的噪音是「重复索引」不是「孤立」**：MOC-Research 422 行里 33 行整行重复 + 38 个重复链接 token，同一条 arXiv 速览最多出现 3 次。去重后 390 行、唯一笔记 300 篇全保留。
3. **标签膨胀的真因是变体而非数量**：1264 个唯一标签中，变体冲突只有 12 类（单复数 8 + 大小写/空格 4），命中 26 篇。归一成本极低，收益是检索不再被拆成两个标签。
4. **行尾是长期隐形税**：`.gitattributes` 声明 `*.md eol=lf` 但 `core.autocrlf=true`，6 篇遗留 CRLF blob 让 `dev` 分支每天出现「幽灵改动」，直接阻塞 `merge main`。已归一为 LF，内容零变化。

## 🔍 研究方法

- 实测：`daily_vault_optimize.py`、`knowledge-lint.py`、`check_wikilinks.py`、`okm_metabolism.py`、`gen-llms-txt.py` 全链路跑通并读输出
- 检索式调研 3 篇外部实践（2026 年）：
  - [PARA + Zettelkasten + MOC 组合实践](https://hutaox.com/blog/2026/10/23/para-zettelkasten-pkm-practice/)——文件夹管「放哪」、卡片盒管「怎么连」、MOC 管「怎么找」、标签管「是什么」
  - [机器可读知识库实践](https://heaven-1314.github.io/posts/knowledge-base-organization/)——MOC 只做索引不写正文；裸链接 `[[页面名]]` 不用路径链接；新建页要有门槛
  - [Obsidian 标签结构体系（少数派）](https://sspai.com/post/104533)——L.A.T. 三层（类型/领域/状态）+ PARA 驱动，标签只描述属性不描述归属

## 📊 研究发现

| 观察项（实测） | 数值 | 判定 |
|:---|:---|:---|
| knowledge/ 页数 / lint 断链 / 入链孤儿 | 720 / 0 / 0 | 健康 |
| vault 全量孤立（含 skills/meta） | 205/1587 = 12% | 口径假象，非缺陷 |
| 唯一标签 / 变体冲突类 / 命中笔记 | 1264 / 12 / 26 | 已归一 |
| MOC-Research 行数 / 重复行 / 重复 token | 422→390 / 33 / 38 | 已瘦身 |
| OKM 看板快照陈旧度 | 700 篇（09-26）→ 757 篇（11-06） | 已刷新 |
| README 数据偏差 | 760+/333/901 文件 → 820+/361/969 文件 | 已校准 |

**推断（未直接验证）**：MOC 重复主要来自「自动挂载」小节与「论文追踪」小节各自登记同一批 arXiv 笔记——脚本只做幂等判断（`[[stem]]` 是否出现），没有跨小节查重，所以每次补录都会新增一条。

**未知**：`dev` 分支上多出的 3 个 `memory/dreaming/2026-09-01` 文件来源未查（无内容影响，留待下次）。

## ✅ 可落地项

- [x] 标签归一化 26 篇 + 规范表写入 `templates/风格指南.md`
- [x] MOC-Research 去重（33 行 / 38 token）+ 时间窗修正
- [x] OKM 看板刷新（757 / 361 / 389）
- [x] README 统计块与徽章校准
- [x] CRLF→LF 归一（main + dev 双分支），解除 dev 同步阻塞
- [ ] 给 `daily_vault_optimize.py` 的 `mount_orphans` 加跨小节查重（本次手工做了一次，脚本下次还会重复登记）
- [ ] 评估 Obsidian Bases（原生表格视图）替代部分手写 MOC 索引——参考 bryanhogan 的 2026 vault 2.0 方案
- [ ] 给 `skills/` 第三方技能文档单独定口径（是否纳入 MOC，当前一律视为外部资产）

## 🔗 相关

- [[MOC-Research]] · [[knowledge-map|🗺️ 知识地图]] · [[METABOLISM]] · [[Home|🏠 Home]]
