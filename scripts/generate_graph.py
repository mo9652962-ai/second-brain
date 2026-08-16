# -*- coding: utf-8 -*-
"""Generate docs/obsidian-graph.png from real vault wikilinks (networkx + matplotlib)."""
import pathlib, re
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import networkx as nx

# Use a CJK-capable font on Windows
for cand in ["Microsoft YaHei", "SimHei", "SimSun", "Noto Sans CJK SC"]:
    try:
        fm.findfont(cand, fallback_to_default=False)
        plt.rcParams["font.sans-serif"] = [cand]
        break
    except Exception:
        continue
plt.rcParams["axes.unicode_minus"] = False

root = pathlib.Path(r"C:\Users\31954\.openclaw\workspace")
exclude_dirs = {".git", ".obsidian", ".venv", "graphify-out", ".code-review-graph", "node_modules", "outputs", "__pycache__", ".trash"}

def iter_md(base):
    for p in base.rglob("*.md"):
        rel = p.relative_to(base)
        if any(part in exclude_dirs for part in rel.parts):
            continue
        yield p

files = list(iter_md(root))
name_of = {}
for p in files:
    stem = p.stem
    name_of.setdefault(stem, p)

G = nx.DiGraph()
for p in files:
    stem = p.stem
    G.add_node(stem)
    try:
        txt = p.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        continue
    for m in re.findall(r"\[\[([^\]|#]+)", txt):
        target = m.strip()
        if target in name_of:
            G.add_edge(stem, target)

# Keep the largest weakly-connected component for a cleaner look
und = G.to_undirected()
comps = sorted(nx.connected_components(und), key=len, reverse=True)
keep = comps[0]
H = G.subgraph(keep)

pos = nx.spring_layout(H, k=0.55, iterations=60, seed=42)
fig, ax = plt.subplots(figsize=(20, 12), dpi=110)
ax.set_facecolor("#1e1e2e")
fig.patch.set_facecolor("#1e1e2e")

# Color by in-degree (hub notes stand out)
degs = dict(H.degree())
colors = [min(1.0, 0.15 + 0.85 * (degs[n] / max(1, max(degs.values())))) for n in H.nodes()]
nx.draw_networkx_edges(H, pos, ax=ax, edge_color="#45475a", width=0.35, arrows=False, alpha=0.6)
nodes = nx.draw_networkx_nodes(H, pos, ax=ax, node_size=[60 + 18 * degs[n] for n in H.nodes()],
                               node_color=colors, cmap=plt.cm.viridis, alpha=0.9)
# Label only hubs (degree >= 3) with small fonts
hubs = [n for n in H.nodes() if degs[n] >= 3]
nx.draw_networkx_labels(H, pos, ax=ax, labels={n: n for n in hubs},
                        font_size=6, font_color="#cdd6f4", alpha=0.85)
ax.set_title(f"Second Brain Knowledge Graph — {H.number_of_nodes()} notes · {H.number_of_edges()} links",
             color="#cdd6f4", fontsize=14)
ax.axis("off")
plt.tight_layout()
out = root / "docs" / "obsidian-graph.png"
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, dpi=110, bbox_inches="tight", facecolor=fig.get_facecolor())
print(f"OK {out} — nodes={H.number_of_nodes()} edges={H.number_of_edges()} comps_total={len(comps)}")
