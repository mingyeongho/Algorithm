import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(input().strip()) for _ in range(N)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def solution(R, C, graph):
    dist = [[[-1] * C for _ in range(R)] for _ in range(2)]
    deq = deque([(0, 0, 0)]) # z, x, y
    dist[0][0][0] = 1
    
    while deq:
        zp, xp, yp = deq.popleft()
        if xp == R-1 and yp == C-1:
            return dist[zp][xp][yp]
        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < R and 0 <= ny < C):
                continue
            if graph[nx][ny] == "0" and dist[zp][nx][ny] == -1: # 다음 칸이 방문한 적 없는 이동할 수 있는 칸일 경우
                deq.append((zp, nx, ny))
                dist[zp][nx][ny] = dist[zp][xp][yp] + 1
            elif graph[nx][ny] == "1" and zp == 0 and dist[1][nx][ny] == -1: # 벽을 부술 수 있고 다음 칸이 벽일 경우
                deq.append((1, nx, ny))
                dist[1][nx][ny] = dist[0][xp][yp] + 1
    return -1

print(solution(N, M, graph))