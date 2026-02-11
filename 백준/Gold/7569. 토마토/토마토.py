import sys
from collections import deque

input = sys.stdin.readline


direction = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]


def solution(R, C, H, graph):
    tomatoes = deque([])
    dist = [[[-1] * C for _ in range(R)] for _ in range(H)]

    for k in range(H):
        for i in range(R):
            for j in range(C):
                if graph[k][i][j] == 1:
                    tomatoes.append((k, i, j))
                    dist[k][i][j] = 0
                elif graph[k][i][j] == -1:
                    dist[k][i][j] = 0

    while tomatoes:
        zp, xp, yp = tomatoes.popleft()
        for dz, dx, dy in direction:
            nz, nx, ny = zp + dz, xp + dx, yp + dy
            if not (0 <= nz < H and 0 <= nx < R and 0 <= ny < C):
                continue
            if dist[nz][nx][ny] == -1:
                dist[nz][nx][ny] = dist[zp][xp][yp] + 1
                tomatoes.append((nz, nx, ny))

    mx = -1
    for k in range(H):
        for i in range(R):
            for j in range(C):
                if dist[k][i][j] == -1:
                    return -1
                mx = max(mx, dist[k][i][j])
    return mx


M, N, H = map(int, input().split())  # M: 가로, N: 세로, H: 높이
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

print(solution(N, M, H, graph))
