import pandas as pd

data_path = "/Users/nandjath/.cache/kagglehub/datasets/azminetoushikwasi/ucl-202122-uefa-champions-league/versions/22"

# all the four datasets
goals = pd.read_csv(f"{data_path}/goals.csv")
attacking = pd.read_csv(f"{data_path}/attacking.csv")
defending = pd.read_csv(f"{data_path}/defending.csv")

#datasets with only the variables we need
goals = goals[["player_name", "club", "goals"]]
assists = attacking[["player_name", "club", "assists"]]
tackles = defending[["player_name", "club", "t_won"]]
recoveries = defending[["player_name", "club", "balls_recoverd"]]

# Calculate the 90th percentile for each category - top 10 players
goals_cutoff = goals["goals"].quantile(0.90)
assists_cutoff = assists["assists"].quantile(0.90)
tackles_cutoff = tackles["t_won"].quantile(0.90)
recoveries_cutoff = recoveries["balls_recoverd"].quantile(0.90)

print("TOP-PERFORMER CUTOFFS")
print("----------------------")
print(f"Goals: {goals_cutoff:.2f}")
print(f"Assists: {assists_cutoff:.2f}")
print(f"Tackles won: {tackles_cutoff:.2f}")
print(f"Balls recovered: {recoveries_cutoff:.2f}")

# Get the top-performing players
top_goals = goals[goals["goals"] >= goals_cutoff].copy()
top_assists = assists[assists["assists"] >= assists_cutoff].copy()
top_tackles = tackles[tackles["t_won"] >= tackles_cutoff].copy()
top_recoveries = recoveries[recoveries["balls_recoverd"] >= recoveries_cutoff].copy()

print("\nTOP GOAL SCORERS")
print(top_goals.sort_values("goals", ascending=False).to_string(index=False))

print("\nTOP ASSIST PROVIDERS")
print(top_assists.sort_values("assists", ascending=False).to_string(index=False))

print("\nTOP TACKLERS")
print(top_tackles.sort_values("t_won", ascending=False).to_string(index=False))

print("\nTOP BALL RECOVERERS")
print(top_recoveries.sort_values("balls_recoverd", ascending=False).to_string(index=False))

# Add a category label to each top-performer dataset

top_goals = top_goals.rename(columns={"goals": "value"})
top_goals["category"] = "Goals"

top_assists = top_assists.rename(columns={"assists": "value"})
top_assists["category"] = "Assists"

top_tackles = top_tackles.rename(columns={"t_won": "value"})
top_tackles["category"] = "Tackles Won"

top_recoveries = top_recoveries.rename(columns={"balls_recoverd": "value"})
top_recoveries["category"] = "Balls Recovered"

# Combine all top performers into one table
top_players = pd.concat(
    [top_goals, top_assists, top_tackles, top_recoveries],
    ignore_index=True
)

print("\nALL TOP PERFORMERS")
print(top_players.to_string(index=False))

# Save the table
output_path = "/Users/nandjath/Desktop/PROJECT-UEFA/top_players.csv"

top_players.to_csv(output_path, index=False)

print(f"\nSaved top_players.csv to: {output_path}")