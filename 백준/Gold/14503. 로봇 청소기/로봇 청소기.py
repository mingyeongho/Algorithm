import sys

input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
direct = [(1, 0, 2), (0, -1, 3), (-1, 0, 0), (0, 1, 1)]  # 남 서 북 동
direction = [
    [direct[1], direct[0], direct[3], direct[2]],  # 서 남 동 북
    [direct[2], direct[1], direct[0], direct[3]],  # 북 서 남 동
    [direct[3], direct[2], direct[1], direct[0]],  # 동 북 서 남
    [direct[0], direct[3], direct[2], direct[1]],  # 남 동 북 서
]
visited = [[False] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            visited[i][j] = True

stk = [(r, c, d)]
visited[r][c] = True
answer = 1
while stk:
    xp, yp, dp = stk.pop()
    flag = False
    for dx, dy, dd in direction[dp]:
        nx, ny = xp + dx, yp + dy
        if not (0 <= nx < N and 0 <= ny < M):
            continue
        if graph[nx][ny] == 0 and not visited[nx][ny]:
            stk.append((nx, ny, dd))
            visited[nx][ny] = True
            answer += 1
            flag = True
            break
    if flag:
        continue
    dx, dy, _ = direct[dp]
    nx, ny = xp + dx, yp + dy
    if graph[nx][ny] == 0:
        stk.append((nx, ny, dp))
print(answer)
