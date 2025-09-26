import sys
input = sys.stdin.readline

N = int(input().strip())
cost = [list(map(int, input().split())) for _ in range(N)]

INF = 1_000 * 1_000
# dp[i][c][s]: i번째 집까지 칠했을 때, i번 집 색=c, 첫 집 색=s인 최소 비용
dp = [[[INF] * 3 for _ in range(3)] for _ in range(N)]

# 시작(0번째 집) 초기화: 첫 집 색 s만 유효
for s in range(3):
    dp[0][s][s] = cost[0][s]

# 점화식
for i in range(1, N):
    for s in range(3):
        dp[i][0][s] = cost[i][0] + min(dp[i-1][1][s], dp[i-1][2][s])
        dp[i][1][s] = cost[i][1] + min(dp[i-1][0][s], dp[i-1][2][s])
        dp[i][2][s] = cost[i][2] + min(dp[i-1][0][s], dp[i-1][1][s])

# 원형 제약: 마지막 집 색 != 첫 집 색
ans = INF
for s in range(3):
    for c in range(3):
        if c != s:
            ans = min(ans, dp[N-1][c][s])

print(ans)
