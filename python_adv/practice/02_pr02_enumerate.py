list1 = [3, 53, 2, True, 6.2, "John", "Joe", 500, 600]
for index, item in enumerate(list1):
    # print(f"{index}->{item}")
    if index == 2 or index == 4 or index == 6:
        print(f"The element at index: {index+1} is {item}")
