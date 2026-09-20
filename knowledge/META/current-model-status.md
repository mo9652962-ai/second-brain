---
type: current-state
verified_at: 2026-09-20
status: active
tags: [meta, models, api, fact-source]
---

# 当前模型与 API 状态

> **事实源**：模型名、价格、可用性一律以本文为准。
> 旧文档中的价格表、模型名可能已过期 —— 不要复制价格，指向官方来源。
> 下次复核：2026-10-20（或 provider 变更时）。

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

## Hermes 运行时配置（2026-09-20 实测）

> 来源：`AppData\Local\hermes\config.yaml`，**不手工猜测**。

```yaml
model:
  default: gemini-3.8-flash-high
  provider: cpa-gui
```

**已配置的 provider**（custom_providers）：
`opencode-go` / `siliconflow` / `moonshot` / `fangzhou-1` / `jiyuanlvdong` /
`dengzhen` / `keylink` / `local-qwen` / `sensenova` / `jiyuanlvdong-2` /
`cpa-gui` / `workbuddy` / `workbuddy-ai`

**辅助任务模型**（auxiliary）：

| 用途 | 模型 | provider |
|:---|:---|:---|
| vision | `qwen-vl-max` | — |
| skill_match | `doubao-seed-1-6-flash-250615` | `custom:fangzhou-2` ⚠️ |
| 其他辅助 | doubao-seed-2-0-* / glm-5-2-260617 / minimax-m3 | `custom:fangzhou-2` ⚠️ |

> ⚠️ **配置缺陷（2026-09-20 发现）**：`auxiliary.*.provider` 引用了 `custom:fangzhou-2`，
> 但 `custom_providers` 中**只定义了 `fangzhou-1`，没有 `fangzhou-2`**。
> 该引用共出现 6 次，可能导致辅助模型（含 skill_match）回退或失败。
> 待处理：确认是否应改为 `custom:fangzhou-1`，或补上 fangzhou-2 定义。

---

## 相关

- [[knowledge/META/current-environment]] — 环境与 Docker 事实源
- [[knowledge/META/knowledge-sources]] — 路径与数量事实源
- [[index]] — 知识库路由层
