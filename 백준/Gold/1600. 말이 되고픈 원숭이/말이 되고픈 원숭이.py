import sys
from collections import deque

input = sys.stdin.readline

K = int(input().strip())
W, H = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(H)]

direction_knight = [
    (-2, 1),
    (-1, 2),
    (1, 2),
    (2, 1),
    (2, -1),
    (1, -2),
    (-1, -2),
    (-2, -1),
]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def solution(K, R, C, graph):
    dist = [[[-1] * C for _ in range(R)] for _ in range(K + 1)]
    q = deque([(0, 0, 0)])  # (k, i, j)
    dist[0][0][0] = 0

    while q:
        zp, xp, yp = q.popleft()
        if xp == R - 1 and yp == C - 1:
            return dist[zp][xp][yp]
        if zp < K:
            for dx, dy in direction_knight:
                nx, ny = xp + dx, yp + dy
                if not (0 <= nx < R and 0 <= ny < C):
                    continue
                if graph[nx][ny] == 0 and dist[zp + 1][nx][ny] == -1:
                    q.append((zp + 1, nx, ny))
                    dist[zp + 1][nx][ny] = dist[zp][xp][yp] + 1
        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < R and 0 <= ny < C):
                continue
            if graph[nx][ny] == 0 and dist[zp][nx][ny] == -1:
                q.append((zp, nx, ny))
                dist[zp][nx][ny] = dist[zp][xp][yp] + 1
    return -1


print(solution(K, H, W, graph))
