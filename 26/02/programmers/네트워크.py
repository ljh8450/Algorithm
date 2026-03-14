from collections import deque
def solution(n, computers):
    answer = 0
    def bfs(v):
        queue = deque([v])
        visited[v] = True
        while queue:
            current = queue.popleft()
            for next_node in graph  [current]:
                if not visited[next_node]:
                    queue.append(next_node)
                    visited[next_node] = True

    visited = [False]*n
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i].append(j)
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
    return answer

n, computers = 3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))