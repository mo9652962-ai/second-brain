---
title: ilspycmd 8.2 在 .NET 8 运行时打通（rollForward + Go shim）
date: 2026-10-24
tags: [reverse-engineering, dotnet, ilspy, ilspycmd, rea, windows, toolchain]
status: 已打通，REA doctor 识别通过，端到端实证
---

# ilspycmd 8.2 在 .NET 8 上跑通

## 结论置顶

**已打通。** `ilspycmd 8.2.0.7535` 在本机（只有 .NET 8.0.21 / 8.0.32，无 .NET 6 / 10）成功运行，反编译 `System.Core.dll` 产出 **694 个 .cs 文件 / 4.1MB**，REA doctor 报 `[OK] ilspycmd`。

关键只有两步：
1. `ilspycmd.runtimeconfig.json` 加 `"rollForward": "Major"` —— 让 net6.0 目标向前滚动到 .NET 8
2. 用 Go 编译一个真 PE shim —— 因为 REA 用 `execFile` 直呼，Node 在 Windows 无法执行 `.bat` / `.cmd`

## 一、踩过的四个坑（按发现顺序）

### 坑 1：目标框架猜错

我原以为 `ilspycmd 8.2` 是 `net8.0`，实测是 **`net6.0`**：

```
tools/net6.0/any/ilspycmd.dll          2023-11-03
tools/net6.0/any/ilspycmd.runtimeconfig.json
```

版本号 8.2 指 ILSpy 产品版本，不是 .NET 目标版本。**版本号不能推断 TFM，必须看包内路径。**

### 坑 2：默认不跨主版本

直接跑报：

```
You must install or update .NET to run this application.
Framework: 'Microsoft.NETCore.App', version '6.0.0' (x64)
The following frameworks were found:
  8.0.21 / 8.0.32
```

runtimeconfig 未声明 `rollForward`，默认 `Minor` —— 只在同一主版本内滚动。

### 坑 3：方向决定成败

**向前滚动可行，向后不可行：**

| 场景 | 方向 | 结果 |
|:---|:---|:---|
| ilspycmd 11.1 (net10.0) → 本机 net8 | **向后** | ❌ `Could not load System.Runtime, Version=10.0.0.0` |
| ilspycmd 8.2 (net6.0) → 本机 net8 | **向前** | ✅ 正常工作 |

.NET 运行时保证向后兼容（新版能跑旧版编译的程序），反之不成立。这是上次 11.1 失败的根因。

### 坑 4：Node execFile 不认 .bat/.cmd

`.bat` / `.cmd` 包装器在终端里跑得好好的：

```
$ cmd.exe /c "ilspycmd.cmd" --version
ilspycmd: 8.2.0.7535
```

但 REA doctor 报 FAIL。原因：REA 用 `execFile` 直接执行路径，而 Node 在 Windows 上**不能直接执行批处理文件**（需要 `shell: true` 或 `cmd /c`）。

**注意：** `.cmd` 的 stdout 经 `od -c` 检查是干净的 `ilspycmd: 8.2.0.7535\r\n`，所以不是输出格式问题，纯粹是执行方式问题。

## 二、失败的三条弯路（别重走）

| 尝试 | 结果 | 原因 |
|:---|:---|:---|
| `dotnet tool install --tool-path` 从本地 nupkg 装 | ❌ | 需要 .NET **SDK**，本机只有运行时 |
| 复制 `dotnet.exe` 改名 `ilspycmd.exe` | ❌ | 明确拒绝：`Error: cannot execute dotnet when renamed to ilspycmd.` |
| 用 ILSpy GUI 的 apphost 改名 | ❌ | apphost 内部绑定自身元数据，改名后静默无输出 |
| 下载 .NET 10 运行时 | ❌ | 经代理仅 ~10KB/s，三次重试均残缺（`End-of-central-directory`） |
| WSL `apt install dotnet-sdk-10.0` | ❌ | Ubuntu 22.04 微软源只到 .NET 9 |

## 三、最终方案（两步）

### 步骤 1：runtimeconfig 加 rollForward

文件：`D:\tools\rea\ilspy\bin82\tools\net6.0\any\ilspycmd.runtimeconfig.json`

```json
{
  "runtimeOptions": {
    "tfm": "net6.0",
    "framework": {
      "name": "Microsoft.NETCore.App",
      "version": "6.0.0"
    },
    "rollForward": "Major",
    "configProperties": {
      "System.GC.Server": true,
      "System.Globalization.Invariant": true,
      "System.Globalization.PredefinedCulturesOnly": true,
      "System.Reflection.Metadata.MetadataUpdater.IsSupported": false
    }
  }
}
```

验证：

```
$ dotnet ilspycmd.dll --version
ilspycmd: 8.2.0.7535
ICSharpCode.Decompiler: 8.2.0.7535
```

### 步骤 2：Go 编译真 PE shim

源码：`D:\tools\rea\ilspy\shim\main.go`

```go
package main

import (
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
)

const (
	dotnetExe   = `C:\Program Files\dotnet\dotnet.exe`
	ilspycmdDll = `D:\tools\rea\ilspy\bin82\tools\net6.0\any\ilspycmd.dll`
)

func main() {
	args := append([]string{ilspycmdDll}, os.Args[1:]...)
	cmd := exec.Command(dotnetExe, args...)
	cmd.Stdin = os.Stdin
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	if err := cmd.Run(); err != nil {
		if ee, ok := err.(*exec.ExitError); ok {
			os.Exit(ee.ExitCode())
		}
		fmt.Fprintf(os.Stderr, "%s: %v\n", filepath.Base(os.Args[0]), err)
		os.Exit(1)
	}
}
```

构建：

```bash
cd /d/tools/rea/ilspy/shim
CGO_ENABLED=0 go build -ldflags="-s -w" -o ilspycmd.exe main.go
```

产物 1968 KB，`CGO_ENABLED=0` 保证无 DLL 依赖、单文件可移植。

一键重建脚本：`D:\tools\rea\ilspy\shim\build.sh`

### 步骤 3：接进 env.sh

```bash
export REA_ILSPY_CMD_PATH="$REA_HOME/ilspy/shim/ilspycmd.exe"
```

## 四、验收证据

### 4.1 REA doctor

```
OK   ilspycmd    D:/tools/rea/ilspy/shim/ilspycmd.exe (ilspycmd: 8.2.0.7535)
```

### 4.2 整程序集反编译

```bash
./shim/ilspycmd.exe --disable-updatecheck \
  -o "D:/tools/targets/ilspy_out" \
  -p "C:/Windows/Microsoft.NET/Framework64/v4.0.30319/System.Core.dll"
```

产出：**694 个 .cs 文件 / 4.1MB**

> ⚠️ 必须加 `--disable-updatecheck`。否则它会先打印「有新版本」然后**不执行反编译、产出 0 文件**。

### 4.3 双源交叉验证（最有说服力的一条）

同一个类型 `System.Linq.Enumerable`，两个独立来源比对：

| 来源 | 方法名数量 |
|:---|:---:|
| ilspycmd 反编译 C# 源码（正则提取） | 85 |
| REA `inspect-managed-members` 静态元数据 | 77 |
| **交集** | **77** |
| 仅 ilspycmd | 8 |
| 仅 REA | **0** |

- **REA 的 77 个方法，ilspycmd 100% 覆盖** —— 没有漏
- ilspycmd 多出 8 个：`Clone` / `Dispose` / `GetCount` / `GetEnumerator` / `GetSourceEnumerator` / `LazyToArray` / `LoadFromEnumerator` / `MoveNext` —— 全是**嵌套类 `Iterator<TSource>` 的成员**，REA 的 `--type` 只查顶层类型，不递归嵌套类
- **零冲突**

这个结果同时验证了两件事：ilspycmd 输出真实完整；REA 静态元数据准确（在顶层类型范围内）。

## 五、使用方式

```bash
source /d/tools/rea/env.sh

# 方式 A: 直接调 shim
D:/tools/rea/ilspy/shim/ilspycmd.exe --disable-updatecheck -t "命名空间.类名" "目标.dll"

# 方式 B: 整程序集导出
D:/tools/rea/ilspy/shim/ilspycmd.exe --disable-updatecheck -o "输出目录" -p "目标.dll"

# 方式 C: REA 静态证据（不需要 ilspycmd，速度更快）
rea inspect-managed-members "目标.dll" --type "命名空间.类名" --format json
```

**选择建议：**

| 需求 | 用什么 |
|:---|:---|
| 看 C# 源码逻辑 | ilspycmd |
| 拿方法 token / 调用边 / 字符串字面量 | REA `inspect-managed-members` |
| 两者互校 | 双跑，比对方法名集合 |
| 大程序集（>64MB 元数据） | 必须用 REA `--type` 局部取，否则撞预算墙 |

## 六、已知限制

| 限制 | 说明 |
|:---|:---|
| 必须带 `--disable-updatecheck` | 否则静默产出 0 文件 |
| 嵌套类型不递归 | REA `--type` 只查顶层；要查嵌套类需单独指定 |
| net6.0 向前滚动属非官方路径 | 官方不保证；但实测稳定。若要长期稳定，装 .NET 6 运行时更正规 |
| 版本停留在 8.2 | 更高版本（10.x/11.x）目标 net8/net10，11.1 实测向后滚动失败 |
| shim 硬编码路径 | `main.go` 里写死 dotnet 和 dll 路径；换机需重编译 |

## 七、文件清单

| 路径 | 说明 |
|:---|:---|
| `D:\tools\rea\ilspy\ilspycmd82.nupkg` | 原始包 3.71MB |
| `D:\tools\rea\ilspy\bin82\tools\net6.0\any\` | 解压后 57 文件 |
| `D:\tools\rea\ilspy\bin82\tools\net6.0\any\ilspycmd.runtimeconfig.json` | 已加 rollForward:Major |
| `D:\tools\rea\ilspy\shim\main.go` | shim 源码 |
| `D:\tools\rea\ilspy\shim\ilspycmd.exe` | 产物 1968KB |
| `D:\tools\rea\ilspy\shim\build.sh` | 一键重建 |
| `D:\tools\targets\ilspy_out\` | 测试产出 694 文件 |
