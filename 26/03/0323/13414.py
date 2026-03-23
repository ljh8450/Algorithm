import sys
input = sys.stdin.readline

k, l = map(int, input().split())

ready = dict()
for i in range(l):
    person = input().rstrip()
    ready[person] = i

result = sorted(ready.items(), key=lambda x: x[1])

count = 0
for p in result:
    if count == k:
        break
    print(p[0])
    count += 1
