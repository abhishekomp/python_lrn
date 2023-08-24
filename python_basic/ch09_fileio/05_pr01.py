f = open("poem.txt")  # mode is by default read
# f = open("poem.txt", "r")
# f = open("poem.txt", "rt")
text = f.read()
if "twinkle" in text:
    print("Twinkle is present")
else:
    print("Twinkle is NOT present")
