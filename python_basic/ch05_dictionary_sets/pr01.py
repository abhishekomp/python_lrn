myDict = {
    "kya": "What",
    "kyun": "Why",
    "kab": "When",
    "kahan": "Where",
    "raja": "King",
    "rani": "Queen",
    "pankha": "Fan",
}

print(f"Options are {list(myDict.keys())}")

searchWord = input("Enter your search word\n")
print(f"The meaning of '{searchWord}' is: {myDict.get(searchWord)}")
