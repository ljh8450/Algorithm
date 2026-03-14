def solution(tickets):
	tickets.sort()
	n = len(tickets)
	visited = [False] * n
	answer = []
	def dfs(curr, path):
		if len(path) == n+1:
			answer.append(path)
			return True
		for i in range(n):
			start, end = tickets[i]
			if not visited[i] and start == curr:
				visited[i] = True
				if dfs(end, path+[end]):
					return True
				visited[i] = False
		return False

	dfs("ICN", ["ICN"])
	return answer[0]

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
print(solution(tickets))