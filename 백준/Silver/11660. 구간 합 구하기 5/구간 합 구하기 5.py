import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            continue

        if i == 0:
            A[i][j] += A[0][j-1]
        elif j == 0:
            A[i][j] += A[i-1][0]
        else:
            A[i][j] += A[i-1][j] + A[i][j-1] - A[i-1][j-1]

for _ in range(M):
    lx, ly, rx, ry = map(int, input().split())
    if lx == 1 and ly == 1:
        print(A[rx-1][ry-1])
    elif lx == 1:
        print(A[rx-1][ry-1] - A[rx-1][ly-2])
    elif ly == 1:
        print(A[rx-1][ry-1] - A[lx-2][ry-1])
    else:
        print(A[rx-1][ry-1] - A[lx-2][ry-1] -
              A[rx-1][ly-2] + A[lx-2][ly-2])
