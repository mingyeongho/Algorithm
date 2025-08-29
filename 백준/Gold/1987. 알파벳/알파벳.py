import sys
input = sys.stdin.readline

R, C = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [False] * 26
visited[ord(graph[0][0]) - ord("A")] = True
answer = 1


def backtrack(x, y, cnt):
    global answer

    if answer < cnt:
        answer = cnt

    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < R and 0 <= ny < C):
            continue
        nxt = ord(graph[nx][ny]) - ord("A")
        if not visited[nxt]:
            visited[nxt] = True
            backtrack(nx, ny, cnt + 1)
            visited[nxt] = False


backtrack(0, 0, 1)
print(answer)
