import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, list(input().strip()))) for _ in range(n)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

visited = [[[-1] * m for _ in range(n)] for _ in range(2)]
visited[0][0][0] = 1
queue = deque([(0, 0, 0)])


while queue:
    zp, xp, yp = queue.popleft()
    if xp == n-1 and yp == m-1:
        print(visited[zp][xp][yp])
        exit(0)
    for dx, dy in direction:
        nx, ny = xp + dx, yp + dy
        if not (0 <= nx < n and 0 <= ny < m):
            continue
        # 이동할 좌표가 벽이고 벽을 한번도 부수지 않았을 때
        if graph[nx][ny] == 1 and zp == 0:
            queue.append((1, nx, ny))
            visited[1][nx][ny] = visited[0][xp][yp] + 1
        # 이동할 좌표가 빈 공간이고 한번도 방문하지 않았을 때
        if graph[nx][ny] == 0 and visited[zp][nx][ny] == -1:
            queue.append((zp, nx, ny))
            visited[zp][nx][ny] = visited[zp][xp][yp] + 1
print(-1)
