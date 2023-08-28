def square(num):
    return num * num


list1 = [1, 2, 3]
# Method 1
list2 = []
for item in list1:
    list2.append(square(item))
print(list2)

# Method 2
list3 = [num * num for num in list1]
print(f"list3= {list3}")

# Method 3
print(list(map(square, list1)))
