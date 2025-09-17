import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(graph, x, y, visited, empty):
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        xp, yp = queue.popleft()
        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < N and 0 <= ny < M):
                continue
            if graph[nx][ny] == 0 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
            if graph[nx][ny] == 1:
                empty[nx][ny] += 1


flag = True
for i in range(N):
    if graph[i].count(1) > 0:
        flag = False
if flag:
    print(0)
    exit(0)

year = 1
while True:
    visited = [[False] * M for _ in range(N)]
    empty = [[0] * M for _ in range(N)]

    bfs(graph, 0, 0, visited, empty)

    is_break = True
    for i in range(N):
        for j in range(M):
            if empty[i][j] > 1:
                graph[i][j] = 0
            if graph[i][j] == 1:
                is_break = False

    if is_break:
        break
    year += 1

print(year)
