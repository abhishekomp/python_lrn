# Write a program to represent a vector of n dimentions return the dimension of the vector
# Enhancement to do: When adding 2 vectors if they are not of same dimensions then show a message that their dimensions are not same and hence cannot be added
# Enhancement: Show an error if the 2 vectors to be added are not of the same dimensions
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
        if len(self) != len(vec2):
            raise ValueError("Dimension of the vectors to be added is not same.")
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)

    # this method gives the dimension of the vector
    def __len__(self):
        return len(self.vec)


# v1 = Vector([1, 4, 6])
# v2 = Vector([1, 6, 9])
# v1 = Vector([1, 4, 6, 9, 12])
v1 = Vector([1, 4, 9, 12])
v2 = Vector([1, 6])
print(v1)
print(f"Dimension: {len(v1)}")
print(v2)
print(f"Dimension: {len(v2)}")
print(f"Sum: {v1 + v2}")
