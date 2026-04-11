import heapq
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    min_heap = []
    max_heap = []
    visited = [False] * n
    for i in range(n):
        o, k = input().split()
        k = int(k)
        if o == 'I':
            visited[i] = True
            heapq.heappush(min_heap, (k, i))
            heapq.heappush(max_heap, (-k, i))
        else:
            if k == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    visited[heapq.heappop(max_heap)[1]] = False
                if max_heap:
                    visited[heapq.heappop(max_heap)[1]] = False
            else:
                while min_heap and not visited[min_heap[0][1]]:
                    visited[heapq.heappop(min_heap)[1]] = False
                if min_heap:
                    visited[heapq.heappop(min_heap)[1]] = False
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    if not min_heap or not max_heap:
        print('EMPTY')
    else:
        print(-max_heap[0][0], min_heap[0][0])