import json

with open("people.json", "r") as jsonfile:
    not_chd_ppl = json.load(jsonfile)
chd_ppl = []
total_people = 0
total_age = 0
oldest_person = {'Name':'null', 'Age':0}
youngest_person = {'Name':'null', 'Age':1000}


for i in not_chd_ppl:
    if isinstance(i['Age'], int) and i['Age'] > 0:
        chd_ppl.append(i)
        total_age += i['Age']
        total_people += 1
        if i['Age'] > oldest_person['Age']:
            oldest_person = i
        if i['Age'] < youngest_person['Age']:
            youngest_person = i

average_age = round(total_age/ total_people) if total_people else 0


report = {
    'total_people': total_people,
    'average_age': average_age,
    'oldest_person': oldest_person,
    'youngest_person': youngest_person
}

with open("report.json", "w") as jsonfile:
    json.dump(report, jsonfile)