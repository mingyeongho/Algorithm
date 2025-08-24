import sys
from collections import deque
input = sys.stdin.readline

K = int(input().strip())  # 원숭이가 말의 움직임을 따라할 수 있는 횟수
W, H = map(int, input().split())  # 가로, 세로
graph = [list(map(int, input().split())) for _ in range(H)]

direction_horse = [(-2, 1), (-1, 2), (1, 2), (2, 1),
                   (2, -1), (1, -2), (-1, -2), (-2, -1)]
direction_monkey = [(-1, 0), (1, 0), (0, -1), (0, 1)]

dist = [[[-1] * W for _ in range(H)] for _ in range(K+1)]
queue = deque([(0, 0, 0)])
dist[0][0][0] = 0
while queue:
    zp, xp, yp = queue.popleft()
    if xp == H-1 and yp == W-1:
        print(dist[zp][xp][yp])
        exit(0)
    if zp < K:
        # 말처럼 움직일 수 있음.
        for dx, dy in direction_horse:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < H and 0 <= ny < W):
                continue
            if dist[zp+1][nx][ny] == -1 and graph[nx][ny] == 0:
                queue.append((zp+1, nx, ny))
                dist[zp+1][nx][ny] = dist[zp][xp][yp] + 1
    # 원숭이처럼만 움직임.
    for dx, dy in direction_monkey:
        nx, ny = xp + dx, yp + dy
        if not (0 <= nx < H and 0 <= ny < W):
            continue
        if dist[zp][nx][ny] == -1 and graph[nx][ny] == 0:
            queue.append((zp, nx, ny))
            dist[zp][nx][ny] = dist[zp][xp][yp] + 1

print(-1)
