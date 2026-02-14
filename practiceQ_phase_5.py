# CLASSES AND OOP 
# TASK 15 BASIC CLASS

class MyClass:
    x = 5


class Person:
    def __init__(self, name, age = 18):
        self.name = name # memes
        self.age = age

p1 = Person("Nigel", 44)

print(p1.age)
print(p1.name)
p2 = Person()