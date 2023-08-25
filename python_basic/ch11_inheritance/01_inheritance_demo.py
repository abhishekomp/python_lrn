class Employee:
    company = "Google"

    def showDetails(self):
        print(f"This is an employee from company {self.company}")


class Programmer(Employee):
    language = "Python"
    company = "Youtube"

    def getLanguage(self):
        print(f"The language is {self.language}")

    def showDetails(self):
        # super().showDetails()
        print(f"This is a programmer from company {self.company}")


e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
print(f"Employee company: {e.company}")
print(f"Programmer company: {p.company}")
