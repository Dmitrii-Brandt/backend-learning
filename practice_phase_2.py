# LOGIC AND LOOPS
# TASK 7

# new_num = int(input("Please give number:"))
# if new_num > 0:
#     print("number is positive")
# elif new_num <0:
#     print("number is negative")
# else:
#     print("number is zero, hehe")
# iterations = 0
# while True:
#     user_age = int(input("What's your age?\n Insert here: "))
#     if user_age >= 18:
#         print("You can vote, congrats")
#     else:
#         print("You need to wait with voting, pal")
#     iterations += 1
#     if iterations == 3:
        # break

# TASK 8
# for i in range(2, 21, 2):
#     print(i)

# my_fruits = ['Mango', 'Cherry', 'Banana', 'Apple']
# for i in range(len(my_fruits)):
#     print(my_fruits[i].upper())

# TASK 9
nums = [1, 3, 4, 199, 101, 110001]
for i in nums:
    if i >= 100:
        print(i)
    else:
        print(f"The number {i} is less then 100")
even_nums = 0
for i in nums:
    if i % 2 == 0:
        even_nums += 1
print(f"There are {even_nums} even numbers")