# 系统清理报告 2026-08-16

**结论：共释放约 6.0 GB，C 盘已用 232G → 227G，可用 216G → 221G（使用率 52% → 51%）**

## 清理明细

| 类别 | 路径 | 清理前 | 清理后 | 释放 |
|---|---|---|---|---|
| 用户 Temp | `%TEMP%` | 2.50 G | 55 M | ~2.45 G |
| Windows Temp | `C:\Windows\Temp` | 1.90 G | 8.2 M | ~1.89 G |
| npm 缓存（含 _npx） | `%LOCALAPPDATA%\npm-cache` | 918 M | 1.3 M | ~917 M |
| Chrome 缓存 | `...\Chrome\User Data\Default\Cache` | 352 M | 5 K | ~352 M |
| 回收站 | `C:\$Recycle.Bin` | 896 M | 539 M | ~357 M |
| pip 缓存 | `%LOCALAPPDATA%\pip\cache` | 31 M | 675 K | ~30 M |
| Edge 缓存 | `...\Edge\User Data\Default\Cache` | 66 M | 5 K | ~66 M |
| Hermes 轮转日志 | `%LOCALAPPDATA%\hermes\logs` | 39 M | 20 M | ~19 M |

> uv cache 本轮不存在（上一轮已清，无需处理）。

## 保留未动（说明）

| 项目 | 大小 | 原因 |
|---|---|---|
| hermes-agent 安装本体 | 9.2 G | venv/node_modules/.git，运行必需 |
| hermes/node | 1.2 G | Hermes 运行时 node，必需 |
| state.db / backups / chrome-profile | ~500 M | 数据库/备份/浏览器会话，保留 |
| 回收站残留 | 539 M | **被进程占用句柄的已删文件**（7/25、8/15 删除的 `$R` 恢复文件），`Clear-RecycleBin` 反复执行无法删除——重启相关进程释放句柄后可再清。 |

## 备注

- **npm-cache `_npx`（425M）**：`npm cache clean --force` 不清它，本轮手动补删——npx 临时包缓存，安全（需要时会自动重下）。
- 占用的 Temp/缓存大文件（Temp 2.5G→55M 后残留部分被其他进程锁定）属正常，跳过。
- 相比上轮（2026-08-09，48%→45% 释放 13.1G）：本轮增量积累约 6G，清理节奏合理（建议 2-3 周一轮）。