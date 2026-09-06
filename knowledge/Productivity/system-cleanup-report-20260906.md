# 系统清理报告 2026-09-06

**结论：共释放约 7 GB，C 盘已用 248G → 241G（使用率 56% → 54%，可用 200G → 207G）**

## 清理明细

| 类别 | 路径 | 清理前 | 清理后 | 释放 |
|---|---|---|---|---|
| 用户 Temp | `%TEMP%` | 2.4G | 69M | ~2.33G |
| Windows Temp | `C:\Windows\Temp` | 53M | 0.5M | ~52M |
| pip 缓存 | `%LOCALAPPDATA%\pip\cache` | 113M | 1.2M | ~112M |
| uv 缓存 | `%LOCALAPPDATA%\uv\cache` | 254M | 0 | 254M |
| npm 缓存 | `%LOCALAPPDATA%\npm-cache`（含 _npx） | 964M | 2.6M | ~961M |
| Chrome 缓存 | Cache + Code Cache + SW CacheStorage | 1.33G | ~9K | ~1.33G |
| Edge 缓存 | `...\Edge\...\Cache` | 79M | 0 | ~79M |
| Hermes 轮转日志 | `agent.log.1-3` + `errors.log.1-2` | ~20M | 0 | ~20M |
| 孤儿目录 | `C:\c`（npm 全局包副本，13081 文件） | 数百MB | 0 | 数百MB |
| 回收站 | `C:\$Recycle.Bin` | ~1.1G | 540M（残留） | ~560M |

## 保留未动（说明）

- **回收站残留 540M**：`S-1-5-21-...-1001` 下 `.xxx…` 前缀暂存文件（含 188M + 177M 两个大文件，8 月日期），被某进程持有句柄，`Clear-RecycleBin` 与直接删除均失败——属已知正常现象，重启持有进程（疑似 Edge/下载工具）后可清。
- **Hermes 安装本体**（~8G：venv/node_modules/.git）：运行必需，不删。
- **pagefile.sys / hiberfil.sys**：系统文件，只报告不动；`powercfg /h off` 可省 ~6.3G 但关休眠/快速启动，需用户确认后才执行。
- **uv cache 已整体清空**（官方工具 `uv cache clean`，非手删）。

## 建议（可选，下次可做）

1. 回收站残留重启 Edge/浏览器后重新清理，预计再释放 ~540M。
2. 磁盘占用大头仍是安装本体与数据，如需更大空间需用户确认是否关休眠/迁移大目录。

---
> 🗺️ 属于 [[MOC-Productivity]] · [[Home|🏠 Home]]
