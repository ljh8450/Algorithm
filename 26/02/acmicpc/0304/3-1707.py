from collections import deque
import sys
input = sys.stdin.readline

def is_bipartite(v, graph):
	color = [0] * (v + 1)  # 0: 미방문, 1/-1: 두 색

	for start in range(1, v + 1):
		if color[start] != 0:
			continue

		q = deque([start])
		color[start] = 1

		while q:
			u = q.popleft()
			for w in graph[u]:
				if color[w] == 0:
					color[w] = -color[u]
					q.append(w)
				elif color[w] == color[u]:
					return False

	return True

t = int(input())
for _ in range(t):
	v, e = map(int, input().split())
	graph = [[] for _ in range(v + 1)]
	for _ in range(e):
		a, b = map(int, input().split())
		graph[a].append(b)
		graph[b].append(a)

	print("YES" if is_bipartite(v, graph) else "NO")