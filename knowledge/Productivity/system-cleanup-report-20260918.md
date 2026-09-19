---
tags: [system-cleanup, productivity, report]
type: report
created: 2026-09-18
title: 系统清理报告 2026-09-18
---
# 系统清理报告 2026-09-18

**结论：共释放约 1.9 GB，C 盘可用 58G → 59G（使用率维持 88%，主要是清理了缓存与回收站残留）**

## 清理明细

| 类别 | 路径 | 清理前 | 清理后 | 释放 |
|---|---:|---:|---:|
| uv 缓存 | AppData/Local/uv/cache | 607M | 16K | ~607M |
| 回收站 .xxx 孤儿残留 | C:\$Recycle.Bin | ~500M+ | ~1K | ~500M |
| 用户 Temp | AppData/Local/Temp | 432M | 194M | ~238M |
| Chrome Cache | Chrome/Default/Cache | 212M | 5K | ~212M |
| npm 缓存（含 _npx） | npm-cache | 215M | 21M | ~194M |
| Chrome Code Cache | Chrome/Default/Code Cache | 99M | ~0 | ~99M |
| Chrome SW CacheStorage | Service Worker/CacheStorage | 32M | ~0 | ~32M |
| Edge Cache | Edge/Default/Cache | 20M | ~0 | ~20M |
| Hermes 轮转日志 | logs/*.log.1/.2/.3 | ~7M | ~0 | ~7M |
| pip 缓存 | pip/cache | 5M | ~0 | ~5M |
| Windows Temp | C:\Windows\Temp | 4.8M | ~0 | ~5M |

**合计约 1.9 GB**

## 保留未动（说明）

- **用户 Temp 残留 194M**：被运行中进程（Hermes / 浏览器）持有的临时文件，属正常，进程退出后可再清。
- **mcp-stderr.log 17.8MB**：Hermes 当前活跃日志（非轮转），未删。若长期堆积可考虑后续截断或加轮转。
- **安装本体**：hermes venv + node_modules + .git（~8G）为运行必需，绝不删。
- **C:\c 孤儿目录**：本次不存在，无需处理。

## 备注

- 回收站本次出现 `.xxx` 前缀孤儿暂存文件（Edge/下载工具残留），本次已随 Clear-RecycleBin 清空，未再被进程占用。

---
> 🗺️ 属于 [[MOC-Productivity]] · [[Home|🏠 Home]]
