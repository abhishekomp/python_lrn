l = [2, 5, 8, 15, 34, 40, 45, 56, 60]
divisible_by_5 = lambda num: num % 5 == 0
l2 = list(filter(divisible_by_5, l))
print(l2)
