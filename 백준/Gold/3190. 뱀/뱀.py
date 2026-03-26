import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
graph = [[0] * N for _ in range(N)]

K = int(input().strip())
for _ in range(K):
    r, c = map(lambda x: int(x) - 1, input().split())
    graph[r][c] = 1

L = int(input().strip())
turns = {}
for _ in range(L):
    x, c = input().split()
    turns[int(x)] = c

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 동 남 서 북
direct = 0  # 현재 방향

snake = deque([(0, 0)])
graph[0][0] = 2  # 뱀

time = 0
while True:
    time += 1

    # 현재 머리
    xp, yp = snake[-1]

    dx, dy = direction[direct]
    nx, ny = xp + dx, yp + dy

    if not (0 <= nx < N and 0 <= ny < N) or graph[nx][ny] == 2:
        break

    if graph[nx][ny] == 1:
        graph[nx][ny] = 2
        snake.append((nx, ny))
    else:
        graph[nx][ny] = 2
        snake.append((nx, ny))
        tx, ty = snake.popleft()
        graph[tx][ty] = 0

    if time in turns:
        if turns[time] == "D":
            direct = (direct + 1) % 4
        else:
            direct = (direct - 1) % 4
print(time)
