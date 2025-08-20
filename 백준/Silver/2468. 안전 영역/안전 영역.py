import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())
map = [list(map(int, input().split())) for _ in range(n)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
mx = 0


def bfs(map, x, y, visited, rain):
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
            if map[nx][ny] > rain:
                queue.append((nx, ny))
                visited[nx][ny] = True


for rain in range(101):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if map[i][j] > rain and not visited[i][j]:
                bfs(map, i, j, visited, rain)
                count += 1
    mx = max(mx, count)

print(mx)
