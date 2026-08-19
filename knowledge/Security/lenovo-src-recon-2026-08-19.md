# 联想 SRC 侦察报告（2026-08-19）

> 日期: 2026-08-19
> 任务: 联想 SRC（LSRC）漏洞挖掘——第一轮侦察
> 目标: *.lenovo.com（P0 已声明域名）
> 状态: 侦察完成，未发现可提交漏洞，明天继续深挖

## 一、侦察成果

### 资产清单
```
📁 knowledge/Security/lenovo-src-assets-2026-08-19.md
→ 391 个联想子域名（OneForAll，Certificate+Dataset 模块）
→ 高价值分类: 测试/预发 71 + AI 20 + API 19 + 认证 11 + 代码仓库 6
```

### 存活检测（107 高价值目标）
```
存活 48 / 107
200: 20 个 | 403: 13 个 | 404: 13 个 | 204: 2 个
```

## 二、已探测目标（结果汇总）

| 目标 | 指纹 | 发现 | 结论 |
|:---|:---|:---|:---|
| api-qas-mds.lenovo.com | Yii2 + PHP 7.1.33 | 登录页/找回密码存在 | 无直接漏洞（无用户枚举）|
| baiyingmalladminsec.lenovo.com | Spring Boot + 权限网关 | 全部 500/401/403 | API 有鉴权，无未授权 |
| api.brain.lenovo.com | Spring Boot | actuator health/info 暴露 | 低危（无敏感泄露）|
| althea-dev/qa.lenovo.com | nginx catch-all | 全路径返回 UP | 无价值 |
| aifusion.lenovo.com | 静态空壳 | index.html 空 | 无价值 |
| api.qira.lenovo.com | Azure WAF | 403 拦截 | 有防护 |
| lps-t3-sit.lenovo.com | Umi.js (AntD Pro) | SPA + API 后端 | 需登录后测 |
| s360-tst.lenovo.com | React + Spring API | /api/* 500（参数缺失）| 需正确参数 |
| webvpntest.lenovo.com | Cisco AnyConnect | VPN 测试环境暴露 | 可测默认凭据（谨慎）|
| financeinvoiceclaim.lenovo.com | Finance Claim | 财务系统 | 未深挖 |
| ainowai.lenovo.com | 阿里云 | 超时（安全组）| 无法访问 |
| artifactory.tc*.lenovo.com | 内网 IP | 10.251.x.x | 公网不可达 |

## 三、关键判断

```
① 联想大厂防护到位: 主要系统都有 WAF/鉴权（Azure Gateway 403 / 权限网关）
② 前端全是 SPA（Umi/React/Vue）→ 后端 API 需要登录态（SSO: bpsso.lenovo.com）
③ 未发现「可直接提交」的漏洞
④ 补充探测（4 目标）: test.relmeetingapp 连接重置 / idp.sandbox 403
   / magiccubetest 403 / laidian 占位页(LenovoMallApplet 标识)
⑤ 结论: 公网 Web 面防护完整 → 转小程序/App 端方向
   （联想商城小程序 = LenovoMallApplet，注册标识 A002305）
```

## 四、明天行动计划

```
① 深挖 webvpntest.lenovo.com（Cisco VPN 测试环境）
   - 尝试默认凭据（admin/admin 等，点到为止）
   - 检查未授权访问漏洞（CVE-2020-3452 等 Cisco 已知漏洞）
② financeinvoiceclaim.lenovo.com（财务系统）业务逻辑
   - 注册/登录流程、越权测试
③ 联想商城/App 小程序（前端密钥扫描，复用 ai_secret_scan）
   - 联想商城小程序/App → 反编译 → 密钥扫描
④ 联想其他 P0 域名（motorola.com / lenovomm.com）子域补充
⑤ 待补: lenovo.com 完整 OneForAll（上次进程被杀，只跑了一半模块）
```

## 五、合规确认

```
✅ 全部探测只读 GET，无攻击性测试
✅ 只测 P0 声明域名（*.lenovo.com）
✅ 未触碰: webshell/DoS/爆破/提权/横向/拖库
✅ 测试记录将按协议保密（VULBOX 众测协议）
```

---
> 🗺️ 属于 [[MOC-Security]] · [[Home|🏠 Home]]
