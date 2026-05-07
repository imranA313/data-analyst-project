"""
India Population Analysis — Main Script
========================================
Project root se run karo:
    python notebooks/01_analysis.py

Steps covered:
  1. Raw data load + quick summary
  2. Clean + feature engineering + save
  3. All 5 charts generate
  4. Key insights print
"""

import sys
from pathlib import Path

# Project root ko Python path mein add karo
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.data_loader  import load_raw, quick_summary
from src.data_cleaner import clean, save_clean
from src.visualizer   import run_all

# ────────────────────────────────────────────────────────────────
# STEP 1 — Load
# ────────────────────────────────────────────────────────────────
print("\n[1/4] Loading raw data...")
df_raw = load_raw()
quick_summary(df_raw)

# ────────────────────────────────────────────────────────────────
# STEP 2 — Clean + Feature Engineering
# ────────────────────────────────────────────────────────────────
print("\n[2/4] Cleaning & feature engineering...")
df = clean(df_raw)
save_clean(df)

print("\nNew columns added (top 10):")
print(
    df[["state", "pop_crore", "pop_density", "pop_share_pct"]]
    .head(10)
    .to_string()
)

# ────────────────────────────────────────────────────────────────
# STEP 3 — Visualizations
# ────────────────────────────────────────────────────────────────
print("\n[3/4] Generating all 5 charts...")
run_all(df)

# ────────────────────────────────────────────────────────────────
# STEP 4 — Key Insights
# ────────────────────────────────────────────────────────────────
print("\n[4/4] KEY INSIGHTS")
print("=" * 55)

most_pop   = df.iloc[0]
least_pop  = df[df["type"] == "State"].iloc[-1]
densest    = df.nlargest(1, "pop_density").iloc[0]
top5_share = df.head(5)["pop_share_pct"].sum()
best_lit   = df.nlargest(1, "literacy_rate").iloc[0]
worst_lit  = df.nsmallest(1, "literacy_rate").iloc[0]

print(f"  Most populated  : {most_pop['state']} ({most_pop['pop_crore']:.1f} Cr)")
print(f"  Least populated : {least_pop['state']} ({least_pop['pop_crore']:.2f} Cr)")
print(f"  Densest state   : {densest['state']} ({densest['pop_density']:.0f}/km²)")
print(f"  Top 5 states    : {top5_share:.1f}% of India's total population")
print(f"  Highest literacy: {best_lit['state']} ({best_lit['literacy_rate']}%)")
print(f"  Lowest literacy : {worst_lit['state']} ({worst_lit['literacy_rate']}%)")
print("=" * 55)
print("\n Project complete! Charts dekho: reports/figures/\n")
