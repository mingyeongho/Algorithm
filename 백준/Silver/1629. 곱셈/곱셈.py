import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

A, B, C = map(int, input().split())


def recur(a, b, c):
    if b == 1:
        return a % c
    half = recur(a, b // 2, c)
    if b % 2:
        return (half * half * (a % c)) % c
    return (half * half) % c


print(recur(A, B, C))
