import sys
import bisect
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
LIS = [A[0]]

for i in range(1, N):
    if LIS[-1] < A[i]:
        LIS.append(A[i])
    else:
        idx = bisect.bisect_left(LIS, A[i])
        LIS[idx] = A[i]
print(len(LIS))