import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
lake = [list(input().strip()) for _ in range(R)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

swans = []
water = deque()

for i in range(R):
    for j in range(C):
        if lake[i][j] != "X":
            water.append((i, j))
        if lake[i][j] == "L":
            swans.append((i, j))

visited = [[False] * C for _ in range(R)]

swan_q = deque()
next_swan_q = deque()

swan_q.append(swans[0])
visited[swans[0][0]][swans[0][1]] = True

water_q = water
next_water_q = deque()


def move_swan():
    while swan_q:
        x, y = swan_q.popleft()

        if (x, y) == swans[1]:
            return True

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                visited[nx][ny] = True

                if lake[nx][ny] == "X":
                    next_swan_q.append((nx, ny))
                else:
                    swan_q.append((nx, ny))
    return False


def melt():
    while water_q:
        x, y = water_q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < R and 0 <= ny < C:
                if lake[nx][ny] == "X":
                    lake[nx][ny] = "."
                    next_water_q.append((nx, ny))


answer = 0

while True:
    if move_swan():
        print(answer)
        break

    melt()

    swan_q = next_swan_q
    water_q = next_water_q

    next_swan_q = deque()
    next_water_q = deque()

    answer += 1
