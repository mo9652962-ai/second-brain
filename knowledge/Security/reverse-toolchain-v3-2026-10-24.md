---
title: 逆向工具链增强 v3（2026-10-24）：binutils 十工具 + Go 符号恢复
date: 2026-10-24
tags: [reverse-engineering, rea, binutils, objdump, go-binary, symbols, toolchain]
status: 完成，61 条测试断言全过
---

# 逆向工具链增强 v3

## 结论置顶

| 项目 | 结果 |
|:---|:---|
| binutils 十工具 | ✅ 一次装齐（objdump 2.47 / objcopy / readelf / nm / strings / strip / gdb / gcc / as / addr2line） |
| **Go 符号恢复** | ✅ **2213 个符号，含 `main.computePan`**（Ghidra 只能给 1758 个 `FUN_xxx`） |
| objdump 接入 REA | ⚠️ 变量已配，但**对 CLI 无实际作用**（见下） |
| 测试断言 | 50 → **61 条**（+11） |
| 脚本语法检查 | 8 → **9 个** |

## 一、最重要的发现：Ghidra 的 Go 符号盲区可以被补上

### 问题

之前的实测：`calc.exe`（Go 1.26.6 编译）在 Ghidra 里是 **1758 个 `FUN_xxx`**，一个符号都没有。用 `rea search --kind procedures "computePan"` 返回空 list。

### 解法

Go 1.18+ 把符号表放在 `pclntab`，Ghidra 不解析。但**函数名以明文存在于二进制里**，`strings` 可以直接捞出来：

```bash
strings -n 6 calc.exe | grep -E "^(main|runtime|internal|...)\.*"
```

实测结果：

```
符号总数: 2213
其中 main.*: 2
Go 版本: go1.26.6
--- main.* 符号 ---
main.computePan     ← 这正是我们要找的 ground-truth 函数
main.main
```

**2213 vs 1758 `FUN_xxx`** —— 这不只是数量差，是「有名字」和「没名字」的差别。

### 工具化

`D:\tools\rea\recover-go-symbols.sh`：

```bash
# 交互模式（打印 main.* 符号）
bash recover-go-symbols.sh calc.exe

# 导出模式
bash recover-go-symbols.sh calc.exe symbols.txt
```

输出文件带元信息头：

```
# Go 符号恢复 — calc.exe
# Go 版本: go1.26.6
# 符号总数: 2213 (main.*: 2)
# 由 recover-go-symbols.sh 生成
```

### 完整工作流

```bash
source /d/tools/rea/env.sh

# 1. 先恢复符号名，知道要找什么
bash recover-go-symbols.sh target.exe symbols.txt
grep "^main\." symbols.txt

# 2. 用 Ghidra 分析拿地址
rea analyze target.exe --provider ghidra --format json

# 3. 用地址反编译
rea function target.exe 0x<addr> --provider ghidra
```

## 二、binutils 十工具（一次装齐）

### 安装方式

```bash
winget install --id BrechtSanders.WinLibs.POSIX.UCRT \
  --accept-package-agreements --accept-source-agreements --disable-interactivity
```

WinLibs 是 MinGW-W64 + GCC 打包，附带完整 binutils。安装路径：

```
C:\Users\USERNAME\AppData\Local\Microsoft\WinGet\Packages\
  BrechtSanders.WinLibs.POSIX.UCRT_Microsoft.Winget.Source_8wekyb3d8bbwe\mingw64\bin
```

### 实际拿到的工具

| 工具 | 版本/用途 |
|:---|:---|
| `objdump` | 2.47.20260726，反汇编/段表/符号/DWARF/重定位 |
| `objcopy` | 格式转换、段提取 |
| `readelf` | ELF 结构（跨平台分析） |
| `nm` | 符号表 |
| `strings` | **字符串提取（Go 符号恢复的关键）** |
| `strip` | 剥离符号（做测试样本） |
| `gdb` | GNU 调试器 |
| `gcc` / `as` | 编译器（**可自己造 ground-truth 样本**） |
| `addr2line` | 地址→源码行 |

### 路径格式坑

git-bash 和原生程序要两种格式：

```bash
export MINGW_BIN="C:/Users/.../mingw64/bin"           # REA/原生程序用
export MINGW_BIN_POSIX="/c/Users/.../mingw64/bin"    # git-bash PATH 用
export PATH="$MINGW_BIN_POSIX:$PATH"
```

**只配 `C:/` 格式进 PATH 是无效的**（实测 `command -v objdump` 返回空）。

## 三、objdump 接入 REA：配了但没用

### 发现过程

配了 `REA_OBJDUMP_COMMAND` 后测试：

```bash
rea inspect-binary-layout calc.exe --provider objdump
# -> code: UNKNOWN, message: "Unknown flag: --provider"
```

查源码定位：`inspectWithObjdump` 是 `AnalysisRuntime` 的内部方法，operation 名 `inspect_with_objdump`，**没有对应的 CLI 子命令**。

```js
inspectWithObjdump(rawInput, options = {}) {
  const parsed = objdumpInputSchema.safeParse(rawInput);
  ...
  return this.#observe("inspect_with_objdump", command, ...);
}
```

CLI 的 `inspect-binary-layout` 走 REA 自己的内置解析器，不经过 objdump provider。

### 结论

| 场景 | 效果 |
|:---|:---|
| `REA_OBJDUMP_COMMAND` 对 CLI | ❌ 无作用 |
| `REA_OBJDUMP_COMMAND` 对 MCP | 未验证（可能需要，但按你的指令不注册 MCP） |
| binutils 独立使用 | ✅ 有效，且 `strings` 价值最大 |

**保留配置**（无害，且 MCP 场景可能需要），但**不声称「objdump 已接入 REA」**。

## 四、REA 平台能力盘点（实测）

### providers 显示 vs 实际可用

`rea providers` 显示的能力声明**不等于实际可用**：

| Provider | 声明可用组 | 实际测试 | 结论 |
|:---|:---:|:---|:---|
| `ghidra` | 20 | ✅ 可用 | 20 组可用，2 组因 Windows P0 只读不可用 |
| `rea-dotnet-static` | 3 | ✅ 可用 | 全可用 |
| `sqlite` | 1 | ✅ 可用 | 可用 |
| `rea-artifact-graph` | 2 | ✅ 可用 | 可用 |
| `ida` | 2 | ❌ `not_configured` | 需 `REA_IDA_MCP_CONFIG` |
| `hopper` | 6 | ❌ `unsupported_host` | 「Hopper integration is not supported on win32」 |
| `kuna` | 0 | ❌ `not_configured` | 且 PE 格式不支持 |
| `native-macos` | 0 | ❌ | 需 macOS |

**教训：能力声明 ≠ 可用。必须实际跑一次。**

### Ghidra 在 Windows 的 2 个不可用能力

```
FAIL annotate_native_function  -> Windows Ghidra P0 does not admit database mutation.
FAIL set_address_name/set_addresses_names -> 同上
```

这是设计限制（P0 只读），已用 WSL2 绕过。

## 五、新验证的 Ghidra 内存级能力

这些在 Windows P0 只读模式下**仍然可用**，实测通过：

### search-bytes

```bash
rea search-bytes calc.exe "4D5A" --format json
```

结果：

```json
{"matches": [
  {"address": "0x140000000", "segment": "Headers", "file_offset": 0},
  {"address": "0x140106a7b", "segment": ".rdata", "file_offset": 1070203}
], "searched": ..., "complete": true}
```

带 `file_offset` 和 `segment`，`confidence: observed`。

### read-bytes

```bash
rea read-bytes calc.exe 0x140000000 --length 64 --format json
```

结果：

```json
{"address": "0x140000000", "requested_bytes": 64, "returned_bytes": 64,
 "bytes_hex": "4d5a90000300000004000000ffff0000...", "complete": true}
```

正是 MZ 头，`confidence: observed`。

### 参数陷阱

| 错误写法 | 正确写法 |
|:---|:---|
| `search-bytes <path> --hex "4D5A"` | `search-bytes <path> "4D5A"` （位置参数） |
| `search <path> --query "x"` | `search <path> "x" --kind procedures` |

## 六、JSON 结构陷阱

`normalized_result` **有时是 dict，有时是 list**：

```python
# search 返回 list
d['normalized_result']  # -> []  空列表（未找到）

# analyze 返回 dict
d['normalized_result']  # -> {'document': ..., 'procedure_count': 1758}
```

写解析代码必须判断类型，否则 `nr.get(...)` 会静默返回 None。

## 七、本轮改动

| 文件 | 改动 |
|:---|:---|
| `env.sh` | 新增 binutils 段（`MINGW_BIN` / `MINGW_BIN_POSIX` / PATH / `REA_OBJDUMP_COMMAND`） |
| `recover-go-symbols.sh` | **新建**，Go 符号恢复工具 |
| `test-dotnet-chain.sh` | +11 断言（binutils 7 条 + Go 符号 3 条 + objdump 执行 1 条） |

## 八、测试覆盖

```
npm run check  →  9 个脚本语法 OK
npm test       →  24 + 37 = 61 条断言全过
```

新增断言：

- binutils 6 个 exe 存在 + `MINGW_BIN` 配置 + objdump 可执行（7 条）
- Go 符号恢复：`main.computePan` / 符号总数 2213 / Go 版本 go1.26.6（3 条）
- 真实执行，非文件存在性检查

### 反向验证

破坏 `recover-go-symbols.sh` 第 26 行（核心 `strings` 调用）→ 测试 exit=1，报 2 个 FAIL：

```
FAIL  Go 符号恢复失败
FAIL  符号数量异常
结果: 35 通过 / 2 失败
```

恢复后 37/37。**门禁有效。**

## 九、未做的事（明确留空）

| 项目 | 状态 | 原因 |
|:---|:---|:---|
| tshark/capinfos（pcap 分析） | 未装 | Wireshark 约 300MB + 需 Npcap 驱动，本轮未做 |
| rizin | 未装 | `REA_RIZIN_COMMAND` 同样无 CLI 出口，且需 rz-pipe |
| binwalk/unblob（固件） | 未装 | **源码明确只支持 Linux**，需走 WSL2 |
| wakaru（JS 反混淆） | 未装 | **源码明确只支持 Linux x64** |
| PDB 符号被 Ghidra 使用 | 未打通 | 上轮已停手，REA 用隔离 user.home |
| ida / hopper / kuna | 不配 | 商业授权 / macOS only / 不支持 PE |
