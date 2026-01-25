from collections import deque

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dist = [[-1 for _ in range(m)] for _ in range(n)]
    dist[0][0] = 1
    deq = deque([(0, 0)])
    
    while deq:
        xp, yp = deq.popleft()
        if xp == n-1 and yp == m-1:
            return dist[n-1][m-1]
        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if maps[nx][ny] == 1 and dist[nx][ny] == -1:
                deq.append((nx, ny))
                dist[nx][ny] = dist[xp][yp] + 1

    return -1