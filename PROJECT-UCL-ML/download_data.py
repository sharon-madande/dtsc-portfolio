import kagglehub

# kaggle dataset
path = kagglehub.dataset_download(
    "ramostherunning/champions-league-historical-match-20202026"
)

print("Path to dataset files:", path)