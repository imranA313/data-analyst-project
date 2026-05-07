# India Population Analysis 🇮🇳

**Tools:** Python · Pandas · Matplotlib · Seaborn  
**Data:** Census 2011 projections + Aadhaar saturation (2024 estimates)

---

## Project Structure

```
india_population_analysis/
├── data/
│   ├── raw/                  ← Original, untouched CSV
│   └── processed/            ← Cleaned CSV (auto-generated)
├── notebooks/
│   └── 01_analysis.py        ← Main script — run this
├── src/
│   ├── config.py             ← Paths, colors, constants
│   ├── data_loader.py        ← Step 1: Load + validate
│   ├── data_cleaner.py       ← Step 2: Clean + feature engineering
│   └── visualizer.py         ← Step 3-4: All 5 charts
├── reports/
│   └── figures/              ← PNG charts (auto-generated)
├── tests/
│   └── test_cleaner.py       ← Unit tests
├── requirements.txt
└── README.md
```

---

## Setup & Run

```bash
# 1. Dependencies install karo
pip install -r requirements.txt

# 2. Project root se run karo
python notebooks/01_analysis.py
```

Charts `reports/figures/` mein save ho jayenge.

---

## Charts Generated

| File | Description |
|------|-------------|
| `01_top10_bar.png` | Top 10 states — horizontal bar |
| `02_population_pie.png` | Population share — pie chart |
| `03_scatter_density.png` | Area vs density — bubble chart |
| `04_region_grouped_bar.png` | Region-wise population + literacy |
| `05_literacy_regression.png` | Literacy vs population trend |

---

## Key Insights

- UP + Maharashtra + Bihar = ~47% of India's population
- Kerala has highest literacy (94%), Bihar lowest (61.8%)
- Delhi is densest (14,000+ per km²) despite being smallest
- Northeast states: small population, high literacy
