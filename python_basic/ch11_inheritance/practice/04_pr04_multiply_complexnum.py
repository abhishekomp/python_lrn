# The formula for multiplying complex numbers is: (a + ib) (c + id) = (ac - bd) + i(ad + bc).
# https://www.mathsisfun.com/algebra/complex-number-multiply.html
class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i

    def __str__(self):
        if self.imaginary < 0:
            return f"{self.real} - {-self.imaginary}i"
        return f"{self.real} + {self.imaginary}i"

    def __add__(self, c):
        return Complex(self.real + c.real, self.imaginary + c.imaginary)

    def __mul__(self, c):
        return Complex(
            ((self.real * c.real) - (self.imaginary * c.imaginary)),
            ((self.real * c.imaginary) + (self.imaginary * c.real)),
        )


c1 = Complex(3, 2)
c2 = Complex(1, 7)
print(c1 + c2)
print(f"Multiplication result: {c1*c2}")
# (3 − 2i) (−4 + 3i) = -6 + 17i
c3 = Complex(3, -2)
c4 = Complex(-4, 3)
print(f"Multiplication result: {c3*c4}")

# Showing negative imaginary part
c5 = Complex(1, -4)
c6 = Complex(331, -37)
print(f"Multiplication result: {c5*c6}")
