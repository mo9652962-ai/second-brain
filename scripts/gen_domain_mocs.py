#!/usr/bin/env python3
"""为无 MOC 的知识域生成 MOC 锚点页。

背景：2026-09-20 仓库评估发现 9 个域无 MOC 锚点，导致：
- knowledge-map 之外无域级索引
- daily_vault_optimize 的 mount_orphans 对无 MOC 域只能挂 knowledge-map（粗粒度）

用法: python scripts/gen_domain_mocs.py [--commit]
"""
import argparse
import datetime
import pathlib
import re
import subprocess

VAULT = pathlib.Path.home() / ".openclaw" / "workspace"
KNOW = VAULT / "knowledge"

# 域 -> (标题, 图标, 描述, 分组规则[(分组名, 文件名正则)])
DOMAINS = {
    "cards": ("知识卡片", "🃏", "每日精选知识卡片（事件/论文/工具速览）",
              [("2026-07", r"^2026-07"), ("2026-08", r"^2026-08"), ("2026-09", r"^2026-09")]),
    "Daily": ("每日产出", "📅", "Hacker News 精选、每日回顾、产出研究",
              [("Hacker News 精选", r"^hackernews"), ("每日产出研究", r"^daily-output"),
               ("每日回顾", r"^(?!hackernews|daily-output).*")]),
    "AI": ("AI 研究与生态", "🤖", "Agent 评估、数字生命、知识库方法论",
           [("Agent / 数字生命", r"AIRI|agent|Agent"), ("知识库方法论", r"知识库|工具精度"),
            ("其他", r".*")]),
    "SOP": ("标准操作流程", "📋", "可复用的标准流程（故障排查/调研/升级/侦察）",
            [("SOP 全表", r"^SOP-")]),
    "Education": ("教育规划", "🎓", "学业规划、家教",
                  [("全部", r".*")]),
    "Creative": ("创意创作", "🎨", "AI 小说、去 AI 味、网文、视觉创作",
                 [("创作流水线", r"小说|novel|漫剧"), ("去 AI 味", r"ai-slop|de-ai|去 ?AI"),
                  ("其他", r".*")]),
    "Product": ("产品", "📦", "墨题及服务类产品研究",
                [("全部", r".*")]),
    "Projects": ("项目", "🚀", "进行中的项目笔记与决策记录",
                 [("全部", r".*")]),
    "Content": ("内容生产", "📣", "抖音 AI 博主、内容流水线、GEO 优化",
                [("内容流水线", r"抖音|脚本|hyperframes|视频"), ("GEO / 增长", r"GEO|生成式引擎"),
                 ("其他", r".*")]),
    "META": ("知识库治理", "🛠️", "知识库规则、MOC 体系、评测规范、研究方法论",
             [("规则与规范", r"RULES|规范|QUERY"), ("方法论", r"方法论|研究|技能"),
              ("其他", r".*")]),
    "gaming": ("游戏研究", "🎮", "游戏 mod、工具、联机",
               [("全部", r".*")]),
    "Archive": ("归档", "🗄️", "冻结的历史笔记",
                [("全部", r".*")]),
}

LINK_RE = re.compile(r"\[\[([^\]|#]+)")


def page_title(p: pathlib.Path) -> str:
    """取 frontmatter title，失败则取正文一级标题，再失败用文件名。"""
    t = p.read_text(encoding="utf-8", errors="ignore")
    m = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', t, re.M)
    if m and m.group(1).strip() not in ("---", ""):
        return m.group(1).strip()[:60]
    m = re.search(r"^#\s+(.+)$", t, re.M)
    if m:
        return m.group(1).strip()[:60]
    return p.stem


def has_inlink(p: pathlib.Path, all_pages) -> bool:
    stem = p.stem
    for q in all_pages:
        if q == p:
            continue
        for tgt in LINK_RE.findall(q.read_text(encoding="utf-8", errors="ignore")):
            if tgt.split("|")[0].split("#")[0].strip().rsplit("/", 1)[-1] in (stem, stem + ".md"):
                return True
    return False


def build_moc(domain: str, spec, pages) -> str:
    title, icon, desc, groups = spec
    today = datetime.date.today().isoformat()
    lines = [
        "---",
        f"tags: [MOC, {domain.lower()}]",
        f"domain: {domain}",
        "type: moc",
        "status: active",
        f"created: {today}",
        f"updated: {today}",
        "---",
        "",
        f"# {icon} {title} — {domain}",
        "",
        "> 🏠 [[HOME]] | 🗺️ [[knowledge/knowledge-map|知识地图]] | 📇 [[knowledge/index|索引]]",
        f"> {desc}",
        "",
    ]
    used = set()
    for gname, pat in groups:
        rx = re.compile(pat)
        sel = [p for p in pages if p not in used and rx.search(p.stem)]
        if not sel:
            continue
        used.update(sel)
        lines.append(f"## {gname}")
        lines.append("")
        for p in sorted(sel):
            rel = f"knowledge/{domain}/{p.name}"
            lines.append(f"- [[{rel[:-3]}|{page_title(p)}]]")
        lines.append("")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--commit", action="store_true")
    args = ap.parse_args()

    all_pages = [p for p in KNOW.rglob("*.md")]
    created = []
    for domain, spec in DOMAINS.items():
        d = KNOW / domain
        if not d.is_dir():
            continue
        moc = d / f"MOC-{domain}.md"
        if moc.exists():
            print(f"  [SKIP] 已存在: {moc.relative_to(VAULT)}")
            continue
        pages = [p for p in d.glob("*.md") if p != moc]
        if not pages:
            continue
        content = build_moc(domain, spec, pages)
        moc.write_text(content, encoding="utf-8")
        n_orphan = sum(1 for p in pages if not has_inlink(p, all_pages))
        print(f"  [NEW] {moc.relative_to(VAULT)} — {len(pages)} 篇（其中 {n_orphan} 篇此前无入链）")
        created.append(moc)

    print(f"\n新建 MOC: {len(created)}")

    if args.commit and created:
        subprocess.run(["git", "-C", str(VAULT), "add", "-A"], capture_output=True, timeout=60)
        r = subprocess.run(
            ["git", "-C", str(VAULT), "commit", "-m",
             f"P2 feat(vault): 为 {len(created)} 个无锚点域补 MOC\n\n"
             + "\n".join(f"- {m.relative_to(VAULT)}" for m in created)],
            capture_output=True, text=True, timeout=60)
        print("commit:", r.stdout.strip()[-60:] if r.returncode == 0 else r.stderr.strip()[-200:])


if __name__ == "__main__":
    main()
