def playGame():
    return 40


score = playGame()
with open("hiscore.txt") as f:
    # hiscore = int(f.read())
    hiscore = f.read()

if hiscore == "" or int(hiscore) < score:
    with open("hiscore.txt", "w") as f:
        f.write(str(score))
        print(f"New hi-score {score} written to the file")
else:
    print(f"Score {score} NOT written to the file")
