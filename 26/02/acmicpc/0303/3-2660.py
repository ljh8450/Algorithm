from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
while True:
    a, b = map(int, input().split())
    if a == b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)

score = [0] * (n+1)

for i in range(1, n+1):
    dist = [-1] * (n+1)
    q = deque([])
    q.append(i)
    dist[i] = 0

    while q:
        this = q.popleft()
        for nxt in graph[this]:
            if dist[nxt] == -1:
                dist[nxt] = dist[this] + 1
                q.append(nxt)
    score[i] = max(dist[1:])
min_score = min(score[1:])
candidate = [k+1 for k, s in enumerate(score[1:]) if s == min_score]
print(min_score, len(candidate))
print(*candidate, sep=' ')