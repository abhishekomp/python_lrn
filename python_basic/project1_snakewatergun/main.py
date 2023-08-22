import random

# Snake, water gun OR Rock paper scissor


def game(comp, you):
    if comp == you:
        return None
    if comp == "s":
        if you == "w":
            return False
        elif you == "g":
            return True
    elif comp == "w":
        if you == "g":
            return False
        elif you == "s":
            return True
    elif comp == "g":
        if you == "s":
            return False
        elif you == "w":
            return True


# a = input("Computer Turn: Snake(s) Water(w) or Gun(g)?")
print("Computer Turn: Snake(s) Water(w) or Gun(g)?")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = "s"
elif randNo == 2:
    comp = "w"
elif randNo == 3:
    comp = "g"

# print(">>>>Computer's chose: " + comp)
you = input("Player's Turn: Snake(s) Water(w) or Gun(g)?")

result = game(comp, you)
print(f"Computer chose {comp}")
print(f"You chose {you}")

if result == None:
    print("The game is a tie!")
elif result == True:
    print("You win!")
elif result == False:
    print("You lose!")
