myDict = {
    "fast": "Abhishek",
    "street": "Claessonsgatan 5",
    "city": "Gothenburg",
    "aList": [1, 2, 3],
}

# Prints the value associated with the key "fast"
print(myDict["fast"])
print(myDict.get("fast2"))

# Can assign value for a key
myDict["streetNum"] = 5
print(myDict)

# Methods
# print(myDict.keys())  # this will give an object of type dict_keys. It gives all the keys.
# print(list(myDict.keys())) #Convert the keys object in a list.

# print(myDict.values())  # prints the values of the dictionary
# print(myDict.items())  # prints the (key, value) for all entries of the dictionary

updatedDict = {"babu": "Abhikriti"}
# updates a dictionary by adding key-value from another dictionary. New key-value entries will be added to the existing dictionary
myDict.update(updatedDict)
print(myDict)

# Difference between using get vs square brackets
# print(myDict.get("fast2"))  # if the key is not present then it will return None else the value associated with the key
# print(myDict["fast2"])  # if the key is not present then it will throw error (key error) else the value associated with the key
