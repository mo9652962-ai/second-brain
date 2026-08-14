---
tags: [周报, GitHub Trending, W33]
date: 2026-08-14
---

# 🗞️ GitHub 周报 — W33（2026-08-14）

> 本周全新面孔为主，5 个精选项目已写入 knowledge/。详细见 [[GitHub-Weekly-2026-08-14]]。

## 项目详情
| # | 项目 | ★ | 本周Δ | 入库 |
|:--|:--|--:|--:|:--|
| 1 | prime-agent (PrimeIntellect) | 15.7k | +12,476 | ⭐ [[prime-agent-rlm-2026-08-14]] |
| 2 | TencentDB-Agent-Memory | 21.5k | +5,388 | *(已评估,跟踪 delta 12k→21.5k)* |
| 3 | addyosmani/agent-skills | 87.1k | +4,562 | ⭐ [[agent-skills-addyosmani-2026-08-14]] |
| 4 | semantica | 7.3k | +4,073 | ⭐ [[semantica-graph-native-2026-08-14]] |
| 5 | cloudflare/computer | 8.1k | +3,599 | ⭐ [[cloudflare-computer-2026-08-14]] |
| ▪ | NVIDIA-NeMo/Switchyard | 1.4k | +900 | ⭐ [[switchyard-llm-routing-2026-08-14]] |

## 可借鉴点归纳
**技术层面**
- prime-agent 的 RLM + Continual Harness：一切皆程序化（持久 IPython 作唯一内置工具）+ /refine 自改进（小步/证据/可回滚/不动基础 prompt）
- Switchyard 统一协议 + 翻译层：跨提供商路由像换数据库驱动一样干净
- addyosmani 四原则（specific/verifiable/battle-tested/minimal）+ references/ 链接 CI 门禁

**方法论层面**
- 「可审计 AI」：semantica 的 provenance（存意义而非只存嵌入）→ 知识库加来源字段
- 「长寿 agent」配方 = 持久目标 + 心跳/调度 + 后台 daemon + 可回滚自改进（Hermes 已覆盖大部分）
- agent 工具权限分离（cloudflare：exec 能力 vs FS 能力分离授予）

**可实操行动（P0/P1/P2）**
- 🟢 P1 Hermes skill 治理：加 references/ 链接完整性校验脚本 + 四原则自检（借 addyosmani）
- 🟢 P1 模型配置：参考 Switchyard「统一协议+翻译」审查 9 provider fallback 链
- 🟡 P2 prime-agent 长期跟踪（RLM 抽象），暂不安装（Hermes 已覆盖）
- 🟡 P2 semantica provenance 思路：Obsidian 笔记 frontmatter 加 provenance 字段

## 文件操作清单
- 新建 5 笔记（knowledge/AI×2 + knowledge/Dev×3）
- 更新 knowledge-map.md（② AI 表 + ③ 工具表 + 关联表）
- 追加 github-projects-tracking.csv（+5 行，共 51 行）
- 本周报 + GitHub-Weekly-2026-08-14.md
- 未建 TencentDB 笔记（08-05/08-08 已评估，结论不变）