import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
indegree = [0] * (N+1)
outdegree = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    indegree[B] += 1
    outdegree[A].append(B)

queue = deque([])
for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)

answer = []
while queue:
    xp = queue.popleft()
    answer.append(xp)
    for nxt in outdegree[xp]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            queue.append(nxt)

print(*answer)
