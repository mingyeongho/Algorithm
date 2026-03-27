import sys

input = sys.stdin.readline

n = int(input().strip())
S = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if S[i] != i + 1:
        cnt += 1
print(cnt)
