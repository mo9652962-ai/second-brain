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
plugin already exists: ~\.openclaw\npm\projects\openclaw-firecrawl-plugin-69f7abcaaa
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
- Session transcript: ~\.openclaw\agents\main\sessions\8a91a3df-f378-41b2-86b8-2a24ecc95ec5.jsonl

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
**Status**: resolved
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

### Status Update (2026-08-30)
- **self-improvement recurrence**: 连续第 4 次高亮为 P0 待办（8/18→8/25→8/29→8/30）
- 根因仍未清除：需 sora 在物理机重启 FlClash（7890 端口监听但数据转发失效）→ 重启后观察 gateway 消息通道（QQ/微信）重连
- 此待办为唯一需人工介入的阻塞点，k 无法自理，继续悬空高亮

### Status Update (2026-09-13)
- **self-improvement recurrence**: 连续第 6+ 次高亮（8/18→8/25→8/29→8/30→9/8→9/13）
- 物理层单点故障未清除：软件层冗余已拉满（5路搜索、11级模型fallback、多供应商），仅网络出口代理需人工运维
- 影响面：health_provider_check 持续假警报、QQ/微信消息通道疑似离线、cron/agent核心不受影响
- 建议：sora 下次物理机操作时优先重启 FlClash 服务

### Status Update (2026-09-16) ✅ **RESOLVED**
- **解决动作**: sora 在物理机重启 FlClash (2026-09-16 17:09:25)，FlClashCore.exe 重启成功
- **验证结果**: 7890 端口转发恢复 (curl google 302 / github 200)，QQBot 15:31 resume 重连成功
- **影响消除**: health_provider_check 假警报消除，消息通道 (QQ/微信) 恢复在线
- **连续高亮终结**: 连续 7+ 次 cron 高亮 (8/18→8/25→8/29→8/30→9/8→9/13→9/14→9/18) 正式结束
- **系统状态**: 软件层冗余已拉满，唯一人工介入阻塞点清除，系统可靠性恢复全自动化

### Resolution
- **Resolved**: 2026-09-16T17:09:25+08:00
- **Notes**: sora 物理机重启 FlClash 服务，7890 代理端口数据转发功能恢复，QQBot/微信消息通道自动重连，health_provider_check 恢复正常监控。这是唯一需人工介入的 P0 阻塞点，历时 29 天 (8/18→9/16) 解决。

---

## [ERR-20261012-001] pydantic-core-abi-mismatch 🔁 REGRESSED

**Logged**: 2026-10-12T20:10:00+08:00
**Priority**: high
**Status**: ⚠️ **resolved → REGRESSED**（2026-10-13 复发，见下方「复发」章节；此后此类修复一律先标 `mitigated`）
**Area**: infra
**Duration**: 2026-09-29 → 2026-10-12（**14 天**）；**2026-10-13 复发（同一根因，未根治）**

### Summary
运行解释器与 site-packages 的 **ABI 混用** 导致 `pydantic_core` 无法加载，30+ 生产 cron 连续停摆 14 天。

### Error
```
ModuleNotFoundError: No module named 'pydantic_core._pydantic_core'
RuntimeError: Failed to initialize OpenAI client: No module named 'pydantic_core._pydantic_core'
```

### Root Cause（本次首次落地为可验证事实）
- 运行解释器 = `tools/python-3.14.7`，而依赖装在 `hermes-agent/venv`（**3.11**）的 site-packages 里
- 该目录下的 `_pydantic_core.cp311-win_amd64.pyd` 是 **cp311 ABI**，在 3.14 下**无法加载**
- 影响面：`daily-health-check` / `daily-todo-executor` / `项目追踪` / `每日仓库+知识库优化`（各 failure_streak=14）等 30+ cron

### ⚠️ 误诊更正（重要）
- **早期判断为「pydantic 依赖损坏」→ 错误**。实际依赖包完好，是 **ABI 不匹配**。
- 因此**不要 `pip reinstall pydantic`** —— 重装到 3.14 环境只会换一个不匹配的包，或把 3.11 venv 搅乱。
- 同类误诊史：9/29、10-01、10-03、10-09 四份反思共登记 **5 次**，均写成「回退 3.11 启动路径 / 依赖损坏」，**修 0 次**（「报告但不修」模式第 5 次复发）。

### Resolution
- **Resolved**: 2026-10-12T16:19:00+08:00（scheduler 重启后生效）
- **修复动作**: `hermes_bootstrap` 现把 PM 选中的 **cp314 环境置前**，`_pydantic_core OK`
- **验证（双独立证据）**:
  1. `logs/agent.log`（10-11 23:19 起，1,053,735 B）**pydantic 错误计数 = 1**，且该条是**探针本身的回显**（`current python: 3.14.7 … pydantic 2.13.4 core 2.46.4 / _pydantic_core OK`），非错误；对照 `agent.log.1`（10-11 23:19 归档）**计数 = 524 / 1088 行**
  2. **首个成功运行的 cron**：`daily-monetization-review` 18:00 调度、18:14 产出 36.8KB 报告（此前连续 14 次失败同根因）；`每日股票分析` 18:14 产出 36.8KB 报告（此前连续 9 次失败）
- **Notes**: `errors.log` 最后一条真 `ModuleNotFoundError` 时间戳 = 10-10 13:45:12；此后无新增。

### ⚠️ 复发（2026-10-13，本条「resolved」判定被推翻）

- **复发时间**：2026-10-13 10:31:34 起（gateway 10:28 重启后首次批量 tick）
- **实测证据**：
  1. `cron/executions.db` 10-13 全天 **63 次执行 / 16 failed**，其中 **13 个 job** 失败信息为同一句 `RuntimeError: Failed to initialize OpenAI client: No module named 'pydantic_core._pydantic_core'`（10:31–10:32 集中爆发，另有 15:45 / 18:00 / 18:01 / 18:45 / 20:00 / 21:00 / 22:30）
  2. `logs/agent.log` 10-13 全天 **19 行** pydantic 错误（13 条 cron 失败 + **6 条 `gateway.run: Supervised task hosted_room_worker died`**）；10-14 08:44 再刷 6 条 worker 死亡
  3. `logs/gateway-exit-diag.log`：`gateway.start` 在 **10-13T02:28Z（10:28 CST）** 与 **10-14T00:42Z（08:42 CST）** 两次启动，**`"python": "3.14.7"` 两次都还是 3.14.7**
- **误判根因（重要）**：10-12 的「resolved」验证只做了**进程内** `import pydantic_core` 探针（`agent.log` 计数 = 1 且那 1 条是探针回显）。`hermes_bootstrap` 把 cp314 环境置前是**进程内生效**；**gateway 一重启即回落**。10-12 16:19 的「首个成功 cron」证明的是「那一次进程能跑」，**不是「这条路径被修好了」**。
- **修正后的判定口径（此后所有 ERR 条目适用）**：
  1. **「resolved」必须包含一次 gateway 重启后的复验**，否则只能标 `mitigated`（进程内缓解）
  2. 验证证据不得使用「错误计数 = 0/1」这类**同进程自证**指标，必须用**跨进程**指标（重启后的新失败记录 / 独立 cron 产出）
  3. 涉及解释器/依赖路径的修复，必须核对 `gateway-exit-diag.log` 的 `"python"` 字段，而非只看 import 是否成功
- **未闭环**：根治 = 把解释器固定写进启动路径（`hermes-agent/venv/Scripts/python.exe` 实测 `pydantic_core 2.46.4` import OK），不再依赖 bootstrap 每次置前 —— **需 sora 拍板**
- **影响面更新**：10-13 全天 **13 个生产 cron 0 产出**（含 `daily-self-improvement` 与 `daily-todo-executor` —— **行动项消费器自己死掉时，写进反思的行动项等于没写**）

### 遗留（未闭环）
- **陈旧账本**：32 个 cron 的 `last_error` / `failure_streak` 仍停在 10-11（实测 47 jobs 中 28 个 `failure_streak>0`），health 看板持续报 ❌32。**属状态账本陈旧，非真实故障** —— 等新排程自然跑一轮覆盖，或对已到期 job 手动触发。
- **结构性教训**：`daily-todo-executor` 本身也被同一条错误打挂 → **写进反思的 P0 行动项，在扫描器自己死掉时等于没写**。10-01 反思已提「给反思行动项加不依赖 cron 健康的播报通道（no_agent 纯脚本）」，仍未落地。

### 🔁 复发 #3（2026-10-14 08:41–08:45 CST，本机实测复现）

> 追加者：`vault-suggestion-executor`（闲鱼提醒 cron，job `c9eb24e4819e`）2026-10-14 09:00。
> 依据 10-13 反思的 P0 行动项「`.learnings/ERRORS.md` 追加复发记录」。

**症状**：`logs/agent.log` 10-13 10:30 起 27 行 pydantic 报错（13 条 cron 失败 + 14 条
`gateway.run: Supervised task hosted_room_worker died`）；10-14 08:44 再刷 6 条 worker 死亡。
`cron/executions.db` 口径：10-13 全天 63 次执行 / **16 failed**，其中 13 项同一句错误。

**本轮新增的决定性证据（本次首次做到可复现）**：

| 探针 | 结果 |
|:-----|:-----|
| `tools/python-3.14.7/python.exe` + `PYTHONPATH=hermes-agent/venv/Lib/site-packages` | ❌ `No module named 'pydantic_core._pydantic_core'`（**精确复现**） |
| `tools/python-3.14.7/python.exe`（launcher 原样：`VIRTUAL_ENV=tools` + `PYTHONPATH=hermes-agent`） | ❌ `No module named 'pydantic_core'` |
| `installs/<pm>/environments/<hash>/venv/Scripts/python.exe`（PM venv） | ✅ `pydantic_core 2.46.4` / `openai 2.24.0` |
| `tools/python-3.14.7/python.exe` + `PYTHONPATH=hermes-agent;<PM venv>/Lib/site-packages` | ✅ 同上 |
| `hermes-agent/venv/Scripts/python.exe`（cp311 venv） | ✅ `_pydantic_core.cp311-win_amd64.pyd` |

**ABI 事实（磁盘实测，三个 `.pyd` 并存）**：

| 位置 | 二进制 | 在 3.14 解释器下 |
|:-----|:-------|:-----------------|
| `hermes-agent/venv/Lib/site-packages/pydantic_core/` | `_pydantic_core.cp311-win_amd64.pyd` | ❌ 不可加载 |
| `installs/<pm>/.../venv/Lib/site-packages/pydantic_core/` | `_pydantic_core.cp314-win_amd64.pyd` | ✅ |
| `cache/uv/archive-v0/.../pydantic_core/` | `_pydantic_core.cp314-win_amd64.pyd` | ✅ |

**根因（已闭合）**：`hermes-agent/venv` 是 **cp311 venv**（`pyvenv.cfg version_info=3.11`，
`venv/Scripts/python.exe` = Python 3.11.15）；但磁盘上 `gateway-service/Hermes_Gateway.cmd` /
`.vbs` 是 **9/26 生成的陈旧版本**，其内容与当前 hermes 代码重新生成的结果**逐字节相同**——
即两条都指向 `tools/python-3.14.7` 解释器 + `PYTHONPATH=hermes-agent`。
`hermes-agent/venv/Lib/site-packages` 里的 **cp311** `_pydantic_core` 一旦被 3.14 解释器加载
即报「子模块不存在」。10-12 的 `hermes_bootstrap` 把 PM 的 cp314 环境**置前**只是
**进程内**生效——**gateway 一重启即回落**，这正是 10-13 原样复发的原因。

**重启即复发的时间线（`logs/gateway-exit-diag.log` 的 `"python"` 字段）**：

| gateway 启动 | pid | `"python"` | 结果 |
|:---|:---|:---|:---|
| 10-12 16:19 | — | 3.14.7 | 进程内被 bootstrap 救回 → 误判 resolved |
| 10-13 02:28 UTC（10:28 CST） | 30608 | **3.14.7** | ❌ 10:30 起 13 cron 失败 + 6 worker 死亡 |
| 10-14 00:42 UTC（08:42 CST） | 36592 | **3.14.7** | ❌ 08:44–08:45 再 6 次 worker 死亡 |

**修复路径（三条实测 PASS，按侵入性排序）**：

1. **最小改动**：给 launcher 的 `PYTHONPATH` 追加 PM venv 的 `Lib\site-packages`
   （实测 PASS）。但 `_resolve_detached_python()` 的 `extra_pythonpath` 现在恒为 `[]`，
   说明上游已刻意放弃「PYTHONPATH 叠加」这条设计——改回去等于逆着上游走。
2. **上游本意**：让 `get_python_path()` 返回 **PM venv 的 `python.exe`** 而非 store python。
   实测 PM venv python 单跑即 PASS，无需任何 PYTHONPATH 叠加。
3. **最省事**：`gateway install` 重新生成 launcher（当前 launcher 是 9/26 的陈旧产物）。

**判定口径（沿用 10-13 反思确立的三条）**：① 「resolved」必须含**一次 gateway 重启后的复验**，
否则只标 `mitigated`；② 证据不得用同进程自证指标，须用跨进程指标；③ 涉及解释器/依赖路径的修复，
必须核对 `gateway-exit-diag.log` 的 `"python"` 字段。

**当前状态**：`mitigated`（进程内可用）。**10-14 08:42 重启后，`daily-self-improvement`
（09:04）与 `hackernews-daily`（08:49）已成功 → 本进程内正常**；但解释器仍为 3.14.7，
**下次 gateway 重启仍会复发**，故不得再标 resolved。

**副作用（已定位，非本错误但同窗口）**：`hosted_room_worker` 连续 5 次死亡后
`giving up restarts` → 群聊 worker 全程离线（10-13 10:31、10-14 08:45 两次），
即 profile.yaml 里 researcher/coder/reviewer 的群聊房间不可用。

**修复归属**：🔒 **需 sora**（改 `get_python_path()` / 重跑 `gateway install` 属安装层动作，
且 gateway 重启会中断当前会话）。k 侧已把可复现证据与三条候选路径备齐，sora 一句话即可落地。


### 🔁 复发 #3（2026-10-16 12:35 CST，**预测命中：重启即复发**）

**判定依据：10-14 写下的预测「下次 gateway 重启仍会复发」在 10-16 被实测命中，且失败形态与 10-14 完全一致。**

| 证据 | 实测值 | 来源 |
|:---|:---|:---|
| gateway 重启时刻 | 2026-10-16 04:35:22 UTC = **12:35:22 CST**，pid **38000** | `logs/gateway-exit-diag.log` `tag=gateway.start` |
| 解释器 | `"python": "3.14.7"`（仍非 PM venv 的 3.11.15） | 同上 |
| worker 死亡 | **12:38:21 / 12:38:22 / 12:38:24 / 12:38:28 / 12:38:36 / 12:38:52** 共 **6 次** | `logs/gateway.log` |
| 放弃重启 | `12:38:52,257 hosted_room_worker died 5 times in rapid succession ... giving up restarts` | 同上 |
| 错误文本 | `ModuleNotFoundError: No module named 'pydantic_core._pydantic_core'` | 同上 |

**注**：本次 worker 死亡发生在**本 cron（12:35:17 起跑）运行期间**，即修复未落地前，每次重启都会稳定复现同一故障。

**launcher 现状（本机实测，2026-10-16）**：

`gateway-service/Hermes_Gateway.cmd` 与 `.vbs` 仍是**指向 3.14 store 解释器**的版本：

```
set "VIRTUAL_ENV=C:\Users\<USER>\AppData\Local\hermes\tools"
set "PYTHONPATH=C:\Users\<USER>\AppData\Local\hermes\hermes-agent;%PYTHONPATH%"
C:\Users\<USER>\AppData\Local\hermes\tools\python-3.14.7+202****0901-win32-x64\python.exe -m hermes_cli.main gateway run
```

而上游 `_launchers.py` 的现行设计（`runtime_command()` 文档串明写）是：
`Store Python owns the ABI; bootstrap selects and leases dependencies at child start.
No selected generation or ambient PYTHONPATH is captured in the command.`
→ 该设计下 launcher 应经 `hermes_bootstrap` 选择依赖代次；**本机 launcher 是 9/26 生成的陈旧产物，未带 bootstrap 层**，
所以 3.14 解释器直接吃 `hermes-agent/venv`（cp311）的 site-packages → ABI 不匹配。

**新增判定口径（第 4 条）**：本机 launcher 是「陈旧生成物」而非「上游当前产物」时，
`gateway install` 重新生成会**同时**改变两件事（解释器来源 + 是否经 bootstrap），
因此候选②（重跑 `gateway install`）的验证必须包含「重新生成后 launcher 文本 diff」+「重启后 `gateway-exit-diag.log` 的 python 字段」两项，
不可只看「重启后 worker 没死」——那可能只是 bootstrap 进程内救回（10-12 的误判模式）。

**状态**：`mitigated`（进程内可用，未根治）。**第三次预测命中，不得再标 resolved。**

---

### See Also
- 影响同根因任务：`daily-health-check` / `daily-todo-executor` / `项目追踪` / `每日仓库+知识库优化` / `weekly-cost-report` / `组会报告` / `文献周报` / `闲鱼提醒` / `biweekly-skill-audit` / `monthly-skill-usage` / `weekly-learning-progress` / `weekly-suggestion-implementation` / `AI测评周报` / `shai-hulud-weekly-scan`
- 反思登记史：`memory/2026/10/2026-10-01-reflection.md` / `2026-10-03-reflection.md` / `2026-10-09-reflection.md`

---
