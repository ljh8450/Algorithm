from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque([])

for _ in range(n):
    ops = input().rstrip()
    if ops == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif ops == 'size':
        print(len(queue))
    elif ops == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif ops == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif ops == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
    else:
        _, operand = ops.split()
        queue.append(operand)