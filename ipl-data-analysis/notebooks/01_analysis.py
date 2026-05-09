# notebooks/01_analysis.py
"""
IPL Data Analysis — Main Script
=================================
Yeh script poora pipeline run karti hai:
  1. Data load
  2. Data clean
  3. Charts generate
  4. Key insights print

Run karo:
    python notebooks/01_analysis.py
"""

import sys
from pathlib import Path

# Project root ko path mein add karo
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.data_loader  import load_matches_data
from src.data_cleaner import clean_matches_data, save_clean_data
from src.visualizer   import run_all


# ────────────────────────────────────────────────────────────────
# STEP 1 — Load
# ────────────────────────────────────────────────────────────────
print("=" * 55)
print("  IPL DATA ANALYSIS — 2008 to 2024")
print("=" * 55)

print("\n[1/4] Loading raw data...")
df_raw = load_matches_data()
print(f"      Rows loaded: {len(df_raw)}")
print(f"      Columns    : {len(df_raw.columns)}")


# ────────────────────────────────────────────────────────────────
# STEP 2 — Clean
# ────────────────────────────────────────────────────────────────
print("\n[2/4] Cleaning data...")
df = clean_matches_data(df_raw)
save_clean_data(df)
print(f"      Clean rows : {len(df)}")
print(f"      New columns: year, month, toss_match_winner, win_type")


# ────────────────────────────────────────────────────────────────
# STEP 3 — Visualizations
# ────────────────────────────────────────────────────────────────
print("\n[3/4] Generating charts...")
run_all(df)


# ────────────────────────────────────────────────────────────────
# STEP 4 — Key Insights
# ────────────────────────────────────────────────────────────────
print("\n[4/4] KEY INSIGHTS")
print("=" * 55)

# Most wins
df_wins = df[df["winner"] != "No Result"]
most_wins = df_wins["winner"].value_counts()
top_team  = most_wins.index[0]
top_wins  = most_wins.iloc[0]
print(f"  🏆 Most wins      : {top_team} ({top_wins} wins)")

# Toss impact
toss_pct = df_wins["toss_match_winner"].mean() * 100
print(f"  🎲 Toss advantage : {toss_pct:.1f}% matches won by toss winner")

# Toss decision
field_pct = (df["toss_decision"] == "field").mean() * 100
print(f"  🏏 Field chosen   : {field_pct:.1f}% times after winning toss")

# Top venue
top_venue = df["venue"].value_counts().index[0]
top_venue_count = df["venue"].value_counts().iloc[0]
print(f"  🏟️  Top venue      : {top_venue} ({top_venue_count} matches)")

# Most matches season
top_season = df.groupby("year")["id"].count().idxmax()
top_season_count = df.groupby("year")["id"].count().max()
print(f"  📅 Busiest season : {top_season} ({top_season_count} matches)")

# No result matches
no_result = len(df[df["winner"] == "No Result"])
print(f"  🌧️  No result      : {no_result} matches (rain/abandoned)")

print("=" * 55)
print("\n✅ Project complete! Charts dekho: reports/figures/\n")