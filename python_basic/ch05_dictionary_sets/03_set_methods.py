# Creating an empty set
b = set()
# print(type(b))  # will print <class 'set'>

# Adding element to the set
b.add(4)
b.add(5)
# b.add([4, 5, 6])  # cannot add a list, dictionary to a set

# Length of Set
print(len(b))

# Remove an element from a Set
b.remove(5)
b.remove(15)  # will throw an error because element 15 does not exist in the Set

# Remove a random element from a Set
b.pop()

# Clear
b.clear()

# Union
set1.union(set2)

# Intersection
set1.intersection(set2)
