---
title: "SOP-005: 小程序反编译密钥审计流程"
type: sop
domain: SOP
status: active
tags: [knowledge/sop]
source: null
---
# SOP-005: 小程序反编译密钥审计流程

- **ID**: SOP-005
- **Category**: SEC（安全）
- **状态**: Active
- **维护者**: k

## 1. 前置条件与触发上下文

- **触发**: SRC 目标有小程序（如联想商城）/ 前端密钥审计
- **前置**: 微信 4.0+ 已打开目标小程序（缓存 wxapkg）/ unveilr / KillWxapkg
- **合规**: 只读静态分析，密钥不实际使用

## 2. 确定性执行步骤

```
① 获取小程序包（微信 4.0+ 新版路径）:
   C:\Users\31954\AppData\Roaming\Tencent\xwechat\radium\users\<hash>\applet\packages\
   → 按修改时间找最新（=刚打开的小程序）
   → wxapkg 在 <appid>/<version>/__APP__.wxapkg
② 反编译:
   cd C:\Users\31954\tools\unveilr
   ./unveilr.exe wx -i <appid> -f -o <输出目录> <wxapkg路径>
   ⚠️ 必须 -i 指定 appid（目录名），否则报 wxAppId must be required
③ 密钥扫描:
   grep -rhoE "secretKey|accessKey|appSecret|LTAI|sk_live|BEGIN PRIVATE|..." --include="*.js"
④ 密钥用途分析:
   - 定位文件/上下文（config.js 等）
   - 确认是生产/测试环境（config.js 常有 host 区分）
   - 确认用途（签名/加密/上报 SDK）→ 判断危害
⑤ API 接口提取（审计副产品）:
   grep -rhoE "url:\s*[\"'][^\"']+" api/*.js
   → 完整接口列表（未授权测试点到为止）
```

## 3. 验证与验收边界

```
✅ 确认小程序身份（appid/名称）
✅ 密钥位置 + 用途 + 环境（生产/测试）明确
✅ 危害评估（能干什么/不能干什么）诚实标注
❌ 未达标准: 只报密钥值不分析用途（可能误报/低价值）
```

## 4. 异常恢复与常见陷阱

```
⚠️ 微信 4.0+ 无 wxapkg 在旧路径（Documents/WeChat Files）→ 在 xwechat/radium/.../applet/packages/
⚠️ unveilr 报 wxAppId must be required → -i 加 appid
⚠️ RSA 私钥在 jsencrypt/fp-wx.min.js = 第三方库 demo（误报，非业务密钥）
⚠️ secretKey 用于神策埋点 = 低-中危（能伪造上报数据，非业务 API 密钥）
⚠️ 业务 API 认证靠登录 token（api-token header）= 未登录访问被拒（400001）
⚠️ 子包（subpackages/）也要查（独立 API）
⚠️ 审计结果注意保密（VULBOX 协议永久保密）
```

## 5. 演进记录

| 日期 | 变更 | 原因 |
|:---|:---|:---|
| 2026-08-19 | 新建 | 联想商城小程序反编译审计流程（unveilr 链）|

---
> 🗺️ 属于 [[SOP-INDEX]] · [[knowledge-map]] · [[Home|🏠 Home]]
