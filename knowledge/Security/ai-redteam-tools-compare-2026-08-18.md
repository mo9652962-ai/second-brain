# AI 红队工作台全景对比（2026-08-18 研究）

> 覆盖：主流 AI 渗透/红队工具形态 + 选型决策树 + 对 sora 工具链的定位

## 一、全景图谱（10 个主流工具）

| 工具 | 形态 | 核心能力 | 适合 |
|:---|:---|:---|:---|
| **PentestGPT v2** | 推理框架 | PTT 任务树（状态持久）+ LeadTester/JuniorTester/Parser 三模块 | 新手/学习 |
| **HexStrike AI** | 多 Agent | 研究/编码/基建三角色并行 + 失败复盘 | 小团队 |
| **Strix** | 自主 Agent | 动态决策 + 覆盖广 | Bug Bounty |
| **CAI 框架** | 可组装平台 | 300+ 模型 + 自定义 Agent | 企业定制 |
| **AutoRedTeam** | 全栈框架 | 132 MCP 工具 + 26 检测器 + MCTS 规划 + C2 + 1980 测试 | 深度红队 |
| **ovogogogo** | 多 Agent 引擎 | 17 Agent 并行 + 22 万 PoC 语义检索 + ShellSession + Critic Loop | 自动化攻击链 |
| **FofaMap v2** | 资产测绘智能体 | FOFA 查询自我反思调优 + MCP 支持 | 资产发现 |
| **Deep Hat** | 专用 LLM | 无审查红队模型（本地部署，数据不出门）| Payload 构造 |
| **蛙池AI** | 白帽工作台 | 对话挖洞 + 智能体 + 报告（漏洞盒子生态）| 漏洞盒子用户 |
| **DRT** | AI 红队平台 | DeepSeek + Hermes Agent + 股权/供应链分析 | 红队打点 |

## 二、2026 三大技术趋势

```
① MCP 协议普及: 工具提供 MCP Server → AI 客户端直接调度
   (AutoRedTeam 132 工具 / FofaMap / PentestGPT 均支持)
② 多 Agent 并行: 研究/编码/执行分工 + 失败复盘
   (HexStrike 3 Agent / ovogogogo 17 Agent)
③ 状态管理: 任务树/知识图谱防上下文丢失
   (PentestGPT PTT 树 / AutoRedTeam SQLite 图谱)
```

## 三、实战战绩参考

| 工具 | 战绩 |
|:---|:---|
| HexStrike | 金融系统渗透 2 周 → 3 天（N+1 注入/越权/XSS）|
| Strix | 电商 4 小时扫 40 端点 → 3 未授权 + 完整 PoC |
| PentestGPT | USENIX Security 2024 顶会；本地 70B 模型推理 ≈ GPT-4 的 70% |
| DRT | FOFA 供应链反查 6 分钟自动完成 |

## 四、选型决策树

```
想玩玩感受    → PentestGPT
开箱即用      → HexStrike AI
企业定制      → CAI 框架
Bug Bounty    → Strix
求稳怕事      → Nebula（人机协同）
资产测绘增强  → FofaMap v2
```

## 五、sora 工具链定位（关键结论）

```
已有: Hermes（通用 Agent + 记忆 + 自动化）+ 自研工具链
     + 蛙池AI（漏洞盒子生态）+ DVWA/OneForAll/Burp/unveilr

最优组合 = 人机协同:
  Hermes = 分析大脑（信息收集编排/AI 审计/报告/复核）
  蛙池   = 执行手（自动探测/验证）
  人工   = 逻辑漏洞 + 红线判断

结论: 不需要再装 PentestGPT/Strix 重型框架
      (Hermes + 蛙池 已覆盖 80% 能力)
      唯一值得补: FofaMap v2 (FOFA AI 智能体, 资产发现增强)
```

## 六、MCP 安全测试工具（补充维度）

```
0xClaw: 本地优先 MCP 安全测试（auth/scope/evidence 强）
Promptfoo: MCP server 直接作为目标测试（prompt injection/工具滥用）
garak (NVIDIA): 模型侧探测（基线扫描）
PyRIT (Microsoft): 多轮攻击编排（converter 链）
Inspect AI (UK AISI): 结构化 AI 安全评估
```
