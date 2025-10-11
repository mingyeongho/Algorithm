import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[0] * (N+1)] + [[0] + list(map(int, input().split()))
                         for _ in range(N)]

H = []
C = []
for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] == 2:
            C.append((i, j))
        elif graph[i][j] == 1:
            H.append((i, j))

answer = []
dist = float("Inf")


def backtrack(start, k):
    global dist

    if k == M:
        d = 0
        for hx, hy in H:
            hd = float("Inf")
            for cx, cy in answer:
                cd = abs(hx - cx) + abs(hy - cy)
                hd = min(hd, cd)
            d += hd
        dist = min(dist, d)
        return
    for i in range(start, len(C)):
        answer.append(C[i])
        backtrack(i+1, k+1)
        answer.pop()


backtrack(0, 0)
print(dist)
