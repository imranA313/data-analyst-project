from pathlib import Path

# ---- Root paths -----------------------------------
ROOT_DIR = Path (__file__).resolve().parent.parent
DATA_RAW = ROOT_DIR /"data" /"raw"
DATA_PROCESSED = ROOT_DIR /"data" /"processed"
FIGURES_DIR = ROOT_DIR /"reports" /"figures"

# ------ Files ---------------------------------------
MATCHES_FILE = DATA_RAW  /"matches.csv"
DELIVERIES_FILE = DATA_RAW /"deliveries.csv"
CLEAN_FILE = DATA_PROCESSED /"matches_clean.csv"

# ----- Charts Setting -------------------------------
FIGURE_DPI = 150
FIGURE_SIZE = (12,6)

# ----- Team Colours  --------------------------------
TEAM_CLOURS = {
    "Mumbai Indians":             "#004BA0",
    "Chennai Super Kings":        "#F9CD05",
    "Royal Challengers Bangalore":"#EC1C24",
    "Kolkata Knight Riders":      "#3A225D",
    "Sunrisers Hyderabad":        "#F7A721",
    "Delhi Capitals":             "#0078BC",
    "Rajasthan Royals":           "#EA1A85",
    "Punjab Kings":               "#AADAFF",
}
