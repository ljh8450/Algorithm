def solution(brown, yellow):
    total = brown + yellow
    for H in range(1, int(total**0.5) + 1):
        if total % H == 0:
            W = total//H
            if W >= H and (W-2)*(H-2) == yellow:
                answer =[W, H]
    return answer

brown, yellow = 10, 2
print(solution(brown, yellow))