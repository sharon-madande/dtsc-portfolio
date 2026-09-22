import pandas as pd

# File paths
top_players_path = "/Users/nandjath/Desktop/PROJECT-UEFA/top_players.csv"
advancement_path = "/Users/nandjath/Desktop/PROJECT-UEFA/team_advancement.csv"

# Load datasets
top_players = pd.read_csv(top_players_path)
team_advancement = pd.read_csv(advancement_path)

# Count unique top-performing players by team and category
team_counts = (
    top_players.groupby(["club", "category"])["player_name"]
    .nunique()
    .unstack(fill_value=0)
    .reset_index()
)

# Make sure all four categories exist
for category in ["Goals", "Assists", "Tackles Won", "Balls Recovered"]:
    if category not in team_counts.columns:
        team_counts[category] = 0

# Count how many categories each team is represented in
team_counts["categories_represented"] = (
    team_counts[
        ["Goals", "Assists", "Tackles Won", "Balls Recovered"]
    ] > 0
).sum(axis=1)

# Count unique top-performing players
unique_players = (
    top_players.groupby("club")["player_name"]
    .nunique()
    .rename("unique_top_players")
)

team_counts = team_counts.merge(
    unique_players,
    on="club",
    how="left"
)

# Count total category qualifications
category_observations = (
    top_players.groupby("club")
    .size()
    .rename("total_top_player_observations")
)

team_counts = team_counts.merge(
    category_observations,
    on="club",
    how="left"
)

# Add attacking and defensive totals
team_counts["attacking_top_players"] = (
    team_counts["Goals"] + team_counts["Assists"]
)

team_counts["defensive_top_players"] = (
    team_counts["Tackles Won"] + team_counts["Balls Recovered"]
)

# IMPORTANT:
# Start with all 32 teams so teams with zero top performers remain.
team_summary = team_advancement.merge(
    team_counts,
    on="club",
    how="left"
)

# Replace missing counts with 0
count_columns = [
    "Goals",
    "Assists",
    "Tackles Won",
    "Balls Recovered",
    "categories_represented",
    "unique_top_players",
    "total_top_player_observations",
    "attacking_top_players",
    "defensive_top_players"
]

team_summary[count_columns] = (
    team_summary[count_columns].fillna(0)
)

# Sort by advancement
team_summary = team_summary.sort_values(
    "advancement_score",
    ascending=False
)

# Save final dataset
output_path = "/Users/nandjath/Desktop/PROJECT-UEFA/team_summary.csv"

team_summary.to_csv(output_path, index=False)

print("TEAM SUMMARY")
print("------------")
print(team_summary.to_string(index=False))

print(f"\nTotal teams: {len(team_summary)}")
print(f"\nSaved team_summary.csv to: {output_path}")