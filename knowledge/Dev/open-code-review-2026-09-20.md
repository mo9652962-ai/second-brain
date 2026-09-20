---
tags: [GitHub, W39, 代码审查, 阿里, Codex, CLI, 质量门禁]
aliases: [open-code-review, OCR, Alibaba OCR]
date: 2026-09-20
source: https://github.com/alibaba/open-code-review
---

# alibaba/open-code-review — 阿里代码审查 Agent CLI（已在用，本周深度补全）

> 2026-09-20 W39 精选。阿里内部官方 AI 代码审查助手开源版：读 git diff → LLM agent 行级评论。**sora 已通过 ai-code-review skill 在用此工具**（07-31 起，ocr review/scan 闭环），本周 trending 21.3k★（5 月开源时 5k→21k），值得深度补全知识 + 更新技能。Apache-2.0。

## 一句话定位

**为代码审查而生**的 agent：确定性管线（任务拆分/文件过滤/行号定位/规则路由）负责「确定的事」，LLM agent 负责「语义的事」（风险检测/上下文探索/问题分类）。官方 benchmark：同模型下 Precision/F1 显著高于通用 agent（Claude Code），token 消耗仅 ~1/9，Recall 故意更低（宁缺毋滥）。

## 核心特征 / 技术架构

### 混合架构：确定性 + Agent 解耦

```
git diff → 确定性管线（文件过滤/规则路由/子任务拆分）
              ↓
        LLM Agent（工具使用：读全文件/搜代码库/查上下文）
              ↓
    行级定位模块（3 层渐进式 LLM 策略 → 精确到行号）
              ↓
    反思模块（拦截幻觉与知识漂移）
              ↓
        结构化评论 + SARIF
```

### 关键能力

| 能力 | 说明 |
|:--|:--|
| ocr review / ocr scan | diff 审查 / 全文件扫描（无 diff 也能审陌生代码库） |
| 内置规则集 | 10+ 语言（Java/TS/Go/Python/Kotlin/Rust/C++/C），NPE/线程安全/XSS/SQL 注入专项 |
| 记忆压缩 | 为 code review 定制 3 层上下文管理（frozen/compress/active），突破 token 限制做深审 |
| 动态并发 | 子任务并行，默认 8 个 goroutine worker |
| 多模型协议 | Anthropic Messages / OpenAI Chat Completions / OpenAI Responses；预设 Anthropic/OpenAI/DashScope/DeepSeek/Z.AI |
| **Delegation Mode** | 编码 agent（Claude Code/Codex）用自己的 LLM 跑审查，无需 OCR API key |
| 插件生态 | Claude Code（slash commands）/ Codex（callable skills）/ Cursor / OpenCode / Kimi；MCP server 扩展审查工具 |
| CI/CD | GitHub Actions / GitLab CI / GitFlic / Gerrit |
| 基准 | AACR-Bench：50 开源仓库 + 200 真实 PR + 10 语言，80+ 高级工程师标注 1,505 ground-truth issues |

## 💎 可借鉴点（对 sora 工作流）

1. **技能更新**：ai-code-review skill 记录的 star 数停留在 11K（07-31）→ 现 21.3k；新增 Delegation Mode、Codex callable skills 插件、AACR-Bench 基准——值得把「委派 Codex 时用 OCR delegation 模式」纳入工作流（自己 LLM 审查、不额外花 OCR API）。
2. **「确定性管线 + LLM 语义」分离架构 = 模板**：sora 的工程工作流（engineering-workflow、code-quality-bootstrapping）可吸收——把「能确定的事」（过滤/定位/规则）与「要语义的事」（风险判断）拆开，是比纯 agent 更省 token 更稳的模式（~1/9 token 实证）。
3. **行级定位 3 层策略 + 反思模块**：先粗后细定位 + 专门模块拦幻觉——对应 sora「ui-pixel-verification 不信视觉模型描述」「完成声明必须核验」的可靠性文化，可写入 code review 技能的反幻觉检查点。
4. **Recall 故意低的取舍**：审查宁缺毋滥（高 Precision）——与 sora 交付质量门（grounded-copy 变模糊为具体、反谄媚承诺）一致：少而准优于多而噪。

## 安装 / 验证命令

```bash
npm install -g @alibaba-group/open-code-review
ocr config set provider deepseek   # 或 anthropic/openai
ocr config set providers.deepseek.api_key "$DEEPSEEK_API_KEY"
ocr llm test
ocr review        # 审当前工作区改动
ocr scan          # 全文件扫描（陌生代码库审计）
# Delegation Mode（Codex 场景）：
ocr delegate preview && ocr delegate rule src/main.go
```

（详细用法见 skill `ai-code-review`，2026-07-31 实测：一轮扫描抓 5 个真 bug。）

## 总结评价表

| 维度 | 评价 |
|:--|:--|
| 技术含金量 | ★★★★★ 阿里大规模验证（数万开发者/百万级缺陷），混合架构 + 记忆压缩工程成熟 |
| 值得安装 | 🟢 **已在用**（ai-code-review skill）——本次更新 star/新特性 |
| 趋势判断 | 专用审查 agent 跑赢通用 agent（~1/9 token + 更高 Precision）→ 垂直工具化是 agent 应用方向；阿里开源生态持续输出 |
| 风险 | Recall 低 = 可能漏报；markdown 等非代码文件默认过滤；规则集需按项目定制 |

---
> 🗺️ 属于 [[MOC-Dev]] · [[MOC-GitHub]] · 周报 [[../../memory/2026/09/github-trending-w39|W39]]
