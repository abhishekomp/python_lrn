class Employee:
    company = "Google"


harry = Employee()
john = Employee()
print(harry.company)
print(john.company)
Employee.company = "YouTube"
print(harry.company)
print(john.company)
harry.company = "Amazon"
print(harry.company)  # instance attribute value will be printed
