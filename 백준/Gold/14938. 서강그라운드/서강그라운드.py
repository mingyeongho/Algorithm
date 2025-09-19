import sys
input = sys.stdin.readline

INF = 1e9

n, m, r = map(int, input().split())
t = list(map(int, input().split()))
dist = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    dist[a][b] = min(dist[a][b], l)
    dist[b][a] = min(dist[b][a], l)


def floyd():
    for i in range(n+1):
        dist[i][i] = 0

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


d = floyd()
count = 0
for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if 0 <= dist[i][j] <= m:
            cnt += t[j-1]
    count = max(count, cnt)

print(count)
