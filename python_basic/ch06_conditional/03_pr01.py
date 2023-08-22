num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

if num1 > num4:
    bigger1 = num1
else:
    bigger1 = num4

if num2 > num3:
    bigger2 = num2
else:
    bigger2 = num3

if bigger1 > bigger2:
    print(str(bigger1) + " is the largest")
else:
    print(str(bigger2) + " is the largest")
