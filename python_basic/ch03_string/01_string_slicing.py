name = "Donald"
print(name[0])  # will print D
name[0] = "T"  # This is not allowed

print(name[0, 3])  # will print Don. From index 0 till index 3(excluding index 3)

# Negative indices
# Donald
# Last character is accessed using -1

# print(name[:4]) is same as print(name[0:4])

# ******************#
# Slicing with skip value
# word = "amazing"
# word[1:6:2] -> 'mzn'
# word[:7] = word[0:] = 'amazing'
