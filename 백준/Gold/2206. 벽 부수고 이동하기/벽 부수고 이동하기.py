import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dist = [[[-1] * M for _ in range(N)] for _ in range(2)]  # z, x, y
queue = deque([(0, 0, 0)])  # z, x, y
dist[0][0][0] = 1
while queue:
    zp, xp, yp = queue.popleft()
    if xp == N-1 and yp == M-1:
        print(dist[zp][xp][yp])
        exit(0)
    for dx, dy in direction:
        nx, ny = xp + dx, yp + dy
        if not (0 <= nx < N and 0 <= ny < M):
            continue
        # 이동할 곳이 벽이면서 내가 벽을 부술 수 있으면
        if graph[nx][ny] == 1 and zp == 0:
            queue.append((1, nx, ny))
            dist[1][nx][ny] = dist[zp][xp][yp] + 1
        # 이동할 곳이 이동할 수 있으면서 아직 방문하지 않았다면
        if graph[nx][ny] == 0 and dist[zp][nx][ny] == -1:
            queue.append((zp, nx, ny))
            dist[zp][nx][ny] = dist[zp][xp][yp] + 1
print(-1)
