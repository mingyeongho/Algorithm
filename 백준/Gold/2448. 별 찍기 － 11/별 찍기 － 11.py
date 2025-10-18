import sys
input = sys.stdin.readline

N = int(input().strip())
graph = [[False] * (2*N-1) for _ in range(N)]


def recur(x, y, n):
    if n == 3:
        graph[x][y] = True
        graph[x+1][y-1] = graph[x+1][y+1] = True
        for i in range(-2, 3):
            graph[x+2][y+i] = True
        return

    new_n = n // 2
    recur(x, y, new_n)
    recur(x + new_n, y - new_n, new_n)
    recur(x + new_n, y + new_n, new_n)


recur(0, N-1, N)
for row in graph:
    print("".join("*" if cell else " " for cell in row))
