import sys
from collections import deque

input = sys.stdin.readline

boards = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
direction = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
answer = float("Inf")  # 최소 이동 횟수
maze = [None] * 5
visited_maze = [False] * 5


def bfs(graph, z, x, y, dist):
    q = deque([(z, x, y)])
    dist[z][x][y] = 0

    while q:
        zp, xp, yp = q.popleft()
        if zp == 4 and xp == 4 and yp == 4:
            return dist[zp][xp][yp]
        for dz, dx, dy in direction:
            nz, nx, ny = zp + dz, xp + dx, yp + dy
            if not (0 <= nz < 5 and 0 <= nx < 5 and 0 <= ny < 5):
                continue
            if graph[nz][nx][ny] == 1 and dist[nz][nx][ny] == -1:
                q.append((nz, nx, ny))
                dist[nz][nx][ny] = dist[zp][xp][yp] + 1
    return -1


def rotate(board: list[list[int]]):
    return [list(row) for row in zip(*board[::-1])]


# 완성된 미로를 회전시키며 최종 미로를 만드는 함수
def make_final_maze(k):
    global maze, answer
    if k == 5:
        if maze[0][0][0] == 1:
            dist = [[[-1] * 5 for _ in range(5)] for _ in range(5)]
            d = bfs(maze, 0, 0, 0, dist)
            if d > -1:
                answer = min(answer, d)
        return

    for _ in range(4):
        make_final_maze(k + 1)
        maze[k] = rotate(maze[k])


# 5개의 판을 쌓아서 미로를 만드는 함수
def make_maze(k):
    if k == 5:
        make_final_maze(0)
        return
    for i in range(5):
        if not visited_maze[i]:
            maze[k] = boards[i]
            visited_maze[i] = True
            make_maze(k + 1)
            visited_maze[i] = False


make_maze(0)

print(answer if answer != float("Inf") else -1)
