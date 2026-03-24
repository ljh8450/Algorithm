import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temperatures = list(map(int, input().split()))

current = sum(temperatures[:k])
answer = current

for i in range(k, n):
    current += temperatures[i] - temperatures[i-k]
    answer = max(answer, current)

print(answer)