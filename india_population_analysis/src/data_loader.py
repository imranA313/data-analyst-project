"""
Step 1 — Data loading aur basic validation.
"""
import pandas as pd
from src.config import RAW_FILE


def load_raw() -> pd.DataFrame:
    """Raw CSV load karo aur column types fix karo."""
    df = pd.read_csv(RAW_FILE)
    df["population_2024"] = df["population_2024"].astype(int)
    df["area_km2"]        = df["area_km2"].astype(float)
    df["literacy_rate"]   = df["literacy_rate"].astype(float)
    return df


def quick_summary(df: pd.DataFrame) -> None:
    """Console pe quick EDA print karo."""
    print("=" * 55)
    print(f"  Shape      : {df.shape}")
    print(f"  Columns    : {list(df.columns)}")
    print(f"\n  Null values:\n{df.isnull().sum().to_string()}")
    print(f"\n  Describe:\n{df.describe().round(2).to_string()}")
    print("=" * 55)


if __name__ == "__main__":
    df = load_raw()
    quick_summary(df)
