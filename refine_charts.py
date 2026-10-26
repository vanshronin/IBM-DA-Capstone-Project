import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

plt.rcParams['font.sans-serif'] = 'Segoe UI'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300

NAVY = '#0F3460'
CYAN = '#00ADB5'
TEAL = '#16C79A'
SLATE = '#1F4068'
CORAL = '#E94560'
AMBER = '#FFA41B'
GRAY_TEXT = '#333333'

df = pd.read_csv(r'DATASET/survey_data.csv', low_memory=False)

def get_top_items(col, n=10):
    valid = df[col].dropna()
    total = len(valid)
    counts = valid.str.split(';').explode().str.strip().value_counts().head(n)
    pcts = (counts / total) * 100
    return counts, pcts, total

# Dashboard Tab 3: Demographics
fig, axs = plt.subplots(2, 2, figsize=(11.5, 6.2))
fig.patch.set_facecolor('#FFFFFF')

# 1. Age Distribution
age_counts = df['Age'].dropna().value_counts()
axs[0, 0].bar(range(len(age_counts)), age_counts.values, color=NAVY, width=0.6)
axs[0, 0].set_xticks(range(len(age_counts)))
short_age = [x.replace(' years old', '').replace(' years or older', '+') for x in age_counts.index]
axs[0, 0].set_xticklabels(short_age, rotation=25, ha='right', fontsize=8.5)
axs[0, 0].set_title('Age Distribution of Survey Respondents', fontsize=10.5, fontweight='bold', color=NAVY, pad=8)
axs[0, 0].spines['top'].set_visible(False)
axs[0, 0].spines['right'].set_visible(False)
axs[0, 0].grid(axis='y', linestyle='--', alpha=0.25)
axs[0, 0].tick_params(labelsize=8)

# 2. Remote Work Distribution - Horizontal Bar Chart (Clean & legible)
rw_counts = df['RemoteWork'].dropna().value_counts()
y_rw = range(len(rw_counts)-1, -1, -1)
rw_labels = ['Hybrid', 'Fully Remote', 'In-Person']
rw_colors = [NAVY, CYAN, TEAL]
bars_rw = axs[0, 1].barh(y_rw, rw_counts.values, color=rw_colors, height=0.55)
axs[0, 1].set_yticks(y_rw)
axs[0, 1].set_yticklabels(rw_labels, fontsize=9, fontweight='medium')
axs[0, 1].set_title('Work Arrangement Models', fontsize=10.5, fontweight='bold', color=NAVY, pad=8)
axs[0, 1].set_xlim(0, max(rw_counts.values) * 1.3)
axs[0, 1].spines['top'].set_visible(False)
axs[0, 1].spines['right'].set_visible(False)
axs[0, 1].grid(axis='x', linestyle='--', alpha=0.25)
total_rw = rw_counts.sum()
for bar, val in zip(bars_rw, rw_counts.values):
    axs[0, 1].text(val + max(rw_counts.values)*0.02, bar.get_y() + bar.get_height()/2,
                   f'{val:,} ({val/total_rw*100:.1f}%)', va='center', fontsize=8.5, fontweight='semibold', color=GRAY_TEXT)

# 3. Education Level (Top 5)
ed_counts = df['EdLevel'].dropna().value_counts().head(5)
y_ed = range(len(ed_counts)-1, -1, -1)
short_ed = ['Bachelor’s degree', 'Master’s degree', 'Some college / university', 'Secondary school', 'Professional (PhD/JD)']
bars_ed = axs[1, 0].barh(y_ed, ed_counts.values, color=SLATE, height=0.55)
axs[1, 0].set_yticks(y_ed)
axs[1, 0].set_yticklabels(short_ed, fontsize=8.5)
axs[1, 0].set_title('Top Educational Attainment Levels', fontsize=10.5, fontweight='bold', color=NAVY, pad=8)
axs[1, 0].set_xlim(0, max(ed_counts.values) * 1.3)
axs[1, 0].spines['top'].set_visible(False)
axs[1, 0].spines['right'].set_visible(False)
axs[1, 0].grid(axis='x', linestyle='--', alpha=0.25)
for bar, v in zip(bars_ed, ed_counts.values):
    axs[1, 0].text(v + max(ed_counts.values)*0.02, bar.get_y() + bar.get_height()/2,
                   f'{v:,} ({v/len(df)*100:.1f}%)', va='center', fontsize=8.5, fontweight='semibold', color=GRAY_TEXT)

# 4. Developer Roles (Top 6)
dev_counts = df['DevType'].dropna().value_counts().head(6)
y_dev = range(len(dev_counts)-1, -1, -1)
short_dev = [x.replace('Developer, ', '').replace('applications or devices', 'apps') for x in dev_counts.index]
bars_dev = axs[1, 1].barh(y_dev, dev_counts.values, color=CORAL, height=0.55)
axs[1, 1].set_yticks(y_dev)
axs[1, 1].set_yticklabels(short_dev, fontsize=8.5)
axs[1, 1].set_title('Top Primary Developer Specializations', fontsize=10.5, fontweight='bold', color=NAVY, pad=8)
axs[1, 1].set_xlim(0, max(dev_counts.values) * 1.3)
axs[1, 1].spines['top'].set_visible(False)
axs[1, 1].spines['right'].set_visible(False)
axs[1, 1].grid(axis='x', linestyle='--', alpha=0.25)
for bar, v in zip(bars_dev, dev_counts.values):
    axs[1, 1].text(v + max(dev_counts.values)*0.02, bar.get_y() + bar.get_height()/2,
                   f'{v:,} ({v/len(df)*100:.1f}%)', va='center', fontsize=8.5, fontweight='semibold', color=GRAY_TEXT)

plt.suptitle('DASHBOARD TAB 3: GLOBAL DEVELOPER DEMOGRAPHICS', fontsize=13, fontweight='bold', color=NAVY, y=0.98)
plt.tight_layout(rect=[0, 0.02, 1, 0.95])
plt.savefig('output/charts/dashboard_tab3.png')
plt.close()

# Appendix Chart: fix executive role label
comp_dev = df.groupby('DevType')['ConvertedCompYearly'].agg(['median', 'count']).sort_values('median', ascending=False)
top_comp = comp_dev[comp_dev['count'] >= 100].head(10)

fig, ax = plt.subplots(figsize=(7.5, 4.8))
y_pos = range(len(top_comp)-1, -1, -1)
names = [
    'Executive (C-Suite/VP)' if 'Executive' in x else
    'AI Developer' if x == 'Developer, AI' else
    x.replace('Developer, ', '')
    for x in top_comp.index
]
values = top_comp['median'].values

bars = ax.barh(y_pos, values, color=NAVY, height=0.65)
bars[0].set_color(AMBER)
bars[1].set_color(CYAN)

ax.set_yticks(y_pos)
ax.set_yticklabels(names, fontsize=9.5, fontweight='medium', color=GRAY_TEXT)
ax.set_xlabel('Median Annual Compensation (USD)', fontsize=9, color=GRAY_TEXT, labelpad=8)
ax.set_title('Top Compensated Tech Specializations (Median USD, N ≥ 100)', fontsize=11.5, fontweight='bold', pad=12, color=NAVY)
ax.set_xlim(0, max(values) * 1.25)
ax.xaxis.set_major_formatter(mtick.StrMethodFormatter('${x:,.0f}'))

for bar, val in zip(bars, values):
    ax.text(val + max(values)*0.02, bar.get_y() + bar.get_height()/2, 
            f'${val:,.0f}', va='center', ha='left', fontsize=8.5, color=GRAY_TEXT, fontweight='semibold')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='x', linestyle='--', alpha=0.3)
plt.tight_layout()
plt.savefig('output/charts/comp_by_role.png')
plt.close()

print('Updated dashboard_tab3 and comp_by_role charts!')
