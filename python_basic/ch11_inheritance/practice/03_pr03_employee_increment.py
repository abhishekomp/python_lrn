class Employee:
    salary = 1000
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary * self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sal):
        self.increment = sal / self.salary


e = Employee()
print(f"Salary after increment: {e.salaryAfterIncrement}")
e.salaryAfterIncrement = 4000
print(f"Salary after increment: {e.salaryAfterIncrement}, increment = {e.increment}")
