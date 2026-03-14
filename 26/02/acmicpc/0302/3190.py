import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
k = int(input())

# 0: 빈칸, 1: 사과, 2: 뱀
graph = [[0] * n for _ in range(n)]

for _ in range(k):
	row, col = map(int, input().split())
	graph[row - 1][col - 1] = 1

l = int(input())
moves = []
for _ in range(l):
	x, c = input().split()
	moves.append([int(x), c])

# 방향: 오른쪽(0), 아래(1), 왼쪽(2), 위(3)
dx = [0, 1, 0, -1]	# 행 변화
dy = [1, 0, -1, 0]	# 열 변화
direction = 0

snake = deque()
snake.append((0, 0))
graph[0][0] = 2	# 뱀 위치 표시

time = 0
move_idx = 0

while True:
	time += 1
	head_x, head_y = snake[-1]
	nx = head_x + dx[direction]
	ny = head_y + dy[direction]

	# 벽에 부딪힘
	if nx < 0 or nx >= n or ny < 0 or ny >= n:
		break

	# 자기 몸에 부딪힘
	if graph[nx][ny] == 2:
		break

	# 사과가 있음 → 머리만 늘리고 꼬리는 그대로 (길이 증가)
	if graph[nx][ny] == 1:
		graph[nx][ny] = 2
		snake.append((nx, ny))
	# 빈칸 → 머리 한 칸 이동 + 꼬리 줄이기
	else:
		graph[nx][ny] = 2
		snake.append((nx, ny))
		tail_x, tail_y = snake.popleft()
		graph[tail_x][tail_y] = 0

	# 방향 전환 시간인지 확인
	if move_idx < l and time == moves[move_idx][0]:
		if moves[move_idx][1] == 'L':
			direction = (direction - 1) % 4
		else:	# 'D'
			direction = (direction + 1) % 4
		move_idx += 1

print(time)