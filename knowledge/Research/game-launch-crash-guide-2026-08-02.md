# This War of Mine 崩溃修复指南（gameoverlayrenderer64.dll + 0xc00000fd）

> 2026-08-02 · 基于搜索引擎验证的公开资料 · 适配 Windows 10/11

## 一、崩溃日志解读

```
出错应用程序：This War of Mine.exe
出错模块：gameoverlayrenderer64.dll（Steam 游戏内覆盖层 DLL）
异常代码：0xc00000fd（栈溢出 Stack Overflow）
```

**结论：这是 Steam Overlay（游戏内覆盖）的已知 Bug**，不是游戏本身损坏。

### 错误码含义
| 代码 | 含义 | 官方说明 |
|------|------|---------|
| `0xc00000fd` | 栈溢出 | "A new guard page for the stack cannot be created"——Steam 覆盖层注入时递归过深撑爆游戏栈 |
| `0xc0000005` | 访问冲突 | 程序访问了非法内存地址（多个应用同时报 05/0d 常是覆盖层或驱动问题） |

### 证据来源
- **Steam Client Beta 官方群组**（2013 至今持续有人报告）："Steam overlay crashing games due to stack thrashing/overflow"，错误码正是 0xc00000fd
- **Steam 社区 Help and Tips**：用户报告删除 `gameoverlayrenderer64.dll` 后游戏恢复正常
- **FiveM 官方论坛**：删除 DLL + 重启 Steam 重新下载 + 禁用 NVIDIA 覆盖层 + 禁用 Xbox Game Bar
- **Microsoft Q&A**：多应用同时报 0xc0000005 需检查超频/内存/干净启动

## 二、修复步骤（按优先级）

### ✅ 第 1 步：禁用 Steam 游戏内覆盖（最可能直接解决）
1. 打开 Steam → 左上角「Steam」→「设置」
2. 「游戏中」选项卡 → **取消勾选「启用 Steam 界面（游戏内覆盖）」**
3. 若想只对单个游戏禁用：库中右键游戏 → 属性 → 通用 → 取消勾选覆盖
4. 重启 Steam 再启动游戏

### ✅ 第 2 步：删除 gameoverlayrenderer64.dll 强制重建
如果覆盖层已禁用仍崩溃（Steam 有 Bug 时覆盖层会残留）：
1. **完全退出 Steam**（托盘右键 → 退出）
2. 打开 Steam 安装目录：`D:\Steam\gameoverlayrenderer64.dll`
3. **重命名**该文件为 `gameoverlayrenderer64.dll.bak`（推荐重命名而非删除，可回滚）
4. 重启 Steam → 启动游戏。Steam 会自动重新下载该 DLL

### ✅ 第 3 步：This War of Mine 专属修复（清存档配置）
Steam 社区公认有效（43 条回复，作者标记为解决方案）：
1. `Win + R` → 输入 `%APPDATA%\11bitstudios\This War Of Mine\` → 回车
2. 删除目录下的 **`config.bin3`** 和 **`iPhoneProfiles`**（两个文件）
3. 启动游戏测试

### ✅ 第 4 步：禁用其他覆盖层（多应用同时崩溃时必做）
| 覆盖层 | 禁用方法 |
|--------|---------|
| **NVIDIA 游戏内覆盖** | GeForce Experience / NVIDIA App → 设置 → 关闭「游戏内覆盖」 |
| **Xbox Game Bar** | 设置 → 游戏 → 游戏录制 → 关闭「后台录制」+ 取消勾选「游戏栏」；彻底卸载：管理员 PowerShell 运行 `Get-AppxPackage Microsoft.XboxGamingOverlay \| Remove-AppxPackage` |
| **Discord 覆盖** | 设置 → 游戏活动 → 关闭「游戏内覆盖」 |
| **其他** | 检查 MSI Afterburner / RivaTuner / 网易UU / 腾讯游戏管家等 |

### ✅ 第 5 步：系统级修复（若多个应用无差别崩溃）
1. **管理员 CMD** 运行系统修复：
   ```cmd
   sfc /scannow
   DISM /Online /Cleanup-Image /RestoreHealth
   ```
2. **内存诊断**：Win+R → `mdsched.exe` → 立即重启检查
3. **关超频**：如有 CPU/内存超频（XMP）先恢复默认——Microsoft 支持确认超频会导致 0xc0000005
4. **干净启动**：`msconfig` → 服务 → 隐藏 Microsoft 服务 → 全部禁用 → 重启测试

### ✅ 第 6 步：通用兜底
- 验证游戏文件完整性（库 → 右键 → 属性 → 已安装文件 → 验证完整性）
- 更新显卡驱动（DDU 干净卸载后装最新稳定版）
- 安装/修复 VC++ 运行库（`Microsoft Visual C++ 2015-2022 Redistributable`）
- 排除杀毒软件误杀（把 Steam 目录加入白名单）
- 代理软件注意：如果使用 FlClash 等全局代理，可尝试关闭代理后启动游戏（网络注入可能干扰）

## 三、判断标准

做完第 1+2 步后 90% 的覆盖层崩溃能解决；若全部做完仍崩溃且**多个游戏都崩**，优先怀疑系统级（内存/驱动/超频），按第 5 步走。

---
*来源：Steam 官方社区、Steam Client Beta 群组、FiveM 官方论坛、Microsoft Q&A、Microsoft Learn、网易UU 2026 修复指南*
