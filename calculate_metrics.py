import pandas as pd

df = pd.read_csv(r'DATASET/survey_data.csv', low_memory=False)

def top_multiselect(col, n=10):
    valid = df[col].dropna()
    total_valid = len(valid)
    counts = valid.str.split(';').explode().str.strip().value_counts()
    pct = (counts / total_valid) * 100
    res = pd.DataFrame({'Count': counts, 'Pct': pct})
    return res.head(n), total_valid

cols = [
    'LanguageHaveWorkedWith', 'LanguageWantToWorkWith', 
    'DatabaseHaveWorkedWith', 'DatabaseWantToWorkWith',
    'PlatformHaveWorkedWith', 'PlatformWantToWorkWith',
    'WebframeHaveWorkedWith', 'WebframeWantToWorkWith'
]

for col in cols:
    res, total = top_multiselect(col, 10)
    print(f"=== {col} (Valid Respondents: {total:,} / {len(df):,}) ===")
    for rank, (name, row) in enumerate(res.iterrows(), 1):
        c = int(row['Count'])
        p = float(row['Pct'])
        print(f"  {rank:2d}. {name:<30} | {c:>7,d} ({p:>5.1f}%)")
    print()

print("=== DEMOGRAPHICS SUMMARY ===")
print("--- Age ---")
age_counts = df['Age'].value_counts(dropna=False)
for k, v in age_counts.items():
    print(f"  {str(k):<30} : {v:>7,d} ({v/len(df)*100:>5.1f}%)")

print("\n--- Education Level ---")
ed_counts = df['EdLevel'].value_counts(dropna=False).head(7)
for k, v in ed_counts.items():
    print(f"  {str(k):<50} : {v:>7,d} ({v/len(df)*100:>5.1f}%)")

print("\n--- Remote Work ---")
rw_counts = df['RemoteWork'].value_counts(dropna=False)
for k, v in rw_counts.items():
    print(f"  {str(k):<35} : {v:>7,d} ({v/len(df)*100:>5.1f}%)")

print("\n--- Country Top 10 ---")
c_counts = df['Country'].value_counts(dropna=False).head(10)
for k, v in c_counts.items():
    print(f"  {str(k):<45} : {v:>7,d} ({v/len(df)*100:>5.1f}%)")

print("\n--- Developer Roles Top 10 ---")
dev_counts = df['DevType'].value_counts(dropna=False).head(10)
for k, v in dev_counts.items():
    print(f"  {str(k):<45} : {v:>7,d} ({v/len(df)*100:>5.1f}%)")
