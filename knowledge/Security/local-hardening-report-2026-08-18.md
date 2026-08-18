# 本机安全加固检查报告（2026-08-18）

> 执行：8 项立即执行清单的可自动化部分

## 检查结果总览

| # | 项目 | 状态 | 说明 |
|:---|:---|:---|:---|
| 1 | BitLocker 全盘加密 | ✅ 通过 | C: D: 均 FullyEncrypted + Protection On |
| 2 | 防火墙三档 | ✅ 通过 | Domain/Private/Public 全开 |
| 3 | SMBv1 | ✅ 通过 | EnableSMB1Protocol: False（WannaCry 已防）|
| 4 | 系统补丁 | ✅ 通过 | 最近补丁 2026-08-12 |
| 5 | 杀软 | ⚠️ 注意 | **McAfee 接管杀毒**（Defender 实时保护因此关闭，属正常机制）|
| 6 | 高危端口 | ⚠️ 注意 | 135(RPC)/445(SMB)/139(NetBIOS) 监听中——防火墙挡外部，局域网暴露 |
| 7 | npm 加固 | ✅ 已修复 | ignore-scripts=true / min-release-age=3 / allow-git=none / allow-remote=none |
| 8 | 密码/2FA | ⏳ 待办 | Bitwarden + 2FA 需人工操作 |

## 已执行的修复

### npm 供应链加固（~/.npmrc 追加）
```ini
ignore-scripts=true    # 禁 postinstall（防 axios 类攻击）
min-release-age=3      # 不装 3 天内新包（防恶意包）
allow-git=none         # 禁 git 来源
allow-remote=none      # 禁 direct URL
```
- 备份：~/.npmrc.bak
- 验证：配置全部生效
- ⚠️ 影响：electron 类包 postinstall 被禁；Hermes 桌面 electron 已安装无需重装，如未来需重装 electron 用 `npm install electron --ignore-scripts=false` 覆盖

## ⚠️ 遗留风险（建议处理）

### 1. McAfee 状态确认
Defender 实时保护关闭是因为 McAfee 接管。需确认：
- McAfee 是否在正常运行/更新
- 若 McAfee 是预装试用版且过期 → 卸载它，让 Defender 重新接管

### 2. 高危端口 135/445/139
- 防火墙已挡外部，但局域网（如公共 WiFi）暴露
- Windows 核心服务不建议直接禁用
- 缓解：确保防火墙 Private 配置正确；陌生网络用 VPN/防火墙公共档

### 3. 密码/2FA（人工操作）
- 装 Bitwarden（或已有密码管理器）生成唯一密码
- 邮箱/银行/云账号开 2FA（优先 passkey/硬件密钥）

### 4. 备份（人工操作）
- 重要数据 3-2-1：外接硬盘（备份后拔掉）+ 云端版本保留

## 下一步建议
1. 确认 McAfee 状态（关键！杀软不能没有）
2. 有空执行：Bitwarden + 2FA + 备份
3. 防御技能已沉淀：src-bug-hunting「防御能力速查」章节
