import sys
input = sys.stdin.readline

n, k = map(int, input().split())

units = [int(input()) for _ in range(n)]

count = 0
for unit in units[::-1]:
    count += k // unit
    k %= unit

print(count)