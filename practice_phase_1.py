# TASK ONE
my_name = 'Dmitrii'
my_age = 1000
print(f'My name is  {my_name} and my age is {my_age}')
print('My name is ', my_name, ' and my age is ', my_age)
my_num = 100.232
print(my_num * 2)
# TASK TWO

sentence = 'Just when i thought i was out, they pull me back in'
print(sentence.upper())
print(sentence.lower())
print(len(sentence))
print(sentence[-3::-1])

# TASK THREE
num_a = 17
num_b = 23
print('nums sum is', num_a + num_b)
print('nums difference is', num_a - num_b)
print('nums product is', num_a * num_b)
print('nums division is', num_a / num_b)
print('nums remainder of a division is', num_a % num_b)
print('num_a in a power of 3 is', pow(num_a, 3))

# TASK FOUR
fruits = ['banana', 'watermelon', 'strawberry', 'apple', 'pineapple']
print(fruits[0], fruits[-1])
fruits.append('mango')
print(fruits[0], fruits[-1])
print(fruits)
if len(fruits) % 2 != 0:
    print('The middle fruit is ', fruits[int((len(fruits)- 1) / 2)])
else:
    print("There's no middle in the list")
fruits.append('peach')
print(fruits)
if len(fruits) % 2 != 0:
    print('The middle fruit is ', fruits[int((len(fruits)- 1) / 2)])
else:
    print("There's no middle in the list")
#fruits.remove(fruits[round(len(fruits)/2,0)])
#print(middle_fruit)
#print(int(len(fruits) / 2))
fruits.sort()
for n in range(0, len(fruits)):
    print(fruits)
    fruits.pop()

# TASK FIVE
my_set = {4, 4, 5, 9}
print(my_set)
my_tuple = (4, 4, 66, 43, 100, 1000, 88, 100000, 25)
print(my_tuple)
def whats_biggest (your_tuple):
    biggest = 0
    for x in range(len(your_tuple)):
        if your_tuple[x] >= biggest:
            biggest = my_tuple[x]
        else:
            continue
    return(biggest)

print(whats_biggest(my_tuple)) 

print(my_tuple.index(25))
print(max(my_tuple))
print(max(my_set))
my_set.add(1000)
print(my_set.pop())

# TASK SIX (DICTIONARIES)
people = {'Bobby': 39,
          'Natalie': 28,
          'Ivan': 55}
for key in people.keys():
    print(key, 'is', people.get(key), 'years old')

people.update({'Bobby':88})
people['Tyrel'] = 25
for key, value in people.items():
    print(f"{key} is {value} years old")
print("People's names are:")
for i in people:
    print(i)
print("People's ages are:")
for i in people.values():
    print(i)
people = dict(sorted(people.items()))
print(people.items())
people.popitem("Ivan")