import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# Set global matplotlib parameters for clean, professional executive styling
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
LIGHT_BG = '#F8F9FA'
GRAY_TEXT = '#333333'

df = pd.read_csv(r'DATASET/survey_data.csv', low_memory=False)

def get_top_items(col, n=10):
    valid = df[col].dropna()
    total = len(valid)
    counts = valid.str.split(';').explode().str.strip().value_counts().head(n)
    pcts = (counts / total) * 100
    return counts, pcts, total

# 1. Chart 1: Top 10 Programming Languages - Current Usage
counts_lc, pcts_lc, n_lc = get_top_items('LanguageHaveWorkedWith', 10)
fig, ax = plt.subplots(figsize=(6.2, 4.8))
y_pos = range(len(counts_lc)-1, -1, -1)
names = counts_lc.index.tolist()
values = counts_lc.values
pct_vals = pcts_lc.values

bars = ax.barh(y_pos, values, color=NAVY, height=0.65, edgecolor='none')
bars[0].set_color(CYAN) # Highlight leader

ax.set_yticks(y_pos)
ax.set_yticklabels(names, fontsize=10, fontweight='medium', color=GRAY_TEXT)
ax.set_xlabel('Number of Respondents', fontsize=9, color=GRAY_TEXT, labelpad=8)
ax.set_title('Top 10 Languages: Current Usage (2024)', fontsize=12, fontweight='bold', pad=12, color=NAVY)
ax.set_xlim(0, max(values) * 1.25)
ax.xaxis.set_major_formatter(mtick.StrMethodFormatter('{x:,.0f}'))

for bar, val, pct in zip(bars, values, pct_vals):
    ax.text(val + max(values)*0.02, bar.get_y() + bar.get_height()/2, 
            f'{val:,} ({pct:.1f}%)', va='center', ha='left', fontsize=8.5, color=GRAY_TEXT, fontweight='semibold')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#CCCCCC')
ax.spines['bottom'].set_color('#CCCCCC')
ax.grid(axis='x', linestyle='--', alpha=0.3, color='#999999')
plt.tight_layout()
plt.savefig('output/charts/lang_curr.png')
plt.close()

# 2. Chart 2: Top 10 Programming Languages - Future Interest
counts_lw, pcts_lw, n_lw = get_top_items('LanguageWantToWorkWith', 10)
fig, ax = plt.subplots(figsize=(6.2, 4.8))
y_pos = range(len(counts_lw)-1, -1, -1)
names = counts_lw.index.tolist()
values = counts_lw.values
pct_vals = pcts_lw.values

bars = ax.barh(y_pos, values, color=SLATE, height=0.65, edgecolor='none')
bars[0].set_color(TEAL) # Highlight leader

ax.set_yticks(y_pos)
ax.set_yticklabels(names, fontsize=10, fontweight='medium', color=GRAY_TEXT)
ax.set_xlabel('Number of Respondents', fontsize=9, color=GRAY_TEXT, labelpad=8)
ax.set_title('Top 10 Languages: Future Interest (Next Year)', fontsize=12, fontweight='bold', pad=12, color=NAVY)
ax.set_xlim(0, max(values) * 1.25)
ax.xaxis.set_major_formatter(mtick.StrMethodFormatter('{x:,.0f}'))

for bar, val, pct in zip(bars, values, pct_vals):
    ax.text(val + max(values)*0.02, bar.get_y() + bar.get_height()/2, 
            f'{val:,} ({pct:.1f}%)', va='center', ha='left', fontsize=8.5, color=GRAY_TEXT, fontweight='semibold')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#CCCCCC')
ax.spines['bottom'].set_color('#CCCCCC')
ax.grid(axis='x', linestyle='--', alpha=0.3, color='#999999')
plt.tight_layout()
plt.savefig('output/charts/lang_want.png')
plt.close()

# 3. Chart 3: Top 10 Databases - Current Usage
counts_dc, pcts_dc, n_dc = get_top_items('DatabaseHaveWorkedWith', 10)
fig, ax = plt.subplots(figsize=(6.2, 4.8))
y_pos = range(len(counts_dc)-1, -1, -1)
names = counts_dc.index.tolist()
values = counts_dc.values
pct_vals = pcts_dc.values

bars = ax.barh(y_pos, values, color=NAVY, height=0.65, edgecolor='none')
bars[0].set_color(CYAN)

ax.set_yticks(y_pos)
ax.set_yticklabels(names, fontsize=10, fontweight='medium', color=GRAY_TEXT)
ax.set_xlabel('Number of Respondents', fontsize=9, color=GRAY_TEXT, labelpad=8)
ax.set_title('Top 10 Databases: Current Usage (2024)', fontsize=12, fontweight='bold', pad=12, color=NAVY)
ax.set_xlim(0, max(values) * 1.25)
ax.xaxis.set_major_formatter(mtick.StrMethodFormatter('{x:,.0f}'))

for bar, val, pct in zip(bars, values, pct_vals):
    ax.text(val + max(values)*0.02, bar.get_y() + bar.get_height()/2, 
            f'{val:,} ({pct:.1f}%)', va='center', ha='left', fontsize=8.5, color=GRAY_TEXT, fontweight='semibold')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#CCCCCC')
ax.spines['bottom'].set_color('#CCCCCC')
ax.grid(axis='x', linestyle='--', alpha=0.3, color='#999999')
plt.tight_layout()
plt.savefig('output/charts/db_curr.png')
plt.close()

# 4. Chart 4: Top 10 Databases - Future Interest
counts_dw, pcts_dw, n_dw = get_top_items('DatabaseWantToWorkWith', 10)
fig, ax = plt.subplots(figsize=(6.2, 4.8))
y_pos = range(len(counts_dw)-1, -1, -1)
names = counts_dw.index.tolist()
values = counts_dw.values
pct_vals = pcts_dw.values

bars = ax.barh(y_pos, values, color=SLATE, height=0.65, edgecolor='none')
bars[0].set_color(TEAL)

ax.set_yticks(y_pos)
ax.set_yticklabels(names, fontsize=10, fontweight='medium', color=GRAY_TEXT)
ax.set_xlabel('Number of Respondents', fontsize=9, color=GRAY_TEXT, labelpad=8)
ax.set_title('Top 10 Databases: Future Interest (Next Year)', fontsize=12, fontweight='bold', pad=12, color=NAVY)
ax.set_xlim(0, max(values) * 1.25)
ax.xaxis.set_major_formatter(mtick.StrMethodFormatter('{x:,.0f}'))

for bar, val, pct in zip(bars, values, pct_vals):
    ax.text(val + max(values)*0.02, bar.get_y() + bar.get_height()/2, 
            f'{val:,} ({pct:.1f}%)', va='center', ha='left', fontsize=8.5, color=GRAY_TEXT, fontweight='semibold')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#CCCCCC')
ax.spines['bottom'].set_color('#CCCCCC')
ax.grid(axis='x', linestyle='--', alpha=0.3, color='#999999')
plt.tight_layout()
plt.savefig('output/charts/db_want.png')
plt.close()

# 5. Dashboard Tab 1 Visual: Current Technology Usage (Languages, Databases, Webframes, Cloud Platforms)
fig, axs = plt.subplots(2, 2, figsize=(11.5, 6.2))
fig.patch.set_facecolor('#FFFFFF')

def plot_sub_barh(ax, col, title, color_bar, top_n=6):
    counts, pcts, total = get_top_items(col, top_n)
    y_pos = range(len(counts)-1, -1, -1)
    ax.barh(y_pos, counts.values, color=color_bar, height=0.6)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(counts.index, fontsize=9)
    ax.set_title(title, fontsize=10.5, fontweight='bold', color=NAVY, pad=6)
    ax.set_xlim(0, max(counts.values) * 1.35)
    for i, (val, pct) in enumerate(zip(counts.values, pcts.values)):
        ax.text(val + max(counts.values)*0.02, top_n - 1 - i, f'{pct:.1f}%', va='center', fontsize=8.5, fontweight='semibold')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='x', linestyle='--', alpha=0.25)
    ax.tick_params(axis='x', labelsize=8)

plot_sub_barh(axs[0, 0], 'LanguageHaveWorkedWith', 'Top Programming Languages (Current)', NAVY)
plot_sub_barh(axs[0, 1], 'DatabaseHaveWorkedWith', 'Top Databases (Current)', CYAN)
plot_sub_barh(axs[1, 0], 'WebframeHaveWorkedWith', 'Top Web Frameworks (Current)', SLATE)
plot_sub_barh(axs[1, 1], 'PlatformHaveWorkedWith', 'Top Cloud Platforms (Current)', TEAL)

plt.suptitle('DASHBOARD TAB 1: CURRENT TECHNOLOGY USAGE OVERVIEW', fontsize=13, fontweight='bold', color=NAVY, y=0.98)
plt.tight_layout(rect=[0, 0.02, 1, 0.95])
plt.savefig('output/charts/dashboard_tab1.png')
plt.close()

# 6. Dashboard Tab 2 Visual: Future Technology Trends (Language Want, Database Want, Framework Want, Platform Want)
fig, axs = plt.subplots(2, 2, figsize=(11.5, 6.2))
fig.patch.set_facecolor('#FFFFFF')

plot_sub_barh(axs[0, 0], 'LanguageWantToWorkWith', 'Top Languages in Demand (Next Year)', '#3D5A80')
plot_sub_barh(axs[0, 1], 'DatabaseWantToWorkWith', 'Top Databases in Demand (Next Year)', '#293241')
plot_sub_barh(axs[1, 0], 'WebframeWantToWorkWith', 'Top Web Frameworks in Demand (Next Year)', '#EE6C4D')
plot_sub_barh(axs[1, 1], 'PlatformWantToWorkWith', 'Top Cloud Platforms in Demand (Next Year)', '#98C1D9')

plt.suptitle('DASHBOARD TAB 2: FUTURE TECHNOLOGY TRENDS & ADOPTION MOMENTUM', fontsize=13, fontweight='bold', color=NAVY, y=0.98)
plt.tight_layout(rect=[0, 0.02, 1, 0.95])
plt.savefig('output/charts/dashboard_tab2.png')
plt.close()

# 7. Dashboard Tab 3 Visual: Demographics (Age, Education, Remote Work, Dev Roles)
fig, axs = plt.subplots(2, 2, figsize=(11.5, 6.2))
fig.patch.set_facecolor('#FFFFFF')

# Age Distribution
age_counts = df['Age'].dropna().value_counts()
axs[0, 0].bar(range(len(age_counts)), age_counts.values, color=NAVY, width=0.6)
axs[0, 0].set_xticks(range(len(age_counts)))
axs[0, 0].set_xticklabels([x.replace(' years old', '').replace(' years or older', '+') for x in age_counts.index], rotation=30, ha='right', fontsize=8)
axs[0, 0].set_title('Age Distribution of Respondents', fontsize=10.5, fontweight='bold', color=NAVY, pad=6)
axs[0, 0].spines['top'].set_visible(False)
axs[0, 0].spines['right'].set_visible(False)
axs[0, 0].grid(axis='y', linestyle='--', alpha=0.25)
axs[0, 0].tick_params(labelsize=8)

# Remote Work Distribution (Donut Chart)
rw_counts = df['RemoteWork'].dropna().value_counts()
wedges, texts, autotexts = axs[0, 1].pie(rw_counts.values, labels=rw_counts.index, autopct='%1.1f%%',
                                         startangle=140, colors=[NAVY, CYAN, TEAL],
                                         wedgeprops=dict(width=0.45, edgecolor='w', linewidth=2),
                                         textprops=dict(fontsize=8))
plt.setp(autotexts, size=8.5, weight="bold", color="white")
axs[0, 1].set_title('Work Arrangement (Remote vs Hybrid vs In-Person)', fontsize=10.5, fontweight='bold', color=NAVY, pad=6)

# Education Level (Top 5)
ed_counts = df['EdLevel'].dropna().value_counts().head(5)
y_ed = range(len(ed_counts)-1, -1, -1)
short_ed = ['Bachelor’s', 'Master’s', 'Some College', 'Secondary School', 'Professional (PhD/JD)']
axs[1, 0].barh(y_ed, ed_counts.values, color=SLATE, height=0.6)
axs[1, 0].set_yticks(y_ed)
axs[1, 0].set_yticklabels(short_ed, fontsize=8.5)
axs[1, 0].set_title('Top Educational Attainment Levels', fontsize=10.5, fontweight='bold', color=NAVY, pad=6)
axs[1, 0].spines['top'].set_visible(False)
axs[1, 0].spines['right'].set_visible(False)
axs[1, 0].grid(axis='x', linestyle='--', alpha=0.25)
for i, v in enumerate(ed_counts.values):
    axs[1, 0].text(v + 500, len(ed_counts)-1-i, f'{v/len(df)*100:.1f}%', va='center', fontsize=8)

# Developer Roles (Top 6)
dev_counts = df['DevType'].dropna().value_counts().head(6)
y_dev = range(len(dev_counts)-1, -1, -1)
short_dev = [x.replace('Developer, ', '').replace('applications or devices', 'apps') for x in dev_counts.index]
axs[1, 1].barh(y_dev, dev_counts.values, color=CORAL, height=0.6)
axs[1, 1].set_yticks(y_dev)
axs[1, 1].set_yticklabels(short_dev, fontsize=8.5)
axs[1, 1].set_title('Top Primary Developer Specializations', fontsize=10.5, fontweight='bold', color=NAVY, pad=6)
axs[1, 1].spines['top'].set_visible(False)
axs[1, 1].spines['right'].set_visible(False)
axs[1, 1].grid(axis='x', linestyle='--', alpha=0.25)
for i, v in enumerate(dev_counts.values):
    axs[1, 1].text(v + 300, len(dev_counts)-1-i, f'{v/len(df)*100:.1f}%', va='center', fontsize=8)

plt.suptitle('DASHBOARD TAB 3: GLOBAL DEVELOPER DEMOGRAPHICS', fontsize=13, fontweight='bold', color=NAVY, y=0.98)
plt.tight_layout(rect=[0, 0.02, 1, 0.95])
plt.savefig('output/charts/dashboard_tab3.png')
plt.close()

# 8. Appendix Chart: Compensation by Developer Role (Median Annual USD)
comp_dev = df.groupby('DevType')['ConvertedCompYearly'].agg(['median', 'count']).sort_values('median', ascending=False)
top_comp = comp_dev[comp_dev['count'] >= 100].head(10)

fig, ax = plt.subplots(figsize=(7.5, 4.8))
y_pos = range(len(top_comp)-1, -1, -1)
names = [x.replace('Developer, ', '').replace('Senior Executive (C-Suite, VP, etc.)', 'Executive (C-Suite/VP)') for x in top_comp.index]
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

print('All charts successfully generated in output/charts!')
