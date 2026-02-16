import sys
from collections import deque

input = sys.stdin.readline
F, S, G, U, D = map(int, input().split())


def solution(F, S, G, U, D):
    dist = [-1] * (F + 1)
    dist[S] = 0
    deq = deque([S])

    while deq:
        xp = deq.popleft()
        if xp == G:
            return dist[xp]
        for dx in [xp + U, xp - D]:
            if not (0 < dx <= F):
                continue
            if dist[dx] == -1:
                deq.append(dx)
                dist[dx] = dist[xp] + 1
    return -1


result = solution(F, S, G, U, D)
print(result if result > -1 else "use the stairs")
