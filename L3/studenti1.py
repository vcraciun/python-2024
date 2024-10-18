import json

with open('Studenti.json') as f:
    data = json.load(f)

cnt = 0
for student in data.values():
    seminar = sum(student['seminarii']) / len(student['seminarii']) * 0.2
    examene = (student['partial'] + student['curs']) * 0.03
    proiect = student['proiect'] * 0.02

    media = seminar + examene + proiect

    if media >= 4.5:
        cnt += 1

print(cnt)