# Calculator
class Calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"The square of {self.number} is {self.number **2}")

    def cube(self):
        print(f"The cube of {self.number} is {self.number **3}")

    def squareroot(self):
        print(f"The squareroot of {self.number} is {self.number **0.5}")


a = Calculator(3)
a.square()
a.squareroot()
a.cube()
