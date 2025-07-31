import sys
input = sys.stdin.readline

N = int(input().strip())

graph = [[] for _ in range(N)]

for i in range(N):
    graph[i] = list(map(int, input().split()))

# dp[i][j]는 i번째 줄 j번째 값까지의 최댓값
# 이차원 배열로 한 이유는 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 오른쪽에 있는 것 중에서만 선택할 수 있다고 해서.
dp = [[-1] * (i+1) for i in range(N)]
dp[0][0] = graph[0][0]

for i in range(1, N):
    for j in range(i+1):
        # dp[i][j] = dp[나한테 올 수 있는 값 중 최댓값] + graph[i][j]
        if j == 0:
            dp[i][0] = dp[i-1][0] + graph[i][0]
        elif j == i:
            dp[i][i] = dp[i-1][i-1] + graph[i][i]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + graph[i][j]

print(max(dp[N-1]))
