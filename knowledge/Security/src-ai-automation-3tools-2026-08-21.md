---
tags: [src, 自动化挖洞, AI, 漏洞挖掘, vulnclaw]
domain: Security
status: fresh
date: 2026-08-21
---

# SRC 自动化挖洞三工具落地（2026-08-21 千轮研究）

> 背景：sora 要「AI 自动跑 + 写报告」的 SRC 流水线（补齐 AI+网安自动化）
> 研究结论：**无 Docker 环境**（VirtualizationFirmwareEnabled=False）→ 排除 Docker 依赖项目
> 决策：**三个全落地**（VulnClaw / SRC-Hunter / AutoSRC）

## 候选矩阵（实证 2026-08-21）

| 项目 | Star/规模 | 部署 | 亮点 | 状态 |
|:---|:---|:---|:---|:---|
| **VulnClaw** | 2067★ MIT | `pip install vulnclaw` | 自然语言→信息收集→挖洞→利用→报告+PoC；13 provider（DeepSeek/基元律动 OpenAI 兼容）；21 Skill+180 文档 | ✅ 落地中 |
| **SRC-Hunter** | 7★ beta | 单进程 FastAPI+SQLite，Windows setup.bat | SRC 专用：FOFA 搜集+LLM Worker+质量闸+去重+情报库+EduSRC 报告 | ✅ 落地中 |
| **AutoSRC** | GitCode 11000 行 | Windows 批处理 | 资产采集/多引擎扫描/AI 误报筛选/核验/SRC 标准报告+表单填充/风控限流 | ✅ 落地中 |
| AutoHunter | 84★ | Docker 必需 | Collector→Worker→Reviewer 三 agent | ❌ 无虚拟化暂缓（有云服务器再上）|
| src-hunter-skill | Claude skill | 需 Claude Code | 19 playbook+2887 H1 案例+报告模板 | ⚪ 知识库借鉴 |

## 配置要点（通用）

- **LLM**：OpenAI 兼容——基元律动（jiyuanlvdong base_url）或 DeepSeek 官方
- **FOFA**（SRC-Hunter 用）：fofa.info 个人中心拿 key
- **合规红线**：只测授权目标/本地靶场；FOFA 语法收窄归属（org/domain/cert）

## 使用定位

- **VulnClaw**：日常主力——单目标自然语言渗透 + 报告/PoC
- **SRC-Hunter**：批量 SRC——FOFA 自动搜集 + 多 Worker 队列 + 去重
- **AutoSRC**：轻量全自动——Windows 批处理挂机 + AI 误报筛选 + 表单填充

## 部署结果（实测 2026-08-21）

| 工具 | 结果 | 备注 |
|:---|:---|:---|
| **VulnClaw 0.3.8** | ✅ scan+report 跑通（扫 127.0.0.1:8765）| 基元律动 key 配置完成；nmap 已装（需 export PATH）|
| **SRC-Hunter** | ✅ localhost:8080 运行中 | 管理员令牌 `Eh3zYJD-B7NUTibPFbHkORGt9VmPbVilyNnzKm5WtRk`（backend/data/admin_token.txt）|
| **AutoSRC** | ✅ venv+依赖+基元律动已配 | 模块导入 OK；注意 workdir 守卫 bug |

## 使用定位

- **VulnClaw**：日常主力——单目标自然语言渗透 + 报告/PoC
- **SRC-Hunter**：批量 SRC——FOFA 自动搜集 + 多 Worker 队列 + 去重
- **AutoSRC**：轻量全自动——Windows 批处理挂机 + AI 误报筛选 + 表单填充

## 待办

- [x] VulnClaw pip install + provider 配置 + 授权目标验证 → ✅ 2026-08-21 已落地：0.3.8 scan+report 跑通（扫 127.0.0.1:8765）
- [x] SRC-Hunter clone + setup + 启动 → ✅ 2026-08-21 已落地：localhost:8080 运行中
- [x] AutoSRC 下载 + 依赖（Chrome/ChromeDriver/Subfinder/Nuclei/Xray/Dirsearch）→ ✅ 2026-08-21 已落地：venv+依赖+基元律动已配（注意 workdir 守卫 bug）
- [x] 实测计划：本地靶场（Vulhub/DVWA）→ 授权目标 → ⏳ 本地靶场已就绪（DVWA 七漏洞通关，见 [[dvwa-practice-2026-08-17]]）；授权目标侦察进行中（联想/小程序/T3 三方向，8/21 反思收敛至补天 1 个有效漏洞）

---
*k (Hermes) 2026-08-21 · 千轮研究落地*

---
> 🗺️ 属于 [[MOC-Security]] · [[Home|🏠 Home]]
