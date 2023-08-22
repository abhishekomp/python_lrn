list = [1, 8, 7, 2, 21, 15]

# sort() This method does not return any thing. It just sorts the provided list.
# list_sorted = list.sort() #This will result in None. sort() is not returning anything. It sorts the original list.
# print(list)

print(f"Sorted list: {list.sort()}")

list.sort()
print(f"The sorted list is: {list}")

# reverse
# list.reverse()
print(
    f"Reverse list: {list.reverse()}"
)  # this prints None. Why? It does not return anything.

# append
list.append(100)
print(list)

# insert at a particular index
list.insert(2, 500)
print(list)

# pop
list.pop()  # removes the last element from the list
# list.pop(2)  # removes the element at index 2
print(list)

# remove
list.remove(15)  # removes the element '15' from the list

# sum a list
marks = [50, 60, 70, 80]
print(f"Sum of marks is: {sum(marks)}")
