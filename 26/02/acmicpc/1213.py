from collections import Counter
from sys import stdin
input = stdin.readline

name = input().rstrip()
count = Counter(name)
odd_chars = [ch for ch, c in count.items() if c%2 == 1]
if len(odd_chars) > 1:
    print("I'm Sorry Hansoo")
else:
    center = odd_chars[0] if odd_chars else ""
    left = []
    for ch in sorted(count.keys()):
        left.append(ch * (count[ch]//2))
    left = ''.join(left)
    answer = left+center+left[::-1]
    print(answer)