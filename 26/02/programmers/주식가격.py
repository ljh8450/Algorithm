def solution(prices):
	n = len(prices)
	answer = [0 for _ in range(n)]
	stack = []
	for i, price in enumerate(prices):
		while stack and prices[stack[-1]] > price:
			j = stack.pop()
			answer[j] = i-j 
		stack.append(i)
	while stack:
		j = stack.pop()
		answer[j] = n-j-1
	return answer

prices=[1, 2, 3, 2, 3]
print(solution(prices))