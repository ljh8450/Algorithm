from collections import deque

def solution(game_board, table):
	n = len(game_board)
	
	# 4방향
	dx = [1, -1, 0, 0]
	dy = [0, 0, 1, -1]
	
	def bfs_collect(board, start_x, start_y, target):
		"""
		board에서 값이 target인 칸들로 이루어진 하나의 도형(연결 컴포넌트)을
		BFS로 찾아서, 그 좌표들을 리스트로 반환.
		"""
		q = deque()
		q.append((start_x, start_y))
		visited[start_x][start_y] = True
		cells = [(start_x, start_y)]
		
		while q:
			x, y = q.popleft()
			for k in range(4):
				nx = x + dx[k]
				ny = y + dy[k]
				if 0 <= nx < n and 0 <= ny < n:
					if not visited[nx][ny] and board[nx][ny] == target:
						visited[nx][ny] = True
						q.append((nx, ny))
						cells.append((nx, ny))
		return cells
	
	def normalize(shape):
		"""
		도형의 좌표들을 (x,y) 리스트로 받고,
		가장 왼쪽 위가 (0,0)이 되게 평행이동 후 정렬해서 반환.
		"""
		min_x = min(x for x, y in shape)
		min_y = min(y for x, y in shape)
		norm = sorted((x - min_x, y - min_y) for x, y in shape)
		return norm
	
	def rotate(shape):
		"""
		도형을 원점 기준으로 시계 방향 90도 회전.
		(회전 후 다시 normalize 해서 위치 고정)
		shape는 이미 normalize된 좌표 리스트라고 가정.
		"""
		rotated = [(y, -x) for x, y in shape]
		return normalize(rotated)
	
	# 1) game_board에서 빈칸(0) 도형들 추출
	visited = [[False] * n for _ in range(n)]
	empty_shapes = []
	for i in range(n):
		for j in range(n):
			if not visited[i][j] and game_board[i][j] == 0:
				cells = bfs_collect(game_board, i, j, 0)
				empty_shapes.append(normalize(cells))
	
	# 2) table에서 퍼즐 조각(1) 도형들 추출
	visited = [[False] * n for _ in range(n)]
	piece_shapes = []
	for i in range(n):
		for j in range(n):
			if not visited[i][j] and table[i][j] == 1:
				cells = bfs_collect(table, i, j, 1)
				piece_shapes.append(normalize(cells))
	
	answer = 0
	
	# 3) 빈칸 하나씩 보면서, 맞는 조각 찾기
	for empty in empty_shapes:
		empty_size = len(empty)
		found_idx = -1
		
		for idx, piece in enumerate(piece_shapes):
			if len(piece) != empty_size:
				continue
			
			rotated = piece
			ok = False
			# 4번 회전하면서 모양이 같아지는지 확인
			for _ in range(4):
				if rotated == empty:
					ok = True
					break
				rotated = rotate(rotated)
			
			if ok:
				found_idx = idx
				break
		
		# 맞는 조각을 찾으면, 그 조각을 사용하고 answer에 칸 수 더하기
		if found_idx != -1:
			answer += empty_size
			piece_shapes.pop(found_idx)  # 사용한 조각 제거
	
	return answer

game_board, table = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]], [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
print(solution(game_board, table))