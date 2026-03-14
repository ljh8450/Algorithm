import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
max_s = 0
cnt = 0

def dfs(x, y, k):
    visited[y][x] = True
    area = 1

    for i in range(4):
        nx, ny, nk = x+dx[i], y+dy[i], k+1
        if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and graph[ny][nx] == 1:
            area += dfs(nx, ny, nk)
    return area

for y in range(n):
    for x in range(m):
        if not visited[y][x] and graph[y][x] == 1:
            cnt += 1
            local_s = dfs(x, y, 1)
            if local_s > max_s:
                max_s = local_s

print(f'{cnt}\n{max_s}')