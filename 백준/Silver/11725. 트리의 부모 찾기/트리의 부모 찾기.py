import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

visited = [True, True] + [False] * (N-1)
parents = [0, 1] + [-1] * (N-1)

queue = deque([1])
visited[1] = True
while queue:
    start = queue.popleft()
    for end in graph[start]:
        if not visited[end]:
            parents[end] = start
            visited[end] = True
            queue.append(end)
print(*parents[2:], sep='\n')
