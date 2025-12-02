import sys
input = sys.stdin.readline

x = input().strip()
stack = []
count = 0

for i in range(len(x)):
    if x[i] == '(':
        stack.append("(")
    else:
        stack.pop()
        if x[i - 1] == '(': # 레이저
            count += len(stack)
        else:
            count += 1
print(count)