---
tags: [cron, maintenance, system-cleanup, windows, report]
title: 系统清理报告 2026-09-15
type: report
created: 2026-09-15
status: adopted
---
# 系统清理报告 2026-09-15

**结论：共释放约 23 GB，C 盘已用 338G → 315G（使用率 76% → 71%，可用空间 110G → 133G）。**
本轮释放空间创下新高（前几轮通常在 1.6G ~ 7GB 之间），主要释放源为用户临时目录堆积的 ~22GB 临时垃圾，同时彻底清空了包管理器缓存（npm/uv/pip）与浏览器缓存。

## 清理明细

| 类别 | 路径 | 清理前 | 清理后 | 释放 |
|---|---|---|---|---|
| 用户 Temp | `%TEMP%` | 22.20 GB | 69.8 MB | **~22.13 GB** |
| Windows Temp | `C:\Windows\Temp` | 17.36 MB | 0.42 MB | ~16.9 MB |
| pip cache | `%LOCALAPPDATA%\pip\cache` | 129.0 MB | 0 | ~129 MB |
| uv cache | `%LOCALAPPDATA%\uv\cache` | 99.8 MB | 0 | ~99.8 MB |
| npm cache（含 _npx） | `%LOCALAPPDATA%\npm-cache` | 921.6 MB | ~20 MB | ~901 MB |
| Chrome Cache & Code Cache | `Chrome\User Data\Default\...` | 408.8 MB | 0 | ~408 MB |
| Edge Cache | `Edge\User Data\Default\Cache` | 130.1 MB | 0 | ~130 MB |
| Hermes 轮转旧日志 | `hermes\logs\agent.log.1 等` | ~7.2 MB | 0 | ~7.2 MB |
| D 盘工具安装包残留 | `EasyCLIProxyAPI-*.zip` | 30 MB | 0 | ~30 MB |
| **合计** | | | | **~23.8 GB** |

## 保留未动（说明）

| 项 | 状态 | 说明 |
|---|---|---|
| 回收站 `.xxx` 残留 | 538.7 MB | 非标准回收站条目（疑似 Edge/下载工具写入的暂存文件），`Clear-RecycleBin` 忽略且被系统/后台进程持有文件句柄，属已知正常现象 |
| hermes-agent 安装本体 | ~8 GB | venv / node_modules / .git，Agent 运行核心环境，绝不清理 |
| mcp-stderr.log | ~17 MB | 当前活动的 MCP 服务日志，保留以便排障 |
| 虚拟内存与休眠文件 | `pagefile.sys` / `hiberfil.sys` | 系统级核心文件，只报告不动；如需腾出 ~12G 可执行 `powercfg /h off`（关闭休眠） |
| 孤儿目录 `C:\c` | 未发现 | 本轮前置检查未发现该目录，未出现 npm 路径错乱重现 |

## 建议与后续

1. **临时文件定期监控**：本次用户 Temp 堆积达 22GB，主要是近期开发、大文件构建解压（如 Docker/APK/打包构建）产生的临时残余，建议每 2-3 周清理一次。
2. **回收站 538.7M 残留**：后续如果完全重启机器或退出浏览器，可再次清空回收站将其彻底擦除。

---
> 🗺️ 属于 [[MOC-Productivity]] · [[Home|🏠 Home]]
