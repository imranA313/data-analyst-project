"""
Project-wide configuration — paths, colors, constants.
Ek jagah se badlo, poore project mein apply hoga.
"""
from pathlib import Path

# ── Root paths ──────────────────────────────────────────────────
ROOT_DIR       = Path(__file__).resolve().parent.parent
DATA_RAW       = ROOT_DIR / "data" / "raw"
DATA_PROCESSED = ROOT_DIR / "data" / "processed"
REPORTS_DIR    = ROOT_DIR / "reports"
FIGURES_DIR    = REPORTS_DIR / "figures"

# ── File names ──────────────────────────────────────────────────
RAW_FILE   = DATA_RAW / "india_population.csv"
CLEAN_FILE = DATA_PROCESSED / "india_population_clean.csv"

# ── Visualization settings ──────────────────────────────────────
FIGURE_DPI  = 150
FIGURE_SIZE = (12, 6)
PALETTE = {
    "North":     "#4C72B0",
    "South":     "#DD8452",
    "East":      "#55A868",
    "West":      "#C44E52",
    "Central":   "#8172B2",
    "Northeast": "#937860",
}
