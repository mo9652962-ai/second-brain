---
tags:
  - research
  - security
  - reverse-engineering
  - ai-agent
  - mcp
type: research
created: 2026-09-03
status: adopted
---

# AI 逆向 × Skill/MCP：阿里 v2 滑块实战研究

> 来源：抖音「青木教Python」《AI逆向没有skill和mcp加持！连阿里v2滑块门都摸不到》+ 8 路搜索引擎交叉研究
> 日期：2026-09-03 · 状态：已沉淀进 `ai-assisted-reversing` 技能 v1.1

## 一句话结论

**AI 逆向 Web 验证码（阿里 v2 滑块）的完整工作流 = Skill 给 AI 脑子 + MCP 给 AI 手 + AI 多轮采样拟合 + 自检纠偏 + 纯协议复现。没有 skill 和 MCP，AI 连门都摸不到。**

## 视频信息

| 项 | 值 |
|:---|:---|
| 标题 | AI逆向没有skill和mcp加持！连阿里v2滑块门都摸不到 |
| 作者 | 青木教Python (uid 3085675177711924) |
| 视频 ID | 7665677440862394339 |
| 时长 | 12分38秒 |
| 热度 | 1274 赞 / 64 评论 / 167 转发 |
| 主题标签 | #python #python爬虫 #js逆向 #skill #程序员 |

## 核心理念（方法论增量）

```
Skill 给 AI 脑子（分析逻辑 / 已复现案例 / 流程规范）
MCP  给 AI 手（js-reverse-mcp 调试工具 / 浏览器控制 / 抓包）
AI   干活（多轮采样 → 拟合 → 自检 → 落地代码）
人   决策（目标 / 边界 / 验证 / 合规）
```

- **没有 skill**：AI 不知道「该断在哪、该采什么、该拟合什么」
- **没有 MCP**：AI 只有嘴没有手（不能控制浏览器、不能调试）
- **skill 自检纠偏是核心增量**：skill 里存「已复现成功案例」→ AI 每次跑完对照自检 → 偏离就自动纠正方向。这是 skill 区别于普通文档的价值——它让 AI 不跑偏

## 阿里 v2 滑块技术背景（4 接口流程）

| # | 接口 | 作用 | 关键参数 |
|:---|:---|:---|:---|
| 1 | `InitCaptchaV2` | 初始化验证码 | SignatureNonce(uuid)、Signature(HMAC-SHA1)、DeviceData |
| 2 | `Log2` | 提交设备环境 | Data = 大环境数组多次 btoa/join/AES |
| 3 | `Log3` | 提交轨迹 | Data = 轨迹 AES 加密（记录整个屏幕轨迹）|
| 4 | `VerifyCaptchaV2` | 最终验证 | CaptchaVerifyParam（deviceToken + data）|

- `VerifyCode=T001` = 通过；`CertifyId` 带入后续请求
- **动态 key**：每次加载的 `feilin.js` / `sg.js` 都不同（sg 1.1.0→1.1.10+，key 达 320 个）
- 轨迹加密链：轨迹 → TextEncoder → deflate 压缩 → AES → base64；vmp 运算（CertifyId + sg key）
- 环境风控点：`dfghfgdh6`、`bgnb89435` 等，环境不对则验证失败

## AI 工作流（视频实测 5 步）

```
① 配置 skill + MCP（ai-reverse-toolkit + js-reverse-mcp）
② 多轮采样：AI 用 Playwright 打开滑块页，自动采样 JS（8 轮不够 → 40 轮）
③ 拟合 + 字节替换动态 key
④ skill 自检纠偏：对照 skill 已复现案例逻辑，偏离 → 纠正方向
⑤ 落地纯协议脚本 → 本地运行 → 稳定 T001 → 完成
```

关键技巧：
- 采样次数要够（动态 key 版本多，8 轮不够就 40 轮）
- AI 默认首选 Playwright 采样（除非强制指定）
- 采样轮数多时让 AI 写自动化脚本批量拉
- 上游非关键报错可忽略，别打断流程
- 先采样再拟合再自检，顺序不能乱

## AI 逆向工具链（skill + MCP 生态）

| 工具 | 用途 |
|:---|:---|
| [ai-reverse-toolkit](https://github.com/zhizhuodemao/ai-reverse-toolkit) | 7 个 skill：find-crypto-entry / env-patch / ast-deobfuscate / android-app-reverse / fingerprint-bypass / wasm-reverse / protocol-analysis |
| [js-reverse-mcp](https://github.com/zhizhuodemao/js-reverse-mcp) | JS 逆向 MCP：反检测浏览器 + 23 调试工具 |
| frida-mcp / adb-mcp / android_proxy_mcp | 动态 hook / 设备 / 抓包 |
| fingerprint-collector | 4 层指纹采集 + 一致性分析 |
| [reverse-skills](https://github.com/dongruijun8-coder/reverse-skills) | 5 skill + 41 MCP 工具，7 Phase 全自动 APK 逆向，三路径输出（全协议/Auth-only/Full RPC）|
| haikow/claude-reverse-skills | apk/ida/radare2/js 逆向 skill 集 + IDA MCP |

## 视频结尾观点（AI 逆向的真相）

> 以前没有 AI 时，别人能做阿卡迈/五秒盾；现在有 AI 了，别人也能做。为什么你的 AI 不行？
> AI 的确有分析能力，但基础立项/编程基础还是要自己具备——AI 是捷径、弯道超车，
> 不是「完全基于 AI 做任何想做的事情」的万能钥匙。

## 沉淀动作

- ✅ `ai-assisted-reversing` 技能 v1.1：新增「AI+Skill+MCP 逆向 Web 验证码（阿里 v2 滑块实战）」章节（4 接口流程 + 5 步工作流 + 关键技巧 + 核心理念）
- ✅ 本知识库文件存档
- 相关技能：`ai-assisted-reversing`、`cyber-security-learning`、`src-bug-hunting`、`miniapp-reversing`

## 合规说明

- 学习目的是「知道验证码怎么被破 → 知道怎么防」（防御者思维）与爬虫自动化研究
- 不针对具体线上业务目标实施绕过；不提供用于攻击第三方系统的工具
- 阿里 v2 滑块分析仅作技术原理研究参考

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
