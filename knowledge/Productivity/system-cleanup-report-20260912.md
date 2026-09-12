---
title: "系统清理报告 2026-09-12"
type: note
domain: Productivity
status: active
tags: [knowledge/productivity, windows, 系统清理, 运维监控]
date: 2026-09-12
---

# 系统清理报告 2026-09-12

**结论：共释放约 2GB，C 盘可用 182G → 184G（使用率 60% → 59%）**

## 清理明细

| 类别 | 路径 | 清理前 | 清理后 | 释放 |
|:---|:---|:---|:---|:---|
| 用户 Temp | %LOCALAPPDATA%\Temp | 1.5G | 103M | ~1.4G |
| npm 缓存 | %LOCALAPPDATA%\npm-cache | 688M | 21M | ~667M |
| uv 缓存 | %LOCALAPPDATA%\uv\cache | 134M | — | ~134M |
| Chrome Cache | …\Default\Cache | 244M | — | ~244M |
| Chrome Code Cache | …\Default\Code Cache | 177M | — | ~177M |
| Chrome Service Worker | …\CacheStorage | — | — | 部分 |
| pip 缓存 | %LOCALAPPDATA%\pip\cache | 34M | — | ~34M（5449 目录） |
| 系统 Temp | C:\Windows\Temp | 30M | — | ~30M |
| Edge Cache | …\Edge\Default\Cache | 25M | — | ~25M |
| Hermes 轮转日志 | %LOCALAPPDATA%\hermes\logs\*.1/.2/.3 | 14M | — | ~14M |
| C:\c 孤儿目录 | C:\c（npm 全局副本） | 3.6M | 已删 | 3.6M |
| 回收站 | C:\$Recycle.Bin | 544M | 540M | 仅 4M |

## 清理后 C 盘

- 已用 266G → 264G，可用 182G → 184G

## 保留未动

- **回收站 540M 残留**：`.xxx` 前缀孤儿暂存文件（188M + 177M + 30M 等，多为 Edge/下载工具写入），被进程持有句柄，`Clear-RecycleBin` 反复执行删不掉、`Remove-Item` 也失败——属正常（坑 6/8 记录类型）。重启浏览器类进程后可再清，非紧急。
- hermes-agent 安装本体（~8G）——运行必需，不删
- pagefile.sys / hiberfil.sys —— 只报告不动（系统虚拟内存/休眠文件）

---
> 🗺️ 属于 [[MOC-Productivity]] · [[Home|🏠 Home]]
