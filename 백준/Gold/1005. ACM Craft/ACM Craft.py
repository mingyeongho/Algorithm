import sys
from collections import deque
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    indegree = [0] * (N+1)
    outdegree = [[] for _ in range(N+1)]
    for _ in range(K):
        X, Y = map(int, input().split())
        indegree[Y] += 1
        outdegree[X].append(Y)
    W = int(input().strip())

    answer = [0] + D
    queue = deque([])
    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        x = queue.popleft()
        if x == W:
            print(answer[x])
            break
        for nxt in outdegree[x]:
            indegree[nxt] -= 1
            answer[nxt] = max(answer[nxt], answer[x] + D[nxt - 1])
            if indegree[nxt] == 0:
                queue.append(nxt)
