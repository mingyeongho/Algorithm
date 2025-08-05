import sys
input = sys.stdin.readline

n = int(input().strip()) # 명령어 개수
stack = []

for _ in range(n):
    command = input().strip()
    
    if 'push' in command:
        stack.append(command.split()[1])
    elif command == 'pop':
        print(stack.pop() if stack else -1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        print(0 if stack else 1)
    elif command == 'top':
        print(stack[-1] if stack else -1)