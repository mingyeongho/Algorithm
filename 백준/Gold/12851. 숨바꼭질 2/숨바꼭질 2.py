import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())


def bfs(N, K):
    dist = [-1] * 100_001  # 거리
    count = [0] * 100_001  # 방법의 수

    queue = deque([N])
    dist[N] = 0
    count[N] = 1

    while queue:
        xp = queue.popleft()
        for nx in [2*xp, xp-1, xp+1]:
            if not (0 <= nx < 100_001):
                continue
            if dist[nx] == -1:
                dist[nx] = dist[xp] + 1
                count[nx] = count[xp]
                queue.append(nx)
            elif dist[nx] == dist[xp] + 1:  # 이미 방문했지만 같은 최단 시간 내에 갈 방법이 존재
                count[nx] += count[xp]
    return [dist[K], count[K]]


print(*bfs(N, K), sep='\n')
