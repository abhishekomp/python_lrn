def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This is not good - Abhishek")


a = increment("24a")
print(a)
