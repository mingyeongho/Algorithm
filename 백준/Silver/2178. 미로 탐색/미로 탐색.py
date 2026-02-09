import sys
from collections import deque

input = sys.stdin.readline

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

R, C = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]  # 문자로 존재 '1', '0'


def bfs(R, C, graph, x, y, dist):
    dist[x][y] = 1
    deq = deque([(x, y)])

    while deq:
        xp, yp = deq.popleft()
        if xp == R - 1 and yp == C - 1:
            return dist[xp][yp]
        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < R and 0 <= ny < C):
                continue
            if graph[nx][ny] == "1" and dist[nx][ny] == -1:
                deq.append((nx, ny))
                dist[nx][ny] = dist[xp][yp] + 1
    return dist[R - 1][C - 1]


def solution(R, C, graph):
    dist = [[-1] * C for _ in range(R)]
    return bfs(R, C, graph, 0, 0, dist)


print(solution(R, C, graph))
