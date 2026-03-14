def solution(participant, completion):
    people = dict()
    for person in participant:
        people[person] = 0
    for person in participant:
        people[person] += 1
    for person in completion:
        people[person] -= 1
    for people_key, people_value in people.items():
        if people_value != 0:
            return people_key
        
print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))