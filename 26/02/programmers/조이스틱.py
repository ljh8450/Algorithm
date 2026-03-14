def solution(name):
	n = len(name)

	# 1) 위/아래 조작(각 글자 바꾸기) 최소 합
	vertical = 0
	for ch in name:
		up = ord(ch) - ord('A')
		down = ord('Z') - ord(ch) + 1
		vertical += min(up, down)

	# 2) 좌/우 이동 최소
	# 기본은 끝까지 오른쪽으로 가는 경우: n-1
	move = n - 1

	for i in range(n):
		# i 다음부터 연속된 'A' 구간 끝 찾기
		j = i + 1
		while j < n and name[j] == 'A':
			j += 1

		# 오른쪽으로 i까지 갔다가(=i), 뒤로 돌아가서(=i) 나머지 처리
		# 또는 반대로 먼저 왼쪽(뒤)로 갔다가 처리
		move = min(move,
			2 * i + (n - j),
			i + 2 * (n - j)
		)

	return vertical + move


name = "JEROEN"
print(solution(name))