import sys

input = sys.stdin.readline

N = int(input().strip())
graph = [list(map(int, input().split())) for _ in range(N)]
mx = -1


def rotate(board):
    return [list(row) for row in zip(*board[::-1])]


# 왼쪽으로 미는 함수
def shift(board):
    new_board = []

    for row in board:
        # 0 제거
        line = [x for x in row if x]

        merged = []
        i = 0

        # merge
        while i < len(line):
            if i + 1 < len(line) and line[i] == line[i + 1]:
                merged.append(line[i] * 2)
                i += 2
            else:
                merged.append(line[i])
                i += 1

        # 0 채우기
        merged += [0] * (N - len(merged))
        new_board.append(merged)

    return new_board


def backtrack(k, board):
    global mx

    if k == 5:
        mx = max(mx, max(map(max, board)))
        return

    for _ in range(4):
        new_board = shift(board)
        backtrack(k + 1, new_board)
        board = rotate(board)


backtrack(0, graph)

print(mx)
