from math import inf
def solution(arr):
    n = len(arr)
    nums = []
    ops = []
    len_op = n//2
    INF = inf
    for i in range(n):
        if i%2 == 0: # nums
            nums.append(int(arr[i]))
        else: # ops
            ops.append(arr[i])
    n = len(nums)
    max_dp = [[-INF]*n for _ in range(n)]
    min_dp = [[INF]*n for _ in range(n)]
    for i in range(n):
        max_dp[i][i] = nums[i]
        min_dp[i][i] = nums[i]

    for length in range(1, n): # 1~n-1 -> 구간 길이
        for i in range(n-length): # i는 구간 시작, j는 구간 끝
            j = i+length
            for k in range(i,j): # 각각의 구간을 k를 기준으로 다시 탐색하며 최대, 최소를 구함
                op = ops[k]
                if op == '+': # 최대: 최대+최대 / 최소: 최소+최소
                    cand_max = max_dp[i][k] + max_dp[k+1][j]
                    cand_min = min_dp[i][k] + min_dp[k+1][j]
                if op == '-': # 최대: 최대-최소 / 최소: 최소-최대
                    cand_max = max_dp[i][k] - min_dp[k+1][j]
                    cand_min = min_dp[i][k] - max_dp[k+1][j]
                max_dp[i][j] = max(max_dp[i][j], cand_max)
                min_dp[i][j] = min(min_dp[i][j], cand_min)
    return max_dp[0][n-1]

arr = ["1", "-", "3", "+", "5", "-", "8"]
print(solution(arr))
