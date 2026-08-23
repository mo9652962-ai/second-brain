# KiCad SWIG→kipy(IPC API) 迁移兼容性测试报告（2026-08-23）

## 测试结论

| 项 | 结果 |
|:--|:---|
| kipy 安装 | ✅ `pip install kicad-python` → 0.7.1（**导入名是 `kipy`，不是 kicad/kicad_python**）|
| 依赖（pynng + protobuf） | ✅ 自动就位 |
| API 表面静态验证 | ✅ Board.get_footprints / get_tracks / begin_commit / drop_commit 全部存在（61 方法）|
| KiCad 版本 | ✅ 本机 10.0.5（IPC API 支持从 9.0 起）|
| api.enable_server 配置 | ✅ 已写入 kicad_common.json（原为 false，已改 true）|
| **kicad-cli api-server（headless）** | ❌ **KiCad 10 无此子命令——11.0 功能**。此前 devlist 公告理解有误：11 nightlies 移除 SWIG + 新增 cli api-server 是配套的 |
| GUI 连接级测试 | ⏸ 需打开 KiCad GUI 后跑（server 随 GUI 启动）|

## 关键修正

之前研究说「kicad-cli api-server 提供 headless 模式」——实测那是 **KiCad 11 的能力**。
KiCad 10.0.5 的 IPC 连接必须开 GUI（Preferences > Plugins 里 server 开关，现已通过
kicad_common.json 直接启用）。

## 迁移映射表（wave-fixture-ai 用到的 SWIG 能力 → kipy）

| SWIG pcbnew | kipy IPC |
|:---|:---|
| `pcbnew.LoadBoard(path)` | `ki.get_board(path)`（GUI 打开后）|
| `board.GetFootprints()` | `board.get_footprints()` ✅ |
| `fp.GetReference()` | `fp.reference`（.value 取字符串）|
| `board.GetTracks()` | `board.get_tracks()` ✅ |
| `board.GetDrawings()` | ⚠️ 方法名待连接后确认（61 方法中无精确名）|
| Edge_Cuts 轮廓提取 | 待运行时确认 |
| 保存 | `begin_commit` / `drop_commit` 提交流程 ✅ |

## 错误类型（迁移时 catch 用）

```python
from kipy.errors import ApiError, ConnectionError, FutureVersionError, ApiStatusCode
```

## 迁移决策

1. **现在不必急迁**：本机锁 KiCad 10.0.5（不升 11），SWIG 脚本继续可用
2. **新代码用 kipy 写**：波峰焊治具等新功能直接走 IPC，避免存量扩大
3. **下次打开 KiCad GUI 时补连接级测试**：验证 get_footprints/get_tracks 实际往返
4. **升级 KiCad 11 前必须完成迁移**：11 移除 SWIG，届时旧脚本全废
5. 坑已记录：pip 包名 kicad-python ≠ 导入名 kipy；10 无 headless server
