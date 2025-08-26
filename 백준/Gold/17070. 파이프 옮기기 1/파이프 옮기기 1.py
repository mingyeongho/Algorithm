import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())
graph = [[0] * (N+1)]
for _ in range(N):
    row = list(map(int, input().split()))
    graph.append([0] + row)

dp = [[[0] * (N+1) for _ in range(N+1)] for _ in range(3)]
dp[0][1][2] = 1

for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] == 1:
            continue

        # 가로
        if j-1 >= 1 and graph[i][j-1] == 0:
            dp[0][i][j] += (dp[0][i][j-1] + dp[2][i][j-1])

        # 세로
        if i-1 >= 1 and graph[i-1][j] == 0:
            dp[1][i][j] += (dp[1][i-1][j] + dp[2][i-1][j])

        # 대각선
        if i-1 >= 1 and j-1 >= 1:
            if graph[i-1][j] == 0 and graph[i][j-1] == 0:
                dp[2][i][j] += (dp[0][i-1][j-1] + dp[1][i-1]
                                [j-1] + dp[2][i-1][j-1])

print(dp[0][N][N] + dp[1][N][N] + dp[2][N][N])
