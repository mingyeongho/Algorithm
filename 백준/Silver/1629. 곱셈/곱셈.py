import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())


def recur(a, b, c):
    if b == 1:
        return a % c
    tmp = recur(a, b // 2, c)
    if b % 2 == 0:
        return (tmp * tmp) % c
    else:
        return (tmp * tmp % c) * a % c


print(recur(a, b, c))
