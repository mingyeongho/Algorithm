import sys
input = sys.stdin.readline

N = int(input().strip())
graph = [list(map(int, input().split())) for _ in range(N)]

count = [0, 0]


def recur(x, y, n):
    color = graph[x][y]
    same = True

    for i in range(x, x+n):
        for j in range(y, y+n):
            if graph[i][j] != color:
                same = False
                break
        if not same:
            break

    if same:
        count[color] += 1
    else:
        new_n = n // 2
        for i in [0, new_n]:
            for j in [0, new_n]:
                recur(x+i, y+j, new_n)


recur(0, 0, N)
print(*count, sep='\n')
