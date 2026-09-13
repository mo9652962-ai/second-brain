---
tags: [周报, GitHub Trending, W38]
date: 2026-09-13
---

# 🗞️ GitHub 周报 — W38（weekly 口径）

## 项目详情

| # | 项目 | ★ | 本周增长 | 核心价值 | 入库笔记 |
|:--|:--|--:|--:|:--|:--|
| 1 | mksglu/context-mode | 22.4k | +1,936 | 上下文沙箱(98%减)+FTS5索引+会话记忆+17平台路由 | [[knowledge/Dev/context-mode-context-window-2026-09-13]] |
| 2 | Tencent/WeKnora | 22.7k | +1,168 | 文档→RAG→Agent→自维护Wiki，记忆按查询排序 | [[knowledge/AI/weknora-knowledge-platform-2026-09-13]] |
| 3 | heygen-com/hyperframes | 49.3k | +5,124 | HTML→确定性MP4，20 skills按需加载 | [[knowledge/Content/hyperframes-html-to-video-2026-09-13]] |
| 4 | petergyang/no-ai-slop | 8.7k | +1,307 | 20+模式规则化去AI味，检测举证不猜 | [[knowledge/Creative/no-ai-slop-2026-09-13]] |
| 5 | tt-a1i/archify | 59.8k | +10,442 | 可验证架构图（W37入库，连榜更新） | [[knowledge/Dev/archify-verifiable-diagrams-2026-09-06]] |
| 6 | THU-MAIC/OpenMAIC | 36.2k | +4,417 | 多Agent课堂（W37入库，连榜更新） | [[knowledge/AI/openmaic-multiagent-classroom-2026-09-06]] |
| 7 | earthtojake/text-to-cad | 15.5k | +1,011 | CAD agent skills（CAD-Design 更新） | [[knowledge/Hardware/CAD-Design]] |

## 可借鉴点归纳

**技术层面**
- 上下文：>100KB 工具输出「索引化+指针」不截断（context-mode FTS5）
- 记忆：检索按查询相关度排序 + 词法融合，静态重要度会漏召回（WeKnora 修复）
- 视频：HTML+GSAP→Puppeteer→FFmpeg 确定性渲染，可 lint/check（hyperframes）
- 去AI味：规则可枚举+检测举证清单，保留个人声音（no-ai-slop）

**方法论层面**
- 数据路由与表达层分离：约束放数据流向，不注入文风（kimi-k2.5 退化证据）
- 确定性工程对抗 LLM 不可靠：编译/渲染/检测都要「产出即带验证」
- skill 即产品：按需加载的路由 skill 形态（/hyperframes 只装 core set）

**可实操行动**
1. 论文降 AI 率交付升级为「检测证据清单」模式（命中模式+原文引用+改后对比）
2. 抖音流水线接入 hyperframes 做零成本确定性渲染层（下次做视频时）
3. 39 类检测清单合并 no-ai-slop 的 10 类新模式（binary contrast/colon reveal/synonym cycling/fake-profound ending）
4. Hermes 侧：大输出「截断+可检索兜底」思路记入 context 技能（勿改核心）

## 文件操作清单

- 新建 4 篇项目笔记（Dev/AI/Content/Creative 各 1）
- 更新 3 处已评估笔记（archify/openmaic/CAD-Design）
- 周报 knowledge/Research/GitHub-Weekly-2026-09-13-weekly-5projects.md + MOC-GitHub + knowledge-map + tracking CSV

---
*W38 · weekly 口径 · 2026-09-13 · 与脚本报告 GitHub-Weekly-2026-09-13（topic Top5 连榜）互补*
