# 系统清理报告 2026-09-13

**结论：共释放约 1.6 GB，C 盘已用 269G → 268G（61% → 60%，可用 179G → 180G）。**
本轮回存量较 09-06 轮（7GB）小：Temp 仅 1.3G、无 npm 孤儿重现、无标准回收站条目可清。回收站 `.xxx` 残留 538.7M 仍被进程持有句柄，属已知项。

## 清理明细

| 类别 | 路径 | 清理前 | 清理后 | 释放 |
|---|---|---|---|---|
| 用户 Temp | `%TEMP%` | 1.3G | 232M | ~1.07G |
| Windows Temp | `C:\Windows\Temp` | 9.7M | 420K | ~9.3M |
| pip cache | `%LOCALAPPDATA%\pip\cache` | 427K | 23K | ~0.4M |
| uv cache | `%LOCALAPPDATA%\uv\cache` | 291M | 16K | ~291M（官方输出 539.9MiB） |
| npm cache（含 _npx） | `%LOCALAPPDATA%\npm-cache` | 106M | 21M | ~85M |
| Chrome Cache | `Chrome\User Data\Default\Cache` | 75M | 1K | ~75M |
| Chrome Code Cache | `...\Default\Code Cache` | 30M | 0 | ~30M |
| Chrome SW CacheStorage | `...\Default\Service Worker\CacheStorage` | 21M | 4K | ~21M |
| Edge Cache | `Edge\User Data\Default\Cache` | 0 | 0 | 0 |
| Hermes 旧日志 | `hermes\logs\bootstrap-*` 等 | ~1M | 0 | ~1M |
| **合计** | | | | **~1.6 GB** |

## 保留未动（说明）

| 项 | 状态 | 说明 |
|---|---|---|
| 回收站 `.xxx` 残留 | 538.7M（100 个文件，8 月日期） | 非标准回收站条目（疑似 Edge/下载工具暂存），Clear-RecycleBin 忽略 + 被进程持有句柄删不掉。与 09-06 轮（540M）基本一致。**建议**：重启浏览器/下载工具后重试，删不掉属正常 |
| `$IF2QOSB.zip` / `$IXZIJRC` | 残留小文件 | 回收站孤儿元数据，Clear-RecycleBin 已跑，属占用残留 |
| hermes-agent 安装本体 | ~8G | venv/node_modules/.git，运行必需，绝不删 |
| mcp-stderr.log 17.7M | 保留 | 当前 mcp 服务可能在写，未动 |
| pagefile.sys / hiberfil.sys | 保留 | 系统文件只报告不动；`powercfg /h off` 可腾 ~12G（关休眠/快速启动，需用户确认） |
| C:\c 孤儿目录 | 未重现 | 09-06 轮已清，本轮检查不存在（好） |

## 可释放建议（未执行）

- 回收站残留 538.7M：重启持有进程（Edge/下载工具）后再次 Clear-RecycleBin + 手动 Remove-Item
- 休眠文件：`powercfg /h off` 可腾 ~12G，代价是关休眠/快速启动——需 sora 确认后执行
- 本轮释放量较小（1.6G vs 上次 7G），说明 Temp/缓存类堆积已处于低位；后续若 C 盘继续紧张，走技能第 9 节「不反弹底层优化」（DISM 清 WinSxS / 个人文件夹转 D 盘 / 组策略锁服务）

---
> 🗺️ 属于 [[MOC-Productivity]] · [[Home|🏠 Home]]
