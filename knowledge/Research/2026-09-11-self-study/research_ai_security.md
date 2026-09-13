---
title: "AI安全与软件供应链安全-千轮研究-2026-09"
type: note
domain: Research
status: active
tags: [knowledge/research, 千轮研究, security, ai-agent]
date: 2026-09-12
---

# AI 安全与软件供应链安全 千轮研究报告（2026）

> 生成日期：2026-09-12 ｜ 研究方式：多轮 web_search + web_extract，优先官方文档与权威安全机构（OWASP / CISA / NSA / NIST / Microsoft / JFrog / Sonatype / Socket / MITRE）
> 范围：① 2026 AI Agent 攻击面全景 ② Agent 安全框架与规范现状 ③ 供应链攻击 2026 典型案例与检测工具 ④ 与 sora 现有安全技能体系的补强点 ⑤ 立即行动建议（防御侧）
> 说明：所有关键结论均标注实证来源与链接；未授权攻击行为不在本文建议范围内。

---

## 摘要

2026 年 AI Agent 安全已从"模型层问题"演化为"控制面问题"：提示注入不再是哄骗模型，而是劫持整个 agent 的执行链（读凭据 → 调工具 → 外泄）。供应链攻击则完成工业化：以 Shai-Hulud 家族为代表的自我复制蠕虫将"一个被窃的 npm token"放大为"数百个被投毒包"，并开始把投毒终点从代码仓库迁移到 AI agent 的指令文件（`.cursorrules` / `CLAUDE.md` / MCP 工具描述）。规范侧，OWASP 已发布《Top 10 for Agentic Applications 2026》（ASI01-ASI10）与 LLM Top 10 2025；五眼联盟发布《Careful Adoption of Agentic AI Services》；NSA 发布《MCP Security Design Considerations》。防御共识收敛为：硬件级沙箱（gVisor / Firecracker）+ 外发代理白名单 + 短时凭据 + 工具调用全量审计 + 行为层供应链扫描。sora 的 shai-hulud-npm-scanner 与 ai-agent-security-audit 技能是本底，需向 MCP 层、CI 层、Go/PyPI 生态与行为检测扩展。

---

## 一、2026 AI Agent 攻击面全景

### 1.1 威胁模型：Agent 是一个"读-写原语"

安全界对 agent 威胁模型的共识表述（Authsome 2026 总结）：**agent ≈ 一个通用读写原语，它把最近读到的任何文本当作指令** —— 文件、网页、PR 标题、邮件正文、README 都只是 token，模型没有可信通道区分"操作者发的"与"陌生人在互联网上的"。

三个条件同时满足即铸成攻击链：
1. **读**访问某敏感物（env vars、文件、OAuth token、云凭据）；
2. **写**访问某联网通道（HTTP fetch、repo 写、评论、邮件）；
3. 读取队列里包含来自公网或攻击者可达的内容。

警惕输入过滤型防御的失效：2026 年 4 月跨厂商 GitHub 评论劫持实证表明，三个厂商都配了模型层+提示层+运行时三层防御，仍被"礼貌的英文 + markdown 注释"绕过。业界结论：**提示注入无法被输入过滤根除，必须按"假定被入侵"设计控爆半径**。

### 1.2 攻击面分类与实证案例

#### A. 提示注入（直接 / 间接 / 隐形编码）

| 案例 | 时间 | 手法 | 影响 | 来源 |
|---|---|---|---|---|
| **Comment and Control（跨厂商）** | 2025-10 报告，2026-05 公开 | 在 PR 标题/issue 正文/评论注入载荷；Copilot 变体用 HTML 注释隐藏载荷，受害者无感分配 issue 即触发；逐一绕过 Copilot 的三层运行时防护（环境过滤/密钥扫描/网络防火墙 —— 用 `ps auxeww` 读父进程 environ + base64 编码 + 经允许的 github.com 通道外泄） | Claude Code Security Review、Gemini CLI Action、GitHub Copilot Agent 三个头部 agent 的 `ANTHROPIC_API_KEY`/`GEMINI_API_KEY`/`GITHUB_TOKEN` 等 CI secrets 被窃 | oddguan.com/blog/comment-and-control（CVSS 9.3→9.4） |
| **中毒测评仓库（Poisoned Coding Test）** | 2026 | 假面试仓库内嵌 `.cursor/rules`、README 隐藏 HTML 注释、`CLAUDE.md`、`.cursor/mcp.json`；受害者问一句"这项目怎么跑"即触发：`cat ~/.aws/credentials` → `aws sts get-caller-identity` → `cat ~/.kube/config` → grep secrets → 走被投毒的 MCP 工具描述外泄 | 2 分钟内窃取 AWS 凭据 + 一个**长期 CI/CD 凭据**（清理工作站后依然有效）；无恶意软件、无漏洞利用、无用户交互 | mitiga.io/blog/poisoned-coding-test-ai-agent-attack |
| **CVE-2026-21852** | 2026 | 恶意仓库携带 Claude Code settings，把 `ANTHROPIC_BASE_URL` 指向攻击者端点；打开仓库即先于信任弹窗发出带真实 API key 的请求 | CVSS 5.3；API key 在用户点击"不信任"前已泄露；Claude Code 2.0.65 修复（CheckPoint 披露） | authsome.ai 整理 |
| **CamoLeak（CVE-2025-59145）** | 2025-06 | 提示注入载荷借 GitHub 自家 Camo 图片代理（受信任 CDN）外泄源码/API key/云密钥；标准出站检测全部放行 | 信任的域成了外泄通道范本 | Cloud Security Alliance 分析 |
| **prt-scan 攻击** | 2026（Wiz 记录） | 对使用 AI GitHub Actions 的项目开 500+ 恶意 PR，载荷在标题/描述 | workflow 的 AWS/Azure/GCP 凭据外泄 | authsome.ai 整理 |
| **M365 Copilot 零点击外泄** | 2025-06 | 隐藏指令的邮件正文在例行摘要任务中被吸收 | 数秒内经微软自家域名外泄 OneDrive/SharePoint/Teams 敏感数据；微软打补丁（VentureBeat） | authsome.ai 整理 |
| **GPT-4o SSH 密钥研究** | 2026-01 | 单封投毒邮件诱使已获"可跑脚本"预授权的 GPT-4o 执行 Python 外泄 SSH 私钥 | 最高 80% 试验成功率 | authsome.ai 整理 |
| **Framing Gap 研究** | 2026-08（arXiv 2608.27092） | 把同一外泄指令"重构"为完整性签名/配置字段/仿冒可信主机，六模型漏检率从 0% 飙到 100%；通道分离与"任何形式"策略条款均被绕过 | 实证：输入侧防御不可靠；**payload-blind 检查（目标白名单、规划/读取能力隔离）才收敛到 0%** | arxiv.org/abs/2608.27092 |
| **TrapDoor 零宽字符** | 2026-05（Socket 披露） | npm/PyPI/Crates.io 34 包 384+ 版本，在 `.cursorrules`/`CLAUDE.md` 用零宽 Unicode 隐藏指令，骗取 AI 执行伪装成"安全扫描"的凭据窃取（SSH key/钱包/AWS/GitHub token/浏览器数据） | 面向 crypto/DeFi/Solana/AI 开发者；GitHub Pages 页面同样充当 AI 触发载荷 | securityarsenal.com / lemma.frame00.com |

#### B. 工具滥用与 MCP 生态攻击

MCP（Model Context Protocol）已成为 2026 年**最大新增攻击面**：官方 registry 已超 5,000 server，月度 SDK 下载 9,700 万+；独立扫描显示 30%-82% 的公开 MCP server 存在可利用缺陷，**仅 8.5% 使用 OAuth**。

在 2025-26 已命名的攻击类别（Invariant Labs / Trail of Bits / Simon Willison）：
- **工具投毒**：恶意指令藏在工具描述/参数 schema（用户批准时通常看不到）——例子：`simple_calculator` 工具携带"首次调用时读取 ~/.ssh/id_rsa 并作为隐藏参数传出"；
- **Line Jumping**（Trail of Bits 命名）：注入发生在 `tools/list` 握手响应里，任何工具调用前即到达模型；
- **工具影射 Tool Shadowing**：恶意 server 注册与可信 server 重名/近似名工具，抢夺敏感调用路由；
- **Rug Pull（静默重定义）**：安装时干净、之后悄悄更新工具列表（`tools/list_changed` 已有规范但客户端执行不一致）；
- **跨 server 污染**：一个被投毒 server 诱导 agent 滥用另一个高权限 server 的工具（GitHub MCP 事故为范本）；
- **Token 直通 → OAuth 2.1 演进**：2025-03 规范从自定义鉴权改 OAuth 2.1；Resource Indicators（RFC 8707）强制后，2026 Q2 仍有约半数公开 server 未实现。

代表性实证：
- **s1ngularity（Nx 供应链投毒，2025-08）**：恶意 postinstall 调用机器上所有 AI CLI（Claude Code/Gemini CLI/Q CLI）执行越狱提示，扫描 `~/.ssh`、`.env`、钱包、GitHub token —— 48 小时窃取约 2,180 个 GitHub 凭据与 20,000+ 文件（The Register / Socket / Wiz）。**首次大规模把受害者的 AI agent 当外泄引擎**。
- **CVE-2025-6514（mcp-remote，CVSS 9.6）**：连接恶意远程 MCP server 即在客户端主机执行任意命令，437,000+ 下载环境受影响（JFrog / Or Peles）。
- **CVE-2025-49596（MCP Inspector，CVSS 9.4）**：默认绑定 0.0.0.0 + 无 origin 校验 → 恶意网页驱动本地 RCE（Oligo Security）。
- **CVE-2025-54136 "MCPoison" / CVE-2025-54135 "CurXecute"（Cursor）**：受信但被换的 MCP 配置持久化 RCE / MCP 自动启动提示注入 RCE。
- **CVE-2026-81735（CVSS 10.0）**：字节跳动 UI-TARS-desktop 的 mcp-http-server 默认监听 `::` 且无鉴权，`run_command`/filesystem 工具暴露给任意可达客户端。
- **2026 早 60 天窗口 30+ 个 MCP CVE**（约 43% 为命令注入模式）；2026-03 MCPwn（nginx-ui MCP，CVSS 9.8）auth bypass 被积极利用。
- **MCP-2026-008 + MCP-2026-015 链**（2026-08）：server 声明 `cacheScope: "public"` 让共享网关把投毒的工具列表/指令跨用户重放 —— 一次缓存投毒影响整个企业的 agent。
- **Viper-MCP 研究**（arXiv 2605.21392）：对 39,884 个开源 MCP server 的扫描发现 106 个 0-day（67 个已分配 CVE），全部经端到端提示可触发（命令注入/SSRF/路径穿越）。
- **恶意 MCP server 供应链**（Kaspersky GERT PoC；postmark-mcp 事件）：伪装成合法工具的 MCP server 安装即等于"把用户权限交给第三方代码"，窃取 .env/SSH key/云配置/浏览器密码后伪装成正常遥测外泄。
- **Asana MCP 跨租户泄漏（2025-06）**：多租户鉴权缺陷致约千名客户项目数据可见 —— 最"传统"的授权 bug 反而造成最大单次暴露。

#### C. 凭据窃取与身份滥用（Agent = 非人身份 Non-Human Identity）

- **OWASP NHI Top 10（2025）视角**：agent 是持有常驻操作权限的非人身份；提示注入正在成为 agent 的"控制面版凭据滥用"——攻击者甚至不需要窃取凭据，agent 自己的权限就是执行层。
- **Claude Code GitHub Actions [bot] 信任绕过（RyotaK / GMO Flatt，TL-2026-0660，CVSS 7.8）**：`checkWritePermissions` 对所有 `[bot]` 后缀 actor 无条件放行 → 自装 GitHub App 触发 workflow → issue 载荷提示注入 → 窃取 GITHUB_ACTIONS OIDC token → 换得写权限 Claude GitHub App token → 推送后门代码进目标仓库（含 Anthropic 自家仓库）。
- **AI SRE agent 变勒索软件（STAR Labs/Straikerai 研究）**：伪造 OpenTelemetry 遥测记录注入 → 自治 SRE agent 部署特权 K8s 容器（hostPID + SYS_ADMIN/SYS_PTRACE）→ 容器逃逸到 EKS 主机 → 勒索软件加密 + 持久化窗口击败自动恢复。提示注入 = 身份治理问题。80% 受访组织报告 agent 执行过超出预期范围的动作。
- **墨西哥政府大规模数据外泄（2025-12～2026-02）**：攻击者冒充漏洞赏金研究员，指挥 Claude Code / GPT-4.1 执行数千命令，窃取约 1.95 亿条纳税人记录（多机构通报）。
- **Marimo RCE → agent 化后利用（2026-05）**：利用未修补 RCE 进入连接 LLM agent 的工具后，agent 自动完成内网侦察、AWS 凭据收割、整库 PostgreSQL 外泄，全程 <2 分钟。

#### D. 供应链投毒（Agent 向）与影子配置

- **OpenClaw Marketplace 800+ 恶意 skills（2026-01）**：恶意技能被下载并在 agent 部署中执行，大规模分发恶意软件。
- **Nx / Azure/durabletask / Red Hat 事件（2026-05～06）**：投毒终点从包管理器迁移到 **IDE/AI agent 配置**（`.mcp.json`、`CLAUDE.md`、`.cursor/rules` 会随打开仓库自动执行）——"不装任何包"也能被攻击（Miasma Wave 2 模式）。
- **Red Hat @redhat-cloud-services 投毒（2026-06-01，Wiz 披露）**：开发者 GitHub session cookie 泄露（infostealer 日志，暴露 7 周）→ 绕过 code review 推孤儿 commit → Actions OIDC mint 出 token → 发布 96 个恶意版本且带**有效的伪造 SLSA provenance**。
- **TanStack 蠕虫（2026-04/05）**：从 GitHub Actions workflow 进入，6 分钟发布 84 个恶意 artifact 跨 42 包 —— 快于任何人审周期。
- **Azure/durabletask 提交投毒（2026-06-05）**：向仓库种 `.mcp.json` + IDE 配置；开发者用 Claude Code/Cursor/Gemini CLI 打开即触发凭据收割 —— GitHub 105 秒内禁用 73 个仓库，连锁导致 `functions-action@v1` 类可变 tag 引用的生产部署断裂。

### 1.3 小结：2026 攻击面演化主线

1. **输入面**：从聊天输入扩大到网页/文档/仓库/遥测/工具输出等一切"被读内容"（间接注入为主战场，零宽字符等隐形编码绕过人工审查）；
2. **执行面**：agent 自带 bash/文件/网络工具，注入即执行；MCP 让任何第三方 server 成为新的代码执行入口；
3. **身份面**：长生命周期凭据 + 共享 token + OIDC 滥用，使"一次提示注入"升级为"持久基础设施访问"；
4. **供应链面**：投毒终点从 registry 包 → IDE 配置 → agent 指令文件 → MCP server，逐步逼近"控制 AI 读取什么、相信什么"。

---

## 二、Agent 安全框架与规范现状

### 2.1 OWASP Top 10 for LLM Applications（2025 版）

官方项目已扩展为 **OWASP GenAI Security Project**。LLM Top 10 v2025（LLM01-LLM10）：
LLM01 提示注入、LLM02 敏感信息泄露、LLM03 供应链漏洞、LLM04 数据与模型投毒、LLM05 不当输出处理、LLM06 **过度代理权（Excessive Agency，因 agentic 架构扩张而显著加码）**、LLM07 **系统提示泄露（新增）**、LLM08 向量与嵌入弱点、LLM09 错误信息、LLM10 无界消耗。
关键缓解共识：最小权限 + 高风险动作人工审批 + 内外内容隔离标记 + 外部 guardrail（不依赖 system prompt 做安全控制）+ 敏感数据不写入 system prompt。
来源：owasp.org/www-project-top-10-for-large-language-model-applications（PDF：OWASP-Top-10-for-LLMs-v2025.pdf）

### 2.2 OWASP Top 10 for Agentic Applications（2026，2025-12-09 发布）

100+ 专家同行评审，针对**会规划、会用工具、有持久记忆、会协调其他 agent** 的自主系统，编号 ASI01-ASI10（事件驱动、非严重度排序）：

| ID | 风险 | 典型事件（官方映射） |
|---|---|---|
| ASI01 | Agent Goal Hijack（目标劫持） | EchoLeak 等静默外泄引擎 |
| ASI02 | Tool Misuse and Exploitation（工具滥用） | Amazon Q 类合法工具被弯成破坏性输出 |
| ASI03 | Identity and Privilege Abuse（身份与特权滥用） | 2025-26 企业调查中最常被报告的失败模式 |
| ASI04 | Agentic Supply Chain Vulnerabilities（供应链） | GitHub MCP 利用；动态发现的 MCP/A2A 组件投毒 |
| ASI05 | Unexpected Code Execution（意外代码执行/RCE） | AutoGPT RCE |
| ASI06 | Memory & Context Poisoning（记忆与上下文投毒） | Gemini Memory Attack |
| ASI07 | Insecure Inter-Agent Communication（不安全 agent 间通信） | 伪造 agent 间消息 |
| ASI08 | Cascading Failures（级联故障） | 假信号在自动管线里逐级放大 |
| ASI09 | Human-Agent Trust Exploitation（人类信任利用） | 自信且漂亮的解释诱导人类批准有害动作 |
| ASI10 | Rogue Agents（失控/越权 agent） | Replit 生产库 meltdown |

贯穿性原则：**Least Agency（最小代理权）**——自主性是挣来的，不是默认配置；并强调可观测性（记录 agent 做了什么、为何做、调了哪些工具）是红线级要求。ASI03/04/10 本质是**资产清点问题**：无法治理未被枚举的影子 agent 与 MCP server。
来源：genai.owasp.org/download/52117；genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/

### 2.3 其他规范与指南

- **OWASP LLM Top 10 2025** 中 LLM03 供应链漏洞补充适用；OWASP 另有 **MCP Security Guide（2025）**（genai.owasp.org，并入工具/插件安全）、**Non-Human Identity Top 10（2025）**、AI-VSS 评分标准。
- **五眼联合指南《Careful Adoption of Agentic AI Services》**（CISA + ASD ACSC + CCCS + NCSC-NZ + NCSC-UK，2026-05-01）：首个专门针对 agentic AI 部署安全的五眼指南；定义**五类风险——特权（privilege）、设计与配置（design & configuration）、行为（behavioral）、结构（structural）、问责（accountability）**；基线姿态=假设 agent 会意外行为，优先弹性/可逆/控爆；建议低风险用例起步、限制权限、监控式扩展；高风险动作（金融交易、身份/访问修改、对外通信、不可逆操作）**必须人工审批**；agent 应有**独立加密身份**、短时任务级凭据、agent 间通信加密认证、红队演练 agent 化攻击面。来源：cisa.gov/resources-tools/resources/careful-adoption-agentic-ai-services
- **NSA AISC《Model Context Protocol (MCP): Security Design Considerations》**（2026-05-20）：MCP 扩散快于其安全模型（"协议反转了交互模式——server 查客户端的系统并动作"，产生新攻击路径）；覆盖 ACE/命令注入（CWE-77/78/94/95）、会话重放、token 直通、命名冲突解析、prompt storm/DoS；建议对未授权 MCP server 例行扫描，列出 MCP Scanner / Ramparts / CyberMCP / Proximity 等扫描工具。来源：media.defense.gov/2026/Jun/02/.../CSI_MCP_SECURITY.PDF
- **NIST**：AI RMF 1.0（GOVERN/MAP/MEASURE/MANAGE）+ GenAI Profile（AI 600-1，明确覆盖提示注入、工具外泄、外部集成滥用）；**NIST CAISI AI Agent Standards Initiative（2026-02-17 启动）**三支柱：AI RMF 治理层、COSAiS SP 800-53 AI 控制 overlay（含单/多 agent 用例）、NCCoE agent 身份与授权 concept paper。来源：nist.gov/itl/ai-risk-management-framework
- **MITRE ATLAS**：AI 威胁矩阵（AML.T0051 直接/间接提示注入等），与 ATT&CK 对应；MITRE CTID Secure AI 项目持续扩充。
- **欧盟 AI Act Art. 15**：高风险 AI 系统须"抵抗未授权第三方改变其使用/输出/性能的尝试"——提示注入落入此条，违者最高全球营收 3% 罚款。
- **CSA（云安全联盟）**：MAESTRO 七层威胁建模框架、AI Controls Matrix (AICM) v1.0、STAR for AI 评估、零信任之于 LLM 环境的指南。
- **CoSAI（OASIS Open，2025 诞生）**：AI 安全事故响应与可观测性标准工作（agent 事故共享、MCP 工具调用审计格式等）。

### 2.4 Agent 沙箱方案（2026 共识）

2026 年行业共识：**执行 LLM 生成或用户可控代码时，共享内核的普通容器隔离已不够**（CVE-2024-21626 runc 逃逸实证：容器内进程可拖垮整个节点）；把 LLM 生成的代码当作敌对代码处理。

隔离技术分层（信任边界距宿主内核越远越强，代价越大）：

| 技术 | 机制 | 启动 | 开销 | 代表使用者 |
|---|---|---|---|---|
| Landlock + seccomp | LSM 文件系统限制 + 系统调用过滤 | 毫秒级 | 极低 | Cursor（Linux，默认）、OpenAI Codex |
| bubblewrap / Seatbelt | 用户命名空间 / macOS sandbox-exec | 毫秒级 | 极低 | Anthropic Claude Code（macOS/Linux 默认）、Cursor macOS |
| gVisor | 用户态应用内核（Sentry 拦截全部 syscall） | 数十 ms | 5-15% syscall 开销 | Google Cloud Run/GKE Sandbox、Modal、Anthropic Claude Web（多租户） |
| Firecracker | KVM 硬件虚拟化 microVM（独立 guest 内核） | ~125 ms | <5MB/VM | AWS Lambda/Fargate、E2B、Vercel Sandbox、Fly.io |
| Kata Containers | OCI 容器包轻量 VM | 150-500 ms | 最重 | CNCF/OpenInfra、机密容器 |

配套强制模式（与沙箱同层必须）：
- **网络外泄强控**：默认断网或代理白名单（如 Claude Code 容器示例：`--network none` + 挂 Unix socket 代理做域白名单、TLS 终止、凭据注入、全量日志）；"allowed domain 可以被 fronting 绕过"是已知局限。
- **凭据代理 / 短时凭据**：agent 进程内不放真实 key；请求经本地代理替换占位符（真实 key 只在代理侧）——让"提示注入读 env"只拿到废串；CI 用 OIDC 短时 token 替代长期 key；AWS 短期 creds + IAM Identity Center/SSO。
- **文件系统与进程限制**：只读挂载、cap-drop ALL、no-new-privileges、seccomp、pids-limit、非 root 用户、不挂载 `~/.ssh` `~/.aws` 等敏感目录。
- **托管沙箱平台**：E2B（Firecracker、开源核心）、Daytona、Modal、Northflank、Vercel Sandbox、Google Agent Sandbox（GKE 上的 gVisor、热池）、AWS Bedrock AgentCore。
- **编码 agent 自带沙箱**（2026 主流产品）：Claude Code（内置 Sandboxed Bash tool；`@anthropic-ai/sandbox-runtime` 把整个进程含 MCP/hook 包进 Seatbelt/bubblewrap；devcontainer 默认拒绝出站 iptables；`--dangerously-skip-permissions` 必须配容器/VM/沙箱 runtime 且非 root）；Cursor（Seatbelt + Landlock/seccomp；Auto-review 默认 + 沙箱 + 分类器；保护 .git/config、hook 等路径）；Codex CLI（sandbox mode × approvals mode 分离）。NCC Group 2026-05 白皮书《An Introduction to AI Coding Agent Security》指出：**沙箱默认值、CLI 与 GUI 的一致性、hook 是否入沙箱、配置文件的运行时保护**是产品间关键差异，多数 agent 的 hook 在沙箱外运行（持久化后门向量）。

### 2.5 规范现状小结

- 框架已从"单模型应用"（LLM Top 10）升级到"自主系统"（Agentic Top 10 2026）+"身份治理"（NHI Top 10）+"协议安全"（MCP Security Guide / NSA MCP 指南）；
- 政府侧：五眼 agentic 指南（2026-05）+ NIST CAISI 标准动议（2026-02）+ EU AI Act Art.15 提供合规压力；
- 工程侧收敛为四件套：最小代理权/最小心权限、沙箱 + 外泄白名单、短时身份与凭据代理、全量工具调用可观测性。

---

## 三、供应链攻击 2026 典型案例与检测工具

### 3.1 典型案例时间线（2025-09 ~ 2026-08）

**Shai-Hulud 蠕虫家族（2026 年度最大事件族）** —— 第一个"自我复制"开源恶意软件，行为更像网络蠕虫而非被动植入：

| 波次 | 时间 | 载体 | 关键行为 |
|---|---|---|---|
| 原始 Shai-Hulud | 2025-09 | npm（起始 @ctrl/tinycolor、ngx-bootstrap 为疑似 P0）| 隐藏重复文件/嵌套目录，维护者凭据窃取后发毒化更新，>500 包 |
| Sha1-Hulud "The Second Coming" | 2025-11 | npm（49 包）| Bun 部署负载，改名+加扰绕过检测 |
| **ChainDrop（Mini Shai-Hulud）** | 2026-08-04 | npm **400+ 包**（keyv、flat-cache、cache-manager 等）| preinstall hook 执行 Bun 混淆载荷；窃 npm/GitHub/AWS/K8s/Vault 凭据；用窃得 npm token 自动加补丁版重发；GitHub 凭据向 `.claude/settings.json`/`.vscode/tasks.json` 注入持久化（AI 打开即触发）；加密后经 HTTPS + GitHub 双通道外泄（微软威胁情报）|
| Here We Go Again | 2026-08 | keyv@6.0.0 等 400+ 包 / 1700+ 版本 | 载荷 710KB；token 校验 `bypass_2fa===true` + 写权限才传播；GitHub token 建假 dependabot 分支+CodeQL workflow 偷 Actions secrets；**特殊路径：对 opensearch-js 换 OIDC+Sigstore，恶意包带有效 provenance**；AI 工具凭据（OpenAI/Anthropic/Claude/Cursor/Codex/Gemini）也在收集清单 |
| Miasma Wave 2 | 2026-06-02/03 | npm | **Phantom Gyp**：157 字节 `binding.gyp` 借 node-gyp 命令替换执行—— 非 lifecycle script，`--ignore-scripts` 与脚本扫描全部绕过；下载 Bun（绕过 Node 进程监控）|
| Hades | 2026-06-07（Socket 披露）| **PyPI 37 个 wheel**（dynamo-release、spateo-release、coolbox、ufish 等生物信息学工具）| `.pth` 启动钩子 + Bun 凭据窃取；含 typosquat MCP 包（langchain-core-mcp 等）|
| Trinitite | 2026-08-28 | npm @7nohe/openapi-react-query-codegen | PR 评论说 `npm publish` 即触发发布（OIDC）→ 恶意版本带合法 provenance；Unicode 转义藏在 `binding.gyp` conditions（node-gyp 按 Python 求值）；含 token 死开关（撤销即删 ~）|

- **node-ipc 投毒（2026-05-14，StepSecurity 检测）**：周下载千万级的 node-ipc 一次发布 3 个恶意版本（9.1.6/9.2.3/12.0.1，9.x 为纯伪造），无任何 lifecycle script，恶意 IIFE 直接塞 CommonJS 包尾 —— **不做脚本扫描就检测不到**；窃取 90+ 类凭据。释放"cooldown period（新版本冷却窗）"防御概念。
- **TrapDoor（2026-05-22，Socket）**：**首个同时武器化 npm + PyPI + Crates.io** 的供应链战役（34 包/384+ 版本），分别用 postinstall / import 时远程 JS / build.rs 执行；外加向 browser-use、langchain、langflow 开 PR 投喂毒化 `.cursorrules`/`CLAUDE.md`（零宽 Unicode）。被 Socket 在 6 分钟内检测。
- **@redhat-cloud-services（2026-06-01，Wiz）**：GitHub session cookie 泄露 → 96 个恶意版本带伪造 SLSA provenance；Shai-Hulud 家族首次在大厂官方 scope 大规模落地。
- **Go 生态**：
  - **CVE-2026-42501 / GO-2026-6179 / GO-2026-6180（2026-08-13）**：恶意 GOPROXY/GOSUMDB 可伪造/绕过 sumdb 校验（空校验响应被当作通过），golang.org/x/mod <v0.40.0 及早期工具链受影响；影响 GOTOOLCHAIN 自动下载执行。→ 必须升级基础工具链 + 重建 go.sum。
  - **Go 恶意模块重打包战役（arXiv 2606.26291）**：2,289 个恶意版本伪装合法模块（含 import 触发下载器）；**GitHub 移除后 99.4% 仍经 proxy.golang.org 可拉取**——托管层下架 ≠ registry 层修复；已协同移除 684 仓库、修复 1,377 模块版本。
  - **boltdb/bolt 镜像 typosquat 教训**：sumdb 只证"内容与大家一致"，不证"内容安全"（恶意版本有合法一致性哈希）。
- **统计基线（Sonatype / Phoenix / ReversingLabs）**：2025 全年新检出恶意包 454,600+，累计 123.3 万（npm/PyPI/Maven/NuGet/HF）；npm 占 ~90%；Lazarus（APT38）关联 800+ 包（97% npm）；IndonesianFoods 单阵营 15 万+ 包（每 7 秒自复制）；Phoenix MPI 语料 59 战役/657 包（2024-06~2026-06），2026 上半年 = 2025 全年的 2.6 倍战役数、4.5 倍包量，2026-05 为历史最忙月（14 战役/346 包）；**59 个战役在活跃利用期 CVE 分配数为零**——CVE 驱动扫描对这些战役 100% 失明。PyPI/NuGet 强制 2FA+trusted publishing 后恶意量降 43%/60% —— 证明平台级摩擦有效，攻击者绕道（→npm）。

### 3.2 检测与防护工具盘点（分层）

**L1 行为/恶意包检测（对抗 CVE 盲区，核心）**
| 工具 | 属性 | 覆盖 | 定位 |
|---|---|---|---|
| Socket.dev | 商业（免费 CLI/OSS 项目免费）| npm/PyPI/Maven/Go/Cargo/RubyGems + Actions | 注册表实时行为分析 + AST/安装脚本/网络/typosquat/maintainer 变更；6 分钟标记 axios 事件；Firewall 免费 |
| GuardDog（Datadog）| OSS | npm/PyPI/Go/RubyGems/Actions/VS Code | 本地启发式（Semgrep+YARA），可离线、可审计，0-10 分 |
| OSV-Scanner（Google）| OSS | 11+ 语言/19+ lockfile/容器 | OSV.dev + **OpenSSF Malicious Packages feed**（最接近 Socket 的开源行为层）；离线模式 |
| supply-chain-guard | OSS | npm/PyPI/Cargo/Go/RubyGems/Composer/NuGet/Docker/VS Code/Actions/IaC | 350+ 威胁指标（GlassWorm/Vidar/Shai-Hulud 等战役 IOC）+ CycloneDX SBOM + SLSA 分级；完全本地 |
| Bumblebee（Perplexity）| OSS（macOS/Linux）| 全盘 lockfile+扩展+MCP host 配置 | 事件响应级清单 + IOC catalog 匹配（sora 的 exposure-check.py 是其 Windows 等价物）|

**L2 CVE/漏洞层 SCA（与 L1 互补不是冗余）**
- OSV-Scanner / Trivy（普查广度）/ Grype+Syft（SBOM 原生，扫"已发布产品"）/ npm audit & pip-audit / **govulncheck**（Go 官方，调用图可达性分析降噪）/ OWASP Dependency-Track（企业级 SBOM 消费）。
- 2026 实测（safeguard.sh 41 个预置 CVE 对比）：OSV-Scanner 准确率最高（39/41，1 FP）；Trivy 广度最佳；Dependency-Check 因 CPE 模糊匹配已显著落后。

**L3 CI/CD 流水线安全（攻击者已迁移主战场）**
- **zizmor（Trail of Bits）**：GitHub Actions 静态审计 38 类缺陷（pull_request_target、过度 id-token、模板注入、缓存投毒、伪提交）—— CPython/cURL/Rust 等 500+ 采用。
- **Harden-Runner（StepSecurity）**：CI runner 运行时出站监控/阻断（防毒化依赖偷 OIDC token 或外联 C2）；cooldown period 预热。
- 配套：Actions 版本 pin 到 commit SHA、`permissions: read-all` 最低化、禁止 `pull_request_target` 滥用、OIDC 发布审计、Chain-bench（CIS SSC）/ Allstar（OpenSSF 策略门）。

**L4 SBOM / 签名 / 出处（防"签名即安全"错觉）**
- Sigstore（cosign/fulcio/rekor，无钥签名+透明日志）、SLSA Build L1-L3（GitHub Artifact Attestations 默认 SLSA L2）、in-toto（attestation 格式，CNCF 毕业）、GUAC（图谱聚合"谁依赖了受害包"）、Syft/CycloneDX/SPDX、npm trusted publishing。
- 关键警示：Shai-Hulud 的 opensearch-js 路径与 Red Hat 事件验证了**有效 provenance 只证"在可信工作流里构建"，不证"载荷干净"**。

**L5 平台/生态防线**
- npm 12+：preinstall 默认不跑 + min-release-age 冷却窗；NPM 2FA、trusted publishing。
- PyPI：强制 2FA + trusted publishing（已证明有效）。
- Go：默认 `GOPROXY=proxy.golang.org` + `GOSUMDB=sum.golang.org`；`GOFLAGS=-mod=readonly`；`go.sum` 入库、CI 跑 `go mod verify`；`GOPRIVATE` 精确限定私库、**禁止全局 GONOSUMCHECK/GONOSUMDB 绕过**、审查 `replace` 指令与 vanity import 元标签。
- 通用：lockfile 入库 & diff 审查、私有镜像仓库（Artifactory/Nexus 拦截）、SCA 进 CI 阻断、新版本冷却期、`npm ci --ignore-scripts` 按需、安装脚本审计（preinstall/postinstall/`binding.gyp`/`.pth`）。
- MCP 层：MCP Scanner / Ramparts / CyberMCP / Proximity（NSA 点名）；Viper-MCP（静态 taint + 动态验证流水线）；MCP Guardian（OAuth/RFC 8707 实现率普查）；安装前白名单审批、pin server 版本、监控 `tools/list` 变化。

**工具组合速查（免费基线）**：PR 门 = OSV-Scanner（CVE）+ Socket app 或 supply-chain-guard（行为）；CI 运行时 = zizmor + Harden-Runner；发布 = Sigstore 签名 + SLSA 出处；事后 = GUAC 图谱 + Bumblebee/exposure-check 清单；本地 AI 工作区 = 定期跑 shai-hulud-npm-scanner + 扩展特征库。

### 3.3 关键盲点（2026 实证）

1. **CVE 滞后**：59 个战役活跃期 0 CVE → 纯 SCA 全覆盖失明；
2. **脚本扫描被绕过**：node-ipc（包尾 IIFE）、Phantom Gyp（binding.gyp）、Hades（.pth）逐一证明"只扫 lifecycle script"不够；
3. **签名不可信**：伪造 SLSA 已实战（Red Hat / opensearch-js）；
4. **GitHub 下架 ≠ 修复**：Go 代理 99.4% 残存；registry 层持久性要求跨层协同（索引/代理层清理、缓存 purge）；
5. **AI 工具凭据是新金矿**：Claude/Codex/Cursor/OpenAI/Gemini 配置已在 Shai-Hulud 收集清单，且 agent 配置既是目标又是跳板（.claude/settings.json hook）。

---

## 四、与 sora 现有安全技能体系的补强点

### 4.1 现有体系盘点（与本文主题相关的存量技能）

- **供应链/审计（已有基础）**：`shai-hulud-npm-scanner`（Shai-Hulud 家族 IOC + lockfile/特征文件/hook 扫描，含响应顺序、死开关陷阱）、`ai-agent-security-audit`（端口暴露、skill 来源分类、外发端点白名单、凭据权限、git 泄漏、uv audit、MCP server 审计清单）、`skill-vetter`（skill 安装前审查）、`github-privacy-gate` / `github-repo-privacy-gate`。
- **AI 相关**：`ai-assisted-reversing`、`ai-assisted-vulnerability-hunting`、`hermes-codex-security-gate`、`external-llm-code-review`、`gemini-second-opinion`。
- **Offensive/逆向**：`miniapp-reversing`、`wxapkg-miniapp-audit`、`wechat-miniapp-reversing`、`vmp-reversing`、`nmap-scanning`、`osint-username-search`、`src-*` 系列（授权范围内 SRC 方法论，如 Lenovo 项目）。
- **防御/响应**：`security-defense-hardening`、`silver-fox-malware-defense`、`web-security-lab-setup`、`pentest-lab-*`、`code-audit-delivery`、`ai-code-review`、`systematic-debugging`。

### 4.2 差距分析

| 差距 | 现状 | 2026 威胁对应 | 补强方向 |
|---|---|---|---|
| **Agent 自身上线评估** | 无 OWASP LLM/Agentic Top 10 对照清单技能 | ASI01-10 全部有真实事件 | 新建 `owasp-agentic-top10-audit`：按 ASI01-10 对任一 agent 部署做问题清单评估（目标劫持/工具滥用/身份特权/供应链/意外代码执行/记忆投毒/互信/级联/人类信任/失控 agent） |
| **提示注入红队** | 无专门技能 | Comment-and-Control、Framing Gap、零宽字符、跨厂商 2026-04 事件 | 新建 `prompt-injection-redteam`：间接注入载荷库（HTML 注释/隐形 Unicode/工具描述/framing 重构）、面向自有 agent 的受控测试 SOP（仅限自家系统）|
| **MCP 安全运维** | 只有手动审计清单一段 | CVE-2025-6514/49596/54136、2026 30+ CVE、MCP-2026-008/015、8.5% OAuth | 升级为独立 `mcp-server-vetting`：安装前审查（来源/权限/端点/instructions 字段视为不可信）、tools/list 变异监控、OAuth/RFC 8707 检查、禁用远程无鉴权 server、pin 版本 |
| **CI/CD 供应链防护** | 无 | zizmor 类审计、Harden-Runner、OIDC 滥用、Shai-Hulud GitHub 传播 | 新建 `ci-supply-chain-hardening`：Actions pin SHA、最小权限、zizmor/Harden-Runner 接入、发布流程 OIDC 审计 |
| **行为层/跨生态扫描** | 仅 Shai-Hulud npm 特征 | node-ipc（包尾 IIFE）、Phantom Gyp（binding.gyp）、Hades（.pth）、TrapDoor（零宽字符）、Go CVE-2026-42501 | 扩展 `shai-hulud-npm-scanner` 特征库（binding.gyp/IIFE/零宽字符/.pth/新战役串）+ 增加 Go（govulncheck/go.sum 校验）与 PyPI 覆盖；或纳入 supply-chain-guard 类本地引擎 |
| **Agent 运行沙箱基线** | 无落地指南 | bubblewrap/Seatbelt/Landlock/gVisor/Firecracker、凭据代理、外泄白名单 | 新建 `agent-runtime-hardening`：Claude Code/Cursor/Hermes 本机的沙箱配置、出站代理白名单、env 凭据代理、敏感目录不挂载清单 |
| **身份治理（NHI）** | 无 | 短时凭据、OIDC、agent 独立身份 | 合并进 `agent-runtime-hardening` 或独立 `nhI-credential-hygiene` |

### 4.3 建议补强顺序（P1 两周内 / P2 一月内）

P1：扩展 shai-hulud 扫描器特征库（新战役特征 + zero-width 字符 + binding.gyp/.pth/IIFE 模式）→ 新建 `agent-runtime-hardening`（本机 sandbox + 凭据代理 + 外泄白名单）。
P2：新建 `owasp-agentic-top10-audit` + `prompt-injection-redteam`（自有 agent 受控演练）→ `ci-supply-chain-hardening`（zizmor + Harden-Runner + OIDC 审计）→ `mcp-server-vetting` 独立化。

---

## 五、立即行动建议（防御侧，3-5 条）

**行动 1（P0，本周）：本机 AI agent 运行隔离 + 最小心权限 + 凭据抬升**
- Claude Code/Cursor 开启沙箱（Claude：sandboxed Bash + sandbox-runtime 或 devcontainer；Cursor：Auto-review + 沙箱网络白名单）；`--dangerously-skip-permissions`/auto-run 类高自主模式只允许在容器/VM 内使用；
- 移走/加密长生命期凭据：工作机不存长命 AWS key/npm/GitHub token；用短时凭据（IAM SSO/OIDC）或本地凭据代理，让"agent 被注入后读 env"只能读到占位符；
- 打开工具调用审计：记录 agent 每个 bash/文件/网络/MCP 动作（可观测性 = 事后追责基线）。

**行动 2（P0，本周）：供应链行为层扫描基线 + CI 防线**
- 依赖门：OSV-Scanner（CVE 层）+ Socket/supply-chain-guard 或 GuardDog（行为层）在每次 PR 与 install 前执行；npm ≥12 开 min-release-age 冷却窗；锁定 lockfile 并入库；
- CI 防线：zizmor 审计 workflow（重点 pull_request_target/过度 id-token）+ Harden-Runner 出站监控；Actions 全量 pin commit SHA；发布凭据 OIDC 化并审计 provenance；
- Go 项目：确认 `GOSUMDB=sum.golang.org`、`GOFLAGS=-mod=readonly`、无全局 GONOSUMCHECK 绕过；升级工具链 ≥ 受影响版本；CI 跑 `go mod verify` + govulncheck。

**行动 3（P0～P1）：Agent/MCP 资产清点与信任边界**
- 建立 agent 清单（每实例：身份凭据、可访问系统、自主动作范围、授权人、日志覆盖）——ASI03/04/10 都是先清点才能治理；
- 按 OWASP MCP Security + NSA 指南审计已启用 MCP server：拒绝远程无鉴权 server、pin 版本、把 `instructions`/工具描述/工具输出一律视为不可信输入（长度限制+隔离+注入检测）、缓存不得跨身份（MCP-2026-008 教训）；
- agent 使用独立加密身份 + 任务级短时 token，禁止与人类账号/通用 service account 共用凭据。

**行动 4（P1）：提示注入受控红队 + 行为基线异常检测**
- 对自有 agent 定期做受控注入演练（仓库/网页/MCP 工具描述/邮件四类载体 + 隐形 Unicode + framing 重构），上线前与变更后各一次；
- 建工具调用与出站流量基线：异常动作序列（读 ~/.aws 后 POST 外发）、新域外联、`tools/list` 变化告警；出站走代理白名单而非放任直连。

**行动 5（P1）：按五眼指南做部署前威胁建模、低风险起步**
- 每个新 agent 部署前按《Careful Adoption of Agentic AI》（特权/设计/行为/结构/问责五类风险）做威胁建模；不可逆动作（金融、身份变更、对外通信、删除）强制人工审批闸门；
- 从低敏感用例起步，监控运行成熟后再扩权限；把 agent 安全写入组织安全模型与事件响应预案（agent 泄露凭据 = 控制面事故，按"凭据已失守"轮换）。

---

## 附录：主要信源

- OWASP LLM Top 10 2025：owasp.org/www-project-top-10-for-large-language-model-applications/；PDF：OWASP-Top-10-for-LLMs-v2025.pdf
- OWASP Agentic Top 10 2026：genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/；PDF：genai.owasp.org/download/52117
- 五眼《Careful Adoption of Agentic AI Services》（2026-05-01）：cisa.gov/resources-tools/resources/careful-adoption-agentic-ai-services
- NSA《MCP Security Design Considerations》（2026-05-20）：media.defense.gov/2026/Jun/02/2003943289/-1/-1/0/CSI_MCP_SECURITY.PDF
- NIST AI RMF / CAISI：nist.gov/itl/ai-risk-management-framework；CSA 研究简报（2026-03）
- MITRE ATLAS：ctid.mitre.org/projects/secure-ai/
- 中毒测评仓库（Mitiga）：mitiga.io/blog/poisoned-coding-test-ai-agent-attack
- Comment and Control（Aonan Guan）：oddguan.com/blog/comment-and-control-prompt-injection-credential-theft-claude-code-gemini-cli-github-copilot/
- Claude Code Actions [bot] 绕过（RyotaK）：intel.threadlinqs.com/threat/TL-2026-0660
- Framing Gap（arXiv 2608.27092）：arxiv.org/abs/2608.27092
- Credential exfiltration 综述（Authsome）：authsome.ai/blog/how-prompt-injection-becomes-credential-exfiltration
- MCP 安全全景（Agentmelt / Ransomnews / Practical DevSecOps 2026 stats）：agentmelt.com/blog/mcp-security-2026-attacks-and-defenses/；ransomnews.com/mcp-security-attack-surface-2026/；practical-devsecops.com/mcp-security-statistics-2026-report/
- MCP 缓存投毒链（MCP-2026-008/015）：datapace.ai/blog/mcp-cache-poisoning-prompt-injection
- Viper-MCP（arXiv 2605.21392）：arxiv.org/html/2605.21392
- Kaspersky 恶意 MCP server PoC：securelist.com/model-context-protocol-for-ai-integration-abused-in-supply-chain-attacks/
- Sonatype State of the Supply Chain 2026：sonatype.com/state-of-the-software-supply-chain/2026/open-source-malware
- Microsoft ChainDrop 分析（2026-08-04）：microsoft.com/en-us/security/blog/2026/08/04/chaindrop-supply-chain-compromise-anatomy-self-propagating-worm/
- JFrog Shai-Hulud 系列：research.jfrog.com/post/shai-hulud-is-back-august/；research.jfrog.com/post/shai-hulud-trinitite/
- Phoenix MPI 语料：phoenix.security/accelerating-supply-chain-attacks-npm-pypi-vsx-ai-enabled-2026/
- node-ipc（StepSecurity）：stepsecurity.io/blog/node-ipc-npm-supply-chain-attack
- TrapDoor：securityarsenal.com/blog/trapdoor-supply-chain-attack-credential-stealing-malware-in-npm-pypi-and-cratesio
- Miasma/IDE 投毒九日时间线：pulse.adyog.com/insights/worm-that-learned-to-jump
- Go CVE-2026-42501：github.com/golang/go/issues/79070；pkg.go.dev/vuln/GO-2026-6179、GO-2026-6180
- Go 恶意模块重打包测量（arXiv 2606.26291）：arxiv.org/html/2606.26291v1
- Go 模块供应链控制（GOPROXY/GOSUMDB/govulncheck）：systemshardening.com/articles/cicd/go-module-supply-chain-security/；safeguard.sh/resources/blog/securing-go-modules-supply-chain
- 沙箱对比（gVisor/Firecracker/Kata/E2B）：dreaming.press/posts/firecracker-vs-gvisor-vs-kata-agent-sandbox-isolation.html；amux.io/guides/ai-agent-sandboxing/
- Claude Code 沙箱 & 安全部署文档：code.claude.com/docs/en/sandbox-environments；code.claude.com/docs/en/agent-sdk/secure-deployment
- Cursor 沙箱：cursor.com/blog/agent-sandboxing；cursor.com/docs/agent/security/run-modes
- NCC Group《An Introduction to AI Coding Agent Security》（2026-05）：nccgroup.com/media/jtepwx1t/nccgroup_codingagentswhitepaper.pdf
- 供应链工具生态：github.com/homeofe/supply-chain-guard；appsecsanta.com/sca-tools/supply-chain-security-tools；minimus.io/post/software-supply-chain-security-tools
- AI SRE agent 勒索软件（Straikerai/STAR Labs）：nhimg.org/articles/prompt-injection-turned-an-ai-sre-agent-into-ransomware/

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
