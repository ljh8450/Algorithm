import heapq
import sys
input = sys.stdin.readline
def dijkstra(s, e, graph, n):
    distances[s] = 0

    pq = []
    heapq.heappush(pq, [0, s])

    while pq:
        dist, now = heapq.heappop(pq)
        if now == e:
            return
        if distances[now] < dist:
            continue
        for next, cost in graph[now]:
            new_distance = dist + cost
            if new_distance < distances[next]:
                distances[next] = new_distance
                heapq.heappush(pq, [new_distance, next])


n = int(input())
m = int(input())
INF = 100_000 * n + 1
graph = [[] for _ in range(n+1)]
distances = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
s, e = map(int, input().split())

dijkstra(s, e, graph, n)
print(distances[e])