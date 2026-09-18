# GenOffice — 全球首个全功能开源 AI Office 套件（千轮研究 2026-09-18）

> 来源：抖音【AI观察笔记】→ genspark-ai/genoffice。一句话定位：**AI 原生开源 Office，自配 CLI + agent skill 让 Codex 直接产出真实 .docx/.xlsx/.pptx。**

## 结论置顶

**对 sora 的核心价值 = 用 Codex 委派直接产出真实 Office 文件，补上论文/PPT 接单链最短的一环。** 之前 Codex 只能吐 Markdown/文本，Word/PPT 得人工搬或手写 python-docx/pptx 代码；GenOffice 的 `genoffice` CLI 让编码 agent 直接创建/编辑真实格式，还能 `render` 出 PNG 自检、`slides check` 防溢出。

## 实证数据（2026-09-18 抓取）

| 项 | 值 |
|---|---|
| 仓库 | `genspark-ai/genoffice` |
| Star / Fork | **7,140** / 937（8/3 发布，1.5 个月） |
| 协议 | Apache-2.0（`ee/` 目录保留企业模块） |
| 活跃度 | 今日仍在 push，最新版 v0.10.639（9/17 发布，迭代极快） |
| 技术栈 | 6 Electron 应用 + TS 引擎 + Rust xlsx sidecar + PDFium WASM |
| 定位 | Docs/Sheets/Slides/PDF/Markdown/HTML 六合一 |

## 关键能力

- **字节级保留**：只重写被改动的部分，其余字节原样保留，文档在 Word/Excel/PPT 里继续正常打开。
- **AI 可审查**：编辑以 tracked changes + diff 落地，一键回滚；表格用活公式而非贴死数字。
- **本地化转换**：PDF→Word/Excel/PPT、Markdown→Word、HTML→Word 全在本机跑，无需云端。
- **BYOK 全接现有 key**：内置 Claude/OpenAI/Gemini/**DeepSeek/Kimi/GLM/Qwen/Doubao/MiniMax**/Grok/OpenRouter + 任意 OpenAI-compatible 端点（含本地服务）—— sora 的方舟/DeepSeek/硅基流动 key 可直接填。

### CLI（对 sora 最有价值）
```bash
genoffice info report.docx --json          # 读文档结构
genoffice convert report.md --to pdf       # 格式互转
genoffice create --type docx --from notes.md --out notes.docx
genoffice create --type xlsx --from table.json --out sales.xlsx  # 公式保活
genoffice docs read report.docx --range 0-9 --json   # 读 → apply 改
genoffice render report.docx --out shots/  # 每页 PNG 自检
genoffice image "..." --aspect 16:9 --out cover.jpg  # 生成图
genoffice slides check/audit/render/replace  # PPT 防溢出+审计+渲染自检流水线
genoffice open sales.xlsx                  # 交给编辑器打开
```

### Agent skill / MCP 接入
- agent skill 支持：Claude Code、**Codex**、Cursor、Gemini CLI、GitHub Copilot、OpenCode、Windsurf。
- 安装：Settings→Integrations 一键写入，或 `npx skills add genspark-ai/genoffice`。
- MCP：`genoffice mcp` stdio server（29 工具），Claude Code：`claude mcp add --transport stdio genoffice -- genoffice mcp`。

## 局限（官网 FAQ 自认）

- 仍 **Alpha**（v0.10），迭代快但不够稳。
- **复杂格式会漂移**："Complex formatting can vary; check important files before sharing" —— 交付客户前必须人工核一遍。
- Electron 应用，吃内存（sora 16G 要注意）。

## 决策建议

- **值得装 Windows 版实测 CLI**（免费/开源/直接强化接单），先跑通 `genoffice --version` + 建测试 .pptx，实证后再决定是否纳入接单流 + 建技能沉淀。
- BYOK 填 DeepSeek/方舟 key 即可用，无需额外付费。