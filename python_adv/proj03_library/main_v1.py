class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print(f"\nAvailable books in the library are: \n")
        for book in self.books:
            print(" * " + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"Book: '{bookName}' has been issued to you")
            self.books.remove(bookName)
        else:
            print("Sorry, this book is already issued")

    def returnBook(self, bookName):
        self.books.append(bookName)
        print(f"Book '{bookName}' has been returned. Thank you!")


class Student:
    def __init__(self):
        pass

    def requestBook(self):
        self.reqBook = input("Enter the name of the book you want to borrow: ")
        return self.reqBook

    def returnBook(self):
        self.returnBook = input("Enter the book to be returned: ")
        return self.returnBook


if __name__ == "__main__":
    student = Student()
    centralLibrary = Library(
        [
            "Algorithms",
            "Django",
            "Clrs",
            "Python Notes",
            "Python in Action",
            "Java in a Nutshell",
        ]
    )
    while True:
        welcomeMsg = """\n=====Welcome to Central Library====
        Please choose an option:
        1. Display books
        2. Borrow book
        3. Return book
        4. Quit
        """
        print(welcomeMsg)
        userChoice = int(input("Enter a choice: "))

        if userChoice == 1:
            centralLibrary.displayAvailableBooks()
        elif userChoice == 2:
            bookRequested = student.requestBook()
            centralLibrary.borrowBook(bookRequested)
        elif userChoice == 3:
            bookToReturn = student.returnBook()
            centralLibrary.returnBook(bookToReturn)
        elif userChoice == 4:
            print("Thanks for choosing Central Library!\n")
            exit()
        elif userChoice == 5:
            print("Invalid choice")
