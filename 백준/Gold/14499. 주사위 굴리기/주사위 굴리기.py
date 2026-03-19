import sys

input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
C = list(map(int, input().split()))  # len: K, 1: 동, 2: 서, 3: 북, 4: 남
dice = [0] * 6  # 0: 위, 1: 북, 2: 동, 3: 서, 4: 남, 5: 아래

direct = [(), (0, 1), (0, -1), (-1, 0), (1, 0)]

for cmd in C:
    dx, dy = direct[cmd]
    nx, ny = x + dx, y + dy
    if not (0 <= nx < N and 0 <= ny < M):
        continue

    if cmd == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif cmd == 2:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif cmd == 3:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    else:  # cmd == 4
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

    if graph[nx][ny]:
        dice[5] = graph[nx][ny]
        graph[nx][ny] = 0
    else:
        graph[nx][ny] = dice[5]

    print(dice[0])
    x, y = nx, ny
