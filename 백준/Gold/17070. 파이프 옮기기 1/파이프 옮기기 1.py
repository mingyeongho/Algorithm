import sys
input = sys.stdin.readline

N = int(input().strip())
graph = [[0] * (N+1)] + [[0] + list(map(int, input().split()))
                         for _ in range(N)]

dp = [[[0] * (N+1) for _ in range(N+1)] for _ in range(3)]
dp[0][1][2] = 1

for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] == 1:
            continue

        if j-1 >= 1 and graph[i][j-1] == 0:
            dp[0][i][j] += (dp[0][i][j-1] + dp[2][i][j-1])

        if i-1 >= 1 and graph[i-1][j] == 0:
            dp[1][i][j] += (dp[1][i-1][j] + dp[2][i-1][j])

        if i-1 >= 1 and j-1 >= 1:
            if graph[i-1][j] == 0 and graph[i][j-1] == 0:
                dp[2][i][j] += (dp[0][i-1][j-1] + dp[1][i-1]
                                [j-1] + dp[2][i-1][j-1])
print(dp[0][N][N] + dp[1][N][N] + dp[2][N][N])
