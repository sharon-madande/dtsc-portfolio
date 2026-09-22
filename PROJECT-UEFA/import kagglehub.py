import kagglehub

path = kagglehub.dataset_download(
    "azminetoushikwasi/ucl-202122-uefa-champions-league"
)

print("Dataset downloaded to:")
print(path)