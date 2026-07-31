---
tags: [research, github, trending, ecc, agent]
created: 2026-07-31
status: absorbed
---

# GitHub 热榜日报 7.28 — 5 项目研究

> 来源：小黑盒热榜日报 · 2026-07-31 落地

## 项目总览（全部已验证）

| # | 项目 | Stars（实测） | 类型 | 决策 |
|:-:|------|:---:|------|------|
| 1 | pascalorg/editor | 17.8k | 3D 建筑方案编辑器（React Three Fiber + WebGPU） | 🟡 存档（无接单场景） |
| 2 | jenkinsci/jenkins | 25.8k | CI/CD 老牌自动化服务器 | ⚪ 与我们无关（Hermes 已覆盖） |
| 3 | andrewyng/aisuite | 15.7k | 统一多模型接口 + Agents API + MCP | 🟡 存档（我们已有 Hermes 多供应商层） |
| 4 | affaan-m/ECC | **236.5k** | Agent 性能优化系统（67 agents/281 skills） | 🔴 **已安装！** |
| 5 | huggingface/speech-to-speech | 9.0k | 本地语音 Agent 流水线（VAD→STT→LLM→TTS） | 🟡 存档（配合 xiaozhi 方向） |

## 🔴 重点：ECC 安装成功（上次网络失败，这次克隆成功）

### 发现
- **ECC 原生支持 Hermes**：`./install.sh --profile minimal --target hermes`，有专属 `docs/HERMES-SETUP.md`
- 项目体量：236.5k stars（今日 +458），67 agents / 281 skills / 94 commands / AgentShield 安全扫描
- 核心哲学：**plan → test → implement → review → verify → remember → improve**
- "Optimize the context window. Persist everything else."（优化上下文窗口，其他全部持久化）

### 安装过程
1. `git clone --depth 1` 成功（3378 文件，上次 zip 下载超时）
2. `npm install` 补依赖（ajv 等）
3. `node scripts/ecc.js install --profile minimal --target hermes` → 装到 `~/.hermes/`
4. 结果：**45 skills + 39 agents + 23 rules**（3.3MB）

### 关键认知：Hermes 真实 skills 目录是 `AppData\Local\hermes\skills\`，不是 `~/.hermes/`
- `~/.hermes/config.yaml` 是 Kimi 接入的历史配置（7-29 验证版），ECC 安装不动它 ✅
- ECC 装到 `~/.hermes/skills/` 后 Hermes 主程序不会自动加载
- **解决方案**：精选 4 个最高价值 skill 导入真实目录（加 ecc- 前缀防冲突）

### 已导入 Hermes 的 4 个技能
| 技能 | 作用 | 与现有体系互补点 |
|------|------|----------------|
| ecc-context-budget | 审计上下文窗口消耗，找出冗余组件 | 补强规则 #15（token 治理） |
| ecc-continuous-learning-v2 | 观察会话→原子直觉→演化为技能 | 补强规则 #12（情景→参数化） |
| ecc-iterative-retrieval | 渐进式检索（解决 subagent 上下文问题） | 补强规则 #21（干湿分离） |
| ecc-delivery-gate | 完成前质量门（阻止提前结束） | 补强规则 #17（评估器自检） |

### 已确认被 Hermes 识别
skills_list 中可见：context-budget、continuous-learning-v2、delivery-gate、iterative-retrieval ✅

## 🟡 存档项目

### pascalorg/editor（17.8k）
- React Three Fiber + WebGPU 的 3D 建筑编辑器，浏览器里做建筑方案
- 节点化场景（Site→Building→Level→Wall/Item）+ 脏节点增量更新 + 事件总线
- 对我们的价值：技术栈学习（Zustand + Zundo + three-bvh-csg），无直接接单场景
- 若要 3D 展示可用（轻量预览），暂不装

### andrewyng/aisuite（15.7k）
- 统一 Chat Completions API + Agents API（tools/toolkits/MCP）
- 内置 fallback + 一键换 provider 对比评测
- 对我们的价值：我们已有 Hermes 多供应商层 + fallback 链，**重复，不装**
- 但 OpenWorker（aisuite 驱动的桌面 AI coworker）值得关注

### huggingface/speech-to-speech（9.0k）
- VAD→STT→LLM→TTS 四组件流水线，OpenAI Realtime 兼容 WebSocket
- 组件全可换：Silero VAD / Parakeet STT / 任意 OpenAI 兼容 LLM / Qwen3-TTS
- 对我们的价值：配合 xiaozhi-esp32 硬件方向（待采购 ESP32-S3），暂不装

## 结论
- **1 项落地**：ECC 安装 + 4 技能导入（解决上次网络失败的遗留任务）
- 其余 4 项存档（2 项与现有体系重复，2 项暂无场景）
