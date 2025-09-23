import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dex = dict()
for i in range(1, N+1):
    name = input().strip()
    dex[str(i)] = name
    dex[name] = i

for i in range(1, M+1):
    q = input().strip()
    print(dex[q])
