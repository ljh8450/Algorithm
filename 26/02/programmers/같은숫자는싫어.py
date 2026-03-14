def solution(arr):
    answer = []
    current = -1
    for num in arr:
        if current != num:
            current = num
            answer.append(num)
    return answer

arr=[4,4,4,3]
print(solution(arr))