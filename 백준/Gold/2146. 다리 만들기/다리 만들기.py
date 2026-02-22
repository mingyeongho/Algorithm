import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
graph = [list(map(int, input().split())) for _ in range(N)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def labeling(N, graph):
    label = 1
    labels = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1 and labels[i][j] == 0:
                deq = deque([(i, j)])
                labels[i][j] = label

                while deq:
                    xp, yp = deq.popleft()
                    for dx, dy in direction:
                        nx, ny = xp + dx, yp + dy
                        if not (0 <= nx < N and 0 <= ny < N):
                            continue
                        if graph[nx][ny] == 1 and labels[nx][ny] == 0:
                            deq.append((nx, ny))
                            labels[nx][ny] = label
                label += 1
    return labels


def solution(N, graph):
    labels = labeling(N, graph)

    dist = [[-1] * N for _ in range(N)]
    q = deque()
    for i in range(N):
        for j in range(N):
            if labels[i][j] != 0:
                q.append((i, j))
                dist[i][j] = 0

    answer = float("Inf")
    while q:
        xp, yp = q.popleft()
        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            # 라벨링이 안되어있는 바다
            if labels[nx][ny] == 0 and dist[nx][ny] == -1:
                labels[nx][ny] = labels[xp][yp]
                dist[nx][ny] = dist[xp][yp] + 1
                q.append((nx, ny))
            elif labels[nx][ny] != labels[xp][yp] and labels[nx][ny] != 0:
                answer = min(answer, dist[nx][ny] + dist[xp][yp])
    return answer


print(solution(N, graph))
