import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))

lis = [A[0]]
for i in range(1, N):
    if lis[-1] < A[i]:
        lis.append(A[i])
    else:
        idx = bisect_left(lis, A[i])
        lis[idx] = A[i]

print(len(lis))
