import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))

rev_A = A[::-1]

dp_i = [1] * N
dp_d = [1] * N

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp_i[i] = max(dp_i[i], dp_i[j] + 1)
        if rev_A[i] > rev_A[j]:
            dp_d[i] = max(dp_d[i], dp_d[j] + 1)

res = [-1] * N
for i in range(N):
    res[i] = dp_i[i] + dp_d[N-i-1] - 1
print(max(res))
