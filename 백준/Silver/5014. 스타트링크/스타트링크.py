import sys
from collections import deque
input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())

visited = [-1] * (f+1)


def bfs(f, s, g, u, d, visited):
    queue = deque([s])
    visited[s] = 0
    while queue:
        sp = queue.popleft()
        if sp == g:
            return visited[sp]
        for c in [sp + u, sp - d]:
            if not (1 <= c <= f):
                continue
            if visited[c] == -1:
                queue.append(c)
                visited[c] = visited[sp] + 1
    return "use the stairs"


print(bfs(f, s, g, u, d, visited))
