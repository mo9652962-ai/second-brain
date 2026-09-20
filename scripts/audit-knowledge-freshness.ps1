#!/usr/bin/env pwsh
# audit-knowledge-freshness.ps1
# 只读扫描：找出知识库中过期的硬约束断言，按三类输出
#   CONFIRMED_STALE     — 与当前实测事实冲突，必须改
#   NEEDS_RUNTIME_VERIFY — 无法静态判定，需运行时验证
#   HISTORICAL_ALLOWED   — 历史记录，允许保留（memory/、Archive/、带历史标注的）
#
# 用法:
#   pwsh -File scripts/audit-knowledge-freshness.ps1
#   pwsh -File scripts/audit-knowledge-freshness.ps1 -Json
#
# 设计原则: 只读。不改任何文件。事实源见 knowledge/META/。

param(
    [switch]$Json,
    [string]$Root = (Split-Path -Parent $PSScriptRoot)
)

$ErrorActionPreference = 'Stop'
# 确保中文输出不乱码（git-bash / cmd 管道均适用）
try {
    [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
    $OutputEncoding = [System.Text.Encoding]::UTF8
} catch { }
$Knowledge = Join-Path $Root 'knowledge'
$Memory    = Join-Path $Root 'memory'

# ── 过期模式定义 ────────────────────────────────────────────────
# 每条: 正则, 分类, 原因
# 注意: 负向先行断言排除「无 Docker 方案/无 Docker 路线」这类**方案名**（不是断言）
$Patterns = @(
    @{ Re = '(?<!方案)(?<!路线)(?<!选型)本机无虚拟化|(?<!方案)(?<!路线)无虚拟化(?!方案)(?!路线)|没有虚拟化'; Cat = 'CONFIRMED_STALE'; Why = 'virtualisation claim conflicts with current HypervisorPresent=True' }
    @{ Re = 'Docker\s*不可用|(?<!方案)(?<!路线)(?<!下的)无\s*Docker(?!\s*(方案|路线|部署方案|栈|生产栈|部署栈|环境\)|不是障碍|生产|部署|）|\)| \+|\s*\+))'; Cat = 'CONFIRMED_STALE'; Why = 'Docker CLI v29.8.0 is installed; only the daemon is not running' }
    @{ Re = 'AppData[\\/]+Local[\\/]+hermes[\\/]+skills';   Cat = 'NEEDS_RUNTIME_VERIFY'; Why = 'skills dir is the live Hermes load path (503 SKILL.md) - verify the claim made about it' }
    @{ Re = '488\+';                                        Cat = 'CONFIRMED_STALE';      Why = 'hardcoded knowledge count; use knowledge/META/knowledge-sources.md' }
    @{ Re = '490\+';                                        Cat = 'CONFIRMED_STALE';      Why = 'hardcoded knowledge count; use knowledge/META/knowledge-sources.md' }
    @{ Re = '451\s*(个)?\s*skills|451\s*个\s*SKILL';        Cat = 'CONFIRMED_STALE';      Why = 'hardcoded skills count; use knowledge/META/knowledge-sources.md' }
    @{ Re = '1550\+';                                       Cat = 'CONFIRMED_STALE';      Why = 'hardcoded skills count; use knowledge/META/knowledge-sources.md' }
    @{ Re = 'deepseek-v4-flash(?!-vision)';                 Cat = 'NEEDS_RUNTIME_VERIFY'; Why = 'legacy alias; canonical model is deepseek-flash (verify context is not historical)' }
    @{ Re = 'flash-0731';                                   Cat = 'HISTORICAL_ALLOWED';   Why = 'dated model version reference' }
    @{ Re = '截至 2026-07|截至2026-07';                     Cat = 'HISTORICAL_ALLOWED';   Why = 'explicitly dated statement' }
    @{ Re = '当前最新';                                      Cat = 'NEEDS_RUNTIME_VERIFY'; Why = '"latest" claim needs a date range' }
    @{ Re = '(?<!能不能)(?<!需要)(?<!要)(?<!是否)已配置|(?<!能不能)(?<!需要)(?<!要)(?<!是否)已安装'; Cat = 'NEEDS_RUNTIME_VERIFY'; Why = 'install/config status not checked in current runtime' }
)

# ── 允许保留的路径（历史记录） ──────────────────────────────────
$HistoricalPaths = @(
    [regex]::Escape($Memory)
    [regex]::Escape((Join-Path $Knowledge 'Archive'))
    [regex]::Escape((Join-Path $Knowledge 'META\current-environment.md'))
    [regex]::Escape((Join-Path $Knowledge 'META\current-model-status.md'))
    [regex]::Escape((Join-Path $Knowledge 'META\knowledge-sources.md'))
    # 日期命名的周期性报告：token-usage-report-YYYYMMDD / hackernews-YYYY-MM-DD 等 → 天然是历史快照
    '(?i)token-usage-report-\d{8}\.md$'
    '(?i)(hackernews|arxiv|graphify|github)[-_].*\d{4}-\d{2}-\d{2}.*\.md$'
    '(?i)[-_]\d{4}-\d{2}-\d{2}[^\\/]*\.md$'
)

# 历史标注标记：文件顶部若含这些，视为已标注
$HistoricalMarkers = @(
    '历史记录', '历史状态', '历史路线', '历史配置', '已退役', '快照',    '不代表当前', '需单独运行时验证', '截至 2026-', '截至2026-'
)

function Test-IsHistorical {
    param([string]$Path, [string]$Head)
    foreach ($p in $HistoricalPaths) { if ($Path -match $p) { return $true } }
    foreach ($m in $HistoricalMarkers) { if ($Head -match [regex]::Escape($m)) { return $true } }
    return $false
}

# ── 扫描 ────────────────────────────────────────────────────────
$findings = [System.Collections.Generic.List[object]]::new()
$files = Get-ChildItem -Path $Knowledge, $Memory -Recurse -Filter '*.md' -File -ErrorAction SilentlyContinue

foreach ($f in $files) {
    $lines = Get-Content -LiteralPath $f.FullName -Encoding UTF8 -ErrorAction SilentlyContinue
    if (-not $lines) { continue }
    $head = ($lines | Select-Object -First 40) -join "`n"
    $isHist = Test-IsHistorical -Path $f.FullName -Head $head

    for ($i = 0; $i -lt $lines.Count; $i++) {
        $line = $lines[$i]
        foreach ($p in $Patterns) {
            if ($line -match $p.Re) {
                $cat = $p.Cat
                # 上下文窗口：本行 + 后续 5 行（修订标注常写在下一行）
                $ctxEnd = [Math]::Min($i + 5, $lines.Count - 1)
                $ctx = ($lines[$i..$ctxEnd] -join "`n")
                # 已带修订/历史标注 → 降级为 HISTORICAL_ALLOWED（这些是"已处理的痕迹"）
                if ($ctx -match '2026-09-20 (修订|修正|更新|更正)|已过期|已不成立|已作废|修正为|已退役|历史记录|历史状态|历史路线|历史配置|历史快照|不代表当前|以官方|为准|需单独运行时验证|待运行时验证|待 Docker|Docker CLI 已装|Daemon 未运行|假阴性') {
                    if ($cat -eq 'CONFIRMED_STALE' -or $cat -eq 'NEEDS_RUNTIME_VERIFY') { $cat = 'HISTORICAL_ALLOWED' }
                }
                # 历史文件（路径或头部标注）→ 全部降级为 HISTORICAL_ALLOWED
                if ($isHist -and $cat -ne 'HISTORICAL_ALLOWED') { $cat = 'HISTORICAL_ALLOWED' }
                # 排除误报：wikilink 内、纯产品特性描述
                $isFalsePositive = $false
                if ($line -match '\[\[[^\]]*\]\]') {
                    # 若整行的匹配都在 wikilink 里，视为误报
                    $stripped = $line -replace '\[\[[^\]]*\]\]', ''
                    if ($stripped -notmatch $p.Re) { $isFalsePositive = $true }
                }
                if ($line -match '无\s*Docker\s*/\s*无运行时|无 Docker / 无运行时') { $isFalsePositive = $true }
                if ($isFalsePositive) { break }
                $rel = $f.FullName.Substring($Root.Length).TrimStart('\','/')
                $findings.Add([pscustomobject]@{
                    Category = $cat
                    File     = $rel
                    Line     = $i + 1
                    Reason   = $p.Why
                    Text     = $line.Trim()
                })
                break
            }
        }
    }
}

# ── 输出 ────────────────────────────────────────────────────────
$order = @('CONFIRMED_STALE','NEEDS_RUNTIME_VERIFY','HISTORICAL_ALLOWED')

if ($Json) {
    $findings | ConvertTo-Json -Depth 4
    exit 0
}

Write-Output "═══════════════════════════════════════════════════════════"
Write-Output " 知识库时效性审计 (read-only)"
Write-Output " 扫描时间: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
Write-Output " 扫描范围: knowledge/ + memory/  ($($files.Count) 个 .md)"
Write-Output "═══════════════════════════════════════════════════════════"
Write-Output ""

foreach ($cat in $order) {
    $group = $findings | Where-Object { $_.Category -eq $cat }
    Write-Output "$cat ($($group.Count)):"
    if ($group.Count -eq 0) { Write-Output "  (无)"; Write-Output ""; continue }
    # CONFIRMED_STALE 最多列 20 条，其余汇总
    $show = if ($cat -eq 'CONFIRMED_STALE') { $group | Select-Object -First 20 } else { $group }
    foreach ($g in $show) {
        Write-Output "  - $($g.File):$($g.Line)"
        Write-Output "    reason: $($g.Reason)"
    }
    if ($group.Count -gt $show.Count) {
        Write-Output "  ... 另有 $($group.Count - $show.Count) 条同类（-Json 查看全部）"
    }
    Write-Output ""
}

Write-Output "───────────────────────────────────────────────────────────"
Write-Output "合计: $($findings.Count) 条"
Write-Output "  其中 CONFIRMED_STALE 需人工修正；NEEDS_RUNTIME_VERIFY 需运行时验证；"
Write-Output "  HISTORICAL_ALLOWED 属正常历史记录，无需处理。"
