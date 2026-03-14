from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    n = 102
    graph = [[False]*n for _ in range(n)]
    visited = [[False]*n for _ in range(n)]
    characterX, characterY = characterX*2, characterY*2
    itemX, itemY = itemX*2, itemY*2
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 =  x1*2, y1*2, x2*2, y2*2
        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                graph[y][x] = True
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 =  x1*2, y1*2, x2*2, y2*2
        for y in range(y1+1, y2):
            for x in range(x1+1, x2):
                graph[y][x] = False
            
    def bfs(characterX, characterY, k):
        queue = deque([[characterX, characterY, k]])
        visited[characterY][characterX] = True
        while queue:
            this_x, this_y, this_k = queue.popleft()
            if this_x == itemX and this_y == itemY:
                return this_k//2
            for i in range(4):
                nx, ny = this_x + dx[i], this_y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx] and graph[ny][nx] == True:
                    queue.append([nx, ny, this_k+1])
                    visited[ny][nx] = True

    answer = bfs(characterX, characterY, 1)
    return answer

rectangle, characterX, characterY, itemX, itemY = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8
print(solution(rectangle, characterX, characterY, itemX, itemY))