# Finally block gets executes even if you have mentined exit() in the program.
# finally block executes irrespective of the exception
try:
    i = int(input("Enter a number: "))
    c = 1 / i
except Exception as e:
    print(e)
    # quit()
    # exit()
else:
    print("We were successful")
finally:
    print("Thanks for using the program")
