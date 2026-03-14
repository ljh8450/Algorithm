from collections import deque
from math import inf
def solution(maps):
    n = len(maps)
    m = len(maps[0]) 
    visited = [[False] * m for _ in range(n)]
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    def bfs(x, y, k):
        nonlocal answer
            
        queue = deque([[x, y, k]])
        visited[x][y] = True
        while queue:
            tx, ty, tk = queue.popleft()
            if tx == n-1 and ty == m-1:
                return tk+1
            for i in range(4):
                nx, ny = tx+dx[i], ty+dy[i]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                    queue.append([nx, ny, tk+1])
                    visited[nx][ny] = True
        return -1

    answer = bfs(0, 0, 0)
    if answer == None:
        return -1
    else:
        return answer

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))
