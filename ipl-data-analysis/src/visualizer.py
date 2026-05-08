from src.data_cleaner import clean_matches_data
from src.data_loader import load_matches_data
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
from src.config import FIGURES_DIR, FIGURE_DPI, FIGURE_SIZE

# ---------- Global Styles --------------------------------------------------------
plt.rcParams.update({
    "font.family":       "DejaVu Sans",
    "axes.spines.top":   False,
    "axes.spines.right": False,
    "axes.grid":         True,
    "grid.alpha":        0.3,
    "figure.dpi":        FIGURE_DPI,
})

# ------------ Team Colors --------------------------------------------------------
TEAM_COLORS = {
    "Mumbai Indians":                "#004BA0",
    "Chennai Super Kings":           "#F9CD05",
    "Royal Challengers Bangalore":   "#EC1C24",
    "Royal Challengers Bengaluru":   "#EC1C24",
    "Kolkata Knight Riders":         "#3A225D",
    "Sunrisers Hyderabad":           "#F7A721",
    "Delhi Capitals":                "#0078BC",
    "Delhi Daredevils":              "#0078BC",
    "Rajasthan Royals":              "#EA1A85",
    "Punjab Kings":                  "#AADAFF",
    "Kings XI Punjab":               "#AADAFF",
    "Deccan Chargers":               "#FFA500",
    "Gujarat Titans":                "#1B2A5C",
    "Gujarat Lions":                 "#E8702A",
    "Lucknow Super Giants":          "#00B4D8",
    "Rising Pune Supergiant":        "#8B008B",
    "Rising Pune Supergiants":       "#8B008B",
    "Pune Warriors":                 "#1C4E9D",
    "Kochi Tuskers Kerala":          "#F4511E",
    "No Result":                     "#BBBBBB",
}


def _save(fig: plt.Figure, name: str) -> None:
    """Save the figure to the specified directory."""
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    path = FIGURES_DIR / f"{name}.png"
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print(f"[✅]Saved figure: -> {path.name}")


# ------------------------- Chart 1: Top 10 Teams by wins ----------------------------
def charts_top_teams_by_wins(df: pd.DataFrame) -> None:
    """Generate a bar chart of the top 10 teams by wins."""
    # No Result hatao
    wins = (
        df[df["winner"] != "No Result"]["winner"]
        .value_counts()
        .head(10)
    )

    colors = [TEAM_COLORS.get(t, "#888888") for t in wins.index]

    fig, ax = plt.subplots(figsize=FIGURE_SIZE)
    bars = ax.barh(
        wins.index[::-1],
        wins.values[::-1],
        color=colors[::-1],
        edgecolor="white",
        linewidth=0.5,
    )

    # Value labels
    for bar, val in zip(bars, wins.values[::-1]):
        ax.text(
            bar.get_width() + 1,
            bar.get_y() + bar.get_height() / 2,
            str(val),
            va="center", fontsize=9, color="#444",
        )

    ax.set_xlabel("Total Wins", fontsize=11)
    ax.set_title("Top 10 Teams by Total Wins — IPL 2008-2024",
                 fontsize=13, pad=14)
    fig.tight_layout()
    _save(fig, "01_top_teams_wins")


# ----- Chart 2: Season wise matches per year ---------------------------------------
def chart_season_trend(df: pd.DataFrame) -> None:
    """Har season mein kitne matches hue?"""

    season_matches = df.groupby("year")["id"].count().reset_index()
    season_matches.columns = ["year", "matches"]

    fig, ax = plt.subplots(figsize=FIGURE_SIZE)

    ax.plot(
        season_matches["year"],
        season_matches["matches"],
        marker="o",
        linewidth=2,
        color="#4C72B0",
        markersize=7,
        markerfacecolor="white",
        markeredgewidth=2,
    )

    # Value labels on points
    for _, row in season_matches.iterrows():
        ax.annotate(
            str(int(row["matches"])),
            (row["year"], row["matches"]),
            textcoords="offset points",
            xytext=(0, 8),
            fontsize=8,
            ha="center",
            color="#444",
        )

    ax.set_xlabel("Year", fontsize=11)
    ax.set_ylabel("Number of Matches", fontsize=11)
    ax.set_title("Season-wise Match Count — IPL 2008-2024",
                 fontsize=13, pad=14)
    ax.set_xticks(season_matches["year"])
    ax.tick_params(axis="x", rotation=45)
    fig.tight_layout()
    _save(fig, "02_season_trend")


# ---- Chart 3: Toss impact — pie chart ------------------------------------------------------
def chart_toss_impact(df: pd.DataFrame) -> None:
    """Toss jeetnewale ne match bhi jeeta?"""

 # No Result hatao
    df_result = df[df["winner"] != "No Result"].copy()

    toss_won = df_result["toss_match_winner"].value_counts()
    labels = ["Toss + Match Jeeta", "Toss Jeeta, Match Nahi"]
    colors = ["#4C72B0", "#BBBBBB"]
    explode = [0.05, 0]

    fig, ax = plt.subplots(figsize=(7, 7))
    wedges, texts, autotexts = ax.pie(
        toss_won.values,
        labels=labels,
        autopct="%1.1f%%",
        colors=colors,
        explode=explode,
        startangle=90,
        textprops={"fontsize": 11},
    )

    for at in autotexts:
        at.set_fontsize(10)
        at.set_color("white")
        at.set_fontweight("bold")

    ax.set_title("Toss Jeeta = Match Jeeta?",
                 fontsize=13, pad=16)
    fig.tight_layout()
    _save(fig, "03_toss_impact")


# ----- Chart 4: Toss decision — bat ya field ------------------------------------------------------
def chart_toss_decision(df: pd.DataFrame) -> None:
    """Toss jeetnewale ne bat choose kiya ya field?"""

    decision = df["toss_decision"].value_counts()

    colors = ["#DD8452", "#55A868"]
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(
        decision.index,
        decision.values,
        color=colors,
        edgecolor="white",
        linewidth=0.5,
        width=0.4,
    )

    # Value labels
    for bar in bars:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 5,
            str(bar.get_height()),
            ha="center", fontsize=11,
            fontweight="bold", color="#444",
        )

    ax.set_xlabel("Toss Decision", fontsize=11)
    ax.set_ylabel("Count", fontsize=11)
    ax.set_title("Toss Decision — Bat ya Field?",
                 fontsize=13, pad=14)
    fig.tight_layout()
    _save(fig, "04_toss_decision")


# ----- Chart 5: Top 10 venues ------------------------------------------------------
def chart_top_venues(df: pd.DataFrame) -> None:
    """Kaunse stadium mein sabse zyada matches hue?"""

    venues = df["venue"].value_counts().head(10)

    fig, ax = plt.subplots(figsize=FIGURE_SIZE)
    bars = ax.barh(
        venues.index[::-1],
        venues.values[::-1],
        color="#4C72B0",
        edgecolor="white",
        linewidth=0.5,
    )

    # Value labels
    for bar, val in zip(bars, venues.values[::-1]):
        ax.text(
            bar.get_width() + 0.3,
            bar.get_y() + bar.get_height() / 2,
            str(val),
            va="center", fontsize=9, color="#444",
        )

    ax.set_xlabel("Number of Matches", fontsize=11)
    ax.set_title("Top 10 IPL Venues by Match Count",
                 fontsize=13, pad=14)
    fig.tight_layout()
    _save(fig, "05_top_venues")


# ── Run all charts ───────────────────────────────────────────────
def run_all(df: pd.DataFrame) -> None:
    """Saare 5 charts ek saath banao."""
    print("\n📊 Generating all charts...\n")
    charts_top_teams_by_wins(df)
    chart_season_trend(df)
    chart_toss_impact(df)
    chart_toss_decision(df)
    chart_top_venues(df)
    print("\n✅ All 5 charts saved in reports/figures/\n")


# ------ Seedha run karo test ke liye ------------------------------------------------------
if __name__ == "__main__":
    import sys
    sys.path.insert(0, ".")
    from src.data_loader import load_matches_data
    from src.data_cleaner import clean_matches_data

df = clean_matches_data(load_matches_data())
run_all(df)
