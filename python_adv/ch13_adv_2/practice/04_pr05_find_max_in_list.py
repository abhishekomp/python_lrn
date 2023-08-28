# Program to find the max number in a given list using reduce function
from functools import reduce

l = [2, 5, 8, 150, 34, 40, 45, 56, 60]
val = reduce(max, l)
print(val)
