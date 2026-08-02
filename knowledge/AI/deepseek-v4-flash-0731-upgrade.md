---
tags: [research, deepseek, model, agent, benchmark]
created: 2026-07-31
status: adopted
---

# DeepSeek V4 Flash 正式版 (0731) — Agent 能力跃升

> 2026-07-31 · 官方 API 公测上线 · 已交叉验证（官方文档 + IT之家 + 网易 + 凤凰）

## 核心结论

**V4-Flash 正式版 Agent 能力大幅超越 V4-Pro-Preview，逼近 Opus 4.8，成本仅 $0.28/M 输出。**

- 架构/尺寸与 Preview 相同（284B 总 / 13B 激活），仅重新后训练
- **性价比之王**：Terminal Bench 82.7 接近 Opus 4.8 的 85.0，成本是 1/100+

## 官方基准（Agent 任务）

| 基准 | Flash 正式版 | Flash Preview | V4-Pro Preview | GLM-5.2 | Opus 4.8 |
|------|:---:|:---:|:---:|:---:|:---:|
| Terminal Bench 2.1 | **82.7** | 61.8 | 72.1 | 81.0 | 85.0 |
| NL2Repo | **54.2** | 39.4 | — | — | — |
| Cybergym | **76.7** | 38.7 | — | — | — |
| DeepSWE | **54.4** | 7.3 | — | — | — |
| Toolathlon verified | **70.3** | 49.7 | — | — | — |
| Agent Last Exam | **25.2** | — | — | — | — |
| Automation Bench | **25.1** | — | — | — | — |
| DSBench-FullStack | **68.7** | — | — | — | 71.6 |
| DSBench-Hard | **59.6** | — | — | — | 71.7 |

> 注：Code Agent 任务用 DeepSeek Harness 极简模式测试（max effort, topp=0.95, temp=1.0）

## API 变更

| 项 | 内容 |
|----|------|
| **模型名** | `deepseek-v4-flash`（调用方式不变） |
| **旧别名** | `deepseek-chat` / `deepseek-reasoner` → 3 个月后退役 |
| **新能力** | 原生支持 Responses API 格式（适配 Codex） |
| **Codex 配置** | Mac: `bash <(curl -fsSL cdn.deepseek.com/api-docs/codex-deepseek-setup.sh)`<br>Win: `irm cdn.deepseek.com/api-docs/codex-deepseek-setup-en.ps1 \| iex` |
| **定价** | 输入 $0.14/M (miss) / $0.0028/M (cache hit) / 输出 $0.28/M |
| **并发** | 2500 |

## 对我们的落地

### 已完成 ✅
1. **fallback 链升级**：`deepseek-chat` → `deepseek-v4-flash`（官方直连，`hermes config set fallback_model`）
2. **官方 API 验证**：curl 直连 `deepseek-v4-flash` 响应正常
3. **记忆更新**：模型信息 + 注意事项

### 可继续探索 🔍
- [ ] opencode-go 代理是否已自动切到正式版（模型名不变，需实测 agent 任务对比）
- [ ] 是否把 Cron 任务的主力从 doubao 换到 v4-flash（成本更低 + Agent 更强）
- [ ] Codex CLI 集成（官方已适配，Windows 一键脚本可用）

## 关键教训

⚠️ **`hermes config set fallback_model` 是整体替换**，不是单项修改——执行前先备份原值。非识别的 config key 会被保存但 Hermes 可能不读取（本次误清空后已恢复）。

---

*2026-07-31 研究沉淀 · 官方 API 直连验证通过*

---
> 关联: [[LLM-Providers]]（供应商/模型策略） | [[HOME|🏠 首页]]
