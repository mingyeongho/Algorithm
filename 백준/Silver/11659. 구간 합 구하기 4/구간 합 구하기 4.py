import sys
input = sys.stdin.readline

N, M = map(int, input().split())
n_seq = list(map(int, input().split()))

dp = [0] + [-1] * N
for i, val in enumerate(n_seq):
    dp[i + 1] = dp[i] + val

for _ in range(M):
    i, j = map(int, input().split())
    print(dp[j] - dp[i-1])
