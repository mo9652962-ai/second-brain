---
aliases:
  - trending-2026-08-05-2
tags:
  - github-trending
  - research
  - cad
  - skills
  - file-transfer
  - agent-security
created: 2026-08-05
updated: 2026-08-05
status: adopted
domain: research
---

# GitHub Trending 研究 — 2026-08-05（第二次，新项目）

> 承接 08-05 第一次热榜研究（pdf-inspector/Agent-Reach/TencentDB/AirLLM/reverse-skill 已评估）
> 本次重点：**4 个与 sora 业务/体系直接相关的新项目**

---

## 🥇 1. earthtojake/text-to-cad（12.5k★）— PCB/机械设计业务直接相关

| 项目 |  |
|:-----|:--|
| **地址** | https://github.com/earthtojake/text-to-cad |
| **协议** | MIT |
| **作用** | CAD/机器人/硬件设计 Agent 技能库——自然语言 → STEP/STL/3MF 3D 模型 |

### 技能组成

| 技能 | 作用 |
|:-----|:-----|
| **CAD** | 自然语言/图片 → 参数化 CAD 模型，**STEP 为主输出**（可导出 STL/3MF/GLB） |
| CAD Viewer | 浏览器本地预览 CAD/G-code/机器人文件 |
| step.parts | 找现成 STEP 标准件（螺丝/轴承/电机/连接器） |
| DXF | 2D DXF 图纸（型材/模板/垫片/切割布局） |
| URDF/SDF/SRDF | 机器人结构描述文件 |

### 对 sora 的价值（⭐ 直接相关）

1. **PCB/机械设计接单**：闲鱼 PCB 单的 3D 外壳/支架初稿，用 text-to-cad 快速出 STEP → EasyEDA/JLC 继续加工
2. **蓝海工程自动化定位**：与 PCB 接单、CAD 技能树完全同向
3. **社区已接 Hermes**：`npx agent-skills-cli add earthtojake/text-to-cad` + 软链接映射即可用
4. **benchmarks**：10 个基准任务（L 支架/阶梯轴/电子外壳/行星齿轮）——可验证 Hermes 集成效果

### 落地评估

| 场景 | 价值 | 行动 |
|:-----|:----:|:-----|
| 3D 外壳/支架初稿（PCB 单配套） | 高 | 🟡 装技能库，用 Hermes 软链接接入，跑 1 个 benchmark 验证 |
| 标准件查找（step.parts） | 中 | 🟡 接单时找螺丝/轴承规格 |
| DXF 切割布局 | 中 | 🟡 激光切割/面板开孔 |

---

## 🥈 2. obra/superpowers（267k★）— AI 技能框架 + SDD 方法论

| 项目 |  |
|:-----|:--|
| **地址** | https://github.com/obra/superpowers |
| **协议** | MIT（v6.2.0，2026-07-24） |
| **作用** | Agent 技能框架 + 软件开发方法论（SDD），被大量团队当 AI 开发流程模板 |

### 核心：Skill-Driven Development（SDD）

```
Brainstorm（需求对齐）→ Plan（设计图）→ 独立分支环境
→ 大任务拆解成 2-5 分钟小步骤 → 每步先写测试 → 小功能完成
→ Fix Loop（R≤3 resume implementer / R≥4 换手）
```

**14 个技能 + 7 步工作流 + 3 条铁律**（社区解读确认）：
- 斜杠命令体系（`/superpowers:brainstorm` 等）
- 计划作用域工作区（plan-scoped workspace）
- 修复循环（fix-loop）设计

### 与 Hermes 体系对比

| 维度 | superpowers | Hermes/Second Brain |
|:-----|:-----------|:-------------------|
| 技能框架 | 14 个技能包 | 200+ skills（含自建） |
| 方法论 | SDD（brainstorm→plan→test→fix） | engineering-workflow（Grill→建模→TDD→Code Review） |
| 流程规范 | 7 步工作流 | 七大自举系统 |
| 多客户端 | Claude/Codex/Cursor/Kimi | Hermes 全平台 |

**同构验证**：sora 的 engineering-workflow 与 superpowers 的 SDD 思想一致（需求对齐→设计→TDD→评审），行业验证了这个模式。

### 落地评估

| 场景 | 价值 | 行动 |
|:-----|:----:|:-----|
| SDD 方法论借鉴 | 中 | 🟢 对照 engineering-workflow，看是否补「fix-loop 换手」机制 |
| 技能组织方式 | 中 | 🟢 学习其 marketplace 多客户端分发（.claude-plugin/.agents/plugins） |

---

## 🥉 3. schollz/croc（39.3k★）— SimSync 存档同步借鉴

| 项目 |  |
|:-----|:--|
| **地址** | https://github.com/schollz/croc |
| **协议** | MIT |
| **作用** | 任意两台电脑端到端加密文件传输（CLI） |

### 特性（与 SimSync 存档同步对比）

| 特性 | croc | SimSync 现状 |
|:-----|:-----|:------------|
| 端到端加密 | PAKE（口令认证密钥协商） | HMAC + CRC（无加密） |
| 传输模式 | relay 中转 + P2P | 直接 TCP |
| 断点续传 | ✅ | ❌ 无 |
| 跨平台 | Win/Linux/Mac/浏览器 | Win 启动器 |
| 端口转发 | 不需要（relay） | LAN 直连 |

### 对 sora 的价值

1. **SimSync 存档同步改进参考**：croc 的 PAKE 思路（房间码→密钥协商）可借鉴——我们房间码只做身份验证，croc 用房间码派生加密密钥
2. **跨网传输兜底**：SimSync 跨公网时 UPnP 失败，可考虑 croc 式中继方案
3. **Web 传输**：浏览器端可收文件（getcroc.com）——给朋友传存档/素材的新路径

### 落地评估

| 场景 | 价值 | 行动 |
|:-----|:----:|:-----|
| SimSync 存档加密升级 | 中 | 🟡 研究 PAKE 协议，考虑房间码→HKDF 派生密钥（已有 HKDF 基础） |
| 跨网文件分发 | 中 | 🟢 装 croc，朋友传大文件（mod zip）替代微信 |
| 断点续传 | 低 | 🟢 存档大时考虑（当前 30MB 内不需要） |

---

## 4. uber/ADR（808★ 新）— Agent 安全检测响应

| 项目 |  |
|:-----|:--|
| **地址** | https://github.com/uber/ADR |
| **协议** | Apache 2.0 |
| **作用** | 企业级 AI Agent 安全（可观测性 + 安全基准 + 威胁检测），**Uber 内部生产部署 + MLSys 2026** |

### 四大能力

1. **Observability**：采集 Claude Code/Cursor/Codex 等 7+ 工具遥测（macOS/Linux/Windows）
2. **Benchmark**：ADR-Bench 300+ 任务、133 MCP 服务器、17 种 agent 攻击技术
3. **Detection**：双层架构（高召回 triage + 深度 agentic 推理）
4. **Prevention**：未开源（企业版）

### 与 sora 的关联

- **agent 安全审计**：security 技能的 ai-agent-security-audit 可借鉴 ADR 的可观测性采集模式
- **确定性验证哨兵**（今天刚落地）：ADR 的 Detection 思路（遥测→检测）与 2608.02464 论文一致——行业三重验证（Uber 生产 + 论文 + 我们的实践）

### 落地评估

| 场景 | 价值 | 行动 |
|:-----|:----:|:-----|
| Hermes 遥测审计 | 低 | 🟢 收藏，参考 Sensor 架构（agent 工具调用遥测标准化） |
| 安全基准测试 | 低 | 🟢 收藏 ADR-Bench（prompt injection 场景） |

---

## 简评（其余）

| 项目 | 星级 | 简评 |
|:-----|:----:|:-----|
| microsoft/generative-ai-for-beginners | 116k | 21 课 AI 入门——学习资源，🟢 收藏 |
| livekit/agents | 12.3k | 实时语音 Agent——sora 无语音业务，🟢 收藏 |
| usekaneo/kaneo | 7.2k | 极简项目管理（Linear/Jira 替代）——自托管，🟢 参考 |
| deno | 108k | JS/TS 运行时——不相关，🟢 路过 |
| Pumpkin (MC 服务器) | 10.4k | Rust MC 服务器——与 SimSync 游戏网络同领域，🟢 参考架构（高并发/插件系统） |
| Automattic/harper | 14.2k | 离线英语语法检查（Rust）——论文润色英文可用，🟡 可选装 |
| RuView | 87.8k | WiFi 人体感知——**疑点**（star 数与 beta 状态不匹配，警惕刷星） |
| worldmonitor | 78.7k | 全球情报仪表盘——信息聚合，🟢 参考 |
| likec4 | 5.3k | 架构图代码化（C4 Model）——SimSync 文档配图可用，🟢 |
| text-to-cad 已评估 | — | 见 🥇 |
| tailwindcss/angular/webpack | — | 前端基建——不相关 |
| witr | 1.8万 | 进程/端口溯源工具——排障有用，🟢 |
| rustfs | 30.6k | Rust S3 存储——不相关 |
| runa | 新 | Rust 游戏引擎——参考 |
| spdlog | 29.4k | C++ 日志——不相关 |
| fjall | 2.2k | Rust KV 存储——不相关 |

---

## 综合评估表

| 项目 | 相关模块 | 可落地性 | 优先级 |
|:-----|:---------|:--------:|:------:|
| text-to-cad | PCB 接单/蓝海工程自动化 | 高 | 🟡 本周评估安装 |
| superpowers | engineering-workflow | 中 | 🟢 对照补 fix-loop |
| croc | SimSync 存档同步 | 中 | 🟡 研究 PAKE 加密 |
| uber/ADR | agent 安全 | 低 | 🟢 收藏 |

## 落地行动清单

### 🟡 本周（1-2 天）
- [x] 装 text-to-cad 技能库（软链接映射给 Hermes），跑 1 个 benchmark 验证（L 支架）✅ 2026-08-05 已装（hermes skills/text-to-cad + text2cad-cad）+ L 支架 benchmark 5/5
- [ ] 研究 croc PAKE → SimSync 房间码派生加密密钥（已有 HKDF 基础，升级成本低）

### 🟢 收藏
- [ ] superpowers SDD 对照 engineering-workflow（fix-loop 换手机制）
- [ ] uber/ADR Sensor 遥测架构（agent 工具调用审计）
- [ ] Pumpkin MC 服务器架构（高并发/插件系统参考）
- [ ] likec4（SimSync 文档配图）

---

*来源：GitHub Trending 第二次（sora 分享）+ web_search 交叉验证 | 状态：adopted*
