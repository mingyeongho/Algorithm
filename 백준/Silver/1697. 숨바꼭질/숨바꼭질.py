import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

visited = [-1] * 100_001


def bfs(visited, n, k):
  queue = deque([n])
  visited[n] = 0

  while queue:
    v = queue.popleft()
    if v == k:
      return visited[v]
    m, p, t = v - 1, v + 1, v * 2

    if m >= 0 and visited[m] == -1:
      visited[m] = visited[v] + 1
      queue.append(m)

    if p <= 100_000 and visited[p] == -1:
      visited[p] = visited[v] + 1
      queue.append(p)

    if t <= 100_000 and visited[t] == -1:
      visited[t] = visited[v] + 1
      queue.append(t)


print(bfs(visited, n, k))
