def dev_it():
    user_num= int(input("Insert a number: "))
    try:
        result = 100 / user_num
    except ZeroDivisionError as zde:
        print(zde)
        print("Number isn't right")
    else:
        print(f"Your answer is {result}")

dev_it()
