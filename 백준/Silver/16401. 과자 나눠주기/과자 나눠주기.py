import sys
input = sys.stdin.readline


def binary():
    st = 0
    en = max(L)
    while st < en:
        mid = (st + en + 1) // 2
        cnt = 0
        for l in L:
            cnt += l // mid
        if cnt >= M:
            st = mid
        else:
            en = mid-1
    return st


M, N = map(int, input().split())
L = list(map(int, input().split()))
print(binary())
