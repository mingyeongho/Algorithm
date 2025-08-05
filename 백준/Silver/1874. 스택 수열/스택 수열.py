import sys
input = sys.stdin.readline

n = int(input().rstrip())

stack, result, i, exit = [], [], 1, False

for _ in range(n):
    x = int(input().rstrip())
    
    while i <= x:
        result.append("+")
        stack.append(i)
        i += 1
    
    if x == stack[-1]:
        result.append("-")
        stack.pop()
    else:
        exit = True
        break

print("NO" if exit else "\n".join(result))