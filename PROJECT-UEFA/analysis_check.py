import pandas as pd

# Load the team-level dataset
team_summary = pd.read_csv(
    "/Users/nandjath/Desktop/PROJECT-UEFA/team_summary.csv"
)

print("DATA CHECK")
print("----------")

print(f"Number of teams: {len(team_summary)}")
print(f"Missing advancement scores: {team_summary['advancement_score'].isna().sum()}")

print("\nTEAMS BY NUMBER OF CATEGORIES REPRESENTED")
print("-----------------------------------------")

print(
    team_summary[
        [
            "club",
            "categories_represented",
            "unique_top_players",
            "attacking_top_players",
            "defensive_top_players",
            "stage",
            "advancement_score"
        ]
    ]
    .sort_values(
        ["categories_represented", "advancement_score"],
        ascending=[False, False]
    )
    .to_string(index=False)
)

print("\nCATEGORY TOTALS")
print("---------------")

print(
    team_summary[
        ["Goals", "Assists", "Tackles Won", "Balls Recovered"]
    ].sum()
)