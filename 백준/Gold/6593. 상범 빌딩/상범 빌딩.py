import sys
from collections import deque
input = sys.stdin.readline

direction = [(-1, 0, 0), (1, 0, 0), (0, -1, 0),
             (0, 1, 0), (0, 0, -1), (0, 0, 1)]


def bfs(graph, z, x, y, visited, l, r, c):
    queue = deque([(z, x, y)])
    visited[z][x][y] = 0

    while queue:
        zp, xp, yp = queue.popleft()
        if graph[zp][xp][yp] == 'E':
            return 'Escaped in ' + str(visited[zp][xp][yp]) + ' minute(s).'
        for dz, dx, dy in direction:
            nz, nx, ny = zp + dz, xp + dx, yp + dy
            if not (0 <= nz < l and 0 <= nx < r and 0 <= ny < c):
                continue
            if visited[nz][nx][ny] == -1 and graph[nz][nx][ny] != '#':
                queue.append((nz, nx, ny))
                visited[nz][nx][ny] = visited[zp][xp][yp] + 1

    return 'Trapped!'


def solution(graph, l, r, c, visited):
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if graph[i][j][k] == 'S':
                    return bfs(graph, i, j, k, visited, l, r, c)


while True:
    l, r, c = map(int, input().split())  # l: 층 수, r: 행, c: 열

    if l == 0 and r == 0 and c == 0:
        break

    graph = []
    for _ in range(l):
        row = [list(input().strip()) for _ in range(r)]
        graph.append(row)
        input().strip()

    visited = [[[-1] * c for _ in range(r)] for _ in range(l)]
    print(solution(graph, l, r, c, visited))
