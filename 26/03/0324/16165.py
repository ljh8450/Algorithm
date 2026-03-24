import sys
input = sys.stdin.readline

n, m = map(int, input().split())

groups, members = [], [[] for _ in range(n)]

for i in range(n):
    group = input().rstrip()
    k = int(input())
    groups.append(group)
    for _ in range(k):
        members[i].append(input().rstrip())
    members[i].sort()
    
for _ in range(m):
    where = input().rstrip()
    quiz = int(input())
    if quiz == 0:
        for i, group in enumerate(groups):
            if where == group:
                print(*members[i], sep='\n')
    if quiz == 1:
        for i, member in enumerate(members):
            if where in member:
                print(groups[i])