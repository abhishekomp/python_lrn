# "with" is context manager. it will ensure to close the file.
with open("another.txt", "r") as f:
    a = f.read()
print(a)
