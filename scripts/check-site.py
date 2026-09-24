#!/usr/bin/env python3
"""check-site.py — 官网 + 文档站门禁（CI 用）

静态检查（默认运行，无依赖）：
  S1  mkdocs.yml nav 目标全部存在于 tracked 文件
      → 防「nav 指向不存在的页面」导致构建"成功"但站点是空的
        （2026-09-21 事故：docs_dir 未设 + 20 条 nav 全 not found → 线上只有 2 页）
  S2  全库 md 可组装（git -c core.quotePath=false ls-files -z）
      → 防中文路径被加引号转义导致 CI `cp` 失败
        （2026-09-21 事故：219 个非 ASCII 路径在 Linux CI 全部 cp 失败）
  S3  docs-site 静态完整性
      → 标签闭合 / 本地引用可解析 / CSS 网格 minmax(0,1fr) / JS 无 innerHTML 调用

浏览器检查（--browser，需 playwright）：
  B1  移动端 390px 零横向溢出
      → 防网格被 nowrap 内容撑破（2026-09-21 事故：溢出 141px）
  B2  滚动后 .reveal 全触发（无永久隐形内容）
      → 防 IntersectionObserver 不触发导致内容 opacity:0

用法：
  python scripts/check-site.py              # 静态检查
  python scripts/check-site.py --browser    # 静态 + 浏览器
退出码：0 = 全通过，1 = 有失败
"""
import os
import re
import subprocess
import sys
import socket
import shutil
import tempfile
import time
import contextlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_DIR = os.path.join(ROOT, "docs-site")
MKDOCS = os.path.join(ROOT, "mkdocs.yml")

FAILURES = []
CHECKS = 0


def ok(name, detail=""):
    global CHECKS
    CHECKS += 1
    print("  \u2705 %-52s %s" % (name, detail))


def fail(name, detail=""):
    global CHECKS
    CHECKS += 1
    FAILURES.append((name, detail))
    print("  \u274c %-52s %s" % (name, detail))


def tracked_files(*patterns):
    """git ls-files -z + quotePath=false：非 ASCII 路径原样返回，不加引号。"""
    cmd = ["git", "-c", "core.quotePath=false", "ls-files", "-z"]
    cmd += list(patterns)
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True)
    if r.returncode != 0:
        return None
    return [p for p in r.stdout.decode("utf-8", "replace").split("\0") if p]


# ── S1: mkdocs nav 目标存在性 ────────────────────────────────
def check_nav_targets():
    print("\n[S1] mkdocs.yml nav 目标存在性")
    if not os.path.exists(MKDOCS):
        fail("mkdocs.yml 存在", "文件缺失")
        return
    tracked = tracked_files()
    if tracked is None:
        fail("git ls-files 可用", "命令失败")
        return
    tracked_set = set(tracked)

    content = open(MKDOCS, encoding="utf-8").read()
    # 匹配 nav 条目：`- 标题: 路径.md`（含缩进）
    nav = re.findall(r"^\s*-\s+[^:\n]+:\s+(\S+\.md)\s*$", content, re.M)
    if not nav:
        fail("nav 条目可解析", "未解析到任何 .md 条目（格式变了？）")
        return

    missing = [p for p in nav if p not in tracked_set]
    if missing:
        fail("nav 目标全部存在", "%d/%d 缺失: %s" % (len(missing), len(nav), missing[:5]))
    else:
        ok("nav 目标全部存在", "%d 条全部命中 tracked" % len(nav))

    # docs_dir 必须可被 CI 注入（否则回退到默认 docs/，nav 必然大面积 not found）
    if "docs_dir" in content and "MKDOCS_DOCS_DIR" in content:
        ok("docs_dir 支持 CI 注入", "!ENV MKDOCS_DOCS_DIR")
    else:
        fail("docs_dir 支持 CI 注入",
             "缺少 docs_dir: !ENV [MKDOCS_DOCS_DIR, docs] → nav 会大面积 not found")


# ── S2: 全库 md 可组装（中文路径）───────────────────────────
def check_assemble():
    print("\n[S2] 全库 md 组装（非 ASCII 路径）")
    files = tracked_files("*.md")
    if files is None:
        fail("git ls-files 可用", "命令失败")
        return
    if len(files) < 100:
        fail("md 文件数量合理", "仅 %d 个（异常偏低）" % len(files))
        return

    tmp = tempfile.mkdtemp(prefix="check-site-assemble-")
    failed = []
    try:
        for f in files:
            dst = os.path.join(tmp, f.replace("/", os.sep))
            try:
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copyfile(os.path.join(ROOT, f), dst)
            except Exception as e:  # noqa: BLE001
                failed.append((f, str(e)[:60]))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    nonascii = sum(1 for f in files if any(ord(c) > 127 for c in f))
    if failed:
        fail("全库 md 可组装", "%d 个失败（示例 %s）" % (len(failed), failed[0]))
    else:
        ok("全库 md 可组装", "%d 个文件（含 %d 个非 ASCII 路径）" % (len(files), nonascii))


# ── S3: docs-site 静态完整性 ────────────────────────────────
def check_static_site():
    print("\n[S3] docs-site 静态完整性")
    idx = os.path.join(SITE_DIR, "index.html")
    css_p = os.path.join(SITE_DIR, "landing.css")
    js_p = os.path.join(SITE_DIR, "landing.js")
    for p in (idx, css_p, js_p):
        if not os.path.exists(p):
            fail("docs-site 三件套存在", "缺失 %s" % os.path.basename(p))
            return

    html = open(idx, encoding="utf-8").read()
    css = open(css_p, encoding="utf-8").read()
    js = open(js_p, encoding="utf-8").read()

    # 标签闭合
    bad_tags = []
    for tag in ("section", "div", "article", "main", "header", "footer", "nav"):
        o, c = html.count("<" + tag), html.count("</" + tag + ">")
        if o != c:
            bad_tags.append("%s %d/%d" % (tag, o, c))
    if bad_tags:
        fail("HTML 标签闭合", ", ".join(bad_tags))
    else:
        ok("HTML 标签闭合", "7 类标签平衡")

    # 本地引用可解析
    refs = [m for m in re.findall(r'(?:href|src)="([^"]+)"', html)
            if not m.startswith(("http", "#", "data:", "mailto"))]
    broken = []
    for r in refs:
        if not r.startswith("./"):
            continue
        target = r[2:].rstrip("/")
        if target.startswith("kb") or target.endswith("kb") or target == "":
            continue  # /kb/ 及其子页面由 deploy workflow 构建，不在 docs-site 内
        if not os.path.exists(os.path.join(SITE_DIR, target)):
            broken.append(r)
    if broken:
        fail("本地引用可解析", "断链: %s" % broken[:3])
    else:
        ok("本地引用可解析", "%d 个引用" % len(refs))

    # CSS 网格必须 minmax(0,1fr)（防被 nowrap 内容撑破）
    no_minmax = []
    for sel in (".cards", ".start-grid", ".dom-grid", ".split", ".hero"):
        m = re.search(re.escape(sel) + r"\s*\{[^}]*grid-template-columns\s*:\s*([^;]+);",
                      css, re.S)
        if m and "minmax(0," not in m.group(1):
            no_minmax.append(sel)
    if no_minmax:
        fail("网格用 minmax(0,1fr)", "未防护: %s" % no_minmax)
    else:
        ok("网格用 minmax(0,1fr)", "5 个网格已防护")

    # JS 不得有 innerHTML 调用（剥离注释后判定）
    code_only = "\n".join(l.split("//")[0] for l in js.split("\n"))
    code_only = re.sub(r"/\*.*?\*/", "", code_only, flags=re.S)
    if "innerHTML" in code_only:
        fail("JS 无 innerHTML 调用", "存在 XSS 面")
    else:
        ok("JS 无 innerHTML 调用", "仅用 DOM API")

    # reveal 必须有兜底（否则内容永久隐形）
    if "sweep" in js and "requestAnimationFrame(sweep)" in js:
        ok("reveal 有 rAF 兜底", "sweep 存在")
    else:
        fail("reveal 有 rAF 兜底", "缺兜底 → 锚点/快速滚动时内容会永久隐形")


# ── B1/B2: 浏览器行为 ───────────────────────────────────────
def free_port():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


@contextlib.contextmanager
def serve(directory):
    port = free_port()
    proc = subprocess.Popen(
        [sys.executable, "-m", "http.server", str(port), "--bind", "127.0.0.1"],
        cwd=directory, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        for _ in range(40):
            try:
                socket.create_connection(("127.0.0.1", port), timeout=0.4).close()
                break
            except OSError:
                time.sleep(0.25)
        yield "http://127.0.0.1:%d/" % port
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=10)
        except subprocess.TimeoutExpired:
            proc.kill()


def check_browser():
    print("\n[B1/B2] 浏览器行为（真实 Chromium）")
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        fail("playwright 可用", "未安装 → CI 需 pip install playwright + playwright install chromium")
        return

    errors = []
    with serve(SITE_DIR) as url:
        with sync_playwright() as p:
            browser = p.chromium.launch()

            # ── B1: 移动端 390px 零横向溢出 ──
            # 注意：不能用 is_mobile=True（会改变视口宽度导致误判）
            m = browser.new_page(viewport={"width": 390, "height": 844}, has_touch=True)
            m.on("pageerror", lambda e: errors.append("mobile: " + str(e)[:80]))
            m.goto(url, wait_until="networkidle", timeout=60000)
            m.wait_for_timeout(2200)
            overflow = m.evaluate(
                "document.documentElement.scrollWidth - document.documentElement.clientWidth")
            if overflow and overflow > 0:
                fail("移动端 390px 零横向溢出", "溢出 %dpx" % overflow)
            else:
                ok("移动端 390px 零横向溢出", "0px")
            m.close()

            # ── B2: 滚动后 reveal 全触发 ──
            d = browser.new_page(viewport={"width": 1440, "height": 900})
            d.on("pageerror", lambda e: errors.append("desktop: " + str(e)[:80]))
            d.goto(url, wait_until="networkidle", timeout=60000)
            d.wait_for_timeout(2000)
            d.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            d.wait_for_timeout(1800)
            shown = d.eval_on_selector_all(".reveal.is-in", "e => e.length")
            total = d.eval_on_selector_all(".reveal", "e => e.length")
            if total == 0:
                fail("reveal 元素存在", "页面无 .reveal（选择器变了？）")
            elif shown < total:
                fail("滚动后 reveal 全触发", "%d/%d（有内容永久隐形）" % (shown, total))
            else:
                ok("滚动后 reveal 全触发", "%d/%d" % (shown, total))

            # 控制台错误
            if errors:
                fail("控制台零 error", "; ".join(errors[:3]))
            else:
                ok("控制台零 error", "(none)")
            d.close()
            browser.close()


def main():
    with_browser = "--browser" in sys.argv
    print("=" * 68)
    print("check-site.py — 官网 + 文档站门禁%s" % ("（含浏览器）" if with_browser else "（静态）"))
    print("=" * 68)

    check_nav_targets()
    check_assemble()
    check_static_site()
    if with_browser:
        check_browser()

    print("\n" + "=" * 68)
    if FAILURES:
        print("\u274c 失败 %d / 共 %d 项" % (len(FAILURES), CHECKS))
        for n, det in FAILURES:
            print("   - %s | %s" % (n, det))
        return 1
    print("\u2705 全部通过（%d 项）" % CHECKS)
    return 0


if __name__ == "__main__":
    sys.exit(main())
