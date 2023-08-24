with open("pr04_input.txt") as f:
    content = f.read()

content = content.replace("donkey", "$#%$#%$#$#%")
with open("pr04_input.txt", "w") as f:
    f.write(content)
    print(f"Done")
