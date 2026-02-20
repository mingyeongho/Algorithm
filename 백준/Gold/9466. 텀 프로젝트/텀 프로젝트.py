import sys
from collections import deque

input = sys.stdin.readline

T = int(input().strip())


def solution(N, graph) -> int:
    in_degree = [0] * (N + 1)
    for i in range(1, N + 1):
        in_degree[graph[i]] += 1

    deq = deque()

    for i in range(1, N + 1):
        if in_degree[i] == 0:
            deq.append(i)

    count = 0

    while deq:
        xp = deq.popleft()
        count += 1

        nxt = graph[xp]
        in_degree[nxt] -= 1

        if in_degree[nxt] == 0:
            deq.append(nxt)

    return count


for _ in range(T):
    N = int(input().strip())
    graph = [0] + list(map(int, input().split()))
    print(solution(N, graph))
