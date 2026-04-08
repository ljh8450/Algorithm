from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque([i for i in range(1, n+1)])

while queue:
    if len(queue) == 1:
        print(queue[0])
        break
    queue.popleft()
    queue.append(queue.popleft())