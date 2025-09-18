import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

S = []
while True:
    try:
        n = int(input().strip())
        S.append(n)
    except:
        break


def recur(S):
    if len(S) == 0:
        return

    left, right = [], []
    mid = S[0]
    for s in range(1, len(S)):
        if mid > S[s]:
            left.append(S[s])
        else:
            right.append(S[s])

    recur(left)
    recur(right)
    print(mid)


recur(S)
