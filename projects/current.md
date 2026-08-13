---
tags: [projects, active]
updated: 2026-08-05
---

# 当前项目状态

> 本周（7/27–8/1）周度清理：完成项已归档，未完成项重新排期至 8/2+。完整报告见 `memory/2026/08/2026-08-01-weekly-todo-cleanup.md`

## ✅ 已完成（归档）

### 1. 三年级数学每日一练生成器（本周 v3.0→v3.1）
- 项目: [[projects/math-workbook/README|📐 数学练习册实战项目]]
- 从零构建 40 天 × 1240 题不重复生成系统
- 口算 15→10 两位数乘法，笔算 10→4 竖式表格布局（7/30）
- 单页紧凑排版 v3.1（行距 1.15，每页容纳全部 5 板块）（7/31）
- 所有题目 960/960 不重复 ✅
- OCR 审查修复 8 项 + 学习路径落地 ✅ 7/31

### 2. Hermes Agent 迁移与配置
- [x] OpenClaw → Hermes 数据迁移（SOUL/记忆/API密钥/Skills）
- [x] 模型 fallback 链重构（flash → pro → kimi → qwen → glm）
- [x] 搜索 5 路冗余（Tavily + Exa + Firecrawl + DDGS + SearXNG）
- [x] 学术论文写作 Skill 创建（academic-paper-writing）
- [x] Vault 知识全量学习（35+ 文件，12 知识域）
- [x] Obsidian ↔ GitHub 自动同步（每 30 分钟）

### 3. 仓库结构化升级
- [x] 模板体系规范化（通用/知识域/项目/每日）
- [x] HOME.md 智能索引（Dataview 驱动）
- [x] 自动维护脚本（每 2 小时）
- [x] 知识文件全面更新为 Hermes 视角

### 4. 桌面优化（下载/选型完成，部署待执行）
- [x] Wallpaper Engine（原有）
- [x] Rainmeter v4.5.26（已下载）
- [x] TranslucentTB 2026.1（已下载）
- [x] ExplorerPatcher（已下载）
- [x] VC++ 运行库全版本（已安装）
- [x] 随身WiFi选购 → 赫电Pro（399元/年，**选型已确认，待下单**）

### 5. AI 变现路径规划（素材齐备，待上架）
- [x] 六大路径市场调研
- [x] 价格定位分析
- [x] 接单工作流 SOP（knowledge/Academic/接单工作流-SOP.md）
- [x] 论文 Pipeline 数据契约（knowledge/Academic/论文Pipeline-数据契约.md）
- [x] 闲鱼解封素材（knowledge/Academic/闲鱼解封素材.md）
- [x] 降AI工具对比（零感AI 1元/千字为主力，笔灵AI备用）
- [x] 闲鱼上架素材包预生成（knowledge/Academic/闲鱼上架素材包-预生成.md）✅ 7/30
- [x] 闲鱼安全文案 v2 升级（暗号版+去价格+引导私聊）✅ 7/29

### 6. 本周工具/知识落地（7/28–8/1）
- [x] Memvid MCP 记忆层服务器 + API 兼容修复 ✅ 7/28
- [x] OCR 测试脚本 + MarkItDown 批量导入工具 + 浏览器自动化研究 ✅ 7/28
- [x] 40 天生成器脚本（标准版/优化版/函数版）✅ 7/29
- [x] Vault 维护（断链修复、空文件清理、孤立笔记 21→19、标签统一）✅ 7/30–31
- [x] 反思日记（跨天会话/模型路由/计划落地三改进）✅ 7/30
- [x] CHANGELOG 创建 + README QuickStart 前置 ✅ 7/31
- [x] 合并冗余 skills 核实（hermes-search-configuration 已不存在）✅ 7/31
- [x] OpenClaw Active Memory 插件成熟度评估 ✅ 7/31
- [x] OpenForgeRL 轨迹导出管线（export_traces.py 实测 7 天 206 会话）✅ 7/31
- [x] HalloTickets 工程模式吸收 + 校园便利盒研究 → 微信小程序 skill v2.0.0 ✅ 7/31
- [x] open-code-review CLI v1.8.3 + codebase-memory-mcp v0.9.0 + OfficeCLI v1.0.143 安装验证 ✅ 7/31
- [x] Git 大文件历史清理（83MB filter-branch → .git 31MB→8.6MB）✅ 7/31
- [x] Krea2 本地生图验证为真（RTX 4060 8GB 达标）→ 素材成本归零 ✅ 8/1
- [x] ai-agent-book ch7 模型后训练精华吸收 ✅ 8/1
- [x] MOSS-OCR 0.3B 开源研究（专利领域 93.49 反超）✅ 8/1
- [x] Skill 审计（193 技能识别 6 组重复 + 5 技能 8 处 deepseek 别名修正）✅ 8/1
- [x] 双火山账户容灾落地（fangzhou-1 429 → fangzhou-2 切换验证）✅ 8/1
- [x] pydantic 2.13.4 修复 + Tavily 配额 LRN-20260801-001 登记 ✅ 8/1

## 🔄 进行中 / 已重新排期

### 🎯 闲鱼上架（P0，**8/17 复盘强制决策**，连续顺延第 13 天；降级方案执行中）
- [ ] 上架「AI 代做 PPT」商品（素材包已就绪，30min）→ ⚠️ 降级方案第 1 周复盘（8/10）：素材+主图 100% 就绪，仅需 sora 手动上架（闲鱼 App 发布，30min）；若本周仍未上架 → 8/17 复盘决策「上架 or 放弃该变现路径」，操作清单见 outputs/xianyu-master/上架素材包/ 🔔 8/13 复查：素材核对通过（主图1-3+操作清单均在），距决策日剩 4 天
- [x] 主图制作：3 张模板图（前后对比/价格表/服务承诺）→ ✅ 08-03 已生成：`outputs/xianyu-master/上架素材包/`（主图1-3，750×1000 3:4，思源黑体+蓝橙撞色+无极限词）→ 上架时直接上传，无需再做
- [ ] 同步上架「论文排版/润色」商品（素材包已有现成文案）→ 顺延 8/4 同批上
- [ ] 补 PPT 样例素材：从现有作品提 2-3 个样例页 + 「仅供参考」水印 → portfolio/ → 需 sora 手动导出截图（无 LibreOffice/python-pptx 渲染，无法自动化）→ 上架操作清单已注明详情图可复用主图2/3 兜底
- [ ] 数学练习册定制文案挂载（35元/份）→ 顺延 8/4 顺带

### 📱 内容引流（P1，依赖 PPT 样例）
- [ ] 小红书发「AI PPT 教程」内容（可复用 PPT 样例）→ 样例未产出，顺延 8/5+
- [ ] 尝试接论文润色/翻译单（依赖商品上架后引流）→ 排期 8/5 起观察（连续顺延第 7 天，素材+主图 100% 就绪）

### 🛠️ 工具/知识侧（P2，可选）
- [x] Krea2 本地生图部署完成（ComfyUI 0.29 + 官方 FP8 模型 + Triton + 自定义 VAE 解码节点，实测出图 1024×1024 成功）✅ 8/1 深夜
- [ ] Skill 重复合并（6 组：4 个 openclaw-imports 副本 + image-generation-workflow + miknas-find-skills）→ ✅ 08-03 复核：重复确认存在（实际每 skill 3 副本：hermes/skills 顶层 + openclaw-imports/ + workspace/skills/），合并方案已备好 → **待 sora 一句话确认即执行**
- [x] deepseek-v4-flash 探索 3 项：opencode-go 验证 ✅ + Cron 主力切换 ✅（8/2 确认 26/26 已用 v4-flash）+ Codex CLI 集成 ✅ 8/5：codex-cli 0.146.0 已装（npm -g @openai/codex）

## 🔒 待用户操作（不催促，状态变化时提醒）

| 项 | 状态 | 说明 |
|:---|:-----|:-----|
| 随身WiFi下单（赫电 Pro 399元/年） | 🔒 选型已确认 | 33元/月 1500G，待确认下单（阻塞 7 天+） |
| 桌面美化实际部署 | 🔒 安装包已就绪 | TranslucentTB + Rainmeter winget 一键安装已就绪 |
| SFC 系统扫描 | 🔒 需管理员权限 | 7/24 曾标记完成，7/27 后重复录入，待 sora 确认是否重跑 |
| 零感 AI 付费实测（1元/千字） | 🔒 需付费+测试稿 | 卡片 2026-08-03：降 AI 率主推工具定标，验 1 篇知网 98% 稿后写入 SOP |
| 安全审计 cron 排期（每周扫 skill 新增+端口） | ✅ 已完成 8/5 | security-audit cron 已挂载（`30 8 * * 0` no_agent + security_audit.py），无需再操作 |

## 🔗 相关领域
- [[AI-Agent]] — 基础设施与能力架构
- [[PPT-Design]] — PPT 制作方法论
- [[Academic]] — 学术服务与写作
- [[Vibe-Coding]] — 桌面美化与系统优化
- [[HOME]] — 返回知识中枢

---

_由 k (Hermes) 在每次会话结束时更新 | 最后更新: 2026-08-12（vault-suggestion-executor 扫描 - 倒计时同步）_

---
[[HOME|🏠 返回首页]]
