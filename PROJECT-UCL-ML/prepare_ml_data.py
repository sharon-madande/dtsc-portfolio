import pandas as pd

# Load the team-season statistics
df = pd.read_csv("team_season_stats.csv")


#Champions for each season
champions = {
    "21/22": "Real Madrid",
    "22/23": "Manchester City",
    "23/24": "Real Madrid",
    "24/25": "Paris Saint-Germain",
    "25/26": "Paris Saint-Germain"
}


#common features from the previous season

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


# --------------------------------------------------
# 3. Create previous-season features
# --------------------------------------------------

previous_season_data = df[
    ["season", "team"] + features
].copy()

previous_season_data = previous_season_data.rename(
    columns={
        feature: "previous_" + feature
        for feature in features
    }
)

# The season represented by these statistics
previous_season_data["previous_season"] = (
    previous_season_data["season"]
)

previous_season_data = previous_season_data.drop(
    columns=["season"]
)


#target-season data
target_seasons = [
    "21/22",
    "22/23",
    "23/24",
    "24/25",
    "25/26"
]

target_data = []

for season in target_seasons:

    # Determine which previous season provides the features
    previous_season_number = int(season[:2]) - 1
    previous_season = (
        f"{previous_season_number:02d}/{season[:2]}"
    )

    # Get teams from the target season
    season_teams = df[
        df["season"] == season
    ][["team"]].copy()

    season_teams["season"] = season

    # Merge with previous-season statistics
    merged = season_teams.merge(
        previous_season_data,
        on="team",
        how="left"
    )

    merged = merged[
        merged["previous_season"] == previous_season
    ].copy()

    # winner target
    merged["Winner"] = (
        merged["team"] == champions[season]
    ).astype(int)

    target_data.append(merged)


# combine all target seasons
ml_data = pd.concat(
    target_data,
    ignore_index=True
)


#missing values

previous_features = [
    "previous_" + feature
    for feature in features
]

for column in previous_features:

    ml_data[column] = ml_data[column].fillna(
        ml_data[column].median()
    )


#training and test seasons

training_seasons = [
    "21/22",
    "22/23",
    "23/24",
    "24/25"
]

test_season = "25/26"

ml_data["dataset_type"] = "training"

ml_data.loc[
    ml_data["season"] == test_season,
    "dataset_type"
] = "test"

ml_data.to_csv(
    "ml_dataset.csv",
    index=False
)


print("New prediction dataset created!")
print()

print(
    "Number of observations:",
    len(ml_data)
)

print()

print(
    "Training observations:",
    len(
        ml_data[
            ml_data["dataset_type"] == "training"
        ]
    )
)

print()

print(
    "2025/26 test observations:",
    len(
        ml_data[
            ml_data["dataset_type"] == "test"
        ]
    )
)

print()

print("Winner observations:")
print(
    ml_data[
        ml_data["Winner"] == 1
    ][
        ["season", "team", "previous_season", "Winner"]
    ].to_string(index=False)
)

print()

print("Dataset split:")
print(
    ml_data[
        ["season", "previous_season", "dataset_type"]
    ]
    .drop_duplicates()
    .sort_values("season")
    .to_string(index=False)
)

print()

print("Missing values:")
print(
    ml_data[previous_features]
    .isnull()
    .sum()
)

print()

print("Saved to: ml_dataset.csv")