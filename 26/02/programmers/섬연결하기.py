def solution(n, costs):
	# 1. 비용 기준으로 정렬 (가장 싼 다리부터 보기)
	costs.sort(key=lambda x: x[2])

	# 2. Union-Find 준비 (각 섬이 어느 그룹에 속했는지 기록)
	parent = [i for i in range(n)]

	def find(x):
		if parent[x] != x:
			parent[x] = find(parent[x])
		return parent[x]

	def union(a, b):
		ra, rb = find(a), find(b)
		# 이미 같은 그룹이면 이 다리를 선택하면 사이클 → 선택 X
		if ra == rb:
			return False
		# 다른 그룹이면 두 그룹을 합침 → 이 다리는 선택
		parent[rb] = ra
		return True

	answer = 0
	edge_count = 0

	# 3. 가장 싼 다리부터 하나씩 보면서 그리디하게 선택
	for a, b, cost in costs:
		if union(a, b):       # 사이클 안 생기면
			answer += cost    # 비용 더하고
			edge_count += 1   # 선택한 다리 수 +1
			if edge_count == n - 1:
				break         # 섬이 n개면 다리는 n-1개면 충분

	return answer