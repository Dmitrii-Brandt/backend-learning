# CLASSES AND OOP 
# TASK 15 BASIC CLASS

''' learning classes
class Person:
    species = "Human"

    def __init__(self, name, age = 18):
        self.name = name # memes
        self.age = age

    def printname(self):
        print(self.name)

    def printage(self):
        print(self.age)

    def displayinfo(self):
        print(f"Name is {self.name}, age is {self.age}")

    def have_birthday(self):
        self.age += 1
        print(f"Happy Birthday, {self.name}, \nyou're {self.age} years old now")

    def __str__(self):
       return f"{self.name} ({self.age})"

p1 = Person("Nigel", 44)

class Student(Person):
    def __init__(self, name, grad_year, age=18):
        super().__init__(name, age)
        self.grad_year = grad_year

    def welcome(self):
        print("Welcome", self.name, "to the class of", self.grad_year)
    

s1 = Student("Mike", 2030)
'''

class Person:
    object_counter = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        type(self).object_counter += 1
    
    def greeting(self):
        print(f"Hello, dear {self.name}")

    def happy_bday(self):
        self.age += 1


guy_1 = Person("Nigel", 44)
guy_2 = Person("Nick", 22)

guy_1.greeting()
guy_2.greeting()
print (Person.object_counter)
