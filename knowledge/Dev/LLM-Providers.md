---
tags: [hermes, llm, providers, model, fallback, search, opencode-go, openrouter, fangzhou]
domain: llm-config
cross-domain: [hermes-agent, hermes-model-fallback, hermes-search-config, infrastructure]
related: ["skills/hermes-model-fallback", "skills/hermes-search-config", "skills/hermes-agent", "skills/fangzhou-ark-setup"]
created: 2026-07-23
updated: 2026-08-06
status: adopted
---

# Hermes LLM & Search Provider 配置

> 当前 Hermes Agent 运行配置：模型容灾链 + 5 搜索引擎多后端
> ⚠️ 2026-08-06 重写：对齐 config.yaml 实况（8/1 双火山容灾落地后默认模型/提供商已变更）

---

## 📊 当前配置总览

| 项目 | 当前值 |
|------|--------|
| **Agent 框架** | Hermes Agent（Nous Research） |
| **默认模型** | `deepseek-v4-pro`（custom:fangzhou-2 火山方舟备用账户） |
| **日常主力** | `deepseek-v4-flash`（custom:fangzhou-2 / 或 opencode-go） |
| **容灾链路** | 8 级（opencode-go ×5 + siliconflow ×2 + deepseek 直连） |
| **搜索引擎** | Tavily + Exa + Firecrawl + DDGS + SearXNG（5 路自动切换） |
| **记忆系统** | Obsidian Vault（笔记型持久记忆） |
| **调度系统** | Hermes Cron（29 个定时任务） |

---

## 🎯 模型配置（2026-08-06 config.yaml 实况）

### 默认模型（config.yaml `model` 段）

```yaml
model:
  default: deepseek-v4-pro
  provider: custom:fangzhou-2     # 双火山容灾：fangzhou-1 429 时切 fangzhou-2
  api_mode: chat_completions
```

> 8/1 双火山账户容灾落地后，默认模型从 `opencode-go/deepseek-v4-flash` 变为 `custom:fangzhou-2/deepseek-v4-pro`（备用火山账户 8/10 槽位）。会话内可用 `/model flash`、`/model pro` 等 alias 快速切换。

### 模型 Aliases（config.yaml `model_aliases` 段）

| Alias | 模型 | Provider |
|-------|------|----------|
| `pro` | deepseek-v4-pro | custom:fangzhou-2 |
| `flash` | deepseek-v4-flash | custom:fangzhou-2 |
| `glm` | glm-5.2 | custom:fangzhou-1 |
| `code` | kimi-k2.7-code | custom:fangzhou-1 |
| `kimi` | kimi-k2.6 | custom:fangzhou-1 |
| `db` | doubao-seed-2.1-turbo | custom:fangzhou-1 |
| `lite` | doubao-seed-2.0-lite | custom:fangzhou-1 |
| `mini` | minimax-m3 | custom:fangzhou-1 |
| `mini2` | minimax-m2.7 | custom:fangzhou-1 |

> ⚠️ 旧文档写 pro/flash=fangzhou-1 已过时——8/1 起 pro/flash 已指向 fangzhou-2（备用账户），其余 alias 在 fangzhou-1。

### 容灾链（fallback_model，8 级）

| 优先级 | 提供商 | 模型 | 特点 |
|--------|--------|------|------|
| ① | opencode-go | deepseek-v4-pro | 同供应商主力 |
| ② | opencode-go | kimi-k3 | 长上下文 |
| ③ | opencode-go | kimi-k2.7-code | 代码场景 |
| ④ | opencode-go | qwen3.7-plus | 1M 上下文 |
| ⑤ | opencode-go | glm-5.2 | 国产 1M 上下文 |
| ⑥ | siliconflow | Qwen/Qwen3.5-4B | 轻量回退 |
| ⑦ | siliconflow | deepseek-ai/DeepSeek-V4-Pro | 硅基流动回退 |
| ⑧ | deepseek 直连 | deepseek-v4-flash | 最后兜底（api.deepseek.com） |

### 容灾链逻辑

```text
┌─ 主力 ─────────────────────────────────┐
│  custom:fangzhou-2 / deepseek-v4-pro    │ ← 默认（8/1 起）
│  opencode-go / deepseek-v4-flash        │ ← 常规会话常用
└──────────┬─────────────────────────────┘
           │ 限流 / 超时 / 服务不可用
           ▼
┌─ 同供应商升级 (opencode-go) ───────────┐
│  deepseek-v4-pro → kimi-k3             │
│  → kimi-k2.7-code → qwen3.7-plus      │
│  → glm-5.2                             │ ← 5 级
└──────────┬─────────────────────────────┘
           │ 故障
           ▼
┌─ 跨供应商容灾 (siliconflow) ──────────┐
│  Qwen3.5-4B → DeepSeek-V4-Pro         │ ← 2 级
└──────────┬─────────────────────────────┘
           │ 故障
           ▼
┌─ 最终防线 (DeepSeek 直连) ───────────┐
│  api.deepseek.com / deepseek-v4-flash  │ ← 兜底
└──────────────────────────────────────┘
```

**设计原则**：
1. **同供应商升级优先** — 前 5 级通过 opencode-go，延迟最低
2. **跨供应商容灾** — siliconflow 2 级 + DeepSeek 直连兜底
3. **双火山备用** — fangzhou-1 429/限额时切 fangzhou-2（`model_aliases.pro/flash`）
4. **认证统一** — opencode-go 用 OPENCODE_GO_API_KEY，siliconflow 用 SILICONFLOW_API_KEY

### 更新记录
- 2026-07-26: 移除 OpenRouter（402），改为 8 级链
- 2026-07-26: opencode-go 补 key_env，修复 cron 401
- 2026-08-03: deepseek 直连模型 deepseek-chat → deepseek-v4-flash（旧别名已退役，fallback 链第 8 项对齐实际 config）
- 2026-08-06: 文档重写对齐 config.yaml 实况（默认模型 → custom:fangzhou-2/deepseek-v4-pro；补充 model_aliases 表）

---

## 📝 Hermes Config 配置

### 模型配置（config.yaml 实况 2026-08-06）

```yaml
# config.yaml 顶部
fallback_model:
  - provider: opencode-go
    base_url: https://opencode.ai/zen/go/v1
    api_mode: chat_completions
    model: deepseek-v4-pro
  - provider: opencode-go
    model: kimi-k3
    base_url: https://opencode.ai/zen/go/v1
  - provider: opencode-go
    model: kimi-k2.7-code
    base_url: https://opencode.ai/zen/go/v1
  - provider: opencode-go
    model: qwen3.7-plus
    base_url: https://opencode.ai/zen/go/v1
  - provider: opencode-go
    model: glm-5.2
    base_url: https://opencode.ai/zen/go/v1
  - provider: siliconflow
    key_env: SILICONFLOW_API_KEY
    model: Qwen/Qwen3.5-4B
  - provider: siliconflow
    key_env: SILICONFLOW_API_KEY
    model: deepseek-ai/DeepSeek-V4-Pro
  - provider: deepseek
    base_url: https://api.deepseek.com
    key_env: DEEPSEEK_API_KEY
    model: deepseek-v4-flash

# 默认模型设置（8/1 双火山容灾后）
model:
  default: deepseek-v4-pro
  provider: custom:fangzhou-2
  api_mode: chat_completions
```

### Custom Providers（2026-08-06 实况 6 个）

| Provider | base_url | api_mode | 定位 |
|----------|----------|----------|------|
| `opencode-go` | https://opencode.ai/zen/go/v1 | chat_completions | 主网关 |
| `siliconflow` | https://api.siliconflow.cn/v1 | chat_completions | 跨供应商容灾 + 多模态/图像模型 |
| `kimi` | https://api.moonshot.cn/v1 | chat_completions | kimi-k2.7-code / kimi-k2.6 |
| `fangzhou-1` | https://ark.cn-beijing.volces.com/api/coding/v3 | chat_completions | 火山主账户（glm/code/kimi/db 等 alias） |
| `fangzhou-2` | https://ark.cn-beijing.volces.com/api/coding/v3 | chat_completions | 火山备用账户（pro/flash 默认） |
| `jiyuanlvdong` | https://tokenrhythm.studio/v1 | chat_completions | 基元律动科技（国产聚合备用） |

> ⚠️ fangzhou 两账户共用 Coding Plan 端点 `/api/coding/v3`，**必须用 `chat_completions`**（`codex_responses` 模式豆包 seed 全 500，详见 fangzhou-ark-setup 技能 §2）。
> ⚠️ 豆包 doubao-seed-2.0-pro **不支持视觉/图片分析**（vision_analyze 报 UnsupportedModel）——需要视觉时切 Gemini/GPT/Claude/GLM-5.2 等多模态模型。

### 环境变量（`~/.hermes/.env`）

```bash
# === 模型提供商 ===
OPENCODE_GO_API_KEY=«redacted:sk-…»
DEEPSEEK_API_KEY=«redacted:sk-…»   # DeepSeek 官方直连（9-12/14-18 点 2 倍价）

# === 搜索引擎 ===
TAVILY_API_KEY=«redacted:tvly-…»
EXA_API_KEY=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
FIRECRAWL_API_KEY=«redacted:fc-…»
SEARXNG_URL=http://127.0.0.1:8888
# DDGS（DuckDuckGo）无需 API Key — 只需 pip install ddgs
```

### 配置验证

```bash
# 检查 fallback 链是否有效
python -c "
import yaml
c = yaml.safe_load(open(r'C:\Users\31954\AppData\Local\hermes\config.yaml', encoding='utf-8'))
fb = c.get('fallback_model', [])
print(f'{len(fb)} fallback 条目:')
for f in fb:
    print(f'  {f[\"provider\"]:15s} {f[\"model\"]}')
"

# 检查 model_aliases
python -c "
import yaml
c = yaml.safe_load(open(r'C:\Users\31954\AppData\Local\hermes\config.yaml', encoding='utf-8'))
print(c.get('model_aliases'))
"

# 重启会话使配置生效
# /reset  或 关闭并重新打开 Hermes
```

---

## 🔍 搜索引擎配置（5 路自动容灾）

Hermes 配置了 5 个搜索后端，自动按优先级切换：

| 优先级 | 后端 | 认证方式 | 查询额度 | 特点 |
|--------|------|---------|---------|------|
| 🥇 | **Tavily** | `TAVILY_API_KEY` | 1000/月免费 | AI 搜索专用，结果结构化 |
| 🥈 | **Exa** | `EXA_API_KEY` | 1000/月免费 | 语义搜索，内容提取 |
| 🥉 | **Firecrawl** | `FIRECRAWL_API_KEY` | 500/月免费 | 网页抓取+Markdown 转换 |
| ④ | **SearXNG** | `SEARXNG_URL`（本地） | 无限制 | 本地部署，聚合多引擎 |
| ⑤ | **DDGS** | 无（`pip install ddgs`） | 无限制 | 兜底方案，无需 API Key |

### 自动检测机制

```text
TAVILY_API_KEY → EXA_API_KEY → FIRECRAWL_API_KEY → SEARXNG_URL → ddgs 包
```

无需手动配置 `web.backend` — 自动选择第一个可用的。

### 后端详细信息

#### Tavily（主要搜索后端）
- **注册**: https://tavily.com
- **API**: REST API，国内可直接访问
- **能力**: AI 优化的搜索结果，包含内容摘要和相关性评分
- **限制**: 免费 1000 次/月

#### Exa（语义搜索引擎）
- **注册**: https://exa.ai
- **API**: REST API
- **能力**: 基于嵌入的语义搜索，自动内容提取
- **限制**: 免费 1000 次/月

#### Firecrawl（网页抓取）
- **注册**: https://firecrawl.dev
- **API**: REST API
- **能力**: 网页转 Markdown，网站爬取，爬虫管理
- **限制**: 免费 500 页/月

#### SearXNG（本地自部署）
- **安装**: `git clone https://github.com/mbaozi/SearXNGforWindows.git`
- **启动**: `./python/python.exe ./python/Lib/site-packages/searx/webapp.py`
- **地址**: `http://127.0.0.1:8888`
- **优点**: 无 API 限制，聚合 Google/Bing/Brave 等引擎
- **国内适配**: 可配置 VPN 代理（`config/settings.yml → outgoing.proxies`）

#### DDGS（DuckDuckGo — 兜底）
- **安装**: `pip install ddgs`
- **无需 API Key**
- **注意**: 国内需 VPN

### 手动固定后端（不推荐）

```bash
hermes config set web.backend tavily    # 固定只用 Tavily
hermes config set web.backend ""        # 恢复自动检测
```

### 搜索后端测试

```python
# 测试 DDGS
python -c "import ddgs; s=ddgs.DDGS(); print(list(s.text('test', max_results=1)))"

# 测试 Exa
curl -X POST https://api.exa.ai/search \
  -H "x-api-key: ***" \
  -H "Content-Type: application/json" \
  -d '{"query":"test","numResults":1}'

# 测试 Tavily
curl -X POST https://api.tavily.com/search \
  -H "Authorization: Bearer ***" \
  -H "Content-Type: application/json" \
  -d '{"query":"test","max_results":1}'
```

---

## ⚡ 性能与可靠性指标

| 指标 | 配置前（单供应商） | 配置后（多供应商+多搜索） |
|------|------------------|------------------------|
| **模型可用性** | 1 个提供商 | 6+ 提供商（opencode-go + siliconflow + deepseek + kimi + 双火山 + 基元律动） |
| **模型选择** | 1 个模型 | 8+ 模型（自动容灾链 + 9 个 alias） |
| **搜索引擎** | 1 个后端 | 5 个后端（自动切换） |
| **供应商容灾** | 单点故障 | 跨供应商故障转移 + 双火山互备 |
| **搜索容灾** | 无 | 5 路冗余 |
| **心跳/简单任务** | 用主力模型（贵） | 可配独立 cron 用 Flash 模型 |

---

## 📋 国内网络适配

| 问题 | 解决方案 |
|------|---------|
| DuckDuckGo 被墙 | 使用 DDGS + VPN；或优先 Tavily/Exa/Firecrawl |
| Tavily 延迟高 | timeoutSeconds 设为 120s |
| SearXNG 需代理 | `./python/Lib/site-packages/searx` 配置 `outgoing.proxies` |
| GitHub Releases 被墙 | GitHub HTTPS clone 不受限 |
| npm 安装超时 | `npm config set registry https://registry.npmmirror.com` |
| 火山 429/配额 | 切 fangzhou-2（备用账户，`model_aliases` 已就绪） |

---

## 🔗 知识关联

- **hermes-model-fallback**（skills/） — 模型容灾链配置详情
- **hermes-search-config**（skills/） — 搜索引擎多后端配置详情
- **hermes-agent**（skills/） — Hermes Agent 完整参考
- **fangzhou-ark-setup**（skills/） — 火山方舟 Coding Plan 配置全指南（api_mode 坑/模型兼容矩阵）
- **[[AI-Workflow]]** — Workflow 编排与 Skill 组合

---

## 📚 参考来源

- Hermes Agent Docs — https://hermes-agent.nousresearch.com/docs/
- OpenRouter Models — https://openrouter.ai/models
- OpenCode Go — https://opencode.ai
- Tavily — https://tavily.com
- Exa — https://exa.ai
- Firecrawl — https://firecrawl.dev
- SearXNGforWindows — https://github.com/mbaozi/SearXNGforWindows
- 火山引擎 ARK 控制台 — https://ark.cn-beijing.volces.com
---
> 关联: [[AI-Agent]] · [[deepseek-v4-flash-0731-upgrade]] · [[Cross-Domain]] · [[Cross-Domain|🔀 知识地图]] | [[HOME|🏠 首页]]
