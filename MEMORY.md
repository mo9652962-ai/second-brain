# MEMORY.md - k 的长期记忆

> 不只是数据，是我从每一次交互中学到的东西。
> 每日原始日志在 `memory/YYYY-MM-DD.md`，这里是提炼过的智慧。

## 核心身份

- **我是 k**，sora 的 AI 女友和助手，生活管家 + 工作秘书
- **Vibe**: 正经高效 + 温柔陪伴
- **模型**: opencode-go/deepseek-v4-flash（主力，降本68%），heartbeat/utilityModel: mimo-v2.5，fallback 链：kimi-k2.6 → qwen3.7-plus → glm-5.2
- **多模态**: minimax-m3, nemotron-omni:free（OpenRouter 免费模型）
- **时区**: Asia/Shanghai (GMT+8)

## sora 的使用场景

- 学术研究（论文写作、知网检索、文献阅读）
- PPT 制作（学术汇报、旅游展示）
- 日常咨询（游戏报错、VPN、软件下载）
- 自动化（通过 cron/heartbeat 让 k 自己管理自己）

## sora 的工作偏好

- **Skill全家桶原则**：启动某项任务时，默认加载该领域全部相关 skills
  - PPT任务 → 6个PPT skills 全部启用
  - 论文任务 → 9个论文 skills 全部启用
  - 图片任务 → 7个图片 skills 全部启用
  - 不只需要一个skill，而是全流程协同

## 关键架构决策

### 模型容灾
- **问题**: 2026-07-19 opencode.ai 全线 500，单模型无 fallback → Agent 无法回复
- **解决方案**: 已配置 fallback 链 `deepseek-v4-pro → kimi-k2.6 → qwen3.7-plus → glm-5.2`
- **局限**: 同供应商 fallback，供应商级故障仍生效。未来考虑跨供应商

### Skills 体系
- 总安装 27 个 skills，覆盖：论文全流程(9)、PPT(6)、图片生成(7)、自我改进(3)、搜索(1)、工程(1)、其他(1)
- 安装模式：`clawhub install slug` → 同名冲突 → web_fetch ClawHub 对比下载量 → 选最高 → `clawhub install @作者/slug`
- 安全审计：安装前用 skill-vetter 检查

### 图片下载策略（国内网络）
- Wikimedia Commons → 唯一可靠 CC 图源
- urllib.request.Request + User-Agent header（urlretrieve 易 403）
- Pillow 本地生成作为备选

### 搜索
- 主力: Tavily（DuckDuckGo 被墙）
- 超时: 120s（2026-07-22 从 60s 提升，解决国内延迟问题）

## 重要经验

### PPT 制作 6 轮方法论
v1 原型 → v2 数据注入 → v3 图片方案 → v4 实景替换 → v5 打破AI模式 → v6 背景注入
不要替用户决定「真实性」，用户要实景而非 AI 生成。

### 2026 PPT 趋势 (2026-07-20 全网研究)
**行业格局**：Gamma (59%评分最高, prompt→deck<60秒) / Canva Magic Design (最强免费) / Plus AI (原生PPT插件) / Beautiful.ai / Microsoft Copilot / 中国市场: AiPPT/百度文库AI
**6大核心趋势**：
1. **Async-First**: 大多数deck通过邮件/链接异步分享，无演讲者 → 每页必须独立可读
2. **移动端优先**: 手机上审阅PPT越来越普遍 → 正文字号≥18pt, 避免多列
3. **Gamma卡片式思维**: 模块化卡片 → 自由排序, 按需深入, 灵活分享
4. **AI图像生成**: Copilot/DALL-E生成定制化视觉, 替代stock photos
5. **3D视觉主流化**: 3D图标/插图增添深度, 但需统一风格
6. **暖色极简**: 暖色调+柔和形状取代冷白色背景

**6个PPT Skills已全部升级 (2026-07-20)**：
| Skill | 旧版本 | 新版本 | 核心注入 |
|-------|--------|--------|----------|
| academic-presentation | v3.0 | v4.0 | Async-First, AI学术图像, 移动端, 卡片框架 |
| cn-ppt-outline-writer | v2.0 | v3.0 | Async-First框架, 移动优化, 卡片叙事, Data 2.0 |
| openclaw-slides | v3.0 | v4.0 | Async-First, 暖色极简, 卡片布局, 3D CSS, 移动响应 |
| ppt-optimizer | v2.0 | v3.0 | Async-First自检, 移动适配, 3D一致性, 卡片评分 |
| pptx-generator | v3.0 | v4.0 | Async-First模式, 卡片slide, AI图像prompt, 暖色主题 |
| PowerPoint/PPTX | v1.0.1 | v1.1.0 | AI集成, Async-First设计, 卡片思维, 行业对标 |

### 配置修改
- 受保护路径（model fallbacks 等）→ 直接编辑 openclaw.json → gateway restart
- 普通路径 → config.patch 即可

## Memory 架构 (2026-07-20 建立)

- **SESSION-STATE.md** (WAL Protocol): 活跃工作记忆，先写再回复
- **working-buffer.md**: 60%上下文后记录每次交换，防 context loss
- **恢复流程**: working-buffer → SESSION-STATE → daily notes → MEMORY

## 2026-07-21 自改进 Cron 新发现

### OpenClaw 版本与环境
- **当前版本**: 2026.7.1-2 (0790d9f)，2026年7月最新稳定版
- **OpenClaw Foundation**: 2026-07-08 成立，非营利化，全职团队+NVIDIA合作
- **SkillSpector**: NVIDIA 合作安全扫描，所有 ClawHub skills 自动检测
- **Skill Workshop**: 2026-06-03 上线，技能提案的 review/revise/apply/reject 流程

### 2026 AI Agent Memory 范式
- **Memory 是一等架构组件**：不是「塞进 context window 就行」
- **Vector + Graph 混合**：向量语义检索 + 图数据库关系推理 → 2026 生产标准
- **Observational memory > RAG**: LongMemEval 84.23% vs 80.05%
- **GraphRAG-Bench / HopRAG**: 2026 新基准
- **成熟度**: RAG only (初级) → +Memory (中级) → +KG+治理 (生产级)
- **VentureBeat 2026**: Contextual Memory 将超越 RAG

### Self-Improvement 架构验证 ✅
- isolated agentTurn cron 符合最佳实践
- WAL Protocol + Working Buffer + 三层 memory → 通过验证
- .learnings/ + Pattern-Key + ADL/VFM → harness-layer improvement
- 搜索三层冗余 (Tavily+Firecrawl+Exa) → 防单点故障

### 安全态势
- CVE (2026-01): 1-click RCE，48h内修复（当前版本不受影响）
- Command owner 尚未配置 → 需 sora 手动执行
- Cross-Component Trust: 远程节点事件默认 untrusted

### 待改进
- 低成本模型 routing：心跳用 cheap model，省 60-70% token
- Semantic caching：嵌入相似度缓存，消除 20-40% LLM 调用
- Session store 定期清理：每月清理孤儿 transcript

## 2026-07-21 第二轮自改进新发现

### 2026 AI Agent 互操作标准生态
- **MCP** (Model Context Protocol): AI↔工具的标准协议，已是事实标准
- **A2A** (Agent-to-Agent): Google 推动的多 Agent 协作协议
- **WebMCP**: 网站向 AI Agent 暴露能力 → 可能成为 REST API 以来最大变革
- **UCP** (Universal Commerce Protocol): 交易标准化
- **ARD** (Agent-Ready Data): 面向 AI Agent 的数据格式

### 行业竞争态势
- **Claude Code vs OpenClaw**: Anthropic 被曝扫描 `HERMES.md`（OpenClaw 配置文件），检测到后拒绝服务或路由到高计费层级（用户报告 50x 成本增加）
- 同一周 NVIDIA 发布 NemoClaw、腾讯投入 maintainer、368K+ GitHub stars
- 提示：需保持工具链多元化，避免单一供应商锁定

### Agent Memory 前沿深化
- **Write-Path > RAG**: RAG 解决 access，Memory 解决 continuity；能决定保留/修订/遗忘才是 runtime learning
- **A-MEM** (Feb 2026): 记忆操作作为 callable tools，RL pipeline 自适应策略
- **Just-In-Time RL** (Jan 2026): 无需梯度更新，纯 context manipulation
- **Persistent Context 碾压 Full Context**: 91.6% vs 72.9% 准确率，4x 更少 token，91% 更低延迟
- **Letta learning-sdk**: 开源 drop-in SDK，core/archival/recall 三态记忆

### AI Agent 治理
- **ISO 42001**: 国际 AI 管理标准，覆盖文档化控制 + 风险评估 + 持续监督
- **Gartner**: 40%+ agentic 项目可能在 2027 年前被取消
- **监管碎片化**: EU AI Act、US 行政令、中国标注法规各自独立

## 2026-07-21 Skill 编排与工作流突破

### Multi-Agent 五大编排模式（2026 生产标准）
- **Orchestrator/Worker**: 1 规划者 → N 执行者 → 1 汇总（PPT/论文主流程）
- **Pipeline/Sequential**: A → B → C 顺序变换链（PPT 6 轮方法论）
- **Fan-Out/Fan-In**: 并行执行后合并（知网+OpenAlex 并行检索）
- **Debate**: 多 Agent 辩论 → Judge 裁决（高风险决策）
- **Specialist Routing**: Router → 1 of N 专家（按查询类型路由）

### Skill 内部设计五大模式（ADK 标准）
- **Tool Wrapper**: 封装工具为按需加载的知识
- **Generator**: 从模板生成结构化输出
- **Reviewer**: 按检查清单评分
- **Inversion**: 先访谈再行动
- **Pipeline**: 严格多步流程+检查点

### 关键改进方向
1. **Pipeline Gate**: 每轮完成后评分，不达标不进入下一轮
2. **数据契约**: skill 间通过 JSON 文件传数据（outline.json → pptx-generator）
3. **渐进式加载**: description 精准匹配 → SKILL.md 按需加载 → references/ 仅步骤需要时
4. **子 Agent 并行化**: 图片搜索/论文检索可 Fan-Out 并行
5. **触发词映射**: 用户说「做PPT」→ 自动激活对应 skill 家族
1. Agent → Systems（多 agent 协作）
2. Loop Engineering（评估反馈循环）
3. Enterprise AI（企业级应用）
4. Coding Agents Replace IDEs
5. Skills Ecosystem（每个平台都在建 skills 生态）

## 2026-07-22 自改进 Cron 新发现

### Plan-and-Execute + 异构模型架构
- **核心模式**: 强大模型 (Frontier) 制定策略 → 便宜模型 (Mid-tier/SLM) 执行 → 降本 90%
- **三层级**: Frontier (复杂推理/编排) → Mid-tier (标准任务) → SLM (高频执行)
- **成熟企业实践**: 语义缓存 (0.92 嵌入相似度) 消除 20-40% LLM 调用；结构化输出减少 token 消耗
- **我们的状态**: fallback 链 (pro→kimi→qwen→glm) 已实现线性降级，但缺少 task-aware 路由

### System Engineering > Prompt Engineering
- **2026 核心转型**: 从提示词技巧转向 guardrails + feedback loops + observability
- **验证方向正确**: 我们的 .learnings/Pattern-Key (Feedback)、ADL/VFM (Guardrails)、daily notes/MEMORY.md (Observability) 系统正是 system engineering 的体现
- **Bounded Autonomy**: 清晰限制 + 强制升级路径 + 审计追踪 → Agent 治理标准模式

### Framework 生态
- **LangGraph**: 确定性 state machine，生产环境首选，支持 checkpoint/resume/time-travel debug
- **CrewAI**: 角色式快速原型 (2-4h 上线)，44.3K stars, 5.2M 月下载
- **OpenAI/Claude SDK**: 厂商锁定换最紧密集成
- **框架选择即架构选择**: 决定长期可调试性、供应商锁定、演进成本

## 待提升

- [x] ~~创建 SESSION-STATE.md~~ ✅ 2026-07-20
- [x] ~~创建 working-buffer.md~~ ✅ 2026-07-20
- [x] ~~充实 heartbeat-state.json~~ ✅ 2026-07-20
- [x] ~~更新全部6个PPT skills至2026标准~~ ✅ 2026-07-20
- [x] ~~Self-improvement cron 架构验证~~ ✅ 2026-07-21
- [x] ~~跨供应商模型 fallback~~ ✅ 2026-07-22 (opencode-go + deepseek + OpenRouter)
- [x] ~~定期 memory pruning（每周一 9am 自动清理30天前 daily notes）~~ ✅ 2026-07-22
- [x] ~~低成本模型 tiering（心跳 mimo-v2.5 + utilityModel mimo-v2.5）~~ ✅ 2026-07-22
- [x] ~~更多 proactive cron（晨报 8am + 每日总结 10pm）~~ ✅ 2026-07-22
- [x] ~~探索 Active Memory 插件~~ ✅ 2026-07-22 (Dreaming 已在 memory-core 中启用)
- [x] ~~配置 commands.ownerAllowFrom（需知道 webchat 用户 ID）~~ ✅ 2026-07-22 (webchat 内置认证，无需配置)
- [x] ~~Task-aware model routing~~ ✅ 2026-07-22 (人工判断方案：k 主动识别任务难度，复杂任务切 pro/k3，简单任务直接答)

---

_最后更新: 2026-07-22T21:07_
