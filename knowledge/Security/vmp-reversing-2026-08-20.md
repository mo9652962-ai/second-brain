# VMP 脱壳学习笔记（洛洛-软件开发 · 抖音 2026-08-20）

> 来源：抖音 @洛洛-软件开发《更新一期vmp学习必看思路》（04:18，逆向开发/安卓逆向/软件破解）
> 处理：Playwright 拦截下载 → ffmpeg 提音频 → **SenseVoice 转写**（40.9s，口播模糊但要点提取成功）+ 页面章节要点 + 千轮研究交叉验证（看雪/吾爱破解/CN-SEC/0xrafasec）

## 视频核心内容（增强转写提取）

**VMP（VMProtect）加壳 64 位程序一键脱壳 + 修复 SDK 虚拟化函数**：

### 工具链（4 个）
- **X64**（X64Dbg 调试器）——主调试/脱壳
- **DVG**——脱壳辅助工具（视频演示流程）
- **CF**——导入表/导出函数修复
- **StuPE**（StudPE）——PE 修改/修复重定位

### 脱壳流程（视频 + 研究交叉验证）
```
① 运行加壳程序 → 定位入口（[esp-4] 硬断 = OEP，esp 定律）
② 内存转储（dump）→ 记录头地址/计算地址大小
③ 关闭冲击位（PE 头标志修复）
④ 转储内存为 .de 文件（修复用）
⑤ 添加导出函数/导入表修复（拖入 DLL 添加导入表）
⑥ 修复重定位（relocation）
⑦ 填写文本地址（16 进制地址回填）
⑧ 跨平台测试（复制到另一台电脑运行验证）
```

## VMP 原理（研究补充）

### 保护方式（三种）
| 方式 | 原理 | 强度 |
|:---|:---|:---|
| 虚拟化 Virtualization | 原始 x86 指令 → 私有字节码 → 运行时解密 handler 表执行 | 最强 |
| 变异 Mutation | 控制流混淆 + 常量加密 | 中 |
| 水印 Watermark | 植入版权标记 | - |

### VMP 虚拟机核心概念
- **vStack**：VMP 自建虚拟栈（不是 rsp 指向的栈）
- **vReg**：虚拟寄存器（寄存器轮转：运行一段后映射关系改变）
- **万用门**：NAND/NOR 模拟所有逻辑运算（`not(a)=P(a,a)`）
- **去中心化 Dispatcher**（VMP3.x）：handler 尾部 push+ret 跳转，静态无法确定下一个 handler
- **垃圾指令**：无效指令混淆（对 VMP 是无效指令不是花指令）
- **密钥链**：每轮解密后生成新密钥（静态无法解密字节码）

### 反调试（高版本 VMP 3.8-3.9）
| 技术 | 绕过 |
|:---|:---|
| PEB BeingDebugged | ScyllaHide 清 flag |
| NtQueryInformationProcess DebugPort | 返回值置 0 |
| DebugObjectHandle | rax 置 C0000353 |
| ZwSetInformationThread hidefromdebugger | rdx 置 0 |
| rdtsc 随机 syscall | Unicorn 模拟跟踪 rdtsc 下一条指令断点 |
| NtClose 无效句柄 | rax 置 C0000008 直接 ret |
| 壳代码自校验 | 段首字节硬断找 jne 次数 |
| 增量链接检测 | 模拟执行 push/pop/xchg/mov/lea 遇 ret 停 |

### 脱壳关键技术
- **找 OEP**：esp 定律 / [esp-4] 硬断（VMP 通过 ret 跳转 OEP）/ 二次内存断点
- **IAT 修复**：Scylla → IAT Autoscan（OEP 上下文）→ Dump → Fix Dump
- **IAT 特征**：加密 API 调用（`mov reg,[addr]; call reg` / `call [addr]` / `jmp [addr]`）→ call 后地址首字节 0x90(nop)
- **重定位修复**：PE-bear / StudPE 修复 section 头
- **SDK 虚拟化函数修复**：视频重点——转储 + 导函数 + 重定位修复后程序可运行
- **反虚拟化**：VTIL（VMProtect Translator IL，需干净 dump 输入）/ 模拟执行 / 硬件断点时间线（HWBP 观察 SMC 自修改）

### 工具全景
| 工具 | 用途 |
|:---|:---|
| X64Dbg + ScyllaHide | 调试 + 反反调试 |
| Scylla | IAT 扫描/修复 |
| PE-bear | PE 查看/修复 |
| StudPE | PE 修改 |
| VTIL | 反虚拟化 |
| Unicorn | 模拟执行（过反调试）|
| IDA + Appcall | 静态分析 |

## ⚠️ 合规红线

- 逆向分析仅限：**自己开发的程序 / 已授权样本 / 学习研究目的**
- VMP 是商业保护产品——对他人商业软件脱壳/破解 = 侵权违法（软件著作权）
- 本笔记定位：**学习 VMProtect 保护原理与逆向工程思路**（防御视角 + 学术研究）
- 不传播破解工具、不协助绕过授权验证、不用于盗版分发

## 与 sora 相关性

- **防御视角**：理解 VMP 反调试/虚拟化原理 → 自己写程序时知道怎么保护（Android 逆向同理）
- **安卓逆向标签**：视频带 #安卓逆向——VMP 在 Android SO 层同样使用（VMP SDK for Android）
- 学习路径参考：看雪课程《VMProtect分析与调试器插件开发》（x32/x64Dbg 插件开发 + Handler 识别）
