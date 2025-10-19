import sys
from collections import deque
input = sys.stdin.readline

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(graph, x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    meet = 0
    while queue:
        xp, yp = queue.popleft()
        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < N and 0 <= ny < M):
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] == 'X':
                continue
            if graph[nx][ny] == 'P':
                meet += 1
            visited[nx][ny] = True
            queue.append((nx, ny))
    return meet


N, M = map(int, input().split())
graph = [list(input().strip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

do = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'I':
            do.append((i, j))
            graph[i][j] = 'X'
            break
    if len(do) > 0:
        break

meet = bfs(graph, do[0][0], do[0][1], visited)
print(meet if meet > 0 else 'TT')
