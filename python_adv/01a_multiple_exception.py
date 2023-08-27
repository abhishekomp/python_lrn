try:
    num = int(input("Enter a number: "))
    answer = 1 / num
    print(answer)
except ValueError as e:
    print(f"Value Error Exception occurred: {e}")
except ZeroDivisionError as e:
    print(f"Make sure you are not dividing by 0")
    # print(f"Zero Exception occurred: {e}")
except Exception as e:
    print(f"Exception occurred: {e}")
print("Thanks for using this code")
