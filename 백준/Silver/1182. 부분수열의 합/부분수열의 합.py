import sys
input = sys.stdin.readline

N, S = map(int, input().split())
A = list(map(int, input().split()))

count = 0


def backtrack(k, total):
    global count

    if k == N:
        if total == S:
            count += 1
        return

    backtrack(k+1, total)
    backtrack(k+1, total + A[k])


backtrack(0, 0)

print(count if S else count-1)
