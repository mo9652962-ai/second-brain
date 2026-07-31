---
tags: [research, github, trending, project-study]
created: 2026-07-31
status: absorbed
---

# GitHub Trending 25 项目研究（小黑盒文章）

> 2026-07-31 · 全部经 GitHub 验证，重点项目已落地

## 已落地（3 个 P0）

### 1. codebase-memory-mcp ✅ 已安装
| 项 | 内容 |
|----|------|
| 仓库 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) 36.7k★ |
| 功能 | 代码库知识图谱 MCP，158 语言，token 省 99%（40万→3千） |
| 安装 | `AppData/Local/Programs/codebase-memory-mcp/` v0.9.0 |
| 验证 | ✅ 工作区索引成功：14,219 节点 / 47,866 边 |
| 查询 | `codebase-memory-mcp cli search_graph --project C-Users-31954-.openclaw-workspace --query "MathWorkbookConfig"` |

### 2. OfficeCLI ✅ 已安装
| 项 | 内容 |
|----|------|
| 仓库 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) 23.5k★ |
| 功能 | AI Agent 专用 Office 套件，单二进制，无 Office 依赖 |
| 安装 | `AppData/Local/OfficeCLI` v1.0.143，**自动装了 Hermes skill** |
| 验证 | ✅ create/add/view PPT 全通 |
| 用法 | `officecli create deck.pptx` → `officecli add deck.pptx / --type slide --prop title="..."` |

### 3. ECC ⏳ 待装（下载失败）
| 项 | 内容 |
|----|------|
| 仓库 | [affaan-m/ECC](https://github.com/affaan-m/ECC) 236k★ |
| 功能 | Agent 技能体系：67 agents + 281 skills + AgentShield 安全扫描 |
| Hermes 支持 | ✅ 官方（`./install.sh --profile minimal --target hermes`） |
| 安装 | 网络恢复后执行 |

## 值得关注（P1/P2）

| 项目 | Stars | 价值 | 状态 |
|------|:---:|------|:---:|
| hallmark | 20.2k | 反 AI 味 UI 设计（57 道关卡） | P1 |
| superpowers | 264k | 技能框架+方法论（流程可借鉴） | P1 |
| speech-to-speech | 9k | HF 本地语音 Agent | P2 |
| open-code-review | 16.8k | ✅ **已装过**（ocr CLI） | 已用 |
| GeoLibre | 3.5k | ✅ **已存档**（待 GIS 需求） | 已用 |

## 存档不装（18 个）

| 项目 | Stars | 原因 |
|------|:---:|------|
| jcode | 14.4k | Rust harness，省内存（我们已有 opencode-go） |
| VibeVoice | 51k | 微软语音，需 GPU |
| airi | 46k | 赛博生命，娱乐向 |
| strix | 44.9k | AI 渗透测试，专业安全场景 |
| MediaCrawler | 58.7k | 爬虫，**合规风险高**（明确警示） |
| FlashKDA | 1.1k | CUDA 内核，需 GPU |
| Kronos | 35k | 金融预测模型 |
| Vibe-Trading | 28.8k | 量化交易（⚠️ 假币警示） |
| colibri | 21.4k | 本地跑 744B GLM（需 370GB 磁盘） |
| claude-video | 12.4k | 视频分析（Hermes 已有 video_analyze） |
| OpenCut | 79.5k | 开源剪映（重写中，用 classic） |
| OmniRoute | 35.7k | AI 网关（我们已有多 provider） |
| Ghost-Downloader-3 | 7.5k | 下载器 |
| MiroFish | 69.7k | 群体智能预测 |
| snipe-it | 14.2k | IT 资产管理 |
| faceswap | 56.8k | 换脸，伦理风险 |
| openwork | 18.7k | Claude Cowork 替代 |
| ECC (其余) | 236k | 只装 Hermes 部分 |

## 趋势洞察
1. **Agent 工程化** — ECC/superpowers/jcode 领跑，技能体系成为核心竞争力
2. **MCP 基础设施** — codebase-memory-mcp/OmniRoute 都是 MCP 生态
3. **本地大模型** — colibri/speech-to-speech 降低本地推理门槛

---

*2026-07-31 研究沉淀 · 3 个 P0 落地 2 个*
