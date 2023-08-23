def calcSum(n):
    if n == 1:
        return 1
    return calcSum(n - 1) + n


num = 10
sum = calcSum(num)
print(f"Sum of all natural numbers upto {num} is {sum}")

n = 8
print("*" * n)  # prints "*"" n times
