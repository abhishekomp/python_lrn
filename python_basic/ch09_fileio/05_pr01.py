f = open("poem.txt")
text = f.read()
if "twinkle" in text:
    print("Twinkle is present")
else:
    print("Twinkle is NOT present")
