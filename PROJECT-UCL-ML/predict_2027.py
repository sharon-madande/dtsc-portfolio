import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("team_season_stats.csv")
ml_data = pd.read_csv("ml_dataset.csv")

features = [
    "matches",
    "wins",
    "draws",
    "losses",
    "goals_scored",
    "goals_conceded",
    "goal_difference",
    "win_rate",
    "goals_per_match",
    "goals_conceded_per_match",
    "shots",
    "shots_on_target",
    "possession",
    "passes"
]

previous_features = [
    "previous_" + feature
    for feature in features
]

X_train = ml_data[previous_features]
y_train = ml_data["Winner"]

final_model = LogisticRegression(
    max_iter=2000
)

final_model.fit(X_train, y_train)

# 4. 2026/27 UEFA Champions League teams

teams_2026_27 = [
    "AEK Athens",
    "Arsenal",
    "Aston Villa",
    "Atlético Madrid",
    "FC Barcelona",
    "FC Bayern München",
    "Bodø/Glimt",
    "Borussia Dortmund",
    "Club Brugge KV",
    "Como",
    "Fenerbahçe",
    "Feyenoord",
    "Galatasaray",
    "Inter",
    "LASK",
    "RB Leipzig",
    "RC Lens",
    "Lille",
    "Liverpool FC",
    "Manchester City",
    "Manchester United",
    "SSC Napoli",
    "Paris Saint-Germain",
    "FC Porto",
    "PSV Eindhoven",
    "Real Betis",
    "Real Madrid",
    "AS Roma",
    "Sabah",
    "Shakhtar Donetsk",
    "SK Slavia Praha",
    "ŠK Slovan Bratislava",
    "Sporting CP",
    "VfB Stuttgart",
    "Viking",
    "Villarreal"
]

# 26/27 team's latest available UCL season

prediction_rows = []

for team in teams_2026_27:

    team_data = df[
        df["team"] == team
    ].copy()

    if team_data.empty:
        continue

    team_data["season_start"] = (
        team_data["season"]
        .str[:2]
        .astype(int)
    )

    # Most recent available UCL season
    latest = team_data.sort_values(
        "season_start",
        ascending=False
    ).iloc[0]

    row = {
        "team": team,
        "source_season": latest["season"]
    }

    for feature in features:
        row[feature] = latest[feature]

    prediction_rows.append(row)

prediction_data = pd.DataFrame(
    prediction_rows
)

# teams with no historical UCL data

available_teams = set(
    prediction_data["team"]
)

missing_teams = [
    team
    for team in teams_2026_27
    if team not in available_teams
]

print()
print("2026/27 TEAMS WITHOUT HISTORICAL KAGGLE UCL DATA")
print("=" * 60)

for team in missing_teams:
    print("-", team)

print()
print(
    "Teams with historical UCL data:",
    len(prediction_data)
)

print(
    "Teams without historical UCL data:",
    len(missing_teams)
)

# Prediction features

X_prediction = prediction_data[
    features
].copy()

X_prediction.columns = previous_features

# Predict winner probability

prediction_data["Winner_Probability"] = (
    final_model
    .predict_proba(X_prediction)[:, 1]
)

# Rank teams

prediction_data = prediction_data.sort_values(
    "Winner_Probability",
    ascending=False
).reset_index(drop=True)

prediction_data["Rank"] = (
    prediction_data.index + 1
)

# final ranking

print()
print("2026/27 CHAMPIONS LEAGUE WINNER ESTIMATE")
print("=" * 75)

print(
    prediction_data[
        [
            "Rank",
            "team",
            "source_season",
            "Winner_Probability"
        ]
    ].to_string(
        index=False,
        formatters={
            "Winner_Probability": "{:.3f}".format
        }
    )
)


top_team = prediction_data.iloc[0]

print()
print("TOP MODEL ESTIMATE")
print("=" * 60)

print(
    f"{top_team['team']} "
    f"({top_team['Winner_Probability']:.3f})"
)

print()
print(
    "These are model estimates, "
    "not the actually winner of the 2027 champion."
)


prediction_data.to_csv(
    "2027_predictions.csv",
    index=False
)

print()
print("Predictions saved to: 2027_predictions.csv")