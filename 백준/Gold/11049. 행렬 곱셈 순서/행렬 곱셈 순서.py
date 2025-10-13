import sys
input = sys.stdin.readline

N = int(input().strip())
M = [tuple(map(int, input().split())) for _ in range(N)]  # M[i] = (r_i, c_i)

# D: M_i = D[i] x D[i+1]
D = [M[0][0]] + [M[i][1] for i in range(N)]

dp = [[0]*N for _ in range(N)]

# 구간 길이 2..N
for length in range(2, N+1):
    for i in range(0, N-length+1):
        j = i + length - 1
        best = 10**19
        Di = D[i]
        Dj1 = D[j+1]
        for k in range(i, j):
            # (M_i..M_k) + (M_{k+1}..M_j) + 두 결과 행렬의 곱 비용
            cost = dp[i][k] + dp[k+1][j] + Di * D[k+1] * Dj1
            if cost < best:
                best = cost
        dp[i][j] = best

print(0 if N == 0 else dp[0][N-1])
