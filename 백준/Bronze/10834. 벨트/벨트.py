import sys

input = sys.stdin.readline

M = int(input())

ans = 1
direction = 0

for _ in range(M):
    a, b, s = map(int, input().split())

    if s == 1:
        direction ^= 1

    ans = (ans * b) // a

print(direction, ans)
