fileName = "pr05_input.txt"
with open(fileName) as f:
    content = f.read()

words = ["donkey", "kaddu"]
for word in words:
    content = content.replace(word, "$#%$#%$#%")

with open(f"{fileName}_updated", "w") as f:
    f.write(content)
    print(f"Done")
