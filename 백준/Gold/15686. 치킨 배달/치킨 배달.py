import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

homes = []  # (i, j)
chickens = []  # (i, j)
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            homes.append((i, j))
        elif graph[i][j] == 2:
            chickens.append((i, j))

mn = float("Inf")
selected = [None] * M


def backtrack(k, start):
    global mn
    if k == M:
        acc = 0
        for hx, hy in homes:
            dist = float("Inf")
            for cx, cy in selected:
                d = abs(cx - hx) + abs(cy - hy)
                dist = min(dist, d)
            acc += dist
        mn = min(mn, acc)
        return
    for idx in range(start, len(chickens)):
        selected[k] = chickens[idx]
        backtrack(k + 1, idx + 1)


backtrack(0, 0)

print(mn)
