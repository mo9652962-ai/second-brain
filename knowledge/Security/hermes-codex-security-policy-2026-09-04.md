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

## k 的落地执行承诺
1. 每次派活 Codex 前先过 Policy Gate 三分类，输出分类结果
2. 涉安全/授权边界任务默认 REVIEW_REQUIRED，等 sora 明确批准再下发
3. 派活包内嵌授权边界段（scope/禁止项/验证等级上限）
4. 挖洞产出只用于授权目标，不进公开仓库，报告人工核验
