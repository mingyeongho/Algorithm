import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
graph = [list(input().strip()) for _ in range(n)]

visited_y = [[False] * n for _ in range(n)]  # 적록색약인 사람
visited_n = [[False] * n for _ in range(n)]  # 적록색약이 아닌 사람

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

graph_y = [[cell if cell != 'G' else 'R' for cell in row] for row in graph]


def bfs(graph, x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        xp, yp = queue.popleft()
        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] != graph[xp][yp]:
                continue
            queue.append((nx, ny))
            visited[nx][ny] = True


count = [0, 0]
for i in range(n):
    for j in range(n):
        if not visited_n[i][j]:
            bfs(graph, i, j, visited_n)
            count[0] += 1
        if not visited_y[i][j]:
            bfs(graph_y, i, j, visited_y)
            count[1] += 1

print(*count)
