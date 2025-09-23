import sys
input = sys.stdin.readline

N, M = map(int, input().split())

answer = [0] * M


def backtrack(start, k):
    if k == M:
        print(*answer)
        return
    for i in range(start, N+1):
        answer[k] = i
        backtrack(i, k+1)


backtrack(1, 0)
