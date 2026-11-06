# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/2.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed (2026-11-06 知识库治理日)

- **标签归一化**: 全库 1264 个唯一标签中清理单复数/大小写/空格变体，26 篇笔记 12 类标签归一（`skill→skills`、`project→projects`、`JLCPCB→jlcpcb`、`Edge ai→edge-ai` 等）；规范表写入 `templates/风格指南.md`，后续新建笔记按表执行。
- **MOC-Research 去重瘦身**: 索引从 422 行降至 390 行，删除 33 条整行重复 + 清理 38 个重复链接 token，唯一笔记 300 篇保留完整；「最新增量」标题时间窗修正为 `2026-10 ~ 11-06`。
- **OKM 看板刷新**: `knowledge/METABOLISM.md` 由 700 篇/333 常青（2026-09-26 快照）刷新为 757 篇 / 361 Evergreen / 389 Budding。
- **README 数据校准**: 资产数 760+ → 820+，常青徽章 333 → 361，仓库统计块 19.8MB/901 文件 → 29MB/969 文件、knowledge 676 → 733 篇、Skill 覆盖 11 → 37 目录。

### Added

- **AI-First 协议支持**: 全新支持 `llmstxt.org` 标准，自动化生成 `/llms.txt`（纲要索引）与 `/llms-full.txt`（221KB 纯净知识平铺包），优化 Agent 摄取上下文。
- **OKM 知识新陈代谢治理 (Open Knowledge Metabolism)**: 新增 `scripts/okm_metabolism.py` 与 `knowledge/METABOLISM.md` 看板，自动化归类 332 篇 Evergreen 常青树、365 篇 Budding 成长笔记。
- **官网与爬虫指引增强**: `docs-site/robots.txt` 声明 `llms.txt` 入口；3D 官网首页 Hero 与页脚新增 `llms.txt` 及 OKM 看板直达。
- **CI/CD 自动化构建集成**: `.github/workflows/deploy-docs.yml` 增加生成阶段，确保每次 Push 自动刷新 llms 索引与新陈代谢指标。

- README: QuickStart 移到顶部，添加"适合谁"定位说明 (#2)
- CHANGELOG.md: 首次创建，遵循 Keep a Changelog 格式
- Python 知识域: `knowledge/Dev/python-ecosystem.md`
- 工具知识域: `knowledge/Dev/hermes-agent-ecosystem.md`
- 记忆贡献度追踪: `scripts/memory_tracker.py` + `scripts/memory_dashboard.py`
- 练习册口算 15→10 两位数乘法，笔算 10→4 竖式表格 (#1)

### Changed

- 知识库维护: 清理 21 个空文件 + 6 个空目录，归档 14 个旧记忆文件
- 跨域链接增强: AI↔Dev↔Productivity 双向链，HOME 更新引用
- MOC-Dev/MOC-Dev: 添加跨域导航

### Fixed

- 练习册排版: 单页紧凑布局（行距 1.15，笔算 8→4 行空白）
- 知识库待办: 全库扫描并落实 6 个文件中的待办项

## [0.3.0] - 2026-07-29

### Added

- 标准教材版练习册 v3.0: 函数化五层架构，40 天 × 1480 题
- 七大自举系统完工: 35/35 满分
- 三大知识领域扩充: AI/MLOps、硬件工程、平台开发

### Changed

- SOUL.md: Relay-OPD 验证 + 新增长任务检查点规则
- Hermes 工作流: 规则 #5-#9 (Cron 错峰/User-blocked/Cron 产出吸收)

## [0.2.0] - 2026-07-28

### Added

- 七大自举系统建设: 知识吸收入门、工具调用、代码质量、输出风格、上下文管理
- MCP 服务器: Memvid 记忆层 MCP + 嘉立创 EDA MCP
- HTML 网页幻灯片生成器

### Changed

- 知识图谱 v2 维护: 批量链接修复，孤立笔记整合
- Obsidian 图谱缓存更新

## [0.1.0] - 2026-07-21

### Added

- 项目初始化: Obsidian + Hermes Agent 知识库
- 初始技能: 硬件创业/PCB/单片机/CAD、现代 Web 开发、平台开发
- GitHub Pages 部署 (MkDocs)
