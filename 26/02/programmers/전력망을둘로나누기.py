from collections import deque

def solution(n, wires):
	graph = [[] for _ in range(n + 1)]
	for a, b in wires:
		graph[a].append(b)
		graph[b].append(a)

	def bfs(start, cut_a, cut_b):
		visited = [False] * (n + 1)
		q = deque([start])
		visited[start] = True
		cnt = 1

		while q:
			x = q.popleft()
			for nx in graph[x]:
				# 끊을 간선이면 스킵
				if (x == cut_a and nx == cut_b) or (x == cut_b and nx == cut_a):
					continue
				if not visited[nx]:
					visited[nx] = True
					q.append(nx)
					cnt += 1
		return cnt

	answer = 10**9
	for a, b in wires:
		size = bfs(a, a, b)
		answer = min(answer, abs(n - 2 * size))

	return answer


n, wires = 9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
print(solution(n, wires))