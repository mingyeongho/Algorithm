import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())
graph = [list(input().strip()) for _ in range(N)]
graph_rg = [["T" if graph[i][j] in (
    "R", "G") else "B" for j in range(N)] for i in range(N)]

visited = [[False] * N for _ in range(N)]
visited_rg = [[False] * N for _ in range(N)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(graph, x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        xp, yp = queue.popleft()
        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            if graph[x][y] == graph[nx][ny] and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True


cnt = 0
cnt_rg = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            cnt += 1
            bfs(graph, i, j, visited)
        if not visited_rg[i][j]:
            cnt_rg += 1
            bfs(graph_rg, i, j, visited_rg)

print(cnt)
print(cnt_rg)
