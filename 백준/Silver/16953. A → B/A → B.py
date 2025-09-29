import sys
from collections import deque, defaultdict
input = sys.stdin.readline

A, B = map(int, input().split())
dist = defaultdict(int)


def bfs(A):
    queue = deque([A])
    dist[A] = 1
    while queue:
        xp = queue.popleft()
        if xp == B:
            return dist[xp]
        for nx in [xp*10+1, xp*2]:
            if nx > B:
                continue
            if dist.get(nx) == None:
                queue.append(nx)
                dist[nx] = dist[xp] + 1
    return -1


print(bfs(A))
