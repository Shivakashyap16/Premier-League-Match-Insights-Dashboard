# streamlit_app.py

# 🧰 Import required libraries
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

# 🎨 Set Streamlit theme
st.set_page_config(
    page_title="Premier League Insights",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load and display Premier League logo
logo = Image.open("assets/premier_league_logol.png")  # Make sure path is correct

col_logo, col_title = st.columns([1, 5])  # Adjust ratio as needed

with col_logo:
    st.image(logo, width=150)

with col_title:
    st.markdown("<h1 style='margin-top: 15px;'>Premier League Match Insights Dashboard</h1>", unsafe_allow_html=True)

st.markdown("---")

# 📥 Load the cleaned dataset
df = pd.read_csv('../data/epl_cleaned.csv')

# Filter for 2018-19 season
df = df[df["Season"] == "2018-19"]

# 🧮 Compute basic metrics
total_matches = len(df)
total_goals = df['TotalGoals'].sum()
average_goals = round(df['TotalGoals'].mean(), 2)

# 🚪 Sidebar filters
st.sidebar.title("Filter Matches")
home_team = st.sidebar.selectbox("Select Home Team", ['All'] + sorted(df['HomeTeam'].unique().tolist()))
away_team = st.sidebar.selectbox("Select Away Team", ['All'] + sorted(df['AwayTeam'].unique().tolist()))
outcome = st.sidebar.selectbox("Select Match Outcome", ['All'] + df['MatchOutcome'].unique().tolist())

# 📊 Apply filters
filtered_df = df.copy()
if home_team != 'All':
    filtered_df = filtered_df[filtered_df['HomeTeam'] == home_team]
if away_team != 'All':
    filtered_df = filtered_df[filtered_df['AwayTeam'] == away_team]
if outcome != 'All':
    filtered_df = filtered_df[filtered_df['MatchOutcome'] == outcome]

# 🔢 Summary Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Matches", total_matches)
col2.metric("Total Goals", total_goals)
col3.metric("Avg. Goals per Match", average_goals)

st.markdown("---")

# 📋 Show Filtered Match Data
st.subheader("Filtered Match Data")
st.dataframe(filtered_df[['HomeTeam', 'AwayTeam', 'HomeGoals', 'AwayGoals', 'TotalGoals', 'MatchOutcome']], use_container_width=True)

st.markdown("---")

# 📊 Visual Insights Section
st.subheader("Match Visual Insights")

# ➕ Create a 3-column layout for compact graphs
col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("**Goals per Match Distribution**")
    fig1, ax1 = plt.subplots(figsize=(4, 3))
    sns.histplot(df['TotalGoals'], bins=10, kde=True, ax=ax1, color='#1f77b4')
    ax1.set_xlabel("Total Goals", fontsize=9)
    ax1.set_ylabel("Frequency", fontsize=9)
    ax1.set_title("Goals Distribution", fontsize=10)
    plt.tight_layout()
    st.pyplot(fig1)

with col5:
    st.markdown("**Match Outcome Count**")
    fig2, ax2 = plt.subplots(figsize=(4, 3))
    sns.countplot(x='MatchOutcome', data=df, palette='pastel', ax=ax2)
    ax2.set_title("Match Results", fontsize=10)
    ax2.set_ylabel("Matches", fontsize=9)
    ax2.set_xlabel("Outcome", fontsize=9)
    plt.tight_layout()
    st.pyplot(fig2)

with col6:
    st.markdown("**Home vs Away Goals**")
    fig3, ax3 = plt.subplots(figsize=(4, 3))
    sns.boxplot(data=df[['HomeGoals', 'AwayGoals']], palette="Set2", ax=ax3)
    ax3.set_title("Home vs Away Goals", fontsize=10)
    ax3.set_ylabel("Goals", fontsize=9)
    plt.tight_layout()
    st.pyplot(fig3)

st.markdown("---")

# 🔝 Top Scoring Teams
st.subheader("Top Scoring Teams")

# Calculate total goals per team (home + away)
home_goals = df.groupby('HomeTeam')['HomeGoals'].sum()
away_goals = df.groupby('AwayTeam')['AwayGoals'].sum()
total_team_goals = home_goals.add(away_goals, fill_value=0).sort_values(ascending=False).head(10)

fig4, ax4 = plt.subplots(figsize=(10, 4))
sns.barplot(x=total_team_goals.index, y=total_team_goals.values, palette="viridis", ax=ax4)
ax4.set_title("Top 10 Highest Scoring Teams", fontsize=12)
ax4.set_ylabel("Total Goals", fontsize=10)
ax4.set_xlabel("Team", fontsize=10)
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig4)

st.markdown("---")

# 🛡️ Strongest Defenses
st.subheader("Strongest Defenses")

home_conceded = df.groupby('HomeTeam')['AwayGoals'].sum()
away_conceded = df.groupby('AwayTeam')['HomeGoals'].sum()
total_conceded = home_conceded.add(away_conceded, fill_value=0).sort_values().head(10)

fig5, ax5 = plt.subplots(figsize=(10, 4))
sns.barplot(x=total_conceded.index, y=total_conceded.values, palette="crest", ax=ax5)
ax5.set_title("Top 10 Teams with Least Goals Conceded", fontsize=12)
ax5.set_ylabel("Goals Conceded", fontsize=10)
ax5.set_xlabel("Team", fontsize=10)
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig5)

# 🧼 Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size: 12px;'>Premier League Match Insights • Streamlit Dashboard • Built with 💙</p>",
    unsafe_allow_html=True
)
