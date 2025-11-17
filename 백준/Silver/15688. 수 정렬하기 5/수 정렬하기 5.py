import sys
input = sys.stdin.readline

N = int(input().strip())
cnt = [0] * 2_000_001
for _ in range(N):
    n = int(input().strip())
    cnt[n + 1_000_000] += 1

for i in range(2_000_001):
    while cnt[i]:
        print(i - 1_000_000, end='\n')
        cnt[i] -= 1
