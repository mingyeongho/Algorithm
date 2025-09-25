import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    A, B = map(int, input().split())
    tree[A].append(B)
    tree[B].append(A)


parents = [0, 1] + [-1] * (N-1)


def bfs(node):
    queue = deque([node])
    while queue:
        xp = queue.popleft()
        for nx in tree[xp]:
            if parents[xp] == nx:
                continue
            queue.append(nx)
            parents[nx] = xp


bfs(1)

for i in range(2, N+1):
    print(parents[i])
