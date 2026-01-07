#!/usr/bin/env python3
"""
Visualization script for thinking patterns analysis.
"""

import json
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

OUTPUT_PATH = Path("/home/orchestra/projects/thinking_patterns_llm_analysis/results")
PLOTS_PATH = OUTPUT_PATH / "plots"
PLOTS_PATH.mkdir(exist_ok=True)

# Load data
with open(OUTPUT_PATH / "analysis_results.json") as f:
    analysis = json.load(f)

with open(OUTPUT_PATH / "pattern_taxonomy.json") as f:
    taxonomy_data = json.load(f)

taxonomy = taxonomy_data.get("taxonomy", [])
pattern_names = analysis["pattern_names"]

# Color scheme
colors = plt.cm.Set3(np.linspace(0, 1, 15))
pattern_colors = {f"P{i:02d}": colors[i-1] for i in range(1, 16)}

# 1. Overall Pattern Distribution (Horizontal Bar Chart)
print("Creating pattern distribution chart...")
fig, ax = plt.subplots(figsize=(14, 10))

sorted_patterns = sorted(
    [(pid, count) for pid, count in analysis["primary_pattern_counts"].items() if pid != "unknown"],
    key=lambda x: x[1], reverse=True
)

patterns = [f"{pid}: {pattern_names.get(pid, pid)[:35]}" for pid, _ in sorted_patterns]
counts = [count for _, count in sorted_patterns]
pcts = [count / analysis["total_papers"] * 100 for count in counts]

y_pos = np.arange(len(patterns))
bars = ax.barh(y_pos, pcts, color=[pattern_colors.get(pid.split(":")[0], 'gray') for pid, _ in sorted_patterns])

ax.set_yticks(y_pos)
ax.set_yticklabels(patterns, fontsize=10)
ax.invert_yaxis()
ax.set_xlabel('Percentage of Papers (%)', fontsize=12)
ax.set_title('Thinking Patterns in Top ML Research (2023-2025)\n3,291 Papers from NeurIPS, ICML, ICLR', fontsize=14, fontweight='bold')

# Add percentage labels
for i, (bar, pct, count) in enumerate(zip(bars, pcts, counts)):
    ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2, 
            f'{pct:.1f}% ({count})', va='center', fontsize=9)

ax.set_xlim(0, max(pcts) * 1.2)
ax.axvline(x=10, color='red', linestyle='--', alpha=0.3, label='10% threshold')
plt.tight_layout()
plt.savefig(PLOTS_PATH / "pattern_distribution.png", dpi=150, bbox_inches='tight')
plt.close()

# 2. Year-over-Year Trends
print("Creating year trends chart...")
fig, ax = plt.subplots(figsize=(14, 8))

years = sorted(analysis["by_year"].keys())
top_patterns = [pid for pid, _ in sorted_patterns[:8]]

x = np.arange(len(years))
width = 0.1
multiplier = 0

for pid in top_patterns:
    pcts_by_year = []
    for year in years:
        year_total = sum(analysis["by_year"][year].values())
        count = analysis["by_year"][year].get(pid, 0)
        pcts_by_year.append(count / year_total * 100)
    
    offset = width * multiplier
    bars = ax.bar(x + offset, pcts_by_year, width, label=f"{pid}: {pattern_names.get(pid, pid)[:25]}", 
                  color=pattern_colors.get(pid, 'gray'))
    multiplier += 1

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Percentage of Papers (%)', fontsize=12)
ax.set_title('Evolution of Thinking Patterns (2023-2025)', fontsize=14, fontweight='bold')
ax.set_xticks(x + width * (len(top_patterns) - 1) / 2)
ax.set_xticklabels([str(y) for y in years])
ax.legend(loc='upper right', fontsize=8, ncol=2)
ax.set_ylim(0, 30)

plt.tight_layout()
plt.savefig(PLOTS_PATH / "year_trends.png", dpi=150, bbox_inches='tight')
plt.close()

# 3. Conference Comparison
print("Creating conference comparison chart...")
fig, axes = plt.subplots(1, 3, figsize=(16, 6))

conferences = ["NeurIPS", "ICML", "ICLR"]
top_6_patterns = [pid for pid, _ in sorted_patterns[:6]]

for idx, conf in enumerate(conferences):
    ax = axes[idx]
    conf_data = analysis["by_conference"].get(conf, {})
    conf_total = sum(conf_data.values())
    
    pattern_pcts = []
    labels = []
    for pid in top_6_patterns:
        count = conf_data.get(pid, 0)
        pct = count / conf_total * 100 if conf_total > 0 else 0
        pattern_pcts.append(pct)
        labels.append(f"{pid}")
    
    # Add "Other" category
    other_pct = 100 - sum(pattern_pcts)
    pattern_pcts.append(other_pct)
    labels.append("Other")
    
    colors_pie = [pattern_colors.get(pid, 'gray') for pid in top_6_patterns] + ['lightgray']
    
    wedges, texts, autotexts = ax.pie(pattern_pcts, labels=labels, autopct='%1.1f%%',
                                       colors=colors_pie, startangle=90)
    ax.set_title(f'{conf}\n({conf_total} papers)', fontsize=12, fontweight='bold')

# Add legend
legend_labels = [f"{pid}: {pattern_names.get(pid, pid)[:30]}" for pid in top_6_patterns] + ["Other patterns"]
fig.legend(legend_labels, loc='lower center', ncol=4, fontsize=9, bbox_to_anchor=(0.5, -0.05))

plt.suptitle('Pattern Distribution by Conference', fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(PLOTS_PATH / "conference_comparison.png", dpi=150, bbox_inches='tight')
plt.close()

# 4. Co-occurrence Heatmap
print("Creating co-occurrence heatmap...")
fig, ax = plt.subplots(figsize=(12, 10))

# Get top 10 patterns for heatmap
top_10 = [pid for pid, _ in sorted_patterns[:10]]
cooc_matrix = np.zeros((10, 10))

for i, p1 in enumerate(top_10):
    for j, p2 in enumerate(top_10):
        if p1 in analysis["cooccurrence"]:
            cooc_matrix[i, j] = analysis["cooccurrence"][p1].get(p2, 0)

im = ax.imshow(cooc_matrix, cmap='YlOrRd')

ax.set_xticks(np.arange(10))
ax.set_yticks(np.arange(10))
ax.set_xticklabels([f"{pid}" for pid in top_10], rotation=45, ha='right')
ax.set_yticklabels([f"{pid}: {pattern_names.get(pid, pid)[:20]}" for pid in top_10])

# Add text annotations
for i in range(10):
    for j in range(10):
        val = int(cooc_matrix[i, j])
        if val > 0:
            text = ax.text(j, i, val, ha="center", va="center", 
                          color="white" if val > 100 else "black", fontsize=8)

ax.set_title('Pattern Co-occurrence Matrix\n(Primary → Secondary)', fontsize=14, fontweight='bold')
ax.set_xlabel('Secondary Pattern', fontsize=11)
ax.set_ylabel('Primary Pattern', fontsize=11)

cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.set_ylabel('Co-occurrence Count', rotation=-90, va="bottom")

plt.tight_layout()
plt.savefig(PLOTS_PATH / "cooccurrence_heatmap.png", dpi=150, bbox_inches='tight')
plt.close()

# 5. Pattern Categories Sunburst-like visualization
print("Creating category breakdown chart...")
fig, ax = plt.subplots(figsize=(12, 8))

# Group patterns by category
categories = taxonomy_data.get("categories", [])
cat_data = []

for cat in categories:
    cat_name = cat["name"]
    cat_patterns = cat["pattern_ids"]
    cat_count = sum(analysis["primary_pattern_counts"].get(pid, 0) for pid in cat_patterns)
    cat_data.append((cat_name, cat_count, cat_patterns))

cat_data.sort(key=lambda x: x[1], reverse=True)

# Create grouped bar chart
cat_names = [c[0][:25] for c in cat_data]
cat_counts = [c[1] for c in cat_data]
cat_pcts = [c / analysis["total_papers"] * 100 for c in cat_counts]

y_pos = np.arange(len(cat_names))
bars = ax.barh(y_pos, cat_pcts, color=plt.cm.Pastel1(np.linspace(0, 1, len(cat_names))))

ax.set_yticks(y_pos)
ax.set_yticklabels(cat_names, fontsize=10)
ax.invert_yaxis()
ax.set_xlabel('Percentage of Papers (%)', fontsize=12)
ax.set_title('Thinking Pattern Categories', fontsize=14, fontweight='bold')

for bar, pct, count in zip(bars, cat_pcts, cat_counts):
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
            f'{pct:.1f}% ({count})', va='center', fontsize=9)

ax.set_xlim(0, max(cat_pcts) * 1.3)
plt.tight_layout()
plt.savefig(PLOTS_PATH / "category_breakdown.png", dpi=150, bbox_inches='tight')
plt.close()

# 6. Oral vs Spotlight comparison
print("Creating presentation type comparison...")
fig, ax = plt.subplots(figsize=(12, 6))

pres_types = ["oral", "spotlight"]
top_8 = [pid for pid, _ in sorted_patterns[:8]]

x = np.arange(len(top_8))
width = 0.35

for idx, ptype in enumerate(pres_types):
    ptype_data = analysis["by_presentation_type"].get(ptype, {})
    ptype_total = sum(ptype_data.values())
    
    pcts = []
    for pid in top_8:
        count = ptype_data.get(pid, 0)
        pct = count / ptype_total * 100 if ptype_total > 0 else 0
        pcts.append(pct)
    
    offset = width * idx
    bars = ax.bar(x + offset, pcts, width, label=f'{ptype.capitalize()} ({ptype_total})')

ax.set_xlabel('Pattern', fontsize=12)
ax.set_ylabel('Percentage (%)', fontsize=12)
ax.set_title('Pattern Distribution: Oral vs Spotlight Papers', fontsize=14, fontweight='bold')
ax.set_xticks(x + width / 2)
ax.set_xticklabels([f"{pid}\n{pattern_names.get(pid, pid)[:15]}" for pid in top_8], fontsize=8)
ax.legend()
ax.set_ylim(0, 30)

plt.tight_layout()
plt.savefig(PLOTS_PATH / "oral_vs_spotlight.png", dpi=150, bbox_inches='tight')
plt.close()

# 7. Top Pattern Pairs (Co-occurrence)
print("Creating top pattern pairs chart...")
fig, ax = plt.subplots(figsize=(14, 8))

# Parse pattern pairs
pairs_data = []
for pair_str, count in analysis.get("pattern_pairs", {}).items():
    try:
        pair = eval(pair_str)
        if len(pair) == 2:
            p1_name = pattern_names.get(pair[0], pair[0])[:20]
            p2_name = pattern_names.get(pair[1], pair[1])[:20]
            pairs_data.append((f"{pair[0]}+{pair[1]}", f"{p1_name} + {p2_name}", count))
    except:
        pass

pairs_data.sort(key=lambda x: x[2], reverse=True)
top_pairs = pairs_data[:15]

pair_labels = [p[1] for p in top_pairs]
pair_counts = [p[2] for p in top_pairs]

y_pos = np.arange(len(pair_labels))
bars = ax.barh(y_pos, pair_counts, color=plt.cm.viridis(np.linspace(0.3, 0.9, len(pair_labels))))

ax.set_yticks(y_pos)
ax.set_yticklabels(pair_labels, fontsize=9)
ax.invert_yaxis()
ax.set_xlabel('Co-occurrence Count', fontsize=12)
ax.set_title('Most Common Pattern Combinations\n(Primary + Secondary)', fontsize=14, fontweight='bold')

for bar, count in zip(bars, pair_counts):
    ax.text(bar.get_width() + 2, bar.get_y() + bar.get_height()/2,
            str(count), va='center', fontsize=9)

ax.set_xlim(0, max(pair_counts) * 1.15)
plt.tight_layout()
plt.savefig(PLOTS_PATH / "top_pattern_pairs.png", dpi=150, bbox_inches='tight')
plt.close()

# 8. Summary infographic
print("Creating summary infographic...")
fig = plt.figure(figsize=(16, 12))

# Title
fig.suptitle('Thinking Patterns in Top ML Research: Key Findings', fontsize=18, fontweight='bold', y=0.98)

# Key stats box
ax1 = fig.add_axes([0.05, 0.75, 0.4, 0.18])
ax1.axis('off')
stats_text = f"""
📊 DATASET OVERVIEW
• Total Papers Analyzed: {analysis['total_papers']:,}
• Conferences: NeurIPS, ICML, ICLR
• Years: 2023-2025 (Oral & Spotlight)
• Patterns Discovered: 15 distinct patterns
• Classification Confidence: 80% High, 10% Medium-High
"""
ax1.text(0, 1, stats_text, transform=ax1.transAxes, fontsize=11,
         verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.3))

# Top 3 patterns
ax2 = fig.add_axes([0.5, 0.75, 0.45, 0.18])
ax2.axis('off')
top3 = sorted_patterns[:3]
top3_text = f"""
🏆 TOP 3 THINKING PATTERNS
1. Gap-Driven Reframing: {top3[0][1]} papers (24.2%)
   "Diagnose limitation → Reframe problem"
   
2. Cross-Domain Synthesis: {top3[1][1]} papers (18.0%)
   "Import ideas from other fields"
   
3. Representation Shift: {top3[2][1]} papers (10.5%)
   "Change core primitives/abstractions"
"""
ax2.text(0, 1, top3_text, transform=ax2.transAxes, fontsize=11,
         verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.3))

# Mini bar chart
ax3 = fig.add_axes([0.08, 0.35, 0.4, 0.35])
top_5 = sorted_patterns[:5]
names = [pattern_names.get(p, p)[:25] for p, _ in top_5]
vals = [c/analysis['total_papers']*100 for _, c in top_5]
bars = ax3.barh(range(5), vals, color=['#2ecc71', '#3498db', '#9b59b6', '#e74c3c', '#f39c12'])
ax3.set_yticks(range(5))
ax3.set_yticklabels(names, fontsize=10)
ax3.invert_yaxis()
ax3.set_xlabel('% of Papers')
ax3.set_title('Top 5 Patterns', fontsize=12, fontweight='bold')
for bar, val in zip(bars, vals):
    ax3.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2, f'{val:.1f}%', va='center')

# Key insights
ax4 = fig.add_axes([0.55, 0.35, 0.4, 0.35])
ax4.axis('off')
insights_text = """
💡 KEY INSIGHTS

1. REFRAME + REPRESENT = BREAKTHROUGH
   Most impactful papers combine gap identification
   with new representations (303 co-occurrences)

2. CROSS-DOMAIN SYNTHESIS DRIVES NOVELTY
   18% of papers import ideas from other fields
   
3. VALIDATION IS ESSENTIAL
   Formal-Experimental Tightening appears as
   secondary pattern in 7.4% of papers

4. UNDEREXPLORED OPPORTUNITIES
   • Multiscale Modeling (1.5%)
   • Inference-Time Control (2.7%)
   • Active Sampling (2.3%)

5. CONFERENCE PREFERENCES
   • ICLR: Representations & Benchmarks
   • ICML: Formal/Statistical Methods
   • NeurIPS: Cross-Disciplinary Work
"""
ax4.text(0, 1, insights_text, transform=ax4.transAxes, fontsize=10,
         verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.3))

# Actionable advice
ax5 = fig.add_axes([0.08, 0.05, 0.87, 0.25])
ax5.axis('off')
advice_text = """
🎯 ACTIONABLE ADVICE FOR RESEARCHERS

FOR PhD STUDENTS:                          FOR EXPERIENCED RESEARCHERS:              THE WINNING FORMULA:
• Practice writing "gap statements"        • Build cross-domain teams                1. Start with a crisp, quantifiable gap
• Master one cross-domain tool             • Create transferable tooling/benchmarks  2. Ask: "What primitive would make this simple?"
• Start with small reframe+repr projects   • Mentor focused validation experiments   3. Borrow abstractions from other domains
• Follow: Gap → Repr → Validate arc                                                  4. Back with rigorous experiments/theory
"""
ax5.text(0, 1, advice_text, transform=ax5.transAxes, fontsize=9,
         verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle='round', facecolor='lavender', alpha=0.3))

plt.savefig(PLOTS_PATH / "summary_infographic.png", dpi=150, bbox_inches='tight')
plt.close()

print(f"\n✓ All visualizations saved to {PLOTS_PATH}")
print(f"  - pattern_distribution.png")
print(f"  - year_trends.png")
print(f"  - conference_comparison.png")
print(f"  - cooccurrence_heatmap.png")
print(f"  - category_breakdown.png")
print(f"  - oral_vs_spotlight.png")
print(f"  - top_pattern_pairs.png")
print(f"  - summary_infographic.png")
