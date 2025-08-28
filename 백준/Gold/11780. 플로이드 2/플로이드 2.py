import sys
input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())

dist = [[float("Inf")] * (N+1) for _ in range(N+1)]
nxt = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c)
    nxt[a][b] = b

for i in range(1, N+1):
    dist[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                nxt[i][j] = nxt[i][k]

for i in range(1, N+1):
    for j in range(1, N+1):
        if dist[i][j] == float("Inf"):
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()
for i in range(1, N+1):
    for j in range(1, N+1):
        if dist[i][j] == 0 or dist[i][j] == float("Inf"):
            print(0, end=' ')
            continue
        path = []
        st = i
        while st != j:
            path.append(st)
            st = nxt[st][j]
        path.append(j)
        print(len(path), end=' ')
        for p in path:
            print(p, end=' ')
        print()
