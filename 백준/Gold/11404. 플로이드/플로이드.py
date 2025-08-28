import sys
input = sys.stdin.readline

N = int(input().strip())  # 도시의 개수
M = int(input().strip())  # 버스의 개수
dist = [[float("Inf")] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())  # 시작 도시, 도착 도시, 비용
    dist[a][b] = min(dist[a][b], c)

for i in range(1, N+1):
    dist[i][i] = 0

for k in range(1, N+1):  # 거쳐서 가는 정점
    for i in range(1, N+1):
        for j in range(1, N+1):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for i in range(1, N+1):
    for j in range(1, N+1):
        if dist[i][j] == float("Inf"):
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()
