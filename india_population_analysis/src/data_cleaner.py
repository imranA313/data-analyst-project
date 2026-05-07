"""
Step 2 — Data cleaning aur feature engineering.
"""
import pandas as pd
from src.config import CLEAN_FILE
from src.data_loader import load_raw


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """
    - Duplicates hatao
    - pop_density column add karo (log/km2)
    - pop_crore column add karo (human-readable)
    - pop_share_pct column add karo
    - Sort by population descending
    """
    df = df.drop_duplicates().copy()

    # Derived columns
    df["pop_density"]   = (df["population_2024"] / df["area_km2"]).round(2)
    df["pop_crore"]     = (df["population_2024"] / 1e7).round(2)
    df["pop_share_pct"] = (
        df["population_2024"] / df["population_2024"].sum() * 100
    ).round(2)

    # Sort + rank
    df = df.sort_values("population_2024", ascending=False).reset_index(drop=True)
    df.index += 1
    df.index.name = "rank"

    return df


def save_clean(df: pd.DataFrame) -> None:
    CLEAN_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(CLEAN_FILE)
    print(f"[✓] Cleaned data saved → {CLEAN_FILE.name}")


if __name__ == "__main__":
    raw = load_raw()
    clean_df = clean(raw)
    save_clean(clean_df)
    print(clean_df[["state", "pop_crore", "pop_density", "pop_share_pct"]].head(10))
