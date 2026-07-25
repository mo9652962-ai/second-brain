---
tags: [hermes, llm, providers, model, fallback, search, opencode-go, openrouter]
domain: llm-config
cross-domain: [hermes-agent, hermes-model-fallback, hermes-search-config, infrastructure]
related: ["skills/hermes-model-fallback", "skills/hermes-search-config", "skills/hermes-agent"]
created: 2026-07-23
updated: 2026-07-23
---

# Hermes LLM & Search Provider 配置

> 当前 Hermes Agent 运行配置：模型容灾链 + 5 搜索引擎多后端

---

## 📊 当前配置总览

| 项目 | 当前值 |
|------|--------|
| **Agent 框架** | Hermes Agent（Nous Research） |
| **主模型提供商** | opencode-go（OpenCode Go 网关） |
| **主力模型** | `deepseek-v4-flash`（$1/Mtok 输出） |
| **升级模型** | `deepseek-v4-pro`（$0.435/$0.87 per MTok） |
| **容灾链路** | 4 级 OpenRouter 容灾 |
| **搜索引擎** | Tavily + Exa + Firecrawl + DDGS + SearXNG（5 路自动切换） |
| **记忆系统** | Obsidian Vault（笔记型持久记忆） |
| **技能系统** | 70+ Skills |
| **调度系统** | Hermes Cron（定时任务自动化） |

---

## 🎯 模型配置

### 主力模型

| 属性 | 值 |
|------|-----|
| **模型** | `deepseek-v4-flash` |
| **提供商** | `opencode-go` |
| **上下文窗口** | 1,000,000 tokens |
| **输出价格** | ~$1/百万 tokens（Flash 版本，极具性价比） |
| **定位** | 日常对话、编码、研究的主流模型 |
| **API 地址** | `https://opencode.ai/zen/go/v1`（通过 OpenCode Go 网关） |

### 升级模型（同供应商）

| 属性 | 值 |
|------|-----|
| **模型** | `deepseek-v4-pro` |
| **提供商** | `opencode-go` |
| **上下文窗口** | 1,000,000 tokens |
| **输出价格** | $0.87/百万 tokens |
| **定位** | 复杂推理、高难度代码、深度分析时自动升级 |
| **触发条件** | 当 v4-flash 失败时自动升级到此模型 |

### 容灾链（跨供应商 — OpenRouter）

| 优先级 | 提供商 | 模型 | 上下文窗口 | 特点 |
|--------|--------|------|-----------|------|
| ③ | `openrouter` | `moonshotai/kimi-k2.6` | 128K | 中文语感极佳，长文理解 |
| ④ | `openrouter` | `qwen/qwen3.7-plus` | **1,000,000** | 超长上下文，代码能力强 |
| ⑤ | `openrouter` | `z-ai/glm-5.2` | **1,000,000** | 最后防线，中文推理可靠 |

### 容灾链逻辑

```text
┌─ 主力 ─────────────────────────────────┐
│  opencode-go / deepseek-v4-flash        │ ← 日常使用（$1/Mtok）
└──────────┬─────────────────────────────┘
           │ 限流 / 超时 / 服务不可用
           ▼
┌─ 同供应商升级 ─────────────────────────┐
│  opencode-go / deepseek-v4-pro          │ ← 更强能力，同 Key
└──────────┬─────────────────────────────┘
           │ 故障
           ▼
┌─ 跨供应商容灾 (OpenRouter) ────────────┐
│  openrouter / kimi-k2.6                 │ ← 中文语感好
│  openrouter / qwen3.7-plus             │ ← 1M 上下文
│  openrouter / glm-5.2                  │ ← 1M 上下文，最终防线
└────────────────────────────────────────┘
```

**设计原则**：
1. **同供应商升级优先** — 相同的认证凭据，延迟最低
2. **跨供应商容灾** — 消除单点故障
3. **OpenRouter 统管** — 所有容灾模型通过 OpenRouter 接入，单一 API Key 管理

---

## 📝 Hermes Config 配置

### 模型配置

```yaml
# ~/.hermes/config.yaml 顶部
fallback_model:
  - provider: opencode-go
    model: deepseek-v4-flash
    base_url: https://opencode.ai/zen/go/v1
  - provider: opencode-go
    model: deepseek-v4-pro
    base_url: https://opencode.ai/zen/go/v1
  - provider: openrouter
    model: moonshotai/kimi-k2.6
  - provider: openrouter
    model: qwen/qwen3.7-plus
  - provider: openrouter
    model: z-ai/glm-5.2

# 默认模型设置
model:
  default: opencode-go/deepseek-v4-flash
  provider: opencode-go
  context_length: 1000000
```

### 环境变量（`~/.hermes/.env`）

```bash
# === 模型提供商 ===
OPENCODE_GO_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxx
OPENROUTER_API_KEY=sk-or-v1-xxxxxxxxxxxxxxxxxxxxx

# === 搜索引擎 ===
TAVILY_API_KEY=tvly-xxxxxxxxxxxxxxxxxxxxx
EXA_API_KEY=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
FIRECRAWL_API_KEY=fc-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
SEARXNG_URL=http://127.0.0.1:8888
# DDGS（DuckDuckGo）无需 API Key — 只需 pip install ddgs
```

### 配置验证

```bash
# 检查 fallback 链是否有效
python -c "
import yaml
c = yaml.safe_load(open(r'C:\Users\31954\AppData\Local\hermes\config.yaml'))
fb = c.get('fallback_model', [])
print(f'{len(fb)} fallback 条目:')
for f in fb:
    print(f'  {f[\"provider\"]:15s} {f[\"model\"]}')
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

Hermes 按此顺序检测可用后端：

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
  -H "x-api-key: $EXA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query":"test","numResults":1}'

# 测试 Tavily
curl -X POST https://api.tavily.com/search \
  -H "Authorization: Bearer $TAVILY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query":"test","max_results":1}'
```

---

## ⚡ 性能与可靠性指标

| 指标 | 配置前（单供应商） | 配置后（多供应商+多搜索） |
|------|------------------|------------------------|
| **模型可用性** | 1 个提供商 | 2+ 提供商（opencode-go + OpenRouter） |
| **模型选择** | 1 个模型 | 5 个模型（自动容灾链） |
| **搜索引擎** | 1 个后端 | 5 个后端（自动切换） |
| **供应商容灾** | 单点故障 | 跨供应商故障转移 |
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

---

## 🔗 知识关联

- **[[hermes-model-fallback]]**（skills/） — 模型容灾链配置详情
- **[[hermes-search-config]]**（skills/） — 搜索引擎多后端配置详情
- **[[hermes-agent]]**（skills/） — Hermes Agent 完整参考
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
---
> 关联: [[AI-Agent]] · [[Cross-Domain]] · [[Cross-Domain|🔀 知识地图]] | [[HOME|🏠 首页]]
