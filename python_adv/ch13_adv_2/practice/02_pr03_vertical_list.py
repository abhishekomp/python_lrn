# For join to work on the elements of this list, the elements itself must be in string format
# TypeError: sequence item 0: expected str instance, int found
# l = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

l = [str(i * 7) for i in range(1, 11)]

str = "\n".join(l)
print(str)
