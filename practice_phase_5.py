# TASK 17 EX
'''
def dev_it():
    try:
        user_num= int(input("Insert a number: "))
        

    except ValueError as ve:
        print(ve)
        print("I said number...")

    else:
        try:
            result = 100 / user_num
        except ZeroDivisionError as zde:
            print(zde)
            print("Number isn't right")
        else:
            print(f"Your answer is {result}")
dev_it()
'''