import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
jewels = list(sorted(tuple(map(int, input().split())) for _ in range(n)))
bags = list(sorted(int(input()) for _ in range(k)))
candidate = []
cost = 0
index = 0

for bag in bags:
    while index < n and jewels[index][0] <= bag:
        heapq.heappush(candidate, -jewels[index][1])
        index += 1
    
    if candidate:
        cost -= heapq.heappop(candidate)

print(cost)