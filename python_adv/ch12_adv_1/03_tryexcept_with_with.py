# Else part of the try except gets executed only when try finishes successfully.
# If try resulted in exception and the exception was handled then else part will not execute

try:
    i = int(input("Enter a number: "))
    c = 1 / i
except Exception as e:
    print(e)
else:
    print("We were successful")
