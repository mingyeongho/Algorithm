import sys
input = sys.stdin.readline

def isVps(word: str) -> bool:
    stack = []
    for i in word:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                return False
    return False if stack else True

n = int(input().strip())

for _ in range(n):
    word = input().strip()
    print("YES" if isVps(word) else "NO")