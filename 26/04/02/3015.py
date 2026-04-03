import sys
input = sys.stdin.readline

n = int(input())
answer = 0
stack = []

for _ in range(n):
    h = int(input())
    cnt = 1

    while stack and stack[-1][0] < h:
        answer += stack.pop()[1]
    
    if stack and stack[-1][0] == h:
        same_cnt = stack.pop()[1]
        answer += same_cnt
        if stack:
            answer += 1

        stack.append((h, same_cnt + 1))
    else:
        if stack:
            answer += 1
        stack.append((h, 1))

print(answer)