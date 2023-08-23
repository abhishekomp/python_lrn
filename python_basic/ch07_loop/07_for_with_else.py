# Else part of the for loop is executed when the for loop completes without any break statement.
# If a break statement is encountered then the else part will not execute.
for i in range(1, 8):
    print(i)
else:
    print("From else part of for loop")

# for else with break. Note it.
for i in range(1, 8):
    print(i)
    if i == 5:
        break
else:
    print("From else part of for loop")
