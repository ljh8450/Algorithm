import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []
answer = 0

for _ in range(n):
    heapq.heappush(heap, int(input()))

while len(heap) > 1:
    card_sum = heapq.heappop(heap) + heapq.heappop(heap)
    answer += card_sum
    heapq.heappush(heap, card_sum)

print(answer)