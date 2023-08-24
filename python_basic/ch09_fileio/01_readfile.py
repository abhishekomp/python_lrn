# Use open function to read the content of a file
# All 3 below statements have the same meaning
f = open("sample.txt")  # by default the mode is r
# f = open("sample.txt", "r")
# f = open("sample.txt", "rt")
data = f.read()
# data = f.read(5) #Reads 5 characters from the file
# data = f.read() #Should not write read multiple times on the same file.
print(data)
f.close()
