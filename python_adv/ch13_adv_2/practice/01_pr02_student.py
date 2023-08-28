name = input("Enter name: ")
marks = input("Enter marks: ")
phoneNum = input("Enter phone number: ")

formatted_str = (
    "The name of the student is {}, his marks are {} and phone number is {}".format(
        name, marks, phoneNum
    )
)
print(formatted_str)
