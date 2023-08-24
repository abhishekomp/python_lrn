"""
Seats: 1  2  3  4  5  6  7  8  9  10
"""


class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getInfo(self):
        print(f"Train name: {self.name}, seats available are: {self.seats}")

    def getSeatFare(self):
        print(f"The price of the ticket is Rs. {self.fare}")

    def bookTicket(self):
        if self.seats > 0:
            print(f"Your ticket is booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print(f"Tyväär! This train is fully booked.")

    def cancelTicket(self):
        pass


intercity = Train("Intercity Express: 14015", 90, 1)
intercity.getInfo()
intercity.getSeatFare()
intercity.bookTicket()

intercity.getInfo()
intercity.bookTicket()
