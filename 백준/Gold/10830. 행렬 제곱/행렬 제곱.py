import sys
input = sys.stdin.readline

N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]


def multi(A, B, N):
    K = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            s = sum(A[i][k] * B[k][j] for k in range(N))
            K[i][j] = s % 1_000
    return K


def square(M, B, N):
    if B == 1:
        return M
    half = square(M, B//2, N)
    if B % 2 == 0:
        return multi(half, half, N)
    else:
        return multi(multi(half, half, N), M, N)


answer = square(matrix, B, N)

for i in range(N):
    for j in range(N):
        print(answer[i][j] % 1_000, end=' ')
    print()
