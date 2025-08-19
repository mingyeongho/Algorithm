import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False] * m for _ in range(n)]


def bfs(x, y):
  queue = deque([(x, y)])
  visited[x][y] = True
  while queue:
    xp, yp = queue.popleft()
    for dx, dy in direction:
      nx, ny = xp + dx, yp + dy
      if not (0 <= nx < n and 0 <= ny < m):
        continue
      if graph[nx][ny] == "0" or visited[nx][ny]:
        continue
      queue.append((nx, ny))
      visited[nx][ny] = True
      graph[nx][ny] = int(graph[xp][yp]) + 1


bfs(0, 0)
print(graph[n - 1][m - 1])
