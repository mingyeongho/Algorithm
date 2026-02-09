import sys
from collections import deque

input = sys.stdin.readline
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

R, C = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]


def solution(R, C, graph):
    fire = deque([])
    fire_dist = [[-1] * C for _ in range(R)]
    jihun = deque([])
    jihun_dist = [[-1] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if graph[i][j] == "J":
                jihun.append((i, j))
                jihun_dist[i][j] = 0
            if graph[i][j] == "F":
                fire.append((i, j))
                fire_dist[i][j] = 0

    while fire:
        xp, yp = fire.popleft()
        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < R and 0 <= ny < C):
                continue
            if (graph[nx][ny] == "." or graph[nx][ny] == "J") and fire_dist[nx][
                ny
            ] == -1:
                fire.append((nx, ny))
                fire_dist[nx][ny] = fire_dist[xp][yp] + 1

    while jihun:
        xp, yp = jihun.popleft()
        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < R and 0 <= ny < C):
                # 탈출
                return jihun_dist[xp][yp] + 1
            if (
                graph[nx][ny] == "."
                and jihun_dist[nx][ny] == -1
                and (
                    fire_dist[nx][ny] == -1
                    or fire_dist[nx][ny] > jihun_dist[xp][yp] + 1
                )
            ):
                jihun.append((nx, ny))
                jihun_dist[nx][ny] = jihun_dist[xp][yp] + 1
    return "IMPOSSIBLE"


print(solution(R, C, graph))
