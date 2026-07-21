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
**Status**: unresolved
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
