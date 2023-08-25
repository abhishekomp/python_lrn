# The concept of property decorator is that we have a method in the class and it will act as a property of the class
# @property is also a getter method
# @name.setter


class Employee:
    company = "Honda"
    salary = 4000
    salarybonus = 500
    # totalSalary = 4500  # what if salarybonus changes next year.

    # Even though this is a function but it will act like a property of the class
    @property
    def totalSalary(self):
        return self.salary + self.salarybonus

    @totalSalary.setter
    def totalSalary(self, val):
        self.salarybonus = val - self.salary


e = Employee()
# Note: we are not writing e.totalSalary()
print(f"Total salary of employee: {e.totalSalary}")
e.totalSalary = 5800
print(f"Salary bonus: {e.salarybonus}")
print(f"Salary: {e.salary}")
