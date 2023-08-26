class Animal:
    animalType = "Mammal"


class Pet(Animal):
    color = "White"


class Dog(Pet):
    @staticmethod
    def bark():
        print(f"Woof Woof")


d = Dog()
d.bark()
