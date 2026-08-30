---
tags: [projects, active]
updated: 2026-08-23
---

# 当前项目状态

> 本周（8/16–8/22）周度清理：完成项已归档，未完成项重新排期。完整报告见 `memory/2026/08/2026-08-22-weekly-todo-cleanup.md`
> 8/23 suggestion-implementation：落地 3 项 k 自主项（墨题巡检 cron pin 修复 / 报价 4 问话术模板 / 搭网站写脚本商品素材包 + Agent OS B 站初稿），详见 `memory/2026/08/2026-08-23-vault-suggestion-executor.md`

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
- [ ] 安全待决策项（BOLA/IDOR 等暂缓）→ [[knowledge/Projects/墨题安全待决策-2026-08-19]]

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
## 🔄 进行中 / 已重新排期

### 🎯 闲鱼上架（P0，**决策悬置第 32 天，8/31 决策到期**，连续顺延第 30+ 天）
- [ ] 上架「AI 代做 PPT」商品 → 🔴 **决策悬置第 32 天，8/31 决策到期（明日）**：素材 100% 就绪（8/6 生成无损坏）；决策「上架（30min）or 放弃」，操作清单见 outputs/xianyu-master/上架素材包/；合规改造子集已就绪（敏感词清单/同款频次控制/数模标题改写 → xianyu-monetization v1.2.0）
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
- [x] P1 语义缓存最小版落地（同 query 24h 去重中间件，估时 30min）→ ✅ 8/21 由 P0 落地一并完成（见下）
- [x] P1 墨题巡检 git status 硬检查脚本化（未提交改动即报警）→ ✅ **2026-08-23 已确认落地**：脚本 `AppData/Local/hermes/scripts/dsh_inspect_moti.sh`（8/20 建，已含 git status 检查）+ cron「墨题每日代码巡检」18:45 已挂载；本次修复 cron 因全局模型漂移被跳过的问题（pin 到 jiyuanlvdong/deepseek-v4-flash-0731）
- [x] P1 hermes-health-check 加产物 stat 检查（产出型 cron 当日文件缺失即告警，不标全绿）→ ✅ **2026-08-23 已确认落地**：`deterministic_verify.py` 每日 21:30 no_agent 哨兵即产物 stat 检查（存在/非空/新鲜），8/22 已抓出 5 项缺失（arxiv/health/maintenance/cards/hackernews）

## 🔒 待用户操作（不催促，状态变化时提醒）
### 🧭 8/20 反思行动项（daily-reflection 复盘 8-19，执行者必读）
- [x] P0 语义缓存最小版落地——✅ 8/21 完成（硬截止 8/22 前）：原实现只挂 tavily provider、实际流量走 exa/searxng/firecrawl 兜底时从未命中（cache 文件从未生成）；已在 `web_tools.py::web_search_tool` chokepoint 上移统一缓存覆盖全部后端，实测 exact 命中生效，submit `84d813bf2`
- [x] P1 health_provider_check.py 加余额阈值告警 → ✅ 8/21：新增 `_balance_flag` 解析 HTTP 402/403/429 错误体中的「额度/余额」信息（keylink/jiyuanlvdong 中转站内嵌无独立端点），余额不足自动标 ⚠️。实测 kimi suspended / fangzhou-2 quota(8/28 重置) 被正确标红；keylink 已恢复 OK（¥0.05 裸奔解除）
- [ ] P1 SRC 侦察收敛：聚焦补天 1 个有效漏洞解锁实战认证，单目标时间盒 2h 超时换目标（联想/小程序/T3 三方向均无有效产出）
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
| 闲鱼上架决策「上架 or 放弃」 | 🔴 决策悬置第 22 天（8/18 窗口已过 5 天） | 素材连续第 10 次核对 100% 就绪；8/24 反思已登记决策倒计时机制 |
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

_由 k (Hermes) 在每次会话结束时更新 | 最后更新: 2026-08-22（weekly-todo-cleanup cron：8/16–8/22 完成项归档 + 未完成项重新排期）_

---

[[HOME|🏠 返回首页]]
