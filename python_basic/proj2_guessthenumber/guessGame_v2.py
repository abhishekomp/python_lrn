"""
Enhancement done: The least number of guess is written to a file. If the number of guesses for a win is lower than the last least number of guesses then the new least guess count is written to the file.

Enhancement To do: If user while guessing enters nothing and presses enter then the program throws an error:
ValueError: invalid literal for int() with base 10: ''
"""

import random
from pathlib import Path


def playGame():
    userGuess = None
    guessCnt = 0
    userPrompt = "Enter your guess\n"
    gameScoreFile = "least_guess.txt"
    while userGuess != randomNumber:
        userGuess = int(input(userPrompt))
        guessCnt += 1
        if userGuess == randomNumber:
            print(f"You guess it right in {guessCnt} guesses.")
            path = Path(f"./{gameScoreFile}")
            if path.is_file():
                with open(f"./{gameScoreFile}") as f:
                    leastGuess = f.read()
                    if leastGuess == "" or int(leastGuess) > guessCnt:
                        with open(f"./{gameScoreFile}", "w") as f:
                            f.write(str(guessCnt))
                            print(
                                f"New hi-score {guessCnt} written to the file {gameScoreFile}"
                            )
            else:
                with open(f"./{gameScoreFile}", "w") as f:
                    f.write(str(guessCnt))
                    print(
                        f"Created new file. New hi-score {guessCnt} written to the file {gameScoreFile}"
                    )
        elif userGuess < randomNumber:
            userPrompt = "That was a lower number. Guess a bigger number.\n"
        else:
            userPrompt = "That was a bigger number. Guess a lower number.\n"
            # print(f"You guess wrong")


# print(f"\n\n")
print(f"\n\n****** Welcome to 'GUESS THE NUMBER GAME 2024' ****** ")
print(f"You need to guess the number that computer has selected from 1 till 100")
randomNumber = random.randint(1, 100)
print(randomNumber)
choice = input("Do you want to play the game? \nType Yes or y to play \n")
# print(choice)
if choice.lower() in ["yes", "y"]:
    print("Let us play")
    playGame()
else:
    print("Hejdå! Vi ses snart!")
