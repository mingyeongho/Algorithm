import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

label = 1
labels = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and labels[i][j] == 0:
            queue = deque([(i, j)])
            labels[i][j] = label
            while queue:
                x, y = queue.popleft()
                for dx, dy in direction:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        if graph[nx][ny] == 1 and labels[nx][ny] == 0:
                            labels[nx][ny] = label
                            queue.append((nx, ny))
            label += 1

dist = [[-1] * n for _ in range(n)]
queue = deque()

for i in range(n):
    for j in range(n):
        if labels[i][j] != 0:
            queue.append((i, j))
            dist[i][j] = 0

answer = sys.maxsize

while queue:
    x, y = queue.popleft()
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if labels[nx][ny] != 0 and labels[nx][ny] != labels[x][y]:
                answer = min(answer, dist[x][y] + dist[nx][ny])
            elif labels[nx][ny] == 0 and dist[nx][ny] == -1:
                labels[nx][ny] = labels[x][y]
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))

print(answer)
