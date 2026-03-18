import sys
from collections import deque

input = sys.stdin.readline


def rotate(gear, direct):
    q = deque(gear)
    q.rotate(direct)
    return list(q)


gears = [[]] + [list(map(int, list(input().strip()))) for _ in range(4)]
K = int(input().strip())
for _ in range(K):
    # d, 1: 시계 방향, -1: 반시계 방향
    n, d = map(int, input().split())
    new_gears = [[None] for _ in range(5)]
    new_gears[n] = rotate(gears[n], d)
    dd = d
    for i in range(n, 1, -1):
        if gears[i][6] != gears[i - 1][2]:
            dd *= -1
            new_gears[i - 1] = rotate(gears[i - 1], dd)
        else:
            break
    dd = d
    for i in range(n, 4):
        if gears[i][2] != gears[i + 1][6]:
            dd *= -1
            new_gears[i + 1] = rotate(gears[i + 1], dd)
        else:
            break
    for idx in range(1, 5):
        if new_gears[idx] == [None]:
            new_gears[idx] = gears[idx]
    gears = new_gears

answer = 0
for i in range(1, 5):
    if gears[i][0] == 1:
        answer += 2 ** (i - 1)
print(answer)
