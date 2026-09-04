# Hermes → Codex 授权安全调用策略（强约束版）

> 来源：sora 定稿 · 2026-09-04 · 落地为 skill: `hermes-codex-security-gate`
> 适用：Hermes 编排层派活 Codex/其他执行 Agent 前的强制 Policy Gate

## 核心原则
```
授权优先于执行 · 范围优先于效率 · 隔离验证优先于真实目标验证
人工审批优先于 Agent 自主决策 · 最小证据优先于扩大访问
```

## 调用链
```
User → Hermes Orchestrator → Policy Gate → Codex → Approved Tools → Isolated/Allowlisted Env
```

## Policy Gate 三分类
- SAFE：允许自动执行
- REVIEW_REQUIRED：等待人工批准
- BLOCKED：不得下发任何执行 Agent

## 触发词分类速查

### BLOCKED（凭证类，默认）
密码抓取 / Cookie 抓取 / Session Token 获取 / API Key 提取 / Access Token 获取 / SSH Key 获取 / 浏览器凭证读取 / 系统凭证转储 / 登录信息窃取 / 从真实用户环境提取认证信息

豁免条件（全满足才可降级为验证）：
1. 完全本地实验环境 2. 虚构测试账号 3. 人工生成测试凭证 4. 不涉及真实用户 5. 不访问第三方系统
豁免后只允许验证「漏洞是否可能导致凭证暴露」，不实际收集真实凭证

### REVIEW_REQUIRED（安全控制绕过类）
绕过认证 / 授权 / MFA / WAF / EDR / 反作弊 / 安全策略 / 访问控制 / 沙箱 / 检测 / 隐藏执行 / 规避日志 / 规避审计 / 反检测 / Evasion / Defense bypass

目标属真实第三方系统且授权不明确 → BLOCKED

### NETWORK_DENY（真实网络目标）
- 扫描公网 / 未列入授权清单的 IP / 枚举未知子域 / 自动发现并攻击相邻资产 / 扩大到供应商/CDN/云服务商/合作伙伴 / 扫描第三方 SaaS / 对真实用户账号测试
- 所有网络目标必须存在于 AUTHORIZED_TARGETS

### SRC/Bug Bounty 双重确认（「这是 SRC」≠ 充分授权）
必须同时确认：Program（项目/平台/是否仍开放）+ Scope（Domain/IP/App/API/Repo）+ Allowed Actions + Prohibited Actions
无法确认 → 不得执行主动攻击动作

## 漏洞验证等级（从低到高，禁止跳级）
| 等级 | 方式 | 自动执行 |
|:---|:---|:---|
| L0 | 静态分析（Code Review/SAST/依赖分析/调用图/数据流）| ✅ 默认 |
| L1 | 本地单元测试（Mock/Fixture/Synthetic Data）| ✅ 默认 |
| L2 | Docker/VM 靶场复现（Sandbox/Disposable VM/Local Replica）| ✅ 默认 |
| L3 | 授权测试环境 | ⚠️ 仅明确授权 |
| L4 | 真实生产环境 | ❌ 默认禁止，必须人工批准 |

## Codex 工具调用限制
- ALLOW：read_file / search_code / grep / static_analysis / compile / unit_test / dependency_scan / create_test / generate_patch / generate_report
- APPROVAL REQUIRED：network_request / browser / scanner / exploit_test / authentication_test / privilege_test / package_install / external_api
- DENY BY DEFAULT：credential_dump / password_collection / token_collection / persistence / lateral_movement / destructive_command / unrestricted_scan / arbitrary_external_target / defense_evasion

## 网络策略
NETWORK_POLICY=DENY_BY_DEFAULT · ALLOWLIST_ONLY=true
Agent 不得自行添加域名/IP/修改 DNS/更改代理/切换出口节点；新增目标必须人工批准

## 密钥策略
禁止读取：浏览器密码 / 系统密码库 / SSH Agent / 用户主目录凭证 / 云平台长期密钥 / 浏览器 Cookie / 生产 Token
测试仅用 TEST_CREDENTIAL_ONLY=true（Temporary/Scoped/Revocable/Non-production）；任务结束 Revoke/Rotate/Destroy

## Agent 自主循环限制
MAX_STEPS=12，达到即 STOP，不得无限重试
禁止自主发生：Scan → Find → Exploit → Escalate → Pivot

## ⚠️ OpenAI 供应商红线（2026-09-04 警告信后新增，**当日已申诉澄清**）

**背景**：sora 收到 OpenAI 官方警告信，Codex 使用被标记「Network Abuse」——Codex 沙箱的高频自动化网络活动（npm/pip install、git、外部 API 调用）被自动检测系统判定为违规模式，再犯将停用服务访问。
**✅ 申诉结果（2026-09-04 当日）**：官方确认是**误报/错报警告**，账号无处罚。
**✅ 已全面恢复（2026-09-04）**：`web_search` 已恢复 `live`，下方「Codex 使用铁律」的临时限制（降频/禁敏感词/依赖离线/墨题不走 Codex）**全部解除**，Codex 正常编码任务恢复使用。本段保留作为事件记录，日常执行以「核心原则 / Policy Gate」常态基线为准。

### Codex 使用铁律
1. **Codex 只跑纯本地代码任务**：读文件/改代码/本地测试/本地构建（L0-L1）
2. **禁止在 Codex 任务里触发网络活动**：npm/pip install、git fetch/push、外部 API、浏览器、抓取、扫描——分流传本地或其他工具
3. **任务包禁敏感词**：不出现「扫描/抓取/绕过/爬虫/侦察/自动化」等字样
4. **降频**：不连续批量跑，每单间隔 5-10 分钟；涉及依赖安装的先本地装好再派活
5. **墨题项目默认本地执行**（2026-09-04 决策）：不再走 Codex
6. **申诉模板**：说明仅做本地开发、常规依赖安装被误判，请求复核

### 操作细则（2026-09-04 sora 精确化补充）
- **网络安全工作只针对**：本地、靶场、staging 或明确授权目标；不碰真实第三方系统
- **任务包功能描述禁区**：不写「自动挖洞/批量扫描/凭据抓取/绕过检测/隐藏运行」——即使任务内容是防御性的，描述也保持中性
- **高风险任务模式**：只读沙箱 + 逐步人工审批（read-only / on-request 限制性配置，与 Codex 官方文档建议一致）
- **依赖策略**：提前锁定版本并尽量离线缓存；减少每个任务临时安装、访问陌生外部服务
- **网络出口**：尽量使用稳定可信出口，避免代理 IP 频繁跳变——这只是降低误报的运营措施，不代表 FlClash 已被确认为原因
- **申诉事实纪律**：不把未验证的「代理 IP 被封」写成申诉事实；若支持团队询问，作为待核实假设说明

### 官方文档对照实证（2026-09-04 子代理审查 + 本机 config 核验）

**Codex 官方文档关键原文（github.com/openai/codex sandbox.md）**：
- *"In workspace-write, network is disabled by default unless enabled in config (`[sandbox_workspace_write].network_access = true`)"*
- 官方推荐安全组合：`--sandbox read-only --ask-for-approval on-request`（安全只读浏览）/ `--sandbox read-only --ask-for-approval never`（CI 只读）/ `--sandbox workspace-write --ask-for-approval on-request`（改代码但高风险动作需批准）
- **避免 `danger-full-access` / `--yolo`**：完全绕过沙箱和审批（官方不建议）
- Windows 沙箱为 **experimental**：AppContainer 限制，world-writable 目录挡不住写

**本机 `~/.codex/config.toml` 实证（9/4 核验）**：
- `sandbox_workspace_write.network_access = False` ✅ 网络默认已关（沙箱内禁止联网）
- `approval_policy = on-request` + `approvals_reviewer = auto_review` ✅ 高风险动作走审查
- `web_search = disabled` ⚠️（2026-09-04 已关闭——**注意合法值只有 disabled/cached/indexed/live，写 `off` 会导致 config_load 失败**，ChatGPT 桌面端直接卡启动）
- `windows.sandbox = elevated` ⚠️ Windows 沙箱本身是 experimental

**结论**：之前用 `codex exec --sandbox workspace-write` 跑的任务，沙箱内网络已被禁；真正的联网通道是 `web_search = live` + 任务文本触发的搜索行为。这解释了「网络滥用」警告的来源之一。

### 推荐配置（官方原文 + 本机适配）
```toml
# ~/.codex/config.toml（观察期建议）
approval_policy = "on-request"        # 高风险动作人工批准（已符合）
approvals_reviewer = "auto_review"    # 自动审查（已符合）
sandbox_mode = "read-only"            # 观察期：只读为主；需改代码时临时切 workspace-write
web_search = "disabled"               # 关闭显式联网通道（观察期；合法值 disabled/cached/indexed/live，无 off）
[sandbox_workspace_write]
network_access = false                # 保持网络关闭（已符合）
```
> 注意：`--sandbox read-only` 与 `--ask-for-approval never` 组合 = 官方推荐 CI 只读模式，适合代码审查类任务。

### 替代执行路径
| 任务类型 | 替代方案 |
|:---|:---|
| 墨题前端/后端改动 | k 本地直接改（patch/write_file + npm build + pytest）|
| 需要装依赖的任务 | 本地终端先装好再决定 |
| 抓取/网络类任务 | 本地脚本 + Hermes 内置工具 |
| 调研/数据任务 | WorkBuddy / dsh |

## k 的落地执行承诺
1. 每次派活 Codex 前先过 Policy Gate 三分类，输出分类结果
2. 涉安全/授权边界任务默认 REVIEW_REQUIRED，等 sora 明确批准再下发
3. 派活包内嵌授权边界段（scope/禁止项/验证等级上限）
4. 挖洞产出只用于授权目标，不进公开仓库，报告人工核验

---
> 🗺️ 属于 [[MOC-Security]] · [[Home|🏠 Home]]
