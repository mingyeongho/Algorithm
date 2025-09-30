import sys
input = sys.stdin.readline


def hasRow(r, num):
    for _ in range(9):
        if num in sudoku[r]:
            return True
    return False


def hasCol(c, num):
    for i in range(9):
        if num == sudoku[i][c]:
            return True
    return False


def hasMatrix(r, c, num):
    nr = (r // 3) * 3
    nc = (c // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudoku[nr+i][nc+j] == num:
                return True
    return False


def dfs(depth):
    if depth >= len(zeros):
        for i in range(9):
            print("".join(map(str, sudoku[i])))
        sys.exit(0)

    nr, nc = zeros[depth]
    for i in range(1, 9+1):
        if not hasRow(nr, i) and not hasCol(nc, i) and not hasMatrix(nr, nc, i):
            sudoku[nr][nc] = i
            dfs(depth + 1)
            sudoku[nr][nc] = 0


sudoku = []
zeros = []
for i in range(0, 9):
    row = list(map(int, input().strip()))
    sudoku.append(row)
    for j in range(len(row)):
        if row[j] == 0:
            zeros.append((i, j))

dfs(0)
