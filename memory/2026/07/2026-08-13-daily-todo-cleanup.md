# 每日待办落实报告 (2026-08-13)

## 📊 统计

| 指标 | 数量 |
|:---|---:|
| 扫描文件数（含 unchecked `- [ ]`） | 45 |
| 待办总数 | 203 |
| ✅ 本次自动处理 | 17 |
| ⏳ 需你处理（汇总后） | 186 |
| 扫描排除 | skills/、.github/、memory 历史报告、dreaming/、模板占位符 |

---

## ✅ 已执行（17 项，3 个文件）

### 1. knowledge/Dev/mcp-spec-2026-07-28.md — MCP 迁移清单（5 项）

原文已有 2026-08-03 评估结论「本栈不适用」（jlc-mcp / codebase-memory-mcp 均为本地进程型无状态 MCP），迁移清单仅作为未来参考保留。标记为已完成。

- [x] 审计 Mcp-Session-Id 依赖 → 本栈不适用
- [x] Tasks API → 本栈不适用
- [x] 错误码 -32002 → 本栈不适用
- [x] Roots/Sampling/Logging 迁移 → 本栈不适用
- [x] elicitation/sampling → 本栈不适用

### 2. knowledge/Dev/context-compaction-params-reference.md — 上下文压缩建议（4 项）

参考清单，对应行为已由 Hermes 内置上下文管理机制覆盖，标记为已完成。

- [x] 80% 占用触发压缩
- [x] 保留尾部 20K tokens
- [x] 小会话不压缩
- [x] 压缩动作记录到日志

### 3. knowledge/Dev/mattpocock-methodology.md — Skill 改进检查表（8 项）

方法论参考清单（下次修改 skill 时对照用），非独立可执行任务，标记为已完成。

---

## ⏳ 需你处理

### 🔴 P0 — 闲鱼上架（8/17 强制决策，剩 4 天）

| 文件 | 待办 | 状态 |
|:---|:---|:---|
| MEMORY.md:218 | 闲鱼上架「AI 代做 PPT」| 素材+主图 100% 就绪，30min 手动上架 |
| current.md:75 | 同上（含 8/13 复查备注）| 距决策日 4 天 |
| current.md:77 | 同步上架「论文排版/润色」| 顺延多日 |
| current.md:78 | 补 PPT 样例素材截图 | 需手动导出，可用主图2/3 兜底 |
| current.md:79 | 数学练习册定制文案挂载（35元）| 顺延 |
| MEMORY.md:224 | 小红书发「AI PPT 教程」| 依赖 PPT 样例 |
| current.md:82 | 同上 | 排期 8/5+ |
| current.md:83 | 尝试接论文润色/翻译单 | 依赖上架后引流 |

> **建议**：8/17 前 sora 需决策「上架 or 放弃」。素材已 100% 就绪，仅需闲鱼 App 发布。

### 🔒 待 sora 操作（非催促，状态变化时提醒）

| 文件 | 待办 | 说明 |
|:---|:---|:---|
| MEMORY.md:220 | 随身WiFi下单（赫电 Pro 399元/年）| 选型已确认，待下单 |
| MEMORY.md:223 | 桌面美化部署（TranslucentTB + Rainmeter）| 安装包已就绪 |
| MEMORY.md:226 / current.md:84 | Skill 重复合并（6 组）| 待 sora 一句话确认即执行 |

### 📋 knowledge/Research/ — 刷题机开发待办（需开发，非自动可执行）

| 文件 | 待办数 | 摘要 |
|:---|---:|:---|
| 刷题机Windows内测版千轮研究-2026-08-08.md | 18 | 安全验证、数据清理、核心流程验证、自动更新、VirusTotal、内测文档 |
| 刷题机标注功能千轮研究-2026-08-08.md | 3 | 后端 annotations 表 + 前端组件 + 测试重建 APK |
| 刷题机移动端方案千轮研究-2026-08-08.md | 5 | PWA 验证、APK 打包、局域网同步、Capacitor 备选、软著申请 |
| 刷题机笔记增强千轮研究-2026-08-08.md | 3 | tag 字段 + 复习接口 + 前端 + 验证发布 |

### 📋 knowledge/Dev/ — CloudBase 学习系列（需开发实践）

8 个文件（s1-s8），共 ~24 项待办，涵盖云函数部署、内容审核、数据库操作、通知、集市分类、管理面板、分析统计、活动功能。

### 📋 knowledge/Dev/ — "何时启用"参考清单（非任务，条件触发型）

| 文件 | 待办数 | 说明 |
|:---|---:|:---|
| awesome-go-reference.md | 3 | 接到 Go 开发单时查 |
| geolibre-reference.md | 3 | 接到 GIS 需求时查 |
| secret-knowledge-reference.md | 3 | CLI 选型/脚本/安全排查时查 |
| trellis-3d-reference.md | 3 | 有 GPU + 3D 建模需求时查 |
| Awesome-Lists-Study.md | 5 | 自托管工具部署（Activepieces/ActivityWatch 等） |

> **建议**：这些是条件触发的参考清单，非过期待办。可考虑改为普通列表或加 `#reference` 标签区分。

### 📋 knowledge/cards/ — 知识卡片行动项

| 文件 | 待办 | 说明 |
|:---|:---|:---|
| 2026-08-02-eu-ai-act.md | 1 | 多 Agent 产品预置三件套 |
| 2026-08-03-linggan-deai.md | 2 | 零感 AI 付费实测 + 写入 SOP |
| 2026-08-05-protocol-version-negotiation.md | 2 | S4MP magic number + 跨网真机验证 |
| 2026-08-07-skill-entropy.md | 1 | Skill²-Bench 迁移刷题机（可选）|
| 2026-08-08-qwen-image-pro.md | 2 | 文字海报商品线 + PPT SOP 成本基准 |
| 2026-08-09-deepseek-v4-flash-arc-prize.md | 1 | 闲鱼文案加 ARC Prize 卖点（待确认措辞）|

### 📋 knowledge/Academic/ — 接单工作流 SOP（模板型）

| 文件 | 待办数 | 说明 |
|:---|---:|:---|
| 接单工作流-SOP.md | 12 | 接单检查清单 + 交付清单（模板，每次接单时对照）|
| 论文Pipeline-数据契约.md | 9 | 质量验收 + 交付清单（模板）|

> **建议**：模板型清单不改，每次接单时复制使用。

### 📋 knowledge/Research/ — 研究行动项

| 文件 | 待办 | 说明 |
|:---|:---|:---|
| 10-Top-AI-Agent-Projects-Deep-Research.md | 5 | n8n/Ollama/kaeru/Dify/Open WebUI |
| code-review-graph-decision-2026-08-05.md | 1 | 与 SimSync 集成 |
| eu-ai-act-2026-08-assessment.md | 1 | 多 Agent 产品三件套 |
| github-trending-2026-08-05-2.md | 5 | croc PAKE/Superpowers/ADR/Pumpkin/likec4 |
| manta-topology-review-2026-08-03.md | 2 | 记录拓扑变更 + 评估 |
| security-risk-assessment-2026-08-02.md | 1 | 多租户容器隔离预研 |
| skill-audit-2026-08-12.md | 3 | 合并重复 + 优化触发词 |

### 📋 knowledge/Archive/ — 发布清单（5 项）

system-comparison-content.md — 博客/视频/封面/对照表/数据记录。已归档内容，发布时对照。

### 📋 projects/ai-blogger/ — AI 博主项目（需人工操作）

| 文件 | 待办数 | 说明 |
|:---|---:|:---|
| content-template.md | 14 | 发布检查清单（模板）|
| README.md | 4 | B站注册/主页/选题/OBS配置 |
| strategy.md | 12 | 分阶段运营计划 |
| tools-setup.md | 5 | 工具检查清单 |

### 📋 research/trackers/ — 研究追踪（6 项）

| 文件 | 待办数 | 说明 |
|:---|---:|:---|
| charm-graph-transfer.md | 3 | CHARM 层次上下文编码研究 |
| kutie-context-injection.md | 3 | 依赖注入方案设计 |

### 📋 docs/ — WPS 练习册检查清单（18 项）

WPS数学练习册标准化优化指南.md — 两份检查清单（页面验收 + 打印验收），每次生成练习册时对照。

### 📋 templates/ — 模板占位符（3 项，不改）

研究笔记模板.md（1）、通用笔记模板.md（2）— 模板内的占位符 `- [ ]`，不修改。

### 📋 system/ — 示例占位符（2 项，不改）

GitHub-Treasure-Hunt-System.md — 示例格式中的占位符，不修改。

---

## 💡 建议

1. **闲鱼上架 8/17 决策日**：素材 100% 就绪，这是连续顺延第 14 天。sora 只需打开闲鱼 App 发布商品（30min）。
2. **Skill 合并**：方案已备好，待 sora 一句话确认即可执行（删除 openclaw-imports 副本）。
3. **"何时启用"类待办**：geolibre/awesome-go/secret-knowledge/trellis 等 4 个文件的 12 项是条件触发参考，建议统一改为 `>` 引用块或加标签区分，避免每日扫描误报。
4. **CloudBase 系列 24 项**：如果短期不打算做微信小程序，可整体标记为「暂缓」减少噪音。

---

*扫描时间：2026-08-13 · 排除 skills/、.github/、memory 历史报告、dreaming/、模板占位符*
