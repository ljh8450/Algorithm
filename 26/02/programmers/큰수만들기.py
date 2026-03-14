def solution(number, k):
	stack = []

	for ch in number:
		while k > 0 and stack and stack[-1] < ch:
			stack.pop()
			k -= 1
		stack.append(ch)

	# 아직 k가 남았다면 뒤에서 제거
	if k > 0:
		stack = stack[:-k]

	return "".join(stack)