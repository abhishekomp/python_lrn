class Vehicle:
    company = "Volvo"

    def __init__(self):
        print(f"Inside Vehicle constructor")

    def drive(self):
        print(f"Inside Vehicle drive function")

    def showDetails(self):
        print(f"Inside show details method of Vehicle")
        # print(f"Vehicle belongs to company {self.company}")


class Automobile:
    def __init__(self):
        print(f"Inside Automobile constructor")

    def showDetails(self):
        print(f"Inside show details method of Automobile")


vehicle = Vehicle()
vehicle.showDetails()
automobile = Automobile()
automobile.showDetails()
