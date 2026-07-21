# 2026 低成本大模型接入方案

> 调研时间：2026-07-21 | 来源：Tavily + SegmentFault + API Dog + 36氪 + 各厂商官网

## 📊 现状分析

| 项目 | 当前 |
|------|------|
| 主力供应商 | opencode-go（聚合代理，一层加价） |
| 主力模型 | deepseek-v4-pro（$0.435/$0.87 per MTok） |
| 备选模型 | kimi-k2.6 / qwen3.7-plus / glm-5.2 / mimo-v2.5-pro |
| 核心风险 | ⚠️ 单供应商故障 = 全部不可用（已验证 2026-07-19） |

## 🎯 推荐方案：增加 2-3 个低成本供应商

### 第一优先：SiliconFlow（硅基流动）⭐

| 项 | 详情 |
|-----|------|
| **定位** | 国内最大的 AI 推理云平台，OpenAI 兼容 |
| **API 地址** | `https://api.siliconflow.cn/v1` |
| **模型覆盖** | DeepSeek-V3/V4、Qwen3、GLM-5、Llama、Mistral 等 40+ 模型 |
| **价格** | DeepSeek-V3: ¥1/M 输入 · Qwen2.5-7B: ¥0.35/M |
| **优势** | 一个 Key 用全家，无需 VPN，比 opencode-go 更便宜（去中介） |
| **注册** | cloud.siliconflow.cn → 免费额度 14 元 |

### 第二优先：DeepSeek 官方 API

| 项 | 详情 |
|-----|------|
| **API 地址** | `https://api.deepseek.com/v1` |
| **价格** | V3: ¥2/M 输入 · V4 Flash: ¥1/M |
| **优势** | 价格屠夫，官方直连零加价 |
| **局限** | 只有 DeepSeek 自家模型，无 Kimi/Qwen/GLM |
| **注册** | platform.deepseek.com |

### 第三优先：智谱 GLM 官方（低成本 Flash 模型）

| 项 | 详情 |
|-----|------|
| **API 地址** | `https://open.bigmodel.cn/api/paas/v4` |
| **Flash 价格** | GLM-4-Flash: **免费调用** · GLM-4.7-Flash: ¥0.42/M |
| **优势** | Flash 模型极便宜，适合 heartbeat/简单任务 |
| **注册** | open.bigmodel.cn |

## 📈 2026 价格对比（每百万 Token 输出价）

```
供应商          模型              输出价     性价比
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SiliconFlow    DeepSeek-V3       ¥2          极高 ★★★★★
DeepSeek直连   V4-Flash          ¥2          极高 ★★★★★  
智谱 GLM       GLM-4-Flash       ¥0 (免费)   无敌 ★★★★★
opencode-go    deepseek-v4-pro   ~¥6          中等 ★★★
Kimi直连       K2.6              ¥18         较低 ★★
GPT-5.5        -                 ¥210        极低 ★
```

## 🏗️ 推荐配置架构

```
任务路由策略:

简单任务 (heartbeat/summarize)
  → SiliconFlow DeepSeek-V3 或 智谱 GLM-4-Flash
  → 节省 80-90% Token 成本

日常对话 (主力)
  → opencode-go/deepseek-v4-pro (保持当前)
  → fallback → DeepSeek 直连 V4-Flash

代码/推理 (高难度)
  → opencode-go 或 SiliconFlow Qwen3-Max

供应商故障
  → opencode-go 挂了 → 自动 fallback 到 SiliconFlow
  → 再挂 → DeepSeek 直连
```

## 📋 接入步骤

### Step 1: 注册获取 API Key

1. **SiliconFlow**: 打开 `cloud.siliconflow.cn` → 注册 → 创建 API Key
   - 新用户送 ¥14 额度，够用很久
2. **DeepSeek**: 打开 `platform.deepseek.com` → 注册 → API Keys
   - 注册送 500 万 Token

### Step 2: 把 API Key 给我

获得 Key 后告诉我，我来编辑 `openclaw.json` 添加新供应商：

```json
"models": {
  "providers": {
    "opencode-go": { ... },
    "siliconflow": {
      "apiKey": "sk-你的key",
      "auth": "api-key",
      "api": "openai-completions",
      "baseUrl": "https://api.siliconflow.cn/v1"
    },
    "deepseek": {
      "apiKey": "sk-你的key",
      "auth": "api-key", 
      "api": "openai-completions",
      "baseUrl": "https://api.deepseek.com/v1"
    }
  }
},
"agents": {
  "defaults": {
    "models": {
      "siliconflow/deepseek-ai/DeepSeek-V3": {},
      "deepseek/deepseek-chat": {},
      ...
    },
    "model": {
      "primary": "opencode-go/deepseek-v4-pro",
      "fallbacks": [
        "siliconflow/deepseek-ai/DeepSeek-V3",
        "deepseek/deepseek-chat",
        "opencode-go/kimi-k2.6",
        "opencode-go/qwen3.7-plus"
      ]
    }
  }
}
```

### Step 3: 重启 Gateway

配置后需 `gateway restart`，之后就可以自动按 fallback 链切换了。

## ⚡ 预期效果

| 指标 | 改进 |
|------|------|
| **供应商容灾** | 从 1 个供应商 → 3 个，消除单点故障 |
| **成本** | 简单任务用 Flash 模型，省 80% |
| **模型选择** | 从 5 个模型 → 15+ 个模型 |
| **心跳成本** | 可配置独立 cron 用 Flash 模型 |
