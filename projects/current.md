---
tags: [projects, active]
updated: 2026-08-21
---

# 当前项目状态

> 本周（8/9–8/15）周度清理：完成项已归档，未完成项重新排期。完整报告见 `memory/2026/08/2026-08-15-weekly-todo-cleanup.md`

## ✅ 已完成（归档）

### 1. 三年级数学每日一练生成器（7/27–8/1）
- 项目: [[projects/math-workbook/README|📐 数学练习册实战项目]]
- 从零构建 40 天 × 1240 题不重复生成系统
- 口算 15→10 两位数乘法，笔算 10→4 竖式表格布局（7/30）
- 单页紧凑排版 v3.1（行距 1.15，每页容纳全部 5 板块）（7/31）
- 所有题目 960/960 不重复 ✅
- OCR 审查修复 8 项 + 学习路径落地 ✅ 7/31

### 2. Hermes Agent 迁移与配置（7/27–8/1）
- [x] OpenClaw → Hermes 数据迁移（SOUL/记忆/API密钥/Skills）
- [x] 模型 fallback 链重构（flash → pro → kimi → qwen → glm）
- [x] 搜索 5 路冗余（Tavily + Exa + Firecrawl + DDGS + SearXNG）
- [x] 学术论文写作 Skill 创建（academic-paper-writing）
- [x] Vault 知识全量学习（35+ 文件，12 知识域）
- [x] Obsidian ↔ GitHub 自动同步（每 30 分钟）

### 3. 仓库结构化升级（7/27–8/1）
- [x] 模板体系规范化（通用/知识域/项目/每日）
- [x] HOME.md 智能索引（Dataview 驱动）
- [x] 自动维护脚本（每 2 小时）
- [x] 知识文件全面更新为 Hermes 视角

### 4. 桌面优化（7/27–8/1，下载/选型完成，部署待执行）
- [x] Wallpaper Engine（原有）
- [x] Rainmeter v4.5.26（已下载）
- [x] TranslucentTB 2026.1（已下载）
- [x] ExplorerPatcher（已下载）
- [x] VC++ 运行库全版本（已安装）
- [x] 随身WiFi选购 → 赫电Pro（399元/年，**选型已确认，待下单**）

### 5. AI 变现路径规划（7/27–8/1，素材齐备，待上架）
- [x] 六大路径市场调研
- [x] 价格定位分析
- [x] 接单工作流 SOP（knowledge/Research/接单工作流-SOP.md）
- [x] 论文 Pipeline 数据契约（knowledge/Research/论文Pipeline-数据契约.md）
- [x] 闲鱼解封素材（knowledge/Research/闲鱼解封素材.md）
- [x] 降AI工具对比（零感AI 1元/千字为主力，笔灵AI备用）
- [x] 闲鱼上架素材包预生成（knowledge/Research/闲鱼上架素材包-预生成.md）✅ 7/30
- [x] 闲鱼安全文案 v2 升级（暗号版+去价格+引导私聊）✅ 7/29

### 6. 工具/知识落地（7/28–8/1）
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

### 7. 本周（8/9–8/15）完成项

**🆕 AI 博主实证测评素材（8/15）**
- [x] AgentScope（小君AI测评）深度测试：抓出「JSON 导入 100% 必挂」严重 bug + 3 中 5 轻问题，修复并提交 PR #3 → https://github.com/Joho6666/xiaojunceping/pull/3
- [x] AI 测评内容素材库建成（10 选题 + 数据弹药：PawBench 工具>模型、价格战一毛钱时代、benchmark 与偏好 r=0.25 等）→ knowledge/Dev/ai测评-内容素材库-2026-08.md
- [x] 《小君AI测评》测评文大纲（标题候选 3 套）→ 素材可直接开写

**🤖 DeepSeek Harness 十轮强化（8/15）**
- [x] 联合工作从「能用」→「可靠」→「有边界认知」：dsh 插件轴 B 无安全设计（40 攻击路径/!!js RCE）、写文件需 DSH_PERMISSION_MODE=danger-full-access、Windows 原生路径、headless 纯文本最稳
- [x] 沉淀技能 hermes-deepseek-harness + 强化记录 knowledge/Dev/hermes-deepseek-harness-十轮强化-2026-08-15.md

**📚 墨题刷题机设计（8/15）**
- [x] P0 错题 AI 诊断设计稿：单题归因已有 80%，补「归因聚合→诊断报告层」；diagnostic_report 聚合 + 水平评估 1-5 + 推荐练习闭环 + 变化视图
- [x] P1 AI 服务层架构设计：ai_router 任务路由 + ai_usage 用量 + 降级链

**🔧 系统/知识基础设施（8/14–15）**
- [x] fallback 链改造：glm-5.2（¥8/M）→ keylink/deepseek-v4-flash 跨 relay 兜底（jiyuanlvdong 挂时切 keylink 而非高价 glm）✅ 8/14
- [x] Skill 链接门禁：skill_link_check.py + cron skill-link-gate（每周一 10:00），首次扫描 301 skill 35 个引用缺口 ✅ 8/14
- [x] Tavily 配额复发（第 2 次，432）→ Firecrawl 无缝接管，5 路冗余降级实测生效 ✅ 8/14–15
- [x] SOUL.md 人设定稿（人格支柱+矛盾张力、负面情绪许可、情感反谄媚、四档关系状态机）✅ 8/15
- [x] 知识域收敛 10→7（Academic→Research、AI→Dev、Design→Hardware）+ MOC 索引合并 ✅ 8/15
- [x] AI 文献周报吸收 5 篇（Embedder's Dilemma / Not Worth Another Token / Beyond Final Scores / AaLLM / Practice Makes Unsafe）✅ 8/15
- [x] Prime Agent 知识卡片（8/14 热榜第一 +12,476⭐；/refine 自改进、Skills=代码与 Hermes 自举同源验证）✅ 8/15
- [x] 模型速查表 + keylink 强模型接入（官方 ID 避坑、v4-pro 性价比王）→ knowledge/Dev/模型速查-2026-08.md ✅ 8/15
- [x] 健康巡检（8/14）：系统基本健康，核心链路在线；4 项待处理

## 🔄 进行中 / 已重新排期

### 🎯 闲鱼上架（P0，**8/18 最后窗口已过 3 天——决策悬置第 20 天**，连续顺延第 19 天）
- [ ] 上架「AI 代做 PPT」商品 → 🔴 **决策悬置第 20 天（8/18 最后窗口已过 3 天）**：素材连续第 10 次核对通过（100% 就绪，8/6 生成无损坏）；决策「上架（30min）or 放弃」，操作清单见 outputs/xianyu-master/上架素材包/
- [x] 主图制作：3 张模板图（前后对比/价格表/服务承诺）→ ✅ 08-03 已生成：`outputs/xianyu-master/上架素材包/`（主图1-3，750×1000 3:4，思源黑体+蓝橙撞色+无极限词）→ 上架时直接上传，无需再做
- [ ] 同步上架「论文排版/润色」商品（素材包已有现成文案）→ 顺延 8/17 同批上
- [ ] 补 PPT 样例素材：从现有作品提 2-3 个样例页 + 「仅供参考」水印 → portfolio/ → 需 sora 手动导出截图（无 LibreOffice/python-pptx 渲染，无法自动化）→ 上架操作清单已注明详情图可复用主图2/3 兜底
- [ ] 数学练习册定制文案挂载（35元/份）→ 顺延 8/17 顺带

### 📝 AI 博主内容（P0/P1，素材已就绪）
- [x] 《小君AI测评》测评文初稿（素材库+大纲+PR 实战全就绪，直接可写；标题候选 3 套）→ ✅ 8/16 已写初稿（约 1700 字：3 坑+PR 故事+竞品对比），见 knowledge/Dev/内容-小君AI测评测评文初稿-2026-08-16.md；发布前需 sora 选标题+配截图
- [ ] 小红书发「AI PPT 教程」内容（可复用 PPT 样例）→ 样例未产出，顺延 8/16+
- [ ] 尝试接论文润色/翻译单（依赖商品上架后引流）→ 排期 8/17 起观察

### 🛠️ 工具/知识侧（P2，可选）
- [x] Krea2 本地生图部署完成（ComfyUI 0.29 + 官方 FP8 模型 + Triton + 自定义 VAE 解码节点，实测出图 1024×1024 成功）✅ 8/1 深夜
- [ ] Skill 重复合并（6 组：4 个 openclaw-imports 副本 + image-generation-workflow + miknas-find-skills）→ ✅ 08-03 复核：重复确认存在（实际每 skill 3 副本）→ **待 sora 一句话确认即执行**
- [x] deepseek-v4-flash 探索 3 项：opencode-go 验证 ✅ + Cron 主力切换 ✅（8/2 确认 26/26 已用 v4-flash）+ Codex CLI 集成 ✅ 8/5：codex-cli 0.146.0 已装（npm -g @openai/codex）


### 🧭 8/18 反思行动项（daily-reflection 2026-08-17 升级，执行者必读）
- [ ] P1 语义缓存最小版落地（同 query 24h 去重中间件，估时 30min）→ 根治 Tavily 配额第 4 次复发（.learnings Recurrence Note 4th confirmation，已顺延 17 天）
- [ ] P1 墨题巡检 git status 硬检查脚本化（未提交改动即报警）→ 把「巡检发现」变「预防」（8/16 反思已列未落地）
- [ ] P1 hermes-health-check 加产物 stat 检查（产出型 cron 当日文件缺失即告警，不标全绿）→ 根治 8-17 五产物缺失被「全绿」掩盖（8/8 同类坑复发）

## 🔒 待用户操作（不催促，状态变化时提醒）
### 🧭 8/20 反思行动项（daily-reflection 复盘 8-19，执行者必读）
- [ ] P0 语义缓存最小版落地——硬截止 8/22（从 P1 升级：Tavily 第 6 次复发 + Gartner 推理成本 5x 预防；同 query 24h 去重中间件，估时 30min）
- [ ] P1 health_provider_check.py 加余额阈值告警（keylink 余额 ¥0.05 险裸奔 + jiyuanlvdong 504×3；余额 <¥1 标红，防「兜底成功」掩盖根因）
- [ ] P1 SRC 侦察收敛：聚焦补天 1 个有效漏洞解锁实战认证，单目标时间盒 2h 超时换目标（联想/小程序/T3 三方向均无有效产出）
- [x] scripts/ 登记表 → ✅ 8/20 反思当场创建 scripts/README.md（杜绝脚本无声消失）

### 🧭 8/21 反思行动项（daily-reflection 复盘 8-20，执行者必读）
- 🔴 语义缓存最小版（同 query 24h 去重中间件）→ **今日落地，截止 8/22 前必须交付**（Tavily 第 7 次复发 + Gartner 推理成本 5x 预防；纯 agent 可执行 30min，本轮反思判定「执行调度缺失」）
- ⏳ 主 provider default 切换 → fangzhou-2 月度配额耗尽（HTTP 429，8/28 才重置），切 deepseek 官方/jiyuanlvdong（436ms 最快；k 可做 10min）
- ⏳ health_provider_check.py 余额阈值告警最小版 → 先做能 fetch 的 provider + fetch 失败标红（连续第 2 轮补齐，keylink ¥0.05 险裸奔收口）
- 🔧 agent 可执行项分类 → projects 待办分「agent 可执行/需 sora」，executor 对 agent 可执行项直接跑（根治「反思≠执行」第 4 复发）

## 🔒 待用户操作（不催促，状态变化时提醒）

| 项 | 状态 | 说明 |
|:---|:-----|:-----|
| 闲鱼上架决策「上架 or 放弃」 | 🔴 决策悬置第 20 天（8/18 窗口已过 3 天） | 素材连续第 10 次核对 100% 就绪；随时可 30min 上架 |
| 随身WiFi下单（赫电 Pro 399元/年） | 🔒 选型已确认 | 33元/月 1500G，待确认下单（阻塞 8 天+） |
| 桌面美化实际部署 | 🔒 安装包已就绪 | TranslucentTB + Rainmeter winget 一键安装已就绪 |
| SFC 系统扫描 | 🔒 需管理员权限 | 7/24 曾标记完成，7/27 后重复录入，待 sora 确认是否重跑 |
| 零感 AI 付费实测（1元/千字） | 🔒 需付费+测试稿 | 卡片 2026-08-03：降 AI 率主推工具定标，验 1 篇知网 98% 稿后写入 SOP |
| DeepSeek 直连充值 | 🔒 余额 ¥7.25 | 8/14 cron 记录；需充值恢复容灾深度 |
| `/new` 开新会话 | 🔒 长会话烧钱 | 「对话历史回顾」1M tokens 接近上限，压缩反复失败 |
| 打开 Obsidian（恢复 MCP） | 🔒 27123 端口无监听 | 依赖 Obsidian 的 cron 会失败 |
| 8/28 确认 fangzhou-2 配额恢复 | 📅 到时提醒 | 月配额 8/28 重置 |
| 安全审计 cron 排期 | ✅ 已完成 8/5 | security-audit cron 已挂载（`30 8 * * 0` no_agent + security_audit.py），无需再操作 |

## 🔗 相关领域
- [[AI-Agent]] — 基础设施与能力架构
- [[PPT-Design]] — PPT 制作方法论
- [[Academic]] — 学术服务与写作
- [[Vibe-Coding]] — 桌面美化与系统优化
- [[HOME]] — 返回知识中枢

---

_由 k (Hermes) 在每次会话结束时更新 | 最后更新: 2026-08-21（daily-reflection cron 复盘 08-20：语义缓存/provider 切换/余额告警三项登记）_

---

[[HOME|🏠 返回首页]]
