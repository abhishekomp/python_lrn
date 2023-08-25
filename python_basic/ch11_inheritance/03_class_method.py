class Employee:
    company = "Toyota"
    salary = 100
    location = "Tokyo"

    # def changeSalary(self, sal):
    #     self.__class__.salary = sal

    @classmethod
    def changeSalary(cls, sal):
        cls.salary = sal


e = Employee()

print(f"Employee object salary: {e.salary}")
print(f"Employee class salary: {Employee.salary}")
e.changeSalary(500)
print(f"After execution of class method")
print(f"Employee object salary: {e.salary}")
print(f"Employee class salary: {Employee.salary}")
