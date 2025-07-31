import sys
from collections import deque
input = sys.stdin.readline

A, B = map(int, input().split())

dist = {}


def bfs():
    queue = deque([A])
    dist.setdefault(A, 1)

    while queue:
        xp = queue.popleft()
        if xp > B:
            return None
        if xp == B:
            return dist.get(B)
        for calc in [xp*2, xp*10+1]:
            if 1 <= calc <= B:
                dist.setdefault(calc, dist.get(xp, 0) + 1)
                queue.append(calc)

    return None


res = bfs()
print(res if res else -1)
