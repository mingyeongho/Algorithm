import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 지훈이와 불이 빈 공간에 몇 분 후 도착하는지를 담을 이차원 배열 필요
f_dist = [[-1] * c for _ in range(r)]
j_dist = [[-1] * c for _ in range(r)]

# 지훈이와 불의 위치를 큐에 저장
j_queue = deque([])
f_queue = deque([])
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'J':
            j_queue.append((i, j))
            j_dist[i][j] = 0
        elif graph[i][j] == 'F':
            f_queue.append((i, j))
            f_dist[i][j] = 0

while f_queue:
    xp, yp = f_queue.popleft()
    for dx, dy in direction:
        nx, ny = xp + dx, yp + dy
        if not (0 <= nx < r and 0 <= ny < c):
            continue
        if graph[nx][ny] != '#' and f_dist[nx][ny] == -1:
            f_queue.append((nx, ny))
            f_dist[nx][ny] = f_dist[xp][yp] + 1

while j_queue:
    xp, yp = j_queue.popleft()
    for dx, dy in direction:
        nx, ny = xp + dx, yp + dy
        # 탈출 성공
        if not (0 <= nx < r and 0 <= ny < c):
            print(j_dist[xp][yp] + 1)
            exit(0)
        if graph[nx][ny] == '#' or j_dist[nx][ny] != -1:
            continue
        if f_dist[nx][ny] != -1 and f_dist[nx][ny] <= j_dist[xp][yp] + 1:
            continue
        j_queue.append((nx, ny))
        j_dist[nx][ny] = j_dist[xp][yp] + 1

print("IMPOSSIBLE")
