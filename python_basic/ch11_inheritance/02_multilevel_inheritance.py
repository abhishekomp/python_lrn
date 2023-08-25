class Person:
    country = "India"

    def __init__(self):
        print(f"Initializing Person")

    def breathe(self):
        print(f"Person is breathing")


class Employee(Person):
    company = "Google"

    def __init__(self):
        print(f"Initializing Employee")

    def breathe(self):
        print(f"Employee is breathing")


class Programmer(Employee):
    company = "Fiverr"

    def __init__(self):
        # super().__init__()
        print(f"Initializing Programmer")

    def breathe(self):
        # super().breathe()
        print(f"Programmer is breathing")
        # super().breathe()


# p = Person()
# p.breathe()
e = Employee()
e.breathe()
print(f"Employee's company: {e.company}")
pr = Programmer()
pr.breathe()
print(f"Programmer's country: {pr.country}")
print(f"Programmer's company: {pr.company}")
