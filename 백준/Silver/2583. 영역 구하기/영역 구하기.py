import sys
from collections import deque
input = sys.stdin.readline

M, N, K = map(int, input().split())
graph = [[True] * N for _ in range(M)]
for _ in range(K):
    L_X, L_Y, R_X, R_Y = map(int, input().split())
    for i in range(L_Y, R_Y):
        for j in range(L_X, R_X):
            graph[i][j] = False

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False] * N for _ in range(M)]


def bfs(graph, x, y, visited) -> int:
    queue = deque([(x, y)])
    visited[x][y] = True
    area = 1
    while queue:
        xp, yp = queue.popleft()
        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < M and 0 <= ny < N):
                continue
            if not visited[nx][ny] and graph[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                area += 1
    return area


cnt = 0
areas = []
for i in range(M):
    for j in range(N):
        if not visited[i][j] and graph[i][j]:
            areas.append(bfs(graph, i, j, visited))
            cnt += 1

print(cnt)
print(*sorted(areas))
