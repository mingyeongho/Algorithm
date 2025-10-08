import sys
input = sys.stdin.readline

A = input().strip()
B = input().strip()
n = len(A)
m = len(B)

dp = [[0] * (n+1) for _ in range(m+1)]
for i in range(1, m+1):
    for j in range(1, n+1):
        if A[j-1] == B[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[m][n])
