import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [-1] * M


def backtrack(k, start):
    if k == M:
        print(*arr)
        return
    for i in range(start, N + 1):
        arr[k] = i
        backtrack(k + 1, i)


backtrack(0, 1)
