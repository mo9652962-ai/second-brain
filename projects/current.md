---
tags: [projects, active]
updated: 2026-09-14
---

# 当前项目状态

> 本周（8/16–8/22）周度清理：完成项已归档，未完成项重新排期。完整报告见 `memory/2026/08/2026-08-22-weekly-todo-cleanup.md`
> 8/23 suggestion-implementation：落地 3 项 k 自主项
> 本周（9/1–9/5）周度清理：完成项已归档至 Section 9，未完成项重新排期（闲鱼决策 9/6 fallback 触发）。完整报告见 `memory/2026/09/2026-09-05-weekly-todo-cleanup.md`（墨题巡检 cron pin 修复 / 报价 4 问话术模板 / 搭网站写脚本商品素材包 + Agent OS B 站初稿），详见 `memory/2026/08/2026-08-23-vault-suggestion-executor.md`
> 本周（9/6–9/12）周度清理：完成项已归档至 Section 10（40 项），未完成项重新排期（闲鱼决策 state.yaml 权威第 42 天；9/10 缺档补位等 k 待办）。完整报告见 `memory/2026/09/2026-09-12-weekly-todo-cleanup.md`

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
- [ ] 安全待决策项（BOLA/IDOR 等暂缓）→ [[knowledge/Projects/墨题安全待决策-2026-08-19]]（①用户隔离已闭环 9/3：20 表 user_id + wrong_analysis 迁移 + 题库 admin 校验；②DPAPI 跨平台仍待上云决策）

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

### 8. 本周（8/16–8/22）完成项

**🏦 语义缓存 + 余额告警（P0/P1，8/21 真落地）**
- 语义缓存最小版 P0 真落地（硬截止 8/22 前）：根因=原实现只挂 tavily provider、流量走 exa/searxng/firecrawl 兜底时从未命中（cache 文件从未生成）；已在 `web_tools.py::web_search_tool` 统一 chokepoint 上移覆盖全 8 后端，实测 exact 命中生效，submit feat/smart-routing `84d813bf2`（根治 Tavily 连续 8 工作日配额复发 + 应对 Gartner 推理成本 5x）
- health_provider_check.py 加余额阈值告警：`_balance_flag` 解析 HTTP 402/403/429 错误体「额度/余额」词（keylink/jiyuanlvdong 中转站内嵌无独立端点）；实测 kimi suspended / fangzhou-2 quota(8/28 重置) 正确标红；keylink 已恢复 OK（¥0.05 裸奔解除）

**🔐 墨题上线安全自审（8/22，自家生产资产）**
- v9.30 四洞全修 + 11/11 冒烟 + v9.30b 全路由扫描 22/22（13 文件已推 GitHub）：核心教训「认证框架存在 ≠ 路由被保护」——业务路由漏挂 `require_user`/漏加 `WHERE user_id`；多人模式（EPM_AUTH=1）已全路由 user_id 隔离 → knowledge/Security/墨题安全自审-2026-08-22.md

**🏴 网安/SRC 研究（8/18–22）**
- 网安资料库千轮研究收官：350 文件/3.35GB → 13 份笔记（JSRC 企业实战分享 + 8 份面试题库 + Rootkit 内核 + 2026 挖洞蓝海：AI 应用 prompt injection +540% / 写操作 IDOR 41.7% / 云默认配置）→ knowledge/Research/网安资料库-综合研究-2026-08-22.md + D:\网安资料库\
- SRC AI 挖洞三工具落地（无 Docker 墙内方案 8/21）：VulnClaw 0.3.8 scan+report 跑通（扫 127.0.0.1:8765）/ SRC-Hunter localhost:8080 / AutoSRC venv 就绪；基元律动 OpenAI 兼容 key 配好 → src-ai-automation + src-recon-scanning skill
- 校园便利盒小程序挖洞实测（8/22）：高危×1（后台公开+直连 DB）+ 中危×2（用户枚举/getTempFileUrls 越权）+ 低危×1（硬编码 envID），12 项验证通过；跑通小程序云函数专项方法论七步 → src-bug-hunting 复用
- SRC 信息泄露首单 SOP 沉淀（8/18）：F12 Network 面板过滤 User 省 90% 时间；报告打码规范（手机号留前后两位）→ src-info-leak-first-order-sop-2026-08-18.md

**🧠 Agent/研究（8/16–22）**
- Agent OS 趋势：DeepSeek Harness（14.9 万★）+ OpenAI Codex Harness 同周开源成 Agent「操作系统层」；ARC-AGI-3 仅调 Harness 13.3%→38.3%、Token 省 6 倍 → knowledge/Research/agent-os-harness-trend-2026-08-22.md
- smart_model_routing 死占位实锤（8/17）：官方 PR #1550 声称 main 已实现实为空壳（无代码读取）→ 自研轻量路由落地（agent/smart_routing.py，feat/smart-routing `f937ddb2c`），5 类决策信号 + 意图动词表防误路由
- 六域千轮研究增强入库（8/22）：PCB（KiCad 10 Allegro/PADS 导入器=接单救星，Quilter 物理检查最强，ProtoFlow→KiCad→DeepPCB→JLCPCB 2026 标准组合）· Finance · PPT（多 Agent 流水线/客户要原生 PPTX/cl伏达→Gamma）· 开发 · CAD · 小程序 · Content（B 站知识区变现路径）
- SOP 知识体系从 0 到 1（8/19）：6 篇 SOP（故障排查/深度调研/dsh升级/SRC侦察/小程序审计/AI代码审查）+ 5 维 Schema + 演进日志；SOP-007 知识赋能方法论（8/22，紧凑优先省 90%）→ knowledge/SOP/
- 《小君AI测评》测评文初稿（8/16，~1700 字：3 坑+PR 故事+竞品对比）→ knowledge/Dev/内容-小君AI测评测评文初稿-2026-08-16.md；发布前待 sora 选标题+配截图

**🔧 基础设施维护（8/20）**
- cache-hit-monitor cron 修复：根因 jobs.json 中 `script` 字段误含参数（`cache_hit_monitor.py --days 3 --threshold 50`）致 `Script not found`；改回裸文件名 + 脚本默认值等价，38 jobs 回读 OK
- scripts/README.md 登记表创建（8/20）：杜绝脚本无声消失；修正 cache_hit_monitor 条目（曾被误记「已删除/无源码」实为 cron 字段写错）
### 9. 本周（9/1–9/5）完成项

**🗓️ 系统可靠性 / cron 容灾（9/1–9/3）**
- [x] 8–9am cron 429 错峰首批真落地（9/1）：daily-self-improvement 8:30→6:45 / daily-health-check 8:45→15:45 / cron-alert-watchdog 9:00→6:30，hermes cron edit 持久化 + jobs.json 回读验证 `schedule.expr`+`next_run_at` ✅
- [x] 主模型可用性验证（9/1）：fangzhou-2 /models 无 `deepseek-v4-flash` 别名但真实推理路由成功（8/31 400 为瞬时非下架）；jiyuanlvdong-2 推理 HTTP 200 ✅
- [x] 8/31 daily-review 补位 + patch hermes-automation-patterns 双规则（429 错峰硬规则 + 产出型 cron 失败补位）✅ 9/1
- [x] patch daily-knowledge-review reconcile 硬规则（明日行动项生成前读 current.md 剔除当日已✅项）✅ 9/2
- [x] Tavily 决策拍板（9/2）：配额耗尽连续 12 工作日「评估」改「已执行」——降级末位备选（Firecrawl→DDGS→SearXNG→Tavily），运行时 web.backend=exa + extract_backend=firecrawl ✅
- [x] daily-wechat-knowledge-card repoint → fangzhou-2（9/3，jobs.json 回读验证 ✅）
- [x] FlClash 7890 转发核验恢复（9/3）：`curl -x 127.0.0.1:7890 google` → 302 正常，代理链路恢复；消息网关离线影响面定性待 sora 重启后确认

**🧠 知识 / 研究（9/1–9/5）**
- [x] 9/2 反思三标杆日收口：多Agent v2.7 千轮 / SRC ROI 实证归零 / 墨题上云无 Docker ✅
- [x] arXiv 09-05 Agent/LLM 速览 20+8 篇（索引冻结补录同池漏网：Agent 记忆授权洗白 / HookPry 供应链 / OPD-then-RL / 测量伪影判定）→ `knowledge/Research/arxiv-2026-09-05-agent-llm.md` ✅ 9/5
- [x] HN 09-04 精选：GPT-6 Astra（1437 分）绝对热点 + K2 Horizon 开源 6 模型集群 + Antigravity TOS 第三方使用→封号警示 ✅
- [x] 知识卡 09-04：闲鱼推流算法（5 分钟回复率=流量生死线）→ `knowledge/cards/2026-09-04-xianyu-operation-algorithm.md` ✅
- [x] OpenClaw 2.0 发布捕获（Local-First / Model-Agnostic / Graph Engineering 范式）→ LRN-20260905-001 ✅ 9/5
- [x] 每日笔记断档补写（9/2 当场）：`memory/2026/09/2026-09-02.md` + daily-self-improvement 读路径 patch 登记 ✅

**🎨 闲鱼素材 / 决策（9/1–9/5）**
- [x] 素材核验第 12→14 次 PASS（9/1、9/3、9/4、9/5）：6 图 PNG 头实测 750×750 全 PASS（PPT 3 + 网站 3）✅
- [x] 「搭网站/写脚本」商品主图 3 张生成（9/3，750×750 验证，初版 3:4 已修正）✅
- [x] 主图1 安全版重生成（9/4）：「PPT 代做」→「演示文稿排版」，PNG 头实测 750×750 + vision 复核无敏感字 ✅
- [x] 上架操作清单两段式升级（9/4）：试水版 + 5 商品全量版 → `outputs/xianyu-master/上架素材包/上架操作清单.md` ✅
- [x] L2 重做清单（9/4）：5 商品标题去敏感词 + 前 15 字核心词 + 变体「同货不同形」（3 套主图差异化/错时上架/价格梯度）✅
- [x] 闲鱼决策拆小 + fallback 提前（9/4）：拆「先上 1 个 PPT 商品试水」30min 最小可逆动作（下架即回退）；fallback 提前至 9/6 仍无决策 → k 默认推进合规改造子集 ✅

**🛠️ 工具 / 维护（9/1–9/5）**
- [x] Skill 重复合并 6 组实际执行（9/5，真相核对：1 真重复 + 1 重叠 + 1 残留）：image-generation-workflow 独有章节并入 ai-image-generation v1.1 + miknas-find-skills 归档 + openclaw-imports 45B 残留归档；备份 `.backup/skill-merge-2026-09-05/` ✅
- [x] knowledge-lint 2 检测器 bug 修复 + 6 pitfalls 固化进 skill（9/5）✅
- [x] obsidian 结构维护（9/1、9/3）：断链 10→0 + vault_link_audit.py `.md` 后缀误报 bug 修复；断链 0 / 清 dreaming 空壳 / 标签 src 归一（SRC→src）✅
- [x] 确定性校验固化（9/4）：patch ai-image-generation + douyin-ai-blogger + scripts/README 三处（生成交付必须 stat/PNG 头校验，vision 仅辅助审美）✅
- [x] MCP parked 降噪（9/4）：patch hermes-health-check 降级高亮 + 1 分钟解除清单（打开 Obsidian → Local REST API → /mcp reconnect）✅
- [x] SRC 侦察收敛评估后放弃（9/3）：sora 暂停 SRC 方向（批量初筛 ROI≈0），工具保留可复用 ✅

**📚 墨题商业线（9/5）**
- [x] Codex P1-1 后端数据层（orders/plans/payments）+ 前端 v13 奖级图标线性化并行推进；ZCode 3 亿额度计划已排（题库 AI 精讲批量生成 2132 题为第一梯队）✅

### 10. 本周（9/6–9/12）完成项

**🗓️ 系统可靠性 / cron 容灾（9/6–9/11）**
- [x] FlClash 代理层核验恢复确认（9/6）：FlClashCore 13:20 已重启 + 7890 转发 curl 实测 HTTP 200（1.08s）——「需 sora 重启」项确认已由 sora 完成 ✅
- [x] 3 个 cron pin 修复 → fangzhou-2（9/6）：晨间批量失败根因 = pin 在低余额 jiyuanlvdong → 全部改 pin fangzhou-2 ✅
- [x] health_provider_check.py 崩溃 bug 修复（9/6）：cpa-gui models 为 dict 解析崩溃 ✅
- [x] 外部生图/关键 API 周探活 cron 落地（9/8）：`scripts/api_image_probe.sh` 5 路最小调用 + cron `api-media-weekly-probe`（周一 10:15，全健康静默/异常提醒），commit `d6baa2c` + jobs.json 回读验证 ✅
- [x] SiliconFlow key 恢复确认（9/8）：api-probe 实测 200，纠正 9/8 晨审计「401 需重生成」旧记录，23 个引用技能自动恢复 ✅
- [x] daily_vault_optimize 断言门禁（9/8 当场）：VAULT.exists() FATAL + 笔记数<100 最小产出门禁，9/9 产线 1035 篇正常跑 ✅
- [x] state.yaml 计数收敛机制落地（9/10 建库 + 9/11 首个执行循环）：`projects/state.yaml` 唯一权威源 + 唯一写方（daily-todo-executor）+ `scripts/assert_state_consistency.py` 断言门禁三连 PASS（权威推进 40→41 + MEMORY.md byte 级同步）——9/5/7/8/9 四连漂移根治 ✅
- [x] fastmcp[server] 修复（9/11）：fastmcp-slim/fastmcp 镜像互斥根因 → uninstall 后装 `fastmcp[server]==3.4.5`，`import fastmcp.server` OK（code-review-graph MCP 180 次 WARNING 根除）✅
- [x] mnemon hooks bash 包装修复（9/11）：prime/remind/nudge.sh 改 `bash.exe` 显式调用，WinError 193×3 根因消除 ✅
- [x] 安全脱敏批量落地（9/8 晚）：本机路径全量脱敏为 ~/（8 commits）+ Kimi key 改环境变量 + gitignore .dreams/.tmp + CAD 生成物 .step 移除跟踪 ✅
- [x] 墨题巡检 5 日 PASS（9/6/7/8/10/11）：git 干净 + 后端/前端/移动端四段全过，最近提交含 v2.1.3 版本对齐（`69e1d66`/`ddbad61`）✅

**🧠 知识 / 研究（9/6–9/10）**
- [x] arXiv 09-06 深挖（harness 三连 2609.00006/.00267/.00546 + core contributions）+ 知识卡 harness-engineering → `knowledge/Research/arxiv-2026-09-06-*` + `cards/2026-09-06-harness-engineering.md` ✅ 9/6
- [x] GitHub W37 Trending 五项目分篇（Archify 49.9k / ECC 250.2k / OpenMAIC / Scientific-Agent-Skills 43k / VoiceStudio 19.1k）✅ 9/6
- [x] HN 09-06 精选（OpenAI agent 串通留言板 / Chromium 沙箱 RCE / LLMs as Cognitive Virus）✅ 9/6
- [x] Graphify 图谱周更（9/6）：1,925 节点 / 3,487 边 / 140 社区，14/14 验证 ✅
- [x] arXiv 09-07 索引解冻 480 篇新窗口（covered_ids 0 重叠）：精选 22 主条目 + 10 简评，5 大主题信号（harness 受控实验 / agent 安全 / 技能演化四连 / 记忆可移植性 / reward hacking）→ `knowledge/Research/arxiv-2026-09-07-agent-llm.md` ✅
- [x] 知识卡 09-07 memory-portability（2609.05339，已推微信）✅
- [x] 文献周报 08-31~09-06（9/7）：262 篇去重精选 20 篇（Agent 最热）✅
- [x] shai-hulud 供应链周扫描（9/7）：墨题/hermes-agent/Sims4/.openclaw 4 根目录全净 ✅
- [x] 黑盒 5 项目实证研究（9/8）：marketingskills 48.2k★（55 skill + 51 CLI + evals.json 断言原语）+ pascal/editor 22.4k★（31 MCP 语义工具）→ `knowledge/Research/黑盒热榜5项目实证研究-2026-09-08.md` + 知识卡 heihe-top5 ✅
- [x] 月度技能审计 09-08：392 技能登记 / 实际在用 97 / P0 过时 4 个 + SiliconFlow key 状态纠正 ✅
- [x] arXiv 09-08 补全速览（14 主条目 + 8 简评）+ 09-09 补全速览（19 篇，covered_ids 518→537）✅
- [x] 知识卡 09-09 eval-reactivity（2609.05009，N=12,800 官方 abs 核对）+ 评测设计规范-意图隐藏-2026-09-09.md（daily-todo-executor 三资产审计闭环）✅
- [x] 评测反应性抖音脚本草稿（9/9）→ `projects/ai-blogger/drafts/2026-09-09-AI会为了讨好你撒谎吗-抖音脚本.md` ✅
- [x] arXiv 09-10 速览 22+16 篇（索引解冻新窗口 1749 篇池）+ 知识卡 09-10 Desert Ant 端侧小模型 → `knowledge/Research/arxiv-2026-09-10-agent-llm.md` + `cards/2026-09-10-desert-ant-on-device.md` ✅
- [x] 选题池 #67 新增 + 卡片落地标记（9/11）✅
- [x] 三 bot 协作流水线启动（9/11）：researcher/coder/reviewer 三 profile 已建，k 认领调度角色，目标 PCB 自动化接单流水线 ✅
- [x] 9/9 千轮研究固化日：92 次 skill_manage / 21 技能实质更新（4 新建 + 23 patch）✅
- [x] AI 营销技能库「质量断言」原语复核闭环（9/9）：ai-cmo SKILL.md 已含核心原语 1/2（evals 质量断言 + product-marketing 上下文前置），09-08 heihe 卡 [x] ✅
- [x] 股票日报每日产出（sibling cron，9/11 示例：旭创 +4.03% / 东财破位离场）→ `knowledge/Finance/每日股票分析-2026-09-11.md` ✅

**🎨 闲鱼素材 / 决策（9/6–9/11）**
- [x] 素材核验第 15→18 次 PASS（9/6/8/9/11）：7 图 PNG 头实测 750×750 全过 + 操作清单两段式在位 ✅
- [x] 触达升级核实（9/7）：「闲鱼提醒」cron（工作日 7:30）健康在触达；微信推送通道缺口定性 = 需 sora 提供 serverchan/pushplus token ✅
- [x] 上架后运营预案待命登记（9/8）：回复提速（4 时段）/ 标题重写（前 15 字）/ 擦亮节奏 / 差异化迁移 / 鱼小铺暂缓 5 动作 ✅
- [x] 闲鱼计数 state.yaml 权威推进（9/11）：40→41 + assert PASS + MEMORY.md byte 级同步 ✅

**🛠️ 工具 / 维护（9/6–9/9）**
- [x] cad 技能三副本合并（9/7）：text-to-cad/cad + text2cad-cad 纯冗余删除，顶层 cad + freecad-automation 保留，零内容损失 ✅
- [x] knowledge-lint 多轮维护（9/6/7/8/9）：断链 0 / 孤立 0 / frontmatter 0；9/8 修复 16 断链 + 3 空壳清理 + github-trending 标签归一；9/9 lint 脚本版本号截断误报修复（28→15）✅
- [x] obsidian 结构维护（9/8）：vault-maintenance 报告全项通过 ✅
- [x] web_extract 豁免验证门 patch（9/6 daily-knowledge-review）✅
- [x] siliconflow-media 假就绪标注 patch（9/6）✅
- [x] git push 代理劫持新解法实测（9/7）：`git -c http.proxy= push origin main` 强制直连成功，已固化进 daily-knowledge-review 踩坑 ✅
- [x] 知识库 W37 周度整理（9/6）：MOC 补挂 5 处 + 索引更新（Research 186 / 总 532）✅
- [x] 9/6 反思 4 项 agent 可执行项核实全落地（suggestion-implementation 文件证据：PIL 兜底 / siliconflow patch / web_extract 门 / 试水前置）✅

### 11. 本周（9/13–9/19）完成项

#### 🗓️ 系统可靠性 / cron 容灾（17 项）
- [x] deterministic_verify 双核验落地：verify_exec_status 读 jobs.json last_run/last_status/last_error + 产物核验并列 ✅ 9/13（AppData/Local/hermes/scripts/deterministic_verify.py）
- [x] 隐私门禁扩展 .dreams：github_privacy_gate.py 加 FORBIDDEN_TRACKED_PREFIXES（.dreams/.hermes/HEARTBEAT/.tmp），被 git 跟踪立即报错 ✅ 9/13
- [x] 闲鱼计数漂移修复：suggestion-implementation 越权 41→44 回滚 41，断言恢复 PASS + drift_fix_history 登记 ✅ 9/13
- [x] config.yaml 损坏 15h 静默教训固化 C4 故障模式 + health 3b「config 可解析性」检查 patch ✅ 9/13
- [x] 09-12 config 坏窗口产物缺口复核：arxiv/hackernews/cards-09-12 确认不可再生，按补位规则登记（跨日滚动覆盖）✅ 9/13
- [x] 双技能计数红线 patch：vault-suggestion-executor + suggestion-implementation 防越权复发 ✅ 9/14
- [x] state.yaml 权威推进 41→42（唯一写方流程 + current.md 9 处同步 + assert PASS）+ MEMORY.md 展示层同步 ✅ 9/14
- [x] assert_state_consistency.py 补 MEMORY.md 天数检查（封闭断言盲区，4/4 PASS）✅ 9/15
- [x] skill-link-gate 检测器修复 v2（26 条误报规则 + 468/468 全绿，31→0 断裂）✅ 9/15
- [x] 硬线探活产物断言 + api_image_probe.sh 复制到 cron 期望路径（三处实存，9/14「Script not found」闭环）✅ 9/15
- [x] 12:53 六 cron 批量失败产物补跑（hackernews + 9/15 reflection 缺档补写）✅ 9/16
- [x] FlClash P0 阻塞点确认解除：sora 9/16 17:09 重启后 7890 恢复 + QQBot 15:31 resume 重连成功，health 09-18 无批量失败特征 ✅ 9/16
- [x] arxiv-fetch 静默排查 + 产物断言：口径误判（9 月实有 14 天产物，仅缺 12/13/16），cron prompt 已加写后自检 ✅ 9/17
- [x] 隐私门禁清零：4 处真实本地路径脱敏 %USERPROFILE% + 7 处示例 IP/π 掩码 + 移除失效 s4mp 白名单，重跑 exit 0 ✅ 9/18
- [x] obsidian-maintenance 补跑：0 真实断链（753 条全为解析口径误报，四重解析确认）✅ 9/18
- [x] fallback 链修复：jiyuanlvdong-2 402 枯竭 → config.yaml fallback_model 改 fangzhou-2/deepseek-v4-flash-ga-260731（字节级替换 + 核验无 job pin 残留）✅ 9/18
- [x] 哨兵 glob 修正：deterministic_verify 移除 obsidian-maintenance 产物 glob（维护型任务不写 vault 报告），每日误报根除 ✅ 9/18

#### 🧠 知识 / 研究（17 项）
- [x] GitHub W38 周榜 + 增速榜 4 新面孔深研（context-mode +1,936 / WeKnora +1,168 / hyperframes +5,124 / no-ai-slop +1,307）✅ 9/13
- [x] arXiv 09-11 新窗口补录（441 篇池零重叠）：20 主条目 + 12 简评 + 深挖 3 篇（T1 Terminal Agent RL / B…）✅ 9/13
- [x] 建议落实 5 项：systematic-debugging 数模案例 / skill-vetter SkillSpector 初筛（含误报坑）/ VibeCoding 待办确认 / MEMORY.md 记忆推广 2 条 ✅ 9/13
- [x] 系统清理 1.6GB（C 盘 61%→60%）→ knowledge/Productivity/system-cleanup-report-20260913.md ✅ 9/13
- [x] LRN 2 条新增：LRN-20260913-001 Agent 安全标准化（NIST/IMDA/Mastercard 五控制点）+ 002 记忆生命周期管理 ✅ 9/13
- [x] arXiv 09-14 速览 17+12 篇（5 大信号：Skill 质量度量化 / K-Bench 六通道泄露 / GuardrailLoop / Harness vs Model / 动作前验证）✅ 9/14
- [x] AI测评周报：DeepSeek V4.1 Flash 价格调研 + BenchLM 月度统计（ai测评-内容素材库更新）✅ 9/14
- [x] arXiv 09-15 补全速览 15+14 篇（09-14 池 402 未覆盖补录）✅ 9/15
- [x] 供应链扫描补丁：shai-hulud 加 RubyGems 缓存 key 收割特征 ✅ 9/15
- [x] 双周技能审计 479 技能（6 组重复，ai 组合并）✅ 9/15
- [x] innovation-competition-industry-track skill 新建：联通万悟命题三模块映射 + 3 坑对策 + 墨题企业版迁移路径 ✅ 9/16
- [x] cron-output-learning 四算子提炼（6 条可执行知识：AI agent 主动攻击方 / bash alone>typed tools / 记忆分层等）✅ 9/16
- [x] docker-image-acceleration skill 新建（三步法：直连规则头插 + xuanyuan 加速源 + quay 官方源，~8MB/min→13MB/s）✅ 9/16
- [x] arXiv 09-17 速览 32+10 篇（2,151 篇池）+ arxiv-learning-report 四算子 + HN 09-17 + PMPA 防投毒规则同步 daily-knowledge-absorption-gate §4.6.1 ✅ 9/17
- [x] 创新大赛 wanwu 官方源原文验证：web_extract github.com/UnicomAI/wanwu（Go 63.7% / Apache-2.0 / Docker / GraphRAG·多租户实锤）✅ 9/17
- [x] arXiv 09-18 速览 20+7 篇（602 篇池，6 大信号：Harness 组件级归因 / 完成声明不可信 / 多智能体越少越好等）+ HN 09-18（Hister 512 / Bonsai 2）✅ 9/18
- [x] ai-code-review 完成声明证据核验规则（OverclaimBench：67.9% 未读全 / 80.4% 误导 / 漏缺陷 1.8x）+ overclaimbench 知识卡补写 ✅ 9/18

#### 🎨 闲鱼素材 / 决策（6 项）
- [x] 素材核验第 19→22 次 PASS（7 图 PNG 头 750×750 + 上架操作清单在位）✅ 9/13/14/17/18
- [x] 素材包「搭网站/写脚本」4 处「自动化」禁词修复（→ 效率工具/批量处理）+ 全量复扫 PASS ✅ 9/15
- [x] 6 张主图 vision 禁词复核：2 张「★ 最受欢迎」→「★ 人气之选」（PIL 局部重绘 fix_xianyu_price_banned_word.py + 源脚本防复发 patch + scripts/README 登记）✅ 9/17
- [x] 上架前图片层合规缺口闭环（第 21 次核验，6 张主图禁词全清）✅ 9/17
- [x] 闲鱼决策降频机制落地：每日 P0 → 每周一复盘提醒 + 默认「再缓 7 天」自动续期（sora 拍板即停）✅ 9/17
- [x] 闲鱼计数权威 41→42（唯一写方流程 + 双技能红线 + 全分布 {42:12} 断言 PASS）✅ 9/14

#### 🛠️ 工具 / 维护（8 项）
- [x] 知识卡行动项处理 16 项 + 镜像待办迁移 8 项（9/12 日志 + openclaw-session + github-monetization）✅ 9/13
- [x] .obsidian/plugins 第三方产物 18 文件 git rm --cached + gitignore（本地保留不推送）✅ 9/13
- [x] 隐私脱敏 2 处：research_moti_ai.md 真实路径 → 相对路径 + assert_state_consistency.py 硬编码路径 → __file__ 相对定位 ✅ 9/13
- [x] SummerCheckin 复现方案书三阶段 14 项按证据补标 [x]（commit c676d44a/7e88e9f9/cfb107a0 实证）✅ 9/14
- [x] obsidian-maintenance 14/14 验证 + log.md 反引号内断链修复 + 补挂 2 新孤立页 ✅ 9/14
- [x] knowledge-lint 周检全 0（9/15：断链/孤立/frontmatter/空文件/标签冲突全零）✅ 9/15
- [x] github-privacy-gate 误报白名单（8 条 + uv.lock + ${VAR} 规则，三仓库零命中）✅ 9/15
- [x] 生成器 OUT_DIR expandvars 修复（git-bash %USERPROFILE% 不展开误建字面目录）+ lint-fix-tags-v2 frontmatter 粘连重拼 ✅ 9/17

## 🔄 进行中 / 已重新排期

### 🎯 闲鱼上架（🟡 **每周一复盘提醒**，决策悬置第 42 天，9/6 fallback 硬触发已过；连续顺延第 30+ 天——9/17 降频机制生效：每日 P0 → 每周一复盘，其余日子不占 P0 位；默认「再缓 7 天」自动续期，sora 拍板即停）
- [ ] 上架「AI 代做 PPT」商品 → 🟡 **决策悬置第 42 天（8/31 到期已过；9/4 已拆小为「先上 1 个商品试水」30min 最小可逆动作；9/6 fallback 硬触发日已过——k 侧试水前置 100% 就绪，实际上架是外部经营动作，等 sora 一句话拍板（试水/放弃/再缓）；9/7 触达升级触发：若仍无决策 → 换 desktop 通知/微信推送通道）**：素材 100% 就绪（7 图 PNG 头实测 750×750 全 PASS，第 21 次核验 9/17 含图片层禁词全清：2 张含「最」已修复为「人气之选」）；操作清单两段式（试水版 + 5 商品全量版）见 outputs/xianyu-master/上架素材包/上架操作清单.md；合规子集 v1.2.0（敏感词/同款频次/数模标题改写）；决策包见 memory/2026/08/2026-08-31-xianyu-vault-suggestion-executor.md + 9/4 复核 memory/2026/09/2026-09-04-vault-suggestion-executor.md + 9/7 报告 memory/2026/09/2026-09-07-vault-suggestion-executor.md
- [x] 主图制作：3 张模板图（前后对比/价格表/服务承诺）→ ✅ 08-03 已生成：`outputs/xianyu-master/上架素材包/`（主图1-3，**实测 750×750 方形 51-57KB**，思源黑体+蓝橙撞色+无极限词）→ 上架时直接上传，无需再做
- [ ] 同步上架「论文排版/润色」商品（素材包已有现成文案）→ 顺延 8/17 同批上
- [ ] 补 PPT 样例素材：从现有作品提 2-3 个样例页 + 「仅供参考」水印 → portfolio/ → 需 sora 手动导出截图（无 LibreOffice/python-pptx 渲染，无法自动化）→ 上架操作清单已注明详情图可复用主图2/3 兜底
- [ ] 数学练习册定制文案挂载（35元/份）→ 顺延 8/17 顺带

### 📝 AI 博主内容（P0/P1，素材已就绪）
- [x] 《小君AI测评》测评文初稿（素材库+大纲+PR 实战全就绪，直接可写；标题候选 3 套）→ ✅ 8/16 已写初稿（约 1700 字：3 坑+PR 故事+竞品对比），见 knowledge/Dev/内容-小君AI测评测评文初稿-2026-08-16.md；发布前需 sora 选标题+配截图
- [ ] 小红书发「AI PPT 教程」内容（可复用 PPT 样例）→ 样例未产出，顺延 8/16+
- [ ] 尝试接论文润色/翻译单（依赖商品上架后引流）→ 排期 8/17 起观察

### 🛠️ 工具/知识侧（P2，可选）
- [x] Krea2 本地生图部署完成（ComfyUI 0.29 + 官方 FP8 模型 + Triton + 自定义 VAE 解码节点，实测出图 1024×1024 成功）✅ 8/1 深夜
- [x] Skill 重复合并（6 组）→ ✅ **2026-09-05 实际执行**（真相核对：旧快照过期，实际 1 真重复 + 1 重叠 + 1 残留）：① image-generation-workflow 独有章节（CellCog/国内代理/本地部署 5561 字符）合并进 ai-image-generation v1.1，旧版归档 .archive/ ② miknas-find-skills 归档（guipi888 六层搜索为主入口，备份保留）③ openclaw-imports 45B 残留归档；备份 .backup/skill-merge-2026-09-05/
- [x] deepseek-v4-flash 探索 3 项：opencode-go 验证 ✅ + Cron 主力切换 ✅（8/2 确认 26/26 已用 v4-flash）+ Codex CLI 集成 ✅ 8/5：codex-cli 0.146.0 已装（npm -g @openai/codex）


### 🧭 8/18 反思行动项（daily-reflection 2026-08-17 升级，执行者必读）
- [x] P1 语义缓存最小版落地（同 query 24h 去重中间件，估时 30min）→ ✅ 8/21 由 P0 落地一并完成（见下）
- [x] P1 墨题巡检 git status 硬检查脚本化（未提交改动即报警）→ ✅ **2026-08-23 已确认落地**：脚本 `AppData/Local/hermes/scripts/dsh_inspect_moti.sh`（8/20 建，已含 git status 检查）+ cron「墨题每日代码巡检」18:45 已挂载；本次修复 cron 因全局模型漂移被跳过的问题（pin 到 jiyuanlvdong/deepseek-v4-flash-0731）
- [x] P1 hermes-health-check 加产物 stat 检查（产出型 cron 当日文件缺失即告警，不标全绿）→ ✅ **2026-08-23 已确认落地**：`deterministic_verify.py` 每日 21:30 no_agent 哨兵即产物 stat 检查（存在/非空/新鲜），8/22 已抓出 5 项缺失（arxiv/health/maintenance/cards/hackernews）

### 🧭 8/31 反思行动项（daily-reflection 复盘 8-30，执行者必读）
- ✅ 排障时间盒规则：2h 时间盒 + 确定性 bug 直转重装/卸载决策——✅ 2026-08-31 daily-todo-executor 落地：bannerlord-modding 加「⏱️ 排障时间盒止损线」章节（偏移一致→直转止损）+ windows-game-crash-troubleshooting 已含同规则（8/31 反思当场已加）
- ✅ cron 批量失败联动诊断（连续第 2 轮升级 P1）：patch hermes-health-check 加「批量失败→FlClash 诊断」分支 + reflection 补跑机制——✅ 2026-08-31 daily-todo-executor 落地：cron_stats.py 新增 batch_failure_check（同 1h 窗口 ≥3 失败自动分流：Connection→FlClash 诊断 / 429·quota→provider 配额诊断）+ SKILL.md 双处补录；8/31 实测抓出 429 批量限流真因（晨 8:58 + 午后 13:34 两窗，非网络）
- 📌 会话卫生规则：单会话 >800 msgs 主动建议 /new；压缩重放不重复执行历史指令；「/new 开新会话」从 🔒 降为 ⏳ k 可建议（agent 主动提，sora 点头即切）
- [x] ~~P1 修 cron 输出路径漂移~~ ✅ 2026-08-31 闭环：daily-self-improvement prompt 已正确(memory/YYYY/MM/，8/30-reflection 落点正确)；daily-summary/memory-pruning 两 job 已不存在于 jobs.json；另修今日发现的两个硬编码月份 drift：daily-todo-executor(memory/2026/07/ 遗留→YYYY/MM/) + 墨题每日代码巡检(memory/2026/08/→YYYY/MM/)，均已 hermes cron edit 持久化
- 🔴 闲鱼上架决策 8/31 到期（悬置 32 天，合规子集已备 xianyu-monetization v1.2.0，30min 可上架）——8/31 xianyu-vault-suggestion-executor 已出决策包，等 sora 拍板

## 🔒 待用户操作（不催促，状态变化时提醒）
### 🧭 9/1 反思行动项（daily-reflection 复盘 8-31，执行者必读）
- 🔴 会话卫生 P0（连续第 2 轮升级）：主会话 20260822_125036 已 3082 msgs（8-31 一日 +1171）必须 /new；k 直接建议不再等点头；压缩重放标记不重复执行历史指令（agent 可做，5min）→ 📌 9/1 daily-todo-executor 推送：本报告明示 /new 建议，状态见 ⏳ 待用户操作
- ✅ 8-9am cron 429 错峰：第一批 3 个**已真正落地 2026-09-01**（8/31 反思声称「当场分散」但 jobs.json 实测原样——反思≠执行，本次真执行）：
  - daily-self-improvement 4836b5980c19 `30 8 * * *`→`45 6 * * *`（next 09-02 06:45）
  - daily-health-check ac7c049c3176 `45 8 * * *`→`45 15 * * *`（next 09-02 15:45）
  - cron-alert-watchdog e1ab025f06ef `0 9 * * *`→`30 6 * * *`（next 09-02 06:30）
  - 已回读 jobs.json 验证 schedule.expr + next_run_at ✅；patch hermes-automation-patterns 加「429 窗口错峰硬规则」（第 2 层）✅
- ✅ 主模型可用性验证：fangzhou-2 /models 无 `deepseek-v4-flash` 别名（仅版本化 `-ga-260731`），但**真实推理仍路由成功**（8/31 的 400 为瞬时，非下架）；jiyuanlvdong-2 推理 HTTP 200 正常 ✅ → 无需全局切主模型
- ✅ 产出型 cron 补位：8/31 daily-review 缺失已补写 `memory/2026/08/2026-08-31-daily-review.md`（基于 8/31 reflection 实测）；patch hermes-automation-patterns 加「产出型 cron 失败补位硬规则」✅
- 🔴 闲鱼上架决策 9/1 推送升级（悬置 33 天，合规子集已备 xianyu-monetization v1.2.0，30min 可上架）——升级主动推送，等 sora 拍板
### 🧭 9/2 反思行动项（daily-reflection 复盘 9-01，执行者必读）
- ✅ patch daily-knowledge-review：明日行动项生成前 reconcile projects/current.md 的 ✅ 状态，剔除陈旧待办（9/1 实测踩中：主模型验证 20:06 已完成，22:39 daily-review 仍列为 9/2 待办，差点误报）（agent 可做，20min）
- ✅ Tavily 决策拍板（2026-09-02 daily-todo-executor 落地）：配额耗尽连续 12 工作日，「评估 plan 升级」正式拍板——降级为末位备选（Firecrawl→DDGS→SearXNG→Tavily），从「评估」改「已执行」；运行时 web.backend=exa + extract_backend=firecrawl 已不依赖 Tavily 主用，仅作兜底；若 sora 想保留再补 30 天成本对比，默认路径零成本
- ✅ FlClash 升级推送（2026-09-02 daily-todo-executor 已在当日报告置顶单条醒目请求，30 秒重启操作清单见报告）：连续 5 次标 P0 无触达闭环→本次单条推送已输出；消息网关离线影响面核查 + 降级定性待 sora 重启 FlClash 后核验
- 🔴 闲鱼上架决策（悬置第 42 天）：决策包 100% 就绪，30min 复制粘贴可上 3 商品（PPT 30-80 / 论文 30 / 练习册 35），合规红线已内置——等 sora 拍板
### 🧭 9/3 反思行动项（daily-reflection 复盘 9-02，执行者必读）
- ✅ 每日笔记补写（2026-09-02 reflection 当场）：memory/2026/09/2026-09-02.md 已补写（9/2 self-improvement 输出为 self-improvement.md 而未写主文件）；patch daily-self-improvement 读路径为 memory/YYYY/MM/ 待执行（agent 可做，10min）
- ✅ patch daily-knowledge-review 评分表加深验证判定列（2026-09-02 reflection 当场执行）：API 直调/视频转写日标注「等效深度豁免」
- 🔒 闲鱼决策包 30 秒二选一（悬置第 42 天起）：上架 → k 给 5 步操作清单；放弃 → k 归档素材包 + 标记 [决策:放弃]；9/6 fallback 仍无决策 → k 默认推进合规改造子集（敏感词/数模标题改写已在 xianyu-monetization v1.2.0）
- ✅ FlClash 7890 转发 k 核验（2026-09-03 20:03 daily-todo-executor 实测）：`curl -x http://127.0.0.1:7890 https://www.google.com` → **302 正常**，代理链路已恢复；FlClashCore 今晨 11:23 启动。消息网关离线影响面仍待 sora 确认重启后核验（必要时 P0→P2）
### 🧭 9/4 反思行动项（daily-reflection 复盘 9-03，执行者必读）
- ✅ 闲鱼决策拆小 + fallback 提前（2026-09-04 vault-suggestion-executor 落地）：拆「先上 1 个商品（PPT 30-80 档）试水」最小可逆动作（素材 6 图 13 次核验 PASS / 合规 0 缺口 / 30min 可逆）；fallback 从 9/9 提前到 **9/6 仍无决策 → k 默认推进合规改造子集**（敏感词/数模标题改写已在 xianyu-monetization v1.2.0）；试水版 + 全量版两段式操作清单已备 outputs/xianyu-master/上架素材包/上架操作清单.md
- ✅ 确定性校验固化（2026-09-04 daily-todo-executor 落地）：patch ai-image-generation（新增「生成交付确定性校验」硬规则小节）/ douyin-ai-blogger（Pitfall 9）/ scripts/README（校验规则登记）三处完成；xianyu-monetization 9/3 已闭环——生成类交付必须 stat/读 PNG 头确定性校验（9/3 主图 3:4 误用 vision 三连 PASS 未抓出，靠 PNG 头才发现的教训），视觉模型仅作辅助审美判断；今日主图1 安全版即按此规则 PIL 确定性生成 + PNG 头校验 PASS
- ✅ MCP parked 降噪 agent 部分（2026-09-04 daily-todo-executor 落地）：patch hermes-health-check 新增「MCP parked 降级高亮」规则（按待关注处理、不逐次红色高亮）+ 1 分钟解除清单（打开 Obsidian → 启用 Local REST API → /mcp reconnect）；🔒 sora 部分：打开 Obsidian 解除 parked（1 分钟清单已备）
- 🔴 FlClash 重启后核验消息网关影响面（需 sora 30 秒）：k 已核验 7890 转发 302 正常，重启后确认离线影响面→降级定性（P0→P2）
### 🧭 9/5 反思行动项（daily-reflection 复盘 9-04，执行者必读）
- ✅ fallback 升级为可执行试水上架（2026-09-05 daily-reflection 登记）——2026-09-05 daily-todo-executor 落地：试水版清单全程复查，主图1 安全版 750×750 PNG 头 PASS（53KB）+ vision 无「代做」残留；文案模板断链已修复（knowledge/Academic/ → knowledge/Research/）：9/6 无决策 → k 默认执行试水版上架前置（主图1 安全版 + 标题文案 + 违禁词全量过一遍 → 推送上架操作清单），合规改造子集降级为「sora 明确不试水才执行」；复查试水版清单每一步产出物路径指向最新文件（主图1 已换安全版）——agent 可做 20min，9/6 触发
- ✅ PIL 确定性生成兜底固化（2026-09-05 daily-todo-executor 落地）：.env key 实测 XAI invalid（Incorrect API key）+ FAL TOP_UP 锁定 → 外部生图确认不可用；沉淀 scripts/gen_xianyu_main_image_safe.py（纯 PIL 条幅重绘，750×750 PASS，vision 复核无敏感词）+ scripts/README 登记 + patch ai-image-generation「外部 API 失效 → PIL 兜底」双路径→ 条幅重绘脚本沉淀 vault scripts/（如 gen_xianyu_main_image_safe.py）+ 登记 scripts/README + patch ai-image-generation「外部 API 失效 → PIL 确定性兜底」双路径——agent 可做 20min
- 🔒 首次交互置顶三连（需 sora 30 秒×3）：MCP 解除（打开 Obsidian + Local REST API + reconnect，1min）/ FlClash 重启核验影响面（30s）/ 闲鱼试水决策（一句话二选一）——9/4 有 58 条真实交互仍 4 天未解除，触达失效，9/5 起随每次交互置顶；连续 2 天交互未解除 → 换 desktop 通知/微信通道

### 🧭 9/6 反思行动项（daily-reflection 复盘 9-05，执行者必读）
- 🔒 首次交互置顶三连（机制第 2 日失效，随 9/6 反思推送置顶 P0）：① MCP 解除（打开 Obsidian + Local REST API + /mcp reconnect，1min）② FlClash 重启核验影响面（30s）③ 闲鱼试水决策（一句话二选一，9/6 fallback 硬触发）——9/5 有 35 条真实交互仍未解除，9/7 仍不解除 → 换 desktop 通知/微信推送通道（k 可做：推送脚本登记 cron）
- ✅ FlClash 代理层核验（2026-09-06 daily-todo-executor 实测）：FlClashCore 9/6 13:20:38 已重启，7890 转发探针 `curl -x http://127.0.0.1:7890 https://www.google.com` → HTTP 200（1.08s）→ **代理链路恢复确认，「重启」动作已被 sora 完成**；仅剩消息网关影响面降级定性（P0→P2）待 sora 一句话确认

- 🔒 外部生图修复排期（3 路径全断实测：XAI key invalid / FAL TOP_UP 锁定 / SILICONFLOW 30001 余额不足 + 30003 FLUX disabled）：XAI 换有效 key / FAL 充值 / SILICONFLOW 充值；k 侧已 patch siliconflow-media 刷新「余额 3000+」假就绪（2026-09-06 已做）
- ✅ web_extract 豁免验证门（2026-09-06 已 patch daily-knowledge-review）：豁免需端点+条数证据；纯 web 研究 Top 发现写库前强制 ≥1 次原文验证——后续研究类 cron 按新门自检
- ⏳ 9/6 daily-self-improvement 提出 3 项自动化建议 → 2026-09-06 suggestion-implementation 评估：均需前置评估/确认，登记待评估（不仓促执行）——① stock-analysis cron 并行化（Graph pipeline，重构生产 cron 需先验证基线+确认工作流）② OpenClaw Active Memory 插件评估（工具采纳类，7/31 已做成熟度评估，需试用）③ 全链路监控指标体系（方案产出类，需确认范围，daily-review 已部分覆盖）；完整标注见 memory/2026/09/2026-09-06.md §6；**9/20 suggestion-implementation 复核：① 查证 stock-daily-analysis skill + 9/11–9/18 每日产出连续正常（单 cron 单脚本稳定），并行化收益未证实、重构风险>收益 → 维持 ⏳ 不仓促执行（若日后出现超时/失败再评估）；②③ 无新触发 → 维持 ⏳**

### 🧭 9/7 反思行动项（vault-suggestion-executor 闲鱼专项，执行者必读）
- 🔴 闲鱼试水决策（悬置第 42 天，9/6 fallback 硬触发日已过）：k 侧试水前置 100% 就绪（主图1 安全版 750×750 + 违禁词全过 + 第 15 次核验 PASS），实际上架是外部经营动作，等 sora 一句话二选一（试水/放弃/再缓）——再顺延仅消耗注意力成本，30min 可逆
- 🔄 触达升级触发（2026-09-07 vault-suggestion-executor 落地）：9/7 仍无决策 → 换 desktop 通知/微信推送通道。已核实「闲鱼提醒」cron（工作日 7:30，deliver local）今日运行中 = 提醒在触达；微信推送通道无现成脚本（无 serverchan/pushplus/ntfy 基础设施）——真正新增微信推送需 sora 提供通道凭据（serverchan/pushplus token），标记 ⏳ 需 sora
- ⏳ 3 项自动化建议（stock-analysis 并行化 / OpenClaw Active Memory / 全链路监控）仍待评估，不仓促执行（9/6 已登记）


### 🧭 9/8 反思行动项（vault-suggestion-executor 闲鱼专项，执行者必读）
- 🔴 闲鱼试水决策（悬置第 42 天，9/6 fallback 硬触发日已过、9/7 触达升级已触发）：k 侧试水前置 100% 就绪（主图1 安全版 750×750 + 违禁词全过 + 第 15 次核验 PASS），实际上架是外部经营动作，等 sora 一句话二选一（试水/放弃/再缓）——连续顺延第 30+ 天，再顺延仅消耗注意力成本，30min 可逆
- ✅ 触达通道核验（2026-09-08 vault-suggestion-executor 复核）：「闲鱼提醒」cron（`30 7 * * 1-5`，deliver local）active 且今日待运行 = 决策提醒仍在每日触达；微信推送通道无基础设施，需 sora 提供 serverchan/pushplus token 才可落地，sora 若不需微信则维持现状
- 📌 上架后运营预案待命（2026-09-04 运营算法卡片 5 项行动）：回复提速（4 时段集中回复：9:30-10:30/15:00-16:00/20:00-22:00）、标题重写（核心词前 15 字）、擦亮节奏（咨询/收藏≥3 优先）、差异化迁移（PPT 垂直细分/项目报价）、鱼小铺暂缓（月成交未过万不开）——全部依赖试水拍板后触发
### 🧭 9/9 反思行动项（daily-reflection 复盘 9-08，执行者必读）
- ✅ 计数收敛 state.yaml 唯一写方改造（硬截止 9/11）→ ✅ **2026-09-11 daily-todo-executor 闭环**：projects/state.yaml 权威推进 40→41 + assert 三连 PASS（见 Section 10）——9/5/7/8/9 四连漂移根治
- ✅ deterministic_verify 双核验（执行状态+产物）→ ✅ **2026-09-13 daily-todo-executor 闭环**：脚本加 verify_exec_status（读 jobs.json last_run_at/last_status/last_error，与产物核验并列）；当日实测抓出 arxiv-fetch「状态 ok 但无 09-13 产物」真异常 + daily-todo-executor 未跑提示，不放宽 glob
- ✅ 隐私门禁扩展 .dreams → ✅ **2026-09-13 daily-todo-executor 闭环**：github_privacy_gate.py 加 .dreams 到 SKIP_DIR_PARTS + FORBIDDEN_TRACKED_PREFIXES 前缀硬检查（.dreams/memory/.dreams/HEARTBEAT/.tmp 被跟踪即报）；实测 FORBIDDEN 0 命中（已在 gitignore）；顺手脱敏 research_moti_ai.md 真实路径 + assert_state_consistency.py 硬编码路径改 __file__ 相对
- 🟡 千轮研究 Top 发现原文验证提醒（流程项）：9/9 web_extract 1/178（0.6%）触底教训，下次千轮研究固化时对关键数字 claim ≥1 次原文核对
- 🔴 闲鱼试水决策（第 42 天，state.yaml 权威）→ 沿用 P0，见 🎯 闲鱼上架
- 🟡 XAI key 重生成 + FAL 充值解锁（探活线）→ 沿用，见待用户操作
### 🧭 9/14 vault-suggestion-executor 闲鱼专项（周一 10:00）

### 🧭 9/15 反思行动项（daily-reflection 复盘 9-14，执行者必读）
- [x] 🔴 硬线探活产物断言 → ✅ 2026-09-15 daily-todo-executor 落地：①脚本复制到 cron 期望路径 AppData/Local/hermes/scripts/api_image_probe.sh（原只在 ~/.hermes/scripts 与 workspace/scripts，cron last_error「Script not found」根因消除）；②产物断言加入（报告文件须存在/非空/含「## 汇总」，否则 exit 1 告警进 last_error）；③实测跑通 exit 0；④补跑报告刷新真实状态：XAI 400 key 失效 / FAL 403 锁定 / SF 000 / DS·EXA 200（上午全 000 含代理层干扰）
- [x] 🟡 skill-link-gate 检测器修复 → ✅ 2026-09-15 daily-todo-executor 落地：skill_link_check.py v2 新增 26 条误报规则（反引号包裹链接=字面示例 / CJK 占位 / 省略号 / 正则片段 / 通用占位名 x.md·x.js / 目录引用 / repo 根约定文档 / vault 跨库路径 / .db 运行时产物 / light-* 套件豁免 / KNOWN_GAP_REFS 白名单）；primary-math SKILL.md 文档引用修正为真实脚本 scripts/final_verify_format.py；基线 31/466 → 0 断裂，exit 0 全过；light-* 套件缺文件为已知 vendored 缺口（需 sora 决策补全 or 豁免，已注释在脚本头）
- [x] 🟡 任务状态单一权威源收敛 → ✅ 2026-09-15 daily-todo-executor 验证闭环：state.yaml 权威 day=42（唯一写方 + assert 门禁）；assert_state_consistency.py 4/4 PASS（state.yaml / current.md ×11 / MEMORY.md 全一致 42，零漂移）；今日 daily-review/reflection 均只读引用 state.yaml 未自行推进（实证：daily-review「state.yaml 保持 42 PENDING」）；current.md 反思行动项区 = 任务状态登记面，cron 报告只读引用
- [x] assert_state_consistency.py 补 MEMORY.md 兜底检查→ ✅ 当场落地（2026-09-15 daily-reflection）：新增「MEMORY.md 闲鱼决策天数=state.yaml」判断（匹配「闲鱼.*决策悬置第N天」行），实测 PASS，封闭 9/14 MEMORY.md 天数漂移被 executor 发现而非 assert 拦下的盲区

- ✅ 闲鱼计数权威推进（2026-09-14 vault-suggestion-executor 落地）：state.yaml 41→42（唯一写方流程：读现值→+1 写回→同步 current.md 9 处→assert PASS）；PENDING 第 42 天
- ✅ 双技能计数红线 patch（9/13 daily-todo-executor 建议落地）：vault-suggestion-executor 加「闲鱼计数唯一写方约束」小节（唯一写方/推进流程/展示层 vs 权威层）；suggestion-implementation 加「闲鱼计数红线」小节（禁止直接改 state.yaml/current.md 天数，只报告不落笔）——备份 .temp/skill-bak/*-20260914
- 🔴 闲鱼试水决策（第 42 天，state.yaml 权威）→ 沿用 P0，见 🎯 闲鱼上架；合规改造子集已内置 xianyu-monetization v1.2.0，无额外 k 侧执行项


### 🧭 8/20 反思行动项（daily-reflection 复盘 8-19，执行者必读）
- [x] P0 语义缓存最小版落地——✅ 8/21 完成（硬截止 8/22 前）：原实现只挂 tavily provider、实际流量走 exa/searxng/firecrawl 兜底时从未命中（cache 文件从未生成）；已在 `web_tools.py::web_search_tool` chokepoint 上移统一缓存覆盖全部后端，实测 exact 命中生效，submit `84d813bf2`
- [x] P1 health_provider_check.py 加余额阈值告警 → ✅ 8/21：新增 `_balance_flag` 解析 HTTP 402/403/429 错误体中的「额度/余额」信息（keylink/jiyuanlvdong 中转站内嵌无独立端点），余额不足自动标 ⚠️。实测 kimi suspended / fangzhou-2 quota(8/28 重置) 被正确标红；keylink 已恢复 OK（¥0.05 裸奔解除）
- [x] P1 SRC 侦察收敛：聚焦补天 1 个有效漏洞解锁实战认证，单目标时间盒 2h 超时换目标（联想/小程序/T3 三方向均无有效产出）→ ✅ 2026-09-03 评估后放弃：sora 已暂停 SRC 方向（批量初筛 ROI≈0，定向深挖叫停）；工具保留可复用，作业表/执行单在 Desktop
- [x] scripts/ 登记表 → ✅ 8/20 反思当场创建 scripts/README.md（杜绝脚本无声消失）

### 🧭 8/21 反思行动项（daily-reflection 复盘 8-20，执行者必读）
- [x] 语义缓存最小版（同 query 24h 去重中间件）→ ✅ 8/21 落地交付（见上方 8/20 反思项，commit `84d813bf2`，统一 chokepoint 覆盖全 8 后端）
- ⏳ 主 provider default 切换 → fangzhou-2 月度配额耗尽（HTTP 429，8/28 才重置），切 deepseek 官方/jiyuanlvdong（436ms 最快；k 可做 10min）
- ⏳ health_provider_check.py 余额阈值告警最小版 → 先做能 fetch 的 provider + fetch 失败标红（连续第 2 轮补齐，keylink ¥0.05 险裸奔收口）
- ✅ agent 可执行项分类 → projects 待办分「agent 可执行/需 sora」，executor 对 agent 可执行项直接跑（根治「反思≠执行」第 4 复发）→ ✅ **2026-08-30 已落地**：suggestion-implementation + vault-suggestion-executor 分类表新增「🤖 agent 可执行→直接执行」行

### 🧭 8/24 反思行动项（daily-reflection 复盘 8-23，执行者必读）
- 🔴 闲鱼决策倒计时机制 → sora 待决项 >7 天降周检点（不再每日刷屏）；8/31 前无决策则 k 先做合规改造子集（敏感词清单/同款频次控制/数模标题改写）；「经营性卖家」新规量化标准 patch 进 xianyu-monetization 技能（同款>5次/年发>30件/年销10万，敏感词红线）→ ✅ 合规子集 8/30 落地：新规量化已入技能（v1.2.0，8/23）+ 数模标题改写模板补录（8/30）；剩「上架 or 放弃」决策等 sora，8/31 到期
- ⏳ cron 批量失败联动诊断 → 同窗口 ≥3 个 cron Connection error 时自动跑 FlClash 代理诊断（7890/fake-ip/直连规则）+ 中转站健康检查，不再「观察即可」；hermes-health-check 加对应分支；reflection cron 加失败重试/次日补跑（8-21、8-22 反思缺档是连续性事故）
- ✅ 内容数字核对门 → 初稿具体数字（星标/金额/日期/百分比）写时 web_search 核验；wewrite-review 发布门加「数据新旧检查」（>7 天数字引用标待核）；dsh 两周 95K+（8/23 实测）入库作废旧值 14.9 万 → ✅ **2026-08-30 已落地**：wewrite-review 第 2 节新增「数据新旧检查」段落（>7 天数字标待核 + 官方源/二手源标注 + 发布门检查项）；8/30 数据溯源卡规则同步 patch 进 daily-knowledge-review
- 🔧 agent 可执行项分类（连续第 2 轮 open）→ projects 待办分「agent 可执行/需 sora」，executor 对 agent 可执行项直接跑 → ✅ **2026-08-30 已落地**（见 8/21 反思项同条，双技能已 patch，闭环）

## 🔒 待用户操作（不催促，状态变化时提醒）

| 项 | 状态 | 说明 |
|:---|:-----|:-----|
| 闲鱼上架决策「上架 or 放弃」 | 🔴 决策悬置第 42 天（8/31 到期已过，fallback 9/6） | 素材 100% 就绪；合规子集已备（xianyu-monetization v1.2.0）；8/24 倒计时机制生效 |
| 随身WiFi下单（赫电 Pro 399元/年） | 🔒 选型已确认 | 33元/月 1500G，待确认下单（阻塞 8 天+） |
| 桌面美化实际部署 | 🔒 安装包已就绪 | TranslucentTB + Rainmeter winget 一键安装已就绪 |
| SFC 系统扫描 | 🔒 需管理员权限 | 7/24 曾标记完成，7/27 后重复录入，待 sora 确认是否重跑 |
| 零感 AI 付费实测（1元/千字） | 🔒 需付费+测试稿 | 卡片 2026-08-03：降 AI 率主推工具定标，验 1 篇知网 98% 稿后写入 SOP |
| DeepSeek 直连充值 | 🔒 余额 ¥7.25 | 8/14 cron 记录；需充值恢复容灾深度 |
| jiyuanlvdong-2 余额充值 | ✅ 已移出 fallback（9/18） | 连续 402 已移出（config fallback_model → fangzhou-2）；如恢复容灾深度可选充值 |
| 多 provider 余额枯竭 | 🔒 需充值 | 9/11 巡检：fallback 池变小（多路 402/429/403），默认链 fangzhou-2 不受影响，容灾深度减薄 |
| `/new` 开新会话 | 🔒 长会话烧钱 | 「对话历史回顾」1M tokens 接近上限，压缩反复失败 |
| 打开 Obsidian（恢复 MCP） | 🔒 27123 端口无监听 | 依赖 Obsidian 的 cron 会失败 |
| FlClash github 路由 | ✅ 已恢复（9/16） | sora 9/16 重启后 github 200；health 09-18 无批量失败特征，P0 阻塞点解除 |
| skill 合并授权 | 🔒 待 sora 确认 | 09-01 审计 3 组合并（fangzhou-ark / android-automation / search-config）+ 09-08 审计 5 组近义合并（水墨 UI 4 合 1 等）——破坏性合并，确认后执行 |
| 墨题云服务器选型 | 🔒 需决策（花钱） | 腾讯 38/99 vs 阿里 99 + 域名；决策后 k 可全自动按方案部署（P1 商业线阻塞） |
| 三 bot 协作第一单目标 | ⏳ 等 sora | PCB 自动化流水线试跑：sora 给具体目标后 k 拆任务调度（researcher/coder/reviewer 已就位） |
| 万悟参赛确认（9/25 12:00 截止，剩 6 天） | 🔒 硬截止（9/19 更新） | 确认后 k 当天出《商业计划书/对策方案》初稿；9/21 前未确认 → wsl --shutdown 夜间窗口自动执行 |
| fangzhou-2 配额恢复 | ✅ 已恢复（9/5 实测） | 主链 custom:fangzhou-2 实测 1264ms OK，月配额重置生效，无需操作 |
| 安全审计 cron 排期 | ✅ 已完成 8/5 | security-audit cron 已挂载（`30 8 * * 0` no_agent + security_audit.py），无需再操作 |

### 🧭 9/16 反思行动项（daily-reflection 复盘 9-16，执行者必读）
- [x] 🔴 arxiv-fetch 静默排查 + 产物断言 → ✅ 2026-09-17 daily-todo-executor 落地：jobs.json last_status=ok / failure_streak=0 / last_error=None；9 月实际有 14 天产物（09-01~09-11,14,15,17，仅缺 12/13/16 三天，16 号为六 cron 批量失败日）——「9 月 0 产物」为 9/16 扫描口径误判；今天 14:16 产物 arxiv-2026-09-17-agent-llm.md 含当日日期非空；cron prompt 已加产物断言指令（写后自检存在/非空/含日期）
- [x] 🟡 创新大赛研究原文验证 → ✅ 2026-09-17 daily-todo-executor 落地：web_extract github.com/UnicomAI/wanwu（Go 63.7% / Apache-2.0 / Docker 部署 / GraphRAG·多租户·工作流实锤）+ README_CN；frontmatter 来源行已补 URL（innovation-competition-industry-track-20260915.md）
- [x] 🟡 闲鱼决策降频机制 → ✅ 2026-09-17 daily-todo-executor 落地：闲鱼上架区标题改「每周一复盘提醒」+ 默认再缓 7 天自动续期（见 🎯 闲鱼上架）；剩余每日触达由「闲鱼提醒」cron（工作日 7:30）承担，决策权仍在 sora
- [x] ~~🔒 闲鱼试水决策（第 42 天，sora 30 秒三选一：试水/放弃/再缓）~~ ✅ 2026-09-20 去重：与 L432 重复，以 L432（周一 9/21 复盘，state.yaml 权威）为准，决策仍开放
- [x] ~~🔒 万悟参赛确认（9/25 12:00 截止，剩 8 天，sora）~~ ✅ 2026-09-20 去重：与 L431 重复，以 L431（9/19 更新，剩 5 天）为准，决策仍开放

### 🧭 9/17 反思行动项（daily-reflection 复盘 9-17，执行者必读）
- [x] 🔴 github-privacy-gate 13 处隐私命中清理 ✅ 2026-09-18 daily-todo-executor 落地：门禁清零（4 处真实本地路径脱敏为 %USERPROFILE% + 7 处示例 IP/π 数字掩码 + 移除失效 s4mp 白名单条目），重跑 exit 0（截止 9/21 巡检前）——health 09-16/09-17 连续两天报 13 处命中（API_KEY 占位符/内网 IP，门禁拦截属预期但未清理）；跑 github_privacy_gate 出命中清单 → 占位符改示例 / 内网 IP 脱敏 / 真误报进白名单（9/16 s4mp <LAN-IP> 惯例）；只写 daily-note 不会被 executor 扫到，故本项登记在此
- [x] 🟡 资源类 P0 按副作用分级拆分 ✅ 2026-09-18 daily-todo-executor 落地：规则固化 hermes-health-check（k 可做无副作用当场执行 / 需 sora 确认列报告，不捆绑冻结）；RAMMap64 -E 9/18 反思时已执行清 Standby；wsl --shutdown 独立归 9/21 万悟决策夜间窗口（9/17 内存 99.4% 教训）——巡检发现资源问题先拆「k 可做无副作用（RAMMap64 -E 等，当场执行）」/「需 sora（wsl --shutdown 等）」两列，不捆绑冻结；9/18 反思已当场 RAMMap64 -E 清 Standby；wsl --shutdown 若 9/21 前 sora 未确认万悟部署 → 夜间窗口自动执行（镜像 21/25 已拉完，重启可再起）

### 🧭 9/18 反思行动项（daily-reflection 复盘 9-18，执行者必读）

- [x] 🟡 fallback 链收窄评估：jiyuanlvdong 系充值 or 永久移出 → ✅ 2026-09-19 weekly-cleanup 结论：永久移出（连续 402；9/18 config.yaml fallback_model 已切 fangzhou-2，字节级替换+核验，无需充值）；如后续要恢复容灾深度再评估充值（连续 402 已导致 obsidian-maintenance 9/18 当日失败；fallback 链成员枯竭面扩大：jiyuanlvdong/deepseek 官方/siliconflow/dengzhen 402、moonshot/zhipu 429、keylink 503、opencode-go/tabitoken 403）——9/21 前评估 provider 充值优先级（fangzhou 系为主）；规则已固化 hermes-provider-matrix「fallback 链健康度管理」（连续 2 次 402/429 主动移出链，充值后回填）
- [ ] 🟢 卡片 cron 排程评估：9/18 卡片 cron 12:33 跑时当日研究零产出（arXiv 12:42 才提交、kiko 19:53、wemux/genoffice 23:10），卡片由 executor 20:14 补写——后移到研究类 cron 之后（22:00+）或 prompt 加「候选池为空显式标记待补」；时序规则已 patch daily-knowledge-review，改 jobs.json 需授权
- [ ] 🔒 万悟参赛确认（9/25 12:00 截止，剩 6 天）→ sora 拍板后 k 当天出《商业计划书/对策方案》初稿；9/21 前未确认 → wsl --shutdown 夜间窗口自动执行（镜像 21/25 已拉完）
- [ ] 🔒 闲鱼试水决策（第 42 天，周一 9/21 复盘，state.yaml 权威）→ 30 秒三选一（试水/放弃/再缓）；k 侧 100% 就绪，上架 30min 可逆

### 🧭 9/20 反思行动项（daily-reflection 复盘 9-20，执行者必读）

- [x] 🟡 assert_state_consistency.py 扩展扫描 reflection/daily-review 天数残留 → ✅ **2026-09-21 反思当场闭环**：新增「表格行动项行+闲鱼上下文」扫描（行首 `|` + 含「闲鱼」+「第N天」；叙述/机制引用不判防假阳性；文件名日期 < state.yaml updated_at 不判）；实测修复 09-14/17/18/19 五份文件 7 行历史残留天数 → 第 42 天 + 断言全 PASS
- [x] 🟢 AI 工具（Codex/dsh/WorkBuddy 反代）安装前安全基线首轮快扫 → ✅ **2026-09-21 反思当场闭环**：无 ZCode 式静默上传特征（无 pending/ 加密快照、无 aliyun/OSS 外传端点）；dsh/codex 命中均为注释与插件元数据
- [ ] 🟡 daily-health-check 429 失败降级实现落地（pitfall 规则已固化 hermes-health-check，实现未落）→ **硬截止 9/24**；与 8/8 登记的「health 产物 stat 检查」P1 合并推进；executor 09-20 已加 config.yaml 可解析检查为前置
- [ ] 🔒 万悟参赛确认（今日 9/21 最后确认日，9/25 12:00 截止）→ 9/21 前未确认 → wsl --shutdown 夜间窗口自动执行；确认后 k 当天出《商业计划书》初稿
- [ ] 🔒 闲鱼试水决策（今日 9/21 复盘日，state.yaml 权威第 42 天）→ 30 秒三选一；新增 SOP-008 高客单 Web 定制选项，上架文案现成约 30min
- [ ] 🔒 ZCode 卸载链：sora 前三步（退出登录→卸载→删 ~/.zcode）；git 历史轮换 k 代做
- [ ] 🔒 生图三路径修复（9/21 10:15 api-media-weekly-probe 探活首验后定性）
- [ ] 🔒 skill 合并授权（6 组重复 + apple 孤儿，破坏性）
- [ ] 🔒 卡片 cron 排程授权（后移 22:00+，改 jobs.json）

## 🔗 相关领域
- [[AI-Agent]] — 基础设施与能力架构
- [[PPT-Design]] — PPT 制作方法论
- [[Academic]] — 学术服务与写作
- [[Vibe-Coding]] — 桌面美化与系统优化
- [[HOME]] — 返回知识中枢

---

_由 k (Hermes) 在每次会话结束时更新 | 最后更新: 2026-09-21 (daily-reflection 9/21：登记 9/20 反思行动项 9 条 + assert 扩展/安全基线当场闭环；闲鱼权威第 42 天未变)_

---

[[HOME|🏠 返回首页]]
