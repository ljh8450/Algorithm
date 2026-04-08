import heapq
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    l = int(input())
    heap = list(map(int, input().split()))
    heapq.heapify(heap)
    cost = 0
    while len(heap) > 1:
        file = heapq.heappop(heap) + heapq.heappop(heap)
        heapq.heappush(heap, file)
        cost += file
    print(cost)