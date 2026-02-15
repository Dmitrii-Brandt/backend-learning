import json

with open("people.json", "r") as jsonfile:
    not_chd_ppl = json.load(jsonfile)

class Person:
    def __init__(self, name, age):
        if not self.__validate(age):
            raise ValueError("Age must be positive integer")
        self.name = name
        self.age = age

    def __validate(self, age):
        if isinstance(age, int) and age > 0:
            return True
        return False
    
    def __repr__(self):
        return f"Person(name = {self.name}, age = {self.age})"

    def to_dict(self):
        return {
            "Name": self.name,
            "Age": self.age
        }

my_list = []
for i in not_chd_ppl:
    my_list.append(Person(i['Name'], i['Age']))

def whos_oldest(persons_list):
    if len(persons_list) > 0:
        oldest = persons_list[0]
        for i in persons_list:
            if i.age > oldest.age:
                # oldest['Name'] = i.name
                # oldest['Age'] = i.age
                oldest = i
        return oldest
    else:
        return "The list is empty"

def whos_youngest(persons_list):
    if len(persons_list) > 0:
        youngest = persons_list[0]
        for i in persons_list:
            if i.age < youngest.age:
                youngest = i
        return youngest
    else:
        return "The list is empty"

total_people = len(my_list)

def count_average_age(persons_list):
    total_age = 0
    if len(persons_list) > 0:
        for i in persons_list:
            total_age += i.age
        return round(total_age / len(persons_list)) 
    else:
        return "The list is empty"

report = {'total_people': total_people,
          'average_age': count_average_age(my_list),
          'oldest_person': whos_oldest(my_list).to_dict(),
          'youngest_person': whos_youngest(my_list).to_dict()
          }

with open("report.json", "w") as jsonfile:
    json.dump(report, jsonfile)
