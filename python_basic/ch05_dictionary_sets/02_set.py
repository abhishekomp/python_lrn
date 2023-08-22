a = {1, 3, 5, 9}
print(type(a))

a = {}  # this will create an empty dictionary and not an empty set.
print(type(a))  # will print <class 'dict'>

# Empty Set
b = set()
print(type(b))  # will print <class 'set'>
b.add(4)
b.add(5)
