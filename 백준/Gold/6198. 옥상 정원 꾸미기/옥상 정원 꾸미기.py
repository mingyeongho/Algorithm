import sys
input = sys.stdin.readline

n = int(input().rstrip())
heights = [int(input().rstrip()) for _ in range(n)]

count = [0] * n
stk = []

for i in range(n, 0, -1):
    h = heights.pop()

    while stk and stk[-1][1] < h:
        count[i-1] += 1 + count[stk[-1][0]-1]
        stk.pop()

    stk.append((i, h))

print(sum(count))
