import pandas as pd

# Tournament advancement for the 2021-2022 UEFA Champions League
# Higher values mean a team advanced further.

advancement = {
    "Ajax": ("Round of 16", 2),
    "Atalanta": ("Group Stage", 1),
    "Atlético": ("Quarterfinal", 3),
    "Barcelona": ("Group Stage", 1),
    "Bayern": ("Quarterfinal", 3),
    "Benfica": ("Quarterfinal", 3),
    "Beşiktaş": ("Group Stage", 1),
    "Chelsea": ("Quarterfinal", 3),
    "Club Brugge": ("Group Stage", 1),
    "Dortmund": ("Group Stage", 1),
    "Dynamo Kyiv": ("Group Stage", 1),
    "Inter": ("Round of 16", 2),
    "Juventus": ("Round of 16", 2),
    "LOSC": ("Round of 16", 2),
    "Leipzig": ("Group Stage", 1),
    "Liverpool": ("Runner-up", 5),
    "Malmö": ("Group Stage", 1),
    "Man. City": ("Semifinal", 4),
    "Man. United": ("Round of 16", 2),
    "Milan": ("Group Stage", 1),
    "Paris": ("Round of 16", 2),
    "Porto": ("Group Stage", 1),
    "Real Madrid": ("Champion", 6),
    "Salzburg": ("Round of 16", 2),
    "Sevilla": ("Group Stage", 1),
    "Shakhtar Donetsk": ("Group Stage", 1),
    "Sheriff": ("Group Stage", 1),
    "Sporting CP": ("Round of 16", 2),
    "Villarreal": ("Semifinal", 4),
    "Wolfsburg": ("Group Stage", 1),
    "Young Boys": ("Group Stage", 1),
    "Zenit": ("Group Stage", 1)
}

# Convert the dictionary into a DataFrame
team_advancement = pd.DataFrame(
    [
        {"club": club, "stage": stage, "advancement_score": score}
        for club, (stage, score) in advancement.items()
    ]
)

# Display the data
print(team_advancement.sort_values("advancement_score").to_string(index=False))

print(f"\nTotal teams: {len(team_advancement)}")

# Save the file
output_path = "/Users/nandjath/Desktop/PROJECT-UEFA/team_advancement.csv"
team_advancement.to_csv(output_path, index=False)

print(f"\nSaved team_advancement.csv to: {output_path}")