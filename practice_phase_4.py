import csv
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
just_people = {"Mark": 22,
               "Zoe": 37,
               "Natalie": 44,
               "Igor": 18}

with open("people.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows([
        ["Bobby", 22],
        ['Maggie', 44]
    ])
