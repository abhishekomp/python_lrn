# Creating a set
a = {1, 3, 5, 9}
print(type(a))

# IMPORTANT: Following will create an empty dictionary and not an empty set.
a = {}
print(type(a))  # will print <class 'dict'>

# Empty Set creation
b = set()
print(type(b))  # will print <class 'set'>

# Adding an element to a set
b.add(4)
b.add(5)

# A list/dictionary cannot be added to a set. A tuple can be added to a set.
# Reason is list is not hasable.
