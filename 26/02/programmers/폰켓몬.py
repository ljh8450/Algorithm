def solution(nums):
    length = len(nums)//2
    ponketmons = set(nums)
    threshold = len(ponketmons)
    answer = min(threshold, length)
    return answer

nums = [3,3,3,2,2,2]
print(solution(nums))