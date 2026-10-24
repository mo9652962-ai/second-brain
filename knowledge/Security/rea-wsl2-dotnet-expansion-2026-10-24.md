---
title: REA 双通道拓展：WSL2 可写逆向 + .NET 反编译链路
date: 2026-10-24
tags: [reverse-engineering, rea, ghidra, wsl2, dotnet, ilspy, windows, deployment]
status: WSL2 通道已实证跑通 / .NET 链路部分完成
machine: Windows 11 x64 + WSL2 Ubuntu-22.04.5 / 16 核 / 15.6GB RAM
---

# REA 双通道拓展：WSL2 可写逆向 + .NET 反编译链路

> 本文是 `rea-full-stack-reverse-engineering-2026-10-24.md` 的拓展篇。
> **核心成果：把 Windows 只读的 Ghidra P0 升级为完整可写通道，用 WSL2 实现重命名/注释。**

---

## 0. 一句话结论

| 拓展项 | 状态 | 关键结果 |
|:---|:---:|:---|
| **WSL2 可写通道** | ✅ **完整跑通** | 重命名 + 注释写入成功，中文注释正常 |
| Windows P0 对照 | ✅ 已复现拒绝 | `Windows Ghidra P0 does not admit database mutation.` |
| .NET 反编译链路 | ⚠️ 部分完成 | REA 内置 metadata 够用；ilspycmd 受网络阻塞 |

---

## 1. WSL2 可写通道（核心拓展）

### 1.1 为什么要这个

Windows Ghidra P0 是**实验性只读**边界。同一操作两侧实测对比：

```bash
# Windows P0
rea annotate-native-function D:/tools/targets/calc.exe 0x140001080 \
  --name win_test --comment "should fail" --provider ghidra --format json
```

**Windows 返回：**
```json
{"error":"Analysis failed","code":"capability_unavailable",
 "details":{"provider_id":"ghidra","operation":"annotate_native_function",
 "reason":"Windows Ghidra P0 does not admit database mutation."}}
```

**WSL2 返回：**
```json
{"annotations":{"address":"0x140001080","name":"compute_pan_candidate",
 "comment":"WSL2 write test","inline_comment":null}}
```

这就是全部差别——**同样的 REA、同样的 Ghidra 12.1.4、同样的目标文件，平台边界决定了能不能写。**

### 1.2 部署清单（全部已装好）

| 组件 | 位置（WSL 内路径） | 说明 |
|:---|:---|:---|
| Node 22.19.0 | `/opt/node22/bin` | WSL 原生，非 Windows 版 |
| REA 6.7.0 | `/opt/rea` | `node_modules/rea-agents/scripts/rea.mjs` |
| Linux JDK 21.0.2 | `/mnt/d/tools/jdk21_linux` | Temurin，含 javac |
| Ghidra 12.1.4 | `/mnt/d/tools/ghidra_12.1.4_PUBLIC` | **与 Windows 共用同一份**，含 `linux_x86_64/decompile` |

**关键洞察**：Ghidra 安装包同时带 `win_x86_64` 和 `linux_x86_64` 两个原生 decompile 二进制。**一份 Ghidra 两个平台都能用**，不用装两遍。

### 1.3 doctor 实测（8/8 全绿）

```
available: True | version: 12.1.4
  [OK] configuration: /mnt/d/tools/ghidra_12.1.4_PUBLIC
  [OK] platform: linux              ← 关键：平台变了
  [OK] architecture: x64
  [OK] installation: .../Ghidra/application.properties
  [OK] version: 12.1.4
  [OK] headless: .../support/analyzeHeadless        ← Linux shell 版
  [OK] native_decompiler: .../linux_x86_64/decompile  ← Linux 原生二进制
  [OK] java: 21.0.2; 64-bit; JDK; /mnt/d/tools/jdk21_linux
```

注意 Windows 侧有 9 项（多一个 `native_authority`），Linux 侧 8 项——Windows 特有的 Job Object / DACL 检查在 Linux 不适用。

### 1.4 封装好的调度器

`D:\tools\rea\wsl-rea.sh`：

```bash
source /d/tools/rea/wsl-rea.sh
```

| 函数 | 作用 |
|:---|:---|
| `wrea <args...>` | 在 WSL2 跑 REA，**自动把 `D:/xxx` 转成 `/mnt/d/xxx`** |
| `wreaname <exe> <addr> <name> [comment]` | 重命名 + 注释（Win P0 做不到） |
| `wrefunc <exe> <addr>` | WSL2 下反编译函数 |
| `wreacheck` | 5 项自检（Node/JDK/REA/Ghidra/decompile） |

自检实测输出：

```
=== WSL2 REA 通道自检 ===
  Node: v22.19.0
  JDK:  openjdk version "21.0.2" 2024-01-16 LTS
  REA:  6.7.0
  Ghidra: 12.1.4
  decompile: OK
```

### 1.5 实战用法

```bash
source /d/tools/rea/wsl-rea.sh

# 1. 找函数地址
wrea search "D:/tools/targets/calc.exe" "." --kind procedures \
  --mode regex --provider ghidra --format json
# → 1758 个函数

# 2. 反编译
wrefunc "D:/tools/targets/calc.exe" 0x140001080
# → confidence: observed | 伪代码 2039 字符

# 3. 重命名 + 注释（Windows 做不到）
wreaname "D:/tools/targets/calc.exe" 0x140001160 "another_renamed_func" "测试注释中文"
# → {"name":"another_renamed_func","comment":"测试注释中文"}
```

**中文注释也正常写入**，实测通过。

### 1.6 性能代价

| 操作 | Windows P0 | WSL2 |
|:---|:---:|:---:|
| Ghidra 冷启动 | — | 10.6 秒 |
| 分析 calc.exe (1.6MB Go PE) | 54 秒 | 62 秒 |
| 跨 `/mnt/d` IO | 无 | 有开销 |

**优化建议**：把目标文件拷到 WSL 内部（`/tmp` 或 `~/work`）再分析，能省掉 `/mnt/d` 的 9p 文件系统开销。

```bash
wsl -e bash -c "cp /mnt/d/tools/targets/calc.exe /tmp/ && echo copied"
```

---

## 2. .NET 反编译链路

### 2.1 先搞清楚 ilspycmd 在 REA 里是什么角色

**重要纠正**：`REA_ILSPY_CMD_PATH` **不是** REA 用来驱动反编译的引擎路径。源码分析确认：

```javascript
// dist/application/DoctorDiagnostics.js:154
const optionalIlspyCheck = async (host) => {
    if (host.configuredIlspyCmdPath === undefined) return undefined;
    const version = await host.ilspyCmdVersion?.(host.configuredIlspyCmdPath);
    return check("ilspycmd", version !== undefined, ...)
};
```

它只是 **doctor 的一个健康检查项**——设了就检查能不能跑，没设就跳过。

REA 真正的 .NET 工作流是：
1. `inspect-managed-members` — 内置 metadata 解析（CIL anchors、ldstr 字符串、签名）
2. `inspect-managed-artifact` — PE/CLI 身份
3. `inspect-managed-native-boundaries` — P/Invoke 边界
4. **你自己**用 ilspycmd/dnSpy 反编译出 C# 源码
5. `import-managed-reconstruction` — 把产物导入，REA 校验是否与静态成员证据一致

```bash
rea import-managed-reconstruction --help
# Usage: rea import-managed-reconstruction <inputJson>
# Import decompiler-produced managed reconstruction against exact static member evidence
```

**这个设计的价值**：REA 不信你的反编译结果，它拿 `signature_sha256` 和 `normalized_il_sha256` 跟静态证据对账。相当于给外部反编译产物加了个防篡改校验。

### 2.2 三条可行路线（按推荐度）

| 路线 | 需要什么 | 状态 |
|:---|:---|:---|
| **① REA 内置 metadata** | 无额外依赖 | ✅ 已可用，够做边界审计 |
| **② ilspycmd 8.2 + 现有 .NET 8** | 无需装任何运行时 | ⏳ 网络阻塞 |
| **③ ILSpy 桌面版自包含** | 52MB zip，免运行时 | 备选 |

### 2.3 路线 ② 的关键发现

**你本机已有 .NET 8.0.21 和 8.0.32 运行时**，而 `ilspycmd 8.2.0.7535` 正好以 `net8.0` 为目标：

```bash
"/c/Program Files/dotnet/dotnet.exe" --list-runtimes
# Microsoft.NETCore.App 8.0.21
# Microsoft.NETCore.App 8.0.32
```

所以**不用装 .NET 10**（那是 11.x 的要求）。8.2 版本直接能跑。

**但踩到的坑**：
- ilspycmd 11.1 要 .NET 10 → 试过改 `runtimeconfig.json` 的 `rollForward`，报 `Could not load System.Runtime, Version=10.0.0.0`（程序集版本硬绑定，rollForward 救不了）
- .NET 10 运行时 37MB，从 `builds.dotnet.microsoft.com` 直连/代理都只有 5-10KB/s（需 1 小时+）
- NuGet CDN（`globalcdn.nuget.org`）同样不稳定
- WSL 内 apt 装 .NET：Ubuntu 22.04 的微软源只提供到 **.NET 9**，没有 10

**当前状态**：ilspycmd 8.2 的 nupkg（3.8MB）在后台断点续传中。下载完即可用：
```bash
"/c/Program Files/dotnet/dotnet.exe" D:/tools/rea/ilspy/bin82/ilspycmd.dll --version
```

### 2.4 现在就能用的 .NET 能力

不用等 ilspycmd，REA 内置的这些已经实测可用：

```bash
source /d/tools/rea/env.sh

# 程序集身份
rea inspect-managed-artifact <dll> --format json

# 成员清单 + 签名 + 字符串字面量（64MB 墙用 --type 绕）
rea inspect-managed-members <dll> --type "System.Net.WebRequest" --format json

# P/Invoke 与原生边界
rea inspect-managed-native-boundaries <dll> --format json

# 成员签名比对（找 patch 差异）
rea compare-managed-members <old.dll> <new.dll> --format json
```

---

## 3. 双通道决策树

```
需要逆向一个二进制
│
├─ 只是看清楚结构 / 找函数 / 读伪代码
│   └─ Windows P0 就够（54 秒，路径简单，无 WSL 开销）
│
├─ 需要重命名函数 / 写注释 / 迭代式手工分析
│   └─ WSL2 通道（wreaname / wrefun）
│       └─ 目标先拷到 /tmp 省 IO 开销
│
├─ .NET 托管程序集
│   ├─ 只要边界审计 / 成员清单 / 签名比对 → REA 内置 metadata
│   └─ 要读 C# 源码 → ilspycmd 8.2（配现有 .NET 8）
│
└─ 动态调试 / 脱壳 / 反混淆
    └─ REA 不做，上 x64dbg / Frida / de4dot
```

---

## 4. 完整环境清单（本次拓展后）

| 层 | 组件 | 路径 |
|:---|:---|:---|
| **Windows 主通道** | REA 6.7.0 + Ghidra 12.1.4 | `D:/tools/rea` + `D:/tools/ghidra_12.1.4_PUBLIC` |
| Windows Android | JADX 0.7.1 + Apktool 2.10.0 + ADB 37.0.1 | `D:/tools/rea/android` |
| Windows 符号 | 微软 PDB 缓存 | `D:/Symbols` |
| **WSL2 可写通道** | Node 22.19.0 + REA 6.7.0 | `/opt/node22` + `/opt/rea` |
| WSL2 Java | Linux JDK 21.0.2 (Temurin) | `D:/tools/jdk21_linux` |
| WSL2 Ghidra | 共用 Windows 那份 | `/mnt/d/tools/ghidra_12.1.4_PUBLIC` |
| .NET | 系统 .NET 8.0.32 运行时 | `C:/Program Files/dotnet` |

**激活命令：**
```bash
source /d/tools/rea/env.sh       # Windows 主通道
source /d/tools/rea/wsl-rea.sh   # WSL2 可写通道
```

---

## 5. 踩坑记录

| # | 坑 | 现象 | 解法 |
|:---|:---|:---|:---|
| 1 | WSL 无 Node | `node: command not found` | 下 Linux 版 Node 22.19 到 `/opt/node22` |
| 2 | WSL 无 JDK | Ghidra 起不来 | 下 Temurin Linux JDK 到 `D:/tools/jdk21_linux` |
| 3 | 项目目录必须先存在 | `Directory not found: /tmp/wsl_test` | `mkdir -p` 先建 |
| 4 | ilspycmd 11.1 要 .NET 10 | `Could not load System.Runtime, Version=10.0.0.0` | 降级到 8.2（匹配现有 .NET 8） |
| 5 | 改 runtimeconfig 无效 | rollForward 救不了程序集版本绑定 | 必须用匹配 TFM 的版本 |
| 6 | Ubuntu 22.04 微软源无 .NET 10 | `Unable to locate package dotnet-sdk-10.0` | 源只到 9.0，要 10 得用其他发行版 |
| 7 | NuGet CDN 极慢 | 5-10KB/s | 断点续传 + 多次重试 |
| 8 | Windows 文件句柄占用 | `Device or resource busy` | `Stop-Process` 杀 curl，或换目录 |
| 9 | `REA_ILSPY_CMD_PATH` 误解 | 以为是反编译引擎路径 | 实际只是 doctor 健康检查项 |
| 10 | 跨 `/mnt/d` IO 慢 | WSL 分析比 Windows 慢 8 秒 | 目标拷到 WSL 内部 `/tmp` |

---

## 6. 参考

- REA 仓库：https://github.com/morluto/rea
- Ghidra 12.1.4：https://github.com/NationalSecurityAgency/ghidra/releases/tag/Ghidra_12.1.4_build
- 前篇：`rea-full-stack-reverse-engineering-2026-10-24.md`
- 审计篇：`rea-mcp-reverse-engineering-audit-2026-10-23.md`
