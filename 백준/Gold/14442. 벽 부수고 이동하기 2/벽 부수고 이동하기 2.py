import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dist = [[[-1] * M for _ in range(N)] for _ in range(K+1)]

queue = deque([(0, 0, 0)])
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
        if zp < K and graph[nx][ny] == 1 and dist[zp+1][nx][ny] == -1:  # 벽을 부술 수 있을 때
            queue.append((zp+1, nx, ny))
            dist[zp+1][nx][ny] = dist[zp][xp][yp] + 1
        elif dist[zp][nx][ny] == -1 and graph[nx][ny] == 0:
            queue.append((zp, nx, ny))
            dist[zp][nx][ny] = dist[zp][xp][yp] + 1

print(-1)
