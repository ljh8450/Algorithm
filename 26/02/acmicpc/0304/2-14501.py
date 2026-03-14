import sys
input = sys.stdin.readline

n = int(input())
t, p = [], []
for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

dp = [0] * (n+1)
for i in range(n-1, -1, -1):
    nxt = i + t[i]
    if nxt <= n:
        dp[i] = max(dp[i+1], p[i] + dp[nxt]) 
    else:
        dp[i] = dp[i+1]
print(dp[0])