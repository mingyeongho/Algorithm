import sys
from collections import deque
import heapq
input = sys.stdin.readline

N = int(input().strip())
graph = [list(map(int, input().split())) for _ in range(N)]

s_x, s_y = 0, 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            s_x, s_y = i, j
            graph[i][j] = 0

direction = [(-1, 0), (0, -1), (0, 1), (1, 0)]

size = 2  # 현재 아기 상어의 크기
eat = 0


def bfs(graph, x, y):
    queue = deque([(x, y)])
    visited = [[False] * N for _ in range(N)]
    visited[x][y] = True
    depth = 0
    can_eat = []

    while queue:
        if len(can_eat) > 0:
            ax, ay = heapq.heappop(can_eat)
            graph[ax][ay] = 0
            return (ax, ay, depth)
        for _ in range(len(queue)):
            xp, yp = queue.popleft()
            for dx, dy in direction:
                nx, ny = xp + dx, yp + dy
                if not (0 <= nx < N and 0 <= ny < N):
                    continue
                if graph[nx][ny] <= size and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    if 0 < graph[nx][ny] < size:
                        heapq.heappush(can_eat, (nx, ny))
        depth += 1
    return (-1, -1, -1)


answer = 0
while True:
    nxt_x, nxt_y, dist = bfs(graph, s_x, s_y)

    if nxt_x == -1:
        print(answer)
        break

    eat += 1
    if eat == size:
        size += 1
        eat = 0

    s_x, s_y = nxt_x, nxt_y
    answer += dist
