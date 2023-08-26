from pathlib import Path


# create a Path object with the path to the file
gameScoreFile = "least_guess.txt"
# path = Path("./least_guess.txt")
path = Path(f"./{gameScoreFile}")
print(path.is_file())
