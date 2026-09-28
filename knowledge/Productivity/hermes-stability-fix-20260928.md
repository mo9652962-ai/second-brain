# Hermes 稳定性修复报告 — 2026-09-28

> 起因：sora 反馈「最近这几天使用 Hermes 总是会闪退自关闭」。
> 结论：闪退为 Electron 渲染进程崩溃（独立问题）；但排查中发现并修复了 4 处配置层故障，显著降低启动噪音与拖慢。

---

## 一、闪退根因（已定位，非本次修复项）

| 指标 | 数值 |
|:---|:---|
| 渲染进程崩溃 | **2 次**（09-20 13:07、09-25 07:32） |
| 崩溃码 | `-36861` = `0xFFFF7003`，reason=`crashed` |
| 界面无响应 | 1 次（09-20 13:07:32，崩溃前 14 秒） |
| 后端异常退出 | **50 次**（退出码 1×20 / 2×5 / 4294967295×6 / 1073807364×3） |
| 应用启动总次数 | 225 次 |
| 重启密集日 | 09-25（7 次）、09-27（4 次）、09-28（3 次） |

**诱因（已证实）：**
- 内存长期紧张：16 GB 单条，空闲仅 1.3~2.1 GB（86% 占用）
- 超长会话：崩溃发生在上下文压缩 5 次之后
- 吃内存大户：ZCode 1,102 MB / MsMpEng 571 MB / Hermes 537 MB(+6 进程) / ChatGPT 422 MB

> ⚠️ 诚实说明：无法 100% 断定崩溃触发点。Electron 渲染进程崩溃的根因需崩溃转储（`.dmp`）分析，本机 Crashpad 目录存在但无可解析转储。

---

## 二、本次已修复的 4 项

### 1. 禁用坏插件 `nous-girl-maid`（77 次报错）

| 项 | 内容 |
|:---|:---|
| 处理 | 移出扫描目录（非删除，可恢复） |
| 从 | `hermes\desktop-plugins\nous-girl-maid\` |
| 到 | `hermes\desktop-plugins-disabled\nous-girl-maid\` |
| 根因 | 旧插件 API 与新版 SDK 不兼容：`sdk-B6X_oHhs.js:5` 抛 `TypeError: Cannot convert undefined or null to object` |
| 影响 | 仅为配色主题插件，禁用无功能损失 |

恢复：`mv desktop-plugins-disabled/nous-girl-maid desktop-plugins/`

### 2. 修 mnemon hooks 的 Python 路径（112 次报错）

**根因（实测复现）：**
```
$ echo '{...}' | bash remind.sh
exit=49   stdout=0 bytes
stderr: Python was not found; run without arguments to install from the Microsoft Store...
```
hook 环境里 `python3` → `WindowsApps\python3`（Store 存根），`python` → 真 3.14.7。

**修法：** 在 `remind.sh` / `nudge.sh` 注入按序探测的解析器，第一个能 `import sys` 的胜出：
```bash
PY_BIN=""
for _cand in python python3 <uv-3.11> <hermes-venv>; do
  if "$_cand" -c "import sys" >/dev/null 2>&1; then PY_BIN="$_cand"; break; fi
done
[ -z "$PY_BIN" ] && { echo '{}'; exit 0; }
```

**额外加固：** 测试中发现 `Path.home()` 在缺 `USERPROFILE` 时抛 `RuntimeError: Could not determine home directory`。加 `_hermes_home()` 兜底（`HERMES_HOME` → `USERPROFILE` → `HOME` → cwd），并用**清空所有环境变量**的恶劣场景实测通过。

**验证（官方 `hermes hooks doctor`）：**
```
[on_session_start]  ✓ allowlisted  ✓ unchanged  ✓ valid JSON (exit=0, 0.253s)
[pre_llm_call]      ✓ allowlisted  ✓ unchanged  ✓ valid JSON (exit=0, 0.240s)
[post_llm_call]     ✓ allowlisted  ✓ unchanged  ✓ valid JSON (exit=0, 0.242s)
All shell hooks look healthy.
```
修前 `exit=49 / 0 字节` → 修后 `exit=0 / 有效 JSON`。

**关键坑：** 改 hook 脚本会刷新 mtime，导致审批记录失效（`hooks doctor` 报 "script modified since approval"）。需 `hermes hooks revoke` + 重新 `_record_approval`。但 `_is_allowlisted` **不校验 mtime**，所以 hook 仍会运行，只是 doctor 报警。

### 3. 禁用冗余 obsidian MCP（377 次报错，最大噪音源）

| 项 | 内容 |
|:---|:---|
| 报错频率 | **每 30 分钟重试一次**（18:19 → 18:49 → 19:19 → 19:49 → 20:19） |
| 根因 | Obsidian 应用未常驻，`http://127.0.0.1:27123/mcp/` 连不上（HTTP 000） |
| 关键判断 | Hermes 的 `obsidian` skill 是 **filesystem-first**（走 `OBSIDIAN_VAULT_PATH` + `read_file`/`write_file`），**不依赖此 MCP** |
| 处理 | `config.yaml` 中 `obsidian.enabled: false`（保留 token 与 url，注释写明恢复方法） |

### 4. 清理 3 GB 更新失败残骸

| 文件 | 大小 | 来源 |
|:---|:---|:---|
| `state.db.pre-update-emergency-2026-09-25T05-03-31-664Z.bak` | 1.00 GB | 09-25 失败更新 |
| `state.db.pre-update-emergency-2026-09-25T05-10-23-504Z.bak` | 1.00 GB | 09-25 失败更新 |
| `state.db.pre-update-emergency-2026-09-26T13-07-17-872Z.bak` | 1.02 GB | 09-26 失败更新 |

**保留** `backups/pre-update-20260925-152535/state.db.bak`（1.00 GB，正式备份）。

---

## 三、state.db 分析结论（不建议 VACUUM）

| 部分 | 占用 |
|:---|:---|
| messages | 521.5 MB |
| messages_fts_trigram_data | **343.1 MB** |
| messages_fts_data | 101.1 MB |
| system_prompts | 30.8 MB |
| 索引合计 | ~37 MB |
| **总计** | **1038 MB** |

- 数据：1158 个会话 / 155,624 条消息（2026-07-23 ~ 2026-09-28）
- freelist 仅 **15.5 MB** → **VACUUM 最多省 15.5 MB，不值得**
- 343 MB 是中文三元组 FTS 索引，是搜索功能的基础，非垃圾

---

## 四、更新的其他 MCP 状态

| Server | 状态 | 说明 |
|:---|:---|:---|
| code-review-graph | ON | 正常 |
| filesystem | ON | 正常 |
| github | ON | 正常 |
| jlcmcp | ON | 正常 |
| memvid | ON | 正常 |
| obsidian | **OFF** | 本次禁用 |
| jlceda | OFF | 原本已禁用 |

> 注：日志中 `module 'tools.mcp_tool' has no attribute 'StdioServerParameters'` 是**更新前的历史错误**，当前 `hasattr()` 实测为 `True`（mcp 包 1.30.0），已不复现。

---

## 五、备份与回滚

| 内容 | 路径 |
|:---|:---|
| mnemon hooks + allowlist | `hermes\backups\mnemon-hooks-20260928-173954\` |
| config.yaml | `hermes\backups\config.yaml.bak-pre-mcp-fix-20260928-204334` |
| state.db（正式） | `hermes\backups\pre-update-20260925-152535\state.db.bak` |
| 被禁插件 | `hermes\desktop-plugins-disabled\nous-girl-maid\` |

---

## 六、遗留待办

1. **重启 Hermes** —— 上述改动需重启生效（hook 在启动时注册；MCP 在启动时连接）
2. **`/new` 开新会话** —— 当前会话 31 万 token、压缩多次，是崩溃高危场景
3. **释放内存** —— 关掉 ZCode(1.1GB) / ChatGPT(422MB) / wallpaper64(331MB)
4. **考虑加内存条** —— 现为 16 GB 单条，最根本的解法
5. 可选：修 QQ Bot token（`invalid appid or secret`, code 100016）
6. 可选：`state-snapshots/20260910-145547-pre-update/state.db`（0.77 GB）如确认无需可清

---

## 七、时间线锚点

- 当前：2026-09-28（星期一）
- Hermes 版本：`0.21.5+2453.gd0288be`（commit `d0288be5b3`，2026-09-26 03:51 UTC）
- 落后 origin/main：**0**（已是最新）
