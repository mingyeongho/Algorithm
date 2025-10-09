import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
M = int(input().strip())

dp = [[False] * N for _ in range(N)]

for i in range(N):
    dp[i][i] = True

for i in range(N-1):
    if A[i] == A[i+1]:
        dp[i][i+1] = True

for i in range(3, N+1):
    for st in range(N-i+1):
        en = st + i - 1
        if A[st] == A[en] and dp[st+1][en-1]:
            dp[st][en] = True


for _ in range(M):
    S, E = map(int, input().split())
    print(1 if dp[S-1][E-1] else 0)
