import sys
input = sys.stdin.readline

while True:
    data = list(map(int, input().split()))
    if data[0] == 0:
        break
    n = data[0]
    rects = data[1:] + [0]
    stack = []
    M = 0

    for i in range(n + 1):
        while stack and rects[stack[-1]] > rects[i]:
            h = rects[stack.pop()]

            if stack:
                width = i - stack[-1] - 1
            else:
                width = i
            M = max(M, h * width)
        stack.append(i)
    print(M)
        