import heapq
import sys
input = sys.stdin.readline

n = int(input())
problems = []
heap = []

for _ in range(n):
    d, c = map(int, input().split())
    problems.append((d, c))
problems.sort()

curr = 0
for d, c in problems:
    heapq.heappush(heap, c)
    if len(heap) > d:
        heapq.heappop(heap)

print(sum(heap))