from collections import deque
import sys
input = sys.stdin.readline

def bfs(sx, sy):
    queue = deque([(sx, sy, 0)])
    dist = [[[-1, -1] for _ in range(m)] for _ in range(n)]
    dist[sy][sx][0] = 1
    while queue:
        tx, ty, is_broken = queue.popleft()
        if tx == m-1 and ty == n-1:
            return dist[ty][tx][is_broken]

        for i in range(4):
            nx, ny = tx+dx[i], ty+dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if matrix[ny][nx] == 0 and dist[ny][nx][is_broken] == -1:
                    dist[ny][nx][is_broken] = dist[ty][tx][is_broken] + 1
                    queue.append((nx, ny, is_broken))
                if matrix[ny][nx] == 1 and is_broken == 0 and dist[ny][nx][1] == -1:
                    dist[ny][nx][1] = dist[ty][tx][is_broken] + 1
                    queue.append((nx, ny, 1))
    return -1

n, m = map(int, input().split())
data = [input().rstrip() for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
matrix = []
for y in range(n):
    row = []
    for x in range(m):
        row.append(int(data[y][x]))
    matrix.append(row)
print(bfs(0, 0))