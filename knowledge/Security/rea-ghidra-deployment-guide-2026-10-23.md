---
title: REA + Ghidra 逆向环境部署与实战指南（Windows）
date: 2026-10-23
tags: [reverse-engineering, rea, ghidra, mcp, windows, deployment]
status: 已部署验证
machine: Windows 11 x64 / Node 26.7.0 / JDK 21.0.2 / 16 核 / 15.6GB RAM
---

# REA + Ghidra 逆向环境部署与实战指南

> **本机状态：已部署并跑通真实反编译。**
> 安装位置 `D:\tools\rea` + `D:\tools\ghidra_12.1.4_PUBLIC`，全程未污染全局环境。

## 0. 一句话结论

| 项 | 结果 |
|:---|:---|
| 部署方式 | **独立目录 + CLI 优先，不注册全局 MCP** |
| Ghidra 版本 | **必须 12.1.x**（REA 源码硬编码 `SUPPORTED_GHIDRA_VERSION = "12.1.4"`，12.2 会被拒） |
| REA 版本 | 钉 6.7.0（一周 4 个大版本 / 23 项 breaking） |
| doctor 结果 | ghidra provider **9/9 检查全绿，available=true** |
| 真实反编译 | ✅ 1758 个函数、伪代码 `confidence=observed` |
| 单次分析耗时 | **54 秒**（冷热一致，无缓存） |

---

## 1. 为什么不用 `npx rea-agents setup`

`setup` 一条命令很香，但它会：

1. 往 `AppData\Local\hermes\config.yaml` 写 MCP 注册
2. 注册 **207 个工具 / `tools/list` 3.16MB ≈ 79 万 tokens**

我实测过：默认档 3,158,358 字节；`REA_MCP_INPUT_SCHEMA_PROFILE=compact` 只降到 2,576,431（-18%）；**两个 profile 全开**（`compact` + `REA_MCP_OUTPUT_SCHEMA_PROFILE=off`）才能降到 **219,226 字节 ≈ 54,807 tokens**。

即便如此 5.5 万 token 的工具清单也够呛。而社区 `leanrea` 的对照 benchmark 说明问题：

| 方案 | 耗时 | 成本 | tokens | 得分 |
|:---|:---|:---|:---|:---|
| 原版 REA（207 工具 MCP） | 627s | $3.36 | 5.93M | 75/75 |
| leanrea（8KB skill + 纯 CLI） | **388s** | **$2.17** | **2.40M** | 74/75 |

**快 38%、省 35%、token 少 60%，准确率几乎相同。** 结论很清楚：CLI 优先。

---

## 2. 部署步骤（已脚本化）

### 一键安装

```bash
bash /d/tools/rea/install.sh
```

脚本做五件事：前置检查 → 装 REA 到独立目录 → 装 Ghidra → 校验三件套 → doctor 全绿验证。

### 手动步骤（想搞清楚每一步）

**Step 1 — 前置检查**

```bash
node -v          # 需 22.19+ / 24.11+ / 26+
ls $JDK_HOME/bin/javac.exe   # 必须是完整 JDK，不能是 JRE
```

JDK 判定标准（缺一不可）：
- `bin/java.exe` + `bin/javac.exe` 都在
- `java --list-modules | grep jdk.compiler` 有输出
- `os.arch = amd64`（64 位）

**Step 2 — 装 REA（独立目录）**

```bash
mkdir -p /d/tools/rea && cd /d/tools/rea
npm init -y
npm install rea-agents@6.7.0 --no-audit --no-fund
# REA_ENTRY = D:/tools/rea/node_modules/rea-agents/scripts/rea.mjs
```

**Step 3 — 装 Ghidra 12.1.4**

```bash
cd /d/tools
curl -x http://127.0.0.1:7890 -L -C - -o ghidra_12.1.4.zip \
  "https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_12.1.4_build/ghidra_12.1.4_PUBLIC_20260921.zip"
unzip -t ghidra_12.1.4.zip    # 必须先验完整性
unzip -q ghidra_12.1.4.zip
```

**速度坑**：直连约 50KB/s（要 3 小时）；走 FlClash 代理 7890 到 700KB/s~2.4MB/s（**13 分钟**）。差 17 倍。

**Step 4 — 三件套校验**（缺一个 REA 就报 `provider_unavailable`）

```bash
G=D:/tools/ghidra_12.1.4_PUBLIC
test -f "$G/support/analyzeHeadless.bat"                                    # headless 启动器
test -f "$G/Ghidra/application.properties"                                  # 版本元数据
test -f "$G/Ghidra/Features/Decompiler/os/win_x86_64/decompile.exe"         # 原生反编译器
```

**Step 5 — 环境变量 + doctor**

```bash
source /d/tools/rea/env.sh
rea doctor --provider ghidra --format json
```

---

## 3. env.sh 关键变量（每个都有理由）

| 变量 | 值 | 为什么 |
|:---|:---|:---|
| `GHIDRA_INSTALL_DIR` | `D:/tools/ghidra_12.1.4_PUBLIC` | 必须是含 `support/` 和 `Ghidra/` 的内层目录 |
| `JAVA_HOME` | `C:/Users/31954/jdk21` | REA 也会自动探测，但显式指定避免歧义 |
| `REA_ANALYSIS_PROVIDER` | `ghidra` | 避免 `auto` 在多引擎时选错 |
| `GHIDRA_HEADLESS_MAXMEM` | `2G` | 本机 15.6GB 但常只剩 2GB 可用，别调大 |
| `REA_GHIDRA_STARTUP_TIMEOUT_MS` | `900000` | 默认 330s 对 1.6MB Go 二进制不够稳 |
| `REA_MCP_INPUT_SCHEMA_PROFILE` | `compact` | 只在接 MCP 时才生效，预留 |
| `REA_MCP_OUTPUT_SCHEMA_PROFILE` | `off` | 砍掉 74.5% 的 schema 体积，预留 |

---

## 4. 实战工作流（真实跑通的命令）

### 4.1 完整分析

```bash
rea analyze "D:/tools/targets/calc.exe" --provider ghidra --format json \
  --filter-output evidence_id
# → "ev_1db3d5d7025bc7fe142d26b9a09d70d4be06f30f57ea27f85b25c27cbe665081"
```

**必须 `--filter-output`**：完整 JSON 是 MB 级，只取 evidence_id 是 414 token。

### 4.2 找函数

```bash
# 按名字搜（符号表里有名字时）
rea search <path> "computePan" --provider ghidra --format json
# → [{"address":"0x1400f3711","value":"main.computePan"}]

# 列全部函数（1758 个）
rea search <path> "." --kind procedures --mode regex --provider ghidra --format json
```

### 4.3 反编译

```bash
rea function <path> 0x140001080 --provider ghidra --format json
```

返回 16 个字段：`pseudocode` / `assembly` / `callers` / `callees` / `incoming_references` / `basic_blocks` / `native_value_flow` / `facet_availability` / `limitations` 等。

`confidence: observed` + `authority: shipped-artifact` —— 这是"实测到的事实"级别，不是猜测。

### 4.4 Go / Rust 二进制元数据（不需要 Ghidra）

```bash
rea inspect-go-binary <path> --format json     # 2.4 秒，读到 go1.26.6 + 模块清单
rea inspect-rust-binary <path> --format json   # cargo-auditable 依赖树
```

### 4.5 Electron / JavaScript（不需要 Ghidra）

```bash
rea analyze-javascript-application <app.asar> --format json \
  --filter-output normalized_result.summary
```

---

## 5. 踩过的坑（全部实测）

| # | 坑 | 现象 | 解决 |
|:---|:---|:---|:---|
| 1 | **Ghidra 12.2 不行** | doctor 报 `unsupported_version` | 降到 12.1.4（源码硬编码） |
| 2 | **`stdin is not a tty`** | 看起来像失败 | 是无害 stderr 提示；加 `< /dev/null` 或忽略 |
| 3 | **地址 ≠ 文件偏移** | `File offset 0x1400f3711 has no loaded source mapping` | 用分析地址（image_base + 偏移），不是文件偏移 |
| 4 | **符号名不能直接反编译** | `Unknown Ghidra procedure name: main.computePan` | 先 `search --kind procedures` 拿地址，再 `function <addr>` |
| 5 | **Go 符号丢失** | 1758 个函数全叫 `FUN_xxx` | Go 剥离符号后无解；靠 `inspect-go-binary` 补元数据 |
| 6 | **.NET 64MB 预算墙** | `System.dll` 返回 `unavailable` / 0 方法 | 用 `--type <全限定类名>` 局部取；实测 0 → 78 方法 |
| 7 | **完整 JSON 爆炸** | 1.2KB fixture 输出 439KB ≈ 12.7 万 token | 永远 `--filter-output`；`--token-limit` 与结构化输出互斥 |
| 8 | **无缓存** | 第二次分析仍 54 秒 | REA 每次重新导入；大目标要有耐心 |
| 9 | **默认 330s 超时** | 稍大二进制 `provider_timeout` | 设 `REA_GHIDRA_STARTUP_TIMEOUT_MS=900000` |
| 10 | **内存吃紧** | 本机常只剩 2GB | `GHIDRA_HEADLESS_MAXMEM=2G`，别贪大 |

### 坑 6 的完整证据

```bash
# System.Core.dll (1.5MB) → coverage: complete, methods: 8293
# System.dll (3.4MB)      → coverage: unavailable, methods: 0
#   原因: "Managed metadata exceeds the 67108864 byte representation budget"
# 绕法:
rea inspect-managed-members System.dll --type "System.Net.WebRequest" --format json
# → coverage: complete, methods: 78   ✅
```

源码位置：`dist/cli-runtime/ManagedSnapshot-CPE9C3OD.js:55` → `MAX_METADATA_REPRESENTATION_BYTES = 64 * 1024 * 1024`

注意：这是**中间表示估算预算**，不是文件大小。1.48MB 的 `System.Core.dll` 能过，3.4MB 的 `System.dll` 过不了。

---

## 6. 能力边界（Windows P0，必须知道）

REA 在 Windows 上的 Ghidra 通道是**实验性只读 P0 边界**：

| 能力 | Windows P0 | Linux/macOS |
|:---|:---:|:---:|
| 原生 x86/x86-64 PE 应用 | ✅ | ✅ |
| DLL | ✅ | ✅ |
| **重命名 / 注释** | ❌ 禁止改数据库 | ✅ |
| no-return 修复 | ❌ 关闭 | ✅ |
| 目标位置 | 仅本地固定 NTFS（UNC/reparse/ADS 全拒） | 任意 |
| .NET 托管 PE | ❌ 走独立 provider | ❌ 走独立 provider |
| ARM64 PE / 非 PE | ❌ | ✅ 部分 |
| 运行时进程捕获 | ❌ 需 Linux/WSL | ✅ |

**想重命名/注释就上 WSL2**（本机已装 Ubuntu-22.04，可作备选路线）。

---

## 7. 分析质量：好在哪里，差在哪里

### 好

- 伪代码带 `confidence` / `authority` / `limitations` 三元标注
- `callers` / `callees` 只含已解析函数，不瞎猜
- 计算调用明确标 `unknown`，不编造
- 1758 函数全解析，0 失败
- 证据链可回溯（每个结论挂 evidence_id）

### 差

| 缺口 | 实测数据 |
|:---|:---|
| Electron 窗口数 | 真值 3 → 只报 **1** |
| `nodeIntegration` | 真值 1 → **0 次出现** |
| IPC reply-back | 真值 2 → **0** |
| 大应用 coverage | 4.5MB asar → 10 万节点撞顶，标 `partial/truncated` |

**「没报 ≠ 没有」**。做安全审计时把 REA 的空缺当"不存在"，会漏掉 `nodeIntegration: true` 这种高危配置。

---

## 8. 推荐工作流（组合拳）

```
① 分诊（不需要引擎，秒级）
   rea inspect-go-binary / inspect-rust-binary / inspect-artifact
   → 判断语言、依赖、打包方式

② 静态结构（不需要引擎）
   rea analyze-javascript-application <asar> --filter-output normalized_result.summary
   → IPC 通道、模块图、preload 边界

③ 原生深挖（需要 Ghidra，54s+/次）
   rea search <path> "." --kind procedures → 拿地址
   rea function <path> <addr> → 伪代码 + 汇编 + 调用关系

④ 补足 REA 的缺口
   - 动态调试：x64dbg（REA 无动态调试能力）
   - Electron 安全：electron-audit / Electronegativity
   - .NET 大程序集：dnSpy / ILSpy
   - 反混淆：de4dot（REA 明确不做）

⑤ 验证闭环
   输入输出对比 → 行为一致性 → 代码级（编译后字节比对）
```

---

## 9. 合规红线

- 只分析**自己拥有或获权检查**的软件
- REA 明确不支持破解 DRM、复制专有代码
- 本地分析 ≠ 数据不出本地：结论仍会进模型厂商
- 拿到客户/NDA 软件时，这一步就可能违约

---

## 10. 文件清单

| 路径 | 内容 |
|:---|:---|
| `D:\tools\rea\` | REA 6.7.0 独立安装（147MB） |
| `D:\tools\rea\install.sh` | 一键安装脚本 |
| `D:\tools\rea\env.sh` | 环境变量 + `rea` / `reaq` 便捷函数 |
| `D:\tools\ghidra_12.1.4_PUBLIC\` | Ghidra 12.1.4（约 1.5GB 解压后） |
| `D:\tools\ghidra_12.1.4.zip` | 原始压缩包（569MB，可删） |
| `D:\tools\targets\calc.exe` | 验证用 Go PE（含已知算法 ground truth） |
| `D:\tools\targets\calc.go` | 对应源码 |

## 参考

- REA 仓库：https://github.com/morluto/rea
- Ghidra 12.1.4：https://github.com/NationalSecurityAgency/ghidra/releases/tag/Ghidra_12.1.4_build
- 前次审计：`rea-mcp-reverse-engineering-audit-2026-10-23.md`
