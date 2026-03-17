import sys
from collections import deque

input = sys.stdin.readline


def rotate(board):
    return [list(row) for row in zip(*board[::-1])]


def shift(board):
    new_board = []
    for row in board:
        filtered = [x for x in row if x != "."]
        filtered += ["."] * (12 - len(filtered))
        new_board.append(filtered)
    return new_board


def bfs(graph, x, y, visited):
    visited[x][y] = True
    cnt = 1
    q = deque([(x, y)])
    stk = [(x, y)]

    while q:
        xp, yp = q.popleft()
        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < 6 and 0 <= ny < 12):
                continue
            if graph[x][y] == graph[nx][ny] and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
                stk.append((nx, ny))
                cnt += 1

    if cnt >= 4:
        for i, j in stk:
            graph[i][j] = "."
        return True
    return False


direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
graph = rotate([list(input().strip()) for _ in range(12)])
answer = 1  # 총 연쇄 횟수

while answer:
    flag = False
    visited = [[False] * 12 for _ in range(6)]
    for i in range(6):
        for j in range(12):
            if graph[i][j] != "." and not visited[i][j]:
                is_bomb = bfs(graph, i, j, visited)
                if is_bomb:
                    flag = True
    if flag:
        graph = shift(graph)
        answer += 1
    else:
        break

print(answer - 1)
