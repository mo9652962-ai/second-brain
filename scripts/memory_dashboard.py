"""
记忆交互式仪表盘 — 本地 Web GUI
读取 memory-tracker.json 并生成可视化仪表盘

用法：
  uv run python scripts/memory_dashboard.py
  然后浏览器访问 http://localhost:8080
"""
import json, os, webbrowser
from pathlib import Path
from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime

TRACKER_FILE = Path.home() / ".openclaw/workspace/.hermes/memory-tracker.json"

def load_data():
    """加载追踪数据"""
    if not TRACKER_FILE.exists():
        return {"entries": {}, "created": datetime.now().isoformat(), "updated": ""}
    return json.loads(TRACKER_FILE.read_text(encoding="utf-8"))


def calculate_stats(entries):
    """计算聚合统计"""
    if not entries:
        return {"total": 0, "high": 0, "medium": 0, "low": 0, "avg_score": 0}
    total = len(entries)
    high = sum(1 for e in entries.values() if e["score"] >= 0.7)
    medium = sum(1 for e in entries.values() if 0.3 <= e["score"] < 0.7)
    low = sum(1 for e in entries.values() if e["score"] < 0.3)
    avg = sum(e["score"] for e in entries.values()) / max(total, 1)
    return {"total": total, "high": high, "medium": medium, "low": low, "avg_score": round(avg, 3)}


def build_html():
    """生成仪表盘 HTML"""
    data = load_data()
    entries = data.get("entries", {})
    stats = calculate_stats(entries)

    # 排序条目
    sorted_entries = sorted(entries.items(), key=lambda x: x[1]["score"], reverse=True)

    table_rows = ""
    for idx, (key, entry) in enumerate(sorted_entries, 1):
        total = entry["hit_count"]
        succ_rate = f"{entry['success_count']/max(total,1)*100:.0f}%"
        score = entry["score"]
        if score >= 0.7:
            badge = "🔥 高价值"
            color = "#22c55e"
        elif score >= 0.3:
            badge = "🟡 中等"
            color = "#eab308"
        else:
            badge = "⚪ 低价值"
            color = "#ef4444"

        table_rows += f"""<tr>
            <td>{idx}</td>
            <td title="{key}">{key[:48]}{'…' if len(key)>48 else ''}</td>
            <td><span class="badge" style="background:{color}20;color:{color};border:1px solid {color}40">{badge}</span></td>
            <td>{score:.3f}</td>
            <td>{entry['hit_count']}</td>
            <td>{succ_rate}</td>
            <td>{', '.join(entry.get('task_types', []))}</td>
        </tr>"""

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>记忆贡献度仪表盘</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4"></script>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: -apple-system, 'Segoe UI', system-ui, sans-serif; background: #f8fafc; color: #1e293b; }}
.header {{ background: linear-gradient(135deg, #1e293b, #334155); color: white; padding: 24px 40px; }}
.header h1 {{ font-size: 24px; font-weight: 600; }}
.header p {{ color: #94a3b8; margin-top: 4px; }}
.stats-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; padding: 24px 40px; }}
.stat-card {{ background: white; border-radius: 12px; padding: 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.08); }}
.stat-card .label {{ font-size: 13px; color: #64748b; }}
.stat-card .value {{ font-size: 28px; font-weight: 700; margin-top: 4px; }}
.chart-row {{ display: flex; gap: 24px; padding: 0 40px 24px; }}
.chart-box {{ flex: 1; background: white; border-radius: 12px; padding: 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.08); }}
.chart-box h3 {{ font-size: 14px; color: #64748b; margin-bottom: 12px; }}
.table-wrap {{ padding: 0 40px 40px; }}
table {{ width: 100%; border-collapse: separate; border-spacing: 0; background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.08); }}
th {{ background: #f1f5f9; text-align: left; padding: 12px 16px; font-size: 12px; text-transform: uppercase; color: #64748b; letter-spacing: 0.05em; }}
td {{ padding: 12px 16px; border-top: 1px solid #f1f5f9; font-size: 14px; }}
tr:hover td {{ background: #f8fafc; }}
.badge {{ padding: 2px 8px; border-radius: 6px; font-size: 12px; }}
.footer {{ text-align: center; color: #94a3b8; font-size: 12px; padding: 20px; }}
.refresh-btn {{ display: inline-block; margin: 12px 40px; padding: 8px 20px; background: #3b82f6; color: white; border: none; border-radius: 8px; cursor: pointer; font-size: 14px; }}
.refresh-btn:hover {{ background: #2563eb; }}
</style>
</head>
<body>
<div class="header">
    <h1>🧠 记忆贡献度仪表盘</h1>
    <p>最后更新: {data.get('updated', '')[:19]}</p>
</div>

<div class="stats-grid">
    <div class="stat-card"><div class="label">总记忆条目</div><div class="value">{stats['total']}</div></div>
    <div class="stat-card"><div class="label">🔥 高价值 (≥0.7)</div><div class="value" style="color:#22c55e">{stats['high']}</div></div>
    <div class="stat-card"><div class="label">🟡 中等 (0.3-0.7)</div><div class="value" style="color:#eab308">{stats['medium']}</div></div>
    <div class="stat-card"><div class="label">⚪ 低价值 (&lt;0.3)</div><div class="value" style="color:#ef4444">{stats['low']}</div></div>
    <div class="stat-card"><div class="label">平均贡献度</div><div class="value">{stats['avg_score']}</div></div>
</div>

<div class="chart-row">
    <div class="chart-box"><h3>价值分布</h3><canvas id="pieChart"></canvas></div>
    <div class="chart-box"><h3>价值-命中率散点</h3><canvas id="barChart"></canvas></div>
</div>

<div style="padding:0 40px"><button class="refresh-btn" onclick="location.reload()">🔄 刷新数据</button></div>

<div class="table-wrap">
    <table>
        <thead><tr>
            <th>#</th><th>记忆键</th><th>评级</th><th>贡献度</th><th>命中</th><th>成功率</th><th>任务类型</th>
        </tr></thead>
        <tbody>{table_rows}</tbody>
    </table>
</div>

<div class="footer">micro-mem-dashboard · 数据来自 {TRACKER_FILE}</div>

<script>
new Chart(document.getElementById('pieChart'), {{
    type: 'pie',
    data: {{
        labels: ['🔥 高价值', '🟡 中等', '⚪ 低价值'],
        datasets: [{{ data: [{stats['high']}, {stats['medium']}, {stats['low']}], backgroundColor: ['#22c55e80', '#eab30880', '#ef444480'] }}]
    }},
    options: {{ responsive: true, plugins: {{ legend: {{ position: 'bottom' }} }} }}
}});

new Chart(document.getElementById('barChart'), {{
    type: 'bar',
    data: {{
        labels: {json.dumps([k[:12] for k, _ in sorted_entries[:10]])},
        datasets: [{{
            label: '贡献度',
            data: {json.dumps([e['score'] for _, e in sorted_entries[:10]])},
            backgroundColor: {json.dumps(['#22c55e' if e['score']>=0.7 else '#eab308' if e['score']>=0.3 else '#ef4444' for _, e in sorted_entries[:10]])}
        }}]
    }},
    options: {{ responsive: true, plugins: {{ legend: {{ display: false }} }}, scales: {{ y: {{ beginAtZero: true, max: 1 }} }} }}
}});
</script>
</body>
</html>"""
    return html


class DashboardHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/dashboard":
            html = build_html()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(html.encode())))
            self.end_headers()
            self.wfile.write(html.encode())
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        print(f"  [{datetime.now().strftime('%H:%M:%S')}] {args[0]}")


def main():
    import sys as _sys
    out_path = Path.home() / "Desktop/memory-dashboard.html"
    
    if len(_sys.argv) > 1 and _sys.argv[1] == "--serve":
        port = int(_sys.argv[2]) if len(_sys.argv) > 2 else 8080
        server = HTTPServer(("0.0.0.0", port), DashboardHandler)
        url = f"http://localhost:{port}"
        print(f"🧠 记忆贡献度仪表盘已启动")
        print(f"  打开浏览器访问: {url}")
        print(f"  (按 Ctrl+C 停止)")
        webbrowser.open(url)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\n  仪表盘已停止")
        return
    
    # Default: save to desktop
    html = build_html()
    out_path.write_text(html, encoding="utf-8")
    print(f"✅ 仪表盘已保存到桌面: {out_path}")
    print(f"   双击 {out_path.name} 即可查看")
    webbrowser.open(str(out_path))


if __name__ == "__main__":
    main()
