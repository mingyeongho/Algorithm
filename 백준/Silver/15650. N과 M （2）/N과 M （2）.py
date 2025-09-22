import sys

input = sys.stdin.readline

n, m = map(int, input().split())

ans = [0] * m


def backtrack(k, start):
    if k == m:
        print(' '.join(map(str, ans)))
        return
    for i in range(start, n+1):
        ans[k] = i
        backtrack(k+1, i+1)


backtrack(0, 1)
