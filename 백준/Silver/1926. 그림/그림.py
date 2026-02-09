import sys
from collections import deque

input = sys.stdin.readline

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

R, C = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]


def bfs(R, C, graph, x, y, visited):
    visited[x][y] = True
    deq = deque([(x, y)])
    area = 1  # 그림의 넓이

    while deq:
        xp, yp = deq.popleft()
        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < R and 0 <= ny < C):
                continue
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                deq.append((nx, ny))
                visited[nx][ny] = True
                area += 1
    return area


def solution(R, C, graph):
    visited = [[False] * C for _ in range(R)]
    cnt = 0  # 그림의 개수
    mx_area = 0  # 가장 넓은 그림

    for i in range(R):
        for j in range(C):
            if graph[i][j] == 1 and not visited[i][j]:
                area = bfs(R, C, graph, i, j, visited)
                cnt += 1
                mx_area = max(mx_area, area)
    return [cnt, mx_area]


print(*solution(R, C, graph), sep="\n")
