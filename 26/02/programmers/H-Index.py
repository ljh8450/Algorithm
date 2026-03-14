def solution(citations):
    answer = 0
    n = len(citations)
    citations = list(sorted(citations, reverse=True))
    for i in range(1, n+1):
        cnt = 0
        for j in range(n):
            if i <= citations[j]:
                cnt += 1
            if cnt == i:
                answer = cnt
                break
    return answer

citations = [3, 0, 6, 1, 5]
print(solution(citations))