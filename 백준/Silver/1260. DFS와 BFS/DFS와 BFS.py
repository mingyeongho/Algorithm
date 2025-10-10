import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    S, E = map(int, input().split())
    graph[S].append(E)
    graph[E].append(S)

for i in range(1, N+1):
    graph[i].sort()


def bfs(graph, start, visited) -> list[int]:
    queue = deque([start])
    visited[start] = True
    while queue:
        xp = queue.popleft()
        print(xp, end=' ')
        for nxt in graph[xp]:
            if not visited[nxt]:
                queue.append(nxt)
                visited[nxt] = True


def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    for nxt in graph[start]:
        if not visited[nxt]:
            dfs(graph, nxt, visited)


visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)
dfs(graph, V, visited_dfs)
print()
bfs(graph, V, visited_bfs)
