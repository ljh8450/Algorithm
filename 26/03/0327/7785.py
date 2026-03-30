n = int(input())
people = {}
for _ in range(n):
    person, key = input().split()
    if key == 'enter':
        people[person] = True
    else:
        people[person] = False
person_list = list(sorted(people.keys(), reverse=True))

for person in person_list:
    check = people[person]
    if check:
        print(person)