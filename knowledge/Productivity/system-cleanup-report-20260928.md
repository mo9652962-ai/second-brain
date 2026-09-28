---
title: "系统清理报告 2026-09-28"
type: report
domain: Productivity
status: done
tags: [knowledge/productivity, cleanup]
date: 2026-09-28
---

# 系统清理报告 2026-09-28

**结论：共释放约 13.4 GB，C 盘可用 64.0 GB → 76.5 GB（使用率 86% → 83%）**

> 说明：本文件同日 11:19 曾存在一份旧版本（记录 7 GB，部分数字与实测不符）。本轮为独立完整清理，以下数字均为本轮实测，已覆盖旧内容。

## 清理明细（实测）

| 类别 | 路径 | 清理前 | 清理后 | 释放 |
|---|---|---|---|---|
| 用户 Temp | `%LOCALAPPDATA%\Temp` | 3.03 GB | 78 MB | ~2.95 GB |
| **`C:\tmp` CDP 浏览器临时配置** | `C:\tmp\chrome-*` 等 15 个 | 1.63 GB | 0 | **1.63 GB** |
| npm 缓存（含 `_npx`） | `%LOCALAPPDATA%\npm-cache` | 880 MB | 21 MB | ~860 MB |
| gradle 构建缓存 | `~\.gradle\caches` | 693 MB | 0 | ~693 MB |
| uv 缓存 | `%LOCALAPPDATA%\uv\cache` | 445 MB | 已清空 | ~445 MB |
| Windows Update 下载缓存 | `C:\Windows\SoftwareDistribution\Download` | 284 MB | 0 | ~284 MB |
| WinSxS 组件存储 | `C:\Windows\WinSxS` | 18.0 GB（表观） | 11.4 GB（表观） | ~6.6 GB（表观值，含硬链接，实际略低） |
| Chrome 缓存三件套 | `Cache` + `Code Cache` + `Service Worker\CacheStorage` | 413 MB | 0 | ~413 MB |
| Edge 缓存 | `...\Edge\Default\Cache` | 138 MB | 0 | ~138 MB |
| 回收站 | `C:\$Recycle.Bin` | 843 MB | 539 MB | ~304 MB（部分被句柄占用） |
| 系统 Temp | `C:\Windows\Temp` | 23 MB | 0.4 MB | ~22 MB |
| Hermes 轮转日志 | `%LOCALAPPDATA%\hermes\logs`（.1/.2/.3） | 48 MB | 29 MB | ~19 MB |
| pip 缓存 | `%LOCALAPPDATA%\pip\cache` | 1.6 MB | 0 | ~1.6 MB |

## 保留未动（安全边界）

| 项 | 大小 | 原因 |
|---|---|---|
| `%LOCALAPPDATA%\hermes` 安装本体 | ~8 GB | 运行必需（venv + node_modules + .git），删了 Hermes 直接废 |
| `~\AppData\Local\Docker\wsl\disk\docker_data.vhdx` | 10.7 GB | WSL2 虚拟磁盘。Docker 本体已不在「已安装程序」列表中（疑似卸载残留），但本机 HypervisorPresent=True，**需你确认是否还要 Docker** 再删 |
| `C:\Recovery\Customizations` | 6.5 GB | **系统恢复分区数据，绝不碰** |
| `C:\eSupport\eDriver\Software` | 6.5 GB | 华硕出厂驱动备份。刷机/重装驱动时是救命稻草，**需你确认** |
| `%LOCALAPPDATA%\hermes\backups\pre-update-20260925-152535` | 1.0 GB | **Hermes 更新还没执行**，这是更新前安全备份，更新成功后再删 |
| `~\AppData\Local\pnpm` | 874 MB | pnpm store，`pnpm` 命令当前不可用（corepack 路径损坏），暂不动 |
| `~\AppData\Local\hermes\backups\pre-migration-2026-07-23-094317.zip` | 89 MB | 历史迁移备份 |
| `C:\swdist\SOLIDWORKS_2026_sp04.1` | 276 MB | SOLIDWORKS 已装（注册表确认 2026 SP04.1 在 `C:\Program Files\SOLIDWORKS Corp`），此安装包为残留，**需你确认** |
| `C:\d\tmp_marketingskills` | 5.3 MB | git 仓库副本，可能被引用 |
| `C:\temp\memory_raw.txt` | 32 KB | 小，不动 |

## 可进一步释放（需你拍板）

| 操作 | 可释放 | 代价 |
|---|---|---|
| 删 `docker_data.vhdx`（Docker 已不用） | **~10.7 GB** | 丢失所有 Docker 镜像/容器（如不需要 Docker 则无损失） |
| 删 `C:\eSupport`（华硕驱动备份） | **~6.5 GB** | 失去出厂驱动离线备份（可从官网重下） |
| 删 SOLIDWORKS 安装包残留 | 276 MB | 无（软件已装） |
| `DISM ... /resetbase`（本轮只跑了 StartComponentCleanup） | 额外数 GB | 无法卸载已装更新 |
| 删 `pre-update-20260925` 备份 | 1.0 GB | **先完成 Hermes 更新**再删 |

> 三项大头（Docker / eSupport / SOLIDWORKS 残留）合计 **~17.5 GB**，确认后 C 盘可再降到 ~94 GB 可用。

## 安全边界执行记录

- ✅ 全部走官方工具（`pip cache purge` / `uv cache clean --force` / `npm cache clean --force` / `Clear-RecycleBin` / `DISM`）
- ✅ 删除前逐项目检：`C:\tmp\chrome-*` 已确认**无 Chrome 进程占用**才删
- ✅ 用户文档区（Documents / Pictures / Desktop / Downloads）**只读扫描，未删任何用户数据**
- ✅ `~\.cache\codex-runtimes`、`~\.vscode\extensions`、`hermes` 安装本体 **未动**
- ✅ 系统恢复分区 `C:\Recovery` **未动**

## 关联
- [[SOP-INDEX]] · 技能 `windows-system-cleanup`
