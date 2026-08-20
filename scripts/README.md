# 🗂️ scripts/ 脚本登记表（单一事实源）

> **用途**：记录本目录所有脚本的用途、依赖、最近修改与状态——杜绝「脚本无声消失、无源码可恢复」（2026-08-18 反思教训：cache-hit-monitor 脚本消失且无登记）。
>
> **规则**：新建脚本 → 在本表加一行；删除/迁移脚本 → 补一句「为何删/替代品」；用途描述随使用更新。
>
> **创建**：2026-08-20 · daily-reflection cron（复盘 8-19，当场补建上轮行动项）

| 脚本 | 用途 | 最近修改 | 状态 |
|:-----|:-----|:--------|:-----|
| api_health_test.sh | API 连通性测试 | 08-06 | 在用 |
| batch-import.py | MarkItDown 批量导入文档→知识库 | 08-06 | 在用 |
| check_wikilinks.py | wikilink 断链检查 | 08-06 | 在用 |
| configure-smart-router.py | smart_model_routing 模型路由配置 | 08-06 | 在用 |
| cron-retry-wrapper.sh | cron 失败重试包装 | 08-06 | 在用 |
| daily_vault_optimize.py | 每日 vault 优化（DIR_MOC 映射清理等） | 08-18 | 在用（8/18 清 8 个过期映射） |
| export_traces.py | OpenForgeRL 轨迹导出（7/31 实测 206 会话） | 08-06 | 在用 |
| gaming-optimize.bat | 游戏性能优化批处理 | 07-21 | 在用 |
| generate_graph.py | Obsidian 图谱生成 | 08-16 | 在用 |
| gen-math-40-days.py | 三年级数学 40 天每日一练生成 | 08-06 | 在用 |
| gh-fast.sh | gh CLI 快速操作封装 | 08-06 | 在用 |
| github_treasure_hunt.py | GitHub 寻宝/趋势探索 | 08-06 | 在用 |
| health_check.ps1 | 系统健康检查 | 08-06 | 在用 |
| health_provider_check.py | provider 连通性探测（不打印密钥） | 08-09 | 在用；待加余额阈值告警（8/20 反思登记） |
| krea2-gen.py | Krea2 本地生图 | 08-06 | 在用 |
| label_traces.py | 轨迹标注 | 08-06 | 在用 |
| memory_dashboard.py | 记忆仪表盘 | 08-06 | 在用 |
| memory_tracker.py | 记忆追踪 | 08-06 | 在用 |
| skill-audit-scan.py | skill 审计扫描 | 08-06 | 在用 |
| sync-docs-knowledge.py | 文档→知识库同步 | 08-06 | 在用 |
| sync-skills.py | skills 同步 | 08-06 | 在用 |
| test-markitdown.py | MarkItDown 测试 | 08-06 | 在用 |
| test-ocr.py | OCR 测试 | 08-06 | 在用 |
| vault-orphan-duplicate-scan.py | 孤立/重复笔记扫描 | 08-17 | 在用 |
| vault-structure.py | vault 结构分析 | 08-06 | 在用 |
| web-archive.py | 网页存档 | 08-06 | 在用 |
| xianyu-master-gen.py | 闲鱼上架素材包生成 | 08-06 | 在用 |
| vault-audit-report.json | vault 审计报告（数据文件，非脚本） | 08-06 | 数据 |

## 已删除/迁移记录

| 脚本 | 删除/迁移时间 | 原因/替代品 |
|:-----|:------------|:-----------|
| cache-hit-monitor | 2026-08 发现缺失 | 无源码可恢复（8/18 反思教训）；如重建需登记回本表 |
