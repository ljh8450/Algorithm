def solution(money):
    n = len(money)
    if n == 3:
        return max(money)
    def find(arr):
        m = len(arr)
        if m == 1:
            return arr[0]
        dp1 = arr[0]
        dp2 = max(arr[0], arr[1])
        for i in range(2, m):
            dp1, dp2 = dp2, max(dp2, dp1+arr[i])
        return dp2
    
    c1 = find(money[:-1])
    c2 = find(money[1:])
    return max(c1, c2)

money = [1, 2, 3, 1]
print(solution(money))