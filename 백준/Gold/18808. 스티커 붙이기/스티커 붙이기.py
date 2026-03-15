import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [[False] * M for _ in range(N)]


def rotate(sticker):
    return [list(row) for row in zip(*sticker[::-1])]


def attach(x, y, sticker):
    r = len(sticker)
    c = len(sticker[0])

    # 붙일 수 있는지 검사
    for i in range(r):
        for j in range(c):
            if sticker[i][j] and board[x + i][y + j]:
                return False

    # 실제로 붙이기
    for i in range(r):
        for j in range(c):
            if sticker[i][j]:
                board[x + i][y + j] = True

    return True


for _ in range(K):
    R, C = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(R)]

    pasted = False

    for _ in range(4):
        r = len(sticker)
        c = len(sticker[0])
        for i in range(N - r + 1):
            for j in range(M - c + 1):
                if attach(i, j, sticker):
                    pasted = True
                    break
            if pasted:
                break
        if pasted:
            break
        sticker = rotate(sticker)


print(sum(sum(row) for row in board))
