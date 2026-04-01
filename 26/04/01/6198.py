import sys
input = sys.stdin.readline

n = int(input())
building = [int(input()) for _ in range(n)]

stack = []
answer = 0

for h in building:
    while stack and stack[-1] <= h:
        stack.pop()
    answer += len(stack)
    stack.append(h)

print(answer)