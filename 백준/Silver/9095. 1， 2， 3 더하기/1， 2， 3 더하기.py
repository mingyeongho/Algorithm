import sys

input = sys.stdin.readline

n = int(input().rstrip())

dp = [0, 1, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(4, 12):
  dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

for _ in range(n):
  m = int(input().rstrip())
  print(dp[m])