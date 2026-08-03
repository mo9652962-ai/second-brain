---
tags: [suggestion-implementation, maintenance, report]
date: 2026-08-03
status: applied
---

# 🧹 建议落实执行报告 · 2026-08-03

> 执行者：vault-suggestion-executor skill（cron，周一）
> 扫描范围：`knowledge/` + `projects/` + `research/` + `concepts/` + `docs/` + `health/`（排除 memory/、.learnings/、skills/）
> 命中：193 处标记 → 分类后真实待办约 30 项

## 📊 总览

| 类别 | 数量 | 处理方式 |
|:-----|:---:|:---------|
| ✅ 可自动执行 | 5 | 全部完成（3 数据核验 + 1 状态确认 + 1 评估） |
| 🔒 需 sora 操作 | 14 | 已标记原因并归集到 projects/current.md 待办表 |
| 📋 模板/触发条件清单 | ~160 | 非待办（SOP 模板、触发词列表、验证清单），跳过 |
| ⏳ 排期未到/条件未满足 | 6 | 记录状态，不动 |

## ✅ 本次执行（5 项）

### 1. 📊 system-comparison-content 数据引用核验（3 项全部通过）
- microsoft/ai-agents-for-beginners：70.5k★（07-31）→ **现 70.8k★** ✅ 增量正常
- datawhalechina/hello-agents：68.9k★（07-31）→ **现 69.8k★** ✅ 增量正常
- 对照表 8 项命中状态与 github-ai-selfstudy-system.md **完全一致** ✅
- 注：GitHub API 直连/代理均 403（代理未开），改用搜索引擎交叉验证

### 2. 🧠 Awesome-Lists-Study Graphify 待办确认完成
- 「研究 Graphify，把代码库转成知识图谱」→ 已落实（07-31 graphify skill + graphify-out/ 产出），标记 [x]

### 3. 🔌 MCP 2026-07-28 规范迁移清单评估（本栈不适用）
- jlc-mcp / codebase-memory-mcp 均为本地进程型无状态 MCP，无 Session-Id / 旧 Tasks / -32002 依赖 → 迁移清单无需执行，已加评估注记；未来新装按「优先 stateless」执行

### 4. 🛠️ Skill 重复合并复核（待确认，已备好方案）
- 确认重复**仍存在且比记录更多**：8051/cad/engineering-workflow/web-dev-2026 各 **3 副本**（hermes/skills 顶层 + openclaw-imports/ + workspace/skills/）+ image-generation-workflow + find-skills×2
- 合并方案：保留顶层规范版，删 openclaw-imports/ 与 workspace/skills/ 副本 → **sora 一句话确认即执行**

### 5. 🚀 Codex CLI 集成预检（排期 8/4+ 未到，不提前执行）
- 环境就绪：node v24.18.0 / npm 11.16.0；codex 未安装 → 排期日执行

## 🔒 需 sora 操作（14 项，已归集到 projects/current.md）

| # | 待办 | 阻塞原因 |
|:-:|------|---------|
| 1 | 闲鱼「AI 代做 PPT」上架（8/3 到期，30min） | 需 sora 在闲鱼 App 操作（素材 100% 就绪，含主图×3，见 outputs/xianyu-master/上架素材包/上架操作清单.md） |
| 2 | PPT 样例页补充（可选） | 需 sora 手动导出截图；详情图可复用主图2/3 兜底 |
| 3 | 论文排版/润色商品同步上架 | 同上，同批操作 |
| 4 | 数学练习册定制文案挂载（35元/份） | 需 sora 操作 |
| 5 | 小红书「AI PPT 教程」 | 依赖 PPT 样例产出 |
| 6 | 论文润色/翻译接单观察 | 依赖商品上架引流，8/4 起 |
| 7 | 随身WiFi下单（赫电 Pro） | 需 sora 确认（**阻塞 7 天+**） |
| 8 | 桌面美化部署 | 需 sora 执行 winget 安装 |
| 9 | SFC 系统扫描 | 需管理员权限 |
| 10 | 零感 AI 付费实测（1 元/千字） | 需付费 + 提供知网 98% 测试稿 |
| 11 | 安全审计 cron 排期 | 方案已备（`0 9 * * 1`），一句话确认即创建 |
| 12 | Skill 重复合并 | 方案已备，确认即执行 |
| 13 | cloudbase-learning s1-s8 实践 | 需 sora 微信云开发环境 |
| 14 | 自托管部署（Activepieces/ActivityWatch/n8n/Ollama 等） | 需 sora 决策部署方案 |

## ⏳ 排期/条件未到（不动）

- Codex CLI（8/4+）、内容发布（B站/掘金/CSDN 账号）、arxiv 试点（周度 digest 负责）、CHARM/kutie tracker（周计划执行中）、对外多租户/多 Agent 三件套（条件触发）

## 📋 排除项（非待办，跳过）

- 接单 SOP / 论文 Pipeline / WPS 指南 / ai-blogger 模板 → 流程模板与验证清单
- awesome-go/geolibre/secret-knowledge/trellis 等 → 触发条件列表
- mattpocock-methodology 检查表 → 永久方法论检查表（设计如此）
- HEARTBEAT.md → 注释模板，设计为空以跳过 heartbeat API（勿填任务）

## 📁 变更文件

| 文件 | 变更 |
|:-----|:-----|
| `knowledge/Content/system-comparison-content.md` | 数据引用核验 3 项 [x] + 实测值 |
| `knowledge/Python/Awesome-Lists-Study.md` | Graphify 待办 [x] |
| `knowledge/Dev/mcp-spec-2026-07-28.md` | 迁移清单加评估注记（本栈不适用） |
| `projects/current.md` | P0 到期标注 + Skill 合并复核 + Codex 预检 + 待办表 +2 行 + 更新日期 |
| `memory/2026/08/2026-08-03-suggestions-applied.md` | 本报告 |

## 下次扫描提示

- 若 8/3 晚间 sora 已上架 → 勾选 P0 5 项
- Skill 合并 / 安全审计 cron 一旦确认 → 立即执行（方案已备）
- Codex CLI 8/4 排期 → 届时按 deepseek 官方 Win 一键脚本安装
