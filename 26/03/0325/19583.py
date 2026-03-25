import sys

S, E, Q = input().split()
enter = set()
leave = set()

for line in sys.stdin:
    time, name = line.split()
	
    if time <= S:
        enter.add(name)
    
    if E <= time <= Q:
        if name in enter:
            leave.add(name)

print(len(leave))