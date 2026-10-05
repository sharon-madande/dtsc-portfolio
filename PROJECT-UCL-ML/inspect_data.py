import os

# path
data_path = "/Users/nandjath/.cache/kagglehub/datasets/ramostherunning/champions-league-historical-match-20202026/versions/1"

print("Files in the dataset folder:")
print()

for file in os.listdir(data_path):
    print(file)