# Problem 1 (Multiplication Table) using while loop
num = int(input("Enter the number \n"))
i = 1
while i <= 10:
    print(f"{str(num)} X {str(i)} = {str(num * i)}")
    i += 1
print(f"Multiplication table of {num} printed.")
