import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

dist = [-1] * 100_001
queue = deque([n])
dist[n] = 0
while queue:
    nx = queue.popleft()
    if nx == k:
        print(dist[nx])
        break
    for idx, calc in enumerate([nx*2, nx-1, nx+1]):
        if not (0 <= calc < 100_001):
            continue
        if dist[calc] == -1:
            if idx == 0:
                dist[calc] = dist[nx]
            else:
                dist[calc] = dist[nx] + 1
            queue.append(calc)
