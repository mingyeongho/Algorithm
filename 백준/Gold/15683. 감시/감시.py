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

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def fill(x: int, y: int, direct: list[int]):
    temp = []  # 어떤 값을 바꿨는지 기억하는 배열, (i, j)
    for d in direct:
        dx, dy = delta[d]
        nx, ny = x, y
        while 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 6:
                break
            if not board[nx][ny]:
                board[nx][ny] = True
                temp.append((nx, ny))
            nx += dx
            ny += dy
    return temp


def recur(k: int):
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
        recur(k + 1)
        for i, j in temp:
            board[i][j] = False


recur(0)
print(mn)
