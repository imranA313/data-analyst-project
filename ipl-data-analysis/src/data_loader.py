import pandas as pd
from src.config import DELIVERIES_FILE, MATCHES_FILE


def load_matches_data() -> pd.DataFrame:
    """Load the matches data from the CSV file."""

    matches_df = pd.read_csv(MATCHES_FILE)
    return matches_df


def load_deliveries_data() -> pd.DataFrame:
    """Load the deliveries data from the CSV file."""

    deliveries_df = pd.read_csv(DELIVERIES_FILE)
    return deliveries_df


def quick_summery(df: pd.DataFrame, name: str = "Dataset") -> None:
    """Print a quick summary of the DataFrame."""

    print(f"\n{'='*53}")
    print(f" {name}")
    print(f"{'='*55}")

    # Shape — kitni rows, kitne columns
    print(f"\n Shape      : {df.shape}")
    print(f" Rows       : {df.shape[0]}")
    print(f" Columns    : {df.shape[1]}")

    # Column names
    print(f"\n Column Names:")
    for i, col in enumerate(df.columns, 1):
        print(f"   {i:2}. {col}")

    # Data types
    print(f"\n Data Types:")
    print(df.dtypes.to_string())

    # Data types
    print(f"\n Data Types:")
    print(df.dtypes.to_string())

    # Null values — kaun se columns mein missing data hai
    nulls = df.isnull().sum()
    nulls = nulls[nulls > 0]  # sirf woh jo null hain
    if len(nulls) > 0:
        print(f"\n Null Values (sirf jahan hain):")
        print(nulls.to_string())
    else:
        print(f"\n Null Values: Koi null nahi! ✅")

    # Statistical summary
    print(f"\n Statistical Summary:")
    print(df.describe().round(2).to_string())

    # first 3 rows
    print(f"\n first 3 rows:")
    print(df.head(3).to_string())

    print(f"\n{'='*55}\n")


    # ----- Direct run for testing  ---------------------------------
if __name__ == "__main__":
    print("Loading matches.csv...")
    matches = load_matches_data()
    quick_summery(matches, "MATCHES DATASET")

    print("Loading deliveries.csv...")
    deliveries = load_deliveries_data()
    quick_summery(deliveries, "DELIVERIES DATASET")
