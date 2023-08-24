class MyNumber:
    def sum(self):
        return self.a + self.b


num = MyNumber()
num.a = 12
num.b = 34
sum = num.sum()
print(f"Sum of {num.a} and {num.b} is: {sum}")
