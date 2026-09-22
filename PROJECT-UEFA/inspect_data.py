import pandas as pd
import os

data_path = "/Users/nandjath/.cache/kagglehub/datasets/azminetoushikwasi/ucl-202122-uefa-champions-league/versions/22"

files = [
    "attacking.csv",
    "attempts.csv",
    "defending.csv",
    "distributon.csv",
    "disciplinary.csv",
    "goalkeeping.csv",
    "goals.csv",
    "key_stats.csv"
]

for file in files:
    file_path = os.path.join(data_path, file)
    df = pd.read_csv(file_path)

    print("\n" + "=" * 60)
    print(file)
    print("=" * 60)
    print("Rows and columns:", df.shape)
    print("Columns:")
    print(df.columns.tolist())
    print("\nMissing values:")
    print(df.isnull().sum())