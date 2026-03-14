import math
from collections import Counter
from sys import stdin
input = stdin.readline

n = int(input())
data = list(int(input()) for _ in range(n))
data.sort()
answers = []
avg_raw = sum(data) / n
common = Counter(data).most_common()
max_freq = common[0][1]
candidate = [val for val, freq in common if freq == max_freq]
candidate.sort()
if len(candidate) > 1:
    most = candidate[1]
else:
    most = candidate[0]

if avg_raw >= 0:
	answers.append(int(avg_raw + 0.5))
else:
	answers.append(int(avg_raw - 0.5))
answers.append(data[n//2])
answers.append(most)
answers.append(data[-1]-data[0])
print(*answers, sep='\n')