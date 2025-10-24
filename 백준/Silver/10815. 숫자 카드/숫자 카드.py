import sys
input = sys.stdin.readline


def binary(x):
    st = 0
    en = N-1
    while st <= en:
        mid = (st + en) // 2

        if A[mid] == x:
            return True
        elif A[mid] < x:
            st = mid + 1
        else:
            en = mid - 1
    return False


N = int(input().strip())
A = list(map(int, input().split()))
A.sort()
M = int(input().strip())
for m in list(map(int, input().split())):
    print(1 if binary(m) else 0, end=' ')
