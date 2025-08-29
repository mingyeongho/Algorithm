import sys
input = sys.stdin.readline

R, C = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [False] * 26

init_idx = ord(graph[0][0]) - ord("A")
visited[init_idx] = True
answer = 1  # 최대 몇 칸을 움직일 수 있는지.
path = []  # 이동하는 경로


def backtrack(x, y):
    global answer

    path.append(graph[x][y])
    if answer < len(path):
        answer = len(path)

    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < R and 0 <= ny < C):
            continue
        nxt = ord(graph[nx][ny]) - ord("A")
        if not visited[nxt]:
            visited[nxt] = True
            backtrack(nx, ny)
            visited[nxt] = False
    path.pop()


backtrack(0, 0)
print(answer)
