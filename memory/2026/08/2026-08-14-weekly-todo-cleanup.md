# 📋 周度待办清理报告 2026-08-14 (周五)

> 执行时间：2026-08-14 · cron 自动执行  
> 遵循 vault-todo-cleanup skill 流程

## 📊 统计

| 指标 | 数值 |
|:-----|:----:|
| 扫描文件 | 91 |
| 原始 `- [ ]` 匹配 | 367 |
| 实际可执行待办 | ~12 |
| 模板/参考/研究追踪（不修改） | ~355 |
| 本周自动处理 | 12（条件触发参考清单标记） |
| 待 sora 处理 | 5 |
| 我的待办 | 2 |

## ✅ 已自动处理

### 条件触发参考清单标记（12项）

以下文件的 `- [ ]` 是「何时启用」条件触发参考，非真实待办，标记为 `(参考清单)` 防止反复扫描膨胀计数：

| 文件 | 项数 | 说明 |
|:-----|:----:|:-----|
| knowledge/Dev/awesome-go-reference.md | 3 | 接到 Go 开发单时查 |
| knowledge/Dev/geolibre-reference.md | 3 | 接到 GIS/地图需求时查 |
| knowledge/Dev/secret-knowledge-reference.md | 3 | CLI 工具选型/安全排查时查 |
| knowledge/Dev/trellis-3d-reference.md | 3 | 接到 3D 建模需求时查 |
| knowledge/Archive/system-comparison-content.md | 5 | 博客/视频发布清单（草稿状态，非当前执行项） |

### 其他维护
- MEMORY.md 最后更新日期 → 2026-08-14

## ⏳ 待 sora 处理（5项）

### P0 — 闲鱼变现（时间敏感）

| # | 事项 | 截止日 | 状态 | 备注 |
|:-|:-----|:-----:|:----:|:-----|
| 1 | **闲鱼上架决策「上架 or 放弃」** | **8/17 周复盘** | ⚠️ 连续顺延第14天 | 素材包+主图 100% 就绪，仅需 30min 手动上架。距强制决策日剩 **3天** |

### P1 — 确认类

| # | 事项 | 状态 | 备注 |
|:-|:-----|:----:|:-----|
| 2 | 随身WiFi下单（赫电 Pro 399元/年） | 选型已确认 | 待 sora 确认下单 |

### P2 — 执行类（不紧急）

| # | 事项 | 状态 | 备注 |
|:-|:-----|:----:|:-----|
| 3 | 桌面美化部署（TranslucentTB + Rainmeter） | 安装包已就绪 | 待 sora 在本机执行安装 |
| 4 | Skill 重复合并（6组） | 合并方案已备好 | 待 sora 一句话确认即执行 |
| 5 | 小红书发「AI PPT 教程」 | 依赖 PPT 样例素材 | 需 sora 手动导出截图 |

### 顺延关联项（随 P0 决策一并处理）

| 事项 | 依赖 | 文件 |
|:-----|:-----|:-----|
| 同步上架「论文排版/润色」商品 | P0 上架后同批 | projects/current.md L77 |
| 补 PPT 样例素材 | sora 手动导出 | projects/current.md L78 |
| 数学练习册定制文案挂载 | P0 上架后顺带 | projects/current.md L79 |
| 尝试接论文润色/翻译单 | 商品上架后引流 | projects/current.md L83 |

## 🔄 我的待办（2项）

| # | 事项 | 状态 | 备注 |
|:-|:-----|:----:|:-----|
| 1 | 语义缓存落地（LRN-20260801-001） | ⏳ 等待窗口 | 缓解 Tavily 配额，当前靠 5 路冗余降级兜底 |
| 2 | 评估 Hermes `/goal` 持久目标机制 | ⏳ 待评估 | prime-agent-rlm 卡片行动项，需查 Hermes 是否已有此机制 |

## 📋 不修改的模板/参考文件

以下文件含 `- [ ]` 但属于模板/SOP/研究追踪，不纳入清理：

| 类别 | 文件 | 项数 |
|:-----|:-----|:----:|
| 接单 SOP | knowledge/Research/接单工作流-SOP.md | 12 |
| 论文 Pipeline | knowledge/Research/论文Pipeline-数据契约.md | 9 |
| CloudBase 学习 | knowledge/Dev/cloudbase-learning-s1~s8 | ~30 |
| AI 博主策略 | projects/ai-blogger/strategy.md + content-template.md + tools-setup.md | ~30 |
| 研究追踪 | knowledge/Research/* | ~40 |
| 知识卡片 | knowledge/cards/* | ~10 |
| Awesome-Lists | knowledge/Dev/Awesome-Lists-Study.md | 3 |

## 💡 建议

1. **P0 闲鱼上架**：8/17 周日强制决策日只剩 3 天。建议 sora 周末抽出 30min 完成上架，或明确放弃以释放追踪开销
2. **Skill 合并**：方案已备好，sora 说「合并」两个字我就能执行，一劳永逸消除 6 组重复
3. **语义缓存**：Tavily 配额问题本周再次触发（432 次搜索），建议优先落地语义缓存

---
*报告路径: memory/2026/08/2026-08-14-weekly-todo-cleanup.md*  
*由 k 在周度 cron 任务中生成*

---
> 🗺️ 属于 [[knowledge-map]] · [[Home|🏠 Home]]
