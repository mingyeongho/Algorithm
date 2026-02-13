import sys
from collections import deque

input = sys.stdin.readline

direction = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]


def solution(L, st_x, st_y, ed_x, ed_y, dist):
    dist[st_x][st_y] = 0
    deq = deque([(st_x, st_y)])

    while deq:
        xp, yp = deq.popleft()
        if xp == ed_x and yp == ed_y:
            return dist[xp][yp]
        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < L and 0 <= ny < L):
                continue
            if dist[nx][ny] == -1:
                deq.append((nx, ny))
                dist[nx][ny] = dist[xp][yp] + 1
    return -1


T = int(input().strip())
for _ in range(T):
    L = int(input().strip())
    st_x, st_y = map(int, input().split())
    ed_x, ed_y = map(int, input().split())
    dist = [[-1] * L for _ in range(L)]
    print(solution(L, st_x, st_y, ed_x, ed_y, dist))
