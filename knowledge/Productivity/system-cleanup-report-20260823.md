---
title: "系统清理报告 2026-08-23"
type: note
domain: Productivity
status: active
tags: [knowledge/productivity]
source: null
---
# 系统清理报告 2026-08-23

**结论：共释放约 8 GB，C 盘可用 207 GB → 215 GB（使用率 54% → 53%）**

## 清理明细

| 类别 | 路径 | 清理前 | 清理后 | 释放 |
|---|---:|---:|---:|
| 用户临时文件 | `%TEMP%` | 2.0 G | 62 M | ~1.94 G |
| 系统临时文件 | `C:\Windows\Temp` | 1.5 G | 512 K | ~1.5 G |
| npm 缓存 | `%LOCALAPPDATA%\npm-cache`（含 `_npx` 残留） | 1020 M | 2.3 M | ~1018 M |
| pip 缓存 | `%LOCALAPPDATA%\pip\cache` | 313 M | 901 K | ~312 M |
| Chrome 缓存 | `...\Chrome\User Data\Default\Cache` | 387 M | 5 K | ~387 M |
| Chrome 代码缓存 | `...\Default\Code Cache` | 310 M | 0 | ~310 M |
| Chrome 离线缓存 | `...\Default\Service Worker\CacheStorage` | 299 M | 4 K | ~299 M |
| Edge 缓存 | `...\Edge\User Data\Default\Cache` | 270 M | 5 K | ~270 M |
| 回收站 | `C:\$Recycle.Bin` | ~1.7 G | 527 M 残留 | ~1.2 G |
| 孤儿目录 | `C:\c`（已确认真身不存在于正常路径） | 91 M | 0 | 91 M |
| Hermes 轮转日志 | `%LOCALAPPDATA%\hermes\logs\*.1/.2/.3` | ~20 M | 0 | ~20 M |
| uv 缓存 | `%LOCALAPPDATA%\uv\cache` | 6 K | ~0 | ~0 |

## 保留未动（说明）

- **回收站残留 527 M**：`.MSYS` 恢复文件（7月25日）被某进程持有句柄，`Clear-RecycleBin` 删不掉——重启持有进程后可清，正常现象，不影响使用。
- **Hermes 安装本体**（`%LOCALAPPDATA%\hermes` ~8 G）：venv + node_modules + .git，运行必需，未动。
- **pagefile.sys / hiberfil.sys**：系统文件，只报告不动。`powercfg /h off` 可再省 ~6 G（关休眠/快速启动，需用户确认）。
- **当前日志**（`agent.log`/`desktop.log`/`errors.log` 等）：仅删轮转备份（.1/.2/.3），当前正在写入的保留。

## 建议

- 如需进一步释放：`powercfg /h off`（~6 G，需确认后执行）、D 盘大文件归档（游戏/安装包）。
- 清理频率：当前 2-3 周一轮，单轮稳定释放 8-13 G，节奏合适。

---
> 🗺️ 属于 [[MOC-Productivity]] · [[Home|🏠 Home]]
