import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()
an = len(a)
bn = len(b)
dp = [[0 for _ in range(bn+1)] for _ in range(an+1)]

for i in range(1, an+1):
    for j in range(1, bn+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[an][bn])