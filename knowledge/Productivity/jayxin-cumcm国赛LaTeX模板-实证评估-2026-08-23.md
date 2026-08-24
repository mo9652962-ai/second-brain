# jayxin/cumcm 国赛 LaTeX 模板实证评估（2026-08-23）

> 来源：抖音「云顶数模」图文作品（2026-08-23 发布，粉丝 7982）推荐 → GitHub jayxin/cumcm
> 实证：仓库真实存在，star 9 / fork 1 / 最近更新 2026-08-14（一周前活跃）

## 仓库信息

| 项 | 值 |
|:---|:---|
| 仓库 | https://github.com/jayxin/cumcm |
| 作者 | jayxin（30 followers，活跃维护 LaTeX 模板系：cumcm/npgmcm/nsmc） |
| 许可证 | LPPL-1.3c |
| 最近更新 | 2026-08-14（模板 2026 国赛已适配） |
| 基于 | latexstudio/CUMCMThesis 二次修改 + 结构重排 |

## 质量评估（已抓取 main.tex + cumcmthesis.cls 实证）

**优点：**
- ✅ 结构清晰：`commons/`（模板）+ `contents/`（内容分章节）+ `docs/`（格式规范 PDF）+ `fonts/`（内嵌字体）
- ✅ 自带 **2026 高教社杯通知 + 2026 修订版格式规范 PDF**（文档同步最新）
- ✅ 内嵌字体（times/arial TTF），跨平台编译不依赖系统字体
- ✅ 文档类选项完整：`withoutpreface`（电子版）/`bwprint`/`colorprint`/`draft`
- ✅ 智能引用：cleveref 中文格式化（图~/表~/式~），上标引用 upcite
- ✅ 数学环境齐全：定义/定理/引理/假设/公理/定律/例/证明/解
- ✅ 编译方式简单：xelatex ×2 或 latexmk main；TeXPage/Overleaf 在线可用
- ✅ 承诺书/编号页内容已更新到《竞赛章程》

**注意点：**
- ⚠️ 只有 9 star（小众但维护活跃，作者是 LaTeX 重度用户）
- ⚠️ 默认 `withoutpreface`（电子版），纸质版需改 documentclass
- ⚠️ 已测环境仅 Linux + TeXLive 2023，Windows 需自行验证

## 对比其他模板

| 模板 | 特点 | 结论 |
|:---|:---|:---|
| **jayxin/cumcm**（本模板） | 结构清晰+内嵌字体+2026 格式文档+cleveref 中文引用 | ✅ **推荐** |
| latexstudio/CUMCMThesis | 官方经典，适配到 2023 | 基础底子 |
| Sustainable-Enjoyment/CUMCM-LaTeX-Template | 2024 国一作者自用，现代化 | 备选 |
| zhanwen/MathModel | 论文库+模板大全（2025 版已更新） | 资料库备用 |

## 落地建议（对 paper-service 数模代写业务）

1. **下载整包**到 `D:\paper-service\latex-templates\cumcm-jayxin\` 作为代写交付模板库
2. 交付时用 `withoutpreface` 电子版模式 + 客户队号填充
3. 此模板适合「要求 LaTeX 交付」的高端客户（可加价项）
4. 与现有 Word 交付流水线（paper_package.py）并列，按客户要求选交付格式

## 下载说明

- GitHub zip：`https://codeload.github.com/jayxin/cumcm/zip/refs/heads/main`（本机代理对 codeload 不通，需开代理后下载或用 TeXPage 在线导入）
- 在线编译：TeXPage 选编译器 xelatex + TeXLive 2023 + 主文档 main.tex
