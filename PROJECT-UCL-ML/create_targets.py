import pandas as pd

df = pd.read_csv("team_season_stats.csv")

# Champions League winners for each season
champions = {
    "20/21": "Chelsea",
    "21/22": "Real Madrid",
    "22/23": "Manchester City",
    "23/24": "Real Madrid",
    "24/25": "Paris Saint-Germain",
}

# Winner column
df["Winner"] = 0

# Winner = 1 to the known champions
for season, champion in champions.items():
    df.loc[
        (df["season"] == season) &
        (df["team"] == champion),
        "Winner"
    ] = 1

# winners found
print("Champions found:")
print()

print(
    df[df["Winner"] == 1][
        ["season", "team", "Winner"]
    ].to_string(index=False)
)

print()

# Count winners
print("Number of winner observations:", df["Winner"].sum())

# Check 25/26 teams
print()
print("2025/26 teams:")
print(
    df[df["season"] == "25/26"][
        ["team", "matches", "wins", "goals_scored", "Winner"]
    ].sort_values("wins", ascending=False).head(15).to_string(index=False)
)

df.to_csv("ml_dataset.csv", index=False)

print()
print("Saved to: ml_dataset.csv")