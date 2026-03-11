import sys

input = sys.stdin.readline

N = int(input().strip())
graph = [list(map(int, input().split())) for _ in range(N)]

count = [0, 0, 0]


def isSame(graph):
    init = graph[0][0]
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if init != graph[i][j]:
                return False
    return True


def recur(start: tuple[int, int], n):
    x, y = start
    init = graph[x][y]
    if isSame([[graph[i][j] for j in range(y, y + n)] for i in range(x, x + n)]):
        count[init + 1] += 1
    else:
        new_n = n // 3
        for i in [0, new_n, 2 * new_n]:
            for j in [0, new_n, 2 * new_n]:
                recur((x + i, y + j), new_n)


recur((0, 0), N)
print(*count, sep="\n")
