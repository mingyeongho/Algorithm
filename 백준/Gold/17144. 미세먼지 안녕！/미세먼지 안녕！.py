import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def spread(graph, dust: list[tuple[int, int]]) -> list[int, int]:
    new_graph = [[0] * C for _ in range(R)]
    for x, y in dust:
        origin = graph[x][y]
        v = graph[x][y] // 5
        cnt = 0
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < R and 0 <= ny < C):
                continue
            if graph[nx][ny] >= 0:
                cnt += 1
                new_graph[nx][ny] += v
        new_graph[x][y] += (origin - v * cnt)
    return new_graph


def rotate(graph: list[int, int], machine):
    new_graph = [*graph]
    ux, _ = machine[0]
    dx, _ = machine[1]

    for j in range(1, C-1):
        new_graph[ux][1], new_graph[ux][j +
                                        1] = new_graph[ux][j+1], new_graph[ux][1]
    for i in range(ux-1, -1, -1):
        new_graph[ux][1], new_graph[i][C -
                                       1] = new_graph[i][C-1], new_graph[ux][1]
    for j in range(C-2, -1, -1):
        new_graph[ux][1], new_graph[0][j] = new_graph[0][j], new_graph[ux][1]
    for i in range(1, ux):
        new_graph[ux][1], new_graph[i][0] = new_graph[i][0], new_graph[ux][1]
    new_graph[ux][1] = 0

    for j in range(1, C-1):
        new_graph[dx][1], new_graph[dx][j +
                                        1] = new_graph[dx][j+1], new_graph[dx][1]
    for i in range(dx+1, R):
        new_graph[dx][1], new_graph[i][C -
                                       1] = new_graph[i][C-1], new_graph[dx][1]
    for j in range(C-2, 0, -1):
        new_graph[dx][1], new_graph[R -
                                    1][j] = new_graph[R-1][j], new_graph[dx][1]
    for i in range(R-1, dx, -1):
        new_graph[dx][1], new_graph[i][0] = new_graph[i][0], new_graph[dx][1]
    new_graph[dx][1] = 0

    return new_graph


for _ in range(T):
    dust = []
    machine = []
    for i in range(R):
        for j in range(C):
            if graph[i][j] > 0:
                dust.append((i, j))
            elif graph[i][j] == -1:
                machine.append((i, j))

    graph = spread(graph, dust)

    for x, y in machine:
        graph[x][y] = -1
    graph = rotate(graph, machine)

print(sum(sum(graph[i]) for i in range(R)) + 2)
