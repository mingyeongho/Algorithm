import sys

input = sys.stdin.readline

n = int(input().rstrip())

dp = [0] * (n + 1)
stairs = [0]
for _ in range(n):
  stairs.append(int(input().rstrip()))

if n == 1:
  print(stairs[1])
elif n == 2:
  print(stairs[1] + stairs[2])
else:
  dp[1] = stairs[1]
  dp[2] = stairs[1] + stairs[2]

  for i in range(3, n + 1):
    dp[i] = max(stairs[i] + stairs[i-1] + dp[i-3], stairs[i] + dp[i-2])

  print(dp[n])