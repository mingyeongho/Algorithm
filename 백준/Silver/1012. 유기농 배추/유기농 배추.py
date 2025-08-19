import sys
from collections import deque
input = sys.stdin.readline

T = int(input().strip())

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(graph, x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        xp, yp = queue.popleft()
        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < N and 0 <= ny < M):
                continue
            if not visited[nx][ny] and graph[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True


for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[-1] * M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1

    visited = [[False] * M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and not visited[i][j]:
                cnt += 1
                bfs(graph, i, j, visited)
    print(cnt)
