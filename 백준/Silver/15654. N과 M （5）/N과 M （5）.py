import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

arr = [-1] * M
used = [False] * (10_001)


def backtrack(k):
    if k == M:
        print(*arr)
        return
    for i in nums:
        if not used[i]:
            arr[k] = i
            used[i] = True
            backtrack(k + 1)
            used[i] = False


backtrack(0)
