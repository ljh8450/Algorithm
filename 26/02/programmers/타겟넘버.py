def solution(numbers, target):
    n = len(numbers)
    answer = 0
    def dfs(data, v):
        nonlocal answer
        if v == n:
            if data == target:
                answer += 1
            return 0
        
        dfs(data+numbers[v], v+1)
        dfs(data-numbers[v], v+1)
    dfs(0, 0)
    return answer

numbers, target = [1, 1, 1, 1, 1], 3
print(solution(numbers, target))