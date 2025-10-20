import sys

input = sys.stdin.readline

n = int(input().rstrip())

chess = [[True] * n for _ in range(n)]

count = 0
isUsedCol = [False] * n
isUsedLCross = [False] * (2*n-1)
isUsedRCross = [False] * (2*n-1)


def backtrack(k):  # 행
    if k == n:
        global count
        count += 1
        return
    for j in range(n):  # 열
        if isUsedCol[j] or isUsedLCross[k+j] or isUsedRCross[k-j+n-1]:
            continue
        isUsedCol[j] = True
        isUsedLCross[k+j] = True
        isUsedRCross[k-j+n-1] = True
        backtrack(k+1)
        isUsedCol[j] = False
        isUsedLCross[k+j] = False
        isUsedRCross[k-j+n-1] = False


backtrack(0)
print(count)
