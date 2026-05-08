\# 🏏 IPL Data Analysis (2008–2024)



> Exploratory Data Analysis of Indian Premier League matches

> using Python, Pandas, and Matplotlib.



\---



\## 📌 Project Overview



This project analyzes \*\*1095 IPL matches\*\* from 2008 to 2024

to uncover patterns in team performance, toss impact,

venue trends, and season-wise statistics.



\---



\## 📂 Project Structure

\---

ipl-data-analysis/

├── data/

│   ├── raw/                  ← Original dataset (Kaggle)

│   └── processed/            ← Cleaned data (auto-generated)

├── src/

│   ├── config.py             ← Paths and constants

│   ├── data\_loader.py        ← Load and validate data

│   └── data\_cleaner.py       ← Clean and feature engineering

├── notebooks/

│   └── 01\_analysis.py        ← Main script

├── reports/

│   └── figures/              ← Generated charts

├── requirements.txt

└── README.md



\## 📊 Key Questions Answered



\- 🏆 Which team won the most IPL matches?

\- 📅 How did the number of matches grow season by season?

\- 🎲 Does winning the toss help win the match?

\- 🏟️ Which venues hosted the most matches?

\- 🏏 Bat or field — what do teams prefer after winning toss?



\---



\## 🛠️ Tech Stack



| Tool | Version | Use |

|------|---------|-----|

| Python | 3.10+ | Core language |

| Pandas | 2.0+ | Data manipulation |

| Matplotlib | 3.7+ | Visualizations |

| Seaborn | 0.12+ | Advanced charts |



\---



\## ⚙️ Setup \& Run



```bash

\# 1. Install dependencies

pip install -r requirements.txt



\# 2. Run analysis

python notebooks/01\_analysis.py

```



\---



\## 📈 Sample Insights



\- \*\*Mumbai Indians\*\* have won the most IPL titles

\- \*\*Toss winner wins \~51%\*\* of matches — barely an advantage

\- \*\*Wankhede Stadium\*\* is the most used IPL venue

\- Most matches are won by \*\*5–10 wickets\*\* margin



\---



\## 📁 Dataset



\- \*\*Source:\*\* \[Kaggle — IPL 2008-2024](https://www.kaggle.com/datasets/saiprudvirajy/indian-premier-league-ipl-2008-2024)

\- \*\*Matches:\*\* 1095 rows × 20 columns

\- \*\*Period:\*\* 2008 to 2024



\---



\*Project by \Imran | Data Analyst Portfolio\*

