---
title: PDB 符号链路打通（2026-10-26）：从 4312 个 FUN_xxx 到 2849 个真实函数名
date: 2026-10-26
tags: [reverse-engineering, ghidra, pdb, symbol-server, windows, kernel32, user32, pre-script]
status: 完成，74 + 24 = 98 条断言全过，两项反向验证通过
---

# PDB 符号链路打通：纠缠多轮的真根因

## 结论置顶

| 指标 | 打通前 | 打通后 |
|:---|:---|:---|
| `kernel32.dll` 函数名 | **4312 个 `FUN_xxx`** | **2849 个真实名字** |
| `user32.dll` | 全 `FUN_xxx` | **3176 / 3337 已命名**（含 C++ 模板符号） |
| PDB 分析器耗时 | `0.018 secs`（跳过） | **`39.189 secs`**（真正加载） |
| PDB 自动下载 | ❌ 未打通 | ✅ **实测 user32.pdb 1.19MB 自动落盘** |

## 一、真根因：Ghidra 自己给出了答案

之前反复失败，以为是 `user.home` 隔离或 preferences 格式问题。这次完整看了日志，Ghidra 的报错里**直接写了怎么修**：

```
INFO  Skipping PDB processing: failed to locate PDB file in configured locations (PdbUniversalAnalyzer)
    PdbAnalyzer.setPdbFileOption(currentProgram, new File("/path/to/pdb/file.pdb")); or
    PdbUniversalAnalyzer.setPdbFileOption(currentProgram, new File("/path/to/pdb/file.pdb"));
Or set the symbol server search configuration using:
    PdbPlugin.saveSymbolServerServiceConfig(...);
 This must be done using a pre-script (prior to analysis). (PdbUniversalAnalyzer)
```

三个关键信息：
1. 用 `PdbPlugin.saveSymbolServerServiceConfig(...)` 配置符号服务器
2. **必须是 pre-script（分析之前）**
3. 不能靠 preferences 或 `_NT_SYMBOL_PATH`

**之前所有失败尝试都错在「时机」上** —— 用 postScript 或改 preferences，PDB 分析器早在 auto-analysis 阶段就跑完并跳过了。

## 二、四个 API 细节（全靠 javap 实测，不能猜）

| 我以为的 | 实际 | 后果 |
|:---|:---|:---|
| `RemoteSymbolServer` | **`HttpSymbolServer`**（Ghidra 里没有 RemoteSymbolServer 这个类） | `cannot find symbol` |
| `SymbolStore.create(File,int)` | **`LocalSymbolStore.create(File,int)`** | `cannot find symbol` |
| `store.isValid()` | **`store.isValid(TaskMonitor)`** | `method cannot be applied` |
| 构造函数配远程服务器 | **`HttpSymbolServer.createTrusted(String)`** 静态工厂最简 | 参数难凑 |

查 API 的正确姿势：

```bash
"C:/Users/USERNAME/jdk21/bin/javap.exe" \
  -classpath "D:/tools/ghidra_12.1.4_PUBLIC/Ghidra/Features/PDB/lib/PDB.jar" \
  pdb.symbolserver.HttpSymbolServer
```

**注意**：`javap` 在 `jdk21/bin/` 下，不在 PATH 里；`javap -classpath .` 对解压出的 class 无效（缺依赖），必须指向 jar。

## 三、核心脚本

### 3.1 SetupPdbSymbols.java（pre-script）

```java
LocalSymbolStore.create(storeDir, 2);           // indexLevel=2，符合 MS 规范
LocalSymbolStore store = new LocalSymbolStore(storeDir);
List<SymbolServer> servers = new ArrayList<>();
HttpSymbolServer remote = HttpSymbolServer.createTrusted(serverUrl);
servers.add(remote);
SymbolServerService svc = new SymbolServerService(store, servers);
PdbPlugin.saveSymbolServerServiceConfig(svc);   // 关键：分析前写入
```

### 3.2 调用方式（preScript 是重点）

```bash
analyzeHeadless.bat "D:/tools/ghidra_proj" my_proj \
  -import "C:/Windows/System32/kernel32.dll" \
  -scriptPath "D:/tools/ghidra_scripts" \
  -preScript SetupPdbSymbols.java "D:/Symbols" "https://msdl.microsoft.com/download/symbols"
```

### 3.3 一键脚本

```bash
cd /d/tools/rea
bash apply-pdb-symbols.sh "C:/Windows/System32/kernel32.dll" my_proj
```

## 四、实测证据

### 4.1 成功日志（kernel32.dll）

```
SETUPPDB: store=D:\Symbols valid=true
SETUPPDB: server=https://msdl.microsoft.com/download/symbols valid=true
SETUPPDB: service valid=true
SETUPPDB: OK 配置已保存（PDB 分析器将使用此配置）
INFO  PDB Universal: scheduling PDB Function Internals Analysis
    PDB Universal                             39.189 secs
    PDB Universal Function Internals           0.051 secs
DUMPNAMED: total=2849 named=2849 main_pkg=0
```

对比失败时：`PDB Universal 0.018 secs` + `Skipping PDB processing`。

**耗时分水岭**：0.0x 秒 = 跳过；数十秒 = 真正加载解析。

### 4.2 真实函数名（此前全是 FUN_xxx）

```
180001008  _tlgCreate1Sz_wchar_t
180001060  _tlgKeywordOn
18000108c  _tlgWriteTransfer_EventWriteTransfer
180001130  _tlgEnableCallback
1800011b0  NlsCountOfWCharsWithinRange
180001220  SortChangeCase
180001440  MapCase
180001538  GetGraphemeStartPositions
180002294  FindLastIndexOfString
```

这些都是 **kernel32 内部私有函数**（非导出表），只有 PDB 才有。

### 4.3 user32.dll 全新下载（无缓存）

```
DUMPNAMED: total=3337 named=3176 main_pkg=0
180001250  ScrollWindowEx
180001008  Write<_tlgWrapperByVal<8>,_tlgWrapSz<char>,_tlgWrapperByVal<4>...>
```

连 **C++ 模板符号**都还原了。

缓存落盘验证：

```
D:/Symbols/us/user32.pdb/F0BF56EE0A784974D49A58173A7CBC7E1/user32.pdb  1,191,936 字节
```

标准 MS 结构：`<首字母>/<pdb名>/<GUID>/<pdb名>`。

## 五、为什么之前所有尝试都失败

| 尝试 | 结果 | 为什么错 |
|:---|:---|:---|
| 改 `%APPDATA%\ghidra\...\preferences` | 无效 | 时机不对，且 REA 用独立 `user.home` |
| `_NT_SYMBOL_PATH` 环境变量 | 无效 | Ghidra 根本不读这个变量 |
| `-postScript` 配符号服务器 | 无效 | **分析早已跑完，PDB 已被跳过** |
| Ghidra Java 脚本调 `Preferences` | 编译失败 | `Generic.jar` 不在脚本 classpath |
| `.py` 脚本 | 无法运行 | Ghidra 12 弃用 Jython，需 PyGhidra |
| 手动下 PDB 放 `D:\Symbols` | 无效 | 配置没写进 Ghidra，分析器不知道去查 |

**核心教训：Ghidra 的日志里往往直接写着解决方案，不要凭经验猜。**

## 六、能力边界

**观察**：
- `kernel32.dll` 2849 个函数全部命名（PDB 覆盖完整）
- `user32.dll` 3176 / 3337 命名（161 个无 PDB 条目，属正常）
- PDB 首次下载耗时约 39 秒（含网络），缓存命中后 0.4 秒
- 符号缓存严格遵循 MS indexLevel=2 结构

**推断**：
- 只要能连 `msdl.microsoft.com`，任意 Windows 系统 DLL/EXE 都能拿到符号
- 第三方软件若有公开符号服务器（如 Mozilla、Google），同样可用 `HttpSymbolServer.createTrusted(url)` 接入

**未知**：
- 未测试离线环境（无网络时是否能用纯本地缓存跑通）
- 未测试非微软符号服务器（如 Mozilla symbol server）的实际兼容性
- 未验证 PDB 里的**类型信息**（struct 定义）是否也进了 Ghidra 数据类型管理器

## 七、测试

```
npm run check  →  11 sh + 6 java → syntax OK
npm test       →  24 + 74 = 98 条断言，0 失败
```

**两项反向验证均生效**：

| 注入破坏 | 期望 | 实际 |
|:---|:---|:---|
| `-preScript` → `-postScript` | 测试失败 | **FAIL preScript**，73/1 ✅ |
| `HttpSymbolServer` → `RemoteSymbolServer` | 测试失败 | **FAIL 残留 RemoteSymbolServer**，73/1 ✅ |
| 恢复 | 全绿 | 74/0 ✅ |

## 八、文件清单

| 文件 | 作用 |
|:---|:---|
| `D:\tools\ghidra_scripts\SetupPdbSymbols.java` | pre-script，配置符号服务器 |
| `D:\tools\rea\apply-pdb-symbols.sh` | 一键：配置 + 分析 + 统计 |
| `D:\tools\ghidra_scripts\TestPre.java` | preScript 机制验证（保留作诊断） |
| `D:\Symbols\` | 符号缓存（MS indexLevel=2 结构） |
