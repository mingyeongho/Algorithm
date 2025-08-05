import sys
input = sys.stdin.readline

n = int(input().rstrip())
stk = []
for _ in range(n):
    m = int(input().rstrip())
    if m == 0:
        stk.pop()
    else:
        stk.append(m)
print(sum(stk))
