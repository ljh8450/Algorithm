def solution(answers):
    answer = []
    n = len(answers)
    people = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    personal_index = [0, 0, 0]
    personal_length = [len(people[0]), len(people[1]), len(people[2])]
    correct = [0, 0, 0]
    for i in range(n):
        for j in range(3):
            if people[j][personal_index[j]] == answers[i]:
                correct[j] += 1
            personal_index[j] = (personal_index[j] + 1) % personal_length[j]
    for i in range(3):
        Top = max(correct)
        if Top == correct[i]:
            print(correct[i])
            answer.append(i+1)
    return answer

answers = [1,3,2,4,2]
print(solution(answers))