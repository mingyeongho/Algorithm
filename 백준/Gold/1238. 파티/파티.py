import sys
import heapq
input = sys.stdin.readline

N, M, X = map(int, input().split())


def dijkstra(graph, start, N):
    dist = [float("Inf")] * (N+1)
    dist[start] = 0
    hq = [(0, start)]

    while hq:
        cost, node = heapq.heappop(hq)
        if cost > dist[node]:
            continue
        for c, n in graph[node]:
            new_c = cost + c
            if new_c < dist[n]:
                dist[n] = new_c
                heapq.heappush(hq, (new_c, n))
    return dist


graph = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s].append((c, e))

dist = dijkstra(graph, X, N)

answer = 0
for i in range(1, N+1):
    if i == X:
        continue
    d = dijkstra(graph, i, N)
    answer = max(answer, d[X] + dist[i])

print(answer)
