class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(
            f"The name of the programmer is {self.company} programmer {self.name} and the product is {self.product}"
        )


abhikriti = Programmer("Abhikriti", "Skype")
johan = Programmer("Johan", "GitHub")
abhikriti.getInfo()
johan.getInfo()
