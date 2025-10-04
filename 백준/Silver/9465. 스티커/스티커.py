import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    A = [list(map(int, input().split())) for _ in range(2)]

    dp = [[-1] * N for _ in range(2)]
    dp[0][0] = A[0][0]
    dp[1][0] = A[1][0]

    for j in range(1, N):
        dp[0][j] = max(dp[0][j-1], dp[1][j-1] + A[0][j])
        dp[1][j] = max(dp[1][j-1], dp[0][j-1] + A[1][j])
    print(max(dp[0][N-1], dp[1][N-1]))
