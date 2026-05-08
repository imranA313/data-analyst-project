import pandas as pd
from src.config import MATCHES_FILE, CLEAN_FILE
from src.data_loader import load_matches_data, quick_summery

def clean_matches_data(matches_df: pd.DataFrame) -> pd.DataFrame:
    """
    matches.csv ko clean karo aur naye columns add karo.

    Steps:
    1. Duplicate rows hatao
    2. date column datetime mein convert karo
    3. Null values handle karo
    4. Naye useful columns add karo
    """
    
    df = matches_df.copy()  # original data ko safe rakhne ke liye copy bana lo
    
    # Step 1: Duplicate rows hatao --------------------------------------------------
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    print(f"[✅]Duplicate rows removed: {before - after}")
      
    
    # Step 2: date column datetime mein convert karo --------------------------------------------------
    df['date'] = pd.to_datetime(df['date'], errors='coerce')  # invalid dates will become NaT
    print(f"[✅]Date column converted to datetime. Null values in date: {df['date'].isnull().sum()}")
    
    # step 3: Null values handle karo ---------------------------------------------
    # date column mein null values hain, unko drop kar dete hain kyunki date important hai
    df["winner"] = df["winner"].fillna("No Result")  # winner column mein null values hain, unko "No Result" se fill kar dete hain
    df["player_of_match"] = df["player_of_match"].fillna("No Award")  # player_of_match column mein null values hain, unko "No Award" se fill kar dete hain
    df["city"] = df["city"].fillna("Unknown")  # city column mein null values hain, unko "Unknown" se fill kar dete hain        
    df["method"] = df["method"].fillna("Normal")  # method column mein null values hain, unko "Unknown" se fill kar dete hain          
    
    # Result_Margin null = Noresult Match
    df["result_margin"] = df["result_margin"].fillna(0)  # result_margin column mein null values hain, unko 0 se fill kar dete hain 
    print(f"[✅]Null values handled.")
    
    # Step 4: Naye useful columns add karo --------------------------------------------------
    # Year coloumn - Grouping krne ke liye kaam ayega
    df['year'] = df['date'].dt.year
    
    # Month column - Kaun se mahine mein zyada matches hote hain, ye dekhne ke liye
    df['month'] = df['date'].dt.month
    
    # Toss_match_winner - Kya toss jeetne wale team ne match jeeta? Ye dekhne ke liye
    df['toss_match_winner'] = df["toss_winner"] == df["winner"]
    
    # Win_type - Kya run se jeeta, wicket se jeeta, ya no result tha
    # Result Column "runs" ya "wicket" se hoga
    df["win_type"] = df["result"].str.strip().str.lower()
    print(f"[✅]Win type column created. Unique values: {df['win_type'].nunique()}")
    
    # Step 5: Final Sort -----------------------------------------------------------------
    df = df.sort_values(by='date').reset_index(drop=True)
    print(f"[✅]Data sorted by date.")
    
    return df
def save_clean_data(df: pd.DataFrame) -> None:
    """Cleaned data ko Processed file mein save karo."""
    CLEAN_FILE.parent.mkdir(parents=True, exist_ok=True)  
    df.to_csv(CLEAN_FILE, index=False)
    print(f"[✅]Cleaned data saved to {CLEAN_FILE}")    
    
    
# ----- Direct run for testing  ---------------------------------
if __name__ == "__main__":
    
    # Load
    print(f"\n[🔄]Loading matches data...")
    matches_df = load_matches_data()      
    
    # Clean    
    print(f"\n[🔄]Cleaning matches data..." )
    clean_df = clean_matches_data(matches_df)
    
    # Save
    print(f"\n[🔄]Saving cleaned data...")                                 
    save_clean_data(clean_df)
    
    # Verify
    print(f"\n[🔍]Verifying cleaned data...")
    
    quick_summery(clean_df, "Cleaned Matches Dataset")
    
    print("\nNew Columns Verification:")
    print(clean_df[['date', 'year', 'month', 'toss_match_winner', 'win_type', 'winner']]
          .head(10).to_string())