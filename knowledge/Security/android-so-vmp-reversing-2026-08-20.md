# 安卓 SO 层 VMP 逆向研究（2026-08-20 千轮研究）

> 承接：VMP 脱壳学习笔记（PC 版，vmp-reversing-2026-08-20.md）→ 安卓 SO 层专题
> 来源：看雪（金罡/简单的简单/0xbad/商业级加固实战）+ CTF 导航 + VmpProject + MogVMP + 学术（VMPP）+ SRC 实战（SecurityGuard x-sign）
> 关联：SRC 移动端审计（小程序/APP SO 加固对抗）

## 背景

- VMProtect **2025-10 起支持 Android ARM64**（此前仅 x86/x64）
- 国内商业加固（梆梆/爱加密/某企业版 com.secneo 等）均有自研 VMP 化 SO 保护
- 核心机制：ARM64 指令 → 自定义 VM 字节码 → 运行时解释执行（VmpProject 开源实现可对照学习）

## 检测特征（识别 SO 有 VMP）

| 特征 | 说明 |
|:---|:---|
| vm_entry | 被虚拟化函数内部 = 只跳转 vm_entry（callee 改、caller 不变）|
| vm_entry 规则 | 单函数调用 + 调用后恢复栈帧 + 直接 RET + 被多处调用 |
| IDA F5 失败 | 间接跳转对抗（目标地址 = 返回地址 + *(返回地址 + 索引×4)）|
| 二级跳转表 | 稀疏 case 的 switch（.data.rel.ro 数据块伪装代码）|

## 分析思路（金罡/简单的简单方法论）

```
① 定位 vm_entry（特征扫描脚本）
② 脚本把间接跳转 → 直接跳转 → Patch 保存 so
③ 重新加载 IDA → F5 正常反编译
④ 主分发器 switch → case 对应 handler 语义
⑤ 复杂样本: 二级跳转表改一级（从下往上 BR->LDR->LDR->ADD，case 存 X16，两条 LDR NOP）
⑥ .data.rel.ro 数据块修复（指向新地址避免被识别成代码）
```

## 工具链全景

| 工具 | 用途 | 场景 |
|:---|:---|:---|
| **unidbg** | 桌面模拟执行 SO（Unicorn/Dynarmic 后端）| ⭐ 黑盒调用首选 |
| **Frida** | 动态 hook | 简单场景（商业壳检测注入）|
| **定制 ROM**（SysTrace）| Dobby/SandHook/Xposed/ROM 打桩 + setup_stealth | 对抗内核级检测 |
| ghost_dumper | /proc/pid/mem 带外读取（不 attach 不 ptrace）| 商业壳脱壳 |
| VmpProject | 开源 ARM64 VMP（68★）| 学习材料 |
| xVMP / nmmp | 开源 VMP demo | 学习 |
| MogVMP | LLVM 反虚拟化（语义提升+优化折叠）| 研究向 |
| 内核级脱壳机 | perf_event 硬件断点 + 时间冻结 + ELF 缝合 | 高级对抗 |

## SRC 移动端审计实战策略（重点）

> **核心认知：不一定要逆 VMP——黑盒调用绕过它拿结果。**

### 策略 A：unidbg 黑盒调用（推荐）
```
① AndroidEmulatorBuilder.for64Bit() + AndroidResolver(23) 建模拟器
② vm.createDalvikVM(apk)（自动做部分签名校验）
③ loadLibrary(so) → callJNI_OnLoad（触发动态注册）
④ callStaticJniMethodObject 调目标函数 → 拿结果
⑤ unidbg-boot-server 起 RPC → Python 实时调用
案例: 某宝系 SecurityGuard x-sign（3 天，Gemini+Claude 补环境）
案例: 某麦 doCommandNative 需按顺序喂 22 个初始化指令（状态累积）
```

### 策略 B：Frida hook 绕过（轻量）
```
① hook 关键函数入口/出口（token/time 检查）
② 强制改返回值绕过检查（ca → return true）
③ hook JNI 接口（FindClass/GetStaticMethodID/NewStringUTF）看调用链
```

### 策略 C：商业加固 DEX 脱壳（需要时）
```
① 解密时机: Bangcle 8-12 秒, 等 libDexHelper 加载完（grep /proc/PID/maps）+ 12s 后 dump
② 双击启动: 首次必闪退（壳初始化检测），第二次正常解密
③ Zero-Break 读取: /proc/pid/mem + pread 带外读（不触发调试检测）
④ Fake Size 对抗: 壳篡改 DEX file_size 字段 → 超量采集（32MB 阈值）
⑤ checksum 修复: fix_dex_checksum_full.py 重算 → jadx 识别
```

## 关键坑

1. **unidbg 版本**：0.9.8 比最新版稳（某麦实战结论）
2. **getStackTrace() 不能返回空**：要模拟真实堆栈，否则风控检测不过
3. **大厂 so 会检测 unidbg**：多线程/环境指纹/进程名校验 → 补环境可能极耗时
4. **VMP 保护范围**：常保护「参数解析 + methodID 分发」（Instruction Stealing），算法本身可能是标准实现（如 AES KeyGenerator）——**别被 VMP 吓住，先看它保护的是什么**
5. **静态 dump 基址坑**：自定义 mmap2（svc 63505）分配的 RWX 段 ≠ module.base+offset

## 合规

- 仅分析：自己 APK / 已授权样本 / SRC 授权范围内资产
- 商业 APP 逆向仅限授权渗透测试（SRC scope 内）
- 黑盒调用注意：只读请求 / 最小影响 / 不拖数据

---
> 🗺️ 属于 [[MOC-Security]] · [[Home|🏠 Home]]
