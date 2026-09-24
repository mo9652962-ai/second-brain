---
tags: [github, github-trending, weekly, research, W38]
aliases: [GitHub 周榜 W38 weekly 口径]
date: 2026-09-13
type: note
---

# 🗞️ GitHub 周榜 W38 — weekly 口径精选（本周增速）

> 与同日脚本报告 [[GitHub-Weekly-2026-09-13]]（topic 总 star 口径，全连榜）互补。本报告按 **star 增速**（github.com/trending?since=weekly）筛选，聚焦新面孔。

## 本周榜单速览

| # | 项目 | ★ | 本周增长 | 定位 | 入库状态 |
|:--|:--|--:|--:|:--|:--|
| 1 | **ayghri/i-have-adhd** | 43.5k | **+15,924** | 输出风格 skill（增速王）| 👀 跟踪（08-02 已评估）|
| 2 | **tt-a1i/archify** | 59.8k | +10,442 | 可验证架构图 | 🔄 更新 [[archify-verifiable-diagrams-2026-09-06]] |
| 3 | **DietrichGebert/ponytail** | 136.7k | +9,272 | 懒人 senior dev 哲学 | 👀 跟踪（已吸收）|
| 4 | **affaan-m/ECC** | 257.2k | +8,086 | agent harness 优化 | 👀 跟踪（09-06 已评估）|
| 5 | **mattpocock/skills** | 260.6k | +8,960 | Real Engineers skills | 👀 跟踪（mattpocock-methodology 已入库）|
| 6 | **cathrynlavery/diagram-design** | 38.9k | +7,409 | 38 种编辑级图表 | 👀 跟踪（08-16 已评估）|
| 7 | **heygen-com/hyperframes** | 49.3k | +5,124 | HTML→确定性视频 | ✅ 新笔记 [[hyperframes-html-to-video-2026-09-13]] |
| 8 | **THU-MAIC/OpenMAIC** | 36.2k | +4,417 | 多 Agent 课堂 | 🔄 更新 [[openmaic-multiagent-classroom-2026-09-06]] |
| 9 | **blader/humanizer** | 47.4k | +4,069 | 去 AI 味 skill | 👀 跟踪（技能族已覆盖）|
| 10 | **obra/superpowers** | 285.9k | +3,938 | agentic skills 框架 | 👀 跟踪（已吸收）|
| 11 | **mksglu/context-mode** | 22.4k | +1,936 | 上下文沙箱/记忆/路由 | ✅ 新笔记 [[context-mode-context-window-2026-09-13]] |
| 12 | **petergyang/no-ai-slop** | 8.7k | +1,307 | 20+ 模式去 AI 味 | ✅ 新笔记 [[no-ai-slop-2026-09-13]] |
| 13 | **Tencent/WeKnora** | 22.7k | +1,168 | RAG+Agent+Wiki 知识平台 | ✅ 新笔记 [[weknora-knowledge-platform-2026-09-13]] |
| 14 | **earthtojake/text-to-cad** | 15.5k | +1,011 | CAD agent skills | 🔄 更新 CAD-Design.md |

## 本周精选 4 项（新面孔）

### 1️⃣ mksglu/context-mode — 上下文窗口优化的另一半
沙箱化工具输出（315KB→5.4KB，98% 减少）+ FTS5 索引化（>100KB 输出不截断只存指针）+ SQLite 会话记忆（压缩时 BM25 按需检索）+ 17 平台路由。核心哲学：**Think in Code**（让 LLM 写脚本算，不读文件进 context）与 **No prose-style enforcement**（文风注入被 kimi-k2.5 基准退化证据打脸后全量移除）。
→ 可借鉴：截断升级为「截断+可检索兜底」；数据路由不碰表达层。详见 [[context-mode-context-window-2026-09-13]]

### 2️⃣ Tencent/WeKnora — 文档→RAG→Agent→自维护 Wiki
腾讯级企业知识平台（v0.8.0）：三大能力 + 跨会话长期记忆 + 技能沙箱 + 修订历史。**最深刻单条教训：记忆按查询相关性排序，不按重要性**（importance DESC 会让 400 名之外的记忆永久不可达，已修复）。
→ 可借鉴：检索排序用相关度 + 词法融合；部署待 Docker Daemon 就绪后评估（本机虚拟化+CLI 已就绪，见 [[knowledge/META/current-environment]]）。详见 [[weknora-knowledge-platform-2026-09-13]]

### 3️⃣ heygen-com/hyperframes — Write HTML. Render Video
确定性 MP4 渲染（HTML+GSAP→Puppeteer→FFmpeg），20 个按需加载 agent skills（路由 + 10 工作流），组件注册表 208 项 + 三档语义搜索（明示答案来源），质量门禁（lint/check）。HeyGen 官方开源，386 releases 极活跃。
→ 可借鉴：抖音流水线零成本确定性渲染层；「产出即带验证」扩展到视频。详见 [[hyperframes-html-to-video-2026-09-13]]

### 4️⃣ petergyang/no-ai-slop — 规则化去 AI 味
20+ 可枚举检测模式（binary contrast / colon reveal / synonym cycling / fake-profound ending...），检测时**只引用证据不猜是否 AI 写的**，改写时保留个人声音。
→ 可借鉴：「检测证据清单」交付法（论文降 AI 率客户可解释性）；与 sora 39 类检测合并互补。详见 [[no-ai-slop-2026-09-13]]

## 💡 本周洞察

1. **Agent Skills 全面爆发成主流分发单元**：本周 trending 榜 25 席中过半是 skills/plugins（superpowers 285k / mattpocock 260k / ponytail 136k / archify 59k / hyperframes 49k / i-have-adhd 43k）——「skill 即产品」时代，sora 的技能体系（130+）站在同一侧。
2. **上下文治理是 agent 规模化的新瓶颈**：context-mode（98% 减少）+ 大量 context 优化项目同周上榜，验证 Hermes 三层截断痛点的行业共性。
3. **确定性工程回潮**：archify（确定性编译+校验收据）、hyperframes（确定性渲染）、no-ai-slop（规则检测）都在用确定性对抗 LLM 不可靠——与 sora 的「渲染验证闭环 / G5 门禁」同一方向。
4. **记忆系统进入「按查询排序」时代**：WeKnora 修复是标志性事件——静态重要度排序会系统性漏召回。
5. **脚本口径 vs weekly 口径**：同日脚本报告 Top5（codebase-memory-mcp/nanobot/chrome-devtools-mcp/TrendRadar/ruflo）全连榜无新面孔；weekly 口径才有 4 个真新增——诚实报告：本周价值在新面孔的增速榜，不在总星榜。

## 文件操作清单

- ✅ 新建 [[context-mode-context-window-2026-09-13]]（Dev）
- ✅ 新建 [[weknora-knowledge-platform-2026-09-13]]（AI）
- ✅ 新建 [[hyperframes-html-to-video-2026-09-13]]（Content）
- ✅ 新建 [[no-ai-slop-2026-09-13]]（Creative）
- ✅ 更新 [[archify-verifiable-diagrams-2026-09-06]]（49.9k→59.8k）
- ✅ 更新 [[openmaic-multiagent-classroom-2026-09-06]]（32.1k→36.2k）
- ✅ 更新 CAD-Design.md（text-to-cad 12.3K→15.5K）
- ✅ 周报 [[GitHub-Weekly-2026-09-13|W38 周报（memory）]] + tracking CSV 快照

---
*weekly 口径 · 数据源 github.com/trending?since=weekly（2026-09-13）*
