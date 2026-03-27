import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

red, blue, hole = [(0, 0), (0, 0), (0, 0)]

for i in range(N):
    for j in range(M):
        if board[i][j] == "R":
            red = (i, j)
        elif board[i][j] == "B":
            blue = (i, j)
        elif board[i][j] == "O":
            hole = (i, j)

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북 동 남 서


def move(x, y, dx, dy):
    cnt = 0
    while True:
        nx, ny = x + dx, y + dy
        if board[nx][ny] == "#":
            break
        x, y = nx, ny
        cnt += 1
        if board[x][y] == "O":
            break
    return x, y, cnt


def bfs(graph, rx, ry, bx, by):
    # (빨간, 파란, depth)
    q = deque([(rx, ry, bx, by, 0)])
    visited = set()
    visited.add((rx, ry, bx, by))

    while q:
        rxp, ryp, bxp, byp, depth = q.popleft()

        if depth >= 10:
            return -1

        for dx, dy in direction:
            nrx, nry, rc = move(rxp, ryp, dx, dy)
            nbx, nby, bc = move(bxp, byp, dx, dy)

            if graph[nbx][nby] == "O":
                continue

            if graph[nrx][nry] == "O":
                return depth + 1

            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy

            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                q.append((nrx, nry, nbx, nby, depth + 1))

    return -1


print(bfs(board, *red, *blue))
