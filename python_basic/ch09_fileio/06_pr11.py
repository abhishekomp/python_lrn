import os

oldname = "sample2.txt"
newname = "renamed_by_python.txt"

with open(oldname) as f:
    contents = f.read()

with open(newname, "w") as f:
    f.write(contents)

os.remove(oldname)
