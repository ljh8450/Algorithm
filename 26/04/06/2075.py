import heapq
import sys
input = sys.stdin.readline

heap = []
n = int(input())
for i in range(n):
    row = list(map(int, input().split()))
    for x in row:
        if len(heap) < n:
            heapq.heappush(heap, x)
        else:
            if heap[0] < x:
                heapq.heapreplace(heap, x)
print(heap[0])