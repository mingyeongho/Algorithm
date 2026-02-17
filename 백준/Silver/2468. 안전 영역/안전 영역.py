import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
graph = [list(map(int, input().split())) for _ in range(N)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def BFS(H, N, graph, x, y, visited):
    visited[x][y] = True
    deq = deque([(x, y)])

    while deq:
        xp, yp = deq.popleft()
        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            if graph[nx][ny] > H and not visited[nx][ny]:
                deq.append((nx, ny))
                visited[nx][ny] = True


def solution(N, graph):
    mx = -1
    for k in range(101):  # 비의 높이
        visited = [[False] * N for _ in range(N)]
        area = 0

        for i in range(N):
            for j in range(N):
                if graph[i][j] > k and not visited[i][j]:
                    BFS(k, N, graph, i, j, visited)
                    area += 1
        if area == 0:
            break
        mx = max(mx, area)
    return mx


print(solution(N, graph))
