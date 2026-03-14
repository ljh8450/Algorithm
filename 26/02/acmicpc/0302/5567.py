from collections import deque
import sys
input = sys.stdin.readline

def bfs(k):
    queue = deque([])
    visited[k] = True
    queue.append([k, 0])
    value = 0
    while queue:
        k, l = queue.popleft()
        if l == 2:
            break
            
        for nk in graph[k]:
            if not visited[nk]:
                value += 1
                visited[nk] = True
                queue.append([nk, l+1])
    return value

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
friend = bfs(1)
print(friend)