---
tags: [GitHub, W39, API网关, 订阅分发, 中转站, Go, 变现]
aliases: [Sub2API, sub2api]
date: 2026-09-20
source: https://github.com/Wei-Shaw/sub2api
---

# Sub2API — 订阅配额分发 AI API 网关平台

> 2026-09-20 W39 精选。Go 实现的一站式开源中转：把 Claude/OpenAI/Gemini/Grok/Kimi 等**订阅账号配额**变成标准 API Key 对外分发，内置计费+支付+管理后台。≈ 39.4k★（8,127 forks），曾多次登顶 GitHub Trending（2026-02-28 首次 #1），本月持续热榜。

## 一句话定位

**订阅配额分发平台**：上游是各家 AI 产品的订阅账号（OAuth/API Key），下游是标准 OpenAI 兼容 API Key；平台负责鉴权、计费、负载均衡、请求转发——本质是把「订阅」拆成「按 token 计费」的 API 生意。

## 核心特征 / 技术架构

技术栈：Go + Vue + PostgreSQL + Redis + Docker（全自托管，无云依赖）

| 模块 | 能力 |
|:--|:--|
| 多账号管理 | 上游账号类型：OAuth / API Key；Grok xAI OAuth、OpenAI 订阅、Antigravity、国产供应商（Kimi/智谱 GLM/DeepSeek） |
| API Key 分发 | 平台为用户生成/管理 API Key，支持过期、限流 |
| 精确计费 | **token 级**用量追踪与成本计算；渠道定价（fast_multiplier/flex_multiplier、上下文区间倍率、谷峰分时定价） |
| 智能调度 | 账号选择 + 粘性会话（sticky session），账号级并发控制 |
| 内置支付 | EasyPay 易支付、支付宝官方、微信官方、Stripe——用户自助充值，无需独立支付服务 |
| 管理后台 | Web 界面监控 + 渠道/模型管理 + iframe 嵌入外部系统（工单等） |
| Composite Groups | 管理端路由层：请求的模型 → 解析到具体供应商；支持 Codex 端点（Alpha Search/Live） |
| 协议兼容 | Chat Completions / Anthropic Messages / OpenAI Responses 三协议；国产账号「自适应协议」一个账号同时承接三种协议 |
| 高级特性 | OpenAI Fast mode（service_tier 按实际档位计费）、OpenAI 重置卡按用量阈值自动使用、Kimi 原生 Responses 转发、Claude Fable 5.1 |

姊妹项目：**Wei-Shaw/claude-relay-service**（12.1k★，自建 Claude Code 镜像/中转，同一作者的拼车生态）。

## 创新点详解

1. **订阅→API 的配额经济模型**：官方 API 是「单价×用量」，订阅是「固定月费」。sub2api 把订阅拆成可计费 API，拼车共享摊薄成本——这是「订阅套利」基础设施化，国内中转站赛道（如 OpenRouter 国产替代）的商业引擎。
2. **自适应多协议**：一个上游账号可同时承接 Chat/Anthropic/Responses 三种协议，按目标端点自动路由——解决了「同一密钥不同工具要求不同协议」的兼容地狱。
3. **token 级计费 + 分时倍率**：不止按次计费，支持 fast/flex 倍率、长上下文阶梯、高峰时段倍率——计费颗粒度到渠道×时段×上下文区间，商业定价能力完整。
4. **支付内置**：支付宝/微信/Stripe 直接集成，一个 Docker Compose 起来就是可收款的服务——个人开发者也能运营收费中转站。

## 💎 可借鉴点（对 sora 工作流）

1. **EasyCLIProxyAPI(8317) / WorkBuddy 反代(codebuddy2api) 的商用升级路径**：当前本机网关是「自用免 key」级别；sub2api 展示了自用→商用的完整功能清单（计费/限流/支付/后台/渠道路由）。若闲鱼/私域要卖「AI API 中转」服务，这就是现成范本（Go 全栈，无 Docker 环境下需评估部署方式——本机无虚拟化，但 Go 单二进制可裸跑 + SQLite 替代 PG 是可行降级）。
2. **国产供应商自适应协议**：墨题/刷题机未来接多 provider 时，「一个账号三协议自适应」比维护三套配置省事得多——记入 multi-end-ai-provider-config 的思路补充。
3. **计费模型直接迁移到闲鱼变现**：fast/flex 倍率 + 上下文区间阶梯 + 分时定价，这套定价心理学同样适用于论文/PPT/PCB 接单的弹性报价（ai-freelance-pricing 可吸收「服务层级倍率」概念）。
4. **拼车经济验证**：AI 订阅拼车（Claude Code 镜像、OpenAI 共享）是 2026 年真实需求——sora 已有 codebuddy2api 反代，可评估是否接 sub2api 做多账号配额池。

## 安装 / 验证命令

```bash
# 官方快速起（需 Docker；本机无 Docker 则参考其单二进制 + PG 方案）
git clone https://github.com/Wei-Shaw/sub2api && cd sub2api
docker compose up -d   # 含 postgres/redis/后端/前端
# 验证：访问管理后台 → 添加上游账号（OAuth）→ 生成 API Key → curl 调用
curl http://localhost:8080/v1/chat/completions \
  -H "Authorization: Bearer <平台生成的key>" \
  -d '{"model":"gpt-4o","messages":[{"role":"user","content":"hi"}]}'
```

## 总结评价表

| 维度 | 评价 |
|:--|:--|
| 技术含金量 | ★★★★★ 计费/调度/多协议网关工程量大且成熟 |
| 值得安装 | 🟡 视中转变现需求——本机自用已有 EasyCLIProxyAPI；商用/拼车场景再上 |
| 趋势判断 | 「订阅配额经济」持续升温；国产供应商支持完善，与国内生态贴合 |
| 风险 | LGPL-3.0 注意合规；订阅共享有账号风控风险（封号），商业运营需自担 |

---
> 🗺️ 属于 [[MOC-Dev]] · [[MOC-GitHub]] · 周报 [[../../memory/2026/09/github-trending-w39|W39]]
