import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().split()))

res = [-1] * n
stk = []
for i in range(n, 0, -1):
    h = arr.pop()

    while stk:
        if stk[-1] > h:
            res[i-1] = stk[-1]
            break
        else:
            stk.pop()

    stk.append(h)

print(*res)
