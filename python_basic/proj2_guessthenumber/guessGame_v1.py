import random


def playGame():
    userGuess = None
    guessCnt = 0
    userPrompt = "Enter your guess\n"
    while userGuess != randomNumber:
        userGuess = int(input(userPrompt))
        guessCnt += 1
        if userGuess == randomNumber:
            print(f"You guess it right in {guessCnt} guesses")
        elif userGuess < randomNumber:
            userPrompt = "That was a lower number. Guess a bigger number.\n"
        else:
            userPrompt = "That was a bigger number. Guess a lower number.\n"
            # print(f"You guess wrong")


# print(f"\n\n")
print(f"\n\n****** Welcome to 'GUESS THE NUMBER GAME 2023' ****** ")
print(f"You need to guess the number that computer has selected from 0 till 100")
randomNumber = random.randint(1, 100)
# print(randomNumber)
choice = input("Do you want to play the game? \nType Yes or y to play \n")
# print(choice)
if choice.lower() in ["yes", "y"]:
    print("Let us play")
    playGame()
else:
    print("Hejdå")
