"""
Step 3 & 4 — Saare charts yahan hain.
Har function ek chart banata hai aur reports/figures/ mein save karta hai.
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
from src.config import FIGURES_DIR, FIGURE_DPI, FIGURE_SIZE, PALETTE

# ── Global style ────────────────────────────────────────────────
plt.rcParams.update({
    "font.family":        "DejaVu Sans",
    "axes.spines.top":    False,
    "axes.spines.right":  False,
    "axes.grid":          True,
    "grid.alpha":         0.3,
    "figure.dpi":         FIGURE_DPI,
})


def _save(fig: plt.Figure, name: str) -> None:
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    path = FIGURES_DIR / f"{name}.png"
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print(f"[✓] Saved → {path.name}")


# ── Chart 1: Top 10 states — horizontal bar ─────────────────────
def chart_top10_bar(df: pd.DataFrame) -> None:
    top10  = df.head(10).copy()
    colors = [PALETTE.get(r, "#888") for r in top10["region"]]

    fig, ax = plt.subplots(figsize=FIGURE_SIZE)
    bars = ax.barh(
        top10["state"][::-1],
        top10["pop_crore"][::-1],
        color=colors[::-1],
        edgecolor="white",
        linewidth=0.5,
    )

    for bar, val in zip(bars, top10["pop_crore"][::-1]):
        ax.text(
            bar.get_width() + 0.3,
            bar.get_y() + bar.get_height() / 2,
            f"{val:.1f} Cr",
            va="center", fontsize=9, color="#444",
        )

    ax.set_xlabel("Population (Crore)", fontsize=11)
    ax.set_title("Top 10 Most Populated States — India 2024", fontsize=13, pad=14)

    legend_elements = [
        mpatches.Patch(facecolor=v, label=k)
        for k, v in PALETTE.items()
        if k in top10["region"].values
    ]
    ax.legend(handles=legend_elements, title="Region",
              fontsize=9, title_fontsize=9, loc="lower right")

    fig.tight_layout()
    _save(fig, "01_top10_bar")


# ── Chart 2: Population share — pie chart ───────────────────────
def chart_pie_share(df: pd.DataFrame) -> None:
    top5  = df.head(5).copy()
    other_val = df.iloc[5:]["pop_share_pct"].sum()
    other = pd.DataFrame([{"state": "Others", "pop_share_pct": other_val}])
    pie_df = pd.concat([top5[["state", "pop_share_pct"]], other], ignore_index=True)

    colors  = ["#4C72B0", "#DD8452", "#55A868", "#C44E52", "#8172B2", "#BBBBBB"]
    explode = [0.04] * len(pie_df)

    fig, ax = plt.subplots(figsize=(8, 8))
    wedges, texts, autotexts = ax.pie(
        pie_df["pop_share_pct"],
        labels=pie_df["state"],
        autopct="%1.1f%%",
        colors=colors,
        explode=explode,
        startangle=140,
        textprops={"fontsize": 10},
    )
    for at in autotexts:
        at.set_fontsize(9)
        at.set_color("white")

    ax.set_title("Population Share by State — India 2024", fontsize=13, pad=16)
    fig.tight_layout()
    _save(fig, "02_population_pie")


# ── Chart 3: Area vs Population density — bubble scatter ────────
def chart_scatter_density(df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=FIGURE_SIZE)

    for region, grp in df.groupby("region"):
        ax.scatter(
            grp["area_km2"] / 1000,
            grp["pop_density"],
            label=region,
            color=PALETTE.get(region, "#888"),
            s=grp["pop_crore"] * 5,
            alpha=0.75,
            edgecolors="white",
            linewidths=0.5,
        )

    for _, row in df.nlargest(5, "pop_density").iterrows():
        ax.annotate(
            row["state"],
            (row["area_km2"] / 1000, row["pop_density"]),
            textcoords="offset points",
            xytext=(6, 4),
            fontsize=8, color="#333",
        )

    ax.set_xlabel("Area (000 km²)", fontsize=11)
    ax.set_ylabel("Population Density (per km²)", fontsize=11)
    ax.set_title(
        "Area vs Population Density\n(Bubble size = population)",
        fontsize=13, pad=14,
    )
    ax.legend(title="Region", fontsize=9, title_fontsize=9)
    fig.tight_layout()
    _save(fig, "03_scatter_density")


# ── Chart 4: Region-wise grouped bar ────────────────────────────
def chart_region_bar(df: pd.DataFrame) -> None:
    region_stats = (
        df.groupby("region")
          .agg(
              total_pop=("pop_crore", "sum"),
              avg_literacy=("literacy_rate", "mean"),
          )
          .reset_index()
          .sort_values("total_pop", ascending=False)
    )

    x      = range(len(region_stats))
    width  = 0.4
    colors = [PALETTE.get(r, "#888") for r in region_stats["region"]]

    fig, ax1 = plt.subplots(figsize=FIGURE_SIZE)
    ax2 = ax1.twinx()

    bars = ax1.bar(
        [i - width / 2 for i in x],
        region_stats["total_pop"],
        width=width, color=colors, alpha=0.85, label="Population (Cr)",
    )
    line, = ax2.plot(
        [i + width / 2 for i in x],
        region_stats["avg_literacy"],
        "o--", color="#333", linewidth=1.8, markersize=6, label="Avg Literacy %",
    )

    ax1.set_xticks(list(x))
    ax1.set_xticklabels(region_stats["region"], fontsize=10)
    ax1.set_ylabel("Total Population (Crore)", fontsize=11)
    ax2.set_ylabel("Average Literacy Rate (%)", fontsize=11)
    ax2.set_ylim(50, 100)
    ax1.set_title("Region-wise Population vs Literacy Rate", fontsize=13, pad=14)

    ax1.legend(
        handles=[bars, line],
        labels=["Population (Cr)", "Avg Literacy %"],
        fontsize=9, loc="upper right",
    )
    fig.tight_layout()
    _save(fig, "04_region_grouped_bar")


# ── Chart 5: Literacy vs Population — regression scatter ────────
def chart_literacy_regression(df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=FIGURE_SIZE)

    colors = [PALETTE.get(r, "#888") for r in df["region"]]
    ax.scatter(
        df["literacy_rate"], df["pop_crore"],
        c=colors, s=60, alpha=0.8,
        edgecolors="white", linewidths=0.5,
    )

    sns.regplot(
        x="literacy_rate", y="pop_crore", data=df,
        scatter=False, ax=ax,
        line_kws={"color": "#555", "linewidth": 1.5, "linestyle": "--"},
    )

    for _, row in df.nlargest(3, "pop_crore").iterrows():
        ax.annotate(
            row["state"],
            (row["literacy_rate"], row["pop_crore"]),
            textcoords="offset points", xytext=(6, 4), fontsize=8,
        )

    ax.set_xlabel("Literacy Rate (%)", fontsize=11)
    ax.set_ylabel("Population (Crore)", fontsize=11)
    ax.set_title(
        "Literacy Rate vs Population — Is there a pattern?",
        fontsize=13, pad=14,
    )
    fig.tight_layout()
    _save(fig, "05_literacy_regression")


# ── Run all ──────────────────────────────────────────────────────
def run_all(df: pd.DataFrame) -> None:
    """Saare 5 charts ek saath banao."""
    print("\n Generating all charts...\n")
    chart_top10_bar(df)
    chart_pie_share(df)
    chart_scatter_density(df)
    chart_region_bar(df)
    chart_literacy_regression(df)
    print("\n All charts saved in reports/figures/\n")


if __name__ == "__main__":
    from src.data_loader  import load_raw
    from src.data_cleaner import clean
    df = clean(load_raw())
    run_all(df)
