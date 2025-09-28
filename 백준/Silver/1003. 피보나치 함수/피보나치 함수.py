import sys
input = sys.stdin.readline

T = int(input().strip())

dp = [(1, 0), (0, 1)]
for i in range(2, 41):
    dp.append((dp[i-2][0] + dp[i-1][0], dp[i-2][1] + dp[i-1][1]))


for _ in range(T):
    N = int(input().strip())
    print(*dp[N])
