import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

A, B, C = map(int, input().split())


def recur(a, b, c):
    if b == 1:
        return a % c
    if b % 2:
        return (recur(a, b - 1, c) * recur(a, 1, c)) % c
    return (recur(a, b // 2, c) ** 2) % c


print(recur(A, B, C))
