import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

dist = [-1] * 100_001
path = [-1] * 100_001

queue = deque([N])
dist[N] = 0
path[N] = 0

while queue:
    xp = queue.popleft()
    if xp == K:
        break
    for nx in [xp*2, xp-1, xp+1]:
        if not (0 <= nx < 100_001):
            continue
        if dist[nx] == -1:
            queue.append((nx))
            dist[nx] = dist[xp] + 1
            path[nx] = xp

print(dist[K])

P = []
while K != N:
    P.append(K)
    K = path[K]
P.append(N)
P.reverse()

print(*P)
