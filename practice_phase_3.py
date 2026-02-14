# TASK 10

# def get_square(num):
#     sqr_num = num*num
#     return(sqr_num)
# print(get_square(10))


# def get_sum(one, two):
#     nums_sum = one + two
#     return(nums_sum)

# print(get_sum(100, 10))

# TASK 11

# def get_largest(your_list):
#     largest = max(your_list)
#     return(largest)

# numbers = [100, 29, 1, 1000, 34343]
# biggest = get_largest(numbers)
# print(biggest)

# def reverse_str(your_string):
#     rev_str = your_string[::-1]
#     return(rev_str)

# print(reverse_str("I got my mind set on you"))

# TASK 12

def greeting (name = 'Guest'):
    user_name = input("Insert your name:")
    if len(user_name) > 0:
        name = user_name
    print(f"Hello, {name}, how are you?")

greeting()
