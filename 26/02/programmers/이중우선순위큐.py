import heapq
def solution(operations):
    min_heap = []
    max_heap = []
    n = len(operations)
    visited = [False] * n
    
    for i, operation in enumerate(operations):
        opeartor, num = operation.split()
        num = int(num)
        if opeartor == 'I':
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
            visited[i] = True
        elif opeartor == 'D':
            if num == -1:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
            elif num == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    if min_heap:
        minimum = min_heap[0][0]
    else:
        return [0, 0]
    if max_heap:
        maximum = -max_heap[0][0]
        
    return [maximum, minimum]

operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(operations))