def greater_than_5(num):
    if num > 5:
        return True
    else:
        return False


g10 = lambda num: num > 10


# fruits = ["Apple", "Banana", "Pears", "Mango", "Blueberry", "Apricot"]
numList = [1, 4, 6, 8, 9, 14, 28]
print(list(filter(greater_than_5, numList)))
print(list(filter(g10, numList)))
