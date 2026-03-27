import sys

input = sys.stdin.readline

p, n, c = map(int, input().split())
answer = p * n - c
print(answer if answer >= 0 else 0)
