import sys
input = sys.stdin.readline

n, k = map(int, input().split())

arr = [i for i in range(1, n + 1)] # 1 ~ n 까지 배열 생성
stack = []
idx = 0

while arr:
    idx = (idx + k - 1) % len(arr)
    stack.append(arr.pop(idx))

print(f"<{', '.join(map(str, stack))}>")