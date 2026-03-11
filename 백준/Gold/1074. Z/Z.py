import sys

input = sys.stdin.readline

N, r, c = map(int, input().split())


def func(N, r, c):
    if N == 1:
        if r == 0 and c == 0:
            return 0
        elif r == 0 and c == 1:
            return 1
        elif r == 1 and c == 0:
            return 2
        else:
            return 3
    half = 2 ** (N - 1)
    if 0 <= r < half and half <= c < 2**N:  # 1사분면
        return func(N - 1, r, c - half) + half**2
    elif 0 <= r < half and 0 <= c < half:  # 2사분면
        return func(N - 1, r, c)
    elif half <= r < 2**N and 0 <= c < half:  # 3사분면
        return func(N - 1, r - half, c) + (half**2) * 2
    else:  # 4사분면
        return func(N - 1, r - half, c - half) + (half**2) * 3


print(func(N, r, c))
