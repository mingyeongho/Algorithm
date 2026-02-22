import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())


def solution(N, K):
    dist = [-1] * 100_001
    q = deque([N])
    dist[N] = 0

    while q:
        xp = q.popleft()
        if xp == K:
            return dist[xp]
        for i, nx in enumerate([xp * 2, xp - 1, xp + 1]):
            if not (0 <= nx < 100_001):
                continue
            if i == 0 and dist[nx] == -1:
                dist[nx] = dist[xp]
                q.append(nx)
            elif dist[nx] == -1:
                dist[nx] = dist[xp] + 1
                q.append(nx)
    return -1


print(solution(N, K))
