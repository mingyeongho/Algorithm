""" 
DP를 사용해서 해야할 거 같음.
Why? 1 <= N <= 1024, 1 <= M <= 100_000, 시간 제한: 1초
시간복잡도를 생각했을 때, O(NM) 시간복잡도를 가지면 1024 * 100_000 = 102_400_000
파이썬에서 1초에 1억번 연산을 할 수 없다. 따라서 시간복잡도가 낮은 알고리즘을 사용해야 한다.
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
""" 
테이블 정의: dp[i][j]는 (0, 0)부터 (i, j)까지 더한 합.
점화식:
    - i가 0일 경우, dp[i][j] = dp[0][j-1] + graph[i][j]
    - j가 0일 경우, dp[i][j] = dp[i-1][0] + graph[i][j]
    - 그 외일 경우, dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + graph[i][j]
초기값: dp[0][0] = graph[0][0]
"""
dp = [[0] * N for _ in range(N)]
dp[0][0] = graph[0][0]

for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            continue

        if i == 0:
            dp[i][j] = dp[i][j-1] + graph[i][j]
        elif j == 0:
            dp[i][j] = dp[i-1][j] + graph[i][j]
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + graph[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == 1 and y1 == 1:
        print(dp[x2-1][y2-1])
    elif x1 == 1:
        print(dp[x2-1][y2-1] - dp[x2-1][y1-2])
    elif y1 == 1:
        print(dp[x2-1][y2-1] - dp[x1-2][y2-1])
    else:
        print(dp[x2-1][y2-1] - dp[x1-2][y2-1] -
              dp[x2-1][y1-2] + dp[x1-2][y1-2])
