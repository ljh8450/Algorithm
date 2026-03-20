import sys
input = sys.stdin.readline

s = input().rstrip()
q = int(input())
n = len(s)

panels = {}

for ch in set(s):
    panels[ch] = [0] * (n+1)

for i in range(n):
    for ch in panels:
        panels[ch][i+1] = panels[ch][i]
    panels[s[i]][i+1] += 1

for _ in range(q):
    alpha, l, r = input().split()
    l = int(l)
    r = int(r)
    temp = 0

    if alpha not in panels:
        print(0)
    else:
        print(panels[alpha][r+1] - panels[alpha][l])