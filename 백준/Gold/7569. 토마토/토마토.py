import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(N)]for _ in range(H)]

dist = [[[-1] * M for _ in range(N)] for _ in range(H)]
direction = [(-1, 0, 0), (1, 0, 0), (0, -1, 0),
             (0, 1, 0), (0, 0, -1), (0, 0, 1)]
queue = deque([])
for k in range(H):
    for i in range(N):
        for j in range(M):
            if dist[k][i][j] == -1 and graph[k][i][j] == 1:
                queue.append((k, i, j))
                dist[k][i][j] = 0

while queue:
    zp, xp, yp = queue.popleft()
    for dz, dx, dy in direction:
        nz, nx, ny = zp + dz, xp + dx, yp + dy
        if not (0 <= nz < H and 0 <= nx < N and 0 <= ny < M):
            continue
        if dist[nz][nx][ny] == -1 and graph[nz][nx][ny] == 0:
            queue.append((nz, nx, ny))
            dist[nz][nx][ny] = dist[zp][xp][yp] + 1

mx = 0
for k in range(H):
    for i in range(N):
        for j in range(M):
            if dist[k][i][j] == -1 and graph[k][i][j] == 0:
                print(-1)
                exit(0)
            mx = max(mx, dist[k][i][j])
print(mx)
