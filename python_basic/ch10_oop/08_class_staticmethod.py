class Employee:
    company = "Google"

    def getSalary(self):
        print(f"Salary of {self.name} is {self.salary}")

    @staticmethod
    def displayCurrentDate():
        print(f"Today is 2023-08-24")


emp = Employee()
emp.name = "John"
emp.salary = 5000
# Employee.getSalary(emp) Below is same as this
emp.getSalary()
emp.displayCurrentDate()
