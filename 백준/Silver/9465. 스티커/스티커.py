import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    n = int(input().strip())
    graph = [list(map(int, input().split())) for _ in range(2)]

    dp = [[-1] * n for _ in range(2)]
    dp[0][0] = graph[0][0]
    dp[1][0] = graph[1][0]

    for i in range(1, n):
        dp[0][i] = max(dp[0][i-1], dp[1][i-1] + graph[0][i])
        dp[1][i] = max(dp[1][i-1], dp[0][i-1] + graph[1][i])
    print(max(dp[0][n-1], dp[1][n-1]))
