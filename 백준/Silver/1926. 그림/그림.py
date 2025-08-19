import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(graph, x, y, visited) -> int:
    queue = deque([(x, y)])
    visited[x][y] = True
    area = 1
    while queue:
        xp, yp = queue.popleft()
        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < N and 0 <= ny < M):
                continue
            if not visited[nx][ny] and graph[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
                area += 1
    return area


count = 0
mx = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j] and graph[i][j] == 1:
            count += 1
            area = bfs(graph, i, j, visited)
            mx = max(mx, area)

print(count)
print(mx)
