def solution(m, n, puddles):
	MOD = 1_000_000_007
	
	dp = [[0] * (m + 1) for _ in range(n + 1)]
	block = [[False] * (m + 1) for _ in range(n + 1)]
	
	for x, y in puddles:
		if 1 <= x <= m and 1 <= y <= n:
			block[y][x] = True
	
	dx, dy = [1, 0], [0, 1]  # 오른쪽, 아래
	dp[1][1] = 1
	
	for y in range(1, n + 1):
		for x in range(1, m + 1):
			# 현재 칸이 물이거나, 시작점은 전파만 담당
			if block[y][x]:
				continue
			for k in range(2):
				nx, ny = x + dx[k], y + dy[k]
				if 1 <= nx <= m and 1 <= ny <= n and not block[ny][nx]:
					dp[ny][nx] = (dp[ny][nx] + dp[y][x]) % MOD
	
	return dp[n][m]

m, n, puddles = 4, 3, [[2, 2]]
print(solution(m, n, puddles))