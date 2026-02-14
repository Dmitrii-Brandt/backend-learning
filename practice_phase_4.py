import csv
import json
# FILE I/O

# TASK 13 READING/ WRITING TEXT
# with open("demofile.txt", "w") as f:
#     for n in range(1,6):
#         f.write(f"It's the {n} line of the file\n")
# with open("demofile.txt") as f:
#     for i in f:
#         print(i)

# with open("demofile.txt", "a") as f:
#     f.write("It's the lastest line!\n")

# with open("demofile.txt") as f:
#     print(f.read())


# TASK 14 CSV AND JSON BASICS
# just_people = {"Mark": 22,
            #    "Zoe": 37,
            #    "Natalie": 44,
            #    "Igor": 18}
fieldnames = ["Name", "Age"]
just_people = [{'Name': 'Mark', 'Age': 22},
                 {'Name': 'Zoe', 'Age': 37},
                 {'Name': 'Natalie', 'Age': 44},
                 {'Name': 'Igor', 'Age': 18}
                 ]
with open("people.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(just_people)

with open("people.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        row['Age'] = int(row['Age'])
        print(row)


with open("people.json", "w") as f:
    json.dump(just_people, f)

with open("people.json", "r") as f:
    new_people = json.load(f)

for i in new_people:
    print(i['Name'])
