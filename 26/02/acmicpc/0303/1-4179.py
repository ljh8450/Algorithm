from collections import deque
import sys
input = sys.stdin.readline

INF = 10**9
r, c = map(int, input().split())
maze = [list(input().rstrip()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
disable = ['F', '#']
jx, jy = 0, 0
fire_q = deque([])
fire_time = [[INF] * c for _ in range(r)]
j_time = [[-1] * c for _ in range(r)]
for y in range(r):
    for x in range(c):
        if maze[y][x] == 'J':
            jx, jy = x, y
            j_time[y][x] = 0
        if maze[y][x] == 'F':
            fire_q.append((x, y))
            fire_time[y][x] = 0

jq = deque([(jx, jy)])

while fire_q:
    tfx, tfy  = fire_q.popleft()
    for i in range(4):
        nfx, nfy = tfx + dx[i], tfy + dy[i]
        if 0 <= nfx < c and 0 <= nfy < r and maze[nfy][nfx] != '#' and fire_time[nfy][nfx] == INF:
            fire_time[nfy][nfx] = fire_time[tfy][tfx] + 1
            fire_q.append((nfx, nfy))

answer = 0
while jq:
    tjx, tjy = jq.popleft()
    t = j_time[tjy][tjx]

    if tjx == 0 or tjx == c-1 or tjy == 0 or tjy == r-1:
        answer = t+1
        break
    for i in range(4):
        njx, njy = tjx + dx[i], tjy + dy[i]
        if 0 <= njx < c and 0 <= njy < r:
            if maze[njy][njx] == '#':
                continue
            if j_time[njy][njx] != -1:
                continue

            nt = t+1
            if nt < fire_time[njy][njx]:
                j_time[njy][njx] = nt
                jq.append((njx, njy))

if answer == 0:
    print("IMPOSSIBLE")
else:
    print(answer)