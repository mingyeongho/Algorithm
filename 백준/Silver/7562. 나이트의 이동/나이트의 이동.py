import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())

direction = [(-2, 1), (-1, 2), (1, 2), (2, 1),
             (2, -1), (1, -2), (-1, -2), (-2, -1)]


def bfs(x, y, end_x, end_y, dist, l):
    queue = deque([(x, y)])
    dist[x][y] = 0
    while queue:
        xp, yp = queue.popleft()
        if xp == end_x and yp == end_y:
            return dist[xp][yp]
        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < l and 0 <= ny < l):
                continue
            if dist[nx][ny] != -1:
                continue
            queue.append((nx, ny))
            dist[nx][ny] = dist[xp][yp] + 1
    return 0


for _ in range(n):
    l = int(input().rstrip())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    dist = [[-1] * l for _ in range(l)]
    print(bfs(start_x, start_y, end_x, end_y, dist, l))
