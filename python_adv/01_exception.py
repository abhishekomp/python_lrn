while True:
    print(f"Press q to quit")
    a = input("Enter a number: ")
    if a == "q":
        # quit()
        break
    try:
        print("Trying...")
        a = int(a)
        if a > 6:
            print(f"You entered a nunber greater than 6")
    except Exception as e:
        print(f"Your input resulted in an error: {e}")
print("Thnaks for play this game")
