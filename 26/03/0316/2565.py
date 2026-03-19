import sys
input = sys.stdin.readline

n = int(input())
graph = []
dp = [1] * n
for _ in range(n):
    a, b = map(int, input().split())
    graph.append((a, b))

graph.sort()

for i in range(n):
    for j in range(i):
        if graph[j][1] < graph[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n-max(dp))