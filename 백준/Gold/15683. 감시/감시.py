import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 0: 북, 1: 동, 2: 남, 3: 서
direction: list[list[list[int]]] = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]],
]

board = [[False] * M for _ in range(N)]
cctvs: list[tuple[int, int, int]] = []
for i in range(N):
    for j in range(M):
        if 1 <= graph[i][j] <= 5:
            cctvs.append((graph[i][j], i, j))
        elif graph[i][j] == 6:
            board[i][j] = True

mn = N * M


def fill(x: int, y: int, direct: list[int]):
    temp = []  # 어떤 값을 바꿨는지 기억하는 배열, (i, j)
    for d in direct:
        if d == 0:
            for i in range(x, -1, -1):
                if graph[i][y] == 6:
                    break
                if not board[i][y]:
                    board[i][y] = True
                    temp.append((i, y))
        elif d == 1:
            for j in range(y, M):
                if graph[x][j] == 6:
                    break
                if not board[x][j]:
                    board[x][j] = True
                    temp.append((x, j))
        elif d == 2:
            for i in range(x, N):
                if graph[i][y] == 6:
                    break
                if not board[i][y]:
                    board[i][y] = True
                    temp.append((i, y))
        else:
            for j in range(y, -1, -1):
                if graph[x][j] == 6:
                    break
                if not board[x][j]:
                    board[x][j] = True
                    temp.append((x, j))
    return temp


def recur(k: int, dist: list[list[int]]):
    global mn
    if k == len(cctvs):
        cnt = 0
        for i in range(N):
            for j in range(M):
                if not board[i][j]:
                    cnt += 1
        if mn > cnt:
            mn = cnt
        return
    cctv, x, y = cctvs[k]
    for direct in direction[cctv]:
        temp = fill(x, y, direct)
        dist.append(direct)
        recur(k + 1, dist)
        for i, j in temp:
            board[i][j] = False
        dist.pop()


recur(0, [])
print(mn)
