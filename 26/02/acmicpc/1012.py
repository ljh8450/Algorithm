from collections import deque
import sys
input = sys.stdin.readline

def bfs(start_x, start_y):
    queue = deque([[start_x, start_y]])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and graph[ny][nx] == 1:
                visited[ny][nx] = True
                graph[ny][nx] = 0
                queue.append([nx, ny])

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    local_value = 0
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    visited = [[False]*m for _ in range(n)]
    for x in range(m):
        for y in range(n):
            if graph[y][x] == 1:
                visited[y][x] = True
                graph[y][x] = 0
                bfs(x, y)
                local_value += 1
    print(local_value)