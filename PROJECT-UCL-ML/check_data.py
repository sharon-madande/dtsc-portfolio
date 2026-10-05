import pandas as pd

# Path to the downloaded dataset
file_path = "/Users/nandjath/.cache/kagglehub/datasets/ramostherunning/champions-league-historical-match-20202026/versions/1/uefa_champions_league_historical_match_statistics_2020_2026.csv"

# Load the dataset
df = pd.read_csv(file_path)

print("Dataset loaded successfully!")
print()

# Basic information
print("Number of rows:", len(df))
print("Number of columns:", len(df))
print()

# Show column names
print("Column names:")
for column in df.columns:
    print("-", column)

print()

# Show the first 5 rows
print("First 5 rows:")
print(df.head())

print()

# Show data types
print("Data types:")
print(df.dtypes)