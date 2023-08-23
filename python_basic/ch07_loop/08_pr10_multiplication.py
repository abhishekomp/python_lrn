# Program to print the multiplication table of user provided number in reverse order
num = int(input("Enter the number \n"))
for i in range(10, 0, -1):
    print(f"{num} X {i} = {num * i}")
