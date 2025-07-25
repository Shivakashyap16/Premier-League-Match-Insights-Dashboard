# 🏆 Premier League Match Insights Dashboard

This is an interactive Streamlit dashboard that provides visual and statistical insights into Premier League matches for the 2018–19 season. It includes goals analysis, match outcomes, top teams, and defensive performance — all with dynamic filtering capabilities.

---

## 📁 Project Structure

```

PremierLeagueDashboard/
│
├── app/
│   └── streamlit_app.py        # Main Streamlit app
│   └── assets/
│         └── premier_league_logol.png  # Premier League logo
│
├── data/
│   └── epl_2018_2019.csv       # Data for 2018-19 season
│   └── epl_cleaned.csv         # Cleaned dataset for 2018–19 season
│
├── images/
│   └── Dashboard               # Screenshot
│   └── Filtered Match Data     # Screenshot
│   └── Match Visual Insights   # Screenshot
│   └── Strongest Defenses      # Screenshot
│   └── Top Scoring Teams       # Screenshot
|
├── notebooks/
│   └── data_cleaning.ipynb     # Jupyter notebook for cleaning and preprocessing raw match data
│   └── eda_analysis.ipynb      # Jupyter notebook for exploratory data analysis and insights generation
|
├── README.md                   # This file
└── requirements.txt            # Python dependencies

````

---

## 🧪 Features

- 📊 Interactive filters for home team, away team, and match outcome
- 📈 Distribution of goals per match
- 📊 Match outcome summary
- 📦 Boxplot of home vs away goals
- 🚀 Top 10 scoring teams
- 🛡️ Strongest defenses (teams with least goals conceded)
- 📑 Filtered match table
- 🖼️ Premier League logo and custom theme

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/PremierLeagueDashboard.git
cd PremierLeagueDashboard
````

### 2️⃣ Install Dependencies

It's recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

Install required packages:

```bash
pip install -r requirements.txt
```

**Or manually install:**

```bash
pip install streamlit pandas matplotlib seaborn pillow
```

### 3️⃣ Run the Streamlit App

```bash
streamlit run app/streamlit_app.py
```

Then open the URL (usually `http://localhost:8501`) in your browser.

---

## 📂 Dataset

* File: `data/epl_cleaned.csv`
* Source: A cleaned version of Premier League match data for the 2018–19 season
* Required columns include:

  * `HomeTeam`, `AwayTeam`
  * `HomeGoals`, `AwayGoals`
  * `TotalGoals`, `MatchOutcome`
  * `Season`

---

## ✅ Requirements

* Python 3.7+
* Streamlit
* Pandas
* Matplotlib
* Seaborn
* Pillow

> These are listed in `requirements.txt` as well.

---

## 📌 Notes

* Ensure the **logo image** is present at `assets/premier_league_logol.png`
* Confirm the **CSV file path** is correct: `data/epl_cleaned.csv`
* App is currently hardcoded to display the **2018–19 season**

---


## 📄 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgements

* [Premier League](https://www.premierleague.com/) — for match data inspiration
* Streamlit — for the web framework

---

> Built with 💙 using Python & Streamlit
