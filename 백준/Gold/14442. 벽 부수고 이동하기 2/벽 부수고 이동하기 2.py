import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

direction = ((-1, 0), (1, 0), (0, -1), (0, 1))

# visited[x][y]는 해당 칸에서 "부순 벽 개수" 상태를 비트마스크로 표시함
# 비트 b가 켜져 있으면 (x,y)를 벽을 정확히 b개 부순 상태에서 방문한 것
visited = [[0] * M for _ in range(N)]

queue = deque()
queue.append((0, 0, 0))  # (행, 열, 부순 벽 개수)
visited[0][0] = 1 << 0

dist = 1  # (0,0)에서 BFS 단계별 거리

while queue:
    # 이 for문에서 len(queue)만큼만 반복하는 이유:
    # BFS의 레벨(거리) 단위 탐색을 보장하기 위함입니다.
    # 즉, 현재 dist(거리)에서 방문 가능한 모든 노드를 한 번에 처리하고,
    # 그 다음에 dist를 1 증가시켜야 최단 거리가 올바르게 계산됩니다.
    # 만약 while queue: 내부에서 바로 xp, yp, zp = queue.popleft()로 처리하면
    # 거리별로 나뉘지 않고, dist가 잘못 증가하여 최단 거리가 깨질 수 있습니다.
    for _ in range(len(queue)):
        xp, yp, zp = queue.popleft()
        if xp == N - 1 and yp == M - 1:
            print(dist)
            sys.exit(0)

        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < N and 0 <= ny < M):
                continue

            # np는 현재까지 부순 벽 개수를 의미한다.
            # np = zp로 초기화한 뒤, 다음 칸이 벽이라면 벽을 하나 더 부순 상태(zp + 1)로 갱신한다.
            # 이렇게 하면 (nx, ny)에 도착했을 때 "벽을 몇 개 부쉈는지" 상태를 올바르게 기록할 수 있다.
            nz = zp
            if graph[nx][ny] == 1:
                if zp >= K:
                    continue
                nz += 1

            # (nx, ny)를 동일한 벽 부순 개수 상태에서 이미 방문했다면 건너뜀
            mask = 1 << nz
            if visited[nx][ny] & mask:
                continue

            visited[nx][ny] |= mask
            queue.append((nx, ny, nz))

    dist += 1

print(-1)
