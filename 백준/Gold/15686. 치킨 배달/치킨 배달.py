import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

homes = []  # (i, j, dist)
chickens = []  # (i, j, flag)
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            homes.append([i, j, float("Inf")])
        elif graph[i][j] == 2:
            chickens.append([i, j, False])

mn = float("Inf")
selected = [None] * M


def backtrack(k, start):
    global mn
    if k == M:
        for home in homes:
            dist = [-1] * len(selected)
            for idx, chicken in enumerate(selected):
                d = abs(chicken[0] - home[0]) + abs(chicken[1] - home[1])
                dist[idx] = d
            home[2] = min(dist)
        acc = 0
        for home in homes:
            acc += home[2]
        mn = min(mn, acc)
        return
    for idx in range(start, len(chickens)):
        chicken = chickens[idx]
        if not chicken[2]:
            chicken[2] = True
            selected[k] = chicken
            backtrack(k + 1, idx + 1)
            chicken[2] = False


backtrack(0, 0)

print(mn)
