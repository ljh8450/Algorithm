import heapq
import sys
input = sys.stdin.readline

min_heap = []
max_heap = []
n = int(input())

for _ in range(n):
    x = int(input())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -x)
    else:
        heapq.heappush(min_heap, x)

    if min_heap and -min_heap[0] > max_heap[0]:
        max_value = -heapq.heappop(max_heap)
        min_value = heapq.heappop(min_heap)

        heapq.heappush(max_heap, -min_value)
        heapq.heappush(min_heap, max_value)

    print(-max_heap[0])