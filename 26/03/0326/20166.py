import sys
input = sys.stdin.readline

def dfs(tx, ty, tc, god_like, make):
    global cnt
    if tc == k:
        if god_like == make:
            cnt += 1
        return
    for i in range(8):
        nx, ny = tx + dx[i], ty + dy[i]
        nc = tc + 1
        if nx < 0:
            nx += m
        if nx >= m:
            nx -= m
        if ny < 0:
            ny += n
        if ny >= n:
            ny -= n
        next_word = grid[ny][nx]
        next_target = god_like[tc]
        if next_word == next_target:
            next_make = make + next_word
            dfs(nx, ny, nc, god_like, next_make)

n, m, k = map(int, input().split())

grid = [input().rstrip() for _ in range(n)]
god_likes = [input().rstrip() for _ in range(k)]

dx, dy = [0, 1, 1, 1, 0, -1, -1, -1], [-1, -1, 0, 1, 1, 1, 0, -1]
sdx, sdy = [0, 0, 1, -1], [1, -1, 0, 0]

for god_like in god_likes:
    cnt = 0
    for x in range(m):
        for y in range(n):
            if god_like[0] != grid[y][x]:
                continue
            make = '' + god_like[0]
            dfs(x, y, 1, god_like, make)
    print(cnt)