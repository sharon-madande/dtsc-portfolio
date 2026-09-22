import pandas as pd

data_path = "/Users/nandjath/.cache/kagglehub/datasets/azminetoushikwasi/ucl-202122-uefa-champions-league/versions/22"

key_stats = pd.read_csv(f"{data_path}/key_stats.csv")

teams = sorted(key_stats["club"].unique())

print("UEFA CHAMPIONS LEAGUE TEAMS")
print("---------------------------")

for team in teams:
    print(team)

print(f"\nTotal teams: {len(teams)}")