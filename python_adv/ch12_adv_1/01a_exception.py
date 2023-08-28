try:
    num = int(input("Enter a number: "))
    answer = 1 / num
    print(answer)
except Exception as e:
    print(f"Exception occurred: {e}")
print("Thanks for using this code")
