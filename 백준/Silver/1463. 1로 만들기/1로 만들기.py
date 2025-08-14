import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())

queue = deque([N])
dist = [-1] * (N+1)
dist[N] = 0
while queue:
    n = queue.popleft()
    if n == 1:
        break
    for d in [n/3, n/2, n-1]:
        if d != int(d):
            continue
        d = int(d)
        if dist[d] == -1:
            dist[d] = dist[n] + 1
            queue.append(d)
print(dist[1])
