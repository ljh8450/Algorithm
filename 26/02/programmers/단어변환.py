from collections import deque
def solution(begin, target, words):
    def bfs(begin, k):
        if target not in words:
            return 0
        queue = deque([(begin, k)])
        while queue:
            comparator, k = queue.popleft()
            if comparator == target:
                return k
            for i in range(n):
                if not visited[i]:
                    word = words[i]
                    if sum(1 for a, b in zip(word, comparator) if a != b) == 1:
                        queue.append((word, k+1))
                        visited[i] = True
                    
        return -1
    n = len(words)
    visited = [False] * n
    
    answer = bfs(begin, 0)
    return answer

begin, target, words = "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))