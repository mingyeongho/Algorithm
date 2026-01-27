import sys

input = sys.stdin.readline


def solution(N, heights):
    mx = 0
    stk = []  # (시작 인덱스, 높이)

    for i in range(N):
        start = i
        while stk and stk[-1][1] > heights[i]:
            idx, h = stk.pop()
            mx = max(mx, h * (i - idx))
            start = idx
        stk.append((start, heights[i]))

    for idx, h in stk:
        mx = max(mx, h * (N - idx))

    return mx


while True:
    cmd = list(map(int, input().split()))
    if cmd[0] == 0:
        break
    heights = cmd[1:]
    print(solution(cmd[0], heights))
