import sys
input = sys.stdin.readline

N = int(input().strip())
costs = [list(map(int, input().split())) for _ in range(N)]

INF = 1_000 * 1_000 + 1
# dp[k][i][j]: 첫 번째 집 색=k, i번째 집 색=j 일 때 최소비용
dp = [[[INF] * 3 for _ in range(N)] for _ in range(3)]

# 첫 집 초기화
for k in range(3):
    dp[k][0][k] = costs[0][k]

# 점화식
for i in range(1, N):
    for k in range(3):  # 시작 색
        dp[k][i][0] = costs[i][0] + min(dp[k][i-1][1], dp[k][i-1][2])
        dp[k][i][1] = costs[i][1] + min(dp[k][i-1][0], dp[k][i-1][2])
        dp[k][i][2] = costs[i][2] + min(dp[k][i-1][0], dp[k][i-1][1])

# 원형 제약: 첫 집 색 != 마지막 집 색
ans = INF
for k in range(3):
    for j in range(3):
        if k != j:
            ans = min(ans, dp[k][N-1][j])

print(ans)
