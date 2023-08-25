class Employee:
    company = "Google"

    def __init__(self):
        print(f"Initializing Employee")

    def showDetails(self):
        print(f"This is an employee from company {self.company}")


class Programmer(Employee):
    language = "Python"
    company = "Youtube"

    def __init__(self):
        super().__init__()
        print(f"Initializing Programmer")

    def getLanguage(self):
        print(f"The language is {self.language}")

    def showDetails(self):
        # super().showDetails()
        print(f"This is a programmer from company {self.company}")


# e = Employee()
# e.showDetails()
p = Programmer()
# p.showDetails()
# print(f"Employee company: {e.company}")
# print(f"Programmer company: {p.company}")
