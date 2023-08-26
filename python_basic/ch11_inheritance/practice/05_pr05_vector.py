# Write a program to represent a vector of n dimentions and methods to add and multiply 2 such vectors


class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index += 1
        return str1[:-1]

    def __add__(self, vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)


# v1 = Vector([1, 4, 6])
# v2 = Vector([1, 6, 9])
# v1 = Vector([1, 4, 6, 9, 12])
v1 = Vector([1, 4])
v2 = Vector([1, 6])
print(v1)
print(v2)
print(f"Sum: {v1 + v2}")
