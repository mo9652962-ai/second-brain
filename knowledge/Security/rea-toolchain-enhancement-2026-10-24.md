---
title: REA 工具链增强实录（2026-10-24）：两个真实 bug + PDB 未打通
date: 2026-10-24
tags: [reverse-engineering, rea, ghidra, pdb, symbols, debugging, pitfalls]
status: 增强完成 / PDB 符号链路未打通（已停手）
---

# REA 工具链增强实录

## 结论置顶

| 项目 | 结果 |
|:---|:---|
| 环境变量覆盖 | 13 → 17 个（补 4 个调优项） |
| 符号缓存结构 | ✅ 按 MS 规范重建（index2.txt + pingme.txt + 000Admin/） |
| PDB 符号下载 | ✅ 实测下载 kernel32.pdb 1.01MB，MSF 魔数校验通过 |
| **PDB 符号被 Ghidra 使用** | ❌ **未打通，已停手** |
| 测试断言 | 40 → 48 条（+8 条，含 2 条防回归硬门禁） |
| 发现并修复的真实 bug | **2 个**（都会导致工具链全线瘫痪） |

## 一、两个真实 bug（本轮最大收获）

### Bug 1：`REA_MCP_MAX_RESPONSE_BYTES=8388608` 导致所有命令失败

我按「8MB 应该够用」的直觉配了 8MB，结果**所有 REA 命令返回 `configuration_invalid`**：

```json
{
  "error": "Analysis failed",
  "code": "configuration_invalid",
  "message": "REA configuration is invalid: REA_MCP_MAX_RESPONSE_BYTES: Too small: expected number to be >=10485760."
}
```

**REA 硬性下限是 10485760（10MB）**，源码在 `SupportedClients-DMafjitv.js:45`：

```js
budgetConstraint = `REA_MCP_MAX_RESPONSE_BYTES must be a decimal safe integer at least ${String(MINIMUM_RES...`
```

修正为 `16777216`（16MB）后恢复。

**教训：配置值不能凭直觉，必须查源码里的 schema 约束。**

### Bug 2：`REA_GHIDRA_DISABLED_ANALYZERS` 打挂 Ghidra bridge

我想禁用 DWARF 分析器提速，配了：

```bash
export REA_GHIDRA_DISABLED_ANALYZERS="DWARF,DWARF Exception Analyzer"
```

结果：

```json
{
  "code": "execution_failure",
  "details": {
    "failure_kind": "process",
    "failure_message": "Ghidra exited before bridge startup"
  }
}
```

对比实验：

| 配置 | 结果 |
|:---|:---|
| 不设 `DISABLED_ANALYZERS` | ✅ 1758 函数，`preset=ghidra-default` |
| 设 `DWARF,DWARF Exception Analyzer` | ❌ `Ghidra exited before bridge startup` |

**原因：`DWARF` 不是 Ghidra 12.1.4 的合法分析器名**，或者禁用它会破坏 bridge 初始化。REA 的 schema 只校验字符串格式（字母数字空格点下划线连字符），不校验名字是否真实存在，所以配错了不报配置错，而是跑到 Ghidra 启动阶段才炸。

**处理：默认不启用，env.sh 里注释保留并写明风险。**

## 二、符号缓存结构（已建成）

Ghidra 的 `LocalSymbolStore.create(level=2)` 要求 MS 符号存储规范：

```
D:\Symbols\
├── index2.txt        ← level-2 存储标记
├── pingme.txt        ← MS 约定
├── 000Admin\         ← 管理目录
└── kernel32.pdb\
    └── E8C3A48CAC7EB60D8781D8C10020C44F1\
        └── kernel32.pdb    (1.01 MB)
```

一键脚本：`D:\tools\rea\setup-symbols.sh`

### PDB 下载实测成功

```bash
curl -sL -x http://127.0.0.1:7890 \
  -o "D:/Symbols/kernel32.pdb/E8C3A48CAC7EB60D8781D8C10020C44F1/kernel32.pdb" \
  "https://msdl.microsoft.com/download/symbols/kernel32.pdb/E8C3A48CAC7EB60D8781D8C10020C44F1/kernel32.pdb"
```

结果：`http=200 size=1060864`，魔数 `4d696372`（MSF）校验通过。

**注意：** msdl 会 302 跳转到 Azure Blob，必须加 `-L`。且输出路径必须用**原生 Windows 路径**（`D:/Symbols/...`），MSYS 路径（`/d/Symbols/...`）会写不进去但报 200。

## 三、PDB 为什么没被 Ghidra 用上（未解）

### 已知事实（观察）

1. Ghidra 有完整 `symbolserver` 包：`HttpSymbolServer` / `LocalSymbolStore` / `SymbolServerService`
2. 配置读取自 **Ghidra Preferences**，不是 `_NT_SYMBOL_PATH` 环境变量
3. 配置 key：
   - `PdbSymbolServer.Symbol_Storage_Directory`
   - `PdbSymbolServer.Symbol_Search_Path`
4. `getSymbolSearchPaths()` 默认返回**空列表**（`Preferences.getProperty(..., "", true)`）—— 开箱即用不查任何符号服务器
5. 我写入 Preferences 后，Ghidra 确实读到了（文件被重写、格式保留）
6. 但 `PDB Universal` 分析器仍只跑 **0.012~0.015 秒**，说明没加载 1MB 的 PDB

### 关键障碍（推断）

REA 启动 Ghidra 时用了**独立的临时 user.home**：

```
-Duser.home=C:\Users\31954\AppData\Local\Temp\rea-ghidra-<hash>\home
```

所以我在 `C:\Users\31954\AppData\Roaming\ghidra\ghidra_12.1.4_PUBLIC\preferences` 里的配置，**REA 调用时根本读不到**。

这解释了为什么手动跑 `analyzeHeadless` 和 REA 跑都没生效——两边的 user.home 不同。

### 未验证的解法（留给后续）

| 方案 | 思路 | 风险 |
|:---|:---|:---|
| A. 预置临时 home 的 preferences | 找到 REA 创建临时 home 的时机，提前放配置文件 | 临时目录每次随机，难命中 |
| B. 用 Ghidra 脚本注入 | 脚本里调 `Preferences.setProperty` | `Preferences` 类不在脚本 classpath（`Generic.jar` 未暴露），实测编译失败 |
| C. 装 PyGhidra | 用 `.py` 脚本 | Ghidra 12 弃用 Jython，PyGhidra 需 Python 包 + `pyghidraRun`，本机 python 路径不被识别 |
| D. 改 REA 源码 | 让它透传 `-Duser.home` 或预置 preferences | 侵入第三方包，升级即失效 |
| E. 接受现状 | 用 REA 的 `inspect-managed-members` 拿静态证据 | 原生 PE 拿不到 PDB 符号名 |

## 四、Ghidra 脚本机制的两个坑（已定位）

| 现象 | 原因 |
|:---|:---|
| Java 脚本报 `The class could not be found` | 脚本 classpath 不含 `Generic.jar`，`import ghidra.framework.preferences.Preferences` 就编不过 |
| `.py` 脚本报 `Ghidra was not started with PyGhidra` | Ghidra 12 弃用 Jython，需 PyGhidra（独立 Python 环境） |

**最小可运行脚本**（只用 `GhidraScript` 基类）：

```java
//@category Test
import ghidra.app.script.GhidraScript;
public class HelloScript extends GhidraScript {
    public void run() throws Exception { println("HELLO"); }
}
```

实测输出 `INFO HelloScript.java> HELLO_FROM_GHIDRA_SCRIPT`。

**排查方法：逐步加 import 二分定位。** `T2.java`（只 import GhidraScript）通过 → `T1.java`（加 Preferences）失败 → 定位到 `Generic.jar` 不可见。

## 五、本轮实际改动

| 文件 | 改动 |
|:---|:---|
| `env.sh` | 补 `REA_MCP_MAX_RESPONSE_BYTES`（16MB）、`REA_JADX_ACTIVE_PROCESSOR_COUNT`（8）、`REA_LOG_LEVEL`（warn）；`DISABLED_ANALYZERS` 注释保留并标风险 |
| `setup-symbols.sh` | 新建，初始化 MS 规范符号存储 |
| `test-dotnet-chain.sh` | +8 断言（调优变量 + 符号结构 + 2 条硬门禁） |
| `D:\Symbols\` | 建成 level-2 结构，含 1.01MB kernel32.pdb |
| `D:\tools\ghidra_scripts\` | HelloScript.java（验证脚本机制）、SetupPdbSymbols.java（未成功） |

## 六、防回归门禁（已加入测试）

```bash
# REA 硬约束: MCP 响应上限必须 >= 10485760
MB=${REA_MCP_MAX_RESPONSE_BYTES:-0}
[ "$MB" -ge 10485760 ] && ok || bad

# 禁用分析器会打挂 Ghidra bridge, 默认必须为空
[ -z "${REA_GHIDRA_DISABLED_ANALYZERS:-}" ] && ok || bad
```

**反向验证：** 注入 `8388608` → 测试报 `FAIL REA_MCP_MAX_RESPONSE_BYTES 低于 REA 下限 10485760`，23/24；恢复后 24/24。门禁有效。

## 七、结论

**做成的：** 符号缓存结构、PDB 下载链路、两个真实 bug 修复、48 条测试断言（含 2 条硬门禁）。

**没做成的：** PDB 被 Ghidra 实际加载。根因是 REA 用独立临时 `user.home`，我的 Preferences 配置被隔离。

**建议：** 这个方向投入产出比已经不划算（试了 5 种方案）。如果确实需要 Windows 原生 PE 的符号名，更实际的路是：
1. 用 `dumpbin`/`pdbparse` 自己解析 PDB，不走 Ghidra
2. 或者接受 `FUN_xxx`，靠字符串/调用图人工还原（Go 二进制本来就这样）
