import sys
input = sys.stdin.readline

C, N = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(N)]  # (Cost, Customer)
dp = [1e6] * (C+100)
dp[0] = 0

for cost, cus in A:
    for k in range(1, C+100):
        if cus <= k:
            dp[k] = min(dp[k], dp[k-cus]+cost)

print(min(dp[C:]))
