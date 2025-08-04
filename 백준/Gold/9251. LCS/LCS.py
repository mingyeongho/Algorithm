import sys
input = sys.stdin.readline

A, B = [input().strip() for _ in range(2)]
len_A, len_B = len(A), len(B)

dp = [[0] * (len_A+1) for _ in range(len_B+1)]

for i in range(1, len_B+1):
    for j in range(1, len_A+1):
        if B[i-1] == A[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len_B][len_A])
