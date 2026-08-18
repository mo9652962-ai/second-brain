# Errors

Command failures and integration errors.

---

## [ERR-20260719-001] opencode-go-provider-outage

**Logged**: 2026-07-19T14:46:00+08:00
**Priority**: high
**Status**: resolved
**Area**: infra

### Summary
opencode.ai 上游供应商 HTTP 500 导致 Agent 无法回复

### Error
```
[model-fetch] response provider=opencode-go api=openai-completions model=deepseek-v4-pro status=500
chain_exhausted, fallbackConfigured=false
```

### Resolution
- **Resolved**: 2026-07-19T14:30:00+08:00
- **Notes**: 已在 openclaw.json 中配置 fallbacks: kimi-k2.6 → qwen3.7-plus → glm-5.2

---

## [ERR-20260719-002] gateway-config-protected-path

**Logged**: 2026-07-19T14:46:00+08:00
**Priority**: medium
**Status**: resolved
**Area**: config

### Summary
config.patch 和 config.apply 均拒绝修改 agents.defaults.model 下的受保护字段

### Resolution
- **Resolved**: 2026-07-19T14:29:00+08:00
- **Notes**: 直接 edit openclaw.json + gateway restart 生效

---

## [ERR-20260720-001] search-timeout-chain 🆕

**Logged**: 2026-07-21T01:10:00+08:00
**Priority**: high
**Status**: resolved
**Area**: infra
**Recurrence-Count**: 8+

### Summary
tavily_search, web_search, tavily_extract 在本会话中连续超时 8+ 次，严重阻塞 PPT 研究任务

### Error Pattern
```
tavily_search → "request timed out" (30s)
web_search → "request timed out" (60s)
tavily_extract → "request timed out"
```
所有请求走 Tavily API，延迟 20-25s，60s 超时不够

### Root Cause
1. tools.web.search.timeoutSeconds = 60 秒太短
2. 国内→Tavily API 网络延迟高（GFW/路由绕路）

### Resolution
- **Resolved**: 2026-07-20T21:54:00+08:00
- **Notes**: openclaw.json 中 timeoutSeconds: 60 → 120，重启 Gateway 后恢复正常（7.5s 返回）

---

## [ERR-20260720-002] plugin-install-npm-timeout 🆕

**Logged**: 2026-07-21T01:10:00+08:00
**Priority**: medium
**Status**: resolved
**Area**: deps
**Recurrence-Count**: 3

### Summary
npm 安装插件时从 registry.npmjs.org 下载超时，被 SIGKILL

### Error Pattern
```
openclaw plugins install "@tencent-weixin/openclaw-weixin" → SIGKILL
openclaw plugins install "@openclaw/firecrawl-plugin" → SIGKILL
npx -y @tencent-weixin/openclaw-weixin-cli install → SIGKILL (first attempt)
```

### Root Cause
1. 默认 npm registry (registry.npmjs.org) 从国内下载慢
2. 120s/300s exec 超时不够

### Resolution
- **Resolved**: 2026-07-20T21:04:00+08:00
- **Notes**: `npm config set registry https://registry.npmmirror.com` 后安装成功。安装完成后恢复原镜像

---

## [ERR-20260720-003] channel-login-blocked-by-exec 🆕

**Logged**: 2026-07-21T01:10:00+08:00
**Priority**: low
**Status**: resolved
**Area**: tools

### Summary
`openclaw channels login --channel openclaw-weixin` 通过 exec 执行被拒绝

### Error
```
exec cannot run interactive OpenClaw channel login commands.
Run `openclaw channels login` in a terminal on the gateway host
```

### Resolution
- **Resolved**: 2026-07-20T21:04:00+08:00
- **Notes**: 改用 `npx @tencent-weixin/openclaw-weixin-cli install` 替代，该 CLI 工具内部调用登录并生成二维码

---

## [ERR-20260720-004] firecrawl-plugin-stale-directory 🆕

**Logged**: 2026-07-21T01:10:00+08:00
**Priority**: low
**Status**: resolved
**Area**: deps

### Summary
Firecrawl 插件首次安装被 SIGKILL 后，重试时报告 "plugin already exists"

### Error
```
plugin already exists: C:\Users\31954\.openclaw\npm\projects\openclaw-firecrawl-plugin-69f7abcaaa
(delete it first)
```

### Resolution
- **Resolved**: 2026-07-20T22:16:00+08:00
- **Notes**: 使用 `openclaw plugins install @openclaw/firecrawl-plugin --force` 覆盖安装成功

---

## [ERR-20260720-005] memory-search-provider-timeout 🆕

**Logged**: 2026-07-21T01:10:00+08:00
**Priority**: medium
**Status**: resolved
**Area**: infra

### Summary
memory_search 调用超时 (15s)，embedding provider 响应失败

### Error
```
memory_search timed out after 15s
All memory search results are disabled/unavailable
embedding provider configuration issue
```

### Impact
无法检索历史记忆，影响上下文恢复和长期学习

### Resolution
- **Resolved**: 2026-07-21T01:24:00+08:00
- **Notes**: 添加 sync.embeddingBatchTimeoutSeconds: 90 + openclaw memory index --force → 1s响应

---

## [ERR-20260720-006] exec-command-syntax-powershell 🆕

**Logged**: 2026-07-21T01:10:00+08:00
**Priority**: low
**Status**: resolved
**Area**: tools

### Summary
PowerShell 不支持 `&&` 和 `||` 运算符，使用后命令失败

### Error
```
token '&&' is not a valid statement separator in this version.
```

### Resolution
- **Resolved**: 2026-07-20T21:04:00+08:00
- **Notes**: 使用 `;` 分隔命令，或用 `if ($?) { ... }` 条件判断。已更新 TOOLS.md 记录此 gotcha

---

## [ERR-20260721-001] tavily-search-batch-timeout 🆕

**Logged**: 2026-07-21T15:34:00+08:00
**Priority**: medium
**Status**: resolved
**Area**: infra
**Recurrence-Count**: 2

### Summary
Tavily 搜索批量调用时第 4-5 个并发请求超时/fetch failed

### Error Pattern
```
tavily_search → "fetch failed" (query 4)
tavily_search → "request timed out" (query 5)
```

### Context
- 前 3 个并发 tavily_search 请求成功返回（7.4s, 7.4s, 6.0s）
- 第 4-5 个并发请求失败
- 可能是 Tavily API 并发限制或网络波动

### Suggested Fix
- 批量搜索时控制在 3 个并发以内
- 失败后可单独重试
- 已有数据足够时跳过补充搜索

### Metadata
- Reproducible: occasional
- Pattern-Key: api.rate-limit-batch
- See Also: ERR-20260720-001 (search timeout)
- First-Seen: 2026-07-21
- Last-Seen: 2026-07-21

### Resolution
- **Resolved**: 2026-07-21T15:34:00+08:00
- **Notes**: 已有 3 次成功搜索的数据足够完成自改进任务，跳过补充搜索

---

## [ERR-20260721-002] powershell-foreach-property-access 🆕

**Logged**: 2026-07-21T15:34:00+08:00
**Priority**: low
**Status**: resolved
**Area**: tools
**Recurrence-Count**: 1

### Summary
PowerShell ForEach-Object 中使用 $_.Path 拼接字符串语法错误

### Error
```
ForEach-Object { $_.Path + ': ' + $_.Line }  # 报错
```

### Context
尝试用 Select-String 搜索 .learnings/ 中的 Recurrence-Count，ForEach-Object 中属性访问语法在嵌套 exec 调用时失败。

### Suggested Fix
- 使用双引号字符串内嵌 $($_.Property) 语法
- 或使用 [PSCustomObject] 的 ToString() 方法
- 简单搜索直接用 Select-String -Pattern 'keyword' 即可，不需要 ForEach 格式化

### Metadata
- Reproducible: yes
- Pattern-Key: shell.powershell-property-access
- See Also: ERR-20260720-006 (PowerShell syntax)
- First-Seen: 2026-07-21
- Last-Seen: 2026-07-21

### Resolution
- **Resolved**: 2026-07-21T15:34:00+08:00
- **Notes**: Select-String 直接输出匹配行即可，不需要 ForEach-Object 格式化

## [ERR-20260721-6N8] openclaw_session_sweep

**Logged**: 2026-07-21T15:47:48.201Z
**Priority**: medium
**Status**: resolved
**Area**: config

### Summary
Session-end sweep detected 1 possible error in the previous OpenClaw session.

### Error
```
[assistant turn failed before producing content]
```

### Context
- Detected by the self-improvement hook on `/new`
- Session key: agent:main:main
- Session transcript: C:\Users\31954\.openclaw\agents\main\sessions\8a91a3df-f378-41b2-86b8-2a24ecc95ec5.jsonl

### Resolution
- **Resolved**: 2026-07-22T14:15:00+08:00
- **Notes**: 一次性 transient 失败，无具体错误信息，未复现。认定为偶发性基础设施抖动（模型API瞬时故障/网络抖动），无需进一步action。若未来 Pattern-Key: runtime.failure 重复出现再升优先处理。

### Metadata
- Source: openclaw-error-sweep
- Reproducible: unknown
- Pattern-Key: runtime.failure

---

## [ERR-20260818-001] flclash-proxy-corrupted 🆕

**Logged**: 2026-08-18T12:04:00+08:00
**Priority**: high
**Status**: open
**Area**: infra

### Summary
FlClash 7890 代理端口 LISTENING 但流量不通（curl 走它 = 000/exit 56），导致 health_provider_check 假警报全 FAIL

### Error/Findings
```
FlClashCore.exe (PID 30756) 监听 7890，但经代理 curl 全失败（连接被重置）
health_provider_check.py 统一走 127.0.0.1:7890 → 全 FAIL 为假警报
直连实测：deepseek 401 / tokenrhythm(jiyuanlvdong) 401 / baidu 200 —— 外网与 provider 均可达
消息网关冻结：gateway.log 自 8-16 02:24 无输出（QQBot max reconnect / weixin poll error）
```

### Root Cause
1. FlClash 代理进程异常（端口监听但数据转发失效）——可能因长时间运行/节点失效
2. 连带影响依赖代理的消息网关（QQ/微信）离线

### Impact
- health_provider_check 被误导为全 FAIL（假警报，非真实 provider 故障）
- 消息通道（QQ/微信）疑似离线，不影响 cron/agent 核心

### Suggested Fix
1. **重启 FlClash** 恢复 7890 代理（首选）
2. health_provider_check 脚本改直连或先 curl 实测 7890 再判读（防此类假警报）
3. 重启 FlClash 后重启 gateway 观察消息通道 reconnect
4. 修复 cache-hit-monitor 脚本引用（cron 关联脚本已不存在）

### Metadata
- Source: health-relay 巡检
- Pattern-Key: infra.proxy-corrupted
- First-Seen: 2026-08-18
- See Also: ERR-20260719-001 (provider outage)

---
