import pandas as pd

file_path = "/Users/nandjath/.cache/kagglehub/datasets/ramostherunning/champions-league-historical-match-20202026/versions/1/uefa_champions_league_historical_match_statistics_2020_2026.csv"

df = pd.read_csv(file_path)

print("Dataset loaded successfully!")
print("Number of matches:", len(df))
print()


#columns we needed

matches = df[
    [
        "temporada",
        "mandante",
        "visitante",
        "placar",
        "finalizacoes_mandante",
        "finalizacoes_visitante",
        "chutes_a_gol_mandante",
        "chutes_a_gol_visitante",
        "posse_de_bola_mandante",
        "posse_de_bola_visitante",
        "passes_mandante",
        "passes_visitante",
    ]
].copy()


# getting home and away goals from the score

score = matches["placar"].str.extract(r"(\d+)\s*x\s*(\d+)")

matches["home_goals"] = pd.to_numeric(score[0], errors="coerce")
matches["away_goals"] = pd.to_numeric(score[1], errors="coerce")


# home-team statistics

home = pd.DataFrame()

home["season"] = matches["temporada"]
home["team"] = matches["mandante"]

home["matches"] = 1

home["wins"] = (matches["home_goals"] > matches["away_goals"]).astype(int)

home["draws"] = (matches["home_goals"] == matches["away_goals"]).astype(int)

home["losses"] = (matches["home_goals"] < matches["away_goals"]).astype(int)

home["goals_scored"] = matches["home_goals"]
home["goals_conceded"] = matches["away_goals"]

home["shots"] = matches["finalizacoes_mandante"]
home["shots_on_target"] = matches["chutes_a_gol_mandante"]
home["possession"] = matches["posse_de_bola_mandante"]
home["passes"] = matches["passes_mandante"]

# away-team statistics

away = pd.DataFrame()

away["season"] = matches["temporada"]
away["team"] = matches["visitante"]

away["matches"] = 1

away["wins"] = (matches["away_goals"] > matches["home_goals"]).astype(int)

away["draws"] = (matches["away_goals"] == matches["home_goals"]).astype(int)

away["losses"] = (matches["away_goals"] < matches["home_goals"]).astype(int)

away["goals_scored"] = matches["away_goals"]
away["goals_conceded"] = matches["home_goals"]

away["shots"] = matches["finalizacoes_visitante"]
away["shots_on_target"] = matches["chutes_a_gol_visitante"]
away["possession"] = matches["posse_de_bola_visitante"]
away["passes"] = matches["passes_visitante"]


#  home and away observations

team_matches = pd.concat([home, away], ignore_index=True)


# aggregate into team-season statistics

team_stats = (
    team_matches
    .groupby(["season", "team"], as_index=False)
    .agg(
        matches=("matches", "sum"),
        wins=("wins", "sum"),
        draws=("draws", "sum"),
        losses=("losses", "sum"),
        goals_scored=("goals_scored", "sum"),
        goals_conceded=("goals_conceded", "sum"),
        shots=("shots", "mean"),
        shots_on_target=("shots_on_target", "mean"),
        possession=("possession", "mean"),
        passes=("passes", "mean"),
    )
)


#  more features

team_stats["goal_difference"] = (
    team_stats["goals_scored"] -
    team_stats["goals_conceded"]
)

team_stats["win_rate"] = (
    team_stats["wins"] /
    team_stats["matches"]
)

team_stats["goals_per_match"] = (
    team_stats["goals_scored"] /
    team_stats["matches"]
)

team_stats["goals_conceded_per_match"] = (
    team_stats["goals_conceded"] /
    team_stats["matches"]
)


output_file = "team_season_stats.csv"

team_stats.to_csv(output_file, index=False)


# results

print("Team-season statistics created successfully!")
print()

print("Number of team-season observations:", len(team_stats))
print()

print("Columns:")
print(team_stats.columns.tolist())
print()

print("First 10 rows:")
print(team_stats.head(10))

print()

print("Saved to:", output_file)