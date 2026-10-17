---
title: "系统清理报告 2026-10-17"
type: report
domain: Productivity
status: done
tags: [knowledge/productivity, cleanup]
date: 2026-10-17
---

# 系统清理报告 2026-10-17

**结论：共释放约 10.0 GB，C 盘可用 34 GB → 44 GB（使用率 93% → 91%）**

## 清理明细（实测）

| 类别 | 路径 | 清理前 | 清理后 | 释放 |
|---|---|---|---|---|
| 用户 Temp | `%LOCALAPPDATA%\Temp` | 3,730.5 MB | 62.8 MB | **~3.67 GB** |
| uv 缓存 | `%LOCALAPPDATA%\uv\cache` | 1,266.8 MB | 0 MB | **~1.27 GB** |
| Windows Update 下载缓存 | `C:\Windows\SoftwareDistribution\Download` | 431.0 MB | 0 MB | ~431.0 MB |
| 回收站 | `C:\$Recycle.Bin` | 915.5 MB | 538.7 MB | ~376.8 MB（残留 538M 为句柄锁定项） |
| npm 缓存（含 `_npx`） | `%LOCALAPPDATA%\npm-cache` | 386.9 MB | 0 MB | ~386.9 MB |
| CBS 系统日志 | `C:\Windows\Logs\CBS` | 266.0 MB | 0.3 MB | ~265.7 MB |
| Chrome 缓存（含 Code Cache） | `%LOCALAPPDATA%\Google\Chrome\...` | 177.7 MB | 0 MB | ~177.7 MB |
| Edge 缓存 | `%LOCALAPPDATA%\Microsoft\Edge\...` | 94.3 MB | 0 MB | ~94.3 MB |
| WinSxS 组件存储 | `C:\Windows\WinSxS` | DISM 发现 4 个可回收包 | 已执行组件清理 | **~3.0+ GB**（实际回收） |
| 系统 Temp | `C:\Windows\Temp` | 18.8 MB | 0.3 MB | ~18.5 MB |
| pip 缓存 | `%LOCALAPPDATA%\pip\cache` | 14.8 MB | 0 MB | ~14.8 MB |
| Hermes 轮转日志 | `%LOCALAPPDATA%\hermes\logs`（.1/.2/.3） | ~12.5 MB | 0 MB | ~12.5 MB |

## 保留未动（安全边界）

| 项 | 大小 | 原因 / 属性 |
|---|---|---|
| `%LOCALAPPDATA%\hermes` 安装本体 | ~8.0 GB | 运行必需（venv + node_modules + .git），系统命脉，绝不删 |
| `~/.cache/codex-runtimes` | 2.0 GB | Codex 运行环境，编码工作流必需，保留 |
| `C:\Recovery` | 6.5 GB | **系统恢复分区数据，安全红线绝不碰** |
| `C:\eSupport` | 6.5 GB | 华硕出厂驱动备份，刷机/救砖必备，未获授权不动 |
| `~/.cache/hyperframes` | 423.6 MB | Hyperframes 运行依赖/素材缓存，保留 |
| `C:\swdist\SOLIDWORKS_2026_sp04.1` | 275.5 MB | SOLIDWORKS 安装残留，需用户拍板确认后再清 |
| 用户工作区与私有知识库 | - | Documents / Desktop / private_knowledge 等全部遵守安全隔离，只读不触碰 |

## 可进一步释放（需确认后操作）

1. **Downloads 目录大安装包残留（共约 2.3 GB）**：
   - `WorkBuddy-setup.exe` 及副本 3 个：共约 **1.2 GB**（软件若已装好，安装包可清）
   - `δȷ 330980.crdownload`：**341 MB**（Chrome 未完成下载残留碎片）
   - `ocs-2.9.24-setup-win-x64.exe`：**260 MB**
   - `wechat_devtools_2.02.2608080_win32_x64.exe`：**182 MB**
   - `r2modman-3.2.20.exe`：**156 MB**
   - `LeiGodSetup.11.3.2.9.exe`：**139 MB**
2. **`C:\swdist\SOLIDWORKS_2026_sp04.1`**：**275.5 MB**（安装包残留）
3. **休眠文件 `hiberfil.sys`（6.7 GB）**：如不使用 Windows 休眠功能，执行 `powercfg /h off` 可直接腾出约 **6.7 GB**。

## 安全协议遵守自检
- ✅ 零误伤：未擅自删除任何 Downloads、Documents、Desktop 用户个人文件或源码。
- ✅ 资产隔离：严格遵守资产隔离，绝不触碰核心资产与敏感配置。
- ✅ 官方工具优先：包管理器调用官方清理命令，组件存储调用 DISM 官方模块。
