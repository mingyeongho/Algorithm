import sys
input = sys.stdin.readline

n = int(input().rstrip())
nums = list(map(int, input().split()))

stack = []
ans = [0] * n

for i in range(n, 0, -1):
    h = nums.pop()

    while stack and stack[-1][1] < h:
        ans[stack[-1][0] - 1] = i
        stack.pop()

    stack.append((i, h))

print(*ans)
