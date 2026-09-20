---
name: "web-dev-2026"
description: "现代 Web 全栈开发 v1.0 (2026)：Next.js 15/React RSC、TypeScript、Tailwind CSS、Biome、GitHub Copilot、Vercel Edge、pnpm Turborepo 全流程。触发词：Web开发/全栈/前端/Next.js/React"
---

# Web 全栈开发 (Web Dev 2026)

> 2026年7月搜索引擎验证
> 技术栈: Next.js 15 + TypeScript + Tailwind + Biome + pnpm + Vercel

---

## Grill 对齐 —— 先问清楚再写代码

> **完成标准**: 项目类型、技术栈、部署方式已明确

在写任何 Web 代码之前，先问:
- □ 项目类型？(网站 / SaaS / API / 移动端适配 / 后台管理)
- □ 框架偏好？(Next.js 15 App Router / Nuxt / 纯前端)
- □ 样式方案？(Tailwind CSS / CSS Modules / 组件库)
- □ 部署方式？(Vercel / 自建服务器 / 静态导出)
- □ 已有设计稿？(Figma / 参考网站 / 无)
- □ 响应式要求？(移动优先 / 桌面为主 / 全适配)
- □ 特殊需求？(国际化 / SEO / 支付 / 权限 / 实时数据)

---

## 🎯 2026 技术栈总览

| 层级 | 推荐技术 | 说明 |
|:----|:--------|:----|
| **框架** | Next.js 15 (App Router) | RSC 默认，Server First |
| **语言** | TypeScript | 非可选，必选 |
| **样式** | Tailwind CSS v3+ | Utility-First 已成标准 |
| **格式化/检查** | **Biome** | Rust 编写，替代 ESLint + Prettier，快 10x |
| **包管理** | pnpm | 省磁盘、快、严格 |
| **Monorepo** | Turborepo | 多应用/包管理 |
| **AI 辅助** | GitHub Copilot | 2026 不可省略的生产力工具 |
| **测试** | Playwright (E2E) + Vitest (单元) | |
| **部署** | Vercel | Zero-config Edge 部署 |
| **组件原型** | v0 (Vercel) | 文本→组件代码生成 |

---

## 📋 开发工作流

```
需求 → Grill 对齐 → 项目初始化 → 组件开发 → 集成 → 测试 → 部署
      ↓
  选择技术栈
      ↓
  pnpm create next-app
      ↓
  配置 Biome + Tailwind + TypeScript
      ↓
  Git 初始化 → 开发
```

---

## 🔧 项目初始化

```bash
# Next.js 15 App Router
pnpm create next-app@latest my-app --typescript --tailwind --app

# 添加 Biome（替代 ESLint + Prettier）
pnpm add -D @biomejs/biome
pnpm biome init

# 配置 biome.json
{
  "$schema": "https://biomejs.dev/schemas/1.9.4/schema.json",
  "organizeImports": { "enabled": true },
  "linter": { "enabled": true, "rules": { "recommended": true } },
  "formatter": { "enabled": true, "indentStyle": "space" }
}
```

### VS Code 必备扩展 2026
- **Biome Extension** — 原生快速格式化
- **GitHub Copilot Chat** — 非建议，是必需
- **Tailwind CSS IntelliSense** — utility class 提示
- **Next.js Snippets** — 组件生成加速

---

## 🏗️ 组件开发模式

### React Server Components (RSC) — 默认模式

```typescript
// app/page.tsx — 默认是 Server Component，无需 "use client"
import { db } from "@/lib/db"

// 这个组件在 Server/Edge 运行，不发送 JS 到客户端
export default async function HomePage() {
  const posts = await db.post.findMany({
    take: 10,
    orderBy: { createdAt: "desc" }
  })

  return (
    <div className="grid gap-4">
      {posts.map(post => (
        <PostCard key={post.id} post={post} />
      ))}
    </div>
  )
}
```

### Client Component — 只在需要交互时使用

```typescript
"use client"  // 只在需要交互时标记

import { useState } from "react"
import { Button } from "@/components/ui/button"

export function LikeButton({ postId }: { postId: string }) {
  const [liked, setLiked] = useState(false)

  return (
    <Button
      variant={liked ? "default" : "outline"}
      onClick={() => setLiked(!liked)}
      className="transition-all duration-200"
    >
      {liked ? "❤️ 已赞" : "🤍 点赞"}
    </Button>
  )
}
```

### Tailwind CSS — 2026 标准样式方案

```tsx
export function Card({ title, description }: { title: string; description: string }) {
  return (
    <div className="rounded-xl border border-gray-200 bg-white p-6 shadow-sm
                    hover:shadow-md transition-shadow duration-200">
      <h3 className="text-lg font-semibold text-gray-900">{title}</h3>
      <p className="mt-2 text-sm text-gray-600 leading-relaxed">{description}</p>
    </div>
  )
}
```

---

## 🧪 测试

```bash
# 单元测试
pnpm add -D vitest @testing-library/react
pnpm vitest

# E2E 测试
pnpm add -D @playwright/test
pnpm playwright install
pnpm playwright test
```

---

## ☁️ Vercel Edge 部署

```bash
# 一键部署
pnpm add -D vercel
vercel --prod

# Edge Functions (全球边缘运行)
// app/api/hello/route.ts
export const runtime = "edge"

export async function GET() {
  return Response.json({ message: "Hello from Edge!" })
}
```

---

## 🚀 Monorepo (Turborepo)

```bash
pnpm add -D turbo

# turbo.json
{
  "pipeline": {
    "build": { "dependsOn": ["^build"], "outputs": [".next/**"] },
    "dev": { "cache": false },
    "lint": { "dependsOn": ["^lint"] }
  }
}
```

---

## 🤖 AI 全栈开发模式（2026 行业实践）

> 基于 Bolt.new + PingCAP Full-Stack App Builder 架构调研

### 模式一：AI 全环境控制（Bolt.new 模式）

AI 模型不仅写代码，还能**控制文件系统、Node 服务器、包管理器、终端、浏览器控制台**。

```
用户 Prompt（"创建一个 Todo 应用，用 Next.js 15 + Tailwind + shadcn"）
  ↓
AI 规划项目结构
  ↓
创建项目 → 安装依赖 → 写代码 → 运行预览 → 修改 → 部署
  ↓                                                                          ↓
全程: 文件系统/包管理器/终端    一键部署到 Vercel
```

**实践技巧**:
- Prompt 里明确技术栈（"Next.js 15 App Router + Tailwind + Prisma"）
- 先搭骨架（路由+布局），再加功能
- 批量指令合并：一次提示同时改配色+响应式+加页面

### 模式二：7 步全自动管线（PingCAP 模式）

```
Prompt → ① Plan → ② Provision → ③ Generate → ④ Migrate → ⑤ Deploy → ⑥ Iterate
          规划     配GitHub+DB     Codex写代码   数据库迁移   自动部署    迭代
```

**架构亮点**:

| 组件 | 技术选型 | 作用 |
|:----|:--------|:----|
| 代码生成 | Codex (gpt-5.1) + Claude Sonnet | 混合模型：Codex 写骨架，Claude 复杂推理 |
| 数据库 | TiDB Serverless | 闲置自动缩到$0，按需付费 |
| 迁移 | Kysely | 类型安全 `up()`/`down()`，可回滚 |
| 版本 | Git 分支 ↔ 数据库分支 | 代码和数据版本一一对应 |
| 预览 | Vercel Sandbox | 每个分支独立预览环境 |
| 认证 | GitHub PAT | 自动创建仓库和推代码 |

**用户流**:
```
用户: "加一个 username 字段"
  → 新 TiDB 分支 + 新 Git 分支
  → Kysely migration: up() 加字段, down() 可回滚
  → Vercel 新 Preview
  → 如果满意: merge 到主分支
```

### 对我们开发的建议

| 场景 | 做法 |
|:----|:----|
| 快速原型 | Bolt.new 模式：AI 全环境控制，prompt→运行 |
| 全栈项目 | PingCAP 管线：Plan→Provision→Generate→Migrate→Deploy |
| 数据库 | TiDB Serverless / Neon，按需付费零成本闲置 |
| 迁移策略 | Kysely 类型安全，每个变更可回滚 |
| 版本同步 | Git 分支 ↔ 数据分支一一对应 |
| AI 模型 | 分层使用：便宜模型写骨架，强模型做复杂推理 |

---

## ⚡ 核心原则

| 原则 | 说明 |
|:----|:----|
| **Server First** | 默认用 RSC，只有交互才用 Client Component |
| **类型安全** | TypeScript 非可选，API 响应需 Zod 验证 |
| **单工具链** | Biome 替代 ESLint+Prettier，消除配置漂移 |
| **移动优先** | Tailwind 的 `sm:` `md:` `lg:` 断点系统 |
| **Edge 优先** | 能跑在 Edge 就不跑在 Server |
| **AI 驱动** | Copilot 生成骨架，人工做架构决策 |

---

## 🔗 参考

- [Next.js 15 Docs](https://nextjs.org/docs)
- [Tailwind CSS v3](https://tailwindcss.com/docs)
- [Biome](https://biomejs.dev)
- [Turborepo](https://turbo.build/repo)
- [Vercel Edge](https://vercel.com/docs/edge-network/overview)
- [Playwright](https://playwright.dev)
