---
tags: [weekly-review, learning-progress, W31]
date: 2026-08-02
type: weekly-learning-review
---

# 📚 周学习回顾 — W31 (2026-07-27 ~ 08-02)

> 本周是「研究吸收 + 变现成型」周：36 篇研究笔记入库（新 Research 域）、闲鱼接单体系从文案到 SOP 全链路就绪、本地生图跑通、Agent 自改进方法论形式化。
> 与结构整理报告互补：文件层见 [[weekly-2026-08-02|W31 周度整理报告]]，本文聚焦内容层学习与掌握度。

---

## 📊 总体统计

| 指标 | 数值 |
|:----|:----:|
| 活跃会话数 | ~10（含 8 类 cron 会话 + Krea2 深度调试 + 用户交互；7/29 起连续安静期第 4 天） |
| 新增 LEARNINGS | **8 条**（7/27×2 · 7/28×2 · 7/29×3 · 8/1×1） |
| 新增知识点 | **~45 个**（跨 9 个知识域） |
| 新建/更新 Skill | 触碰 **179 次**（7/27 批量导入/刷新社区 Skill ~102；随后自建/更新 ~77） |
| 新增/修改笔记 | knowledge 166 · memory 63（含索引/维护文件） |
| 新建 MOC | 1 个（🔬 Research，索引 36 篇研究笔记） |
| 故障修复 | 5 项（auto-sync 推送分支、Tavily 配额、opencode-go SSL、Vault 断链/幽灵标签、dreaming 空壳堆积） |
| Git 推送 | 158 次 commit（auto-sync 为主，含 Krea2 定版、安全审计等实质提交） |

---

## 📖 按知识域汇总

### ① 🤖 AI Agent 架构 — 🟢 从理论吸收 → 工程落地

| 新知识点 | 来源 | 掌握程度 |
|:---------|:----|:--------:|
| **OpenMLE 四算子方法论**（Draft/Improve/Debug/Crossover；Frontis-MA1 35B：MLE-Bench 39.4%→71.2%）→ 映射为 learn→research→apply 形式化 v2 | arXiv W32 交叉验证 | 🟢 已应用 |
| **OpenForgeRL**（proxy+K8s 把任意 agent harness 变成 RL 训练环境；harness 即训练对象）→ `export_traces.py` 实测 7 天 206 会话/77k 消息/81.7MB，达论文数据门槛 | arXiv 2607.21557 + 亲身实践 | 🟢 🛠️ 可执行 |
| **StateAct**（程序状态优先于像素，GUI 只做兜底，成本低 9x）→ workflow 规则 #16「状态层优先」 | arXiv 2607.22798 | 🟢 已应用 |
| **OSReward**（VLM judge 系统性宽松偏差，失败被标成成功）→ 规则 #17「评估器可靠性自检」 | arXiv 2607.28609 | 🟢 已应用 |
| **AgentRadio 五阶段编排**（四 agent 62.1% > 单 agent 32.3%，架构>模型） | arXiv W32 | 🟡 理解 |
| **qm 多人 Agent 框架**：scope 隔离 / skill 一等公民 / 安全三档可直接迁移（Kimi-K3 开源 4 天 7.5k⭐，前沿模型开源=流量密码） | GitHub Trending 双口径 | 🟡 理解 |
| **生产级 Agent 7 步法**（eval-first、工具 ≤8 个、max_steps=10、幻觉工具处理） | LRN-20260727-001 | 🟡 理解 |

### ② ⚙️ Hermes 配置与安全运维 — 🟢 可执行 + 安全加固

| 新知识点 | 来源 | 掌握程度 |
|:---------|:----|:--------:|
| **安全风险评估 P0/P1 全部落地**：Skill 来源审计（121 目录=28 市场导入+93 官方/自写）、.env icacls 收紧、api.json 移除 git 跟踪 | 亲身实践 | 🟢 🛠️ 已执行 |
| **auto-sync 推送分支 bug**：`obsidian-sync.py` 硬编码 `origin main`，实际工作分支 dev → 本地积压 ahead 14；改动态分支检测后完全同步 | 亲身实践 | 🟢 🛠️ 已修复 |
| **5 路搜索冗余实战验证**：Tavily 配额耗尽（432）→ Firecrawl/SearXNG/DDGS/Exa 兜底，配额恢复后保持语义缓存+并发≤3 | LRN-20260801-001 | 🟢 已解决 |
| **Cron 错误模式库**（CRON-001/002/003：超时→切方舟、配置漂移→pin 模型、MSYS 路径→原生路径），经验式修复跳过全推理 | LRN-20260729-001 | 🟢 🛠️ 可执行 |
| **浏览器异步验证三步法**（等待→确认→重试，Desktop-Delta Bench 参考） | LRN-20260729-002 | 🟢 已实践 |
| **Memory 归档与容量监控**（>100 文件警告 / 60 天归档 / 快照保留最新 3 份） | LRN-20260729-003 | 🟢 已实践 |
| **配置文档准确性审计**：对照真实 config.yaml 发现 8 处文档错误（LLM-Providers 过时、fangzhou alias 错、router 引用未部署模型）→ 6 文件待更新 | 亲身实践 | 🟡 进行中 |
| Vault 维护 cron 频率控制（增量检查优于全量扫描） | LRN-20260728-002 | 🟢 已实践 |
| Subagent 结果收割与正确性验证（子任务 claim 需 read_file/terminal 复核） | LRN-20260728-001 | 🟡 理解 |

### ③ 💰 变现 / 闲鱼 — 🟡 研究准备 → 🟢 可执行（本周最大跃迁）

| 新知识点 | 来源 | 掌握程度 |
|:---------|:----|:--------:|
| **闲鱼安全文案 v2「暗号化」**：放弃服务商定位→帮忙/交流定位；8 组暗语对照表（代做→帮忙看看…）；价格全移私聊；100% 避开风控关键词 | 亲身实践 | 🟢 🛠️ 可执行 |
| **接单工作流 SOP + 论文 Pipeline 数据契约**（报价档位/状态机/质量门禁，全链路交付流水线） | 亲身实践 | 🟢 🛠️ 可执行 |
| **降AI工具对比速查表**（笔灵 3 / 零感 1 / 森克兰特 1 元千字 + Hallmark 57 道检测门） | web_search + 实测 | 🟢 可执行 |
| **闲鱼上架素材包预生成**（PPT 3 套标题+详情+红线；复制即上架，~30min） | 亲身实践 | 🟢 🛠️ 素材就绪 |
| **校园便利盒报价基准**（完整平台 3000-8000 / 单项 400-2000）；「合规可变现 vs 灰色只吸收」判断标准 | 项目研究 | 🟢 已应用 |
| **3 个 AI 项目变现评估**：MoneyPrinterTurbo（AI 视频代做）、xiaozhi-esp32（100 元内语音助手成品）、OpenDuckMini（长期） | GitHub 研究 | 🟡 理解 |
| **数学练习册标准化**（哈希去重 1400+ 题、WPS 格式优化、GUI 点击即用）→ 第一个完全 ready 的标准化服务 | 亲身实践 | 🟢 🛠️ 可交付 |

### ④ 🎨 本地生图 / 创意工具 — 🆕 新域 🟢 已跑通

| 新知识点 | 来源 | 掌握程度 |
|:---------|:----|:--------:|
| **Krea2 本地部署定版**（RTX 4060 8GB：`--lowvram`、CFG 必须 1.0、1024 直接采样黑图→512+4x-UltraSharp 超分 2048 最优、VAE 用 Krea2VAEDecodeOfficial）→ `krea2-gen.py --hires` 脚本化 | 亲身调试（十轮研究） | 🟢 🛠️ 可执行 |
| ComfyUI 本地部署/排障（venv、自定义节点、VAE 替换） | 亲身实践 | 🟢 🛠️ 已实践 |
| 图像生成工作流整合（提示词工程+模型选型+批量生成） | skill 更新 | 🟢 可执行 |

### ⑤ 💻 微信小程序 / Dev — 🆕 CloudBase 可执行

| 新知识点 | 来源 | 掌握程度 |
|:---------|:----|:--------:|
| **CloudBase 8 站学习路径**（登录/内容审核/DB 操作/通知/类目/管理后台/统计/活动）→ 校园便利盒复刻能力 | 项目拆解 | 🟢 🛠️ 可执行 |
| **System Prompts 逆向参考库**（Claude Code Opus 5 / GPT-5.6 Codex / DeepSeek / Hermes 自己） | 收集研究 | 🟢 已实践 |
| MCP 规范候选版 / TRELLIS 3D / Awesome-Go / GeoLibre / secret-knowledge 参考 | 热榜研究 | 🔵 关注 |
| Browser-Use + Hermes 集成深度研究、浏览器自动化最佳实践 | 深度研究 | 🟡 理解 |

### ⑥ 📚 学术研究体系 — 🆕 Research 域成型

| 新知识点 | 来源 | 掌握程度 |
|:---------|:----|:--------:|
| **arXiv 周报 4/4 交叉验证全属实**（Frontis-MA1 / OpenForgeRL / AgentRadio / OSReward），单卡 12GB 思路可借鉴 | arXiv W32 | 🟢 已实践 |
| 10-Top AI Agent 项目深度研究（Deep Research 方法论） | web_search | 🟡 理解 |
| 文献检索坑（ai-literature-search-pitfalls）、负结果登记（negative-results-registry）、方法论手册 | 文章研究 | 🟡 理解 |
| **Skill 库审计**（6 组重复待合并、121 目录来源分类）→ skill-library-audit skill | 亲身实践 | 🟢 已实践 |

### ⑦ ⚖️ EU AI Act 合规 — 🆕 新域

| 新知识点 | 来源 | 掌握程度 |
|:---------|:----|:--------:|
| **高风险义务 8/2 正式执法**：对外多 Agent 产品需预置「日志 + 人工升级 + 透明度」三件套；闲鱼接单不受影响；是 AI 博主现成内容选题 | 法规研究 + 知识卡片 | 🟢 已应用（评估+卡片） |
| 合规义务分级（风险分类法） | web_search | 🟡 理解 |

### ⑧ 🎮 用户需求驱动研究（边缘域）— 🟢 已交付

| 新知识点 | 来源 | 掌握程度 |
|:---------|:----|:--------:|
| Skyrim Together Reborn 双人联机 mod 清单（D:/Skyrim_Mods 未装） | 用户需求研究 | 🟢 已交付 |
| Windows 游戏启动崩溃排查指南（帮他人远程） | 亲身实践 | 🟢 已实践 |

---

## 📈 掌握度总表

| 知识域 | W30 (7/19-26) | W31 (7/27-8/2) | 变化 |
|:-------|:---:|:---:|:----:|
| AI Agent 架构 | 🟢 深度吸收 | 🟢 **工程落地**（四算子映射/轨迹导出/规则固化） | 🔺 吸收→落地 |
| Hermes 配置 | 🟢 可执行 | 🟢 **可执行+安全加固**（审计/修复/冗余验证） | 🟢 维持 |
| PPT 设计 | 🟢 Skill 就绪 | 🟢 **上架就绪**（素材包 3 套文案） | 🟢 维持 |
| 学术写作 | 🟢 Skill 就绪 | 🟢 **接单可执行**（SOP+数据契约+降AI速查） | 🔺 升级 |
| Memory 架构 | 🟡 理解 | 🟡 理解（归档规则已实践） | 🟢 部分实践 |
| DevOps/Infra | 🟢 可执行 | 🟢 可执行（频率控制/增量检查） | 🟢 维持 |
| 变现/闲鱼 | 🟡 研究准备 | 🟢 **🛠️ 可执行**（暗号文案/素材包/报价/SOP） | 🔺 大幅提升 |
| 本地生图 Krea2/ComfyUI | — | 🟢 **🛠️ 可执行**（4060 跑通+脚本化） | 🆕 新域 |
| 微信小程序 CloudBase | — | 🟢 **🛠️ 可执行**（8 站路径+接单脚手架） | 🆕 新域 |
| EU AI Act 合规 | — | 🟡 理解（8/2 生效评估+卡片） | 🆕 新域 |
| Research 研究域 | — | 🟢 已实践（36 篇+MOC） | 🆕 新域 |

---

## 🏆 本周最有价值的发现 Top 5

| ⭐ | 发现 | 为何重要 |
|:-:|:----|:---------|
| 1 | **闲鱼变现体系全链路就绪**（暗号化文案+素材包+SOP+数据契约+降AI速查+报价基准） | 从「研究准备」到「复制即上架」，P0 上架是唯一剩余阻塞 |
| 2 | **OpenMLE 四算子方法论**：AI 自改进 = Draft/Improve/Debug/Crossover 循环（39.4%→71.2%） | 把 learn→research→apply 自举系统形式化，Second Brain 有了理论根基 |
| 3 | **OpenForgeRL 验证：Hermes 原生轨迹层（state.db）即可做自训数据** | 无需额外 proxy，`export_traces.py` 实测 81.7MB/7 天，已达论文数据门槛 |
| 4 | **EU AI Act 高风险义务 8/2 生效** | 跨域知识（法规→合规→内容选题），卡片机制成功锁定时效知识 |
| 5 | **Krea2 本地生图十轮定版**（CFG=1.0 / 512+超分 / 官方 VAE 绕坑） | 素材成本归零，可支撑 PPT/设计接单主图制作 |

---

## 📌 下周优先项 (W32 8/3-8/9)

**🔴 必须做：**
- [x] ~~闲鱼上架~~ ✅ 已迁移至 projects/current.md 统一追踪
- [x] Hermes 配置文档修复：LLM-Providers.md 重写 + fangzhou-ark-setup alias 修正 ✅ 2026-08-06：LLM-Providers.md 已重写对齐 config.yaml 实况（默认模型 custom:fangzhou-2/deepseek-v4-pro + model_aliases 表 + 6 个 custom_providers）；fangzhou-ark-setup skill 已含 08-02 alias 修正注记
- [x] ~~主图制作~~ ✅ 主图1-3 已生成（outputs/xianyu-master/上架素材包/主图1-3.png）

**🟡 建议做：**
- [x] ~~小红书「AI PPT 教程」~~ ✅ 已迁移至 projects/current.md 统一追踪
- [x] ~~零感 AI 实测~~ ✅ 已迁移至 projects/current.md 统一追踪
- [x] ~~xiaozhi-esp32 采购清单~~ ✅ 已迁移至 MEMORY.md 统一追踪
- [x] ~~Skill 重复合并~~ ✅ 已迁移至 MEMORY.md 统一追踪

**🔵 可考虑：**
- [x] ~~随身 WiFi 下单~~ ✅ 已迁移至 MEMORY.md 统一追踪
- [x] 安全审计 cron 排期（每周 skill 新增 + 端口扫描）✅ 2026-08-06：已存在 security-audit cron（74dbe08a5d77，周日 8:30，no_agent 跑 security_audit.py）
- [x] ~~Agent 互操作标准~~ ✅ 长期追踪项，暂无具体行动

---

## 🔗 跨域关联

```
  OpenMLE 四算子 ──形式化──→ Second Brain 自举系统 (learn→research→apply v2)
        ↑
  arXiv W32 (Frontis/OpenForgeRL/AgentRadio/OSReward) ──→ Hermes workflow 规则 #16/#17
        │
  OpenForgeRL 轨迹导出 ──→ 自训数据管线 ──→ AI 博主内容选题
        │
  Krea2 本地生图 ──→ PPT 主图/设计接单 ──→ 闲鱼素材包
        │
  EU AI Act ──→ 多 Agent 产品合规 ──→ 博主内容选题（跨 3 域）
        │
  CloudBase 8 站 ──→ 校园便利盒接单 ──→ 闲鱼小程序开发报价（3000-8000）
```

> 本周主线：**研究吸收（36 篇）→ 工程落地（轨迹导出/规则固化/本地生图）→ 变现闭环（文案→素材→SOP→定价）**，learn→research→apply 全流程跑通 6 次以上。

---

_生成: weekly-learning-review cron · k (Hermes) · 2026-08-02 20:15_
