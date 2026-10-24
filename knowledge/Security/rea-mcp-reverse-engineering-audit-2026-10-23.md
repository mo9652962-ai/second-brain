---
title: REA (Reverse Engineer Anything) 实证审计
date: 2026-10-23
tags: [reverse-engineering, mcp, agent, audit, rea]
status: 已实证
verdict: 可用但别当依赖
---

# REA 实证审计（rea-agents 6.7.0）

> 一句话结论：**REA 是套在 Ghidra/IDA/Hopper 外面的「证据契约层」，不是逆向引擎。**
> 真实价值在证据规范（观察/推断/未知三分）与统一接口；真实风险在上下文成本与覆盖缺口。

## 1. 仓库基本面（2026-10-23 API 实测）

| 指标 | 数值 |
|:---|:---|
| Stars | 371,158 |
| Forks | 92,950 |
| Watchers（真订阅） | 1,317 |
| watcher/star | **0.355%** |
| 创建 / 最后 push | 2026-04-14 / 2026-10-23 |
| 语言 / 许可 | TypeScript / MIT |
| 核心提交 | morluto 2,413；前 3 人占非 bot 提交 90%+ |

watcher/star 横向对照：vscode 1.83% · next.js 1.13% · claude-code 0.60% · openclaw 0.43% · **REA 0.355%（最低）**。
→ 典型「路过点赞」曲线，star 数不代表使用深度。

**fork 批量证据**：抽样最新 100 个 fork，`pushed_at` 落在同一分钟的最多 12 个；仓库 size 全部是 102042(85)/102797(14) 两个值 —— 零改动纯 fork。

npm 下载：周 415,576 / 月 549,553（其中 76% 集中在最近一周）。

## 2. 上下文成本（最致命的一项，实测）

| 项 | 数值 |
|:---|:---|
| MCP 工具数 | **207** |
| `tools/list` 响应 | 3,158,358 字节 ≈ **789,590 tokens** |
| ├ outputSchema | 2,354,101 字节（74.5%） |
| ├ inputSchema | 667,850 字节（21.1%） |
| └ name+description | 102,412 字节（3.2%） |
| compact profile（`REA_MCP_INPUT_SCHEMA_PROFILE=compact`） | 2,576,431 字节 ≈ 644,108 tokens（仅降 18%） |
| 标记 readOnlyHint 的工具 | 5 / 207 |

79 万 token 的工具清单大于任何模型上下文窗口。服务端不做 deferred loading / tool_search，全靠客户端兜底。
→ **全局注册进 Hermes 会直接挤爆上下文，绝不能装。**

## 3. 能力实测（本机 Windows 11 + Node 26.7.0 + JDK 21，无 Ghidra/IDA/Hopper/JADX）

| 能力 | 结果 | 耗时 | 备注 |
|:---|:---|:---|:---|
| 静态 JS/Electron（自建 4 文件 fixture，1.2KB） | ✅ | 1.8s | 输出 439KB |
| 静态 JS/Electron（真 app.asar 4.5MB，778 文件/678 解析） | ✅ | 2m34s | 输出 **216MB** JSON |
| Go 二进制内嵌依赖（`inspect-go-binary`） | ✅ | 2.4s | 读到 go1.26.6 + 完整模块清单 + h1 哈希 |
| 通用 artifact 清单（`inspect-artifact`） | ✅ | 2.4s | 7KB |
| PE 二进制 inspect | ❌ | - | `provider_unavailable`（需 Ghidra/IDA/Hopper） |
| 反编译（decompile） | ❌ | - | 同上 |
| PE 签名（inspect-signature） | ❌ | - | 仅 macOS（native-macos provider） |

真 app.asar 分析质量：8132 findings、560 模块、1,770,630 AST 节点、0 parse failures、
IPC 32/32 配对成功、37 条 sender 校验观察 —— **静态 JS 这一路是真能干活**。
但 `semantic_graph` 触顶 100,000 节点上限，coverage 标 `partial/truncated`。

## 4. 覆盖缺口（自建 ground-truth 复现，关键发现）

自建 3 文件 Electron fixture，已知真值：**3 个 BrowserWindow（1 个 `nodeIntegration:true`）、2 处 reply-back、6 个 channel**。

| 项 | 真值 | REA 报出 |
|:---|:---|:---|
| BrowserWindow 数 | 3 | **1** |
| `nodeIntegration` 命中 | 1 | **0 次出现** |
| reply-back（`sender.send` / `webContents.send`） | 2 | **0**（renderer_listeners=0） |
| channel | 6 | 4 |
| IPC 操作 | - | 7 |

与 SystemDesign Academy 对开源 Electron 应用的独立测试完全同型（1/8 窗口、0/8 reply-back、0/4 nodeIntegration）。

> **「没报 ≠ 没有」。** 做安全审计时把 REA 的空缺当「不存在」，会直接漏掉 `nodeIntegration:true` 这类高危配置。

## 5. 输出成本控制（唯一实用姿势）

| 调用方式 | token 成本 |
|:---|:---|
| 完整 JSON（1.2KB fixture） | 126,827 |
| `--filter-output normalized_result.summary` | **202** |

`--token-limit` 与结构化输出互斥（报 `UNSUPPORTED_OUTPUT_COMBINATION`），只能靠 `--filter-output` 或命令级分页。
→ 正确用法：CLI + 精确 filter，或 `export_evidence_bundle` 落盘后按需读。

## 6. 风险清单

| 风险 | 说明 |
|:---|:---|
| 版本激进 | 一周 4 个大版本、23 项 breaking change；minor 当 major 用，无向后兼容承诺。证据存档保质期以天计 |
| Bus factor ≈ 3 | 核心作者单人 2,413 提交；review 是唯一吞吐瓶颈 |
| 本地 ≠ 沙箱 | 分析在本地跑，但结论仍进模型厂商；不给未授权样本 |
| 安装器权限 | Linux 上 Hopper 安装走系统包管理器（root），校验仅 SHA-1 |
| 法律 | 拆了洁净室隔离墙，同一 Agent 既读反编译又写新代码（IP laundering 争议）；多数商业 EULA 禁反编译 |
| 冒名风险 | 已出现同名仿冒仓库与代币，只从 `morluto/rea` / `rea-agents` npm 官方渠道取 |

## 7. 定位与建议

**该用**：有具体问题要回答的窄任务 —— 某函数的计算规则、某 Electron 应用的 IPC 链路、某 Go/Rust 二进制的依赖构成、版本间行为 diff。
**不该用**：整应用复刻（官方自己声明不做）、安全审计的完整性判断、需要动态调试（VMP/反调试/内核）的目标。

落地配置建议：

1. **不注册全局 MCP**（207 工具 79 万 token）。用 CLI 按需调用。
2. 原生逆向需要引擎：装 **Ghidra 12.2**（569MB，免费）+ 设 `GHIDRA_INSTALL_DIR`。本机 JDK 21 已被 REA 自动识别，Java 侧就绪。
3. 输出永远走 `--filter-output` 或落盘，别把原始 JSON 喂模型。
4. 把「观察/推断/未知」三分法抄进自己的分析流程 —— 这是 REA 最值得借鉴的部分，与证据契约无关。

## 参考

- 仓库：https://github.com/morluto/rea （npm `rea-agents`）
- 官方站：https://rea.tools
- 独立测试：SystemDesign Academy（Electron 覆盖缺口）、SMF Clearinghouse（安装与安全审视）、SoloSoft（token 账单实测）
