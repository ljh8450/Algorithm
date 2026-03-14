import heapq
import sys
input = sys.stdin.readline
INF = 10**9

m, n = map(int, input().split())
maze = list(input().rstrip() for _ in range(n))

dist = [[INF] * m for _ in range(n)]
dist[0][0] = 0

pq = [(0, 0, 0)]

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

while pq:
    w, x, y = heapq.heappop(pq)

    if w > dist[y][x]:
        continue

    if x == m-1 and y == n-1:
        print(w)
        break
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < m and 0 <= ny < n:
            nw = w + (1 if maze[ny][nx] == '1' else 0)

            if nw < dist[ny][nx]:
                dist[ny][nx] = nw
                heapq.heappush(pq, (nw, nx, ny))