---
title: 二进制自动化分诊与混淆字符串解密（2026-10-26）：DIE 3.21 与 FLOSS 3.1.1 流水线落地
date: 2026-10-26
tags: [reverse-engineering, die, detect-it-easy, floss, obfuscation, stackstrings, deobfuscation, triage, entropy]
status: 完成，115 + 24 = 139 条断言全绿，双反向验证通过
---

# 二进制自动化分诊与混淆字符串解密：从未知外壳到静态解密全景

## 结论置顶

| 分析维度 | 工具方案 | 核心输出能力 | 实测验证 |
|:---|:---|:---|:---:|
| **格式/编译器/加壳器判定** | **Detect It Easy (DIE 3.21 CLI / `diec.exe`)** | PE/ELF/APK 格式解析、Linker/Compiler/Packer 签名识别 | ✅ 实测通 |
| **Section 级 Shannon 熵扫描** | **`diec.exe -e -j`** | 逐段计算熵值，阈值 `≥ 7.0` 自动告警（识别加壳与加密 payload） | ✅ 实测通 |
| **栈字符串 (Stackstrings)** | **FLARE FLOSS 3.1.1 (`floss.exe`)** | 动态栈构造字符串还原（`Hidden_StackStr!`） | ✅ 实测通（传统 `strings` 为 0） |
| **紧凑/异或解密字符串** | **`floss.exe` (Tightstrings / Decoded)** | 模拟执行自动提取 XOR / RC4 / 自定义解密函数中的明文（`Secret_Token_2026`） | ✅ 实测通（传统 `strings` 为 0） |
| **一键分诊与引擎推荐** | **`triage-binary.sh`** | 全景终端仪表盘 + 聚合 JSON 输出 + Go/Rust/.NET 智能路由 | ✅ 实测通 |

---

## 一、逆向工程 Phase 0 / Phase 1 的核心痛点

面对一个完全陌生的二进制目标：
1. **加壳盲区**：不知道是 UPX、VMProtect 还是普通编译器直出；如果盲目扔进 Ghidra 反编译，遇到强壳会耗费大量时间分析无意义的解包 Stub。
2. **字符串防御欺骗**：恶意软件和商用防护软件通常不把关键配置（C2 域名、API Token、注册表键值、解密密钥）明文硬编码在数据段，而是使用运行时栈拼接（Stackstring）或函数内动态 XOR 异或还原。传统的 `strings` 工具对此**完全失明（返回 0 结果）**。

---

## 二、双核心引擎技术突破与实证

### 2.1 Detect It Easy (DIE 3.21)
- **部署位置**：`D:/tools/die/diec.exe`
- **实测样本验证**：
  - `calc.exe` → 准确识别 `PE64 Compiler: Go(1.18.X-1.24.0)`
  - `rg.exe` → 准确识别 `PE64 Linker: Microsoft Linker(14.51) Tool: Visual Studio 2026 Debug data: [codeview, vc_feature, pogo]`
  - `ilspycmd.dll` → 准确识别 `PE32 Library: .NET Core(CLR 4.0.30319)`
  - `ApiDemos-debug.apk` → 准确识别 `APK Package: io.appium.android.apis(3.1.0)`
- **熵扫描 (`diec -e`)**：
  - `calc.exe` 最高熵 6.26（未加壳）；
  - `ApiDemos-debug.apk` 压缩段熵达 7.44（准确触发高熵压缩告警）。

### 2.2 FLARE FLOSS (3.1.1)
- **部署位置**：`D:/tools/floss/floss.exe`
- **自建 Ground-Truth 验证样本** (`D:/tools/targets/obf_sample.c`)：
  - 栈字符串：`volatile char s[20]` 逐字节拼装 `"Hidden_StackStr!"`；
  - 异或解密：`enc[] ^ 0x5A` 动态解密 `"Secret_Token_2026"`；
  - 经 `gcc -O1` 编译并 `strip` 剥离符号。
- **对照实测结果**：
  - 传统 `strings obf_sample.exe | grep -iE "hidden|secret"`：**返回 0 条匹配（完全漏报）**；
  - `floss.exe --no static -q obf_sample.exe`：
    - 成功提取 `Hidden_StackStr!` (Stackstrings)
    - 成功提取 `Secret_Token_2026` (Tightstrings)
    - 成功提取 `Secret_Token_2026` (Decoded strings 模拟执行命中)
    - **召回率 100%！**

---

## 三、工程实现与一键分诊流水线

### 3.1 `triage-binary.sh`
源码位置：`D:\tools\rea\triage-binary.sh`
- **输入**：任意待分析二进制目标。
- **执行**：
  1. 计算 SHA256 / MD5 / 文件尺寸；
  2. DIE 深入识别文件类型、编译器、链接器与数字签名；
  3. 计算各段 Shannon 熵，高亮 `≥ 7.0` 加壳可疑段；
  4. 对 `<= 50MB` 二进制调用 FLOSS 快速提取隐藏栈字符串与解密字符串；
  5. 自动根据语言指纹推荐后续深度逆向工具（`gosym`、`rearust`、`reacpp`、`reapdb`）。
- **参数支持**：
  - `-j` / `--json`：输出机读 JSON 报告。
  - `-q` / `--quick`：跳过耗时的动态解密，秒级出基础分诊报告。

### 3.2 环境变量与快捷函数 (`env.sh`)
- `export DIEC_PATH="D:/tools/die/diec.exe"`
- `export FLOSS_PATH="D:/tools/floss/floss.exe"`
- `readie <target>`：快速查编译器与壳
- `reaentropy <target>`：快速扫 Section 熵
- `reafloss <target>`：快速解密栈与混淆字符串
- `reatriage <target>`：一键全景分诊

---

## 四、测试与反向验证（Mutation Testing）

自动化测试套件包含在 `test-dotnet-chain.sh` 的第 18 组中：
```
npm run check  →  14 个 .sh + 10 个 .java 语法检查 OK (check_exit=0)
npm test       →  24 通过 / 0 失败
                  115 通过 / 0 失败 (test_exit=0)
总计 139 条断言全绿，0 失败。
hermes verify --json: ok=true (npm install + npm test + npm check 全绿)
```

**双重反向验证实证记录**：
1. **反向验证 A（分诊 JSON 字段破坏）**：将 `obfuscated_strings` 篡改为 `corrupted_strings`，测试断言阻断：`FAIL 分诊 JSON (114 通过 / 1 失败)`，恢复后回升至 115。
2. **反向验证 B（栈字符串断言破坏）**：将断言目标改为不存在的 `Nonexistent_StackStr!`，测试断言双重阻断：`FAIL FLOSS 栈字符串` + `FAIL 分诊 JSON (113 通过 / 2 失败)`，恢复后回升至 115。
