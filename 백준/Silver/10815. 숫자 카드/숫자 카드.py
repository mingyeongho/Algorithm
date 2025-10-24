import sys
import bisect
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
A.sort()
M = int(input().strip())
for m in list(map(int, input().split())):
    l, r = bisect.bisect_left(A, m), bisect.bisect_right(A, m)
    print(1 if r - l > 0 else 0, end=' ')
