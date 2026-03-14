import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [0] * n

for i in range(n):
    dp[i] = a[i]
    for j in range(n):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + a[i])

print(max(dp))