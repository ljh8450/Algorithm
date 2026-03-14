import heapq

def solution(jobs):
	jobs = [[s ,l ,i] for i, (s, l) in enumerate()]
	heapq.heapify(jobs)
	n = len(jobs)
	total = 0
	done = 0
	ready = []
	time = 0
	while done < n:
		while ready and jobs[0][0] <= time:
			s, l, i = heapq.heappop(jobs)
			heapq.heappush(ready, (l, s, i))
		if ready:
			l, s, i = heapq.heappop(ready)
			time += l
			total += (time-s)
			done += 1
		else:
			s, l, i = heapq.heappop(jobs)
			time = s
			heapq.heappush(ready, (l, s, i))
	return total//n


jobs = [[0, 3], [1, 9], [3, 5]]	
print(solution(jobs))