import sys
from collections import deque
input = sys.stdin.readline

"""
안전 영역 크기의 최댓값을 구하는 프로그램

풀이
- 벽을 반드시 3개 세워야 함.
- 빈칸을 전부 확인한 다음 3중 for문을 돌며 해당 칸을 벽으로 막고 BFS를 돌린 후 안정영역을 센다.
"""

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(graph, x, y, visited):  # 현재 그래프의 (x, y) 좌표에서 빈 칸을 이은 BFS
    queue = deque([(x, y)])
    visited[x][y] = True
    area = 1
    isVirus = False
    while queue:
        xp, yp = queue.popleft()
        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < N and 0 <= ny < M):
                continue
            if graph[nx][ny] == 2:
                isVirus = True
            if graph[nx][ny] == 0 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                area += 1
    return area if not isVirus else 0


# 현재 모든 빈 칸 구하기
empty = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            empty.append((i, j))
visited = [False] * len(empty)
answer = 0


def backtrack(start, k):  # N과 M 문제처럼 백트래킹을 사용해서 현재 empty에서 3개를 구한다.
    global answer

    if k == 3:
        v = [[False] * M for _ in range(N)]
        area = 0
        for i in range(N):
            for j in range(M):
                if graph[i][j] == 0 and not v[i][j]:
                    area += bfs(graph, i, j, v)
        answer = max(answer, area)
        return
    for i in range(start, len(empty)):
        if not visited[i]:
            xp, yp = empty[i]
            visited[i] = True
            graph[xp][yp] = 1
            backtrack(i+1, k+1)
            visited[i] = False
            graph[xp][yp] = 0


backtrack(0, 0)
print(answer)
