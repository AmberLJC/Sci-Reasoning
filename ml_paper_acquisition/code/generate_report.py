"""
Generate final statistics report and visualizations
"""

import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Load statistics
with open('results/data/statistics_fast.json', 'r') as f:
    stats = json.load(f)

# Create output directory for plots
Path('results/plots').mkdir(parents=True, exist_ok=True)

# Define colors
colors = {
    'oral': '#e74c3c',      # Red
    'spotlight': '#f39c12',  # Orange
    'poster': '#3498db'      # Blue
}

conference_colors = {
    'ICLR': '#2ecc71',       # Green
    'NeurIPS': '#9b59b6',    # Purple
    'ICML': '#e67e22'        # Orange
}

# Prepare data
conferences = ['ICLR_2023', 'ICLR_2024', 'ICML_2023', 'ICML_2024', 'NeurIPS_2023', 'NeurIPS_2024']
conf_data = stats['by_conference_and_type']

# Figure 1: Stacked bar chart by conference
fig, ax = plt.subplots(figsize=(14, 8))

x = np.arange(len(conferences))
width = 0.6

oral_counts = [conf_data.get(c, {}).get('oral', 0) for c in conferences]
spotlight_counts = [conf_data.get(c, {}).get('spotlight', 0) for c in conferences]
poster_counts = [conf_data.get(c, {}).get('poster', 0) for c in conferences]

bars1 = ax.bar(x, oral_counts, width, label='Oral', color=colors['oral'])
bars2 = ax.bar(x, spotlight_counts, width, bottom=oral_counts, label='Spotlight', color=colors['spotlight'])
bars3 = ax.bar(x, poster_counts, width, bottom=[o+s for o,s in zip(oral_counts, spotlight_counts)], label='Poster', color=colors['poster'], alpha=0.7)

ax.set_xlabel('Conference', fontsize=12)
ax.set_ylabel('Number of Papers', fontsize=12)
ax.set_title('Paper Distribution by Conference and Presentation Type\n(ICML, ICLR, NeurIPS 2023-2024)', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels([c.replace('_', ' ') for c in conferences], rotation=45, ha='right')
ax.legend(loc='upper left')

# Add total counts on top
for i, (o, s, p) in enumerate(zip(oral_counts, spotlight_counts, poster_counts)):
    total = o + s + p
    ax.annotate(f'{total}', xy=(i, total), ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('results/plots/papers_by_conference_stacked.png', dpi=150, bbox_inches='tight')
plt.close()

# Figure 2: Oral + Spotlight only (focus on high-impact papers)
fig, ax = plt.subplots(figsize=(12, 7))

x = np.arange(len(conferences))
width = 0.35

bars1 = ax.bar(x - width/2, oral_counts, width, label='Oral', color=colors['oral'])
bars2 = ax.bar(x + width/2, spotlight_counts, width, label='Spotlight', color=colors['spotlight'])

ax.set_xlabel('Conference', fontsize=12)
ax.set_ylabel('Number of Papers', fontsize=12)
ax.set_title('Oral and Spotlight Papers by Conference\n(High-Impact Papers Only)', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels([c.replace('_', ' ') for c in conferences], rotation=45, ha='right')
ax.legend()

# Add value labels
for bar in bars1:
    height = bar.get_height()
    if height > 0:
        ax.annotate(f'{int(height)}', xy=(bar.get_x() + bar.get_width()/2, height),
                   ha='center', va='bottom', fontsize=9)
for bar in bars2:
    height = bar.get_height()
    if height > 0:
        ax.annotate(f'{int(height)}', xy=(bar.get_x() + bar.get_width()/2, height),
                   ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig('results/plots/oral_spotlight_by_conference.png', dpi=150, bbox_inches='tight')
plt.close()

# Figure 3: Pie chart of overall distribution
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# All papers
total_by_type = stats['by_type']
sizes = [total_by_type['oral'], total_by_type['spotlight'], total_by_type['poster']]
labels = ['Oral', 'Spotlight', 'Poster']
explode = (0.05, 0.05, 0)

ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        colors=[colors['oral'], colors['spotlight'], colors['poster']],
        shadow=True, startangle=90)
ax1.set_title('Distribution of All Papers\nby Presentation Type', fontsize=12, fontweight='bold')

# Oral + Spotlight only
sizes_os = [total_by_type['oral'], total_by_type['spotlight']]
labels_os = ['Oral', 'Spotlight']
ax2.pie(sizes_os, labels=labels_os, autopct='%1.1f%%',
        colors=[colors['oral'], colors['spotlight']],
        shadow=True, startangle=90)
ax2.set_title('Distribution of High-Impact Papers\n(Oral + Spotlight Only)', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('results/plots/paper_distribution_pie.png', dpi=150, bbox_inches='tight')
plt.close()

# Figure 4: Year-over-year comparison
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

for idx, conf in enumerate(['ICLR', 'ICML', 'NeurIPS']):
    ax = axes[idx]
    
    conf_2023 = f'{conf}_2023'
    conf_2024 = f'{conf}_2024'
    
    data_2023 = conf_data.get(conf_2023, {})
    data_2024 = conf_data.get(conf_2024, {})
    
    categories = ['Oral', 'Spotlight', 'Poster']
    vals_2023 = [data_2023.get('oral', 0), data_2023.get('spotlight', 0), data_2023.get('poster', 0)]
    vals_2024 = [data_2024.get('oral', 0), data_2024.get('spotlight', 0), data_2024.get('poster', 0)]
    
    x = np.arange(len(categories))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, vals_2023, width, label='2023', color=conference_colors[conf], alpha=0.6)
    bars2 = ax.bar(x + width/2, vals_2024, width, label='2024', color=conference_colors[conf])
    
    ax.set_ylabel('Number of Papers')
    ax.set_title(f'{conf}', fontsize=12, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.legend()
    
    # Add value labels
    for bar in bars1:
        height = bar.get_height()
        if height > 0:
            ax.annotate(f'{int(height)}', xy=(bar.get_x() + bar.get_width()/2, height),
                       ha='center', va='bottom', fontsize=8)
    for bar in bars2:
        height = bar.get_height()
        if height > 0:
            ax.annotate(f'{int(height)}', xy=(bar.get_x() + bar.get_width()/2, height),
                       ha='center', va='bottom', fontsize=8)

plt.suptitle('Year-over-Year Comparison (2023 vs 2024)', fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('results/plots/year_over_year_comparison.png', dpi=150, bbox_inches='tight')
plt.close()

# Figure 5: Summary statistics table as image
fig, ax = plt.subplots(figsize=(12, 8))
ax.axis('off')

# Create table data
table_data = []
headers = ['Conference', 'Year', 'Oral', 'Spotlight', 'Poster', 'Total', 'Oral+Spotlight %']

for conf in conferences:
    data = conf_data.get(conf, {})
    oral = data.get('oral', 0)
    spotlight = data.get('spotlight', 0)
    poster = data.get('poster', 0)
    total = oral + spotlight + poster
    os_pct = ((oral + spotlight) / total * 100) if total > 0 else 0
    
    conf_name, year = conf.split('_')
    table_data.append([conf_name, year, oral, spotlight, poster, total, f'{os_pct:.1f}%'])

# Add totals row
total_oral = sum(conf_data.get(c, {}).get('oral', 0) for c in conferences)
total_spotlight = sum(conf_data.get(c, {}).get('spotlight', 0) for c in conferences)
total_poster = sum(conf_data.get(c, {}).get('poster', 0) for c in conferences)
grand_total = total_oral + total_spotlight + total_poster
total_os_pct = (total_oral + total_spotlight) / grand_total * 100

table_data.append(['TOTAL', '2023-24', total_oral, total_spotlight, total_poster, grand_total, f'{total_os_pct:.1f}%'])

table = ax.table(cellText=table_data, colLabels=headers, loc='center', cellLoc='center')
table.auto_set_font_size(False)
table.set_fontsize(11)
table.scale(1.2, 1.8)

# Style the table
for i in range(len(headers)):
    table[(0, i)].set_facecolor('#34495e')
    table[(0, i)].set_text_props(color='white', fontweight='bold')

# Highlight totals row
for i in range(len(headers)):
    table[(len(table_data), i)].set_facecolor('#ecf0f1')
    table[(len(table_data), i)].set_text_props(fontweight='bold')

plt.title('ML Conference Paper Statistics Summary\n(ICML, ICLR, NeurIPS 2023-2024)', fontsize=14, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('results/plots/statistics_table.png', dpi=150, bbox_inches='tight')
plt.close()

print("✅ All visualizations generated successfully!")
print(f"   - papers_by_conference_stacked.png")
print(f"   - oral_spotlight_by_conference.png")
print(f"   - paper_distribution_pie.png")
print(f"   - year_over_year_comparison.png")
print(f"   - statistics_table.png")
