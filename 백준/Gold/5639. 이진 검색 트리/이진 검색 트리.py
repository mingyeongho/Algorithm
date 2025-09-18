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


def recur(start, end):
    if start > end:
        return

    mid = end+1
    for i in range(start+1, end+1):
        if S[start] < S[i]:
            mid = i
            break
    recur(start+1, mid-1)
    recur(mid, end)
    print(S[start])
    pass


recur(0, len(S)-1)
