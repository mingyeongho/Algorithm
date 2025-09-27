import sys
input = sys.stdin.readline

N, M = map(int, input().split())
d = dict()
for _ in range(N):
    domain, pw = input().split()
    d[domain] = pw
for _ in range(M):
    domain = input().strip()
    print(d[domain])
