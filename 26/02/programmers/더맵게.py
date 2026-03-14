import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) > 1 and scoville[0] < K:
        food1 = heapq.heappop(scoville)
        food2 = heapq.heappop(scoville)
        new_food = food1 + food2*2
        heapq.heappush(scoville, new_food)
        answer += 1
    if scoville[0] < K:
        return -1
    else:
        return answer

scoville=[1, 2, 3, 9, 10, 12]
k=7
print(solution(scoville, k))