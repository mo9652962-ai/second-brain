---
type: current-state
verified_at: 2026-11-08
status: active
tags: [meta, models, api, fact-source]
---

# 当前模型与 API 状态

> **事实源**：模型名、价格、可用性一律以本文为准。
> 旧文档中的价格表、模型名可能已过期 —— 不要复制价格，指向官方来源。
> 下次复核：2026-12-08（或 provider 变更时）。

## 命名规范

**canonical model** = 配置中应当使用的规范名。
**legacy alias** = 历史名称，可能仍被接受，但对应模型已退役，实际由新模型提供服务。

新写的配置示例一律用 canonical model；legacy alias 只出现在「历史兼容」说明里。

---

## DeepSeek

```yaml
canonical_model: deepseek-flash
model_version: DeepSeek-V4.1-Flash
legacy_aliases:
  - deepseek-v4-flash
  - deepseek-v4-flash-vision-exp
availability: 可用
pricing_source: https://api-docs.deepseek.com/quick_start/pricing
last_verified: 2026-09-20
next_review: 2026-10-20
```

- 旧名称仍可能被接受，但对应模型**已经退役**，实际请求由 **V4.1 Flash** 提供
- **当前价格以官方页面为准**，不在多个历史文件中复制价格表
- 旧 benchmark 卡片保留，但必须加历史标注（见下）

> ⚠️ **不要**在配置示例中写 `deepseek-v4-flash` 作为主力模型 —— 用 `deepseek-flash`。

### 历史 benchmark 卡片的标注要求

旧评测卡片保留原文，但顶部加：

```markdown
> 历史记录：该模型/别名的评测结果截至 2026-08-09。
> 不代表当前 API 的 canonical model 或当前价格。
```

---

## 其他 Provider

### Google Gemini

```yaml
canonical_model: gemini-3.8-flash-high
availability: 可用
pricing_source: https://ai.google.dev/pricing
last_verified: 2026-09-20
next_review: 2026-10-20
```

### OpenAI

```yaml
canonical_model: (按 config.yaml 实际配置为准)
availability: 待运行时验证
pricing_source: https://openai.com/api/pricing/
last_verified: (未验证)
next_review: 2026-10-20
```

### Anthropic Claude

```yaml
canonical_model: (按 config.yaml 实际配置为准)
availability: 待运行时验证
pricing_source: https://www.anthropic.com/pricing
last_verified: (未验证)
next_review: 2026-10-20
```

### Qwen (阿里云 DashScope)

```yaml
canonical_model: qwen-vl-max        # 视觉辅助
availability: 可用
pricing_source: https://help.aliyun.com/zh/model-studio/models
last_verified: 2026-09-20
next_review: 2026-10-20
```

---

## Hermes 运行时配置（2026-11-08 实测）

> 来源：`AppData\Local\hermes\config.yaml`，**不手工猜测**（yaml 解析实读，非肉眼抄）。

```yaml
model:
  default: deepseek-v4.1-flash
  provider: workbuddy-ai
fallback_model:
  - provider: custom:workbuddy-ai
    model: deepseek-v4.1-flash
    base_url: http://127.0.0.1:8788/v1
    api_mode: chat_completions
```

**已配置的 provider**（`providers:` 共 19 个，2026-11-08 实读）：
`moonshot` / `moonshot-2` / `opencode-go` / `siliconflow` / `fangzhou-1` / `fangzhou-2` /
`jiyuanlvdong` / `jiyuanlvdong-2` / `dengzhen` / `dashscope` / `keylink` / `local-qwen` /
`tabitoken` / `zhipu` / `sensenova` / `openrouter` / `workbuddy` / `workbuddy-ai` / `cpa-gui`

> 注：`custom_providers:` 这个键现在是空列表 `[]`——09-20 版文档按旧 schema 把它当 provider 清单，
> 会得出「只有 13 个 provider」的错误结论。**以 `providers:` 为准**。

**辅助任务模型**（auxiliary，9 项全部实读）：

| 用途 | 模型 | provider |
|:---|:---|:---|
| vision | `glm-5v-turbo` | `workbuddy-ai` |
| compression | `deepseek-v4.1-flash` | `workbuddy-ai` |
| approval_classifier | `glm-5.2` | `workbuddy-ai` |
| browser_screenshot | `minimax-m3` | `custom:opencode-go` |
| memory_refresh | `deepseek-v4.1-flash` | `workbuddy-ai` |
| session_summary | `deepseek-v4.1-flash` | `workbuddy-ai` |
| skill_match | `deepseek-v4.1-flash` | `workbuddy-ai` |
| tool_dispatch | `deepseek-v4.1-flash` | `workbuddy-ai` |
| web_summary | `deepseek-v4-flash` | `custom:workbuddy` |

> ✅ **旧配置缺陷已闭环（2026-11-08 复核）**：09-20 记的「`auxiliary.*.provider` 引用
> `custom:fangzhou-2` 但未定义」已不复存在——`fangzhou-2` 现已在 `providers:` 中定义，
> 且 auxiliary 已整体切到 `workbuddy-ai`，不再有任何 `fangzhou-2` 引用。
> 复核命令（5 秒）：
> `python -c "import yaml,io;c=yaml.safe_load(io.open('~/AppData/Local/hermes/config.yaml',encoding='utf-8'));print(c['model']);print(list(c['providers']));print(c['auxiliary'])"`

---

## 相关

- [[knowledge/META/current-environment]] — 环境与 Docker 事实源
- [[knowledge/META/knowledge-sources]] — 路径与数量事实源
- [[index]] — 知识库路由层
- [[knowledge/AI/免费额度模型通道-2026-11-06]] — 官方零费率 / 注册赠额通道盘点（数字未逐条复核，接入前看官方页）
