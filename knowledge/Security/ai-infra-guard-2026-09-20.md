---
tags: [github, W39, 安全, AI红队, MCP安全, Skills扫描, Agent安全, 腾讯]
aliases: [AI-Infra-Guard, AIG, AI基础设施守卫]
date: 2026-09-20
source: https://github.com/Tencent/AI-Infra-Guard
---

# Tencent AI-Infra-Guard（A.I.G）— AI 红队平台：扫 Agent / MCP / Skills / 基础设施

> 2026-09-20 W39 精选。腾讯朱雀实验室开源的 **AI 红队平台**：Agent Scan + MCP Server & Agent Skills Scan + AI infra 漏洞扫描 + 越狱评估四合一。≈ 6.1k★（+525/周），Apache-2.0。W38 腾讯 WeKnora 之后又一份腾讯开源，方向是 AI 安全体检。

## 一句话定位

给「AI 应用栈」做安全自检的一站式红队工具：你的 MCP server / Agent Skill / Agent 工作流 / 推理框架（Ollama/ComfyUI/vLLM/n8n…）有哪些漏洞、哪些注入面、能不能被越狱——扫描并出报告。

## 核心特征 / 技术架构

| 扫描器 | 能力 |
|:--|:--|
| **mcp-scan** | MCP Server & Agent Skills 扫描：14 大风险类别（MCP01–MCP10 + 3 补充），支持源码目录/远程 URL，无需跑实例；输出 SARIF 2.1.0（可直接进 GitHub Code Scanning/VS Code） |
| **agent-scan** | 多 Agent 自动化扫描框架：评估 AI agent 工作流安全（OWASP Top 10 for Agentic Apps），支持 Dify/Coze 平台 |
| **AI infra 扫描** | 识别 100+ AI 框架组件指纹，覆盖 2,000+ CVE：Ollama、ComfyUI、vLLM、n8n、Triton Inference Server 等 |
| **Jailbreak 评估** | 4 种多轮越狱攻击（Few-Shot、PAIR、GOAT 等）自动化评估 |
| **ClawScan** | **OpenClaw Security Scan**——针对 OpenClaw 生态的安全扫描（凭据泄漏等） |
| **SkillTrustBench** | Agent Skill 可信度基准 + AI 安全技能市场 |

### mcp-scan 的 MCP 风险分类（MCP01–MCP10 + 3）

| 规则 | 风险 |
|:--|:--|
| MCP01 | Token & Secret 暴露 |
| MCP02 | 权限提升 / 越权（工具权限定义过宽） |
| MCP03 | 工具投毒（合法工具注入恶意逻辑） |
| MCP04 | 供应链攻击（恶意第三方 server） |
| MCP05 | 命令注入与执行 |
| MCP06 | 提示注入劫持模型 |
| MCP07 | 认证授权缺失 |
| MCP08 | 审计/遥测缺失（调用日志可篡改） |
| MCP09 | Shadow MCP Server（未授权实例） |
| MCP10 | 上下文注入与过度共享 |
| +3 | 名称混淆攻击 / Rug Pull（信任后改行为）/ 工具阴影（同名覆盖） |

### 红队模块（redteam/）

- 三 LLM 角色：Attacker（生成攻击）→ Target Runner（源码分析+LLM 模拟响应，不启真实进程）→ Evaluator（on_topic / score 1-10 / is_successful）
- 两种攻击策略：**Crescendo**（渐进升级：建立信任→试边界→升级→攻击）与 **TAP**（树状攻击+剪枝：分支变体→on_topic 过滤→top-k 剪枝→继续扩展）
- 攻击目标对齐 OWASP Agentic Top 10：数据窃取/间接提示注入/SSRF via Agent/RCE via Tool/权限提升/工具投毒
- Agent Skill 一致性审计：SKILL.md 描述 vs scripts 实现（Intent Alignment）、隐藏行为检测、输出格式校验

## 💎 可借鉴点（对 sora 工作流）

1. **第三方 skills 安装前的安全体检**：sora 大量安装外部 GitHub skills（external-skill-installation、skill-vetter、security skills）——A.I.G 的 skill-scan/mcp-scan 可做成「装前扫描」门禁：SKILL.md 与脚本一致性审计 + 高风险模式预扫（curl|bash、云 metadata、凭据窃取）正是 skill-vetter 的机械化升级。**落地建议**：评估 skill-scan CLI 直接纳入 skill 安装流水线。
2. **MCP server 风险分类表可直接进知识库**：MCP01–MCP10 + 名称混淆/Rug Pull/工具阴影——这是审查 MCP 的现成 checklist（对照 code-review-graph MCP、jlcmcp 等已装 MCP 自查）。
3. **Crescendo + TAP 红队方法论**：多轮越狱/攻击评估的两套策略（渐进升级 vs 树状+剪枝）可复用到任何 agent 安全测试（如墨题反作弊检测的授权测试场景）。
4. **OpenClaw 生态安全**：ClawScan 直接面向 OpenClaw——sora 的 workspace 是 OpenClaw 遗产，可用它做一次本机生态体检（只扫本地，属内部动作，大胆做）。

## 安装 / 验证命令

```bash
# mcp-scan 独立 CLI（单阶段快速模式，~3x 快）
git clone https://github.com/Tencent/AI-Infra-Guard && cd AI-Infra-Guard/mcp-scan
pip install -r requirements.txt
python main.py --repo ./myproject -o results.json   # SARIF 2.1.0
# 或接入 AIG Web 平台做三阶段交互扫描（信息收集→代码审计→漏洞复核）
# 平台提供任务创建 API：AI infra scan / MCP Server scan / Jailbreak eval
```

## 总结评价表

| 维度 | 评价 |
|:--|:--|
| 技术含金量 | ★★★★★ 覆盖 MCP/Skill/Agent/Infra 四层，SARIF 标准输出，工程完整 |
| 值得安装 | 🟡 skill-scan/mcp-scan 值得装进 skill 安装门禁；全平台部署看需求 |
| 趋势判断 | AI 安全体检工具化是确定方向（MCP 生态爆发 → 供应链风险同步爆发）；腾讯连续押注（WeKnora→A.I.G） |
| 风险 | 6k★ 相对新，规则覆盖面持续演进；扫描结果是辅助，仍需人工复核高危项 |

---
> 🗺️ 属于 [[MOC-Security]] · [[MOC-GitHub]] · 周报 [[GitHub-Weekly-2026-09-20|W39]]
