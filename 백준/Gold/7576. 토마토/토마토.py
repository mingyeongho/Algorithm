import sys
from collections import deque
input = sys.stdin.readline

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]

def func(N, M, graph) -> int:
    dist = [[-1 for _ in range(N)] for _ in range(M)]
    
    queue = deque()
    
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                queue.append((i, j))
                dist[i][j] = 0
    
    while queue:
        xp, yp = queue.popleft()
        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < M and 0 <= ny < N):
                continue
            if graph[nx][ny] == 0 and dist[nx][ny] == -1:
                queue.append((nx, ny))
                dist[nx][ny] = dist[xp][yp] + 1
    
    mx = 0
    for i in range(M):
        for j in range(N):
            if dist[i][j] == -1 and graph[i][j] == 0:
                return -1
        mx = max(mx, max(dist[i]))
    return mx
    
print(func(N, M, graph))