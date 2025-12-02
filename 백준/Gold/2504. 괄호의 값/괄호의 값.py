import sys
input = sys.stdin.readline

b = input().strip()
answer = 0
stk = []
multi = 1
for i, bb in enumerate(b):
    if bb == "(":
        stk.append(bb)
        multi *= 2
    elif bb == "[":
        stk.append(bb)
        multi *= 3
    elif bb == ")":
        if not stk or stk[-1] != "(":
            print(0)
            exit(0)
        if b[i-1] == "(":
            answer += multi
        multi //= 2
        stk.pop()
    elif bb == "]":
        if not stk or stk[-1] != "[":
            print(0)
            exit(0)
        if b[i-1] == "[":
            answer += multi
        multi //= 3
        stk.pop()
print(answer if not stk else 0)
