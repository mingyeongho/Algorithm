import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]

direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def func(R, C, graph) -> str | int:
    dist = [[[-1, -1] for _ in range(C)] for _ in range(R)]
    ji = deque()
    fire = deque()
    for i in range(R):
        for j in range(C):
            if graph[i][j] == "F":
                fire.append((i, j))
                dist[i][j][1] = 0
            elif graph[i][j] == "J":
                ji.append((i, j))
                dist[i][j][0] = 0
    
    while fire:
        xp, yp = fire.popleft()
        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < R and 0 <= ny < C):
                continue
            if dist[nx][ny][1] == -1 and graph[nx][ny] == ".":
                dist[nx][ny][1] = dist[xp][yp][1] + 1
                fire.append((nx, ny))
                
    while ji:
        xp, yp = ji.popleft()
        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < R and 0 <= ny < C):
                # 탈출
                return dist[xp][yp][0] + 1
            if dist[nx][ny][0] == -1 and graph[nx][ny] == "." and (dist[nx][ny][1] == -1 or dist[nx][ny][1] > dist[xp][yp][0] + 1):
                dist[nx][ny][0] = dist[xp][yp][0] + 1
                ji.append((nx, ny))
    
    return "IMPOSSIBLE"

print(func(R, C, graph))