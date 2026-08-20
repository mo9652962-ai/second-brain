# SOP-004: SRC 资产侦察标准流程

- **ID**: SOP-004
- **Category**: SEC（安全）
- **状态**: Active
- **维护者**: k

## 1. 前置条件与触发上下文

- **触发**: 开始挖新 SRC 项目（拿到授权域名列表后）
- **前置**: OneForAll（C:\Users\31954\OneForAll）/ FlClash 代理 / 目标 P0 域名
- **合规前提**: 只测授权域名（SRC 声明范围），验证点到为止

## 2. 确定性执行步骤

```
① 子域名枚举（OneForAll 后台跑）:
   python oneforall.py --target <domain> run
   ⚠️ 大域名跑一半可能被杀 → 结果在 result.sqlite3（表格 <domain 下划线化>）
   提取: SELECT DISTINCT subdomain FROM <table> WHERE subdomain IS NOT NULL
② 高价值过滤 + 存活检测:
   - 过滤关键词: test/dev/qa/pre/sandbox/api/admin/idp/ai/git/artifactory
   - httpx/python 并发存活检测（只读 GET 根路径，15 并发）
   - 结果按状态码分组（200/403/404）
③ 指纹识别（批量）:
   curl -sI + grep title/server/x-powered-by
   Server: earth = 联想自研网关；React/Vue/Umi SPA = 前端壳
④ 高价值目标深挖（逐个）:
   - 测试/预发环境优先（防护弱）
   - 常见路径: /api /swagger /actuator /admin /login /robots.txt
   - SPA fallback 特征: 所有路径 200 返回 index.html = 前端壳（别误判）
   - /api/ 前缀返回真实 JSON = 后端网关（重点）
⑤ 判断是否值得继续:
   - 有未授权接口/信息泄露 → 深挖
   - 全部 401/403/登录墙 → 换目标（大厂防护完整时 ROI 低）
```

## 3. 验证与验收边界

```
✅ 产出资产清单（子域名 + 存活 + 指纹分类）
✅ 产出目标优先级（哪些值得深挖）
✅ 全程只读 GET（合规）
❌ 未达标准: 只枚举不分析 / 误把 SPA fallback 当漏洞
```

## 4. 异常恢复与常见陷阱

```
⚠️ OneForAll 被杀（大域名跑一半）→ SQLite 里已有部分结果，先提取再用
⚠️ 内网 IP 子域（10.x 开头）→ 公网不可达，跳过（合规也不测）
⚠️ SPA fallback: /actuator 返回 200 但内容是 index.html = 假阳性！
   → 必须看响应体（JSON vs HTML）区分
⚠️ 所有 /api/* 返回 500 = 后端挂了（不是接口存在）
⚠️ CORS 全开（Access-Control-Allow-Origin: *）无凭据模式 = 非漏洞
⚠️ WAF 拦截（Azure Gateway 403 / wswaf）→ 有防护，攻击面受限
⚠️ 硬编码密钥扫描:
   - 第三方库 demo 密钥（jsencrypt 自带 RSA 测试私钥）= 误报
   - 神策/埋点 SDK 的 secretKey = 低-中危（可伪造埋点数据）
   - 生产环境密钥硬编码 = 明确信息泄露（可提交）
```

## 5. 演进记录

| 日期 | 变更 | 原因 |
|:---|:---|:---|
| 2026-08-19 | 新建 | 联想 SRC 第一轮侦察全流程复盘（391 子域→48 存活→16 深挖）|

---
> 🗺️ 属于 [[knowledge-map]] · [[Home|🏠 Home]]
