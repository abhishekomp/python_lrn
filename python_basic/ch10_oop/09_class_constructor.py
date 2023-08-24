class Employee:
    company = "Google"

    # def __init__(self):
    #     print("No-arg Construtor invoked")

    def __init__(self, name, salary):
        print("parameterized Construtor invoked")
        self.name = name
        self.salary = salary

    def getSalary(self):
        print(f"Salary of {self.name} is {self.salary}")

    @staticmethod
    def displayCurrentDate():
        print(f"Today is 2023-08-24")


# emp = Employee()  #This will throw an error
emp2 = Employee("Mark", 50000)
emp2.getSalary()
