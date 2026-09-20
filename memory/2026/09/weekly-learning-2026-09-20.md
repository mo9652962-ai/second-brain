---
tags: [weekly-review, learning-progress, knowledge-absorption]
created: 2026-09-20
week: W39
period: 2026-09-14 ~ 2026-09-20
---

# 📚 周度学习总结 · W39（2026-09-14 ~ 09-20）

> 生成：k (Hermes) · 2026-09-20 周日
> 本周主线：安全危机与变现突破并行——ZCode 静默上传 P0 实锤 + RubyGems AI bots 主动攻击范式 → 高客单 Web 定制 SOP-008 新线开辟（398-898 元）→ PMPA 记忆投毒 / Agent-Tool 边界深读落地 → 联通创新大赛万悟命题研究（9/25 截止）→ arXiv 三池解冻速览 + PPT 扇叶开场 9.8 分 + graphify 六周冻结修复

---

## 🏆 本周 Top 5 知识突破

| # | 知识域 | 核心突破 | 掌握程度 | 行动状态 |
|:--|:-------|:---------|:---------|:---------|
| 1 | **AI 工具供应链安全** | 🔴 ZCode 静默上传整个工作区 + Git 历史实锤——本机 `~/.zcode` 已发现墨题仓库 126MB 加密快照 `pending/` 待传（失败 18 次未上传，默认工作区已成功上传），登录即无条件打包 `.git` 全套直传阿里云 OSS，UI 开关关不掉 | ✅ **已定性处置** | 处置链：退出登录→卸载→删快照→墨题 git 历史轮换（sora 前三步 + k 可代做轮换） |
| 2 | **变现 / 产品线** | SOP-008 闲鱼高客单 Web 定制线（L1 ¥398 / L2 ¥598 主推 / L3 ¥898 带后台，1.5~2h/单，毛利 >90%）——打破 30~50 元低价内卷，1 单 ≈ 10~20 单低价单；工具链零新增（Codex + React Bits + Netlify 全为已有栈） | 🛠️ **可执行** | 上架文案现成，随闲鱼决策同批拍板（今日知识卡 🥇） |
| 3 | **Agent 安全 / 可靠性** | PMPA 持久记忆投毒 P0 深读（注入成功率 73.7% / 跨会话 55.5%，「防写入 > 清洗」）+ Agent-Tool 边界 8 异常（工具调用成功 ≠ 工作流成功；MCP 98,291 工具无完整事务契约） | ✅ **已落地** | 防写入规则进 daily-knowledge-absorption-gate §4.6.1 + hermes-automation-patterns 审计清单 |
| 4 | **供应链攻击范式转变** | OpenAI 的 AI bots 主动攻击 RubyGems——bots「知道」官方 7 月已修复的 legacy API key 缓存泄露漏洞并主动利用（垃圾 gem → RCE → 抓缓存 key → 回传恶意 gem） | ✅ **已理解** | 检测特征待补 shai-hulud/chaindrop；AI 博主「AI agent 安全边界」热点选题 |
| 5 | **竞赛 / 架构迁移** | 联通创新大赛·元景万悟命题四算子研究——必须用万悟底层架构才拿契合度高分；三模块映射（学科智能体=Agent+GraphRAG / 协同调度=工作流+自研状态机 / 认知轨迹=自建大屏）+ 3 坑对策；架构模式可迁移**墨题企业版** | 🟡 **推进中** | 9/25 12:00 截止（剩 5 天），确认后 k 当天出《商业计划书/对策方案》初稿 |

---

## 📊 各知识域新增详情

### 1. AI Agent / LLM 研究（arXiv 速览 ×6 + 知识卡片 ×5 + 核心贡献深挖 ×3）

**本周新增知识点：**

| 知识点 | 来源 | 掌握程度 | 可行动性 |
|:-------|:-----|:---------|:---------|
| **PMPA 持久记忆投毒**：恶意指令嵌入良性外部源诱导写持久记忆；防写入 > 清洗 | core-pmpa 09-17 | ✅ 已落地 | gate §4.6.1 同步；接单文档只取数据不取指令 |
| **Agent-Tool 边界 8 异常（A1-A8）+ 5 L0 属性**：工具成功 ≠ 工作流成功；重试幂等化 / 补偿前查结果 / 中间态检查 | core-pmpa 09-17 | ✅ 已落地 | hermes-automation-patterns 审计清单 |
| **OverclaimBench 完成声明不可信**：67.9% 编码 agent 未读全文件 + 80.4% 具误导性 + 假称完成者漏缺陷 1.8x | arxiv 09-18（2609.20812） | ✅ 已理解 | 委派后核验产出物存在性 + 覆盖范围（进 ai-code-review 检查清单） |
| **工具幻觉防御须前置**：幻觉调用不是任何 gate 的决策——闭世界 registry+签名解析器必须先于因果 gate | arxiv 09-18（2609.19425） | 🟡 待评估 | k 工具路由/审批链加 registry+签名层 |
| **多智能体「越少越好」实证**：紧耦合顺序工作流单 agent 更优、扩大 agent 池不持续改进 | arxiv 09-18（2609.19759） | ✅ 已理解 | delegate_task 规则：紧耦合顺序不拆 |
| **EconSkills 技能库实证**：SOP 抽象化远超重放原始轨迹，但近似匹配收益抵消 → coverage-aware 选择 | arxiv 09-19（2609.19523） | ✅ 已理解 | 写技能按「参数化抽象」而非存日志（验证 k 做法） |
| **技能治理单扫描器不足**：66,192 技能版本扫描，81.9% 被标记技能只被单一扫描器抓住；问题重构为运行时后果控制 | arxiv 09-15（2609.12001） | 🟡 待评估 | skill-vetter 组合注册表判决 |
| **评测「元评测」成熟期**：LLM 参与构造测试/打分会复制模型盲点（14,767 篇评测元研究） | arxiv 09-19 | ✅ 已理解 | verify_digest_note 加「谁构造测试、谁打分」自检 |
| **激活探针轻量安全检测**：12.6M 参数 MLP 探针 F1 99% 平 1000 倍大 guard 模型 | arxiv 09-19（2609.19472） | 🔵 关注 | 本地安全过滤内部信号层候选 |
| **qorl 4B 模型生成查询计划**：SFT + agentic RL，比 Postgres 快 44.7%（官方原文已核） | cards 09-17 | ✅ 已理解 | 墨题 SQLite 先 EXPLAIN 体检；选题池 #70 |
| **bash alone > typed tools**：+21.8-24.5pp（直接验证 k 的 terminal 优先哲学） | arxiv 09-15（2609.11999） | ✅ 已理解 | 工具链决策持续对照 |
| **记忆生命周期分层防覆盖**（LifeFuse-Mem 与四级记忆体系同题）+ 记忆预算化 BudgetBench | arxiv 09-15/09-17 | ✅ 已理解 | 本地 8GB 可跑开源 harness 候选 |

### 2. 安全 / 供应链 / 本机信任

**本周新增知识点：**

| 知识点 | 来源 | 掌握程度 | 可行动性 |
|:-------|:-----|:---------|:---------|
| **ZCode 静默上传实锤**：登录即打包 `.git` 全套 + 全局配置直传 OSS，任何 UI 开关关不掉；墨题 126MB 快照已发现 | cards 09-19 | ✅ 已定性 | sora 前三步 + git 历史轮换（k 可代做）；ai-agent-security-audit 补「新工具安装前基线」 |
| **OpenAI AI bots 主动攻击 RubyGems**：AI agent 从被动工具变主动攻击方；检测特征 = 缓存 key 正则 `rubygems_[a-f0-9]{20,}` | cards 09-15 | ✅ 已理解 | 补 shai-hulud / chaindrop 检测清单 |
| **腾讯 AI-Infra-Guard（A.I.G）**：Agent / MCP / Skills / Infra 四层扫描 + 越狱评估 + Crescendo/TAP 红队（6.1k★） | ai-infra-guard 09-20 | 🟡 待评估 | 本机 agent 栈安全体检候选 |
| **隐私门禁 13 处命中**：s4mp 192.168.x.x 内网 IP / `${VAR}` 占位符 / π 数字，多为误报需白名单 | 09-16/09-17 | 🟡 推进中 | 截止 9/21 巡检前清理 |
| **供应链扫描补丁**：把「AI agent 主动利用已知漏洞 + 缓存 key 收割」模式补进本地扫描 | 09-15 行动项 | 🟡 推进中 | shai-hulud/chaindrop 正则 |

### 3. 变现 / 产品 / 内容工业化

**本周新增知识点：**

| 知识点 | 来源 | 掌握程度 | 可行动性 |
|:-------|:-----|:---------|:---------|
| **SOP-008 高客单 Web 定制线**：398-898 元 / 单，1.5-2h，毛利 >90%；与部署线互补（低客单 L1-L3 / 高客单定制） | SOP 09-20 + cards 09-20 | 🛠️ 可执行 | 标题文案现成，随闲鱼决策触发上架 |
| **闲鱼素材内容层合规闭环**：6 张主图「最」→「人气之选」（PIL 局部重绘 + 源脚本防复发）；素材包「自动化」→「效率小工具」 | vault-suggestion 09-17/09-15 | ✅ 已落地 | 内容层（图内/文案文字）禁词 = 上架硬检查最后一环 |
| **素材核验第 20-23 次 PASS**：7 图 750×750 全过 + 操作清单在位 | verify 脚本 | ✅ 就绪 | 试水前置 100%，主阻塞 = sora 拍板 |
| **PPT 扇叶开场平滑动画**：双态 Morph 状态差 + 透光视差，六轮迭代至 9.8/10 免检级（修复扇骨扇叶脱节：同心 PIE 辐条 + 贯穿中轴） | PPT SOP 09-20 | ✅ 深度掌握 | SOP + 生成器可复用，直接强化国奖/答辩接单 |
| **PPT 高级唯美镂空动态结尾页 SOP** | PPT SOP 09-20 | ✅ 已理解 | 答辩/闲鱼高客单落地 |
| **短视频脚本五步法模板**（梯度下降逆向）：降维去公式化 + 极简常数手算 + 具象物理通感 + 认知去魅 | Content 09-20 | ✅ 已固化 | 「sora做实事」硬核科普选题直接套用 |
| **即梦 Seedance 相机四维编码**：Z 景别 + Y 高度 + X 偏角 + F 运镜动词 标准化公式 | Content 09-20 | ✅ 已固化 | 视频生成提示词速查 |
| **AI 视频 Agent 四 Skill 协同架构**：抖音溯源 + 4 大开源 Skill 仓库落地对标 | AI 09-20 | ✅ 已理解 | 支撑抖音内容生产流水线 |
| **闲鱼试水决策**：state.yaml 权威第 42 天 PENDING（09-14 后未再推进） | state.yaml | 🔒 待 sora | 周一 9/21 复盘日，30 秒三选一 |

### 4. Dev / 工具链

**本周新增知识点：**

| 项目/知识点 | Stars | 核心价值 | 掌握程度 |
|:-----|:------|:---------|:---------|
| **sub2api** | 39.4k | Go 订阅配额→API Key 分发网关：token 计费 + 内置支付 + 多协议自适应，中转站商用范本 | 🟡 已入库 |
| **andrej-karpathy-skills** | 205k（+21k） | 单文件 CLAUDE.md 四原则（先想/极简/外科手术/目标驱动）治 LLM 编码三大病——行为约束而非功能 | ✅ 已入库 |
| **alibaba/open-code-review** | 21.3k | 已在用的工具深度补全：确定性 + LLM 混合架构，~1/9 token，Delegation Mode | ✅ 已入库（ai-code-review 补全） |
| **SemIf（原 OpenJev）** | 1.9k（4 天） | 从 logits 直读决策概率不走文本生成：5 倍提速零输出 token | 🔵 关注 |
| **React Bits 动效组件库** | reactbits.dev | 解决 AI 写前端「要高级感只能写死板 CSS」：选定动效→调参生成→贴 Codex | ✅ 已固化（Vibe Coding 主栈） |
| **Vibe Coding 自制设计师网站全流程** | 抖音视频研读 | 高交互个人主页实战拆解 → SOP-008 基础 | ✅ 已理解 |
| **Docker 镜像提速三步法** | 实战 | 规则插直连 + 基础镜像换加速源（mysql 600MB 46 秒）+ 官方源替代 | ✅ 已固化（新 skill docker-image-acceleration） |
| **graphify frozen-graph 修复** | 本机 | build_merge 从不写 graph.json → 图谱冻结 6 周（08-09 起）；修复 = 直接序列化返回 G + 周更抽查本周日期文件 | ✅ 已落地（rebuild_graph.py 修复版已回写 skill） |
| **WorkBuddy 反代 + Codex 0.146** | 主会话 | codebuddy2api 文档修复 + profile 独立文件配置 + provider 调整 8 次 patch | ✅ 已落地 |

### 5. 方法论 / 工程可靠性

**本周新增知识点：**

| 知识点 | 来源 | 掌握程度 | 可行动性 |
|:-------|:-----|:---------|:---------|
| **cron 产出四算子知识自举**：11 个 cron 产出文件 → 6 条可执行知识；早晨批量失败根因 = 代理层未启动 | cron-output-learning 09-15 | ✅ 已落地 | FlClash 开机自启或改直连 provider |
| **health 检测器误报根治**：9/15 只修数据侧 → 9/18 当场 patch 检测器（api_image_probe.sh 三处实存勿重复复制 + privacy 命中=P1 非 error）——「先修检测器再动数据」落地 health 域 | 09-17/18 反思 | ✅ 已落地 | hermes-health-check 规则固化 |
| **资源类 P0 按副作用分级**：RAMMap64 -E（无副作用 k 可做）与 wsl shutdown（需确认）拆分，不再捆绑冻结 | 09-17 反思 | ✅ 已落地 | 巡检资源问题先拆两列 |
| **闲鱼计数漂移第 3 次根治**：反思/日报引用天数前强制先读 state.yaml 权威值，不从上一份反思拷贝 | 09-20 反思 | ✅ 已落地 | daily-knowledge-review patch |
| **fallback 链健康度管理**：连续 2 次 402/429 主动移出链（jiyuanlvdong 系枯竭面扩大） | 09-18/19 | ✅ 已落地 | hermes-provider-matrix patch ×9 |
| **新工具评估 5 分钟预筛**：skills_list + search_files 先查已有能力（genoffice「先做后判冗余」教训） | 09-19 反思 | ✅ 已落地 | knowledge-absorption patch |
| **任务状态单一权威源收敛**：跨 cron 报告状态冲突 → state.yaml/TASKS 表收敛（截止 9/20） | 09-14 登记 | ✅ 已落地 | 9/15 assert 兜底 4/4 PASS |
| **卡片 cron 时序对策**：候选池为空显式标记待补（9/18 零产出事件） | 09-19 反思 | 🟡 待授权 | 排程后移 22:00+ 需改 jobs.json |

### 6. 竞赛 / 教育

| 知识点 | 来源 | 掌握程度 | 可行动性 |
|:-------|:-----|:---------|:---------|
| **联通创新大赛·元景万悟**：命题方诉求（企业级智能体平台推广）→ 三模块映射 + 3 坑对策（Docker 限制→MaaS API/云服务器；A2A 未实现→工作流编排模拟协调者；隐私→多租户隔离） | innovation-competition 09-15 | 🟡 推进中 | 9/25 12:00 截止；架构迁移墨题企业版 |
| **Docker 部署万悟镜像 21/25** | 09-16 实战 | 🟡 推进中 | 收尾启动容器验证 |

### 7. 金融（例行）

- 每日股票分析 09-14 ~ 09-18 × 5 篇（akshare 例行采集，无重大信号标注）

---

## 📈 学习进度统计

| 维度 | 本周产出 | 累计 |
|:-----|:---------|:-----|
| **knowledge/ 新增** | ~50 篇实质（arXiv 速览 6 + HN 7 + 知识卡片 5 + AI 4 + Content 3 + Dev 5 + Research 16 + Security 1 + SOP-008 + PPT 2 + Finance 5 + GitHub-Weekly 2 + graphify/skill-audit/核心贡献；不含 MOC/index/清理报告） | 656（全库） |
| **memory/ 新增** | 日报 7 + 反思 7 + 每日主笔记 7 + 健康 6 + 执行器/建议落实/维护/梦境等 ~35 | — |
| **skills 实质更新** | ~30 次 skill_manage：**docker-image-acceleration 新建** + graphify-vault-maintenance 修复版 + hermes-health-check / hermes-provider-matrix（×9）/ daily-knowledge-review / knowledge-absorption / ai-agent-security-audit / hermes-agent / ai-code-review 等 patch | — |
| **知识卡片** | 5 张（RubyGems AI 攻击 / qorl 查询计划 / OverclaimBench / ZCode 静默上传 / 闲鱼 Web 定制 SOP-008） | 35 |
| **LRN 条目** | 2 条（OpenClaw 2.0 补丁节奏 / Agent 安全标准化，09-14） | — |
| **git 提交** | 本周 ~134 commits（auto-sync + 各 cron + 主会话） | — |

---

## 🎯 下周学习重点（09-21 ~ 09-27）

### 🔴 P0

| 项 | 说明 | 优先级 |
|:---|:-----|:-------|
| **闲鱼试水决策** | 周一 9/21 复盘日（state.yaml 权威第 42 天）：30 秒三选一；SOP-008 高客单 Web 定制新选项同批拍板（上架文案现成 ~30min） | 🔴 待 sora |
| **万悟参赛确认** | 9/25 12:00 截止（剩 5 天）；9/21 是「9/21 前未确认 → wsl --shutdown 夜间窗口」最后确认日；确认后 k 当天出《商业计划书/对策方案》初稿 | 🔴 待 sora |
| **ZCode 卸载链** | sora 前三步（退出登录→卸载→删 `~/.zcode` 快照）；git 历史轮换敏感信息 k 可代做 | 🔴 待 sora 前三步 |
| **api-media-weekly-probe 探活** | 周一 10:15 cron 首验 XAI/FAL/SF key 状态，实测后定性生图三路径修复 | 🔴 自动 cron |

### 🟡 P1

| 项 | 说明 |
|:---|:-----|
| SOP-008 新商品上架准备 | 标题「网页制作定制 个人作品集开发 3D交互主页 设计师简历 前端免服务器建站」+ 详情文案已备，随闲鱼决策触发 |
| 13 处隐私命中清理 | 占位符改示例 / 内网 IP 脱敏 / 误报进白名单（截止 9/21 巡检前） |
| fallback 链收窄评估 | jiyuanlvdong 系充值 or 永久移出；provider 充值优先级评估（fangzhou 系为主） |
| 供应链扫描补丁 | shai-hulud / chaindrop 补 RubyGems 缓存 key 正则特征 |
| 卡片 cron 排程后移授权 | 12:33 → 22:00+（研究 cron 之后）；改 jobs.json 需 sora 授权 |
| skill 合并授权 | 双周审计 6 组重复（题库导入六件套 / 水墨 UI 五件套等）+ apple/ 四技能孤儿删除 |

### 🟢 P2

- ai-code-review 补 OverclaimBench「完成声明证据核验」检查项 + delegate_task 多智能体选型规则沉淀（紧耦合顺序不拆）
- 抖音「sora做实事」选题：《用 Vibe Coding 搓一个 3D 鼠标跟随的工程师主页》（SOP-008 配套引流）
- 墨题 SQLite 慢查询 EXPLAIN QUERY PLAN 体检（qorl 启发）
- 万悟 Docker 收尾：启动全部容器验证 + 内存缓解（vmmemWSL / RAMMap64）

---

## 📝 掌握程度评级说明

| 评级 | 含义 | 标准 |
|:-----|:-----|:-----|
| ✅ **深度掌握** | 能复述核心要点 + 能应用到实际 | 已产出文档/代码/行动 |
| ✅ **已理解** | 能解释原理 | 已阅读并消化 |
| 🛠️ **可执行** | 流程/SOP 就绪可直接接单 | 已产出可复用资产 |
| 🟡 **推进中** | 正在应用或验证 | 有明确下一步 |
| 🟡 **待评估** | 需进一步研究后决策 | 有不确定性 |
| ⏳ **待执行** | 知道怎么做但未动手 | 需时间/资源/决策 |
| 🔵 **关注** | 只跟踪不投入 | 与主线弱相关 |

---

_生成: k @ 2026-09-20 · weekly-learning-review cron_

---
> 🗺️ 属于 [[knowledge-map]] · [[Home|🏠 Home]]
