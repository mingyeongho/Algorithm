import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())


def solution(N, K):
    dist = [-1] * 100_001  # 시간이 들어있는 배열
    direct = [-1] * 100_001  # 이전 경로가 들어있는 배열

    q = deque([N])
    dist[N] = 0

    while q:
        xp = q.popleft()
        if xp == K:
            d = []
            end = xp
            while direct[end] != -1:
                d.append(end)
                end = direct[end]
            d.append(end)
            d.reverse()
            return (dist[xp], d)
        for nx in [xp * 2, xp + 1, xp - 1]:
            if not (0 <= nx < 100_001):
                continue
            # 다음 좌표의 이전 경로가 없고 시간도 없을 경우
            if dist[nx] == -1 and direct[nx] == -1:
                dist[nx] = dist[xp] + 1
                direct[nx] = xp
                q.append(nx)


dist, direct = solution(N, K)
print(dist)
print(*direct)
