---
aliases:
  - trending-2026-08-05
tags:
  - github-trending
  - research
  - pdf
  - agent-infra
  - memory
  - llm-inference
created: 2026-08-05
updated: 2026-08-05
status: adopted
domain: research
---

# GitHub Trending 研究 — 2026-08-05（5 项目）

> 来源：sora 分享的 GitHub 趋势摘要 + web_search 交叉验证
> 方法：learn（读原文）→ research（引擎验证）→ apply（评估落地）

---

## 🥇 1. Agent-Reach（66.4k stars）— 最值得落地

| 项目 |  |
|:-----|:--|
| **地址** | https://github.com/Panniantong/Agent-Reach |
| **协议** | MIT |
| **作用** | 给 AI Agent 装"互联网眼睛"——6+ 平台一站式 CLI，零 API 费用 |
| **平台** | 网页(零配置) / YouTube 字幕(零配置) / RSS(零配置) / GitHub / Twitter / Reddit / B站 / 小红书 / Facebook / Instagram / LinkedIn / V2EX / 雪球 / 小宇宙 |

### 核心价值（对 sora 系统）

**Hermes 现在缺的正好是这几个**：
- **B站**：bili-cli 搜索+视频详情，字幕需 OpenCLI（免费）
- **小红书**：搜索/阅读/评论（Cookie-Editor 或 OpenCLI 复用 Chrome 会话）
- **雪球**：股票行情/热门帖/热门股票排行
- **YouTube 字幕**：yt-dlp 零配置

### 架构亮点（值得借鉴）

1. **多后端路由**：每平台「首选+备选」，yt-dlp 被 B站风控封死 → 自动切 bili-cli，用户零操作
2. **Cookie 本地存储**：只存本地不上传；`agent-reach doctor` 一条命令诊断
3. **一句话安装**：复制 install.md URL 给 Agent，自动装完
4. **自带诊断**：doctor 命令检查每渠道状态

### ⚠️ 风险（研究确认）

- Cookie 登录的平台（Twitter/小红书）有**封号风险**——必须用**专用小号**
- Cookie = 完整登录权限，泄露=号没
- 本地电脑不需要代理，服务器才需要（~$1/月）

### 落地评估

| 场景 | 价值 | 行动 |
|:-----|:----:|:-----|
| B站视频/字幕调研 | 高 | 🟡 装 agent-reach，用 bili-cli（无需登录，零风险） |
| 小红书口碑调研（闲鱼接单/竞品） | 高 | 🟡 用专用小号 cookie，评估后再上 |
| 雪球行情（AI 博主选题） | 中 | 🟢 零配置即可用 |
| YouTube 字幕总结 | 高 | 🟢 yt-dlp 零配置 |
| Twitter 搜索 | 中 | 🟡 需 cookie，用小号 |

---

## 🥈 2. firecrawl/pdf-inspector（9.6k stars）— PDF 处理升级

| 项目 |  |
|:-----|:--|
| **地址** | https://github.com/firecrawl/pdf-inspector |
| **协议** | MIT |
| **作用** | Rust PDF 分类 + 文本提取 + Markdown 转换，**无需 OCR**（文本版 PDF） |
| **绑定** | Python / Node.js / WASM（浏览器） |

### 基准（opendataloader-bench，200 PDF，M4 Pro）

| 引擎 | Overall | Tables | Speed(200 docs) |
|:-----|:-------:|:------:|:---------------:|
| **pdf-inspector** | **0.875** | **0.814** | **0.470s** |
| liteparse | 0.873 | 0.693 | 0.750s |
| opendataloader | 0.831 | 0.489 | 2.569s |
| pymupdf4llm | 0.735 | 0.401 | 17.117s |
| markitdown | 0.589 | 0.273 | 16.165s |

**pdf-inspector 比 pymupdf4llm 快 36 倍，表格准确率翻倍。**

### 智能路由（核心卖点）

```
PDF 到达 → 分类（~20ms，Tj/TJ 文本算子检测）
  ├─ TextBased + 高置信 → 本地提取（~150ms）→ done
  └─ Scanned/ImageBased → 送 OCR 服务（2-10s）
```

54% 的 PDF 是文本版——先分类再路由，省掉不必要的 OCR 成本。

### 落地评估

| 场景 | 价值 | 行动 |
|:-----|:----:|:-----|
| 论文 PDF → Markdown（arXiv/周报输入） | 高 | 🟡 装 pdf-inspector 到 python 环境，替代 markitdown |
| 闲鱼接单 PDF 解析 | 中 | 🟡 客户发扫描件仍需 OCR，文本版提速 |
| 表格提取（财报/数据） | 高 | 🟢 比 markitdown 强很多 |

---

## 🥉 3. TencentDB-Agent-Memory（12k stars）— 记忆架构对标

| 项目 |  |
|:-----|:--|
| **地址** | https://github.com/TencentCloud/TencentDB-Agent-Memory |
| **协议** | MIT |
| **作用** | Agent 长期记忆系统：4 类记忆资产统一注册 |

### 四类记忆资产（对标 Second Brain）

| TencentDB 资产 | 对应 Second Brain | 差距 |
|:---------------|:------------------|:-----|
| Chat Memory（对话记忆） | memory/ + LEARNINGS.md | ✅ 已有 |
| Skills（技能库） | skills/ | ✅ 已有 |
| Wiki（知识 Wiki） | knowledge/ | ✅ 已有 |
| **CodeGraph（代码图）** | ❌ 无 | 🟡 差距——代码依赖图谱 |

### 关键设计：Memory Hub 统一注册

所有记忆资产注册到 Memory Hub（统一索引），Agent 通过一个接口读写任意类型——对应我们四大自举系统各自为政的痛点。

### 落地评估

| 差距点 | 行动 |
|:-------|:-----|
| CodeGraph（代码依赖图） | 🟡 评估 codebase-memory-mcp 是否可补（已装，14k 节点） |
| Memory Hub 统一索引 | 🟢 借鉴思路：给 Second Brain 加统一索引（MOC 已部分覆盖） |
| 符号短记忆 + 长期记忆分层 | 🟢 对应 context-management-bootstrapping 四级记忆 |

---

## 📌 简评（低优先级）

### 4. AirLLM（28.2k stars）— 4GB 显存跑 70B

- **原理**：流式加载权重（分块加载+计算），不全部塞显存；MoE 模型一次流一个 expert
- **实测**：70B/4GB、405B/8GB、DeepSeek-V3 671B/~12GB、Kimi K3 2.8T/3.72GB
- **代价**：流式加载有推理延迟——只适合离线/批量，不适合实时
- **评估**：sora 有 RTX 4060 8GB，可跑 70B 全精度——但 Hermes 用 API 更划算（DeepSeek 官方直连），本地推理价值低 🟢 收藏不装

### 5. reverse-skill（10k stars）— 逆向/渗透技能路由

- **作用**：AI Agent 自动路由安全工具链（jadx/apktool/Frida/IDA/Burp），经验沉淀复用
- **社区评价**：正面（"AI 做逆向终于不瞎搞了"）
- **评估**：sora 主业不是安全研究；但"技能路由 + 经验自举"架构与 Hermes skills 体系同构，值得参考设计 🟢 收藏借鉴架构，不装工具链

---

## 综合评估表

| 项目 | 相关模块 | 可落地性 | 优先级 |
|:-----|:---------|:--------:|:------:|
| Agent-Reach | Hermes 信息获取（B站/小红书/雪球） | 高 | 🟡 本周评估安装 |
| pdf-inspector | 论文解析/文档提取 | 高 | 🟡 装到 python 环境 |
| TencentDB-Memory | Second Brain 记忆架构 | 中 | 🟢 借鉴 CodeGraph/统一索引 |
| AirLLM | 本地推理 | 低 | 🟢 收藏 |
| reverse-skill | 技能路由架构 | 低 | 🟢 收藏借鉴 |

## 落地行动清单

### 🟡 本周（1-2 天）
- [x] 评估 `pip install agent-reach` —— 先装零配置渠道（B站/YouTube/RSS/网页），cookie 平台用小号再上 ✅ 2026-08-05 已装 v1.5.0（零配置渠道可用；cookie 平台待小号）
- [x] 装 pdf-inspector 到 python 环境，跑一个论文 PDF 对比 markitdown 速度 ✅ 2026-08-05 已装 v0.2.6（markitdown 对比待有论文 PDF 素材时补跑）

### 🟢 收藏
- [x] TencentDB 四类记忆资产 vs Second Brain 差距表（CodeGraph 补缺）✅ 2026-08-06 已收藏备查：TencentDB-Memory 借鉴点 = 统一索引/结构化记忆，待 Second Brain 扩容 >1000 篇时再对照落地
- [x] AirLLM 记录在案（RTX 4060 8GB 可跑 70B，实时场景不考虑）✅ 2026-08-06 已记录：本地推理备选，仅离线/研究场景
- [x] reverse-skill 的"路由+自举"架构参考 ✅ 2026-08-06 已收藏：技能路由+自举模式，与 hermes-smart-model-router 思路同源

---

*来源：GitHub Trending（sora 分享）+ web_search 交叉验证 | 状态：adopted*
