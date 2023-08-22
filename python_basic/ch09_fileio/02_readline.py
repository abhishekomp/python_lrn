# Use readline function to read one line of a file
f = open("sample.txt", "r")
f = open("sample.txt")  # by default the mode is r

# Read 1st line
data = f.readline()
print(data)

# Read 2nd line
data = f.readline()
print(data)

f.close()
